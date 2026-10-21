"""Page templates for KY Accountancy. Run: python3 _build/pages.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from layout import (L, r, lines, LANGS, ICON, UI, page, asset, ADDRESS, PHONE_DISPLAY, PHONE_INTL, PHONE_TEL, EMAIL,
                    WECHAT_URL, WHATSAPP_URL, ACCA_URL, MAPS_URL, DIAMOND_SVG)
from content import SERVICES, ACCREDITATIONS, NEWS, fmt_date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def label(n, text, lang):
    return f'<p class="label"><span class="label-n">({n:02d})</span>{r(text, lang)}</p>'


def roll_text(text):
    return f'<span class="roll" data-text="{text}"><span>{text}</span></span>'


def accreditation_strip(lang):
    a = asset(lang)
    imgs = "".join(f'<li><img src="{a}img/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></li>'
                   for f, alt, w, h in ACCREDITATIONS)
    return f'<ul class="accred">{imgs}</ul>'


def chat_cards(lang):
    a = asset(lang)
    tap = r(L('Scan or tap', '扫码或点击', '스캔 또는 탭'), lang)
    return f"""<div class="chat-cards">
  <a class="qr" href="{WECHAT_URL}" rel="noopener" target="_blank">
    <img src="{a}img/qr-wechat.png" alt="WeChat QR code — KY Accountancy" width="180" height="180" loading="lazy">
    <span class="qr-cap"><strong>{r(L('WeChat', '微信', 'WeChat'), lang)}</strong><span>{tap} ↗</span></span>
  </a>
  <a class="qr" href="{WHATSAPP_URL}" rel="noopener" target="_blank">
    <img src="{a}img/qr-whatsapp.png" alt="WhatsApp QR code — KY Accountancy" width="180" height="175" loading="lazy">
    <span class="qr-cap"><strong>WhatsApp</strong><span>{tap} ↗</span></span>
  </a>
</div>"""


def status_chip(lang):
    return (f'<div class="status" data-open-status><span class="dot"></span>'
            f'<span data-status-text>{r(UI["hours_days"], lang)} · {r(UI["hours_time"], lang)}</span></div>')


def page_hero(lang, n, eyebrow, title, lead=None):
    lead_html = f'<p class="page-lead reveal-up">{r(lead, lang)}</p>' if lead else ""
    return f"""
<section class="page-hero dark">
  <div class="hero-diamond hero-diamond-sm">{DIAMOND_SVG}</div>
  <div class="wrap">
    {label(n, eyebrow, lang)}
    <h1 class="display split">{lines(r(title, lang))}</h1>
    {lead_html}
  </div>
</section>"""


def cta_band(lang):
    return f"""
<section class="section cta-sec cta-sec-sm">
  <div class="wrap">
    <a class="giant-cta" href="contact.html">
      <span class="giant-cta-t split">{lines(r(L('Questions about|your situation?', '对您的情况|有疑问？', '궁금한 점이|있으신가요?'), lang))}</span>
      <span class="giant-cta-c">{ICON['arrow-ne']}</span>
    </a>
  </div>
