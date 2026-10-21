"""Page content for KY Accountancy. Run: python3 _build/pages.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from layout import (L, r, LANGS, ICON, UI, page, asset, ADDRESS, PHONE_DISPLAY, PHONE_INTL, PHONE_TEL, EMAIL,
                    WECHAT_URL, WHATSAPP_URL, ACCA_URL, MAPS_URL)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- services data
SERVICES = [
    {
        "id": "limited-company", "icon": "ltd",
        "name": L("Limited companies", "有限公司", "법인(유한회사)"),
        "short": L("Company formation, bookkeeping, payroll, VAT and year-end accounts — so you can run the business.",
                   "公司注册、簿记、工资单、增值税及年终账目，让您专心经营业务。",
                   "법인 설립, 장부 기장, 급여, VAT, 연말 결산까지 — 사업에만 집중하세요."),
        "intro": L(
            "A limited company is a separate legal entity from its shareholders, which gives you the protection of "
            "limited liability. Some customers and suppliers also prefer to deal with a company rather than a sole "
            "trader. We look after the whole compliance calendar so you can focus on growing the business.",
            "有限公司是独立于股东的法人，股东只承担有限责任——即使业务出现问题，个人资产也能得到更多保障。"
            "部分客户和供应商也更愿意与有限公司合作。我们为您打理全年的合规事务，让您专心发展业务。",
            "유한회사는 주주와 별개의 법인으로, 주주는 유한책임만 집니다. 일부 거래처는 개인사업자보다 법인과의 거래를 "
            "선호하기도 합니다. 연간 신고 일정을 저희가 모두 관리해 드리니 사업 성장에만 집중하세요.",
        ),
        "items": L(
            ["Company incorporation", "HMRC tax registrations", "Bookkeeping", "Payroll and RTI", "Workplace pensions",
             "VAT returns (Making Tax Digital)", "Corporation Tax returns (CT600)", "Year-end accounts for Companies House",
             "Confirmation statements", "Management accounts"],
            ["公司注册成立", "HMRC 各类税务登记", "簿记", "工资单及 RTI 申报", "职场养老金", "增值税申报（数字化税务 MTD）",
             "公司税申报（CT600）", "向 Companies House 递交年度账目", "公司年度信息确认声明", "管理会计报表"],
            ["법인 설립", "HMRC 세무 등록", "장부 기장", "급여 및 RTI 신고", "직장 연금", "VAT 신고 (MTD)",
             "법인세 신고 (CT600)", "Companies House 결산서 제출", "Confirmation Statement 제출", "관리회계 보고서"],
        ),
        "note_title": L("Good to know", "温馨提示", "알아두세요"),
        "note": L(
            "Private company accounts are due at Companies House 9 months after the year end. Corporation Tax is "
            "payable 9 months and 1 day after the end of the accounting period, and the CT600 return is due within "
            "12 months. Directors and people with significant control now also need to verify their identity with "
            "Companies House — we can help with that too.",
            "私人有限公司须在会计年度结束后 9 个月内向 Companies House 递交账目；公司税须在会计期结束后 9 个月零 1 天内缴纳，"
            "CT600 申报表须在 12 个月内递交。此外，公司董事及重要控制人（PSC）现须向 Companies House 完成身份验证，我们也可协助办理。",
            "비상장 법인의 결산서는 회계연도 종료 후 9개월 이내에 Companies House에 제출해야 합니다. 법인세는 회계기간 종료 후 "
            "9개월 1일 이내에 납부하고, CT600 신고서는 12개월 이내에 제출합니다. 이사 및 주요 지배주주(PSC)는 이제 "
            "Companies House 신원 확인도 필요하며, 이 절차도 도와드립니다.",
        ),
    },
    {
        "id": "self-employed", "icon": "self",
        "name": L("Self-employed &amp; sole traders", "自雇人士", "자영업자"),
        "short": L("UTR registration, bookkeeping and your Self Assessment return, filed on time.",
                   "UTR 登记、簿记及个人报税，准时递交。",
                   "UTR 등록, 장부 기장, Self Assessment 신고를 기한 내에 처리합니다."),
        "intro": L(
            "If your business is relatively simple, registering as self-employed is the easiest and most "
            "cost-effective way to start. There's no company law to worry about and no annual accounts to file — "
            "if you're not VAT-registered, your main obligation is the Self Assessment return, due by 31 January.",
            "如果您的业务比较简单，登记为自雇人士是最简便、最节省成本的方式。您无需处理公司法事务，也不必递交年度公司账目；"
            "如未登记增值税，主要只需在每年 1 月 31 日前递交个人报税表。",
            "사업 구조가 단순하다면 자영업자로 등록하는 것이 가장 간편하고 비용도 적게 듭니다. 회사법이나 연간 결산서 제출 "
            "부담이 없으며, VAT 미등록 사업자라면 매년 1월 31일까지 Self Assessment 신고만 하면 됩니다.",
        ),
        "items": L(
            ["UTR registration", "HMRC tax registrations", "Bookkeeping", "Payroll", "Workplace pensions", "VAT returns",
             "Self Assessment tax return", "Year-end financial statements", "Making Tax Digital for Income Tax", "Management accounts"],
            ["自雇 UTR 号码登记", "HMRC 各类税务登记", "簿记", "工资单", "职场养老金", "增值税申报", "个人年度报税（Self Assessment）",
             "年终财务报表", "个人所得税数字化申报（MTD）", "管理会计报表"],
            ["UTR 등록", "HMRC 세무 등록", "장부 기장", "급여 관리", "직장 연금", "VAT 신고", "Self Assessment 종합소득세 신고",
             "연말 재무제표", "소득세 MTD 디지털 신고", "관리회계 보고서"],
        ),
        "note_title": L("Making Tax Digital is here", "数字化税务（MTD）已开始实施", "MTD(디지털 세무) 시행 중"),
        "note": L(
            "Since 6 April 2026, sole traders and landlords with qualifying income over £50,000 must keep digital "
            "records and send quarterly updates to HMRC. The threshold drops to £30,000 from April 2027 and £20,000 "
            "from April 2028. We'll set you up with compatible software and file the updates for you.",
            "自 2026 年 4 月 6 日起，自雇及房东的合资格收入超过 £50,000 的，须以数字方式记账并每季度向 HMRC 提交更新。"
            "门槛将于 2027 年 4 月降至 £30,000，2028 年 4 月降至 £20,000。我们可为您设置合规软件并代为提交。",
            "2026년 4월 6일부터 적격 소득이 £50,000을 넘는 자영업자와 임대인은 디지털 장부를 작성하고 분기별로 HMRC에 "
            "보고해야 합니다. 기준 금액은 2027년 4월 £30,000, 2028년 4월 £20,000으로 낮아집니다. 호환 소프트웨어 설정과 "
            "분기 보고를 대신 처리해 드립니다.",
        ),
    },
    {
        "id": "online-sellers", "icon": "seller",
        "name": L("Amazon &amp; online sellers", "亚马逊及跨境电商", "아마존 · 온라인 셀러"),
        "short": L("UK and EU VAT registration and returns for Amazon and cross-border e-commerce.",
                   "为亚马逊及跨境电商卖家办理英国及欧盟增值税注册与申报。",
                   "아마존 및 해외 전자상거래 셀러를 위한 영국·EU VAT 등록과 신고."),
        "intro": L(
            "Selling on Amazon and other marketplaces brings VAT obligations from the very first sale. Overseas "
            "businesses that hold stock in the UK have no VAT registration threshold, and storing goods in an EU "
            "warehouse usually means registering in that country too. We register you, file the returns and keep "
            "you compliant as you expand into new markets.",
            "在亚马逊等平台销售，可能从第一笔交易起便须承担增值税义务。在英国存放库存的海外企业不设增值税登记门槛；"
            "若在欧盟国家仓库（如亚马逊 FBA）存货，通常也须在当地登记。我们为您办理登记、申报，助您在拓展新市场时保持合规。",
            "아마존 등 마켓플레이스 판매는 첫 판매부터 VAT 의무가 생길 수 있습니다. 영국에 재고를 둔 해외 사업자에게는 "
            "VAT 등록 기준 금액이 없으며, EU 창고(예: 아마존 FBA)에 재고를 보관하면 보통 해당 국가에도 등록해야 합니다. "
            "등록과 신고를 대행해 새로운 시장으로 확장할 때도 규정을 지킬 수 있도록 돕습니다.",
        ),
        "items": L(
            ["UK VAT registration", "UK VAT returns", "EU VAT registration", "EU One Stop Shop (OSS) returns",
             "Monthly or quarterly EU VAT returns", "German annual VAT return", "Management reports"],
            ["英国增值税（VAT）注册", "英国增值税申报", "欧盟国家增值税注册", "欧盟一站式申报（OSS）", "欧盟月度或季度增值税申报",
             "德国增值税年度申报", "管理会计报表"],
            ["영국 VAT 등록", "영국 VAT 신고", "EU 국가 VAT 등록", "EU OSS(One Stop Shop) 신고", "EU 월별·분기별 VAT 신고",
             "독일 연간 VAT 신고", "관리 보고서"],
        ),
        "note_title": L("Current thresholds", "现行门槛", "현행 기준 금액"),
        "note": L(
            "UK: £90,000 for UK-established businesses; no threshold for overseas sellers. EU: a single €10,000 "
            "threshold for cross-border sales to consumers across all member states, reported through the One Stop "
            "Shop. The old country-by-country distance-selling thresholds were abolished in July 2021.",
            "英国：本地企业门槛为 £90,000；海外卖家不设门槛。欧盟：面向消费者的跨境销售统一门槛为全欧盟合计 €10,000，"
            "可通过一站式申报（OSS）处理。旧有的各国远程销售门槛已于 2021 年 7 月取消。",
            "영국: 영국 내 사업자는 £90,000, 해외 셀러는 기준 금액 없음. EU: 모든 회원국 소비자 대상 국경 간 판매 합계 "
            "€10,000 단일 기준이 적용되며 OSS로 신고합니다. 국가별 원격판매 기준은 2021년 7월 폐지되었습니다.",
        ),
    },
    {
        "id": "charities", "icon": "charity",
        "name": L("Charities", "慈善机构", "자선단체"),
        "short": L("Registration, Gift Aid, payroll and independent examination for income up to £1 million.",
                   "慈善机构注册、Gift Aid、工资及独立审查（年收入 £100 万以下）。",
                   "등록, Gift Aid, 급여, 연소득 £100만 이하 독립 검토."),
        "intro": L(
            "We have extensive experience with charity accounts and can act as Independent Examiner for charities "
            "with income up to £1 million. From setting up the charitable company to the annual return at the "
            "Charity Commission, we handle the paperwork so your trustees can focus on the cause.",
            "我们在慈善机构账目方面经验丰富，可为年收入不超过 £100 万的慈善机构担任独立审查员（Independent Examiner）。"
            "从成立慈善公司到向慈善委员会递交年度申报，我们一手包办，让受托人专注于慈善事业本身。",
            "자선단체 회계 경험이 풍부하며, 연소득 £100만 이하 자선단체의 독립 검토인(Independent Examiner)을 맡을 수 "
            "있습니다. 자선 법인 설립부터 Charity Commission 연간 보고까지 처리해 이사회가 본연의 활동에 집중할 수 있도록 "
            "돕습니다.",
        ),
        "items": L(
            ["Charitable company registration at Companies House", "Charity registration with the Charity Commission",
             "HMRC charity and Gift Aid registration", "Gift Aid claims", "Bookkeeping", "Payroll and pensions",
             "Independent examination", "Accounts and confirmation statement", "Annual return to the Charity Commission",
             "Year-end financial statements"],
            ["在 Companies House 成立慈善公司", "向慈善委员会（Charity Commission）登记慈善机构编号", "HMRC 慈善机构及 Gift Aid 登记",
             "Gift Aid 退税申请", "簿记", "工资及退休金", "独立审查", "年度账目及信息确认声明", "向慈善委员会递交年度申报", "年终财务报表"],
            ["Companies House 자선 법인 등록", "Charity Commission 자선단체 등록", "HMRC 자선단체 및 Gift Aid 등록",
             "Gift Aid 환급 신청", "장부 기장", "급여 및 연금", "독립 검토", "결산서 및 Confirmation Statement",
             "Charity Commission 연간 보고", "연말 재무제표"],
        ),
        "note_title": None, "note": None,
    },
    {
        "id": "personal-tax", "icon": "tax",
        "name": L("Personal &amp; property tax", "个人及房产税务", "개인 · 부동산 세무"),
        "short": L("Income tax, landlords, Capital Gains Tax on property, refunds and tax planning.",
                   "个人所得税、房东报税、房产资本利得税、退税及税务规划。",
                   "소득세, 임대소득, 부동산 양도소득세, 세금 환급, 절세 설계."),
        "intro": L(
            "Our aim is to save you time and money. Good tax planning can reduce your liability significantly — "
            "whether you rent out a flat, are selling a property, have income from abroad or think you may have "
            "overpaid.",
            "我们的目标是为您节省时间和金钱。良好的税务规划能显著降低您的税负——无论您是出租房产、出售物业、有海外收入，"
            "还是可能多缴了税款。",
            "시간과 비용을 아껴 드리는 것이 목표입니다. 주택 임대, 부동산 매각, 해외 소득, 과다 납부 등 어떤 경우든 "
            "적절한 세무 설계로 세금 부담을 크게 줄일 수 있습니다.",
        ),
        "items": L(
            ["Income tax returns", "Rental income for landlords", "Capital Gains Tax", "60-day property CGT returns",
             "Tax refunds", "Tax credit and allowance claims", "Personal tax planning"],
            ["个人所得税申报", "房东租金收入报税", "资本利得税", "60 天内房产资本利得税申报", "各类个人退税", "申请各类税务补贴及免税额",
             "个人税务规划"],
            ["소득세 신고", "임대소득 신고", "양도소득세", "부동산 양도세 60일 신고", "세금 환급", "세액공제 및 공제 신청", "개인 절세 설계"],
        ),
        "note_title": L("Selling a UK home?", "出售英国住宅物业？", "영국 주택을 매각하시나요?"),
        "note": L(
            "If Capital Gains Tax is due on the sale of UK residential property, you must report and pay it within "
            "60 days of completion — separately from your annual tax return.",
            "出售英国住宅物业如须缴纳资本利得税，须在交易完成后 60 天内申报并缴税——这与年度报税是分开的。",
            "영국 주거용 부동산 매각으로 양도소득세가 발생하면, 연간 신고와 별도로 거래 완료 후 60일 이내에 신고·납부해야 "
            "합니다.",
        ),
    },
]

ACCREDITATIONS = [
    ("acca.jpg", "ACCA", 64, 62), ("aat.jpg", "AAT Licensed Accountant", 146, 40),
    ("cisi.jpg", "CISI — Chartered Institute for Securities &amp; Investment", 95, 50),
    ("aia.png", "AIA — Member in Practice", 92, 55),
]


def accreditation_strip(lang):
    a = asset(lang)
    imgs = "".join(f'<li><img src="{a}img/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></li>'
                   for f, alt, w, h in ACCREDITATIONS)
    return f'<ul class="accred">{imgs}</ul>'


def chat_cards(lang):
    a = asset(lang)
    return f"""<div class="chat-cards">
  <figure class="qr">
    <img src="{a}img/qr-wechat.png" alt="WeChat QR code — KY Accountancy" width="180" height="180" loading="lazy">
    <figcaption><strong>{r(L('WeChat', '微信', 'WeChat'), lang)}</strong><a href="{WECHAT_URL}" rel="noopener" target="_blank">{r(L('Open in WeChat', '在微信中打开', 'WeChat에서 열기'), lang)} ↗</a></figcaption>
  </figure>
  <figure class="qr">
    <img src="{a}img/qr-whatsapp.png" alt="WhatsApp QR code — KY Accountancy" width="180" height="175" loading="lazy">
    <figcaption><strong>WhatsApp</strong><a href="{WHATSAPP_URL}" rel="noopener" target="_blank">{r(L('Open in WhatsApp', '在 WhatsApp 中打开', 'WhatsApp에서 열기'), lang)} ↗</a></figcaption>
  </figure>
