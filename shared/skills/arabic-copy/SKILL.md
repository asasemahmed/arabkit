---
name: arabic-copy
description: Write clear, contemporary Modern Standard Arabic (فصحى معاصرة) product copy for apps and websites that serve several Arab countries or need a neutral voice. Use when writing or translating UI strings, errors, onboarding, notifications, and marketing into Arabic without one country's dialect, deciding which markets need their own dialect copy, addressing users by gender and number, or fixing stiff, bureaucratic, or machine-translated Arabic. For one country's local voice, use that country's copy skill (for example egypt-copy).
metadata:
  version: 1.0.0
  country: shared
  locale: ar
  tags: [arabic, msa, copywriting, localization]
---

# Arabic Product Copy (Modern Standard Arabic)

## Purpose

Most products that serve several Arab countries write in Modern Standard Arabic, and most of that Arabic reads like a legal notice or a machine translation. This skill produces MSA that is clear, contemporary, and warm enough for product UI, and that reads naturally from Casablanca to Muscat. It also decides when a market deserves copy in its own dialect.

## Use this skill when

Use it for pan-Arab SaaS, marketplaces, fintech, government and education services, and any product whose Arabic must work in more than one country. Pair it with `arabic-ui` for layout and `arabic-rtl` for mixed-direction text. When one market needs a local voice, hand that market to its country copy skill, such as `egypt-copy`.

## Workflow

1. Identify the target markets, audience, domain, risk, and channel.
2. Choose a language strategy (below) and record it in one sentence, for example: "MSA for all markets, dialect only in Egyptian and Saudi marketing."
3. Choose a form of address and one button pattern for the whole product.
4. Build a terminology list for repeated actions, entities, and statuses before writing screens.
5. Write from the user's intent and the consequence of the action. Do not keep English word order.
6. Read the copy aloud and remove bureaucratic, ornate, or translated phrasing.
7. When copy is shared across markets, have native readers from at least two target countries review it.

## Choose a language strategy

| Strategy | Fits | Watch out for |
|---|---|---|
| One MSA voice everywhere | Pan-Arab SaaS, finance, government, education, B2B | Sounding cold; fix with plain words and short sentences, not dialect |
| MSA base plus dialect on selected surfaces | Consumer products with one or two main markets: marketing, onboarding, push notifications | Keep transactional, legal, and security copy in MSA |
| Fully local copy per market | Consumer brands with a strong local presence in each country | Cost; every market needs its own copy owner |

- Do not pick Egyptian or Levantine dialect for a multi-country product because "everyone understands it." Understanding a dialect is not the same as feeling addressed, and many Maghrebi and Gulf users will read it as foreign.
- Never mix two dialects, or dialect and MSA, inside one flow.

## Write contemporary MSA