</section>"""


# ---------------------------------------------------------------- home
def home(lang):
    h1 = lines(r(L("Precise accounts.|Clear advice.|<em>In your language.</em>",
                   "账目精准，|建议清晰，|<em>用您的语言沟通。</em>",
                   "정확한 회계,|명확한 조언,|<em>익숙한 언어로.</em>"), lang))

    rows = "".join(f"""
      <li><a href="services.html#{s['id']}" class="svc-row">
        <span class="svc-n">{i:02d}</span>
        <span class="svc-t">{r(s['name'], lang)}</span>
        <span class="svc-d">{r(s['short'], lang)}</span>
        <span class="svc-a">{ICON['arrow-ne']}</span>
      </a></li>""" for i, s in enumerate(SERVICES, 1))

    steps = [
        (L("Get in touch", "联系我们", "문의하기"),
         L("Call, email, or message us on WeChat or WhatsApp in English, Chinese or Korean.",
           "通过电话、电邮、微信或 WhatsApp 联系我们，可使用中文、英语或韩语。",
           "전화, 이메일, WeChat, WhatsApp으로 한국어·영어·중국어로 편하게 문의하세요.")),
        (L("We agree the scope", "确定服务内容", "업무 범위 확정"),
         L("We look at your situation, explain what HMRC and Companies House need from you, and agree what we’ll handle.",
           "我们了解您的情况，说明 HMRC 和 Companies House 的要求，并与您确认由我们负责的事项。",
           "상황을 살펴보고 HMRC와 Companies House가 요구하는 사항을 설명한 뒤, 저희가 맡을 업무를 함께 정합니다.")),
        (L("We keep you on track", "按时完成申报", "기한 관리"),
         L("We prepare and file your returns, and remind you before every deadline so there are no penalties.",
           "我们为您准备并递交各类申报，并在每个截止日期前提醒您，避免罚款。",
           "신고서를 준비·제출하고 마감 전에 미리 알려드려 가산세 걱정이 없도록 합니다.")),
    ]
    steps_html = "".join(f'<li class="step"><span class="step-n">{i:02d}</span><div><h3>{r(t, lang)}</h3><p>{r(d, lang)}</p></div></li>'
                         for i, (t, d) in enumerate(steps, 1))

    stats = [
        ('data-since="2014"', "12", L("Years in New Malden", "年扎根新莫尔登", "년 뉴몰든에서")),
        ('data-count="3"', "3", L("Languages spoken", "种服务语言", "개 언어 상담")),
        ('data-count="5"', "5", L("Service areas", "大服务范畴", "개 서비스 분야")),
        ('data-count="4"', "4", L("Professional bodies", "个专业协会资格", "개 전문 협회")),
    ]
    stats_html = "".join(f'<li><span class="stat-n" {attr}>{v}</span><span class="stat-l">{r(t, lang)}</span></li>'
                         for attr, v, t in stats)

    statement = r(L(
        "Since 2014 we’ve helped sole traders, limited companies, online sellers, landlords and charities across London keep HMRC and Companies House happy — in the language they think in.",
        "自 2014 年以来，我们帮助伦敦各地的自雇人士、有限公司、跨境电商、房东和慈善机构，用他们最熟悉的语言，从容应对 HMRC 与 Companies House 的各项要求。",
        "2014년부터 런던의 자영업자, 법인, 온라인 셀러, 임대인, 자선단체가 가장 편한 언어로 HMRC와 Companies House 업무를 해결할 수 있도록 도와 왔습니다.",
    ), lang)

    body = f"""
<section class="hero dark" data-hero>
  <div class="hero-diamond">{DIAMOND_SVG}</div>
  <div class="wrap hero-inner">
    <ul class="hero-tags reveal-up">
      <li>ACCA {r(L('certified', '认证', '인증'), lang)}</li>
      <li>New Malden, London</li>
      <li>Est. 2014</li>
    </ul>
    <h1 class="hero-title split">{h1}</h1>
    <div class="hero-bottom">
      <p class="hero-lead reveal-up">{r(L('ACCA-certified accountants for sole traders, limited companies, online sellers, landlords and charities.', '为自雇人士、有限公司、跨境电商、房东及慈善机构服务的 ACCA 认证会计师。', '자영업자, 법인, 온라인 셀러, 임대인, 자선단체를 위한 ACCA 인증 회계사.'), lang)}</p>
      <div class="hero-actions reveal-up">
        <a class="btn btn-gold" href="contact.html"><span>{r(L('Book a consultation', '预约咨询', '상담 예약'), lang)}</span>{ICON['arrow']}</a>
        <a class="btn-text" href="services.html">{roll_text(r(L('Explore services', '浏览服务', '서비스 보기'), lang))}</a>
      </div>
      <div class="hero-live reveal-up">
        {status_chip(lang)}
        <a class="next-dl" href="#key-dates" data-next-deadline hidden>
          <span class="next-dl-k">{r(L('Next HMRC deadline', '下一个 HMRC 截止日', '다음 HMRC 마감일'), lang)}</span>
          <span class="next-dl-v"><b data-dl-date></b> · <span data-dl-in></span></span>
        </a>
      </div>
    </div>
  </div>
</section>

