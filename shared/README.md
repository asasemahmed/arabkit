# Shared Arabic skills · مهارات عربية مشتركة

Skills here apply to Arabic products in **any** country: Arabic typography and UI, RTL and bidirectional text, Arabic search, and general Arabic writing quality.

| | |
|---|---|
| Skill name prefix | `arabic-` |
| Status | 4 skills. More welcome. |

## Skills

| Skill | What it does |
|---|---|
| [`arabic-ui`](skills/arabic-ui/SKILL.md) | Arabic typography, layout, components, states, and accessibility. |
| [`arabic-rtl`](skills/arabic-rtl/SKILL.md) | Logical CSS, bidi isolation, icon mirroring, and RTL testing. |
| [`arabic-copy`](skills/arabic-copy/SKILL.md) | Contemporary Modern Standard Arabic copy for products that serve several countries. |
| [`arabic-search`](skills/arabic-search/SKILL.md) | Normalization, analyzers, synonyms, and relevance testing for Arabic search. |

## What belongs here

A skill belongs in `shared/` only if its guidance holds in every Arab country. If a rule depends on a dialect, a currency, a phone format, a payment method, or a local law, it belongs in that country's folder instead.

Ideas for the next shared skills:

- `arabic-a11y`: screen readers, language tagging, and accessible Arabic forms.
- `arabic-dates`: Hijri and Gregorian calendars, regional month names, and date input.
- `arabic-dataviz`: charts, axes, and numbers in RTL dashboards.

`arabic-ui` and `arabic-rtl` are adapted from [MasrKit](https://github.com/asasemahmed/MasrKit).

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