- **Prefer verbs to noun chains.** `احفظ التغييرات`, not `القيام بعملية حفظ التغييرات`.
- **Drop bureaucratic openers.** Remove `يرجى العلم بأن`, `نود إعلامكم`, and `عزيزي العميل` unless the context is a formal letter.
- **Name the object.** `تم حفظ التغييرات` says more than `تمت العملية بنجاح`. Do not start every status line with `تم`; the system can speak in first-person plural: `أرسلنا رمز التحقق إلى…`.
- **Use familiar words.** `ابدأ` over `استهلّ`, `اختر` over `قم بانتقاء`.
- **Avoid calques from English.** `لا تتردد في التواصل معنا` (don't hesitate to contact us) and `انقر هنا` (click here) are translations, not Arabic. Name the destination or the action instead.
- **Spell carefully.** Hamza placement (`إنشاء`, not `انشاء`), `ة` versus `ه`, and `ى` versus `ي` matter more in MSA than in dialect: errors here make a product look careless.
- **Use Arabic punctuation.** `،` `؛` `؟` inside Arabic sentences. A Latin comma or question mark in Arabic text looks broken.
- **Add diacritics only to prevent misreading,** for example a shadda that distinguishes two words. Full vocalization makes UI text heavy.

## Address the user

MSA second-person forms carry gender and number: `اكتب` / `اكتبي` / `اكتبوا`. Decide one policy for the whole product:

1. **Generic masculine singular (default).** The common convention in Arabic interfaces, and read as neutral in short commands. Use it when there is no stored preference.
2. **Neutral constructions.** Verbal nouns on buttons (`حفظ`, `إرسال`, `متابعة`), statements about the object (`تم حذف الملف`), and first-person plural for the system (`أرسلنا`). Use them where they read naturally.
3. **Plural (`اكتبوا`).** Some brands use it in marketing to sound inclusive. It reads collective and formal, so do not use it for personal account actions.
4. **User-chosen form.** If the product lets users choose how to be addressed, use that choice in personalized messages and keep shared UI generic.

- Never infer gender from a name, photo, or ID.
- Avoid slash forms like `اكتب/ي` in product UI.
- **Pick one button pattern.** Either imperative (`احفظ`, `أرسل`) or verbal noun (`حفظ`, `إرسال`). Mixing both on one screen looks unfinished.

## Common UI terms

Neutral terms that work across markets. Some everyday words differ by region; the notes show where a local term may fit better in a single-country product.

| Concept | Recommended | Avoid | Notes |
|---|---|---|---|
| Sign in / Sign out | تسجيل الدخول / تسجيل الخروج | الولوج (outside the Maghreb) | |
| Create account | إنشاء حساب | تسجيل عضوية جديدة | |
| Password | كلمة المرور | الرقم السري | `كلمة السر` is fine in casual products |
| Verification code | رمز التحقق | كود التفعيل الخاص بك | |
| Mobile number | رقم الهاتف المحمول / رقم الجوال | | `جوال` is common in the Gulf and Levant, `موبايل` in Egypt, `الهاتف النقال` in the Maghreb |
| Settings | الإعدادات | الضبط | |
| Notifications | الإشعارات | | `التنبيهات` is also common |
| Download / Upload | تنزيل / رفع | تحميل for upload | `تحميل` means download in many markets and upload in others, so avoid it for upload |
| Cart / Checkout | السلة / إتمام الشراء | الخروج | `الخروج` is a literal translation of "check out" |
| Delete / Cancel | حذف / إلغاء | إزالة نهائية | Keep `إلغاء` for dismissing, `حذف` for data |
| Search / Filter / Sort | بحث / تصفية / ترتيب | فلترة | |
| Dashboard | لوحة التحكم | الداشبورد | |
| Free trial | تجربة مجانية | فترة تجريبية مجانًا | |
| Next / Back | التالي / السابق | | Flip the arrow icons in RTL |

## States and messages

| Situation | Machine-shaped | Contemporary MSA |
|---|---|---|
| Required field | `هذا الحقل مطلوب` | `اكتب رقم الهاتف` (name the field) |
| Network error | `حدث خطأ ما، يرجى المحاولة لاحقًا` | `تعذّر الاتصال. تحقّق من الإنترنت ثم حاول مرة أخرى.` |
| Save failed | `فشلت العملية` | `تعذّر حفظ التغييرات. ما كتبته ما زال هنا، حاول مرة أخرى.` |
| Empty list | `لا توجد بيانات` | `لا توجد طلبات بعد. ستظهر طلباتك هنا.` |
| Pending payment | `تمت عملية الدفع بنجاح` | `الدفع قيد التأكيد. سنحدّث حالة الطلب فور وصول النتيجة.` |
| Delete confirmation | `هل أنت متأكد؟` | `حذف الملف؟ لا يمكن التراجع عن ذلك.` with buttons `حذف` and `إلغاء` |
| Welcome | `مرحبًا بك في منصتنا الرائدة` | `مرحبًا بك. لنبدأ بإعداد حسابك.` |
| Call to action | `انقر هنا` | `ابدأ التجربة المجانية` |

- Errors say what failed, what is safe, and what to do next.
- Never show success for an operation that is still pending.
- Confirmation dialogs name the object and the consequence; button labels repeat the action (`حذف`), not `نعم`.

## Numbers, dates, and currency across markets

- **Digits.** Western digits (0-9) are the norm in the Maghreb and common in apps everywhere; Arabic-Indic digits (٠-٩) appear more in formal and print contexts in the Mashriq. Choose per product and market, and keep one system per screen.
- **Formatter defaults differ by locale.** `Intl` formats `ar-EG`, `ar-SA`, and the Levant locales with Arabic-Indic digits (`١٬٢٣٤٫٥`), `ar-AE` with Western digits (`1,234.5`), and the Maghreb locales with Western digits and swapped separators (`1.234,5`). Add `-u-nu-latn` (for example `ar-SA-u-nu-latn`) to force Western digits.
- **Month names differ by region.** Egypt, the Gulf, Morocco, and Libya use `يناير، فبراير…`; the Levant and Iraq use `كانون الثاني، شباط…`; Algeria and Tunisia use `جانفي، فيفري…`. Locale-aware formatters follow these conventions, so the locale you pass decides the month names. For one shared locale, prefer numeric dates or localize per market.
- **Currency names are ambiguous.** `ريال`, `دينار`, and `جنيه` each name several currencies. Always show the country's own currency code or symbol.
- **Mixed-direction values.** Phone numbers, emails, codes, and amounts inside Arabic sentences need isolation; follow `arabic-rtl`.

## Anti-patterns

- Translating English copy sentence by sentence.
- Ornate or legalistic MSA in everyday UI (`يسرّنا أن نحيطكم علمًا`).
- One market's dialect used as the "neutral" voice for all markets.
- `تم` at the start of every message, and `تمت العملية بنجاح` for everything.
- Transliterated English where a clear Arabic term exists (`الداشبورد`, `فلترة`), or forced Arabic where the English product term is what users recognize.
- Mixed gender forms, or imperative and verbal-noun buttons on the same screen.
- Latin punctuation inside Arabic sentences.

## Quality checklist

- [ ] Markets, audience, and the language strategy are stated in one sentence.
- [ ] Copy is written from intent, not translated line by line.
- [ ] One form of address and one button pattern are used throughout.
- [ ] Errors name the problem, preserve work, and offer recovery; pending is never shown as success.
- [ ] Terms are consistent across screens, notifications, and emails, and regional variants were chosen deliberately.
- [ ] Spelling (hamza, `ة`/`ه`, `ى`/`ي`) and Arabic punctuation are correct.
- [ ] Dates, digits, and currency match each target market.
- [ ] Native readers from at least two target countries reviewed shared copy.