<section class="accred-sec accred-top" aria-label="{r(L('Professional memberships', '专业资格', '전문 자격'), lang)}">
  <div class="wrap accred-inner">
    <p class="accred-k">{r(L('Regulated &amp; accredited', '专业认证', '공인 자격'), lang)}</p>
    {accreditation_strip(lang)}
  </div>
</section>

<section class="section statement-sec" id="intro">
  <div class="wrap">
    {label(1, L('Who we are', '关于我们', '회사 소개'), lang)}
    <p class="statement">{statement}</p>
    <ul class="stats">{stats_html}</ul>
  </div>
</section>

<section class="section services-sec">
  <div class="wrap">
    <div class="sec-head">
      {label(2, L('Services', '服务项目', '서비스'), lang)}
      <h2 class="h-xl split">{lines(r(L('Everything HMRC|asks of you, handled.', 'HMRC 的要求，|交给我们。', 'HMRC 업무,|저희가 처리합니다.'), lang))}</h2>
    </div>
    <ol class="svc-rows">{rows}</ol>
  </div>
</section>

<section class="section process-sec">
  <div class="wrap process-grid">
    <div class="process-sticky">
      {label(3, L('How we work', '合作流程', '진행 방식'), lang)}
      <h2 class="h-xl split">{lines(r(L('Straightforward|from the first call.', '从第一次沟通|开始，简单清晰。', '첫 상담부터|명확하게.'), lang))}</h2>
      <p class="muted reveal-up">{r(L('Our accountants have worked in finance teams from small businesses to multinational headquarters — and bring that experience to every client, whatever their size.', '我们的会计师曾任职于中小企业至跨国公司总部的财务部门，无论客户规模大小都同样用心。', '저희 회계사들은 중소기업부터 다국적 기업 본사 재무팀까지 경험을 쌓았으며, 규모와 상관없이 모든 고객에게 그 경험을 제공합니다.'), lang)}</p>
    </div>
    <ol class="steps" data-progress>{steps_html}</ol>
  </div>
</section>

<section class="section dark dates-sec" id="key-dates">
  <div class="wrap">
    <div class="sec-head">
      {label(4, L('Key dates', '重要日期', '주요 일정'), lang)}
      <h2 class="h-xl split">{lines(r(L('Never miss an|HMRC deadline.', '不再错过|HMRC 截止日期。', 'HMRC 마감일,|놓치지 마세요.'), lang))}</h2>
    </div>
    <div class="dates-grid">
      <div class="countdown" data-countdown>
        <div class="cd-num"><span class="cd-n" data-cd-days>—</span><span class="cd-u" data-cd-unit></span></div>
        <p class="cd-label"><span data-cd-until></span><br><span class="cd-what" data-cd-what></span></p>
        <ol class="dl-list" data-deadlines>
          <li>{r(L('31 January — online return and payment', '1 月 31 日——网上报税及缴税', '1월 31일 — 온라인 신고 및 납부'), lang)}</li>
          <li>{r(L('31 July — second payment on account', '7 月 31 日——第二期预缴税款', '7월 31일 — 2차 예정납부'), lang)}</li>
          <li>{r(L('5 October — register if you’re new to Self Assessment', '10 月 5 日——新报税人登记', '10월 5일 — 신규 등록'), lang)}</li>
          <li>{r(L('31 October — paper return deadline', '10 月 31 日——纸质报税截止', '10월 31일 — 서면 신고 마감'), lang)}</li>
        </ol>
      </div>
      <div class="calc-card">
        <h3>{r(L('Limited company calculator', '有限公司截止日计算器', '법인 마감일 계산기'), lang)}</h3>
        <form class="calc" data-ct-calc>
          <label for="ye">{r(L('Your financial year end', '会计年度结束日', '회계연도 종료일'), lang)}</label>
          <input type="date" id="ye" name="ye" value="2026-03-31">
        </form>
        <dl class="calc-out" data-ct-out></dl>
        <p class="fine">{r(L('For an established private company. First-year accounts have different deadlines — ask us.', '适用于已运营的私人有限公司。首年账目截止日期不同，请咨询我们。', '기존 비상장 법인 기준입니다. 첫 회계연도는 마감일이 다르니 문의해 주세요.'), lang)}</p>
      </div>
    </div>
  </div>
