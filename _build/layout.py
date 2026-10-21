"""Shared header, footer and page shell for every language."""
import json

LANGS = {
    "en": {"dir": "", "html": "en-GB", "label": "EN", "name": "English"},
    "zh": {"dir": "zh/", "html": "zh-Hans", "label": "中文", "name": "简体中文"},
    "ko": {"dir": "ko/", "html": "ko", "label": "한국어", "name": "한국어"},
}

SITE = "https://www.kyaccountancy.com/"
PHONE_DISPLAY = "020 8942 8547"
PHONE_INTL = "+44 20 8942 8547"
PHONE_TEL = "+442089428547"
EMAIL = "info@kyaccountancy.com"
WECHAT_URL = "https://u.wechat.com/kLmBtSFjA2uLcSl9BzCH8WE"
WHATSAPP_URL = "https://wa.me/qr/SLMGOVUIFX5LL1"
ACCA_URL = ("https://www.accaglobal.com/uk/en/member/find-an-accountant/find-firm/results/"
            "details.html?isocountry=GB&location=new+malden&country=UK&organisationid=ACCA&advisorid=4818904")
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=39-41+High+Street+New+Malden+KT3+3BY"


def L(en, zh, ko=None):
    return {"en": en, "zh": zh, "ko": ko if ko is not None else en}


def r(x, lang):
    return x[lang] if isinstance(x, dict) else x


NAV = [
    ("services.html", L("Services", "服务项目", "서비스")),
    ("about.html", L("About", "关于我们", "회사 소개")),
    ("news.html", L("News", "新闻资讯", "소식")),
    ("contact.html", L("Contact", "联系我们", "문의하기")),
]

ADDRESS = L(
    ["KY Accountancy Services Ltd", "Units 2, 5 &amp; 6, 2nd Floor", "39–41 High Street", "New Malden, Surrey KT3 3BY"],
    ["KY Accountancy Services Ltd", "Units 2, 5 &amp; 6, 2nd Floor", "39–41 High Street", "New Malden, Surrey KT3 3BY"],
    ["KY Accountancy Services Ltd", "Units 2, 5 &amp; 6, 2nd Floor", "39–41 High Street", "New Malden, Surrey KT3 3BY"],
)

UI = {
    "skip": L("Skip to content", "跳至正文", "본문으로 건너뛰기"),
    "menu": L("Menu", "菜单", "메뉴"),
    "call": L("Call", "致电", "전화"),
    "email": L("Email", "电邮", "이메일"),
    "chat": L("WeChat / WhatsApp", "微信 / WhatsApp", "WeChat / WhatsApp"),
    "chat_short": L("Message", "微信", "메시지"),
    "hours": L("Opening hours", "办公时间", "영업시간"),
    "hours_days": L("Monday – Friday", "周一至周五", "월요일 – 금요일"),
    "hours_time": L("9:00am – 5:30pm", "上午 9:00 – 下午 5:30", "오전 9:00 – 오후 5:30"),
    "hours_closed": L("Closed weekends and bank holidays", "周末及英国公众假期休息", "주말 및 영국 공휴일 휴무"),
    "office": L("Office", "办公室地址", "사무실"),
    "directions": L("Get directions", "查看地图", "길찾기"),
    "footer_blurb": L(
        "ACCA-certified accountants for individuals, small businesses and charities. "
        "On New Malden High Street since 2014.",
        "ACCA 认证会计师事务所，为个人、中小企业及慈善机构提供会计与税务服务。2014 年起扎根新莫尔登高街。",
        "개인, 중소기업, 자선단체를 위한 ACCA 인증 회계 사무소. 2014년부터 뉴몰든 하이 스트리트에 있습니다.",
    ),
    "rights": L("All rights reserved.", "版权所有。", "모든 권리 보유."),
    "reg": L("Registered in England and Wales.", "于英格兰及威尔士注册。", "잉글랜드 및 웨일스 등록 법인."),
    "languages": L("We speak English, 中文 and 한국어", "我们提供英语、中文（普通话）及韩语服务", "영어, 중국어, 한국어로 상담 가능합니다"),
}

