# Contributing to ArabKit

ArabKit grows one country at a time, and the people who know a country best are the ones who should write its skills. Thank you for helping.

## Start here

- The pinned [roadmap](https://github.com/asasemahmed/arabkit/issues/16) lists every country, what exists, and what is open.
- [Good first issues](https://github.com/asasemahmed/arabkit/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) are small tasks that do not need a whole skill: reviews, data checks, and translations.
- Questions and ideas go in [Discussions](https://github.com/asasemahmed/arabkit/discussions). Say hello in the [introductions thread](https://github.com/asasemahmed/arabkit/discussions/17).
- Before starting a skill, comment on its issue (or open one) so two people do not write the same thing.

## Where things go

```text
countries/<country>/skills/<prefix>-<topic>/SKILL.md   # guidance for one country
shared/skills/arabic-<topic>/SKILL.md                  # guidance true for every Arab country
```

- Each country's folder name and skill prefix are listed in [`countries.json`](countries.json) and in the country's README. For example, Saudi skills live in `countries/saudi-arabia/skills/` and are named `saudi-<topic>`.
- Skill names must be unique across the whole repository, because agents install them into one flat folder. The prefix guarantees this.
- If a rule depends on a dialect, currency, phone format, payment method, or law, it belongs in a country folder, not in `shared/`.
- Never add a top-level `skills/` folder or a `SKILL.md` anywhere else. The skills CLI stops looking in country folders when it finds one, and the validator rejects it.

## Add a skill

1. Copy [`templates/SKILL.template.md`](templates/SKILL.template.md) to `countries/<country>/skills/<prefix>-<topic>/SKILL.md`.
2. Fill in the frontmatter. `name` must match the folder name. `metadata.country` must match the country folder (or `shared`).
3. Keep the four required sections: `Purpose`, `Use this skill when`, `Workflow`, and `Quality checklist`.
4. Put long tables and datasets (governorates or regions, terminology, provider lists) in a `references/` folder next to `SKILL.md`.
5. Add your skill to the **Skills** list in the country README and change its status line.
6. Update the country tables in both main READMEs, then run the validator:

   ```bash
   python scripts/build_readme.py
   python scripts/validate.py
   ```

   The validator fails if the README tables are out of date.

7. Open a pull request. Say which real agent mistake the skill prevents.

## What makes a good skill

- **Specific to the place.** Generic engineering advice ("store money as integers") is only useful when paired with the local detail an agent would not know (the currency's minor units, local payment timing).
- **Clear about what changes.** Mark facts that change over time, such as providers, fees, laws, and number ranges, and give a "last reviewed" date.
- **Written for how people talk.** Say when the local dialect fits and when Modern Standard Arabic is better. Avoid caricature, forced slang, and stereotypes about any group.
- **A description that triggers.** Say *when* to load the skill, using words users type, and name the neighboring skill to use instead.
- **Honest.** Never invent customer numbers, regulations, provider features, or partnerships.

## Become a country maintainer

Each country folder can have one or more maintainers who review pull requests for that country. Open a [country maintainer issue](https://github.com/asasemahmed/arabkit/issues/new?template=country-maintainer.yml) to volunteer. Maintainers are listed in the country README.

## Add a country or fix country data

The 22 member states of the Arab League each have a folder. To correct a calling code, currency, name, or prefix, edit `countries.json` and the country README in the same pull request.

## Code of conduct

Everyone taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md).