</section>


<section class="section cta-sec">
  <div class="wrap">
    {label(5, L('Contact', '联系我们', '문의하기'), lang)}
    <a class="giant-cta" href="contact.html">
      <span class="giant-cta-t split">{lines(r(L('Book a|consultation.', '预约|咨询。', '상담을|예약하세요.'), lang))}</span>
      <span class="giant-cta-c">{ICON['arrow-ne']}</span>
    </a>
    <div class="cta-grid">
      <div class="cta-info">
        <p class="muted">{r(L('Scan to add us on WeChat or WhatsApp, or call the office during opening hours. We speak English, 中文 and 한국어.', '扫码添加微信或 WhatsApp，或在办公时间致电办公室。我们提供中文、English 及 한국어 服务。', 'WeChat 또는 WhatsApp을 추가하거나 영업시간에 사무실로 전화하세요. 한국어, English, 中文 상담 가능.'), lang)}</p>
        <a class="big-link" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <p class="addr">{'<br>'.join(ADDRESS[1:])}</p>
      </div>
      {chat_cards(lang)}
    </div>
  </div>
</section>
"""
    return page(lang, "index.html",
                r(L("KY Accountancy — ACCA accountants in New Malden | English, 中文, 한국어",
                    "KY 会计师事务所 — 伦敦新莫尔登 ACCA 认证会计师 | 中文服务",
                    "KY Accountancy — 뉴몰든 ACCA 회계사 | 한국어 상담"), lang),
                r(L("ACCA-certified accountants in New Malden, London since 2014. Accounts, tax, VAT and payroll for sole traders, limited companies, Amazon sellers and charities — in English, Chinese and Korean.",
                    "KY 会计师事务所自 2014 年起位于伦敦新莫尔登，为自雇人士、有限公司、亚马逊卖家及慈善机构提供会计、税务、增值税及工资服务，提供中文服务。",
                    "2014년부터 런던 뉴몰든에서 자영업자, 법인, 아마존 셀러, 자선단체에 회계·세무·VAT·급여 서비스를 제공하는 ACCA 인증 회계 사무소. 한국어 상담 가능."), lang),
                body, "home")


# ---------------------------------------------------------------- services
def services(lang):
    toc = "".join(f'<li><a href="#{s["id"]}"><span>{i:02d}</span>{r(s["name"], lang)}</a></li>'
                  for i, s in enumerate(SERVICES, 1))
    sections = ""
    for i, s in enumerate(SERVICES, 1):
        items = "".join(f"<li>{ICON['check']}<span>{it}</span></li>" for it in r(s["items"], lang))
        note = ""
        if s["note"]:
            note = f'<aside class="note reveal-up"><h3>{r(s["note_title"], lang)}</h3><p>{r(s["note"], lang)}</p></aside>'
        sections += f"""
    <section class="svc-section" id="{s['id']}">
      <span class="svc-big-n" aria-hidden="true">{i:02d}</span>
      <h2 class="h-lg split">{lines(r(s['name'], lang))}</h2>
      <p class="svc-intro reveal-up">{r(s['intro'], lang)}</p>
      <h3 class="list-h">{r(L('What we do for you', '我们的服务包括', '제공 서비스'), lang)}</h3>
      <ul class="check-list">{items}</ul>
      {note}
    </section>"""
    body = page_hero(lang, 1, L('Our services', '服务项目', '서비스'),
                     L('Everything HMRC|asks of you, handled.', 'HMRC 的要求，|交给我们。', 'HMRC 업무,|저희가 처리합니다.'),
                     L('Tailored to your business goals — whether you’re starting out as a sole trader or running a growing company.',
                       '根据您的业务目标量身定制——无论您是刚起步的自雇人士，还是正在发展中的公司。',
                       '이제 막 시작한 자영업자부터 성장 중인 법인까지, 사업 목표에 맞춰 도와드립니다.')) + f"""
<div class="wrap svc-layout">
  <nav class="toc" aria-label="{r(L('Services', '服务', '서비스'), lang)}"><ul>{toc}</ul></nav>
  <div class="svc-body">{sections}
  </div>
