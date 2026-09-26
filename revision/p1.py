# AMLO Part 1: preliminary. The map of the whole Ordinance, who can change the
# rulebook, and the Government and immunity sections.
from ui import *


LINK = ' ↗'   # marks a box that opens a page or section of the pack


def _bi_gap(c):
    """In the combined view, open a small gap between the English and the Chinese text of a card."""
    sp = 6
    c.seg['both'] = c.seg['en'] + [('', 't', sp)] + c.seg['tc']
    if lay() == 'both':
        c.h += sp * LH
    return c


def _pair(a, b):
    """A Part and its Schedule get one height, so their edges line up."""
    h = max(a.h, b.h)
    a.h = b.h = h


def _clabel(x, y, en, tc):
    """Connector label. One language: every line stacks above the line. Combined view: English above, Chinese below."""
    step = 16
    out = []
    for v in ('en', 'tc', 'both'):
        one = en if v == 'en' else tc
        if v == 'both':
            above, below = en, tc
        else:   # all lines above, so the connector never cuts through a label
            above, below = one, []
        g = [f'<text class="lbl s-{v}" text-anchor="middle">']
        n = len(above)
        for i, l in enumerate(above):
            g.append(f'<tspan x="{x}" y="{y - 8 - (n - 1 - i) * step:.1f}">{esc(l)}</tspan>')
        for i, l in enumerate(below):
            g.append(f'<tspan x="{x}" y="{y + 19 + i * step:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def _card(x, w, title, body=None, **k):
    """Card whose body may carry '|' to force line breaks in a language (each line must still fit)."""
    plain = tuple(t.replace('|', '') for t in body) if body else body
    c = Card(x, w, title, plain, **k)
    for i, v in enumerate(('en', 'tc')):
        if body and '|' in body[i]:
            lines = [l.strip() for l in body[i].split('|')]
            head = [s_ for s_ in c.seg[v] if 't-b' in s_[1]]
            rest = [s_ for s_ in c.seg[v] if 't-b' not in s_[1]]
            cls, size = rest[0][1], rest[0][2]
            for l in lines:
                assert tw(l, size) <= w - 24, l
            c.seg[v] = head + [(l, cls, size) for l in lines]
    c.seg['both'] = c.seg['en'] + c.seg['tc']
    c.h = sum(s_ * LH for _, _, s_ in c.seg[lay()]) + 16 + (CS * LH if c.cite else 0)
    return _bi_gap(c)


def fig_map():
    W = 1000
    PX, PW, SX, SW = 16, 500, 648, 336
    C = _card
    P1 = C(PX, PW, ("Part 1 · Preliminary" + LINK, "第1部 · 導言" + LINK),
           ("Makes Schedule 1 the home of the shared definitions, applies the Ordinance to the Government, and shields anyone performing its functions in good faith from civil liability",
            "以附表1載列通用釋義；條例適用於政府；|真誠執行職能者免負民事法律責任"), href="#doc-p1")
    S1 = C(SX, SW, ("Schedule 1 · Interpretation" + LINK, "附表1 · 釋義" + LINK),
           ("Money service, ML and TF, financial institution, relevant authority and other shared terms",
            "金錢服務、洗錢、恐怖分子資金籌集、金融機構、有關當局等通用詞語"), href="#doc-s1")
    P2 = C(PX, PW, ("Part 2 · CDD and record-keeping" + LINK, "第2部 · 客戶盡職審查及備存紀錄" + LINK),
           ("Binds financial institutions, you included, to Schedule 2, and makes it a crime to contravene a specified provision knowingly or with intent to defraud a relevant authority",
            "令附表2對金融機構（包括你）具約束力；|明知而違反指明的條文，或出於詐騙有關當局的意圖而違反，即屬犯罪"), href="#doc-p2")
    S2 = C(SX, SW, ("Schedule 2 · The duties themselves" + LINK, "附表2 · 具體規定" + LINK),
           ("When and how to carry out CDD, monitor business relationships continuously, handle transfers and keep records",
            "何時及如何執行客戶盡職審查、持續監察、轉帳及備存紀錄"), href="#doc-s2")
    P3 = C(PX, PW, ("Part 3 · Supervision and investigations" + LINK, "第3部 · 監管及調查" + LINK),
           ("Routine inspections, investigations, warrants, and the offences for not cooperating",
            "例行視察、調查、手令，以及不合作的罪行"), href="#doc-p3")
    P4 = C(PX, PW, ("Part 4 · Disciplinary actions" + LINK, "第4部 · 紀律行動" + LINK),
           ("For breaching a specified provision of Schedule 2: reprimands, orders to take remedial action and penalties up to the greater of $10,000,000 or 3 times the profit gained or costs avoided",
            "就違反附表2的指明條文：譴責、採取糾正行動的命令，|以及最高$10,000,000或所獲取的利潤或所避免的開支的3倍|（以較大者為準）的罰款"), href="#doc-p4")
    P5 = C(PX, PW, ("Part 5 · Regulation of money service" + LINK, "第5部 · 對經營金錢服務的規管" + LINK),
           ("Your licence: grant, renewal, approvals, duties, and the Commissioner's own discipline",
            "你的牌照：批給、續期、批准、責任，以及關長本身的紀律處分權力"), href="#doc-p5")
    S3 = C(SX, SW, ("Schedule 3 · Fees" + LINK, "附表3 · 費用" + LINK),
           ("Fees for licence applications|and renewals, approvals, new or|particular premises, and register|copies and certificates",
            "牌照申請及續期、批准、新增或特定處所，|以及登記冊複本及證明書的收費"), href="#doc-s3")
    PX5 = C(PX, PW, ("Parts 5A, 5B and 5C · Other sectors", "第5A、5B及5C部 · 其他行業"),
            ("Trust or company service providers, virtual asset services, and dealers in precious metals and stones",
             "信託或公司服務提供者、虛擬資產服務，以及貴金屬及寶石交易商"), kind='faint')
    SX3 = C(SX, SW, ("Schedules 3A to 3K" + LINK, "附表3A至3K" + LINK),
            ("Those regimes' fees, forms and amounts", "上述三個制度的費用、表格及款額"), kind='faint', href="#s3-lettered")
    P6 = C(PX, PW, ("Part 6 · Review Tribunal" + LINK, "第6部 · 覆核審裁處" + LINK),
           ("Challenge the Commissioner's decisions, then appeal to the Court of Appeal with leave",
            "就關長的決定申請覆核，其後經許可可上訴至上訴法庭"), href="#doc-p6")
    S4 = C(SX, SW, ("Schedule 4 · Tribunal provisions" + LINK, "附表4 · 審裁處的條文" + LINK),
           ("Who sits on a review, and how it runs", "審裁處由誰組成，以及聆訊如何進行"), href="#doc-s4")
    P6A = C(PX, PW, ("Part 6A · Confidentiality" + LINK, "第6A部 · 保密的規定" + LINK),
            ("Who must keep inspection, investigation and disciplinary information secret, you included",
             "誰須對視察、調查及紀律程序的資料保密（包括你）"), href="#doc-p6a")
    P7 = C(PX, PW, ("Part 7 · Miscellaneous" + LINK, "第7部 · 雜項條文" + LINK),
           ("Standard of proof, prosecutions, how notices reach you, and legal professional privilege",
            "舉證準則、檢控、通知如何送達，以及法律專業保密權"), href="#doc-p7")
    P8 = C(PX, PW, ("Part 8 · Omitted as spent", "第8部 · 已失時效而略去"), None, kind='faint')
    for a, b_ in ((P1, S1), (P2, S2), (P5, S3), (PX5, SX3), (P6, S4)):
        _pair(a, b_)
    rows = [([P1, S1], 14), ([P2, S2], 14), ([P3], 14), ([P4], 14), ([P5, S3], 14), ([PX5, SX3], 14),
            ([P6, S4], 14), ([P6A], 14), ([P7], 14), ([P8], 0)]
    H = place(rows, y0=40)
    b = []
    for v, (pe, se), ls in (('en', ("PARTS", "SCHEDULES"), 1), ('tc', ("各部", "附表"), 0),
                            ('both', ("PARTS 各部", "SCHEDULES 附表"), 0)):
        for x, t in ((PX + PW / 2, pe), (SX + SW / 2, se)):
            b.append(f'<text class="c-sans s-{v}" x="{x}" y="26" font-size="{12 * FS}" font-weight="600" '
                     f'text-anchor="middle" letter-spacing="{ls}">{esc(t)}</text>')
    for n in (P1, S1, P2, S2, P3, P4, P5, S3, PX5, SX3, P6, S4, P6A, P7, P8):
        b.append(n.render())
    mx = (PX + PW + SX) / 2
    for p, lab in ((P1, (["s.2"], ["第2條"])), (P2, (["s.5"], ["第5條"])),
                   (P5, (["s.28, 30, 31,", "35–39, 50"], ["第28、30、31、", "35至39、50條"])),
                   (P6, (["s.58"], ["第58條"]))):
        b.append(hline(PX + PW, SX, p.cy))
        b.append(_clabel(mx, p.cy, *lab))
    # the other sectors' link: as faint as the boxes it joins, and places no duty on you
    b.append(f'<line class="e e-dash" style="stroke:var(--muted)" x1="{PX + PW}" y1="{PX5.cy:.0f}" x2="{SX}" y2="{PX5.cy:.0f}"/>')
    aria = ("Map of the Ordinance. The Parts run down the left in order and each Schedule sits beside the Part that gives it effect: Schedule 1 beside Part 1 through section 2, Schedule 2 beside Part 2 through section 5, Schedule 3 beside Part 5 through the fee sections 28, 30, 31 and 35 to 39 and the amending power in section 50, Schedules 3A to 3K beside Parts 5A to 5C, and Schedule 4 beside Part 6 through section 58. Parts 5A to 5C and their Schedules regulate other sectors, and Part 8 is spent.",
            "條例結構圖。左欄按次序列出各部，每個附表置於賦予其效力的一部旁邊：附表1經第2條連接第1部，附表2經第5條連接第2部，附表3經第28、30、31及35至39條的收費條文及第50條的修訂權力連接第5部，附表3A至3K連接第5A至5C部，附表4經第58條連接第6部。第5A至5C部及其附表規管其他行業，第8部已失時效。")
    return svg(W, H + 14, ''.join(b), aria, 'p1m', 860)


MAP_KEY = legend([('', ("applies to you as a money service operator", "適用於作為金錢服務經營者的你")),
                  ('faint', ("another sector's regime, or spent: places no duty on you", "其他行業的制度或已失時效：不對你施加責任"))])

A = sec('map', [("Part 1", "第1部"), "s.1–s.4", ("and the map", "及全貌")],
        ("The whole Ordinance on one page", "一頁看清整條條例"),
    P("Read the left column from the top: these are the Parts in the order they appear. A Schedule sits beside the Part that brings it into force, and the label on the connecting line names the section or sections that do it. The dashed line to the other sectors' Schedules is left unlabelled. A title ending in ↗ is a link: click the box to open that part of the pack.",
      "由左欄頂部讀起：這些是按次序排列的各部。每個附表置於令其生效的一部旁邊，連接線上的標籤是負責連接的條文。通往其他行業附表的虛線不設標籤。標題末端有 ↗ 的方格可以點擊，開啟本資料集的相應部分。")
    + fig(fig_map, ("Two things this map settles. First, Schedules are not free-standing: Schedule 2 binds you only because section 5 says so, and Schedule 4 governs the Tribunal only because section 58 says so. Second, the lettered Parts and Schedules between 5 and 6 belong to three other regulatory regimes; knowing where they sit is enough.",
                      "這張圖釐清兩點。第一，附表並非獨立存在：附表2之所以約束你，是因為第5條如此規定；附表4之所以規管審裁處，是因為第58條如此規定。第二，第5與第6部之間附有字母的各部及附表，屬於另外三個規管制度；知道它們的位置便已足夠。"), MAP_KEY)
    + traps(
        trap(("Where a word is defined depends on who uses it", "詞語在哪裏界定，視乎由誰使用"),
             ("Schedule 1 holds the terms used across the Ordinance. But terms that only one Part or Schedule needs are defined there instead: beneficial owner and business relationship in Schedule 2, ultimate owner in Part 5, authorized person in Part 3, specified decision in Part 6. The Schedule 1 page has the full lookup.",
              "附表1載有整條條例通用的詞語；但只供某一部或某一附表使用的詞語，則在該處界定：實益擁有人及業務關係在附表2，最終擁有人在第5部，獲授權人在第3部，指明決定在第6部。完整對照見附表1一頁。"),
             "s.2(1) · s.1 Sch. 2 · s.24 · s.8 · s.54"),
        trap(("Schedule 3 is yours; Schedules 3A, 3C and 3K are not", "附表3屬於你；附表3A、3C及3K則不是"),
             ("All four are fee schedules. Only Schedule 3 prices a money service operator's licence; the lettered ones price the trust or company service, virtual asset and precious metals regimes.",
              "四者都是收費表，但只有附表3訂明金錢服務經營者牌照的收費；附有字母的幾個附表，分別是信託或公司服務、虛擬資產及貴金屬制度的收費。"),
             ("Sch. 3 · Sch. 3A · Sch. 3C · Sch. 3K", "附表3 · 附表3A · 附表3C · 附表3K")),
    ))

# ---------------------------------------------------------------- B. who can change the rules
B_ = sec('rulebook', ["s.2(2)", "s.6 · s.7", "s.50 · s.51", "s.58 · s.76 · s.77"],
         ("Who can change the rules without a new Ordinance", "誰可在不另立條例的情況下修改規則"),
    P("Parts of the rulebook can be changed by a notice in the Gazette or by subsidiary rules, and the hand holding the pen changes from item to item. The right-hand columns are what to learn.",
      "規則的若干部分可藉憲報公告或附屬規則修改，而執筆者因項目而異。要記的是右邊兩欄。")
    + table([th("What can be changed", "可修改甚麼"), th("Who changes it", "由誰修改"), th("How", "方式")], [
        tr(td("Schedule 1, Part 2: the institutional definitions such as financial institution and relevant authority", "附表1第2部：金融機構、有關當局等機構類定義", "s.2(2)"),
           td("The <b>Secretary</b> for Financial Services and the Treasury", "財經事務及庫務局<b>局長</b>"),
           td("Notice published in the Gazette", "藉憲報公告")),
        tr(td("Schedule 1, Part 1: money service, money laundering, terrorist financing and the other general terms", "附表1第1部：金錢服務、洗錢、恐怖分子資金籌集等一般詞語", "s.2"),
           td("<b>No one, by notice.</b> The Ordinance gives no such power, so only an amending Ordinance can change them", "<b>任何人均不可藉公告修改。</b>條例並無賦予此權力，故只可由修訂條例修改", post=flag()),
           td("—", "—")),
        tr(td("Schedule 2, the CDD and record-keeping duties", "附表2，即盡職審查及備存紀錄的規定", "s.6"),
           td("The <b>Secretary</b>", "<b>局長</b>"),
           td("Notice published in the Gazette", "藉憲報公告")),
        tr(td("Schedule 3, the fees (for licences, approvals and register copies)", "附表3，即費用（牌照、批准及登記冊複本）", "s.50"),
           td("The <b>Commissioner</b>", "<b>關長</b>", post=flag()),
           td("Notice published in the Gazette", "藉憲報公告")),
        tr(td("Schedule 4, the Review Tribunal provisions", "附表4，即覆核審裁處的條文", "s.58(2)"),
           td("The <b>Secretary</b>", "<b>局長</b>"),
           td("Notice published in the Gazette", "藉憲報公告")),
        tr(td("Guidelines on how Schedule 2 operates, such as the Guideline on Anti-Money Laundering and Counter-Financing of Terrorism (For Money Service Operators)", "就附表2的施行而發出的指引，例如《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》", "s.7(1), (3), (6)"),
           td("The <b>relevant authority</b>, which for you is the Commissioner", "<b>有關當局</b>，就你而言即關長"),
           td("Published in the Gazette, and amendable from time to time. Not subsidiary legislation", "在憲報公布，並可不時修訂。並非附屬法例")),
        tr(td("Guidelines on imposing pecuniary penalties", "施加罰款的指引", "s.23 · s.45"),
           td("The <b>relevant authority</b> for Part 4 penalties; the <b>Commissioner</b> for Part 5 penalties", "第4部罰款由<b>有關當局</b>發出；第5部罰款由<b>關長</b>發出"),
           td("Must be published in the Gazette <b>before</b> the power is first used. Not subsidiary legislation", "須在首次行使權力<b>之前</b>在憲報公布。並非附屬法例")),
        tr(td("Regulations for the Ordinance as a whole, except Parts 5, 5A, 5B and 5C", "整條條例的規例（第5、5A、5B及5C部除外）", "s.77"),
           td("The <b>Chief Executive in Council</b>", "<b>行政長官會同行政會議</b>"),
           td("Regulations, which may include transitional and evidential provisions", "規例；可包括過渡性及關於證據的條文")),
        tr(td("Regulations for Part 5, your licensing regime", "第5部（你的發牌制度）的規例", "s.51 · s.26(2)"),
           td("The <b>Commissioner of Customs and Excise</b> personally. Section 26 bars him from delegating it; the only other function on that list is the power to delegate itself", "<b>海關關長</b>本人。第26條禁止他轉授此權力；該條所列的另一項職能是轉授權本身", "s.26(2)", post=flag()),
           td("Regulations. Breaching one is a trigger for Part 5 discipline", "規例。違反規例即觸發第5部的紀律行動")),
        tr(td("Rules on registering Tribunal orders in the Court of First Instance, and on the procedure for appeals", "在原訟法庭登記審裁處命令的規則，以及上訴程序的規則", "s.76"),
           td("The <b>Chief Justice</b>", "<b>終審法院首席法官</b>"),
           td("Rules", "規則")),
    ], minw=780)
    + traps(
        trap(("The Secretary or the Commissioner?", "局長還是關長？"), None, ("s.2(2) · s.6 · s.50 · s.58(2) · s.53ZTM · s.53ZVQ", "第2(2)條 · 第6條 · 第50條 · 第58(2)條 · 第5B部修訂附表3B至3F的條文 · 第5C部修訂附表3H至3K的條文"),
             vs=[(("The Secretary", "局長"), ("Schedule 1 Part 2, Schedule 2 and Schedule 4. The policy-level rules. (For other sectors the Secretary also amends Schedule 3B of the virtual asset regime and Schedules 3H and 3I of the precious metals and stones regime.)", "附表1第2部、附表2及附表4。屬政策層面的規則。（就其他行業而言，局長亦可修訂虛擬資產制度的附表3B，以及貴金屬及寶石交易商制度的附表3H及3I。）")),
                 (("The Commissioner", "關長"), ("Schedule 3: the fees for your own licensing regime, which he administers. He also amends Schedules 3J and 3K of the precious metals and stones regime, which do not apply to you.", "附表3：由他執行的發牌制度的費用。他亦可修訂貴金屬及寶石交易商制度的附表3J及3K，但該兩個附表不適用於你。"))]),
        trap(("What the Commissioner can never hand to someone else", "關長絕不可轉授的權力"),
             ("Under section 26 he may delegate any of his functions under the Ordinance in writing to a public officer employed in the Customs and Excise Department, except two: the power to delegate itself, and the power to make Part 5 regulations under section 51. Amending the Schedule 3 fees under section 50 is not on that list, so it can be delegated. Part 5C, the precious metals and stones regime, has its own separate list.",
              "根據第26條，海關關長可藉書面把其在本條例下的職能轉授予受僱於香港海關的公職人員，只有兩項除外：轉授權本身，以及根據第51條訂立第5部規例的權力。根據第50條修訂附表3費用並不在此列，故可以轉授。第5C部（貴金屬及寶石交易商制度）另有其本身的獨立規定。"),
             "s.26 · s.50 · s.51"),
    ))

# ---------------------------------------------------------------- C. government and immunity
C_ = sec('govt', ["s.3", "s.4", ("with s.21(9)", "另及第21(9)條"), "s.25"],
         ("The Government, and who is shielded from civil liability", "政府，以及誰可免負民事法律責任"),
    P("Two short sections, each with a qualification that changes the answer. Find the situation on the left.",
      "兩條簡短的條文，各有一項會改變答案的限制。先在左邊找出情況。")
    + table([th("The situation", "情況"), th("The general rule", "一般規則"), th("The qualification", "限制")], [
        tr(rh("The Government is the one dealing in money, or breaking a rule", "政府本身處理款項，或違反規定", "s.3"),
           td("The Ordinance applies to the Government, <b>except as otherwise expressly provided</b>.", "除另有<b>明文規定</b>外，本條例適用於政府。"),
           td("Two express exceptions matter to you. Part 5 does not apply to the Government at all, so it needs no licence. And the Part 4 pecuniary penalty, including the daily pecuniary penalty, cannot be imposed on the Government; a reprimand and an order to take remedial action still can.",
              "有兩項明文例外與你相關。第5部完全不適用於政府，故政府毋須領牌。第4部的罰款（包括按日罰款）不可向政府施加；但譴責及採取糾正行動的命令仍然可以。", "s.25 · s.21(9)", post=flag())),
        tr(rh("A public officer employed in the Customs and Excise Department, acting in good faith while carrying out an inspection, causes you loss", "受僱於香港海關的公職人員在視察期間真誠行事，令你蒙受損失", "s.4(1)"),
           td("The relevant authority and <b>any other person</b> incur no civil liability for acts or omissions in good faith in performing, or purporting to perform, a function under the Ordinance.", "有關當局及<b>任何其他人</b>在執行或本意是執行本條例的職能時，真誠地作出的作為或不作為，均無須招致民事法律責任。"),
           td("The shield is personal. The <b>Government's</b> own liability for what a public officer did is not affected, so a claim can still lie against the Government.", "該保障只屬個人。<b>政府</b>就公職人員的作為或不作為而須負的法律責任不受影響，故仍可向政府提出申索。", "s.4(2)")),
        tr(rh("The officer acted outside his actual powers, but honestly believed he was exercising them", "該人員超越實際權力行事，但真誠相信自己在行使權力", "s.4(1)"),
           td("Covered. The words are <b>performance or purported performance</b> of a function, so an honest mistake about the scope of a power is still protected.", "受保障。條文用語是<b>執行或本意是執行</b>職能，故對權力範圍的真誠誤解仍受保障。"),
           td("Good faith is the condition. An act done in bad faith falls outside the section.", "條件是真誠。以不真誠方式作出的作為不在保障之內。")),
        tr(rh("The question is whether an officer can be prosecuted", "問題是某人員會否被檢控", "s.4(1)"),
           td("Section 4 speaks only of <b>civil</b> liability.", "第4條只涉及<b>民事</b>法律責任。"),
           td("It gives no protection from criminal liability.", "它並不就刑事法律責任提供任何保障。")),
    ], minw=760)
    + traps(
        trap(("The Government is covered, then carved out", "條例適用於政府，但另有豁除"),
             ("Start from coverage: the Ordinance does apply to the Government. Only an express provision takes it out, and the two you need are the Part 5 licensing exemption and the ban on Part 4 money penalties.",
              "先記住適用：條例確實適用於政府。只有明文條文才可把政府豁除，而你需要記住的是第5部的發牌豁免，以及第4部罰款不適用於政府。"),
             "s.3 · s.25 · s.21(9)"),
        trap(("Immune from civil liability, not from the law", "免負民事法律責任，並非凌駕法律"),
             None, "s.4",
             vs=[(("What it covers", "涵蓋甚麼"), ("Civil liability, for good-faith acts in performing or purporting to perform a function.", "真誠執行或本意是執行職能時的民事法律責任。")),
                 (("What it does not", "不涵蓋甚麼"), ("Criminal liability, bad-faith acts, and the Government's own liability for its officers.", "刑事法律責任、不真誠的作為，以及政府就其人員的作為而須負的法律責任。"))]),
    ))

P1_NAV = [('map', 'The whole Ordinance', '條例全貌'), ('rulebook', 'Who can change the rules', '誰可修改規則'),
          ('govt', 'Government and immunity', '政府與豁免')]
P1_BODY = A + B_ + C_
