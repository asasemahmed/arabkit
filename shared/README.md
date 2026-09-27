# Shared Arabic skills · مهارات عربية مشتركة

Skills here apply to Arabic products in **any** country: Arabic typography and UI, RTL and bidirectional text, Arabic search, and general Arabic writing quality.

| | |
|---|---|
| Skill name prefix | `arabic-` |
| Status | No skills yet. Looking for contributors. |

## What belongs here

A skill belongs in `shared/` only if its guidance holds in every Arab country. If a rule depends on a dialect, a currency, a phone format, a payment method, or a local law, it belongs in that country's folder instead.

Good candidates:

- `arabic-ui`: Arabic fonts, type scale, layout, and component states.
- `arabic-rtl`: logical CSS, bidi isolation, icon mirroring, and RTL testing.
- `arabic-search`: normalization, diacritics, and letter-form folding for search.
- `arabic-msa-copy`: clear, modern Standard Arabic for products that serve several countries.

MasrKit's [`arabic-ui`](https://github.com/asasemahmed/MasrKit/tree/main/skills/arabic-ui) and [`arabic-rtl`](https://github.com/asasemahmed/MasrKit/tree/main/skills/arabic-rtl) skills are a good starting point for the first two.

## Layout

```text
shared/
├── README.md
└── skills/
    └── arabic-<topic>/
        ├── SKILL.md
        └── references/
```

Read [CONTRIBUTING.md](../CONTRIBUTING.md) before adding a skill.