# Strings main.js needs (open-now status, deadlines, calculator, form)
JS_STRINGS = {
    "en": {
        "open": "Open now", "closes": "until 5:30pm", "closed": "Closed now",
        "opensToday": "opens 9am today", "opensTomorrow": "opens 9am tomorrow", "opensMonday": "opens 9am Monday",
        "today": "today", "tomorrow": "tomorrow", "inDays": "in {n} days",
        "dl": {
            "jan": "Online Self Assessment return and tax due for {ty}",
            "jul": "Second payment on account for {ty}",
            "oct5": "Register for Self Assessment if you started self-employment or letting in {ty}",
            "oct31": "Paper Self Assessment return deadline for {ty}",
        },
        "calc": {"accounts": "Accounts to Companies House", "ctpay": "Corporation Tax payment", "ct600": "Company Tax Return (CT600)"},
        "mailSubject": "Website enquiry", "mailName": "Name", "mailPhone": "Phone", "mailLang": "Preferred language",
        "mailService": "Service",
    },
    "zh": {
        "open": "营业中", "closes": "至下午 5:30", "closed": "已下班",
        "opensToday": "今天上午 9 点开门", "opensTomorrow": "明天上午 9 点开门", "opensMonday": "周一上午 9 点开门",
        "today": "今天", "tomorrow": "明天", "inDays": "还有 {n} 天",
        "dl": {
            "jan": "{ty} 税务年度网上个人报税及缴税截止",
            "jul": "{ty} 税务年度第二期预缴税款",
            "oct5": "如在 {ty} 税务年度开始自雇或出租房产，须登记个人报税",
            "oct31": "{ty} 税务年度纸质个人报税表截止",
        },
        "calc": {"accounts": "向 Companies House 递交年度账目", "ctpay": "缴纳公司税", "ct600": "递交公司税申报表（CT600）"},
        "mailSubject": "网站咨询", "mailName": "姓名", "mailPhone": "电话", "mailLang": "希望使用的语言",
        "mailService": "咨询服务",
    },
    "ko": {
        "open": "영업 중", "closes": "오후 5:30까지", "closed": "영업 종료",
        "opensToday": "오늘 오전 9시 오픈", "opensTomorrow": "내일 오전 9시 오픈", "opensMonday": "월요일 오전 9시 오픈",
        "today": "오늘", "tomorrow": "내일", "inDays": "{n}일 남음",
        "dl": {
            "jan": "{ty} 과세연도 온라인 종합소득세 신고 및 납부 마감",
            "jul": "{ty} 과세연도 2차 예정납부",
            "oct5": "{ty} 과세연도에 자영업·임대를 시작했다면 Self Assessment 등록 마감",
            "oct31": "{ty} 과세연도 서면 신고 마감",
        },
        "calc": {"accounts": "Companies House 결산서 제출", "ctpay": "법인세 납부", "ct600": "법인세 신고서(CT600) 제출"},
        "mailSubject": "웹사이트 문의", "mailName": "이름", "mailPhone": "전화번호", "mailLang": "희망 언어",
        "mailService": "문의 서비스",
    },
}

ICON = {
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "ext": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>',
    "ltd": '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M5 28V9l9-4v23M14 12h13v16M9 12h1M9 17h1M9 22h1M18 16h1M22 16h1M18 21h1M22 21h1M3 28h26"/></svg>',
    "self": '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="10" r="5"/><path d="M6 28c0-5.5 4.5-9 10-9s10 3.5 10 9"/><path d="M20 23l2 2 4-4"/></svg>',
    "seller": '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M4 11 16 5l12 6v12l-12 6-12-6z"/><path d="m4 11 12 6 12-6M16 17v12"/></svg>',
    "charity": '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 27S4 20 4 12a6 6 0 0 1 12-1 6 6 0 0 1 12 1c0 8-12 15-12 15z"/></svg>',
    "tax": '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M5 14 16 5l11 9M8 12v15h16V12"/><path d="m12.5 23.5 7-7"/><circle cx="13" cy="17" r="1.3"/><circle cx="19" cy="23" r="1.3"/></svg>',
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>',
}


def lang_switch(lang, page):
    prefix = "../" if LANGS[lang]["dir"] else ""
    items = []
    for code, meta in LANGS.items():
        href = prefix + meta["dir"] + (page if page != "index.html" else "")
        if not href:
            href = "./"
        cur = ' aria-current="true"' if code == lang else ""
        items.append(f'<a href="{href}" lang="{meta["html"]}" hreflang="{meta["html"]}"{cur}>{meta["label"]}</a>')
    return '<div class="lang" role="group" aria-label="Language">' + "".join(items) + "</div>"


def header(lang, page):
    home = "./"
    cur = ' aria-current="page"'
    nav = "".join(
        f'<a href="{href}"{cur if href == page else ""}>{r(label, lang)}</a>'
        for href, label in NAV
    )
    a = asset(lang)
    return f"""<a class="skip" href="#main">{r(UI['skip'], lang)}</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{home}" aria-label="KY Accountancy — home">
      <img src="{a}img/logo-mark.png" alt="" width="42" height="48">
      <span class="brand-text"><span class="brand-name">KY Accountancy</span><span class="brand-sub">ACCA · New Malden</span></span>
    </a>
    <nav class="main-nav" id="main-nav" aria-label="Main">
      {nav}
      {lang_switch(lang, page)}
    </nav>
    <a class="btn btn-sm btn-gold header-call" href="tel:{PHONE_TEL}">{ICON['phone']}<span>{PHONE_DISPLAY}</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="main-nav"><span></span><span></span><span></span><span class="sr">{r(UI['menu'], lang)}</span></button>
  </div>
</header>"""


