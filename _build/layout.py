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


def lines(text):
    """Split a headline on '|' into masked lines for the reveal animation."""
    return "".join(f'<span class="line"><span>{part}</span></span>' for part in text.split("|"))


NAV = [
    ("services.html", L("Services", "服务项目", "서비스")),
    ("about.html", L("About", "关于我们", "회사 소개")),
    ("news.html", L("News", "新闻资讯", "소식")),
    ("contact.html", L("Contact", "联系我们", "문의하기")),
]

ADDRESS = ["KY Accountancy Services Ltd", "Units 2, 5 &amp; 6, 2nd Floor", "39–41 High Street", "New Malden, Surrey KT3 3BY"]

UI = {
    "skip": L("Skip to content", "跳至正文", "본문으로 건너뛰기"),
    "menu": L("Menu", "菜单", "메뉴"),
    "close": L("Close", "关闭", "닫기"),
    "call": L("Call", "致电", "전화"),
    "email": L("Email", "电邮", "이메일"),
    "chat_short": L("Message", "微信", "메시지"),
    "talk": L("Book a consultation", "预约咨询", "상담 예약"),
    "hours": L("Opening hours", "办公时间", "영업시간"),
    "hours_days": L("Monday – Friday", "周一至周五", "월요일 – 금요일"),
    "hours_time": L("9:00am – 5:30pm", "上午 9:00 – 下午 5:30", "오전 9:00 – 오후 5:30"),
    "hours_closed": L("Closed weekends and bank holidays", "周末及英国公众假期休息", "주말 및 영국 공휴일 휴무"),
    "office": L("Office", "办公室地址", "사무실"),
    "pages": L("Pages", "页面", "페이지"),
    "directions": L("Get directions", "查看地图", "길찾기"),
    "footer_q": L("Have a question about|your accounts?", "对您的账目|有疑问？", "회계·세무에 대해|궁금한 점이 있으신가요?"),
    "rights": L("All rights reserved.", "版权所有。", "모든 권리 보유."),
    "reg": L("Registered in England and Wales.", "于英格兰及威尔士注册。", "잉글랜드 및 웨일스 등록 법인."),
    "top": L("Back to top", "返回顶部", "맨 위로"),
}

