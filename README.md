# KY Accountancy — website redesign

A redesign of [kyaccountancy.com](https://www.kyaccountancy.com/) for KY Accountancy Services Ltd, an ACCA-certified accountancy firm at 39–41 High Street, New Malden. Plain HTML, CSS and JavaScript — host the repository root on any static host (GitHub Pages, Netlify, Cloudflare Pages, Vercel).

## Languages

| Path   | Language     |
|--------|--------------|
| `/`    | English      |
| `/zh/` | 简体中文     |
| `/ko/` | 한국어       |

Every page exists in all three languages, with `hreflang` links between them and a language switch in the header and footer.

**Pages:** Home · Services · About · News & careers · Contact

## Run locally

```bash
python3 -m http.server 5180
```

Then open http://localhost:5180.

## Editing

The HTML is generated so the header, footer and contact details stay consistent across 15 pages:

- Contact details, header, footer, UI strings: `_build/layout.py`
- Services and news text (all three languages side by side, via `L(english, 中文, 한국어)`): `_build/content.py`
- Page layouts and headlines: `_build/pages.py` (a `|` in a headline marks a line break for the reveal animation)

Rebuild after editing (Python 3, no dependencies):

```bash
python3 _build/pages.py
```

**Fonts** are self-hosted subsets in `assets/fonts/`, built by `_build/fonts.py` (needs `pip install fonttools brotli`). The Chinese and Korean heading fonts contain only the characters used on the site, so **after adding or changing Chinese or Korean text, also run**:

```bash
python3 _build/fonts.py
```

Otherwise new characters fall back to the system serif font.

## What the redesign adds

**Design.** An editorial look built from the KY diamond logo: deep navy, gold, warm paper, and Source Serif 4 headlines with Inter for body text (Noto Serif SC / KR for Chinese and Korean). No stock photos.

**Motion** is deliberately restrained, as befits an accountancy firm, and switches off entirely for visitors who ask their device for reduced motion:

- The KY logo (redrawn as SVG from the original artwork) draws itself once, faintly, behind the inner-page headings
- Headlines slide up line by line and paragraphs fade in, once, as they come into view
- Statistics and the HMRC countdown count up once
- A gold progress line runs down the "How we work" steps
- Quiet hover states: service rows tint and their arrow turns navy

The home page hero pairs the headline with a warm ivory **office card** laid out like a ledger: open/closed status, then phone, WeChat/WhatsApp and ACCA verification as full-width rows with gold icons, and the next HMRC deadline with a countdown. The accreditation logos (ACCA, AAT, CISI, AIA) sit directly under the hero, in greyscale until hovered. If the firm can supply photos of the team or the office, a photo would be a stronger hero than the card.

**Useful features:**

- Fixed **Call / Message / Email** bar on phones; tap-to-open WeChat and WhatsApp links (decoded from the existing QR codes) as well as the QR codes
- Live **"Open now / Closed · opens 9am tomorrow"** status on London time
- **Next HMRC deadline** countdown and upcoming Self Assessment dates, worked out from today's date
- **Limited company deadline calculator**: enter a year end, get the Companies House accounts, Corporation Tax payment and CT600 dates
- One services page covering all five service areas, each with a current "Good to know" note (Making Tax Digital for Income Tax, Companies House ID verification, current UK/EU VAT thresholds, 60-day property CGT)
- Contact form that opens the visitor's email app with the enquiry pre-filled (service, preferred language)
- Correct `tel:` and `mailto:` links, `AccountingService` structured data, per-page titles and descriptions in each language

## Structure

```
_build/layout.py     header, footer, page shell, contact details, UI strings
_build/content.py    services, accreditations, news (three languages side by side)
_build/pages.py      page templates
_build/fonts.py      builds the self-hosted font subsets
assets/fonts/        Source Serif 4, Inter, Noto Serif SC / KR (subset WOFF2)
assets/css/style.css
assets/js/main.js    reveals, menu, open-now status, deadlines, calculator, form
```

## Internal notes

The review of the current site, the items to confirm with the client and the pitch material are kept locally in `.private/` (git-ignored, never committed).

After cloning, enable the git hooks:

```
git config core.hooksPath .githooks
```

Commits and pushes are then blocked if they include `.private/` or a phrase from `.private/blocklist.txt`, and the open to-dos in `.private/NOTES.md` are printed. To see them any time: `sh .githooks/remind.sh`
