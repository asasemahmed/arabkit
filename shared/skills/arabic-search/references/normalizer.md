# Arabic search-key normalizer

Reference implementations of the folds in the `arabic-search` skill. Both produce identical output for the test cases below. Bump the version whenever the rules change, and rebuild the index.

## Python

```python
import re
import unicodedata

NORMALIZER_VERSION = 1
DIACRITICS = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭ]")
INVISIBLE = re.compile(r"[ـ​-‏‪-‮⁦-⁩]")  # tatweel, zero-width, bidi controls
LETTERS = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ة": "ه", "ى": "ي", "ی": "ي", "ک": "ك", "ؤ": "و", "ئ": "ي"})
DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹", "0123456789" * 2)


def search_key(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = DIACRITICS.sub("", text)
    text = INVISIBLE.sub("", text)
    text = text.translate(LETTERS).translate(DIGITS)
    return " ".join(text.casefold().split())
```

## JavaScript

```js
export const NORMALIZER_VERSION = 1;
const DIACRITICS = /[ؐ-ًؚ-ٰٟۖ-ۭ]/g;
const INVISIBLE = /[ـ​-‏‪-‮⁦-⁩]/g; // tatweel, zero-width, bidi controls
const LETTERS = { "أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ة": "ه", "ى": "ي", "ی": "ي", "ک": "ك", "ؤ": "و", "ئ": "ي" };

export function searchKey(text) {
  return text
    .normalize("NFKC")
    .replace(DIACRITICS, "")
    .replace(INVISIBLE, "")
    .replace(/[أإآٱةىیکؤئ]/g, (c) => LETTERS[c])
    .replace(/[٠-٩]/g, (d) => String(d.charCodeAt(0) - 0x0660))
    .replace(/[۰-۹]/g, (d) => String(d.charCodeAt(0) - 0x06f0))
    .toLowerCase()
    .split(/\s+/)
    .filter(Boolean)
    .join(" ");
}
```

## Test cases

| Input | Search key |
|---|---|
| `مُحَمَّد` | `محمد` |
| `أحمد` | `احمد` |
| `إسلام` | `اسلام` |
| `آمنة` | `امنه` |
| `مدرسة` | `مدرسه` |
| `مصطفى` | `مصطفي` |
| `العربيـــة` | `العربيه` |
| `ﻻ` | `لا` |
| `فارسی کتاب` | `فارسي كتاب` |
| `٠١٠١٢٣٤٥٦٧٨` | `01012345678` |
| `iPhone ١٥ برو` | `iphone 15 برو` |
| `مسؤول` | `مسوول` |
| `رئيس` | `رييس` |
| `۱۲۳` | `123` |

Add the cases from your own data to these, and run them in CI.
