#!/usr/bin/env python3
"""Validate ArabKit country folders, skill metadata, and local Markdown links."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"name", "description", "metadata"}
REQUIRED_METADATA = {"version", "country", "locale", "tags"}
SECTIONS = {"Purpose", "Use this skill when", "Workflow", "Quality checklist"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SHARED = {"slug": "shared", "prefix": "arabic"}
SKIP_DIRS = {".git", ".venv", "node_modules"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def parse_scalar(value: str):
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        return [part.strip().strip("'\"") for part in value[1:-1].split(",") if part.strip()]
    return value.strip("'\"")


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    try:
        raw, body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("unclosed YAML frontmatter") from exc
    data: dict = {}
    section = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        if line.startswith("  ") and section:
            data[section][key] = parse_scalar(value)
        elif not value.strip():
            data[key] = {}
            section = key
        else:
            data[key] = parse_scalar(value)
            section = None
    return data, body


def load_countries() -> tuple[list[dict], list[str]]:
    try:
        data = json.loads((ROOT / "countries.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [], [f"countries.json: {exc}"]
    errors = []
    countries = data.get("countries", [])
    seen: dict[str, set[str]] = {"slug": set(), "prefix": {SHARED["prefix"]}}
    for country in countries:
        for field in ("slug", "iso", "name_en", "name_ar", "prefix"):
            if not country.get(field):
                errors.append(f"countries.json: {country.get('slug', '?')} is missing {field}")
        for field in ("slug", "prefix"):
            value = country.get(field, "")
            if value in seen[field]:
                errors.append(f"countries.json: duplicate {field} {value!r}")
            seen[field].add(value)
            if not NAME_RE.fullmatch(value):
                errors.append(f"countries.json: invalid {field} {value!r}")
    return countries, errors


def validate_skill(path: Path, owner: dict, names: set[str]) -> list[str]:
    errors = []
    try:
        meta, body = parse_frontmatter(path)
    except ValueError as exc:
        return [f"{rel(path)}: {exc}"]
    missing = REQUIRED - meta.keys()
    if missing:
        errors.append(f"{rel(path)}: missing frontmatter: {', '.join(sorted(missing))}")
    name = str(meta.get("name", ""))
    if name != path.parent.name:
        errors.append(f"{rel(path)}: name must match its directory")
    if not NAME_RE.fullmatch(name):
        errors.append(f"{rel(path)}: invalid skill name {name!r}")
    if not name.startswith(owner["prefix"] + "-"):
        errors.append(f"{rel(path)}: skills in {owner['slug']}/ must be named {owner['prefix']}-<topic>")
    if name in names:
        errors.append(f"{rel(path)}: duplicate skill name {name}")
    names.add(name)
    if len(str(meta.get("description", ""))) < 30:
        errors.append(f"{rel(path)}: description is too short")
    extension = meta.get("metadata", {})
    if not isinstance(extension, dict):
        errors.append(f"{rel(path)}: metadata must be an object")
        extension = {}
    missing_extension = REQUIRED_METADATA - extension.keys()
    if missing_extension:
        errors.append(f"{rel(path)}: missing metadata fields: {', '.join(sorted(missing_extension))}")
    if not VERSION_RE.fullmatch(str(extension.get("version", ""))):
        errors.append(f"{rel(path)}: metadata.version must be SemVer")
    if extension.get("country") and extension.get("country") != owner["slug"]:
        errors.append(f"{rel(path)}: metadata.country must be {owner['slug']!r}")
    tags = extension.get("tags", [])
    if not isinstance(tags, list) or len(tags) < 2:
        errors.append(f"{rel(path)}: tags must be an inline list with at least two values")
    headings = set(re.findall(r"^## (.+?)\s*$", body, re.MULTILINE))
    for section in sorted(SECTIONS - headings):
        errors.append(f"{rel(path)}: missing required section '{section}'")
    if any(token in body for token in ("TODO", "TBD", "PLACEHOLDER")):
        errors.append(f"{rel(path)}: unfinished placeholder found")
    return errors


def validate_layout(countries: list[dict]) -> tuple[list[str], int]:
    errors = []
    names: set[str] = set()
    owners = {c["slug"]: c for c in countries if c.get("slug")}
    for slug in owners:
        if not (ROOT / "countries" / slug / "README.md").is_file():
            errors.append(f"countries/{slug}/README.md is missing")
    for folder in sorted((ROOT / "countries").iterdir()):
        if folder.is_dir() and folder.name not in owners:
            errors.append(f"countries/{folder.name}/ is not listed in countries.json")
    count = 0
    for path in sorted(ROOT.rglob("SKILL.md")):
        if SKIP_DIRS & set(path.parts):
            continue
        parts = path.relative_to(ROOT).parts
        if len(parts) == 4 and parts[0] == "shared" and parts[1] == "skills":
            owner = SHARED
        elif len(parts) == 5 and parts[0] == "countries" and parts[2] == "skills" and parts[1] in owners:
            owner = owners[parts[1]]
        else:
            errors.append(f"{rel(path)}: skills must live in countries/<country>/skills/<name>/ or shared/skills/<name>/")
            continue
        errors.extend(validate_skill(path, owner, names))
        count += 1
    return errors, count


def validate_links() -> list[str]:
    errors = []
    for path in ROOT.rglob("*.md"):
        if SKIP_DIRS & set(path.parts):
            continue
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            clean = target.split("#", 1)[0]
            if not clean or clean.startswith(("http://", "https://", "mailto:")):
                continue
            if not (path.parent / clean).resolve().exists():
                errors.append(f"{rel(path)}: broken link: {target}")
    return errors


def main() -> int:
    countries, errors = load_countries()
    layout_errors, count = validate_layout(countries)
    errors += layout_errors + validate_links()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validation passed: {len(countries)} countries, {count} skills, links valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
