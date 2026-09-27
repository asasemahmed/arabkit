#!/usr/bin/env python3
"""Regenerate the country tables and skill counts in README.md and README.ar.md.

Run after adding a skill or changing countries.json:

    python scripts/build_readme.py

`python scripts/validate.py` fails when the READMEs are out of date.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START, END = "<!-- countries:start -->", "<!-- countries:end -->"

REGIONS = [
    ("Arabian Peninsula", "شبه الجزيرة العربية"),
    ("Levant and Iraq", "الشام والعراق"),
    ("Nile Valley", "وادي النيل"),
    ("Maghreb", "المغرب العربي"),
    ("Horn of Africa and Indian Ocean", "القرن الأفريقي والمحيط الهندي"),
]


def skills_in(folder: Path) -> list[str]:
    return sorted(p.parent.name for p in folder.glob("skills/*/SKILL.md"))


def status(skills: list[str], folder: str, arabic: bool) -> str:
    if not skills:
        return "مفتوح للمساهمة" if arabic else "Open for contributors"
    return " ".join(f"[`{name}`]({folder}/skills/{name}/SKILL.md)" for name in skills)


def tables(countries: list[dict], arabic: bool) -> str:
    out = []
    for region_en, region_ar in REGIONS:
        members = [c for c in countries if c["region"] == region_en]
        if not members:
            continue
        out.append(f"### {region_ar if arabic else region_en}\n")
        if arabic:
            out.append("| | الدولة | Country | البادئة | المهارات |\n|---|---|---|---|---|")
        else:
            out.append("| | Country | الدولة | Prefix | Skills |\n|---|---|---|---|---|")
        for c in members:
            folder = f"countries/{c['slug']}"
            skills = skills_in(ROOT / folder)
            first, second = (c["name_ar"], c["name_en"]) if arabic else (c["name_en"], c["name_ar"])
            out.append(
                f"| {c['flag']} | [{first}]({folder}/README.md) | {second} | `{c['prefix']}-` | {status(skills, folder, arabic)} |"
            )
        out.append("")
    shared = skills_in(ROOT / "shared")
    label = "كل الدول (shared)" if arabic else "All countries (shared)"
    out.append(f"### {label}\n")
    if arabic:
        out.append("| | المجلد | البادئة | المهارات |\n|---|---|---|---|")
        out.append(f"| 🌍 | [`shared/`](shared/README.md) | `arabic-` | {status(shared, 'shared', True)} |")
    else:
        out.append("| | Folder | Prefix | Skills |\n|---|---|---|---|")
        out.append(f"| 🌍 | [`shared/`](shared/README.md) | `arabic-` | {status(shared, 'shared', False)} |")
    return "\n".join(out).rstrip() + "\n"


def render(text: str, countries: list[dict], arabic: bool) -> str:
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        raise ValueError("country table markers not found")
    block = f"{START}\n\n{tables(countries, arabic)}\n{END}"
    text = pattern.sub(lambda _: block, text, count=1)
    total = sum(len(skills_in(p)) for p in (ROOT / "countries").iterdir() if p.is_dir()) + len(skills_in(ROOT / "shared"))
    return re.sub(r"(img\.shields\.io/badge/skills-)\d+(-)", rf"\g<1>{total}\g<2>", text)


def targets() -> dict[Path, str]:
    countries = json.loads((ROOT / "countries.json").read_text(encoding="utf-8"))["countries"]
    result = {}
    for name, arabic in (("README.md", False), ("README.ar.md", True)):
        path = ROOT / name
        result[path] = render(path.read_text(encoding="utf-8"), countries, arabic)
    return result


def stale() -> list[str]:
    """README files whose generated sections are out of date."""
    try:
        return [path.name for path, text in targets().items() if path.read_text(encoding="utf-8") != text]
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        return [f"README generation failed: {exc}"]


def main() -> int:
    for path, text in targets().items():
        path.write_bytes(text.encode("utf-8"))
        print(f"updated {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