# Strings main.js needs (open-now status, deadlines, calculator, form)
JS_STRINGS = {
    "en": {
        "open": "Open now", "closes": "until 5:30pm", "closed": "Closed now",
        "opensToday": "opens 9am today", "opensTomorrow": "opens 9am tomorrow", "opensMonday": "opens 9am Monday",
        "today": "today", "tomorrow": "tomorrow", "inDays": "in {n} days", "days": "days", "day": "day",
        "until": "until {date}",
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
        "today": "今天", "tomorrow": "明天", "inDays": "还有 {n} 天", "days": "天", "day": "天",
        "until": "距离 {date}",
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
        "today": "오늘", "tomorrow": "내일", "inDays": "{n}일 남음", "days": "일", "day": "일",
        "until": "{date}까지",
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
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "arrow-ne": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>',
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>',
}

DIAMOND_SVG = """<svg class="diamond" viewBox="0 0 600 600" aria-hidden="true">
  <defs>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f1d9a0"/><stop offset=".45" stop-color="#b48f4c"/><stop offset="1" stop-color="#e9cf8f"/>
    </linearGradient>
    <linearGradient id="silver" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#8d92ad"/><stop offset=".5" stop-color="#e4e6f0"/><stop offset="1" stop-color="#8d92ad"/>
    </linearGradient>
  </defs>
  <g fill="none" stroke-linejoin="miter">
    <path class="d d1" pathLength="1" d="M300 20 580 300 300 580 20 300Z" stroke="url(#gold)" stroke-width="2"/>
    <path class="d d2" pathLength="1" d="M300 70 530 300 300 530 70 300Z" stroke="url(#silver)" stroke-width="1.5"/>
    <path class="d d3" pathLength="1" d="M300 120 480 300 300 480 120 300Z" stroke="url(#gold)" stroke-width="3"/>
    <path class="d d4" pathLength="1" d="M60 210h120M420 210h120M60 390h120M420 390h120" stroke="url(#gold)" stroke-width="1.5"/>
  </g>
  <g class="ky" fill="url(#gold)" font-family="Instrument Serif, Georgia, serif">
    <text x="232" y="318" font-size="150">K</text><text x="298" y="372" font-size="150">Y</text>
  </g>
</svg>"""


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


def roll(text):
    """Nav label that rolls to a copy of itself on hover."""
    return f'<span class="roll" data-text="{text}"><span>{text}</span></span>'


def asset(lang):
    return ("../" if LANGS[lang]["dir"] else "") + "assets/"


def header(lang, page):
    a = asset(lang)
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{href}"{cur if href == page else ""}>{roll(r(label, lang))}</a>' for href, label in NAV)
    big = "".join(
        f'<li><a href="{href}"{cur if href == page else ""}><span class="mn">0{i}</span>{r(label, lang)}</a></li>'
        for i, (href, label) in enumerate(NAV, 1))
    return f"""<a class="skip" href="#main">{r(UI['skip'], lang)}</a>
<header class="site-header" data-header>
  <div class="wrap header-inner">
    <a class="brand" href="./" aria-label="KY Accountancy — home">
      <img src="{a}img/logo-mark.png" alt="" width="34" height="39">
      <span class="brand-name">KY Accountancy</span>
    </a>
    <nav class="main-nav" aria-label="Main">{nav}</nav>
    {lang_switch(lang, page)}
    <a class="btn btn-pill header-cta" href="contact.html">{roll(r(UI['talk'], lang))}</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="menu"><span class="menu-lines"><span></span><span></span></span><span class="sr">{r(UI['menu'], lang)}</span></button>
  </div>
</header>
<div class="menu" id="menu" hidden>
  <div class="wrap menu-inner">
    <ul class="menu-links">{big}</ul>
    <div class="menu-foot">
      <a href="tel:{PHONE_TEL}">{PHONE_INTL}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      {lang_switch(lang, page)}
    </div>
  </div>
</div>"""


def footer(lang, page):
    a = asset(lang)
    nav = "".join(f'<li><a href="{h}">{roll(r(lbl, lang))}</a></li>' for h, lbl in NAV)
    addr = "<br>".join(ADDRESS)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <h2 class="footer-q split">{lines(r(UI['footer_q'], lang))}</h2>
      <div class="footer-contact">
        <a class="big-link" href="mailto:{EMAIL}">{EMAIL}</a>
        <a class="big-link" href="tel:{PHONE_TEL}">{PHONE_INTL}</a>
      </div>
    </div>
    <div class="footer-grid">
      <div><h3 class="f-h">{r(UI['office'], lang)}</h3><p>{addr}</p><p><a class="u" href="{MAPS_URL}" rel="noopener" target="_blank">{r(UI['directions'], lang)} ↗</a></p></div>
      <div><h3 class="f-h">{r(UI['hours'], lang)}</h3><p>{r(UI['hours_days'], lang)}<br>{r(UI['hours_time'], lang)}<br><span class="dim">{r(UI['hours_closed'], lang)}</span></p></div>
      <div><h3 class="f-h">{r(UI['pages'], lang)}</h3><ul class="f-links">{nav}</ul></div>
      <div><h3 class="f-h">Language</h3>{lang_switch(lang, page)}<p class="f-acca"><a class="u" href="{ACCA_URL}" rel="noopener" target="_blank">ACCA firm details ↗</a></p></div>
    </div>
  </div>
  <div class="wordmark" aria-hidden="true"><span>KY Accountancy</span></div>
  <div class="wrap footer-base">
    <span>© <span data-year>2026</span> KY Accountancy Services Ltd. {r(UI['reg'], lang)} {r(UI['rights'], lang)}</span>
    <a href="#main" class="u">{r(UI['top'], lang)} ↑</a>
  </div>
</footer>
<nav class="action-bar" aria-label="Quick contact">
  <a href="tel:{PHONE_TEL}">{ICON['phone']}<span>{r(UI['call'], lang)}</span></a>
  <a href="contact.html#chat">{ICON['chat']}<span>{r(UI['chat_short'], lang)}</span></a>
  <a href="mailto:{EMAIL}">{ICON['mail']}<span>{r(UI['email'], lang)}</span></a>
</nav>"""


FONTS = {
    "en": "family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600",
    "zh": "family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&family=Noto+Serif+SC:wght@500;600",
    "ko": "family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&family=Noto+Serif+KR:wght@500;600",
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
<meta name="theme-color" content="#0b0e2c">
<link rel="icon" type="image/png" href="{a}img/favicon.png">
<link rel="apple-touch-icon" href="{a}img/apple-touch-icon.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{FONTS[lang]}&display=swap">
<link rel="stylesheet" href="{a}css/style.css">
<script>document.documentElement.classList.add("js")</script>
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