</div>
{cta_band(lang)}"""
    return page(lang, "services.html",
                r(L("Services — limited companies, self-employed, VAT, charities & tax | KY Accountancy",
                    "服务项目 — 有限公司、自雇、增值税、慈善机构及税务 | KY 会计师事务所",
                    "서비스 — 법인, 자영업, VAT, 자선단체, 세무 | KY Accountancy"), lang),
                r(L("Accounting and tax services in New Malden: company formation, bookkeeping, payroll, VAT, Self Assessment, Amazon and EU VAT, charity independent examination and property tax.",
                    "新莫尔登会计与税务服务：公司注册、簿记、工资、增值税、个人报税、亚马逊及欧盟增值税、慈善机构独立审查及房产税务。",
                    "뉴몰든 회계·세무 서비스: 법인 설립, 기장, 급여, VAT, 종합소득세, 아마존·EU VAT, 자선단체 독립 검토, 부동산 세무."), lang),
                body)


# ---------------------------------------------------------------- about
def about(lang):
    values = [
        (L("Quality first", "专注品质", "품질 우선"),
         L("We focus fully on the quality of our professional work, tailored to your own business goals.",
           "我们专注于专业服务的品质，并根据您的业务目标量身定制。",
           "고객의 사업 목표에 맞춘 전문 서비스의 품질에 집중합니다.")),
        (L("Long-term relationships", "长期合作", "장기적인 관계"),
         L("Many of our clients have been with us for years. Good service is what we’re proudest of.",
           "许多客户与我们合作多年。优质的服务和良好的口碑是我们最引以为傲的。",
           "많은 고객이 오랫동안 함께하고 있습니다. 좋은 서비스와 평판이 저희의 자랑입니다.")),
        (L("More than bookkeeping", "不止于簿记", "기장 그 이상"),
         L("Good accounting supports your operations, brand and strategy — not just your tax return.",
           "良好的会计服务不仅仅是簿记，对企业运营、品牌、市场策略及管理同样至关重要。",
           "좋은 회계는 세금 신고뿐 아니라 운영, 브랜드, 전략에도 도움이 됩니다.")),
    ]
    vals = "".join(f'<li class="value"><span class="value-n">{i:02d}</span><h3>{r(t, lang)}</h3><p>{r(d, lang)}</p></li>'
                   for i, (t, d) in enumerate(values, 1))
    body = page_hero(lang, 1, L('About us', '关于我们', '회사 소개'),
                     L('A New Malden|firm, since 2014.', '扎根新莫尔登，|始于 2014 年。', '2014년부터|뉴몰든에서.')) + f"""
<section class="section">
  <div class="wrap">
    <p class="statement">{r(L('KY Accountancy provides a complete range of accounting services to private individuals and small to medium-sized businesses in the United Kingdom.', 'KY 会计师事务所为英国的个人及中小企业提供全面的会计服务。', 'KY Accountancy는 영국의 개인 및 중소기업에 종합 회계 서비스를 제공합니다.'), lang)}</p>
    <div class="two-col prose">
      <p class="reveal-up">{r(L('We’re based on the High Street in New Malden, home to London’s Korean community, and serve clients across London and the UK. Since 2014 we’ve grown into one of the fastest-growing accountancy firms in south-west London, built on good relationships and word of mouth.', '我们位于伦敦西南部著名的韩国城——新莫尔登（New Malden）商业街，服务遍及伦敦及全英国。自 2014 年成立以来，凭借良好的客户关系与口碑，我们已成为伦敦西南部发展最快的会计师事务所之一。', '저희는 런던 한인타운으로 잘 알려진 뉴몰든 하이 스트리트에 있으며, 런던과 영국 전역의 고객을 돕고 있습니다. 2014년 설립 이후 고객과의 신뢰와 입소문을 바탕으로 런던 남서부에서 가장 빠르게 성장하는 회계 사무소 중 하나가 되었습니다.'), lang)}</p>
      <p class="reveal-up">{r(L('Our accountants have worked across many industries, in finance departments from small businesses to multinational headquarters. We work with sole traders, limited companies, foreign-owned businesses, cross-border e-commerce sellers and charities — in English, Chinese and Korean.', '我们的会计师拥有丰富的专业经验，曾任职于不同行业、从中小企业到跨国公司总部的财务部门。我们的客户包括自雇人士、中小型有限公司、外资企业、跨境电商及慈善机构，并可用中文、英语和韩语沟通。', '저희 회계사들은 다양한 업종에서 중소기업부터 다국적 기업 본사 재무팀까지 폭넓은 경험을 쌓았습니다. 자영업자, 법인, 외국계 기업, 해외 전자상거래 셀러, 자선단체를 한국어, 영어, 중국어로 지원합니다.'), lang)}</p>
    </div>
  </div>
