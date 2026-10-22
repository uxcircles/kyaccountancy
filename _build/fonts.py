"""Self-hosted, subset web fonts. Run after editing Chinese or Korean text:

    python3 _build/pages.py && python3 _build/fonts.py

Downloads the full fonts from Google Fonts once (cached in _build/.font-cache),
then writes small WOFF2 subsets to assets/fonts/:

- Source Serif 4: Google's variable Latin subset, trimmed to the weights we use but keeping the
  optical-size axis, so large headings keep their refined display letterforms
- Inter: Latin only
- Noto Serif SC / KR: only the characters used on the zh/ and ko/ pages

Needs `pip install fonttools brotli`.
"""
import glob
import html
import os
import re
import urllib.request

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
CACHE = os.path.join(BUILD, ".font-cache")
OUT = os.path.join(ROOT, "assets", "fonts")

G = "https://fonts.gstatic.com/s/"
SOURCES = {
    "source-serif-var": G + "sourceserif4/v15/vEFI2_tTDB4M7-auWDN0ahZJW1gb8te1Xb7G.woff2",
    "source-serif-var-italic": G + "sourceserif4/v15/vEFK2_tTDB4M7-auWDN0ahZJW1gewtW_WpzEpMs.woff2",
    "inter-400": G + "inter/v20/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuLyfMZg.ttf",
    "inter-500": G + "inter/v20/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuI6fMZg.ttf",
    "inter-600": G + "inter/v20/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuGKYMZg.ttf",
    "noto-serif-sc-500": G + "notoserifsc/v36/H4cyBXePl9DZ0Xe7gG9cyOj7uK2-n-D2rd4FY7SwqyWv.ttf",
    "noto-serif-kr-500": G + "notoserifkr/v32/3JnoSDn90Gmq2mr3blnHaTZXbOtLJDvui3JOncjUeM52.ttf",
}

LATIN = ("U+0020-007E,U+00A0-00FF,U+0131,U+0152-0153,U+2013-2014,U+2018-201E,U+2022,U+2026,"
         "U+2032-2033,U+20AC,U+2122,U+2190-2193,U+2197,U+2212")
# Characters that main.js writes at runtime (dates, countdowns)
RUNTIME = {"zh": "0123456789年月日天还有今明", "ko": "0123456789년월일남음오늘내"}


def fetch(name):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, name + os.path.splitext(SOURCES[name])[1])
    if not os.path.exists(path):
        print("downloading", name)
        urllib.request.urlretrieve(SOURCES[name], path)
    return path


def page_chars(lang):
    chars = set(RUNTIME[lang])
    for f in glob.glob(os.path.join(ROOT, lang, "*.html")):
        text = open(f, encoding="utf-8").read()
        text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", text, flags=re.S)
        text = html.unescape(re.sub(r"<[^>]+>", " ", text))
        chars.update(ch for ch in text if ord(ch) > 0x2E7F)  # CJK, Hangul, full-width forms
    return "".join(sorted(chars))


def make(name, out, unicodes=None, text=None):
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["*"]
    opts.name_IDs = ["*"]
    font = subset.load_font(fetch(name), opts)
    sub = subset.Subsetter(opts)
    sub.populate(unicodes=subset.parse_unicodes(unicodes) if unicodes else [], text=text or "")
    sub.subset(font)
    path = os.path.join(OUT, out + ".woff2")
    subset.save_font(font, path, opts)
    print(f"{out}.woff2  {os.path.getsize(path) // 1024} KB")


def make_variable(name, out, limits):
    font = instancer.instantiateVariableFont(TTFont(fetch(name)), limits)
    font.flavor = "woff2"
    path = os.path.join(OUT, out + ".woff2")
    font.save(path)
    print(f"{out}.woff2  {os.path.getsize(path) // 1024} KB")


def build():
    os.makedirs(OUT, exist_ok=True)
    for f in glob.glob(os.path.join(OUT, "*.woff2")):
        os.remove(f)
    make_variable("source-serif-var", "source-serif", {"wght": (500, 600), "opsz": (20, 60)})
    make_variable("source-serif-var-italic", "source-serif-italic", {"wght": (400, 500), "opsz": (20, 60)})
    for name in ["inter-400", "inter-500", "inter-600"]:
        make(name, name, unicodes=LATIN)
    for lang, name in [("zh", "noto-serif-sc-500"), ("ko", "noto-serif-kr-500")]:
        chars = page_chars(lang)
        print(lang, len(chars), "characters")
        make(name, name, text=chars)


if __name__ == "__main__":
    build()
