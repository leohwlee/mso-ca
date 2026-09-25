# AMLO Part 2: requirements relating to CDD and record-keeping, ss.5-7.
# The duties themselves are on the Schedule 2 page; this page is about why they bind you.
from ui import *


NB = ' '   # keeps a phrase on one line inside a figure box


class BCard(Card):
    """A Card whose title and body may carry '|' to fix where a line breaks.

    Each piece still wraps on its own if it is too long for the box."""

    def __init__(self, x, w, title, body=None, kind='plain', cite=None, size=11.5, tsize=12.5, minh=0, **kw):
        flat = lambda t: tuple(s.replace('|', ' ' if i == 0 else '') for i, s in enumerate(t)) if t else t
        super().__init__(x, w, flat(title), flat(body), kind, cite, size=size, tsize=tsize, minh=minh, **kw)
        size, tsize = size * FS, tsize * FS
        inner = w - 24

        def lines(text, sz):
            out = []
            for piece in text.split('|'):
                out += wrap(piece, inner, sz)
            return out
        tcls = 't-inv t-b' if kind == 'stop' else ('t t-b t-faint' if kind == 'faint' else 't t-b')
        bcls = 't-inv' if kind == 'stop' else ('t t-faint' if kind == 'faint' else 't')
        for i, v in enumerate(('en', 'tc')):
            tl = lines(title[i], tsize) if title and title[i] else []
            bl = lines(body[i], size) if body and body[i] else []
            self.seg[v] = [(l, tcls, tsize) for l in tl] + [(l, bcls, size) for l in bl]
        # a little air between the English and the Chinese in the combined view
        self.seg['both'] = self.seg['en'] + [('', 't', 8 / LH)] + self.seg['tc']
        self.h = max(minh, sum(s * LH for _, _, s in self.seg[lay()]) + 16 + (CS * LH if cite else 0))
        self.topalign = False   # True: text starts at a fixed inset from the top edge instead of centring

    def render(self):
        if not self.topalign:
            return super().render()
        # Same drawing as Card.render, but top-aligned, so boxes stretched to a common
        # height keep their titles on one line across a row.
        k = self.kind
        out = [f'<rect class="n n-{k}" x="{self.x}" y="{self.y}" width="{self.w}" height="{self.h}" rx="6"/>']
        for v, seg in self.seg.items():
            y = self.y + 8
            g = [f'<g class="s-{v}">']
            for t, cls, s in seg:
                g.append(f'<text class="{cls}" font-size="{s}" text-anchor="middle"><tspan x="{self.cx}" y="{y + s * 0.95:.1f}">{esc(t)}</tspan></text>')
                y += s * LH
            if self.cite:
                ccls = 'c-inv' if k == 'stop' else 'c'
                g.append(f'<text class="{ccls}" font-size="{CS}" text-anchor="middle"><tspan x="{self.cx}" y="{y + CS * 0.95:.1f}">{esc(cite_txt(self.cite, v))}</tspan></text>')
            g.append('</g>')
            out.append(''.join(g))
        body = ''.join(out)
        body = f'<g class="answer" tabindex="0">{body}</g>' if self.answer else f'<g>{body}</g>'
        if self.href:
            body = f'<a class="figlink" href="{self.href}">{body}</a>'
        return body