def footer(lang, page):
    a = asset(lang)
    nav = "".join(f'<li><a href="{h}">{r(lbl, lang)}</a></li>' for h, lbl in NAV)
    addr = "<br>".join(r(ADDRESS, lang))
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <a class="brand brand-light" href="./"><img src="{a}img/logo-mark.png" alt="" width="42" height="48"><span class="brand-text"><span class="brand-name">KY Accountancy</span><span class="brand-sub">ACCA · New Malden</span></span></a>
      <p>{r(UI['footer_blurb'], lang)}</p>
      {lang_switch(lang, page)}
    </div>
    <div>
      <h2 class="f-h">{r(UI['office'], lang)}</h2>
      <p>{addr}</p>
      <p><a href="{MAPS_URL}" rel="noopener" target="_blank">{r(UI['directions'], lang)} ↗</a></p>
    </div>
    <div>
      <h2 class="f-h">{r(UI['hours'], lang)}</h2>
      <p>{r(UI['hours_days'], lang)}<br>{r(UI['hours_time'], lang)}<br><span class="muted">{r(UI['hours_closed'], lang)}</span></p>
      <p><a href="tel:{PHONE_TEL}">{PHONE_INTL}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div>
      <h2 class="f-h">KY</h2>
      <ul class="f-links">{nav}</ul>
    </div>
  </div>
  <div class="wrap footer-base">
    <span>© <span data-year>2026</span> KY Accountancy Services Ltd. {r(UI['reg'], lang)} {r(UI['rights'], lang)}</span>
    <a href="{ACCA_URL}" rel="noopener" target="_blank">ACCA Firm details ↗</a>
  </div>
</footer>
<div class="action-bar" aria-label="Quick contact">
  <a href="tel:{PHONE_TEL}">{ICON['phone']}<span>{r(UI['call'], lang)}</span></a>
  <a href="contact.html#chat">{ICON['chat']}<span>{r(UI['chat_short'], lang)}</span></a>
  <a href="mailto:{EMAIL}">{ICON['mail']}<span>{r(UI['email'], lang)}</span></a>
</div>"""


def asset(lang):
    return ("../" if LANGS[lang]["dir"] else "") + "assets/"


FONTS = {
    "en": "family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600",
    "zh": "family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&family=Noto+Serif+SC:wght@600",
    "ko": "family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&family=Noto+Serif+KR:wght@600",
}


def page(lang, name, title, description, body, body_class=""):
    a = asset(lang)
    meta = LANGS[lang]
    alts = "\n".join(
        f'<link rel="alternate" hreflang="{m["html"]}" href="{SITE}{m["dir"]}{"" if name == "index.html" else name}">'
        for m in LANGS.values()
    )
    canonical = f'{SITE}{meta["dir"]}{"" if name == "index.html" else name}'
    js = json.dumps(JS_STRINGS[lang], ensure_ascii=False)
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "AccountingService",
        "name": "KY Accountancy Services Ltd", "url": SITE, "telephone": PHONE_INTL, "email": EMAIL,
        "address": {"@type": "PostalAddress", "streetAddress": "Units 2, 5 & 6, 2nd Floor, 39-41 High Street",
                    "addressLocality": "New Malden", "addressRegion": "Surrey", "postalCode": "KT3 3BY", "addressCountry": "GB"},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                       "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                       "opens": "09:00", "closes": "17:30"}],
        "foundingDate": "2014", "knowsLanguage": ["en", "zh", "ko"],
    }, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="{meta['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
{alts}
<link rel="alternate" hreflang="x-default" href="{SITE}{'' if name == 'index.html' else name}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#161b4d">
<link rel="icon" type="image/png" href="{a}img/favicon.png">
<link rel="apple-touch-icon" href="{a}img/apple-touch-icon.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{FONTS[lang]}&display=swap">
<link rel="stylesheet" href="{a}css/style.css">
<script type="application/ld+json">{schema}</script>
</head>
<body class="{body_class}">
{header(lang, name)}
<main id="main">
{body}
</main>
{footer(lang, name)}
<script>window.KY = {js};</script>
<script src="{a}js/main.js" defer></script>
</body>
</html>
"""