</section>
<section class="section values-sec">
  <div class="wrap">
    {label(2, L('What we stand for', '我们的理念', '저희의 가치'), lang)}
    <ol class="values">{vals}</ol>
  </div>
</section>
<section class="section dark acca-sec">
  <div class="wrap acca-grid">
    <div>
      {label(3, L('Professional standards', '专业资格', '전문 자격'), lang)}
      <h2 class="h-xl split">{lines(r(L('An ACCA-|certified practice.', 'ACCA 认证|会计师事务所。', 'ACCA 인증|회계 사무소.'), lang))}</h2>
    </div>
    <div>
      <p class="reveal-up">{r(L('The Association of Chartered Certified Accountants (ACCA) was founded in 1904 and is one of the UK’s chartered accountancy bodies, recognised around the world. You can check our firm on the ACCA register.', '英国皇家特许公认会计师公会（ACCA）成立于 1904 年，是英国具有皇家特许资格的会计师组织之一，享誉全球。您可在 ACCA 官网查询我们事务所的资料。', 'ACCA(국제공인회계사협회)는 1904년에 설립된 영국 왕실 인가 회계사 단체로, 전 세계적으로 인정받고 있습니다. ACCA 웹사이트에서 저희 사무소 정보를 확인하실 수 있습니다.'), lang)}</p>
      <p><a class="btn btn-gold" href="{ACCA_URL}" rel="noopener" target="_blank"><span>{r(L('View our ACCA firm details', '查看 ACCA 事务所资料', 'ACCA 사무소 정보 보기'), lang)}</span>{ICON['arrow-ne']}</a></p>
      <div class="accred-light">{accreditation_strip(lang)}</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap visit-grid">
    <div>
      {label(4, L('Visit', '到访', '방문'), lang)}
      <h2 class="h-lg split">{lines('39–41 High Street,|New Malden')}</h2>
      <p class="muted">{'<br>'.join(ADDRESS)}</p>
      <p><a class="btn btn-dark" href="{MAPS_URL}" rel="noopener" target="_blank"><span>{r(UI['directions'], lang)}</span>{ICON['arrow-ne']}</a></p>
    </div>
    <div class="visit-card">
      {status_chip(lang)}
      <dl class="kv">
        <div><dt>{r(UI['hours'], lang)}</dt><dd>{r(UI['hours_days'], lang)}<br>{r(UI['hours_time'], lang)}</dd></div>
        <div><dt>{r(L('Phone', '电话', '전화'), lang)}</dt><dd><a href="tel:{PHONE_TEL}">{PHONE_INTL}</a></dd></div>
        <div><dt>{r(UI['email'], lang)}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      </dl>
    </div>
  </div>
</section>"""
    return page(lang, "about.html",
                r(L("About us | KY Accountancy, New Malden", "关于我们 | KY 会计师事务所", "회사 소개 | KY Accountancy"), lang),
                r(L("KY Accountancy is an ACCA-certified accountancy firm on New Malden High Street, serving individuals, small businesses and charities since 2014.",
                    "KY 会计师事务所是位于新莫尔登高街的 ACCA 认证会计师事务所，自 2014 年起服务个人、中小企业及慈善机构。",
                    "KY Accountancy는 2014년부터 뉴몰든 하이 스트리트에서 개인, 중소기업, 자선단체를 돕는 ACCA 인증 회계 사무소입니다."), lang),
                body)


# ---------------------------------------------------------------- news
def news(lang):
    items = "".join(f"""
    <article class="news-item">
      <div class="news-meta"><time datetime="{n['date']}">{fmt_date(n['date'], lang)}</time><span class="tag">{r(n['tag'], lang)}</span></div>
      <div class="news-main">
        <h2>{r(n['title'], lang)}</h2>
        <p>{r(n['body'], lang)}</p>
        <a class="btn-text" href="{n['link']}" rel="noopener" target="_blank">{roll_text(r(L('Read on GOV.UK', '在 GOV.UK 阅读', 'GOV.UK에서 보기'), lang))} ↗</a>
      </div>
    </article>""" for n in NEWS)
    body = page_hero(lang, 1, L('News &amp; careers', '新闻及招聘', '소식 및 채용'),
                     L('Tax changes|worth knowing.', '值得关注的|税务新动向。', '알아두면 좋은|세무 소식.')) + f"""
