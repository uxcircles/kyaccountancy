"""Content shared by the page templates: services, accreditations, news."""
from layout import L

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


