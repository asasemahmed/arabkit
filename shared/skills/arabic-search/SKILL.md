---
name: arabic-search
description: Build Arabic search that finds what users mean. Use when implementing or tuning search, autocomplete, filtering, or deduplication over Arabic text in Elasticsearch, OpenSearch, PostgreSQL, SQLite, Meilisearch, Typesense, or application code, including folding hamza and alef forms, ta marbuta, and alef maqsura, stripping diacritics and tatweel, converting Arabic-Indic digits, handling mixed Arabic and English queries, regional word variants, and Arabizi (Franco) spellings. Not for the layout of search screens (use arabic-ui).
metadata:
  version: 1.0.0
  country: shared
  locale: ar
  tags: [arabic, search, normalization, backend]
---

# Arabic Search

## Purpose

Arabic users type the same word many ways: with or without hamza, `ة` or `ه` at the end, `ى` or `ي`, with diacritics or tatweel, in Arabic-Indic or Western digits, on a Persian keyboard, or in Latin letters. A search that matches raw strings misses most of them. This skill builds a normalized search key, picks analyzers per field, and measures relevance with real queries.

## Use this skill when

Use it for product, content, people, and place search; autocomplete; duplicate detection; and any matching over Arabic text. It applies in every Arab country. Pair it with the country's backend or product-ux skill for local data such as names, addresses, and product vocabulary.

## Workflow

1. Collect real queries and documents: product names, people and place names, misspellings, mixed Arabic and English, and Arabizi. Do not tune on dictionary words.
2. Classify every field: free text, names, brands and product titles, identifiers, and exact-match fields.
3. Define one versioned normalization function and apply it identically at index time and query time.
4. Choose tokenization and stemming per field class.
5. Add recall helpers: synonyms, transliteration aliases, and typo tolerance.
6. Build a relevance test set and measure every change against it.
7. When the normalizer version changes, rebuild the index.

## Normalize a search key, never the source

Store the user's text exactly as written and index a separate search key. Folds that help search would corrupt display text.

| Step | What | Example | Default |
|---|---|---|---|
| Unicode NFKC | Presentation forms and ligatures to base letters | `ﻻ` → `لا` | On |
| Diacritics | Remove harakat, shadda, sukun, superscript alef, Quranic marks | `مُحَمَّد` → `محمد` | On |
| Tatweel and invisible marks | Remove `ـ`, zero-width characters, and bidi controls | `العربيـــة` → `العربية` | On |
| Alef forms | `أ إ آ ٱ` → `ا` | `أحمد` → `احمد` | On |
| Ta marbuta | `ة` → `ه` | `مدرسة` → `مدرسه` | On |
| Alef maqsura | `ى` → `ي` | `مصطفى` → `مصطفي` | On |
| Persian and Urdu lookalikes | `ی` → `ي`, `ک` → `ك` | `کتاب` → `كتاب` | On |
| Hamza carriers | `ؤ` → `و`, `ئ` → `ي` | `مسؤول` → `مسوول` | On for broad search |
| Digits | Arabic-Indic and Extended Arabic-Indic to ASCII | `١٥` → `15` | On |
| Latin case | Case-fold the Latin part | `iPhone` → `iphone` | On |

Some folds merge different words, for example `على` (on) and `علي` (Ali). That is acceptable in broad search and wrong for exact matching, which is why fields are classified first.

Tested Python and JavaScript implementations are in [references/normalizer.md](references/normalizer.md).

## Choose analysis per field

| Field class | Normalize | Stem | Typo tolerance | Notes |
|---|---|---|---|---|
| Free text (descriptions, articles) | Yes | Light stemming | Yes | Removing `ال`, `و`, and common suffixes improves recall |
| Names of people and places | Yes | No | Small | Stemming breaks names; add known spelling variants as aliases |
| Brands and product titles | Yes | No | Yes | Add Arabic and English aliases (`ايفون` ↔ `iphone`) |
| Identifiers, codes, emails | Digits only | No | No | Exact match after digit conversion |
| Passwords, legal identity matching | No | No | No | Never fold; compare exactly |

- Keep an unstemmed subfield next to a stemmed one, and boost exact and prefix matches on the unstemmed field.
- Light stemming beats aggressive root extraction for product search. Roots merge unrelated words (`كتب`, `مكتب`, `كاتب`).

## Engine notes

- **Elasticsearch and OpenSearch:** the built-in `arabic` analyzer combines `arabic_normalization` (alef, ta marbuta, alef maqsura, diacritics, tatweel) and the light `arabic_stem` filter. For more control, build a custom analyzer with `lowercase`, `decimal_digit` (Arabic-Indic digits to ASCII), `arabic_normalization`, `persian_normalization` if users type on Persian keyboards, and `arabic_stem` only on free-text fields. Check which folds `arabic_normalization` does not cover (for example hamza carriers) and add a `mapping` character filter if you need them.
- **PostgreSQL:** compute the search key in the application with the normalizer and store it in its own column. Index that column with `pg_trgm` for fuzzy and prefix matching. Check `\dF` for an `arabic` text search configuration on your version before relying on built-in stemming.
- **SQLite FTS5, Meilisearch, Typesense, and others:** check exactly which Arabic folds the tokenizer performs. If you are not sure, index the pre-normalized key and normalize queries with the same function.
- **Autocomplete:** normalize before building prefixes, so `أحم` and `احم` complete the same way.

## Mixed language, regional words, and Arabizi

- **Mixed queries are normal.** Users search `ايفون 15`, `iphone ١٥`, and `آيفون١٥`. Normalize digits, split letter and digit runs, and keep an alias table for top brands and products.
- **Regional vocabulary differs.** Potatoes are `بطاطس` in Egypt and `بطاطا` in the Levant and Gulf; tomatoes are `طماطم` in many markets and `بندورة` in the Levant. Maintain a synonym list per market from your real query logs.
- **Arabizi (Franco).** Many users type Arabic in Latin letters with digits for missing sounds: `3` for `ع`, `7` for `ح`, `5` for `خ`, and `2` for hamza are common, while `9`, `8`, and `6` vary by region. Generic transliteration is noisy; add Arabizi aliases for your top entities and route short Latin queries through both indexes.
- **Dialect spellings.** Colloquial product names and common misspellings belong in the synonym list, not in the normalizer.

## Measure relevance

- Keep a test set of at least 50 real queries with the documents that should rank first, covering each fold, mixed queries, regional words, and Arabizi.
- Track recall at the top results and the zero-result rate for each normalizer version and analyzer change.
- Log zero-result queries in production (without personal data) and review them regularly; they are the best source of new synonyms.

## Anti-patterns

- Normalizing the stored display text instead of a separate search key.
- Different normalization at index time and query time.
- Aggressive root stemming on names, brands, or product titles.
- Folding identifiers, passwords, emails, or legal names used for identity checks.
- Tuning on dictionary words instead of real queries.
- Changing the normalizer without a version number and an index rebuild.

## Quality checklist

- [ ] Original text is stored untouched; a versioned search key is indexed separately.
- [ ] The same normalizer runs at index and query time.
- [ ] Every field is classified, and names, brands, and identifiers are not stemmed.
- [ ] Arabic-Indic digits, Persian lookalike letters, and invisible marks are handled.
- [ ] Mixed Arabic and English queries and top Arabizi spellings return results.
- [ ] Regional synonyms come from real query logs for each target market.
- [ ] A relevance test set exists and is run on every change.
