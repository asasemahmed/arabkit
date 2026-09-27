<div dir="rtl">

<div align="center">

# ArabKit

### مهارات لوكلاء الذكاء الاصطناعي لبناء منتجات تبدو محلية في كل دولة عربية.

[الدول](#الدول) · [المساهمة](CONTRIBUTING.md) · [English](README.md)

</div>

---

العربية لغة واحدة، لكن أسواقها كثيرة. صفحة الدفع التي تبدو طبيعية في القاهرة قد تبدو غريبة في الرياض أو الدار البيضاء: تختلف اللهجة، وتختلف معها صيغ أرقام الهاتف، والعناوين، والعملات، وطرق الدفع، وما يثق به الناس.

ArabKit مكتبة مفتوحة المصدر لمهارات وكلاء الذكاء الاصطناعي، مقسّمة **حسب الدولة**. لكل دولة عربية مجلد خاص بها، يكتبه ويراجعه أشخاص يعيشون فيها ويبنون منتجات لأهلها. أما المهارات التي تصلح لكل الدول فمكانها `shared/`.

> **الحالة:** الهيكل جاهز، وكل مجلدات الدول مفتوحة للمساهمة. لا توجد مهارات بعد، وأول المساهمين في كل دولة هم من سيحددون شكل العمل فيها. اقرأ [CONTRIBUTING.md](CONTRIBUTING.md).

## الدول

| الدولة | Country | بادئة اسم المهارة | المهارات |
|---|---|---|---|
| 🇩🇿 [الجزائر](countries/algeria/README.md) | Algeria | `algeria-` | 0 |
| 🇧🇭 [البحرين](countries/bahrain/README.md) | Bahrain | `bahrain-` | 0 |
| 🇰🇲 [جزر القمر](countries/comoros/README.md) | Comoros | `comoros-` | 0 |
| 🇩🇯 [جيبوتي](countries/djibouti/README.md) | Djibouti | `djibouti-` | 0 |
| 🇪🇬 [مصر](countries/egypt/README.md) | Egypt | `egypt-` | 0 |
| 🇮🇶 [العراق](countries/iraq/README.md) | Iraq | `iraq-` | 0 |
| 🇯🇴 [الأردن](countries/jordan/README.md) | Jordan | `jordan-` | 0 |
| 🇰🇼 [الكويت](countries/kuwait/README.md) | Kuwait | `kuwait-` | 0 |
| 🇱🇧 [لبنان](countries/lebanon/README.md) | Lebanon | `lebanon-` | 0 |
| 🇱🇾 [ليبيا](countries/libya/README.md) | Libya | `libya-` | 0 |
| 🇲🇷 [موريتانيا](countries/mauritania/README.md) | Mauritania | `mauritania-` | 0 |
| 🇲🇦 [المغرب](countries/morocco/README.md) | Morocco | `morocco-` | 0 |
| 🇴🇲 [عُمان](countries/oman/README.md) | Oman | `oman-` | 0 |
| 🇵🇸 [فلسطين](countries/palestine/README.md) | Palestine | `palestine-` | 0 |
| 🇶🇦 [قطر](countries/qatar/README.md) | Qatar | `qatar-` | 0 |
| 🇸🇦 [السعودية](countries/saudi-arabia/README.md) | Saudi Arabia | `saudi-` | 0 |
| 🇸🇴 [الصومال](countries/somalia/README.md) | Somalia | `somalia-` | 0 |
| 🇸🇩 [السودان](countries/sudan/README.md) | Sudan | `sudan-` | 0 |
| 🇸🇾 [سوريا](countries/syria/README.md) | Syria | `syria-` | 0 |
| 🇹🇳 [تونس](countries/tunisia/README.md) | Tunisia | `tunisia-` | 0 |
| 🇦🇪 [الإمارات](countries/uae/README.md) | United Arab Emirates | `uae-` | 0 |
| 🇾🇪 [اليمن](countries/yemen/README.md) | Yemen | `yemen-` | 0 |

المهارات العربية العامة التي تصلح لكل الدول مكانها [`shared/`](shared/README.md)، وبادئتها `arabic-`.

## كيف تساهم

1. اختر مجلد دولتك من [`countries/`](countries).
2. ابدأ من القالب [`templates/SKILL.template.md`](templates/SKILL.template.md). مهارة للمحتوى (copy) أو لتجربة المستخدم (product UX) بداية مناسبة.
3. شغّل `python scripts/validate.py` ثم افتح Pull Request.

ويمكنك أيضًا [التطوع مسؤولًا عن دولتك](https://github.com/asasemahmed/arabkit/issues/new?template=country-maintainer.yml).

## مشاريع مرتبطة

[MasrKit](https://github.com/asasemahmed/MasrKit) مجموعة مهارات مصرية متكاملة، وهي النموذج الذي يسعى ArabKit إلى بلوغ مستواه في كل دولة.

## الترخيص

[MIT](LICENSE)

</div>
