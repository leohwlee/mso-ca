# Figures for the Guideline Chapters 8 and 9 page: what records are for, training by
# role along the reporting line, and the training cycle from hiring to refresher.
from ui import *


def cc(*cs):
    """Join several citations into one (en, tc) pair."""
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


def mlab(x, y, en, tc, anchor='middle', pitch=17):
    """Edge label like ui.mlabel, but with room between the stacked English and Chinese
    lines so the Chinese line's halo does not erase the English descenders."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        n = len(ls)
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (n - 1 - i) * pitch:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


# ---------------------------------------------------------------- 1. what records are for
def fig_uses():
    W = 1000
    R = Card(30, 270, ("Your records", "你的紀錄"),
             ("CDD information, transaction records and other records: what the statutory and regulatory requirements need, appropriate to the nature, size and complexity of your business",
              "盡職審查資料、交易紀錄及其他紀錄：足以符合法定及監管規定，並切合你的業務性質、規模及複雜程度"),
             'plain', "¶8.2")
    M1 = Card(380, 590, ("A clear and complete audit trail", "清晰及完備的審計線索"),
              ("For funds moving through you that relate to any customer and, where appropriate, the beneficial owner of the customer, account or transaction",
               "經由你提存、與任何客戶及（如適用）客戶的實益擁有人有關的資金、戶口或交易"), 'must', "¶8.2(a)")
    M2 = Card(380, 590, ("Swift access, on appropriate authority", "迅速提供予有適當授權者"),
              ("All CDD information and transaction records reach the Commissioner, other authorities and auditors swiftly",
               "所有盡職審查資料及交易紀錄，迅速提供予有適當授權的關長、其他機構及核數師"), 'must', "¶8.2(b)")
    M3 = Card(380, 590, ("Proof that you comply", "證明你合規"),
              ("You can demonstrate compliance with the AMLO, the rest of the Guideline, and the Commissioner's other guidelines and guidance",
               "你能證明符合《打擊洗錢條例》、本指引其他章節，以及關長發出的其他指引"), 'must', "¶8.1, 8.2(c)")
    F1 = Card(380, 590, ("Investigating authorities", "調查當局"),
              ("Establish a suspect's financial profile and trace criminal or terrorist property or funds: the audit trail for detection, investigation and confiscation",
               "確定疑犯的財政狀況，追查罪犯或恐怖分子的財產或資金：用於偵察、調查及沒收的審計線索"), 'faint', "¶8.1")
    F2 = Card(380, 590, ("The Court", "法院"),
              ("Examines all relevant past transactions to assess whether property or funds are the proceeds of, or relate to, criminal or terrorist offences",
               "審查所有相關的過往交易，以評估有關財產或資金是否刑事或恐怖分子罪行的收益，或是否與該等罪行有關連"), 'faint', "¶8.1")
    right = [M1, M2, M3, F1, F2]
    H = place([([M1], 14), ([M2], 14), ([M3], 30), ([F1], 14), ([F2], 0)], y0=14)
    R.y = (M1.y + F2.y + F2.h) / 2 - R.h / 2
    b = [n.render() for n in [R] + right]
    m = 'g8u'
    tx = 340
    b.append(f'<line class="e" x1="{R.x + R.w}" y1="{R.cy:.0f}" x2="{tx}" y2="{R.cy:.0f}"/>')
    b.append(f'<line class="e" x1="{tx}" y1="{M1.cy:.0f}" x2="{tx}" y2="{F2.cy:.0f}"/>')
    for n in right:
        b.append(edge([(tx, n.cy), n.left], mid=m))
    aria = ("What records are for. Your records, meaning CDD information, transaction records and other records suited to your business, should give a clear and complete audit trail of funds moving through you, be available swiftly to the Commissioner, other authorities and auditors on appropriate authority, and let you demonstrate compliance. They also let investigating authorities build a suspect's financial profile and trace property, and let the Court examine past transactions.",
            "紀錄的用途。你的紀錄，即切合業務的盡職審查資料、交易紀錄及其他紀錄，應提供經由你提存的資金的清晰及完備審計線索，迅速提供予有適當授權的關長、其他機構及核數師，並讓你證明合規。紀錄亦讓調查當局確定疑犯的財政狀況及追查財產，並協助法院審查過往交易。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


USES_KEY = legend([('', ("your records", "你的紀錄")),
                   ('must', ("what you should make sure they do", "你應確保紀錄做到的事")),
                   ('faint', ("who else relies on them", "還有誰依賴這些紀錄"))])


# ---------------------------------------------------------------- 2. training by role
def fig_roles():
    W = 1000
    ALL = Card(40, 920, ("Every member of staff, whatever the role", "每一名職員，不論職位"),
               ("Should be made aware of the five points in the table below: the firm's and their own statutory obligations under the AMLO and five other ordinances and what a breach can cost, your AML/CFT policies and procedures, and new ML/TF methods they need for their role",
                "應促使他們留意下表五項：你和他們本身在《打擊洗錢條例》及另外五條條例下的法定責任及違反的後果、你在打擊洗錢方面的政策及程序，以及履行其職責所需的洗錢／恐怖分子資金籌集新手法"),
               'must', "¶9.4")
    NEW = Card(40, 920, ("Every new joiner, whatever their seniority", "所有新職員，不論資歷"),
               ("An introduction to the background to ML/TF and the importance you place on it; the need to identify suspicious transactions and report them to the MLRO; and the offence of tipping off",
                "洗錢／恐怖分子資金籌集的背景，以及你對此問題的重視的簡介；識別可疑交易並向洗錢報告主任舉報的必要；以及「通風報訊」的罪行"),
               'plain', "¶9.5(a)")
    FL = Card(40, 320, ("Staff dealing directly with the public, such as front-line staff", "與公眾有直接接觸的職員（例如前線人員）"),
              ("The importance of their role in your ML/TF strategy as the first point of contact with potential money launderers; the CDD and record-keeping policies relevant to their job; the circumstances that may give rise to suspicion, the lines of reporting, and when extra vigilance may be needed",
               "在你的洗錢／恐怖分子資金籌集策略中，他們作為與潛在洗錢人第一個接觸點的重要性；與其職責相關的客戶盡職審查及備存紀錄政策及程序；可能引起懷疑的情況及相關政策及程序，例如報告的流程及應何時提高警覺"),
              'plain', "¶9.5(b)")
    BO = Card(375, 235, ("Back-office staff, depending on their roles", "後勤職員（視乎他們的職責）"),
              ("Customer verification and the related processing procedures; recognising unusual activity, including abnormal settlements, payments or delivery instructions",
               "客戶核實及相關處理程序；如何識別不尋常活動，包括不正常的結算、付款及交付指示"),
              'plain', "¶9.5(c)")
    ML = Card(120, 440, ("The MLRO", "洗錢報告主任"),
              ("Assessing the suspicious transaction reports staff submit, and reporting suspicious transactions to the JFIU; keeping abreast of AML/CFT requirements and developments generally",
               "評估所收到的可疑交易報告，並向財富情報組舉報可疑交易；掌握打擊洗錢／恐怖分子資金籌集的一般規定及發展"),
              'plain', "¶9.5(e)")
    JF = Card(230, 220, ("The JFIU", "財富情報組"), ("Receives the suspicious transaction reports", "接收可疑交易報告"), 'faint')
    MG = Card(625, 335, ("Managerial staff, including internal audit officers and compliance officers", "經理級人員包括內部審計人員及合規主任"),
              ("Higher-level training on every aspect of your AML/CFT regime; and specific training on their duties to supervise or manage staff, audit the system, perform random checks, and report suspicious transactions to the JFIU",
               "更高層次的培訓，涵蓋你打擊洗錢制度的各方面；以及涵蓋監督或管理職員、系統審查、進行隨機抽查，以及向財富情報組舉報可疑交易的職責的特定培訓"),
              'plain', "¶9.5(d)")
    ALL.y = 14
    NEW.y = ALL.y + ALL.h + 16
    y2 = NEW.y + NEW.h + 34
    for n in (FL, BO, MG):
        n.y = y2
    bus = y2 + max(FL.h, BO.h, MG.h) + 22
    ML.y = bus + 56
    JF.y = ML.y + ML.h + 56
    H = JF.y + JF.h
    b = [n.render() for n in (ALL, NEW, FL, BO, MG, ML, JF)]
    m = 'g8r'
    for n in (FL, BO, MG):
        b.append(f'<line class="e" x1="{n.cx:.0f}" y1="{n.y + n.h:.0f}" x2="{n.cx:.0f}" y2="{bus:.0f}"/>')
    b.append(f'<line class="e" x1="{FL.cx:.0f}" y1="{bus:.0f}" x2="{MG.cx:.0f}" y2="{bus:.0f}"/>')
    b.append(edge([(ML.cx, bus), (ML.cx, ML.y)], mid=m))
    b.append(mlab(ML.cx + 12, (bus + ML.y) / 2 + 5 + (8 if lay() == 'both' else 0), "internal reports", "內部舉報", 'start'))
    b.append(edge([ML.bottom, JF.top], mid=m))
    b.append(mlab(ML.cx + 12, (ML.y + ML.h + JF.y) / 2 + 5 + (8 if lay() == 'both' else 0), "STR", "可疑交易報告", 'start'))
    aria = ("Training by role. Every member of staff should be made aware of five points, listed in the table below. Every new joiner, whatever their seniority, learns the background to ML/TF, to report suspicious transactions to the MLRO, and the tipping-off offence. Front-line staff learn the importance of their role as first point of contact, the CDD and record-keeping policies for their job, and when to be suspicious and how to report. Back-office staff learn verification and processing and to recognise abnormal settlements, payments or delivery instructions. Managerial staff, including internal audit officers and compliance officers, get higher-level training on the whole regime and on supervising, auditing, random checks and their duties in reporting to the JFIU. Internal reports from every group go to the MLRO, trained to assess them and report suspicious transactions to the JFIU, and to keep abreast of developments.",
            "按職位劃分的培訓。應促使每名職員留意下表所列五項。所有新職員不論資歷，學習洗錢及恐怖分子資金籌集的背景、向洗錢報告主任舉報可疑交易，以及「通風報訊」的罪行。前線職員學習其作為第一個接觸點的重要性、與其職責相關的盡職審查及備存紀錄政策，以及何時須起疑及如何舉報。後勤職員學習核實及處理程序，並識別不正常的結算、付款及交付指示。經理級人員包括內部審計人員及合規主任，接受涵蓋整個制度的更高層次培訓，以及監督、審查、隨機抽查及向財富情報組舉報的職責的培訓。各類職員的內部舉報均交予洗錢報告主任，其培訓涵蓋評估舉報、向財富情報組舉報可疑交易及掌握最新發展。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


ROLES_KEY = legend([('must', ("what staff should be made aware of: everyone", "應促使職員留意的事項：所有職員")),
                    ('', ("training that may be appropriate for that group", "或適用於該類職員的培訓")),
                    ('faint', ("outside your firm", "你的機構以外"))])


# ---------------------------------------------------------------- 3. the training cycle
def fig_cycle():
    W = 1000
    POL = Card(40, 920, ("Your training policy", "你的培訓政策"),
               ("Clear and well articulated, so that relevant staff receive adequate AML/CFT training. Scope and frequency are tailored to your specific risks and pitched to each person's job functions, responsibilities and experience",
                "清晰及明確，確保有關職員獲得充分的打擊洗錢培訓。培訓的範疇及頻密程度應切合你面對的特定風險，並顧及職員的職能、職責及經驗"),
               'must', "¶9.2–9.3")
    S1 = Card(40, 560, ("Someone is hired or appointed", "有人獲聘用或委任"), None, 'plain')
    S2 = Card(40, 560, ("Initial training, as soon as possible", "盡快接受初步培訓"),
              ("New staff should be required to attend it after being hired or appointed; the topics for new joiners are in the figure above",
               "新職員獲聘用或委任後，應盡快接受；新職員的培訓範疇見上圖"), 'must', "¶9.2, 9.5(a)")
    S3 = Card(40, 560, ("Deliver it with a mix of methods", "混合使用各種培訓技巧及工具"),
              ("Such as online learning systems, focused classroom training, relevant videos, and paper- or intranet-based procedures manuals; you may consider adding FATF papers and typologies to the materials",
               "例如網上學習系統、課堂上的集思培訓、相關影片，以及紙張形式或以內聯網為本的程序手冊；可考慮加入特別組織的文章及典型案件作為材料"),
              'plain', "¶9.6")
    S4 = Card(40, 560, ("Keep records, whatever the method", "不論使用哪種方法，均應備存紀錄"),
              ("You should monitor and keep records of who was trained, when they received the training, and what type of training it was; the records should be kept for at least 3 years",
               "你應監察誰人已接受培訓、何時接受培訓，以及所提供培訓的類別，並備存紀錄；紀錄應最少保存3年"), 'must', "¶9.7")
    S5 = Card(40, 560, ("Monitor whether it works", "監察培訓的效用"),
              ("You should monitor whether training works. The Guideline says it may be done by testing staff's understanding and their ability to recognise suspicious transactions; by monitoring their compliance and the quality and quantity of internal reports; and by following up anyone who misses training without reasonable cause",
               "你應監察培訓的效用。指引指可透過以下方法達致：測試職員的理解，以及他們辨認可疑交易的能力；監察職員的合規情況及內部報告的質和量；以及跟進沒有合理因由而缺席培訓的職員"),
              'must', "¶9.8(a)–(c)")
    R = Card(670, 280, ("Refresher training, regularly", "定期舉辦複修培訓"),
             ("Reminds staff of their responsibilities and keeps them informed of new ML/TF developments",
              "確保職員明白本身的責任，並掌握有關洗錢／恐怖分子資金籌集的最新發展"), 'must', "¶9.2")
    H = place([([POL], 30), ([S1], 30), ([S2], 30), ([S3], 30), ([S4], 30), ([S5], 0)], y0=14)
    R.y = S4.cy - R.h / 2
    b = [n.render() for n in (POL, S1, S2, S3, S4, S5, R)]
    m = 'g8c'
    for a, c in ((POL, S1), (S1, S2), (S2, S3), (S3, S4), (S4, S5)):
        b.append(edge([(c.cx, a.y + a.h), (c.cx, c.y)], mid=m))
    b.append(edge([S5.right, (R.cx, S5.cy), R.bottom], mid=m))
    b.append(mlab((S5.x + S5.w + R.cx) / 2, S5.cy - 8, "then, regularly", "其後定期"))
    b.append(edge([R.top, (R.cx, S3.cy), S3.right], mid=m))
    b.append(mlab((S3.x + S3.w + R.cx) / 2, S3.cy - 8, "back to delivery", "回到培訓方式"))
    aria = ("The training cycle. A clear training policy, tailored to your risks and each person's role, governs everything. When someone is hired or appointed, they attend initial training as soon as possible. Training is delivered with a mix of methods. You should record who was trained, when and in what, and keep the records for at least three years; and you should monitor whether the training works, which the Guideline says may be done by testing staff, monitoring compliance and the quality and quantity of internal reports, and following up missed attendance. Refresher training then brings staff back regularly.",
            "培訓循環。一套切合你的風險及每名職員職務的清晰培訓政策統領一切。有人獲聘用或委任後，應盡快接受初步培訓。培訓混合使用各種方法。你應記錄誰人、何時接受了哪類培訓，紀錄應最少保存3年；並應監察培訓的效用，指引指可透過測試職員、監察合規情況及內部報告的質和量，以及跟進缺席情況達致。其後以複修培訓定期讓職員再次接受培訓。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


CYCLE_KEY = legend([('must', ("what the Guideline says you should do", "指引指你應做的事")),
                    ('', ("a step, or how you deliver it", "步驟，或培訓的方式"))])