<section class="section">
  <div class="wrap">
    <div class="news-list">{items}</div>
  </div>
</section>
<section class="section dark careers-sec">
  <div class="wrap careers-grid">
    <div>
      {label(2, L('Careers', '招聘', '채용'), lang)}
      <h2 class="h-xl split">{lines(r(L('Work|with us.', '加入|我们。', '함께|일해요.'), lang))}</h2>
    </div>
    <div>
      <p class="reveal-up">{r(L('We have no open vacancies right now. We’re always happy to hear from accountants who speak Chinese or Korean.', '目前暂无空缺职位。我们随时欢迎会说中文或韩语的会计人才。', '현재 채용 중인 포지션은 없습니다. 한국어 또는 중국어가 가능한 회계사의 지원은 언제나 환영합니다.'), lang)}</p>
      <a class="btn btn-gold" href="mailto:{EMAIL}?subject=CV"><span>{r(L('Send your CV', '发送简历', '이력서 보내기'), lang)}</span>{ICON['arrow']}</a>
    </div>
  </div>
</section>"""
    return page(lang, "news.html",
                r(L("News & careers | KY Accountancy", "新闻及招聘 | KY 会计师事务所", "소식 및 채용 | KY Accountancy"), lang),
                r(L("UK tax news from KY Accountancy: Making Tax Digital, Companies House identity checks, VAT penalties, and careers.",
                    "KY 会计师事务所英国税务新闻：MTD 数字化申报、Companies House 身份验证、增值税罚款及招聘信息。",
                    "KY Accountancy 영국 세무 소식: MTD, Companies House 신원 확인, VAT 가산세, 채용 정보."), lang),
                body)


# ---------------------------------------------------------------- contact
def contact(lang):
    svc_opts = "".join(f'<option>{r(s["name"], lang).replace("&amp;", "&")}</option>' for s in SERVICES)
    other = r(L("Something else", "其他", "기타"), lang)
    names = ["English", "中文", "한국어"]
    sel = {"en": 0, "zh": 1, "ko": 2}[lang]
    langs = "".join(f'<option{" selected" if i == sel else ""}>{x}</option>' for i, x in enumerate(names))
    body = page_hero(lang, 1, L('Contact us', '联系我们', '문의하기'),
                     L('Talk to an|accountant.', '与会计师|聊一聊。', '회계사와|상담하세요.'),
                     L('Call, message or visit us on New Malden High Street. We speak English, Chinese and Korean.',
                       '欢迎致电、留言或亲临新莫尔登高街办公室，我们提供中文、英语及韩语服务。',
                       '전화, 메시지, 또는 뉴몰든 하이 스트리트 사무실 방문 모두 환영합니다. 한국어, 영어, 중국어 상담 가능.')) + f"""
