<div align="center">

# ArabKit

### Agent skills for building products that feel local in every Arab country.

[Countries](#countries) · [How it works](#how-it-works) · [Contribute](CONTRIBUTING.md) · [اقرأ بالعربي](README.ar.md)

</div>

---

Arabic is one language with many markets. A checkout that feels natural in Cairo can feel foreign in Riyadh or Casablanca: the dialect changes, and so do phone formats, addresses, currencies, payment methods, and what people trust.

ArabKit is an open-source library of AI agent skills organized **by country**. Each Arab country has its own folder, maintained by people who live there and build for it. Skills that hold everywhere live in `shared/`.

> **Status:** the structure is ready and every country folder is open. There are no skills yet. The first contributors for each country shape how it is done. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Countries

| Country | الدولة | Skill prefix | Skills |
|---|---|---|---|
| 🇩🇿 [Algeria](countries/algeria/README.md) | الجزائر | `algeria-` | 0 |
| 🇧🇭 [Bahrain](countries/bahrain/README.md) | البحرين | `bahrain-` | 0 |
| 🇰🇲 [Comoros](countries/comoros/README.md) | جزر القمر | `comoros-` | 0 |
| 🇩🇯 [Djibouti](countries/djibouti/README.md) | جيبوتي | `djibouti-` | 0 |
| 🇪🇬 [Egypt](countries/egypt/README.md) | مصر | `egypt-` | 0 |
| 🇮🇶 [Iraq](countries/iraq/README.md) | العراق | `iraq-` | 0 |
| 🇯🇴 [Jordan](countries/jordan/README.md) | الأردن | `jordan-` | 0 |
| 🇰🇼 [Kuwait](countries/kuwait/README.md) | الكويت | `kuwait-` | 0 |
| 🇱🇧 [Lebanon](countries/lebanon/README.md) | لبنان | `lebanon-` | 0 |
| 🇱🇾 [Libya](countries/libya/README.md) | ليبيا | `libya-` | 0 |
| 🇲🇷 [Mauritania](countries/mauritania/README.md) | موريتانيا | `mauritania-` | 0 |
| 🇲🇦 [Morocco](countries/morocco/README.md) | المغرب | `morocco-` | 0 |
| 🇴🇲 [Oman](countries/oman/README.md) | عُمان | `oman-` | 0 |
| 🇵🇸 [Palestine](countries/palestine/README.md) | فلسطين | `palestine-` | 0 |
| 🇶🇦 [Qatar](countries/qatar/README.md) | قطر | `qatar-` | 0 |
| 🇸🇦 [Saudi Arabia](countries/saudi-arabia/README.md) | السعودية | `saudi-` | 0 |
| 🇸🇴 [Somalia](countries/somalia/README.md) | الصومال | `somalia-` | 0 |
| 🇸🇩 [Sudan](countries/sudan/README.md) | السودان | `sudan-` | 0 |
| 🇸🇾 [Syria](countries/syria/README.md) | سوريا | `syria-` | 0 |
| 🇹🇳 [Tunisia](countries/tunisia/README.md) | تونس | `tunisia-` | 0 |
| 🇦🇪 [United Arab Emirates](countries/uae/README.md) | الإمارات | `uae-` | 0 |
| 🇾🇪 [Yemen](countries/yemen/README.md) | اليمن | `yemen-` | 0 |

Arabic-wide skills for every country go in [`shared/`](shared/README.md), with the prefix `arabic-`.

## How it works

```text
arabkit/
├── countries/
│   ├── egypt/
│   │   ├── README.md
│   │   └── skills/
│   │       └── egypt-copy/
│   │           ├── SKILL.md
│   │           └── references/
│   ├── saudi-arabia/
│   └── ... (22 countries)
├── shared/            # skills true for every Arab country (arabic-*)
├── templates/         # starting point for a new SKILL.md
├── countries.json     # folder names, prefixes, and basic country data
└── scripts/validate.py
```

- A skill is a folder with a `SKILL.md` file: YAML frontmatter that tells the agent when to use it, followed by plain Markdown guidance. It works with Claude Code, Codex, Cursor, Gemini CLI, and other agents that load skills.
- Every skill name starts with its country's prefix, such as `saudi-copy` or `morocco-product-ux`, so skills from different countries never collide when installed together.
- `python scripts/validate.py` checks folder layout, naming, required sections, and links. It runs on every pull request.

## Install skills

Once skills are added, you will be able to install them with the [skills CLI](https://www.skills.sh):

```bash
npx skills add asasemahmed/arabkit --skill <skill-name>
```

## Contribute

The best way to help is to take your own country:

1. Pick your country's folder under [`countries/`](countries).
2. Start from [`templates/SKILL.template.md`](templates/SKILL.template.md). A copy or product-UX skill is a good first one.
3. Run `python scripts/validate.py` and open a pull request.

You can also [volunteer as a country maintainer](https://github.com/asasemahmed/arabkit/issues/new?template=country-maintainer.yml). Read [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

## Related

[MasrKit](https://github.com/asasemahmed/MasrKit) is a complete set of Egyptian skills. It is the model for the structure and depth ArabKit aims for in every country.

## License

[MIT](LICENSE)