def flabel(x, y, en, tc):
    """A fork label, left-aligned at x; y is the baseline of its last line.

    The combined view stacks English over Chinese with room between them."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        g = [f'<text class="lbl s-{v}" text-anchor="start">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (len(ls) - 1 - i) * 18:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def fig_chain():
    W = 1000
    N1 = BCard(250, 500, ("You are a financial institution", "你是金融機構"),
               ("A licensed money service operator is item (f) of the definition", "持牌金錢服務經營者是該定義的第(f)項"), cite="Sch. 1 Pt 2")
    N2 = BCard(250, 500, ("Schedule 2 has effect with respect to you, in full", "附表2就你全面具有效力"),
               ("Authorized insurers, licensed insurance agents and brokers, and the issue of stored value facilities by SVF licensees or banks get partial carve-outs;|a money service operator gets none",
                "獲授權保險人、持牌保險代理及保險經紀公司，|以及工具持牌人或銀行發行儲值支付工具，|均有部分例外；金錢服務經營者則沒有"), cite="s.5(1)–(4)")
    N3 = BCard(250, 500, ("You contravene a specified provision", "你違反指明的條文"),
               ("One of the Schedule 2 duties that section 5(11) lists", "即第5(11)條所列的附表2責任之一"), cite="s.5(11)")
    O1 = BCard(16, 260, ("Part 4 discipline", "第4部紀律行動"),
               ("Any one or more of: public|reprimand, a remedial order,|and a penalty up to the|greater of $10,000,000 or|3 times the profit gained|or costs avoided.|No one has to show you knew",
                "一項或多於一項：公開譴責、|糾正命令、罰款（上限為|$10,000,000或所獲取的利潤|或所避免的開支的3倍，|以較大者為準）。|毋須證明你明知"), 'must', "s.21(1)–(2)", answer=True)
    O2 = BCard(290, 222, ("Offence:|the institution knew", "罪行：機構明知而違反"),
               ("On indictment,|$1,000,000 and 2 years", "公訴程序：|罰款$1,000,000及監禁2年"), 'stop', "s.5(5)", answer=True)
    O3 = BCard(526, 222, ("Offence:|intent to defraud", "罪行：機構意圖詐騙"),
               ("The institution|meant to defraud|a relevant authority.|On indictment,|$1,000,000 and 7 years", "意圖詐騙有關當局。|公訴程序：|罰款$1,000,000及監禁7年"), 'stop', "s.5(6)", answer=True)
    O4 = BCard(762, 222, ("Offence:|staff or managers", "罪行：僱員及管理層"),
               ("An employee, anyone employed to work for it, or anyone concerned in its management, who caused or permitted the breach knowingly, or to defraud",
                "僱員、受僱為機構工作的人，|或關涉機構管理的人，|明知而致使或准許違反，|或為詐騙而如此行事"), 'stop', "s.5(7)–(8)", answer=True)
    row = (O1, O2, O3, O4)
    hmax = max(o.h for o in row)
    for o in row:          # one height, one top edge, one title line: four parallel outcomes
        o.h = hmax
        o.topalign = True
    gap = 90 if lay() == 'both' else 64
    H = place([([N1], 30), ([N2], 30), ([N3], gap), (list(row), 0)])
    b = [n.render() for n in (N1, N2, N3) + row]
    m = 'p2c'
    b.append(edge([N1.bottom, N2.top], mid=m))
    b.append(edge([N2.bottom, N3.top], mid=m))
    by = O1.y - 22
    b.append(f'<polyline class="e" points="{O1.cx:.0f},{by:.0f} {O4.cx:.0f},{by:.0f}"/>')
    b.append(f'<polyline class="e" points="{N3.cx:.0f},{N3.bottom[1]:.0f} {N3.cx:.0f},{by:.0f}"/>')
    for o in row:
        b.append(edge([(o.cx, by), o.top], mid=m))
    b.append(flabel(N3.cx + 12, by - 12, "discipline and prosecution can both follow", "紀律行動與刑事檢控可同時進行"))
    aria = ("How a Schedule 2 breach reaches a money service operator: the licensee is a financial institution, Schedule 2 has effect on it in full, and contravening a specified provision opens Part 4 discipline, which needs no proof of knowledge, and three criminal offences: the institution acting knowingly, the institution acting with intent to defraud, and its employees, people employed to work for it or people concerned in its management causing or permitting the contravention.",
            "附表2的違規如何牽涉金錢服務經營者：持牌人屬金融機構，附表2對其全面具有效力；違反指明的條文會開啟第4部紀律行動（毋須證明明知）及三類刑事罪行：機構明知而違反、機構意圖詐騙，以及其僱員、受僱為機構工作或關涉機構管理的人致使或准許違反。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


A = sec('chain', [("Part 2", "第2部"), "s.5", ("with Sch. 1, s.21", "另及附表1、第21條")],
        ("How a Schedule 2 breach reaches you", "附表2的違規如何牽涉你"),
    P("Follow the chain down the middle. The top two boxes are why Schedule 2 binds you at all; the third is the breach; the four at the bottom are what can follow it. Only the red box can happen without anyone proving what you knew.",
      "沿中間的鏈條往下看。上面兩個方格說明附表2為何約束你，第三個是違規本身；下面四個方格是違規後可能出現的後果。只有紅色方格不需要證明你知道甚麼。")
    + fig(fig_chain, ("Section 5 does not create the duties; it gives them effect and attaches the criminal sanction. The duties themselves, and their thresholds, are on the Schedule 2 page.",
                        "第5條本身並不訂立各項責任，而是令其生效並附加刑事制裁。各項責任及其門檻，見附表2一頁。"),
          legend([('', ("the chain from your licence to a breach", "由持牌到違規的鏈條")),
                  ('must', ("disciplinary action by the Commissioner", "關長的紀律行動")),
                  ('stop', ("a criminal offence, tried in court", "刑事罪行，由法院審理"))]))
    + traps(
        trap(("The carve-outs in section 5 are not yours", "第5條的例外與你無關"),
             ("There are three. Long term business limits Schedule 2 for authorized insurers; subsection (3) limits it, for licensed insurance agents, agencies and broker companies, to transactions involving certain contracts of insurance; and the $3,000 physical-device test limits it for the issue of stored value facilities by SVF licensees or banks. None of them touches a money service operator, so a question that applies any of them to you is wrong.",
              "共有三項。「長期業務」限制附表2對獲授權保險人的適用範圍；第(3)款把附表2對持牌個人保險代理、持牌保險代理機構及持牌保險經紀公司的適用範圍，限於涉及某些保險合約的交易；$3,000及實物裝置的測試則限制其對工具持牌人或銀行發行儲值支付工具的適用範圍。這些例外全都與金錢服務經營者無關，任何把它們套用在你身上的選項都是錯的。"),
             "s.5(2)–(4)"),
        trap(("Knowledge decides the crime, not the discipline", "明知與否決定罪行，而非紀律行動"), None, "s.5(5) · s.21(1)",
             vs=[(("Prosecution", "刑事檢控"), ("Needs the institution to have acted knowingly, or with intent to defraud.", "須證明機構明知而違反，或意圖詐騙。")),
                 (("Part 4 discipline", "第4部紀律行動"), ("Needs only the contravention itself.", "只需有違反的事實。"))]),
    ))

# ---------------------------------------------------------------- B. the offences
def cell(desc, pen, cite, extra=''):
    return (f'<td>{B(*desc)}<div class="pen2"><span class="answer" tabindex="0">{B(*pen)}</span></div>{extra}{cite_html(cite)}</td>')


KNOW = ("On indictment: $1,000,000 and 2 years. Summarily: level 6 and 6 months.", "公訴程序：罰款$1,000,000及監禁2年。簡易程序：第6級罰款及監禁6個月。")
FRAUD = ("On indictment: $1,000,000 and 7 years. Summarily: $500,000 and 1 year.", "公訴程序：罰款$1,000,000及監禁7年。簡易程序：罰款$500,000及監禁1年。")

B_ = sec('offences', ["s.5(5)–(10)", ("four offences", "四項罪行")],
         ("The four offences, side by side", "四項罪行一併比較"),
    P("Read across for the mental element and down for who is charged. The fine on indictment never moves from $1,000,000; what intent to defraud changes is the prison term, and the summary penalty turns from a level into a sum.",
      "橫看是犯罪意圖，直看是被控者。循公訴程序定罪的罰款一律是$1,000,000；意圖詐騙所改變的，是監禁刑期，而簡易程序的罰則亦由罰款級別變為具體款額。")
    + table([th("", ""), th("Acting knowingly", "明知而為"), th("Acting with intent to defraud", "意圖詐騙")], [
        tr(rh("The institution: you", "機構本身：你"),
           cell(("<b>Knowingly contravenes</b> a specified provision.", "<b>明知而違反</b>指明的條文。"), KNOW, "s.5(5)"),
           cell(("Contravenes a specified provision with intent to defraud <b>any relevant authority</b>.", "意圖詐騙<b>任何有關當局</b>而違反指明的條文。"), FRAUD, "s.5(6)")),
        tr(rh("Its people: an employee, a person employed to work for it, or anyone concerned in its management", "其僱員及管理層：僱員、受僱為該機構工作的人，或關涉該機構的管理的人"),
           cell(("<b>Knowingly causes or knowingly permits</b> the institution to contravene.", "<b>明知而致使或明知而准許</b>該機構違反。"), KNOW, "s.5(7)"),
           cell(("Causes or permits the contravention with intent to defraud <b>the institution or any relevant authority</b>.", "意圖詐騙<b>該機構或任何有關當局</b>，而致使或准許該機構違反。"), FRAUD, "s.5(8)", flag())),
        tr(rh("The only defence written in", "條文訂明的唯一免責辯護"),
           td("For the offence in subsection (7) only, an <b>employee</b> or a person <b>employed to work for</b> the institution can prove they acted in accordance with the policies and procedures it set up for complying with that provision. A person concerned in management cannot.",
              "只適用於第(7)款的罪行：<b>僱員</b>或<b>受僱為該機構工作的人</b>，如能證明其作為符合該機構為遵守有關條文而設立和維持的政策及程序，即可以此免責。關涉該機構的管理的人不可以此免責。", "s.5(9)", post=flag()),
           td("The section writes in none, for the institution or for its people.", "條文並無為機構或其僱員及管理層訂明任何免責辯護。")),
    ], cls='cmp', note=B("If the institution is a <b>partnership</b>, a fine imposed on it is paid out of the partnership's funds.", "如該機構是<b>合夥</b>，對其判處的罰款須以合夥的資金支付。") + ' ' + cite_html("s.5(10)"), minw=780)
    + traps(
        trap(("Whose fraud counts?", "詐騙的對象是誰？"), None, "s.5(6) · s.5(8)",
             vs=[(("The institution's offence", "機構的罪行"), ("Intent to defraud <b>a relevant authority</b>. Defrauding someone else does not fit this subsection.", "意圖詐騙<b>有關當局</b>。詐騙其他人並不符合本款。")),
                 (("Its people's offence", "僱員及管理層的罪行"), ("Intent to defraud <b>the institution itself</b>, or a relevant authority.", "意圖詐騙<b>該機構本身</b>或有關當局。"))]),
        trap(("The employee's defence has two limits", "僱員的免責辯護有兩項限制"),
             ("It answers only the knowingly offence, never the fraud offence. And it belongs only to an employee or someone employed to work for the institution; a manager charged under the same subsection has nothing equivalent. This is why written procedures protect your counter staff.",
              "它只適用於明知而為的罪行，從不適用於詐騙罪行；而且只屬於僱員或受僱為機構工作的人，被控同一罪行的管理層並無同等保障。這正是書面程序能保障櫃位僱員的原因。"),
             "s.5(9)"),
        trap(("A level or a sum, summarily?", "簡易程序：罰款級別還是具體款額？"), None, "s.5(5)–(8)",
             vs=[(("Knowingly", "明知而為"), ("Level 6 and 6 months.", "第6級罰款及監禁6個月。")),
                 (("With intent to defraud", "意圖詐騙"), ("$500,000 and 1 year.", "罰款$500,000及監禁1年。"))]),
    ))

# ---------------------------------------------------------------- C. specified provisions
SPEC = [
    ("Carry out CDD before a business relationship, before an occasional transaction at the threshold, and whenever you suspect ML/TF or doubt identity information obtained earlier",
     "在建立業務關係前、在達門檻的非經常交易前，以及每當懷疑涉及洗錢或恐怖分子資金籌集，或懷疑過往取得的身分資料時，執行客戶盡職審查", True, None, "s.3(1), (1A) Sch. 2"),
    ("Verify identity only after the relationship starts, where that is necessary not to interrupt normal business and the ML/TF risk is effectively managed",
     "在為不干擾正常業務運作而有必要，且洗錢或恐怖分子資金籌集風險已獲有效管理的情況下，於建立業務關係後才核實身分", False,
     ("A permission. Once you use it, completing verification as soon as reasonably practicable (subsection (3)) is specified", "屬准許。但一旦採用，在合理地切實可行的範圍內盡快完成核實（第(3)款）即屬指明的條文"), "s.3(2) Sch. 2"),
    ("Do not proceed, or end the relationship, when CDD cannot be completed", "未能完成客戶盡職審查時，不可進行交易，或須終止業務關係", True, None, "s.3(4) Sch. 2"),
    ("Simplified due diligence for the listed low-risk customers and products", "就所列低風險客戶及產品執行簡化客戶盡職審查", False,
     ("A permission, so there is nothing in it to break", "屬准許，故當中並無可違反之處"), "s.4 Sch. 2"),
    ("Monitor each business relationship continuously, adding measures for customers not present, PEPs and high-risk situations",
     "持續監察每段業務關係；就沒有現身的客戶、政治人物及高風險情況採取額外措施", True, None, "s.5(1), (3) Sch. 2"),
    ("Carry out CDD on a pre-existing customer when a trigger event occurs, or end the relationship", "先前客戶出現觸發事件時執行客戶盡職審查，否則須終止業務關係", True, None, "s.6 Sch. 2"),
    ("Take at least one extra measure when the customer is not physically present", "客戶沒有現身時，最少採取一項額外措施", True, None, "s.9 Sch. 2"),
    ("For a PEP: senior management approval, and source of wealth and of funds", "就政治人物：取得高級管理層批准，並確立財富來源及資金來源", True,
     ("The former-PEP exemption in subsection (3) is not", "第(3)款有關前政治人物的豁免則不是"), "s.10 Sch. 2"),
    ("Wire transfers: record, include, pass on and chase the originator and recipient information", "電傳轉帳：記錄、附上、傳遞及追補匯款人及收款人資料", True,
     ("The exemptions and the batch-file option are not", "豁免情況及群組檔案安排則不是"), "s.12 Sch. 2"),
    ("Remittance transactions other than wire transfers, of $8,000 or more: identify and verify the originator, and record the details", "$8,000或以上的匯款交易（電傳轉帳除外）：識別及核實匯款人身分，並記錄有關資料", True, None, "s.13(2) Sch. 2"),
    ("Virtual asset transfers: obtain, record and submit the originator and recipient information", "虛擬資產轉帳：取得、記錄及提交匯款人及收款人資料", True, None, "s.13A Sch. 2"),
    ("Enhanced measures in high-risk situations, including any the Commissioner specifies in a written notice", "在高風險情況下（包括關長藉書面通知指明的情況）採取更嚴格措施", True, None, "s.15 Sch. 2"),
    ("Never open or keep an anonymous account, or one in a fictitious name", "不得開立或維持匿名戶口，或以虛構姓名或名稱開立的戶口", True, None, "s.16 Sch. 2"),
    ("When relying on an intermediary: obtain its data immediately, and make sure copies come on request", "依賴中介人時：立刻取得其數據或資料，並確保可應要求取得複本", True,
     ("The permission to rely, in subsection (1), is not", "第(1)款准許依賴中介人的條文則不是"), "s.18 Sch. 2"),
    ("Effective procedures: PEP screening, wire and virtual asset transfers, and each kind of customer, relationship, product and transaction",
     "有效的程序：斷定政治人物、處理電傳轉帳及虛擬資產轉帳，以及就每種客戶、業務關係、產品及交易而設的程序", True, None, "s.19 Sch. 2"),
    ("Keep records for at least five years, longer if a notice says so, in the prescribed form", "按訂明方式備存紀錄最少五年；如有通知規定則更長", True,
     ("The Commissioner's power to demand a longer period is not; complying with his notice is", "關長要求延長期間的權力則不是；遵從其通知才是"), "s.20–21 Sch. 2"),
    ("Make overseas branches and subsidiaries follow similar requirements, or inform the Commissioner and mitigate", "確保海外分行及附屬企業遵從類似規定，否則須通知關長並減低風險", True, None, "s.22(1)–(2) Sch. 2"),
    ("Take all reasonable measures to prevent a breach of Schedule 2 Parts 2 and 3, and to mitigate ML/TF risk", "採取所有合理措施，防止違反附表2第2及3部，並減低洗錢及恐怖分子資金籌集風險", True, None, "s.23 Sch. 2"),
    ("Insurance policy beneficiaries, correspondent banking and shell banks", "保險單受益人、代理銀行服務及空殼銀行", True,
     ("Specified, but written for insurers and banks, not for you", "屬指明的條文，但針對保險人及銀行，並非針對你"), "s.7, 11, 14, 17 Sch. 2"),
]


def spec_rows():
    out = []
    for en, tc, yes, note, cite in SPEC:
        v = YES if yes else NO
        n = f'<div class="small">{B(*note)}</div>' if note else ''
        cls = '' if yes else 'soft'
        out.append(f'<tr class="{cls}"><td>{B(en, tc)}{cite_html(cite)}</td><td class="verdict">{v}{n}</td></tr>')
    return out


C_ = sec('specified', ["s.5(11)", ("the list", "清單")],
         ("Which Schedule 2 rules are specified provisions", "附表2哪些規定屬指明的條文"),
    P("A specified provision is a Schedule 2 sentence that tells you to do something, or not to. Definitions, permissions and exemptions are left off the list, because there is nothing in them to break. Find the rule on the left; the right-hand column says whether breaking it opens the offences and Part 4.",
      "指明的條文，是附表2中要求你作出或不作出某事的句子。定義、准許及豁免不在清單之內，因為當中並無可違反之處。在左邊找出規定，右欄說明違反它是否會引致刑事罪行及第4部的紀律行動。")
    + table([th("The Schedule 2 rule, in plain words", "附表2的規定（淺白說明）"), th("Specified provision?", "是否指明的條文？")], spec_rows(), minw=700, cls='spec')
    + traps(
        trap(("A permission cannot be breached, but the duties around it can", "准許本身不能違反，但相關的責任可以"),
             ("Delayed verification and simplified due diligence are permissions, so neither is on the list. The duties around them are. Once you verify late, you must complete the verification as soon as reasonably practicable. If you cannot complete CDD, or that verification, you must not establish a business relationship or carry out an occasional transaction with that customer, or must end an existing relationship as soon as reasonably practicable. A customer who does not meet the simplified due diligence conditions simply gets full CDD; failing those conditions is not itself a reason to stop.",
              "延後核實及簡化客戶盡職審查屬准許，故不在清單之內，但相關的責任則在清單之內。一旦延後核實，你須在合理地切實可行的範圍內盡快完成核實。如不能完成客戶盡職審查或該項核實，便不可建立業務關係或進行非經常交易，或須在合理地切實可行的範圍內盡快結束業務關係。客戶如不符合簡化客戶盡職審查的條件，你便須執行全面的客戶盡職審查；不符合這些條件本身並不是停止交易的理由。"),
             "s.3(1), (2)–(4), 4(1) Sch. 2"),
    ))

# ---------------------------------------------------------------- D. guidelines
def fig_guide():
    W = 1000
    TOP = BCard(250, 500, ("You did not follow a provision of the C&ED Guideline", "你沒有遵從海關指引的某項條文"),
                ("A guideline published in the Gazette under section 7|on how Schedule 2 operates", "即根據第7條在憲報公布、就附表2的施行提供導引的指引"), cite="s.7(1)")
    G1 = BCard(10, 310, ("Not by itself|a ground for proceedings", "此事本身不構成被起訴的理由"),
               ("No judicial or other proceedings can|rest on the guideline breach alone", "不能單憑沒有遵守指引，|而提起任何司法或其他法律程序"), 'ok', "s.7(4)", answer=True)
    G2 = BCard(345, 310, ("The Commissioner must|have regard to it", "關長須顧及該指引"),
               ("When he considers whether you|contravened Schedule 2, any relevant|provision counts", "他考慮你有否違反附表2時，|須顧及當中任何相關條文"), 'must', "s.7(5)", answer=True)
    G3 = BCard(680, 310, ("A court must weigh|any relevant provision", "法院須考慮攸關的條文"),
               ("In proceedings under the Ordinance|before a court, the guideline is|admissible in evidence, and any|provision the court finds relevant|must be taken into account",
                "在根據本條例於法院進行的|法律程序中，指引可獲接納為證據；|法院如覺得指引內的條文攸關|有關問題，須考慮該條文"), 'must', "s.7(4)", answer=True)
    row = (G1, G2, G3)
    hmax = max(g.h for g in row)
    for g in row:          # one height, one top edge, one title line: three parallel consequences
        g.h = hmax
        g.topalign = True
    H = place([([TOP], 50), (list(row), 0)])
    b = [n.render() for n in (TOP,) + row]
    m = 'p2g'
    by = TOP.bottom[1] + 24
    b.append(f'<polyline class="e" points="{TOP.cx:.0f},{TOP.bottom[1]:.0f} {TOP.cx:.0f},{by:.0f}"/>')
    b.append(f'<polyline class="e" points="{G1.cx:.0f},{by:.0f} {G3.cx:.0f},{by:.0f}"/>')
    for g in row:
        b.append(edge([(g.cx, by), g.top], mid=m))
    aria = ("What a departure from the C&ED Guideline means: it is not by itself a ground for proceedings, but the Commissioner must have regard to relevant provisions when deciding whether Schedule 2 was contravened; and in proceedings under the Ordinance before a court the guideline is admissible in evidence, and the court must take into account any provision it finds relevant.",
            "沒有遵從海關指引的後果：此事本身不構成被起訴的理由；但關長在決定有否違反附表2時須顧及相關條文；而在根據本條例於法院進行的法律程序中，該指引可獲接納為證據，法院如覺得指引內的條文攸關有關問題，須考慮該條文。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


D_ = sec('guidelines', ["s.7", "s.23 · s.45", ("guidelines", "指引")],
         ("What the Guideline is worth in law", "指引在法律上的份量"),
    P("Start from the top box, which is you departing from a line of the Guideline, and read the three consequences left to right. The green one is the only comfort, and it is narrower than it looks.",
      "由頂部方格開始，即你沒有遵從指引的某一條文，然後由左至右閱讀三項後果。綠色的一項是唯一的寬慰，而且範圍比表面上窄。")
    + fig(fig_guide, ("In practice the Guideline is the yardstick. It sets out the standards a money service operator should meet to comply with the Ordinance, and compliance with it is enforced through the Ordinance: an operator that fails to comply with the Guideline may face disciplinary and other action under the Ordinance for not meeting the relevant requirements (Guideline ¶1.3). The Ordinance says CDD must be done; the Guideline says what adequate CDD looks like.",
                        "實際上，指引就是衡量的準則。它載列金錢服務經營者為履行條例的法定規定而應遵守的準則，其遵行情況按照條例強制執行：金錢服務經營者如未有遵守指引，或會因沒有遵守相關規定而面對根據條例採取的紀律行動及其他行動（指引第1.3段）。條例規定必須執行客戶盡職審查；指引說明怎樣才算充分。"),
          legend([('', ("the starting point", "起點")), ('ok', ("a protection for you", "你可依靠的保障")),
                  ('must', ("a consequence for you", "你要承受的後果"))]))
    + table([th("", ""), th("The guideline on how Schedule 2 operates", "就附表2的施行發出的指引"), th("The guidelines on imposing a pecuniary penalty", "施加罰款的指引")], [
        tr(rh("Made under", "根據"), td("Section 7", "第7條"), td("Section 23 for Part 4 penalties; section 45 for Part 5 penalties", "第23條（第4部罰款）；第45條（第5部罰款）")),
        tr(rh("Your copy", "你手上的版本"),
           td("Guideline on Anti-Money Laundering and Counter-Financing of Terrorism (For Money Service Operators), June 2023", "《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》，2023年6月"),
           td("Disciplinary Fining Guideline, May 2018, under section 23; and Disciplinary Action Guideline on Imposition of Pecuniary Penalty, April 2018, under section 45", "《紀律處分罰款指引》（2018年5月），根據第23條；以及《施加罰款紀律行動指引》（2018年4月），根據第45條", post=flag())),
        tr(rh("When it must exist", "何時必須存在"), td("Whenever the authority considers it appropriate", "有關當局認為適當時"), td("<b>Before</b> the penalty power is first used", "在首次行使罰款權力<b>之前</b>")),
        tr(rh("Where published", "在哪裏公布"), td("The Gazette", "憲報"), td("The Gazette, and any other manner the authority considers appropriate", "憲報，以及有關當局認為適當的其他方式")),
        tr(rh("Who must weigh it", "誰必須考慮"), td("The authority, when assessing a Schedule 2 breach; a court, in proceedings under the Ordinance", "有關當局評估有否違反附表2時；法院審理本條例下的法律程序時"), td("The authority, every time it imposes a penalty", "有關當局每次施加罰款時")),
        tr(rh("Legal status", "法律地位"), td("Not subsidiary legislation; a reference to it means the guideline as amended", "並非附屬法例；提述該指引即指經修訂的版本"), td("Not subsidiary legislation", "並非附屬法例")),
    ], minw=780, cls='cmp')
    + traps(
        trap(("Two penalty guidelines with similar names", "兩份名稱相近的罰款指引"), None, "s.23 · s.45",
             vs=[(("Disciplinary Fining Guideline, May 2018", "《紀律處分罰款指引》（2018年5月）"),
                  ("Section 23, Part 4. Penalties for breaching a Schedule 2 specified provision, up to $10,000,000 or 3 times the profit gained or costs avoided, whichever is greater.", "第23條，第4部。就違反附表2指明的條文施加的罰款，上限為$10,000,000或所獲取的利潤或所避免的開支的3倍（以較大者為準）。")),
                 (("Disciplinary Action Guideline on Imposition of Pecuniary Penalty, April 2018", "《施加罰款紀律行動指引》（2018年4月）"),
                  ("Section 45, Part 5. Penalties for breaching a licence condition, a Part 5 regulation or a Part 5 duty, up to $1,000,000.", "第45條，第5部。就違反牌照條件、第5部規例或第5部責任施加的罰款，上限為$1,000,000。"))]),
        trap(("Not subsidiary legislation does not mean optional", "並非附屬法例不等於可有可無"),
             ("The Guideline cannot on its own found proceedings, but it is admissible, any relevant provision must be taken into account, and the Commissioner must have regard to it. Treating it as advice you may ignore is the wrong answer.",
              "指引本身不能作為提起法律程序的依據，但它可獲接納為證據，攸關的條文必須予以考慮，而關長亦須顧及。視之為可以忽略的意見，是錯誤的答案。"),
             "s.7(4)–(6)"),
    ))

P2_NAV = [('chain', 'How it reaches you', '如何牽涉你'), ('offences', 'The four offences', '四項罪行'),
          ('specified', 'Specified provisions', '指明的條文'), ('guidelines', 'What a guideline is worth', '指引的份量')]
P2_BODY = A + B_ + C_ + D_