<section class="section">
  <div class="wrap contact-grid">
    <form class="form" data-contact-form novalidate>
      {label(2, L('Send a message', '在线留言', '메시지 보내기'), lang)}
      <div class="field"><input id="f-name" name="name" autocomplete="name" placeholder=" " required><label for="f-name">{r(L('Your name', '您的姓名', '이름'), lang)}</label></div>
      <div class="field-row">
        <div class="field"><input id="f-email" name="email" type="email" autocomplete="email" placeholder=" " required><label for="f-email">{r(L('Email', '电邮', '이메일'), lang)}</label></div>
        <div class="field"><input id="f-phone" name="phone" type="tel" autocomplete="tel" placeholder=" "><label for="f-phone">{r(L('Phone (optional)', '电话（选填）', '전화번호 (선택)'), lang)}</label></div>
      </div>
      <div class="field-row">
        <div class="field field-select"><select id="f-service" name="service">{svc_opts}<option>{other}</option></select><label for="f-service">{r(L('What can we help with?', '咨询服务', '어떤 도움이 필요하세요?'), lang)}</label></div>
        <div class="field field-select"><select id="f-lang" name="lang">{langs}</select><label for="f-lang">{r(L('Preferred language', '希望使用的语言', '희망 언어'), lang)}</label></div>
      </div>
      <div class="field"><textarea id="f-msg" name="message" rows="4" placeholder=" " required></textarea><label for="f-msg">{r(L('Tell us about your situation', '请简述您的情况', '상황을 알려주세요'), lang)}</label></div>
      <p class="form-error" data-form-error hidden>{r(L('Please fill in your name, email and message.', '请填写姓名、电邮及留言内容。', '이름, 이메일, 문의 내용을 입력해 주세요.'), lang)}</p>
      <button class="btn btn-dark btn-lg" type="submit"><span>{r(L('Send message', '发送', '보내기'), lang)}</span>{ICON['arrow']}</button>
      <p class="fine">{r(L('This opens your email app with your message ready to send to', '点击后将打开您的电邮程序，信息将发送至', '이메일 앱이 열리며 다음 주소로 메시지가 작성됩니다:'), lang)} {EMAIL}.</p>
    </form>
    <aside class="contact-side">
      <div class="visit-card">
        {status_chip(lang)}
        <dl class="kv">
          <div><dt>{r(L('Phone', '电话', '전화'), lang)}</dt><dd><a href="tel:{PHONE_TEL}">{PHONE_INTL}</a></dd></div>
          <div><dt>{r(UI['email'], lang)}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
          <div><dt>{r(UI['office'], lang)}</dt><dd><a href="{MAPS_URL}" rel="noopener" target="_blank">{'<br>'.join(ADDRESS[1:])}</a></dd></div>
          <div><dt>{r(UI['hours'], lang)}</dt><dd>{r(UI['hours_days'], lang)}<br>{r(UI['hours_time'], lang)}</dd></div>
        </dl>
      </div>
      <div id="chat">
        <h2 class="h-sm">{r(L('WeChat &amp; WhatsApp', '微信及 WhatsApp', 'WeChat · WhatsApp'), lang)}</h2>
        {chat_cards(lang)}
      </div>
    </aside>
  </div>
</section>
<section class="map-wrap" aria-label="{r(L('Map', '地图', '지도'), lang)}">
  <iframe title="Map — 39–41 High Street, New Malden KT3 3BY" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
    src="https://www.google.com/maps?q=39-41+High+Street,+New+Malden+KT3+3BY&amp;output=embed"></iframe>
</section>"""
    return page(lang, "contact.html",
                r(L("Contact | KY Accountancy, 39–41 High Street, New Malden", "联系我们 | KY 会计师事务所", "문의하기 | KY Accountancy"), lang),
                r(L("Call 020 8942 8547, email info@kyaccountancy.com or visit us at 39–41 High Street, New Malden KT3 3BY. WeChat and WhatsApp welcome.",
                    "致电 020 8942 8547、电邮 info@kyaccountancy.com，或亲临 39–41 High Street, New Malden KT3 3BY。欢迎添加微信及 WhatsApp。",
                    "전화 020 8942 8547, 이메일 info@kyaccountancy.com, 또는 39–41 High Street, New Malden KT3 3BY 방문. WeChat, WhatsApp 상담 가능."), lang),
                body)


def build():
    for lang, meta in LANGS.items():
        out = os.path.join(ROOT, meta["dir"])
        os.makedirs(out, exist_ok=True)
        for name, fn in [("index.html", home), ("services.html", services), ("about.html", about),
                         ("news.html", news), ("contact.html", contact)]:
            with open(os.path.join(out, name), "w", encoding="utf-8") as f:
                f.write(fn(lang))
    print("built", len(LANGS) * 5, "pages")


if __name__ == "__main__":
    build()