</div>"""


def office_card(lang, deadline=True):
    addr = "<br>".join(r(ADDRESS, lang)[1:])
    dl = ""
    if deadline:
        dl = f"""<div class="card-deadline" data-next-deadline hidden>
      <span class="eyebrow">{r(L('Next HMRC deadline', '下一个 HMRC 截止日期', '다음 HMRC 마감일'), lang)}</span>
      <strong data-dl-date></strong><span data-dl-label></span><span class="pill" data-dl-in></span>
    </div>"""
    return f"""<aside class="office-card">
    <div class="status" data-open-status><span class="dot"></span><span data-status-text>{r(UI['hours_days'], lang)} · {r(UI['hours_time'], lang)}</span></div>
    <ul class="office-list">
      <li>{ICON['phone']}<a href="tel:{PHONE_TEL}">{PHONE_INTL}</a></li>
      <li>{ICON['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{ICON['pin']}<a href="{MAPS_URL}" rel="noopener" target="_blank">{addr}</a></li>
    </ul>
    {dl}
  </aside>"""


# ---------------------------------------------------------------- home
def home(lang):
    cards = "".join(f"""
      <a class="svc-card" href="services.html#{s['id']}">
        <span class="svc-icon">{ICON[s['icon']]}</span>
        <h3>{r(s['name'], lang)}</h3>
        <p>{r(s['short'], lang)}</p>
        <span class="more">{r(L('Learn more', '了解详情', '자세히 보기'), lang)} {ICON['arrow']}</span>
      </a>""" for s in SERVICES)

    steps = [
        (L("Get in touch", "联系我们", "문의하기"),
         L("Call, email, or message us on WeChat or WhatsApp in English, Chinese or Korean.",
           "通过电话、电邮、微信或 WhatsApp 联系我们，可使用中文、英语或韩语。",
           "전화, 이메일, WeChat, WhatsApp으로 한국어·영어·중국어로 편하게 문의하세요.")),
        (L("We agree the scope", "确定服务内容", "업무 범위 확정"),
         L("We look at your situation, explain what HMRC and Companies House need from you, and agree what we'll handle.",
           "我们了解您的情况，说明 HMRC 和 Companies House 的要求，并与您确认由我们负责的事项。",
           "상황을 살펴보고 HMRC와 Companies House가 요구하는 사항을 설명한 뒤, 저희가 맡을 업무를 함께 정합니다.")),
        (L("We keep you on track", "按时完成申报", "기한 관리"),
         L("We prepare and file your returns, and remind you before every deadline so there are no penalties.",
           "我们为您准备并递交各类申报，并在每个截止日期前提醒您，避免罚款。",
           "신고서를 준비·제출하고 마감 전에 미리 알려드려 가산세 걱정이 없도록 합니다.")),
    ]
    steps_html = "".join(f'<li><span class="step-n">{i}</span><h3>{r(t, lang)}</h3><p>{r(d, lang)}</p></li>'
                         for i, (t, d) in enumerate(steps, 1))

    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="eyebrow eyebrow-gold">{r(L('Accountants on New Malden High Street · since 2014', '新莫尔登高街会计师事务所 · 始于 2014 年', '뉴몰든 하이 스트리트 회계 사무소 · 2014년 설립'), lang)}</p>
      <h1>{r(L('Your accounts and tax, explained in <em>your</em> language.', '会计与税务，<em>用您的语言</em>讲清楚。', '회계와 세무, <em>모국어로</em> 편하게 상담하세요.'), lang)}</h1>
      <p class="lead">{r(L('ACCA-certified accountants for sole traders, limited companies, online sellers, landlords and charities — working with you in English, 中文 and 한국어.', 'ACCA 认证会计师，为自雇人士、有限公司、跨境电商、房东及慈善机构提供服务——可用中文、English 及 한국어 沟通。', '자영업자, 법인, 온라인 셀러, 임대인, 자선단체를 위한 ACCA 인증 회계사 — 한국어, English, 中文으로 상담합니다.'), lang)}</p>
      <div class="hero-cta">
        <a class="btn btn-gold" href="contact.html">{r(L('Book a consultation', '预约咨询', '상담 예약'), lang)}</a>
        <a class="btn btn-ghost-light" href="services.html">{r(L('Our services', '服务项目', '서비스 보기'), lang)}</a>
      </div>
      <ul class="hero-facts">
        <li><strong>2014</strong><span>{r(L('Established', '成立年份', '설립'), lang)}</span></li>
        <li><strong>ACCA</strong><span>{r(L('Certified firm', '认证事务所', '인증 사무소'), lang)}</span></li>
        <li><strong>3</strong><span>{r(L('Languages', '种服务语言', '개 언어 상담'), lang)}</span></li>
      </ul>
    </div>
    {office_card(lang)}
  </div>
</section>

<section class="band band-accred" aria-label="{r(L('Professional memberships', '专业资格', '전문 자격'), lang)}">
  <div class="wrap">{accreditation_strip(lang)}</div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{r(L('What we do', '服务范围', '서비스 분야'), lang)}</p>
      <h2>{r(L('Complete accounting for individuals and small businesses', '为个人及中小企业提供全面的会计服务', '개인과 중소기업을 위한 종합 회계 서비스'), lang)}</h2>
    </div>
    <div class="svc-grid">{cards}
      <a class="svc-card svc-card-cta" href="contact.html">
        <h3>{r(L('Not sure what you need?', '不确定需要哪项服务？', '어떤 서비스가 필요한지 모르겠다면?'), lang)}</h3>
        <p>{r(L('Tell us about your situation and we’ll point you in the right direction.', '告诉我们您的情况，我们为您指引方向。', '상황을 알려주시면 알맞은 방법을 안내해 드립니다.'), lang)}</p>
        <span class="more">{r(L('Ask us', '咨询我们', '문의하기'), lang)} {ICON['arrow']}</span>
      </a>
    </div>
  </div>
</section>

<section class="section section-tint">
  <div class="wrap split">
    <div>
      <p class="eyebrow">{r(L('How we work', '合作流程', '진행 방식'), lang)}</p>
      <h2>{r(L('Straightforward from the first call', '从第一次沟通开始，简单清晰', '첫 상담부터 명확하게'), lang)}</h2>
      <p class="muted-lead">{r(L('Our accountants have worked in finance teams from small businesses to multinational headquarters. We bring that experience to every client, whatever their size.', '我们的会计师曾任职于各行各业，从中小企业到跨国公司总部财务部门，经验丰富，无论客户规模大小都同样用心。', '저희 회계사들은 중소기업부터 다국적 기업 본사 재무팀까지 다양한 경험을 갖추고 있으며, 규모와 상관없이 모든 고객에게 그 경험을 제공합니다.'), lang)}</p>
    </div>
    <ol class="steps">{steps_html}</ol>
  </div>
</section>

<section class="section" id="key-dates">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{r(L('Key dates', '重要日期', '주요 일정'), lang)}</p>
      <h2>{r(L('Never miss an HMRC deadline', '不再错过 HMRC 截止日期', 'HMRC 마감일을 놓치지 마세요'), lang)}</h2>
    </div>
    <div class="dates-grid">
      <div class="panel">
        <h3>{r(L('Self Assessment', '个人报税（Self Assessment）', 'Self Assessment (종합소득세)'), lang)}</h3>
        <ol class="deadlines" data-deadlines>
          <li class="deadline-fallback">{r(L('31 January — online return and payment', '1 月 31 日——网上报税及缴税', '1월 31일 — 온라인 신고 및 납부'), lang)}</li>
          <li class="deadline-fallback">{r(L('31 July — second payment on account', '7 月 31 日——第二期预缴税款', '7월 31일 — 2차 예정납부'), lang)}</li>
          <li class="deadline-fallback">{r(L('5 October — register if you’re new to Self Assessment', '10 月 5 日——新报税人登记', '10월 5일 — 신규 등록'), lang)}</li>
        </ol>
      </div>
      <div class="panel">
        <h3>{r(L('Limited company dates', '有限公司截止日期', '법인 마감일 계산'), lang)}</h3>
        <form class="calc" data-ct-calc>
          <label for="ye">{r(L('Your company’s financial year end', '公司会计年度结束日', '회사 회계연도 종료일'), lang)}</label>
          <input type="date" id="ye" name="ye" value="2026-03-31">
        </form>
        <dl class="calc-out" data-ct-out></dl>
        <p class="fine">{r(L('For an established private company. First-year accounts have different deadlines — ask us.', '适用于已运营的私人有限公司。首年账目截止日期不同，请咨询我们。', '기존 비상장 법인 기준입니다. 첫 회계연도는 마감일이 다르니 문의해 주세요.'), lang)}</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-navy">
  <div class="wrap split split-center">
    <div>
      <p class="eyebrow eyebrow-gold">{r(UI['languages'], lang)}</p>
      <h2>{r(L('Message us the way you already do', '用您习惯的方式联系我们', '익숙한 방법으로 연락하세요'), lang)}</h2>
      <p class="lead">{r(L('Scan to add us on WeChat or WhatsApp, or call the office during opening hours. We reply as soon as we can.', '扫码添加我们的微信或 WhatsApp，或在办公时间致电办公室，我们会尽快回复您。', 'WeChat 또는 WhatsApp QR을 스캔하거나 영업시간에 사무실로 전화하세요. 최대한 빨리 답변드립니다.'), lang)}</p>
      <div class="hero-cta">
        <a class="btn btn-gold" href="tel:{PHONE_TEL}">{ICON['phone']} {PHONE_DISPLAY}</a>
        <a class="btn btn-ghost-light" href="contact.html">{r(L('Send a message', '在线留言', '메시지 보내기'), lang)}</a>
      </div>
    </div>
    {chat_cards(lang)}
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
    toc = "".join(f'<li><a href="#{s["id"]}">{r(s["name"], lang)}</a></li>' for s in SERVICES)
    sections = ""
    for s in SERVICES:
        items = "".join(f"<li>{ICON['check']}<span>{i}</span></li>" for i in r(s["items"], lang))
        note = ""
        if s["note"]:
            note = f'<div class="note"><h3>{r(s["note_title"], lang)}</h3><p>{r(s["note"], lang)}</p></div>'
        sections += f"""
    <section class="svc-section" id="{s['id']}">
      <div class="svc-section-head"><span class="svc-icon">{ICON[s['icon']]}</span><h2>{r(s['name'], lang)}</h2></div>
      <p class="svc-intro">{r(s['intro'], lang)}</p>
      <h3 class="list-h">{r(L('What we do for you', '我们的服务包括', '제공 서비스'), lang)}</h3>
      <ul class="check-list">{items}</ul>
      {note}
    </section>"""
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow eyebrow-gold">{r(L('Our services', '服务项目', '서비스'), lang)}</p>
    <h1>{r(L('Everything HMRC and Companies House ask of you, handled', 'HMRC 与 Companies House 的各项要求，交给我们', 'HMRC와 Companies House 업무를 맡겨 주세요'), lang)}</h1>
    <p class="lead">{r(L('Tailored to your business goals — whether you’re starting out as a sole trader or running a growing company.', '根据您的业务目标量身定制——无论您是刚起步的自雇人士，还是正在发展中的公司。', '이제 막 시작한 자영업자부터 성장 중인 법인까지, 사업 목표에 맞춰 도와드립니다.'), lang)}</p>
  </div>
</section>
<div class="wrap svc-layout">
  <nav class="toc" aria-label="{r(L('Services', '服务', '서비스'), lang)}"><ul>{toc}</ul>
    <a class="btn btn-navy btn-block" href="contact.html">{r(L('Ask about a service', '咨询服务', '서비스 문의'), lang)}</a></nav>
  <div class="svc-body">{sections}
  </div>
</div>
<section class="cta-band">
  <div class="wrap cta-inner">
    <h2>{r(L('Questions about your situation?', '对您的情况有疑问？', '궁금한 점이 있으신가요?'), lang)}</h2>
    <div class="hero-cta"><a class="btn btn-gold" href="contact.html">{r(L('Contact us', '联系我们', '문의하기'), lang)}</a>
    <a class="btn btn-ghost-light" href="tel:{PHONE_TEL}">{ICON['phone']} {PHONE_DISPLAY}</a></div>
  </div>
</section>"""
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
    a = asset(lang)
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
    vals = "".join(f'<li><h3>{r(t, lang)}</h3><p>{r(d, lang)}</p></li>' for t, d in values)
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow eyebrow-gold">{r(L('About us', '关于我们', '회사 소개'), lang)}</p>
    <h1>{r(L('A New Malden accountancy firm, since 2014', '扎根新莫尔登的会计师事务所，始于 2014 年', '2014년부터 뉴몰든을 지켜온 회계 사무소'), lang)}</h1>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="prose">
      <p class="lead-dark">{r(L('KY Accountancy provides a complete range of accounting services to private individuals and small to medium-sized businesses in the United Kingdom.', 'KY 会计师事务所为英国的个人及中小企业提供全面的会计服务。', 'KY Accountancy는 영국의 개인 및 중소기업에 종합 회계 서비스를 제공합니다.'), lang)}</p>
      <p>{r(L('We’re based on the High Street in New Malden, home to London’s Korean community, and serve clients across London and the UK. Since 2014 we’ve grown into one of the fastest-growing accountancy firms in south-west London, built on good relationships and word of mouth.', '我们位于伦敦西南部著名的韩国城——新莫尔登（New Malden）商业街，服务遍及伦敦及全英国。自 2014 年成立以来，凭借良好的客户关系与口碑，我们已成为伦敦西南部发展最快的会计师事务所之一。', '저희는 런던 한인타운으로 잘 알려진 뉴몰든 하이 스트리트에 있으며, 런던과 영국 전역의 고객을 돕고 있습니다. 2014년 설립 이후 고객과의 신뢰와 입소문을 바탕으로 런던 남서부에서 가장 빠르게 성장하는 회계 사무소 중 하나가 되었습니다.'), lang)}</p>
      <p>{r(L('Our accountants have worked across many industries, in finance departments from small businesses to multinational headquarters. We work with sole traders, limited companies, foreign-owned businesses, cross-border e-commerce sellers and charities — in English, Chinese and Korean.', '我们的会计师拥有丰富的专业经验，曾任职于不同行业、从中小企业到跨国公司总部的财务部门。我们的客户包括自雇人士、中小型有限公司、外资企业、跨境电商及慈善机构，并可用中文、英语和韩语沟通。', '저희 회계사들은 다양한 업종에서 중소기업부터 다국적 기업 본사 재무팀까지 폭넓은 경험을 쌓았습니다. 자영업자, 법인, 외국계 기업, 해외 전자상거래 셀러, 자선단체를 한국어, 영어, 중국어로 지원합니다.'), lang)}</p>
    </div>
    <ul class="values">{vals}</ul>
  </div>
</section>
<section class="section section-tint">
  <div class="wrap split split-center">
    <div class="prose">
      <p class="eyebrow">{r(L('Professional standards', '专业资格', '전문 자격'), lang)}</p>
      <h2>{r(L('An ACCA-certified practice', 'ACCA 认证会计师事务所', 'ACCA 인증 회계 사무소'), lang)}</h2>
      <p>{r(L('The Association of Chartered Certified Accountants (ACCA) was founded in 1904 and is one of the UK’s chartered accountancy bodies, recognised around the world. You can check our firm on the ACCA register.', '英国皇家特许公认会计师公会（ACCA）成立于 1904 年，是英国具有皇家特许资格的会计师组织之一，享誉全球。您可在 ACCA 官网查询我们事务所的资料。', 'ACCA(국제공인회계사협회)는 1904년에 설립된 영국 왕실 인가 회계사 단체로, 전 세계적으로 인정받고 있습니다. ACCA 웹사이트에서 저희 사무소 정보를 확인하실 수 있습니다.'), lang)}</p>
      <p><a class="link-arrow" href="{ACCA_URL}" rel="noopener" target="_blank">{r(L('View our ACCA firm details', '查看 ACCA 事务所资料', 'ACCA 사무소 정보 보기'), lang)} {ICON['ext']}</a></p>
    </div>
    <div class="accred-panel">{accreditation_strip(lang)}</div>
  </div>
</section>
<section class="section">
  <div class="wrap split split-center">
    <div class="prose">
      <h2>{r(L('Visit the office', '欢迎莅临', '사무실 방문'), lang)}</h2>
      <p>{"<br>".join(r(ADDRESS, lang))}</p>
      <div class="hero-cta"><a class="btn btn-navy" href="contact.html">{r(L('Contact us', '联系我们', '문의하기'), lang)}</a>
      <a class="btn btn-outline" href="{MAPS_URL}" rel="noopener" target="_blank">{r(UI['directions'], lang)}</a></div>
    </div>
    {office_card(lang, deadline=False)}
  </div>
</section>"""
    return page(lang, "about.html",
                r(L("About us | KY Accountancy, New Malden", "关于我们 | KY 会计师事务所", "회사 소개 | KY Accountancy"), lang),
                r(L("KY Accountancy is an ACCA-certified accountancy firm on New Malden High Street, serving individuals, small businesses and charities since 2014.",
                    "KY 会计师事务所是位于新莫尔登高街的 ACCA 认证会计师事务所，自 2014 年起服务个人、中小企业及慈善机构。",
                    "KY Accountancy는 2014년부터 뉴몰든 하이 스트리트에서 개인, 중소기업, 자선단체를 돕는 ACCA 인증 회계 사무소입니다."), lang),
                body)


# ---------------------------------------------------------------- news
NEWS = [
    {
        "date": "2026-04-06", "tag": L("Self Assessment", "个人报税", "종합소득세"),
        "title": L("Making Tax Digital for Income Tax has started",
                   "个人所得税数字化申报（MTD）正式实施",
                   "소득세 MTD(디지털 세무) 시행"),
        "body": L("From 6 April 2026, sole traders and landlords with qualifying income over £50,000 must keep digital records and send HMRC quarterly updates. The threshold falls to £30,000 in April 2027 and £20,000 in April 2028. Talk to us about getting set up.",
                  "自 2026 年 4 月 6 日起，合资格收入超过 £50,000 的自雇人士及房东须以数字方式记账，并每季度向 HMRC 提交更新。门槛将于 2027 年 4 月降至 £30,000，2028 年 4 月降至 £20,000。欢迎联系我们协助设置。",
                  "2026년 4월 6일부터 적격 소득이 £50,000을 넘는 자영업자와 임대인은 디지털 장부를 작성하고 분기별로 HMRC에 보고해야 합니다. 기준은 2027년 4월 £30,000, 2028년 4월 £20,000으로 낮아집니다. 준비가 필요하시면 문의해 주세요."),
        "link": "https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax",
    },
    {
        "date": "2025-11-18", "tag": L("Limited companies", "有限公司", "법인"),
        "title": L("Companies House identity verification for directors",
                   "Companies House 董事身份验证",
                   "Companies House 이사 신원 확인"),
        "body": L("New directors and people with significant control must now verify their identity with Companies House. Existing directors verify when the company files its next confirmation statement. We can guide you through it.",
                  "新任董事及重要控制人（PSC）现须向 Companies House 完成身份验证；现任董事须在公司下一次递交信息确认声明时完成验证。我们可协助您办理。",
                  "신규 이사 및 주요 지배주주(PSC)는 이제 Companies House에서 신원 확인을 받아야 하며, 기존 이사는 다음 Confirmation Statement 제출 시 확인합니다. 절차를 안내해 드립니다."),
        "link": "https://www.gov.uk/guidance/verifying-your-identity-for-companies-house",
    },
    {
        "date": "2023-01-01", "tag": L("VAT", "增值税", "VAT"),
        "title": L("HMRC’s points-based VAT penalties and interest",
                   "HMRC 增值税积分制罚款及利息",
                   "HMRC VAT 벌점제 가산세 및 이자"),
        "body": L("Late VAT returns now earn penalty points, with a £200 fine once you reach the threshold, and late payments attract separate penalties and interest. Filing and paying on time matters more than ever.",
                  "逾期递交增值税申报将被记罚分，累积达到上限后罚款 £200；逾期缴税另有罚款及利息。按时申报和缴税比以往更重要。",
                  "VAT 신고가 늦어지면 벌점이 쌓이고 기준에 도달하면 £200의 벌금이 부과되며, 납부 지연에는 별도의 가산세와 이자가 붙습니다. 기한 내 신고·납부가 그 어느 때보다 중요합니다."),
        "link": "https://www.gov.uk/government/news/hmrc-reminds-businesses-about-new-vat-penalties-and-interest-payments",
    },
]


def fmt_date(d, lang):
    y, m, dd = d.split("-")
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    if lang == "zh":
        return f"{y} 年 {int(m)} 月 {int(dd)} 日"
    if lang == "ko":
        return f"{y}년 {int(m)}월 {int(dd)}일"
    return f"{int(dd)} {months[int(m) - 1]} {y}"


def news(lang):
    items = "".join(f"""
    <article class="news-item">
      <div class="news-meta"><span class="tag">{r(n['tag'], lang)}</span><time datetime="{n['date']}">{fmt_date(n['date'], lang)}</time></div>
      <h2>{r(n['title'], lang)}</h2>
      <p>{r(n['body'], lang)}</p>
      <a class="link-arrow" href="{n['link']}" rel="noopener" target="_blank">{r(L('Read on GOV.UK', '在 GOV.UK 阅读', 'GOV.UK에서 보기'), lang)} {ICON['ext']}</a>
    </article>""" for n in NEWS)
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow eyebrow-gold">{r(L('News &amp; careers', '新闻及招聘', '소식 및 채용'), lang)}</p>
    <h1>{r(L('Tax changes worth knowing about', '值得关注的税务新动向', '알아두면 좋은 세무 소식'), lang)}</h1>
  </div>
</section>
<section class="section">
  <div class="wrap news-layout">
    <div class="news-list">{items}</div>
    <aside class="panel careers">
      <p class="eyebrow">{r(L('Careers', '招聘', '채용'), lang)}</p>
      <h2>{r(L('Work with us', '加入我们', '함께 일해요'), lang)}</h2>
      <p>{r(L('We have no open vacancies right now. We’re always happy to hear from accountants who speak Chinese or Korean — send your CV to', '目前暂无空缺职位。我们随时欢迎会说中文或韩语的会计人才，请将简历发送至', '현재 채용 중인 포지션은 없습니다. 한국어 또는 중국어가 가능한 회계사의 지원은 언제나 환영합니다. 이력서를 보내 주세요:'), lang)} <a href="mailto:{EMAIL}?subject=CV">{EMAIL}</a>.</p>
    </aside>
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
    langs = "".join(f"<option>{x}</option>" for x in ["English", "中文", "한국어"])
    default_lang = {"en": 0, "zh": 1, "ko": 2}[lang]
    langs = langs.replace(f"<option>{['English', '中文', '한국어'][default_lang]}</option>",
                          f"<option selected>{['English', '中文', '한국어'][default_lang]}</option>")
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow eyebrow-gold">{r(L('Contact us', '联系我们', '문의하기'), lang)}</p>
    <h1>{r(L('Talk to an accountant', '与会计师聊一聊', '회계사와 상담하세요'), lang)}</h1>
    <p class="lead">{r(L('Call, message or visit us on New Malden High Street. We speak English, Chinese and Korean.', '欢迎致电、留言或亲临新莫尔登高街办公室，我们提供中文、英语及韩语服务。', '전화, 메시지, 또는 뉴몰든 하이 스트리트 사무실 방문 모두 환영합니다. 한국어, 영어, 중국어 상담 가능.'), lang)}</p>
  </div>
</section>
<section class="section">
  <div class="wrap contact-grid">
    <form class="panel form" data-contact-form novalidate>
      <h2>{r(L('Send us a message', '在线留言', '메시지 보내기'), lang)}</h2>
      <div class="field"><label for="f-name">{r(L('Name', '姓名', '이름'), lang)}</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field-row">
        <div class="field"><label for="f-email">{r(L('Email', '电邮', '이메일'), lang)}</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="f-phone">{r(L('Phone (optional)', '电话（选填）', '전화번호 (선택)'), lang)}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="f-service">{r(L('What can we help with?', '咨询服务', '어떤 도움이 필요하세요?'), lang)}</label><select id="f-service" name="service">{svc_opts}<option>{other}</option></select></div>
        <div class="field"><label for="f-lang">{r(L('Preferred language', '希望使用的语言', '희망 언어'), lang)}</label><select id="f-lang" name="lang">{langs}</select></div>
      </div>
      <div class="field"><label for="f-msg">{r(L('Message', '留言内容', '문의 내용'), lang)}</label><textarea id="f-msg" name="message" rows="5" required></textarea></div>
      <p class="form-error" data-form-error hidden>{r(L('Please fill in your name, email and message.', '请填写姓名、电邮及留言内容。', '이름, 이메일, 문의 내용을 입력해 주세요.'), lang)}</p>
      <button class="btn btn-navy" type="submit">{r(L('Send message', '发送', '보내기'), lang)}</button>
      <p class="fine">{r(L('This opens your email app with your message ready to send to', '点击后将打开您的电邮程序，信息将发送至', '이메일 앱이 열리며 다음 주소로 메시지가 작성됩니다:'), lang)} {EMAIL}.</p>
    </form>
    <div class="contact-side">
      {office_card(lang, deadline=False)}
      <div class="panel" id="chat">
        <h2 class="h-sm">{r(L('WeChat &amp; WhatsApp', '微信及 WhatsApp', 'WeChat · WhatsApp'), lang)}</h2>
        {chat_cards(lang)}
      </div>
    </div>
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
