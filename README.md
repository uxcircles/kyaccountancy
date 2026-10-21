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

## What this fixes on the current site

Reviewed on kyaccountancy.com (Wix) in October 2026:

- **Wrong email address.** The footer on every page shows `info@kyacccountancy.com` (three c's).
- **Broken phone link.** Tapping the number dials `+44020…` (extra 0), which doesn't connect.
- **Not mobile-friendly.** Phones get the desktop layout shrunk down, with small text and no call button.
- **Pages at the wrong addresses.** `/about` shows *Ltd Company*, `/bookkeeping` shows *Self-Employed*, `/company-formation` shows *Amazon Business*, `/self-employed` shows *Charity Accounts*. Chinese and Korean pages live at `/copy-of-about-us`, `/copy-of-about-us-1`, `/copy-of-소식`, etc.
- **Out-of-date tax information.** The Amazon page lists EU country-by-country distance-selling thresholds (Germany €100,000, France €35,000…) and a UK £70,000 threshold — these were abolished in July 2021. *Tier 1 visa* accounts are still listed although the route has closed.
- **Stale news.** The only vacancy closed on 10/12/2023; "Click her to see more"; © 2023.
- **Translation issues.** 中文 calls a limited company 股份有限公司 (a joint-stock company) instead of 有限公司. The Korean pages mix in English and translate "Charity Accounts" as 자선 계정.
- **No address or opening status on the home page**, no meta descriptions, no structured data for Google.

## What the redesign adds

**Design.** An editorial look built from the KY diamond logo: deep navy, gold, warm paper, and oversized Instrument Serif headlines (Noto Serif SC / KR for Chinese and Korean). No stock photos.

**Motion** (all of it switched off for visitors who ask their device for reduced motion):

- The KY diamond draws itself in the hero, turns as you scroll and drifts with the mouse
- The hero's gold word rotates through English → 中文 → 한국어
- Headlines slide up line by line; the "who we are" statement lights up word by word as you scroll; numbers count up
- Gold marquee of services in three languages
- Services as a big numbered list; each row fills navy on hover
- "How we work" stays pinned while a gold progress line runs down the steps
- Giant HMRC countdown in days, and a giant "Let's talk" call to action
- Curtain transition between pages, magnetic buttons, a small blend-mode cursor on desktop, film-grain texture, oversized wordmark in the footer

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
assets/css/style.css
assets/js/main.js    motion, menu, open-now status, deadlines, calculator, form
```

## For the firm to check before launch

- **News items** (MTD for Income Tax, Companies House ID verification) are new drafts written for this redesign — please review the wording.
- **Contact form** has no server; it opens the visitor's email app. Swap in Formspree, Netlify Forms or similar if you want submissions without email.
- **Opening status** doesn't know about bank holidays.
- Add the **company registration number** to the footer if you'd like it shown.
- The Wix URLs should be **redirected** to the new pages (e.g. `/copy-of-about-us` → `/zh/about.html`).
