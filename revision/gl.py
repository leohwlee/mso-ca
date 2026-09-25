# The C&ED guidelines that sit beside the Ordinance: the Licensing Guide, the
# Competence Assessment notes, the two fit-and-proper guidelines, the Business Plan
# and AML/CFT Policy guidelines, and the two penalty guidelines. Only what they add
# to the AMLO and the AML/CFT Guideline is kept; statutory rules link to their pages.
from ui import *
from bl_core import _runs
from gl_fig import (LG, GN, fig_route, ROUTE_KEY, fig_pass, PASS_KEY, fig_renew, RENEW_KEY,
                    fig_scale, SCALE_KEY)


def FPG(p):
    return (f"F&P Guideline ¶{p}", f"《適當人選指引》第{_runs(p)}段")


def FPS(p):
    return (f"Supplementary F&P Guideline ¶{p}", f"《適當人選補充指引》第{_runs(p)}段")


def BPG(i):
    return (f"Business Plan guidelines item {i}", f"《業務計劃指引》第{_runs(i)}項")


def APG(i):
    return (f"AML/CFT Policy guidelines item {i}", f"《打擊洗錢政策指引》第{_runs(i)}項")


def DFG(p):
    return (f"Disciplinary Fining Guideline ¶{p}", f"《紀律處分罰款指引》第{_runs(p)}段")


def DAG(p):
    return (f"Disciplinary Action Guideline ¶{p}", f"《施加罰款紀律行動指引》第{_runs(p)}段")


def cc(*cs):
    """Join several citations into one."""
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


def vd(ch):
    return f'<td class="verdict">{ch}</td>'


def dash_td():
    return '<td class="faint">—</td>'


def _cell(x):
    """An (en, tc) pair, optionally followed by a citation and a post-text marker."""
    en, tc = x[0], x[1]
    cite = x[2] if len(x) > 2 else None
    post = x[3] if len(x) > 3 else ''
    return B(en, tc) + post + cite_html(cite)


def numreq_c(rows, heading=True, minw=760):
    """numreq() with a citation allowed in any cell: each of the three text cells is
    (en, tc[, cite[, post]]); the last element of a row is the requirement's citation."""
    head = ('<thead><tr>'
            f'<th>{B("The number", "數字")}</th>'
            f'<th>{B("What it requires", "規定甚麼")}</th>'
            f'<th>{B("When it applies", "何時適用")}</th>'
            f'<th>{B("If it is missed", "未達標的後果")}</th>'
            '</tr></thead>')
    body = ''.join(
        '<tr>'
        f'<td class="numreq"><span class="answer" tabindex="0">{B(*num)}</span></td>'
        f'<td>{_cell(req)}{cite_html(cite)}</td>'
        f'<td>{_cell(when)}</td>'
        f'<td class="cons">{_cell(cons)}</td>'
        '</tr>'
        for num, req, when, cons, cite in rows)
    h3_ = '<h3>' + B("The numbers in this section, and what happens if you miss them",
                     "本節的數字，以及未達標的後果") + '</h3>' if heading else ''
    return h3_ + f'<div class="tbl"><table style="min-width:{minw}px">{head}<tbody>{body}</tbody></table></div>'


OKP = chip("suitable", "適合", 'ink')
BADP = chip("not suitable", "不適合")
SAMPLE4 = ("Sample question 4", "參考試題4")
# a marker for a contrast that only the English text draws (the combined view shows it too)
FLAG_EN = f'<span class="only-en">{flag()}</span>'

# ---------------------------------------------------------------- A. the route
A = sec('route', [("Licensing Guide", "《牌照指引》"), ("¶5.1–5.11", "第5.1至5.11段"), ("CA Notes ¶4.5", "《能力評核須知》第4.5段")],
        ("From application to licence", "由申請到領牌"),
    P("Follow the left-hand column from top to bottom. On the right are C&amp;ED's own checks, which run alongside, and the ways an application stalls or ends before the Commissioner decides; the two boxes at the foot are his decision.",
      "由上而下跟着左欄走。右邊是海關同步進行的查核，以及申請在關長作出決定前停頓或終結的情況；底部兩個方格是他的決定。")
    + fig(fig_route, ("The vetting on the right runs while you wait, which is why the Licensing Guide will not promise a processing time: it depends on your documents, the inspection, other authorities' records and the Assessment.",
                        "右邊的審查在你等候期間同步進行，因此《牌照指引》不會承諾處理時間：時間取決於你的文件、實地視察、其他機構的紀錄及能力評核。"), ROUTE_KEY)
    + h3("Who does what, by type of business", "按業務類別劃分的角色")
    + table([th("If the applicant is", "如申請人是"), th("Who attends the interview", "誰出席會面"),
             th("Who may sit the Assessment", "誰可應考能力評核"), th("Who files a fit-and-proper declaration", "誰須遞交適當人選聲明表格")], [
        tr(rh("A sole proprietorship", "獨資經營"),
           td("The sole proprietor", "獨資經營者", LG("5.5(a)")),
           td("The sole proprietor", "獨資經營者", GN("4.2")),
           td("The proprietor and each ultimate owner, on Form 3A", "經營者及每名最終擁有人，使用表格3A", LG("5.7–5.8"))),
        tr(rh("A partnership", "合夥"),
           td("A partner or staff member authorised in writing by <b>every</b> partner", "獲<b>每一名</b>合夥人書面授權的合夥人或員工", LG("5.5(b)")),
           td("Partners only, with no more than three nominated", "只限合夥人，獲提名者不得超過三名", GN("4.2"), post=flag()),
           td("Each partner and each ultimate owner: Form 3A for an individual, 3B for a corporate partner", "每名合夥人及每名最終擁有人：個人用表格3A，法團合夥人用表格3B", LG("5.7–5.8"))),
        tr(rh("A corporation", "法團"),
           td("A director or staff member authorised in writing by the board", "獲董事局書面授權的董事或員工", LG("5.5(c)")),
           td("The sole director, or up to three directors who are natural persons", "唯一董事，或最多三名屬自然人的董事", GN("4.2"), post=flag()),
           td("Each director and each ultimate owner: Form 3A or 3B", "每名董事及每名最終擁有人：表格3A或3B", LG("5.7–5.8"))),
    ], note=B("Appendix I to Form 3A is signed in front of a witness: an authorized officer of the C&amp;ED, a practising professional such as a solicitor, accountant or auditor, a notary public, or a Justice of the Peace. The witness checks the particulars against the declarant's original identity document and certifies them.",
              "表格3A的附錄I須在見證人面前簽署。見證人可以是海關的獲授權人員、執業專業人士（例如事務律師、會計師或核數師）、公證人或太平紳士。見證人須以聲明人身份證明文件的正本核對所載資料並作出證明。") + ' ' + cite_html(LG("5.8")), minw=860)
    + numreq_c([
        (("2 photographs", "兩張照片"),
         ("4R size, 102 × 152 mm: one of the inside, such as the counter or office, one of the outside, such as the signboard", "4R尺寸（102 × 152毫米）：一張顯示內部（例如櫃枱或辦事處），一張顯示外部（例如招牌）"),
         ("Each particular premises, and each separate place used as the local management office or the local place for storage of books and records; at grant and at renewal", "每個特定處所，以及另設作本地管理辦事處或本地儲存帳目及紀錄地點的每個地點；批給及續期時均適用"),
         ("Documents still missing after the specified period make the application invalid", "逾指明期限仍欠交文件，申請即屬無效"),
         LG("5.1, 6.3")),
        (("30 days", "30日"),
         ("Your nominees sit the Assessment", "獲提名人士應考能力評核"),
         ("Counted from the interview, for a new application", "新申請：自會面起計"),
         ("Not attending the designated session may result in refusal of the licence application; at renewal it will result in rejection (<a href=\"#renewal\">renewal countdown</a>)",
          "未有出席指定時段的評核，會導致相關申請被拒絕；續牌時亦然（見<a href=\"#renewal\">續牌倒數</a>）",
          LG("5.4, 6.2"), FLAG_EN),
         cc(GN("4.5"), LG("5.4"))),
        (("after 30 days", "30日後"),
         ("One retake if nobody passed", "如無人合格，可重考一次"),
         ("Counted from the result notice", "自成績通知發出起計"),
         ("If still nobody passes, the Commissioner may find you not fit and proper and refuse", "如仍無人合格，關長可裁定你並非適當人選而拒絕申請"),
         GN("4.5")),
        (("HK$1,000,000 + 2 years", "港幣100萬元 + 2年"),
         ("Do not operate a money service before you hold a licence", "未領牌前不得經營金錢服務"),
         ("On conviction on indictment. Tried summarily: HK$100,000 and 6 months", "循公訴程序定罪。循簡易程序定罪：港幣10萬元及監禁6個月"),
         ("Operating without a licence is an offence", "無牌經營即屬犯罪"),
         cc(LG("2.7, 2.11"), "s.29")),
        (("HK$50,000 + 6 months", "港幣5萬元 + 6個月"),
         ("Do not leave a material particular out of a statement in a grant or renewal application so that the statement becomes false or misleading, such as premises that must be registered. Making a false or misleading statement carries the same penalty", "申請批給或續期時，不得在陳述中遺漏要項，以致該陳述成為虛假或具誤導性，例如須登記的處所。作出虛假或具誤導性的陳述，罰則相同"),
         ("When you know, or are reckless as to whether, it is left out", "你知道該陳述遺漏該要項，或罔顧該陳述是否遺漏該要項"),
         ("An offence under section 52", "屬第52條所訂罪行"),
         cc(LG("4.9"), "s.52(1)–(3)")),
    ])
    + traps(
        trap(("Staff can stand in at the interview (partnerships and corporations only), never at the Assessment", "員工可代為出席會面（只限合夥及法團），但不可代考能力評核"), None, cc(LG("5.5"), GN("4.2")),
             vs=[(("The interview", "會面"), ("A sole proprietor must attend in person. For a partnership or corporation, partners, directors or staff members may attend if every partner or the board has authorised them in writing.", "獨資業務須由獨資經營者親自出席。合夥或法團可由合夥人、董事或員工出席，但須獲每一名合夥人或董事局書面授權。")),
                 (("The Assessment", "能力評核"), ("Only senior management: the sole proprietor, partners, or directors who are natural persons, and no more than three.", "只限高級管理層：獨資經營者、合夥人，或屬自然人的董事，最多三人。"))]),
        trap(("Invalid and refused are different endings", "無效與被拒是兩種不同的結局"), None, cc(LG("5.4"), LG("5.10–5.11")),
             vs=[(("Invalid", "無效"), ("Information or documents were not produced within the specified period. The application is simply not processed.", "未能在指明期限內提供資料或文件。申請只是不獲處理。")),
                 (("Refused", "被拒"), ("The Commissioner decides against you and says so in writing. You have 21 days to take it to the Review Tribunal.", "關長作出不利於你的決定並以書面通知。你有21日時間向覆核審裁處申請覆核。"))]),
        trap(("A shop that takes foreign currency is not a money changer", "收取外幣的商店不是貨幣兌換商"),
             ("The Licensing Guide spells out an exclusion the statutory definition leaves unsaid: exchanging currency only incidentally to a main business, such as a retail shop accepting foreign currency from customers, is not a money changing service. The hotel exception in the Ordinance itself is on the Schedule 1 page.",
              "《牌照指引》明確列出法定定義沒有明言的排除情況：只屬主要業務附帶部分的貨幣兌換，例如零售商店向顧客收取外幣，不屬貨幣兌換服務。條例本身的酒店例外，見附表1一頁。"),
             LG("2.3")),
        trap(("Fees: paid with the application, charged again at each renewal, never refunded", "費用：須附隨申請，每次續期再收，概不退還"), None,
             cc(LG("2.8, 4.14"), "s.30(1)(b) · s.31(2)", ("Sch. 3 items 4–5", "附表3第4至5項")),
             vs=[(("Refunds", "退款"), ("The application fee and the fit-and-proper fee are not refunded, whether the application is approved or refused.", "申請費及適當人選判定費，不論申請獲批或被拒，均不獲退還。")),
                 (("When they are paid", "何時繳付"), ("A grant or renewal application must be accompanied by the Schedule 3 fee, and a renewal must be made not later than 45 days before expiry.", "批給或續期的申請須附隨附表3指明的費用；續期申請須在牌照期滿前45日或之前提出。")),
                 (("How often", "繳付次數"), ("The fit-and-proper fee is charged for each person subject to the test, on a grant and again on each renewal. The amounts are on the <a href=\"#s3-fees\">Schedule 3 page</a>.", "適當人選判定費按每一個須判定是否適當人選的人收取，批給時收取，每次續期亦再收取。金額見<a href=\"#s3-fees\">附表3一頁</a>。"))]),
    ))

# ---------------------------------------------------------------- B. premises
B_ = sec('premises', [("Licensing Guide", "《牌照指引》"), ("¶4.4–4.11", "第4.4至4.11段")],
         ("Where you may trade, and the two places C&amp;ED must be able to reach", "在哪裏經營，以及海關必須能夠找到的兩個地方"),
    P("Use the first two tables to decide whether you have particular premises and whether they will pass. That answer decides whether you also need a local management office; every applicant needs the local place for storage of books and records. The third table sets the two side by side.",
      "先用首兩個表判斷你是否有特定處所，以及該處所能否通過審核。這個答案決定你是否亦須設立本地管理辦事處；所有申請人都必須有本地儲存帳目及紀錄地點。第三個表把兩者並列比較。")
    + table([th("The situation", "情況"), th("Particular premises?", "屬特定處所？"), th("What follows", "後果")], [
        tr(td("You occupy the premises to run the money service, advertise them as the place to meet customers, a signboard included, and control them as landlord or tenant",
              "你佔用該處所經營金錢服務、宣傳其為會見客戶的地方（包括展示招牌），並以業主或租戶身分經常控制該處所", LG("4.4")),
           vd(YES), td("Register it. Each additional premises goes into the same application, with its own fee", "須登記。其他處所一併列入同一申請，每個另繳費用", LG("2.6"))),
        tr(td("You are only a visitor or customer there: a restaurant, a bank, or an accountant's or solicitor's office where your papers are processed",
              "你只是該處所的訪客或顧客：食肆、銀行，或為處理公司文件而到的會計師行或律師行", LG("4.4")),
           vd(NO), td("Nothing to register for that place", "該處所毋須登記")),
        tr(td("Door-to-door service, meeting customers at their own office, or dealing on mobile devices", "上門服務、在顧客的辦事處會見顧客，或只使用流動電子設備進行交易", LG("4.5")),
           vd(NO), td("You operate without particular premises: the application must give a local management office, a correspondence address and a local place for storage of books and records",
                      "你屬在沒有特定處所的情況下經營：申請須提供本地管理辦事處、通訊地址及本地儲存帳目及紀錄地點", LG("4.5"))),
    ], minw=760)
    + table([th("The premises", "處所"), th("Suitable?", "是否適合？")], [
        tr(td("Accessible to C&amp;ED officers for their functions under the regime", "海關人員可進入以執行監管制度下的職能", LG("4.6")), vd(OKP)),
        tr(td("In a mixed commercial and residential building", "位於混合式商住樓宇", LG("4.6, 4.10")),
           td("Only with every occupant's written consent to inspection, the statutory rule on the <a href=\"#p5-fitproper\">Part 5 page</a>",
              "須取得每名佔用人同意視察的書面同意；此為法定規則，見<a href=\"#p5-fitproper\">第5部一頁</a>")),
        tr(td("In a wholly residential building", "位於純住宅樓宇", LG("4.6")), vd(BADP)),
        tr(td("Already used by another MSO, or declared by another applicant for a grant or renewal", "現由另一名金錢服務經營者使用，或另一名申請人已就批給或續期申請填報該處所", LG("4.6")), vd(BADP)),
        tr(td("Reachable only through another business's area, with its occupier's permission or help", "須經另一業務佔用的範圍，並獲其佔用人准許或協助才能進入", LG("4.6")), vd(BADP)),
        tr(td("Its signboard shows a business name different from the one on the Business Registration Certificate you submitted", "招牌展示的業務名稱，與你遞交的商業登記證上的名稱不同", LG("4.6"), post=flag()), vd(BADP)),
        tr(td("Shared with another business", "與其他業務共用", LG("4.8")),
           td("Only if your money service is clearly partitioned and distinguished from it. Sharing with another MSO is never accepted",
              "你的金錢服務須設有明顯分隔，與其他業務清楚區分。與另一名金錢服務經營者共用處所一概不獲接納")),
    ], minw=640)
    + table([th("", ""), th("Local management office", "本地管理辦事處"), th("Local place for storage of books and records", "本地儲存帳目及紀錄地點")], [
        tr(rh("Who needs one", "誰須設立"),
           td("Only an operator <b>without</b> particular premises", "只限<b>沒有</b>特定處所的經營者", LG("4.7"), post=flag()),
           td("<b>Every</b> applicant and licensee", "<b>所有</b>申請人及持牌人", LG("4.10"))),
        tr(rh("What it is", "是甚麼"),
           td("A physical office in Hong Kong that is also your correspondence address. C&amp;ED officers must be able to reach it in person and by telephone, and it receives their circulars and notices",
              "位於香港的實體辦事處，兼作通訊地址。海關人員須能親身前往及以電話聯絡，並用作接收海關的通函及通知書"),
           td("A physical place in Hong Kong holding the full set of books and records of your money service transactions, under your control so officers can get at them",
              "位於香港、存放全套金錢服務交易帳目及紀錄的實體地點，須由你控制，以便海關人員查閱", LG("4.11"))),
        tr(rh("Who must be there", "誰須在場"),
           td("The sole proprietor, a partner, a director, an ultimate owner or the compliance officer", "獨資經營者、合夥人、董事、最終擁有人或合規主任"),
           td("None stated, but it must be under your control", "沒有訂明，但須由你控制")),
        tr(rh("Never accepted", "一概不獲接納"),
           td("A residential address, or the premises of a service provider such as a company secretary, accountant or solicitor", "住址或住宅處所，或服務供應商（例如公司秘書事務所、會計師行或律師行）的處所", post=flag()),
           td("The same", "同上")),
        tr(rh("Landlord", "業主"),
           td("Permission to use it for the money service business, in the tenancy agreement or a letter from the landlord", "准許用作金錢服務業務，須載於租約或業主發出的准許信"),
           td("The same", "同上")),
        tr(rh("Missing when you apply", "申請時欠缺"),
           td("An invalid application, not processed, or a refusal", "申請視作無效、不獲處理，或被拒絕"),
           td("The same", "同上")),
        tr(rh("Not kept up once licensed", "持牌後未能維持"),
           td("Failure will result in suspension and/or revocation, including when the office fails to serve as the point of contact with C&amp;ED, such as when none of the licensee's personnel is there",
              "未能維持或會導致暫時吊銷及／或撤銷牌照，包括本地管理辦事處未能作為與海關溝通的聯絡點，例如持牌人的人員並不在場",
              LG("4.7")),
           td("Failure will result in suspension and/or revocation, though the list of grounds says the Commissioner may", "未能維持將會導致暫時吊銷及／或撤銷牌照，但該指引列出的理由則指關長可以這樣做", cc(LG("4.11"), LG("7.1(d)")))),
    ], minw=760, cls='cmp')
    + traps(
        trap(("A management office is only for operators without premises", "本地管理辦事處只適用於沒有特定處所的經營者"),
             ("The official sample paper tests exactly this: the statement \"The licensees operating with or without particular premises must maintain a LMO\" is false. Every licensee needs a local place for storage of books and records; only one trading without particular premises needs the management office.",
              "官方參考試題正好考這一點：「無論持牌人會或不會在特定處所經營金錢服務，都須維持本地管理辦事處」是錯誤的。每名持牌人都須有本地儲存帳目及紀錄地點；只有在沒有特定處所的情況下經營的人才須設本地管理辦事處。"),
             cc(LG("4.7, 4.10"), SAMPLE4)),
    ))

# ---------------------------------------------------------------- C. standing requirements
C_ = sec('standing', [("Licensing Guide", "《牌照指引》"), ("¶4.15 · ¶7.1 · ¶11.1", "第4.15、7.1、11.1段")],
         ("What you must have in place, from the application onwards", "由申請起必須具備的條件"),
    P("Each row is something the Licensing Guide expects you to keep. Read across: what it takes, what happens if it is missing when you apply, and what happens if it lapses once you hold the licence.",
      "每一行是《牌照指引》要求你維持的事項。橫向閱讀：要求甚麼、申請時欠缺的後果，以及持牌後失去的後果。")
    + table([th("Requirement", "要求"), th("What it takes", "要求內容"), th("Missing when you apply", "申請時欠缺"), th("Lost once licensed", "持牌後失去")], [
        tr(rh("Compliance officer and MLRO", "合規主任及洗錢報告主任", LG("4.15(a), 11.3")),
           td("A competent compliance officer, the focal point for your AML/CFT systems, and a money laundering reporting officer, the central point for suspicious transaction reports. Both must be your <b>employees</b> under the Employment Ordinance (Cap. 57), unless a sole proprietor, partner, director or ultimate owner holds the post. Appointments are notified on the supplementary information form",
              "合資格的合規主任，作為監督打擊洗錢制度的中心點；以及洗錢報告主任，作為報告可疑交易的中央聯絡點。兩者均須是根據《僱傭條例》（第57章）受聘於你的<b>僱員</b>，除非由獨資經營者、合夥人、董事或最終擁有人擔任。委任須以補充資料表格具報", post=flag()),
           td("A ground for refusal. The application must include copies of both officers' Hong Kong identity cards and valid employment contracts, and proof of their residential address issued within the three months before the application date",
              "拒絕申請的理由。申請須附兩名主任的香港身份證複本、有效僱傭合約複本，以及在申請日期前三個月內發出的住址證明複本", LG("5.10(g), 16.3")),
           td("A ground for suspension or revocation; a change goes on Form 6 within one month", "暫時吊銷或撤銷牌照的理由；如有改變，須於一個月內以表格6具報", LG("7.1(i), 9.1(n), 9.2"))),
        tr(rh("Business registration", "商業登記", LG("4.15(c)")),
           td("A valid Business Registration Certificate from the Commissioner of Inland Revenue, under Cap. 310", "由稅務局局長根據第310章發出的有效商業登記證"),
           td("The application is not processed", "申請不獲處理"),
           td("Suspension or revocation", "暫時吊銷或撤銷牌照")),
        tr(rh("The bank account", "銀行帳戶", LG("11.1(j)")),
           td("Any account used for the business must be in the name of the licensee's company, the sole proprietor, a partner, a director or an ultimate owner, never a third party's. With no account at all, the Business Plan must explain how the service runs without one",
              "用於業務的帳戶必須屬持牌人公司、獨資經營者、合夥人、董事或最終擁有人名下，絕不可屬第三方。如完全不用銀行帳戶，業務計劃須說明如何在沒有帳戶的情況下經營", BPG("8"), post=flag()),
           td("Proof of ownership, and the bank's acknowledgement that the account is used for money service, go with the application", "申請須附帳戶擁有權證明，以及銀行確認該帳戶用於金錢服務業務的文件", LG("16.3")),
           td("A change of account goes on Form 6 within one month", "更改帳戶須於一個月內以表格6具報", LG("9.1(k), 9.2"))),
        tr(rh("Someone who has passed the Assessment", "已在能力評核取得合格成績的人", GN("8.1–8.2")),
           td("At least one of your senior management, the sole proprietor, a partner or a director, must <b>pass</b> the Assessment",
              "高級管理層中必須有最少一名成員（獨資經營者、合夥人或董事）在能力評核<b>取得合格成績</b>",
              cc(LG("4.15(b)"), GN("3.1"))),
           td("A ground for refusal if nobody attends or nobody passes", "如無人應考或無人合格，屬拒絕申請的理由", LG("5.10(i)–(j)")),
           td("The company's pass lapses automatically; the <a href=\"#ca\">Assessment section</a> has the 30-day chance to sit again", "公司的合格資格自動失效；30日內再考的機會見<a href=\"#ca\">能力評核一節</a>")),
        tr(rh("Periodic returns", "定期申報表", LG("11.2")),
           td("Lodged within 2 weeks beginning from each half year, in the form and manner the Commissioner specifies. Each return covers the half year just ended: the January to June return is lodged from 1 July. Since 2025 they are half-yearly and online only: see the <a href=\"#ci-returns\">Circulars page</a>",
              "每半年開始後的兩星期內，按關長指明的格式及方式遞交。每份申報表涵蓋剛結束的半年：1月至6月的申報表由7月1日起遞交。自2025年起每半年遞交一次，並只接受網上遞交：見<a href=\"#ci-returns\">通函一頁</a>",
              ("Circular 30 May 2025", "2025年5月30日通函")),
           dash_td(),
           td("Late filing may result in the suspension and/or revocation of the licence",
              "未能按時遞交定期申報表，將會導致牌照被暫時吊銷及／或撤銷", cc(LG("7.1(f), 11.2"), ("Circular 30 May 2025", "2025年5月30日通函")))),
        tr(rh("A money service that actually runs", "確實經營的金錢服務", LG("7.1(g)")),
           td("A genuine intention and readiness to carry on the business you applied for", "確實有意並已準備經營申請時所述的業務", FPS("6(f)")),
           td("Weighed in the fitness test", "在適當人選判定中考慮"),
           td("A licence never used for a money service is a ground for suspension or revocation", "從未用於提供金錢服務的牌照，屬暫時吊銷或撤銷的理由")),
    ], minw=900)
    + traps(
        trap(("A director's account is fine; a friend's is not", "董事的帳戶可以，朋友的帳戶不可以"),
             ("The account must be in the name of the licensee or of someone who owns or runs it: the sole proprietor, a partner, a director or an ultimate owner. The Business Plan guidelines put the other half bluntly: no third party bank account is allowed.",
              "帳戶必須屬持牌人，或擁有或經營持牌人的人（獨資經營者、合夥人、董事或最終擁有人）名下。《業務計劃指引》亦直言：不得使用第三方銀行戶口。"),
             cc(LG("11.1(j)"), BPG("8"))),
        trap(("Employees, unless a proprietor, partner, director or ultimate owner takes the post", "須為僱員，除非由獨資經營者、合夥人、董事或最終擁有人擔任"),
             ("The compliance officer and the MLRO must be employed by you within the meaning of the Employment Ordinance. The one exception is a sole proprietor, partner, director or ultimate owner doing the job.",
              "合規主任及洗錢報告主任必須是按《僱傭條例》受聘於你的僱員。唯一例外是由獨資經營者、合夥人、董事或最終擁有人擔任。"),
             LG("4.15(a)")),
    ))

# ---------------------------------------------------------------- D. business plan and policy
D_ = sec('plans', [("Business Plan guidelines", "《業務計劃指引》"), ("AML/CFT Policy guidelines", "《打擊洗錢政策指引》"), ("version 12/2019", "2019年12月版")],
         ("What the Business Plan and the AML/CFT Policy must cover", "業務計劃及打擊洗錢政策須涵蓋甚麼"),
    P("The two sets of guidelines read your application from two sides. Each row is one topic: the middle column is what the Business Plan must describe, the right-hand column what the AML/CFT Policy must set out on the same topic. A dash means that set of guidelines does not ask.",
      "兩份指引從兩個角度審視你的申請。每一行是一個主題：中間一欄是業務計劃須描述的內容，右欄是打擊洗錢政策就同一主題須訂明的內容。橫線表示該指引沒有要求。")
    + table([th("Topic", "主題"), th("Business Plan: 17 items", "業務計劃：17項"), th("AML/CFT Policy: 19 items", "打擊洗錢政策：19項")], [
        tr(rh("Who you are", "你是誰"),
           td("Company and business names, website, logo and trademark; history, source of capital and any group that controls you; key executives' nationality, career, qualifications and education; where key decisions are made, and any back office in or outside Hong Kong",
              "公司及業務名稱、網址、標誌及商標；公司歷史、資本來源及控制你的任何集團；主要行政人員的國籍、工作經驗、資歷及學歷；主要決策的所在地，以及在香港境內或境外的任何後勤辦事處", BPG("1–4")),
           td("An introduction: all reasonable measures against breaching Parts 2 and 3 of Schedule 2; procedures under section 19(3) of Schedule 2; a risk-based approach; the compliance officer and MLRO named, with the reporting line",
              "引言：採取一切合理措施防止違反附表2第2及3部；按附表2第19(3)條訂立的程序；風險為本的方法；列明合規主任及洗錢報告主任姓名，以及匯報路線", APG("1"))),
        tr(rh("Customers and markets", "客戶及市場"),
           td("Expected customers: where they are, their nationality, and how you make contact", "預期客戶：所在地、國籍及接觸方式", BPG("5")),
           td("Target customers; target jurisdictions for inward and for outward remittances; the main currencies you deal in", "目標客戶；匯入及匯出匯款的目標司法管轄區；主要處理的貨幣", APG("6–8"))),
        tr(rh("How the business runs", "業務如何運作"),
           td("The whole transaction process in Hong Kong, from order to movement of funds, compliance and record keeping; each product, its launch date and full delivery channel through every foreign agent or MSO, with the service agreements; how customer funds are protected if an agent fails",
              "在香港的整個交易流程，由落單、資金流動，到合規及備存紀錄；每項產品、推出時間，以及經每個外地代理人或金錢服務經營者的完整交付渠道，連同服務協議；代理人未能履行時如何保障客戶資金", BPG("6–7")),
           td("Distribution channels, with the percentage of face-to-face and non-face-to-face business; how you make money; the payment, fund-flow and settlement system for remittances and wire transfers, with checks on counterparties and on overseas branches and agents",
              "分銷渠道，連同面對面及非面對面交易的百分比；收入模式；匯款及電傳轉帳的支付、資金流動及結算系統，以及對交易對手、海外分行及代理人的查核", APG("5, 9–10"))),
        tr(rh("Money", "資金"),
           td("Every bank account used, with its number and owner, and no third-party account; if you think you need no bank account, a detailed account of how you will provide the service without one; expected profit margin and turnover for each product over the next two years, and running capital",
              "所用的每個銀行戶口的號碼及擁有人，不得使用第三方銀行戶口；如認為無需開設銀行戶口，須詳述如何在沒有銀行戶口的情況下提供金錢服務；未來兩年每項產品的預期利潤率及營業額，以及營運資金", BPG("8–9")),
           dash_td()),
        tr(rh("People and structure", "人員及架構"),
           td("Group charts inside and outside Hong Kong; any other business on your premises and its links to you; the management team and staff: numbers, roles, full or part time, reporting lines",
              "香港境內及境外的集團架構圖；在你處所經營的其他業務及其與你的關係；管理團隊及僱員：人數、職位、全職或兼職、報告流程", BPG("10–12")),
           td("The compliance function: management oversight, the compliance department and any committee, the compliance officer's duties; the suspicious transaction reporting procedure and the MLRO's role",
              "合規職能：管理層監督、合規部門及任何委員會、合規主任的職責；可疑交易報告程序及洗錢報告主任的角色", APG("13–14"))),
        tr(rh("Systems and outsiders", "系統及外判"),
           td("Outsourced AML/CFT services, such as external audit or a specified intermediary; the computerised and screening systems, naming the vendor",
              "外判的打擊洗錢服務，例如外聘審核或指明中介人；電腦化及篩查系統，並列明供應商名稱", BPG("13–14")),
           td("Screening against targeted financial sanctions on terrorism and on proliferation, and for politically exposed persons; the AML/CFT audit function, internal or external",
              "篩查與恐怖主義及擴散有關的針對性金融制裁，以及政治人物；內部或外聘的打擊洗錢審核職能", APG("11, 15"))),
        tr(rh("Other relationships", "其他關係"),
           td("Acting as agent or principal for another MSO or an overseas business; third-party payment platforms such as digital wallets; anyone moving physical cash for you, locally or across the boundary; any other regulator that supervises you or your group",
              "為另一金錢服務經營者或海外業務擔任代理人或主事人；第三方支付平台，例如電子錢包；為你在本地或跨境運送實體現金的人；監管你或你所屬集團的任何其他監管者", BPG("15–17")),
           td("Cooperation with C&amp;ED inspections and investigations, and with other law enforcement", "配合海關的例行視察及調查，以及其他執法機構", APG("19"))),
        tr(rh("Risk and CDD", "風險及盡職審查"),
           dash_td(),
           td("ML, TF and PF explained, with the three stages of money laundering, warning signs, suspicious transaction reports and tipping off; CDD thresholds, including one-off transactions for walk-in customers and linked transactions; customer risk assessment; simplified and enhanced due diligence; source of funds and of wealth; third-party funding; ongoing monitoring; records retrievable within a reasonable time, say one day; your risk assessment method",
              "解釋洗錢、恐怖分子資金籌集及擴散資金籌集，包括洗錢的三個階段、警示跡象、可疑交易報告及通風報訊；盡職審查門檻，包括街客的一次過交易及有關連的交易；客戶風險評估；簡化及更嚴格的盡職審查；資金來源及財富來源；第三方資助；持續監察；可在合理時間內（例如一日）檢索紀錄；你的風險評估方法", APG("2–3, 12"))),
        tr(rh("Training and extras", "培訓及其他"),
           dash_td(),
           td("A training programme so staff can carry out their own AML/CFT duties, covering their personal statutory obligations and the consequences of failing to report suspicious transactions; your statutory obligations and the consequences of breaching the legislation; your AML/CFT policies and procedures; new and emerging ML/TF techniques, methods and trends; and \"other issues set out in para. 9.7 of the AML Guideline\". That is the template's 2019 cross-reference: in the June 2023 Guideline the topics are in ¶9.4–9.5 (<a href=\"#g8-who\">Guideline Ch. 8–9 page</a>) and ¶9.7 is about training records (<a href=\"#g8-cycle\">same page</a>). Test staff understanding and their ability to recognise suspicious transactions; keep records of who was trained, when, and the type of training. Also: other internal controls; supporting forms such as internal report and onboarding forms",
              "培訓計劃，令職員能執行本身的打擊洗錢及恐怖分子資金籌集職務，涵蓋職員本身的法定責任及未有舉報可疑交易的後果；你的法定責任及違反相關法例的後果；你的打擊洗錢及恐怖分子資金籌集政策及程序；洗錢及恐怖分子資金籌集的嶄新及新興技巧、方法及趨勢；以及「《打擊洗錢指引》第9.7段所載列的其他事宜」。這是該範本2019年的交互參照：在2023年6月版指引中，培訓範疇載於第9.4至9.5段（見<a href=\"#g8-who\">指引第8至9章一頁</a>），第9.7段則關乎培訓紀錄（見<a href=\"#g8-cycle\">同一頁</a>）。測試職員對上述事宜的理解及辨認可疑交易的能力；記錄受訓人員、受訓時間及培訓類別。另須列明其他內部監控；內部舉報表格及客戶開戶表格等輔助文件", APG("16–18"))),
    ], minw=900, cls='cmp')
    + numreq_c([
        (("2 years", "2年"),
         ("Forecast the profit margin and turnover of each product and service, and state the running capital", "預測每項產品及服務的利潤率及營業額，並列明營運資金"),
         ("In the Business Plan", "於業務計劃內"),
         ("An application whose Business Plan does not follow the guidelines can be refused", "業務計劃未按指引提交的申請可被拒絕", LG("5.10(f)")),
         BPG("9")),
        (("1 month", "1個月"),
         ("Confirm in writing, inside the Business Plan, that you know you must notify any change in particulars within one month, and will", "在業務計劃內以書面確認，你知悉並會遵守在一個月內具報詳情改變的法定要求"),
         ("Every Business Plan, at grant and renewal", "每份業務計劃，批給及續期時均適用"),
         ("Missing information may delay or hinder the processing of your application", "欠缺資料可能延誤或妨礙申請的處理"),
         ("Business Plan guidelines, introduction", "《業務計劃指引》引言")),
        (("HK$200,000", "港幣200,000元"),
         ("The AML/CFT Policy guidelines' own example of a high-risk situation needing enhanced due diligence: a walk-in customer remitting HK$200,000 in cash to the Mainland",
          "《打擊洗錢政策指引》自行列舉須採取更嚴格盡職審查的高風險例子：街客以現金匯款港幣200,000元往內地"),
         ("In the EDD part of the AML/CFT Policy, beside PEPs, non-face-to-face business and high-risk countries", "於打擊洗錢政策中有關更嚴格盡職審查的部分，與政治人物、非面對面業務及高風險國家並列"),
         ("A Policy that does not say how such cases get EDD falls short of the guidelines", "政策如未說明如何對此類情況採取更嚴格措施，即不符合指引"),
         APG("3")),
        (("one day", "一日"),
         ("Retrieve CDD, transaction, screening and customer risk assessment records within a reasonable time", "在合理時間內檢索客戶盡職審查、交易、篩查及客戶風險評估紀錄"),
         ("The record-keeping part of the AML/CFT Policy, which must say whether your system can do it", "打擊洗錢政策中有關備存紀錄的部分，須說明你的系統能否做到"),
         ("A Policy that does not follow the guidelines can lead to refusal", "未按指引提交的政策可導致申請被拒", LG("5.10(f)")),
         APG("3")),
    ])
    + traps(
        trap(("The Policy must come out of your own risk assessment", "政策必須源自你自己的風險評估"),
             ("The guidelines are not a form to copy. They expect you to complete a self-assessment of your ML/TF risks first, and to base the policy on that assessment and your own business profile.",
              "該指引並非照抄的表格。它要求你先就本身的洗錢及恐怖分子資金籌集風險完成自我評估，並以該評估及你的業務狀況作為政策的基礎。"),
             ("AML/CFT Policy guidelines, introduction", "《打擊洗錢政策指引》引言")),
        trap(("Both documents are endorsed by the people who own and run you", "兩份文件均須由擁有及經營你的人簽署確認"),
             ("The checklist wants the Business Plan and the AML/CFT Policy endorsed by the sole proprietor, or by each individual partner, director and ultimate owner. It also wants a copy of the agreement or contract with each local or foreign third party involved in the money service process.",
              "核對清單要求業務計劃及打擊洗錢政策由獨資經營者，或每名個人合夥人、董事及最終擁有人確認；亦要求提交與參與經營金錢服務的每個本地及／或外地第三方簽訂的協議或合約複本。"),
             LG("16.3")),
    ))

# ---------------------------------------------------------------- E. fit and proper
E_ = sec('fitproper', [("F&P Guideline", "《適當人選指引》"), ("April 2018", "2018年4月"), ("Supplement", "補充指引"), ("January 2020", "2020年1月")],
         ("Fit and proper: what the Commissioner weighs beyond the statutory list", "適當人選：法定清單以外，關長還會考慮甚麼"),
    P("The statutory list of matters is on the <a href=\"#p5-fitproper\">Part 5 page</a>. Section 30(4) also lets the Commissioner weigh any other matter he considers relevant, on top of the listed ones. These two guidelines say what that covers: the 2020 Supplement gives examples of such other matters, and the 2018 Guideline lists the factors he takes into account, some of which restate the statutory list. The first table says whom each guideline reaches; the second groups their examples by theme.",
      "法定的考慮事項清單見<a href=\"#p5-fitproper\">第5部一頁</a>。第30(4)條亦容許關長在清單所列事宜以外，考慮任何其他其認為有關的事宜。這兩份指引說明其涵蓋範圍：2020年補充指引列舉這類其他事宜的例子；2018年指引則列出關長會考慮的因素，其中部分重述法定清單。第一個表說明每份指引適用於誰；第二個表按主題把各例子分組。")
    + table([th("", ""), th("Grant", "批給"), th("Renewal", "續期"), th("While licensed", "持牌期間")], [
        tr(rh("Guideline on Criteria for Determining Fitness and Propriety, April 2018", "《有關適當人選準則的指引》（2018年4月）", FPG("4")),
           vd(YES), td("Not mentioned", "沒有提及"),
           td("Written for the grant, and said to cover the person who will hold the licence", "為批給牌照而寫，並表明適用於將持有牌照的人")),
        tr(rh("Supplementary Guideline, January 2020", "《補充指引》（2020年1月）", FPS("5")),
           vd(YES), vd(YES),
           td("Yes. Licensees must go on meeting the criteria, and failing them would be a ground for suspension or revocation under section 34", "適用。持牌人須持續符合準則，未能符合可構成根據第34條暫時吊銷或撤銷牌照的理由", post=flag())),
    ], minw=760)
    + table([th("Theme", "主題"), th("Examples the Commissioner considers relevant", "關長認為相關的例子"), th("Where", "出處")], [
        tr(rh("Compliance record", "遵從紀錄"),
           td("Failing to comply with the Ordinance, a Commissioner's regulation or a licence condition; a record of non-compliance that led to administrative action, prosecution, a written warning or discipline; not following the C&amp;ED's guidelines, such as the Licensing Guide and the AML/CFT Guideline",
              "未有遵從條例、關長訂立的規例或牌照條件；因違規而遭行政處分、檢控、書面警告或紀律處分的紀錄；未有遵從海關指引，例如《牌照指引》及《打擊洗錢指引》"),
           td("2018 ¶5(a), (d); 2020 ¶6(a)–(c)", "2018年第5(a)、(d)段；2020年第6(a)至(c)段", cls='faint')),
        tr(rh("Honesty", "誠信"),
           td("A conviction outside the statutory list that bears badly on honesty, integrity and reliability, such as offences relating to fraud, dishonesty and malpractice; unresolved criminal charges anywhere; criminal or disciplinary proceedings, or notice of a possible investigation, in any jurisdiction; giving false or misleading information, leaving out material information, or not cooperating with C&amp;ED",
              "不在法定清單之內、但對誠實、誠信及可靠性有重大而負面影響的定罪，例如與詐騙、不誠實及舞弊行為有關的罪行；在任何地方尚未了結的刑事控罪；在任何司法管轄區的刑事或紀律程序，或獲通知可能展開的調查；提供虛假或具誤導性的資料、遺漏要項，或不與海關合作"),
           td("2018 ¶5(e); 2020 ¶6(e), (i), (l)–(m)", "2018年第5(e)段；2020年第6(e)、(i)、(l)至(m)段", cls='faint')),
        tr(rh("Standing elsewhere", "在其他地方的紀錄"),
           td("Censure, discipline or public criticism by any regulator or professional body; being refused or restricted from a licensed trade or profession; disqualification as a director by a court",
              "被任何監管機構或專業團體譴責、紀律處分或公開批評；被拒絕或限制從事須領牌的行業或專業；被法院取消董事資格"),
           td("2020 ¶6(n)–(p)", "2020年第6(n)至(p)段", cls='faint')),
        tr(rh("Competence and fairness", "能力及公平"),
           td("The skills, knowledge, experience and professionalism to run the business, including an understanding of its rules, where <b>not taking or failing the C&amp;ED test</b> is the example given; running the business competently, honestly and fairly, where consumer-protection breaches or complaints made reasonably and in good faith count against you",
              "經營業務所需的技能、知識、經驗及專業，包括了解相關規定，指引所舉的例子是<b>沒有應考海關的測驗或未能在測驗取得合格成績</b>；以稱職、誠實及公平的方式經營，違反保障消費者的法例，或被合理及真誠地投訴，均屬不利因素", post=flag()),
           td("2020 ¶6(d), (h)", "2020年第6(d)、(h)段", cls='faint')),
        tr(rh("Systems and structure", "制度及架構"),
           td("Effective AML/CFT systems, such as a competent compliance officer senior enough to oversee them; an organisational structure and staff that meet the requirements; infrastructure and internal controls that manage risk, avoid conflicts of interest and keep an audit trail",
              "有效的打擊洗錢制度，例如具足夠職級及權力監督制度的合資格合規主任；符合規定的組織架構及人員；能管理風險、避免利益衝突及保存審計線索的基礎設施及內部管控"),
           td("2020 ¶6(g), (j)–(k)", "2020年第6(g)、(j)至(k)段", cls='faint')),
        tr(rh("Money and intention", "財務及營業意向"),
           td("Being an undischarged bankrupt or subject to bankruptcy proceedings, or a corporation being wound up or in receivership: both are already statutory matters under s.30(4)(d)–(e), which the 2018 Guideline restates. Beyond the list: financial integrity, with resources adequate to the business, where an unpaid judgment debt or a compromise with creditors counts against you; a genuine intention to trade, where providing no money service for a long time after the grant counts against you; the state of any other business you run, if it exposes you to money laundering or weakens your finances",
              "屬未獲解除破產的破產人或《破產條例》下破產程序的標的，或法團正在清盤或已委任接管人：兩者本已是第30(4)(d)至(e)條的法定事宜，2018年指引只是重述。清單以外：財政穩健，具備與業務相稱的資源，未有清償判定債項或與債權人達成債務重整安排均屬不利因素；確實有意經營，批給後長期未有提供金錢服務屬不利因素；你經營的其他業務，如令你面對洗錢風險或削弱你的財政狀況", post=flag()),
           td("2018 ¶5(b)–(c); 2020 ¶6(f), (q)–(r)", "2018年第5(b)至(c)段；2020年第6(f)、(q)至(r)段", cls='faint')),
    ], minw=820)
    + traps(
        trap(("One failing is not automatically fatal", "一項不符並非必然致命"),
             ("The examples are likely to raise concern, but failing an individual element may not stop the Commissioner being satisfied. Each case turns on its own facts, and both guidelines state that they are advisory.",
              "這些例子可能引起關注，但個別一項不符合，未必令關長不信納。每宗個案按其本身特點判斷，兩份指引均表明屬指引性文件。"),
             cc(FPS("7–8"), FPG("6–7"))),
        trap(("The Assessment sits inside the fitness test", "能力評核屬適當人選判定的一部分"),
             ("Not taking or failing the C&amp;ED test is the Supplement's own example of lacking the knowledge a fit and proper person needs, and the Guidance Notes say the result carries a substantial weighting in the overall fitness evaluation.",
              "沒有應考海關的測驗或未能在測驗取得合格成績，是《補充指引》本身所舉缺乏適當人選應有知識的例子；《能力評核須知》亦指評核成績在整體適當人選評估中佔相當比重。"),
             cc(FPS("6(h)"), GN("3.1"))),
        trap(("A conviction off the statutory list can still count", "法定清單以外的定罪仍可計算在內"),
             ("Of the AMLO's own offences, the list names only those under sections 5(5)–(8), 10(1), (3) and (5)–(8), 13(1), (3) and (5)–(8), 17(9), 20(1), 61(2) and 66(3). Not every AMLO offence is on the list: operating without a licence under section 29, for one, is not. It also lists offences under section 14 of the United Nations (Anti-Terrorism Measures) Ordinance; and, under the drug trafficking and organised crime ordinances, the offences in sections 25(1), 25A(5) and 25A(7) and those specified in their schedules. It also lists convictions outside Hong Kong for equivalent offences, for money laundering or terrorist financing, or for any offence that needed a finding of fraudulent, corrupt or dishonest conduct. Any other conviction that bears significantly and negatively on honesty, integrity and reliability can still weigh against you, such as an offence relating to fraud, dishonesty or malpractice.",
              "就本條例本身的罪行，清單只列明第5(5)至(8)、10(1)、(3)及(5)至(8)、13(1)、(3)及(5)至(8)、17(9)、20(1)、61(2)及66(3)條所訂罪行，並非所有本條例罪行都在清單之內，例如第29條的無牌經營罪行便不在其中；亦列明《聯合國（反恐怖主義措施）條例》第14條所訂罪行；以及《販毒（追討得益）條例》和《有組織及嚴重罪行條例》第25(1)、25A(5)或(7)條所訂罪行及其附表指明的罪行；亦列明在香港以外地方就相應罪行、關乎洗錢或恐怖分子資金籌集的罪行，或須裁斷該人曾有欺詐性、舞弊或不誠實作為的罪行而被定罪。任何其他對誠實、誠信及可靠性有重大而負面影響的定罪，仍可成為不利因素，例如與詐騙、不誠實及舞弊行為有關的罪行。"),
             cc("s.30(4)(a)–(b)", FPG("5(e)"), FPS("6(l)"))),
        trap(("\"Persistently\" in the Ordinance, not in the 2018 Guideline", "條例寫「屢次」，2018年指引沒有"), None, cc("s.30(4)(c)", FPG("5(a)")),
             vs=[(("The statutory list", "法定清單"), ("Whether the person has <b>persistently</b> failed to comply with a requirement under the Ordinance or a regulation made by the Commissioner.", "該人是否<b>屢次</b>不遵從根據本條例施加的要求或關長訂立的任何規例。")),
                 (("The 2018 Guideline", "2018年指引"), ("Whether the person has failed to comply with any requirement under the Ordinance or any regulation made by the Commissioner: there is no \"persistently\", so on its wording a single failure can be weighed.", "該人是否曾不遵從打擊洗錢條例施加的要求或關長訂立的任何規例：沒有「屢次」一詞，按其字面，單一次不遵從亦可予以考慮。"))]),
    ))

# ---------------------------------------------------------------- F. the Assessment
F_ = sec('ca', [("CA Guidance Notes", "《能力評核須知》"), ("December 2022", "2022年12月"), ("sample questions", "參考試題")],
         ("The Competence Assessment you are sitting", "你將應考的能力評核"),
    P("Start with the figure: the pass rule has two conditions and a candidate must meet both. The tables that follow cover who may sit, when, and what happens after the result.",
      "先看圖：合格準則有兩個條件，應考者必須同時符合。其後的表格說明誰可應考、何時應考，以及成績公布後的安排。")
    + fig(fig_pass, ("Each square is one question. The rule rewards an even spread: two wrong in each of five modules still passes, but three wrong in any one module fails however well the rest went.",
                       "每個方格代表一題。此準則着重平均：五個單元各錯兩題仍可合格，但任何一個單元錯三題，其他單元再好也不合格。"), PASS_KEY)
    + numreq([
        (("35 questions", "35題"),
         ("Seven modules of five multiple-choice questions, each with one correct answer, in Chinese or English", "七個單元，每單元五條選擇題，每題只有一個正確答案，備中文或英文版本"),
         ("Every sitting", "每次評核"),
         ("Marking two or more answers to one question scores nothing for it", "同一題填寫多於一個答案，該題不獲分"),
         GN("5.1–5.2, 11.5")),
        (("1 hour 15 minutes", "1小時15分鐘"),
         ("The whole paper", "整份試卷"),
         ("From the start; nobody is let in once it has begun", "由開考起計；開考後不准進場"),
         ("Answers not on the answer sheet are not marked, and no changes are accepted after time", "沒有填寫在答題紙上的答案不獲評分，時間完結後不接受更改答案"),
         GN("5.1, 10.2, 10.9, 11.6")),
        (("2 wrong", "錯2題"),
         ("The most you may get wrong in any one module", "每個單元最多可答錯的題數"),
         ("Each of the seven modules, separately", "七個單元各自計算"),
         ("A third wrong answer in any module fails the paper", "任何單元答錯第三題即不合格"),
         GN("5.3")),
        (("25 of 35", "35分中25分"),
         ("The minimum total", "最低總分"),
         ("On top of the module rule", "在單元規則之外另須符合"),
         ("Below 25 fails even with no module at three wrong", "即使沒有單元錯三題，總分低於25分仍不合格"),
         GN("5.3")),
    ])
    + h3("The seven modules, and the nearest pages in this pack", "七個單元，以及本資料包最相關的頁面")
    + table([th("Module", "單元"), th("As the Guidance Notes name it", "《須知》所列名稱"), th("Nearest pages here", "本資料包最相關的頁面")], [
        tr(rh("1", "1"), td("General knowledge on AML/CFT and counter proliferation financing", "有關打擊洗錢及恐怖分子資金籌集與打擊擴散資金籌集的常識"),
           td("Guideline <a href=\"#g1-threats\">Ch. 1</a> for the threats, the FATF, the six ordinances and the offences; <a href=\"#g6-tf\">Ch. 6</a> for terrorist financing, sanctions and proliferation financing; <a href=\"#g7-duty\">Ch. 7</a> for the duty to report; <a href=\"#s1-mltf\">Schedule 1</a> for the definitions",
              "指引<a href=\"#g1-threats\">第1章</a>：威脅、財務行動特別組織、六條條例及罪行；<a href=\"#g6-tf\">第6章</a>：恐怖分子資金籌集、金融制裁及擴散資金籌集；<a href=\"#g7-duty\">第7章</a>：舉報責任；<a href=\"#s1-mltf\">附表1</a>：定義")),
        tr(rh("2", "2"), td("Parts 1 to 7 of the AMLO", "《打擊洗錢條例》第1至7部"), td("The Part pages, 1 to 7", "第1至7部各頁")),
        tr(rh("3", "3"), td("Schedules to the AMLO", "《打擊洗錢條例》的附表"), td("The Schedule pages, 1 to 4", "附表1至4各頁")),
        tr(rh("4", "4"), td("Guidelines promulgated by the C&amp;ED", "海關頒布的指引"),
           td("This page; how a \"should\" in the Guideline binds you, on the <a href=\"#g1-status\">Guideline Ch. 1 page</a>; what the guidelines are in law, on the <a href=\"#p2-guidelines\">Part 2 page</a>",
              "本頁；指引中「應」字的約束力，見<a href=\"#g1-status\">指引第1章一頁</a>；各指引的法律地位，見<a href=\"#p2-guidelines\">第2部一頁</a>")),
        tr(rh("5", "5"), td("MSO's systems and controls (i): institutional governance and strategy", "金錢服務經營者的系統及管控措施(i)：機構層面的管治及策略"),
           td("Guideline <a href=\"#g2-rba\">Ch. 2</a> for the risk-based approach, the institutional risk assessment and customer risk; <a href=\"#g3-build\">Ch. 3</a> for the AML/CFT Systems, the compliance officer and MLRO, and groups; <a href=\"#s2-systems\">Schedule 2</a>; the <a href=\"#ci-warnings\">Circulars page</a>",
              "指引<a href=\"#g2-rba\">第2章</a>：風險為本的方法、機構層面的風險評估及客戶風險；<a href=\"#g3-build\">第3章</a>：打擊洗錢制度、合規主任及洗錢報告主任，以及集團；<a href=\"#s2-systems\">附表2</a>；<a href=\"#ci-warnings\">通函一頁</a>")),
        tr(rh("6", "6"), td("MSO's systems and controls (ii): AML/CFT control areas", "金錢服務經營者的系統及管控措施(ii)：打擊洗錢及恐怖分子資金籌集的管控範疇"),
           td("<a href=\"#s2-map\">Schedule 2</a> for customer due diligence; Guideline <a href=\"#g2-cra\">Ch. 2</a> for customer risk assessment; <a href=\"#g5-extent\">Ch. 5</a> for ongoing monitoring; <a href=\"#g6-screening\">Ch. 6</a> for sanctions screening; <a href=\"#g7-duty\">Ch. 7</a> for suspicious transaction reports; <a href=\"#g8-who\">Ch. 9</a> for training; the <a href=\"#ci-cdd\">Circulars page</a>",
              "<a href=\"#s2-map\">附表2</a>：客戶盡職審查；指引<a href=\"#g2-cra\">第2章</a>：客戶風險評估；<a href=\"#g5-extent\">第5章</a>：持續監察；<a href=\"#g6-screening\">第6章</a>：制裁篩查；<a href=\"#g7-duty\">第7章</a>：可疑交易報告；<a href=\"#g8-who\">第9章</a>：培訓；<a href=\"#ci-cdd\">通函一頁</a>")),
        tr(rh("7", "7"), td("MSO's systems and controls (iii): demonstrating and monitoring compliance", "金錢服務經營者的系統及管控措施(iii)：證明符合規定及監察合規水平"),
           td("Guideline <a href=\"#g3-audit\">Ch. 3</a> for the independent audit; <a href=\"#g7-after\">Ch. 7</a> for the registers kept after a report; <a href=\"#g8-file\">Ch. 8</a> for what goes in the records and <a href=\"#g8-elsewhere\">records held elsewhere</a>; <a href=\"#g8-cycle\">Ch. 9</a> for training records; <a href=\"#s2-records\">Schedule 2</a> for the retention periods; the <a href=\"#ci-returns\">Circulars page</a> for periodic returns",
              "指引<a href=\"#g3-audit\">第3章</a>：獨立審核；<a href=\"#g7-after\">第7章</a>：提交報告後備存的登記冊；<a href=\"#g8-file\">第8章</a>：紀錄須載有的內容，以及<a href=\"#g8-elsewhere\">存放於別處的紀錄</a>；<a href=\"#g8-cycle\">第9章</a>：培訓紀錄；<a href=\"#s2-records\">附表2</a>：備存期限；<a href=\"#ci-returns\">通函一頁</a>：定期申報表")),
    ], note=B("Questions are set mainly from five public sources: the Ordinance, the AML/CFT Guideline, the Licensing Guide, the other C&amp;ED guidelines, and the circulars. The official samples give four numbered statements and five fixed options, the last being all of the above.",
              "試題主要取材自五類公開資料：條例、《打擊洗錢指引》、《牌照指引》、海關其他指引，以及通函。官方參考試題列出四項編號陳述，配以五個固定選項，最後一項為以上皆是。")
       + ' ' + cite_html(cc(GN("5.2, 6.1"), ("Sample questions, 12 May 2021", "2021年5月12日參考試題"))), minw=760)
    + h3("Who may sit: senior management, and why", "誰可應考：高級管理層，以及原因")
    + table([th("A candidate must be all of these", "應考者必須同時符合以下各項")], [
        tr(td("Senior management of the applicant or licensee, overseeing the operation of the money service business", "牌照申請人或持牌人的高級管理層，負責監督金錢服務業務的運作", GN("4.1(i)"))),
        tr(td("Directly involved in making decisions on company policy and governance arrangements", "直接參與有關公司政策及管治安排的決策", GN("4.1(ii)"))),
        tr(td("Held accountable for the company's compliance functions and systems", "須對公司的合規職能及制度負責", GN("4.1(iii)"))),
        tr(td("The sole proprietor, a partner, the sole director, or a director who is a natural person; a partnership or corporation nominates no more than three", "獨資經營者、合夥人、唯一董事，或屬自然人的董事；合夥或法團最多提名三人", GN("4.2"))),
    ], note=B("Why senior management: so that it clearly understands the ML/TF risks the business is exposed to and can implement effective AML/CFT systems that manage and mitigate them, meeting the statutory and regulatory requirement for senior management oversight.",
              "為何是高級管理層：確保高級管理層清楚了解業務面對的洗錢及恐怖分子資金籌集風險，並有能力推行有效的打擊洗錢及恐怖分子資金籌集制度，以管理及減低這些風險，符合有關高級管理層監督的法定及監管規定。")
       + ' ' + cite_html(LG("4.15(b), 11.4")), minw=620)
    + h3("Who is nominated, when, and what if nobody passes", "何時提名、誰應考，以及無人合格的後果")
    + table([th("Situation", "情況"), th("Nominate?", "須否提名"), th("Sit by", "應考限期"), th("If nobody passes", "如無人合格")], [
        tr(rh("A new application", "新申請", GN("4.4(i), 4.5")),
           td("Yes, once, when invited after your documents are complete", "須提名一次，於文件齊備後獲邀時提名", LG("5.4")),
           td("Within 30 days of the interview", "會面後30日內"),
           td("One retake after 30 days from the result; then the application may be refused", "於成績通知發出30日後重考一次；其後申請可被拒絕")),
        tr(rh("Renewal, whether or not someone already holds a pass", "續牌，不論是否已有人持有合格成績", LG("6.2")),
           td("Yes. The invitation comes with the 90-day reminder to every licensee: nominate within 7 days of receiving it, or the renewal application is invalid",
              "須提名。邀請信隨90日提示通知發給每名持牌人：須在接獲邀請信當日起計7日內提名，否則續牌申請即屬無效", LG("6.4(c)"), post=flag()),
           td("Within 30 days of receiving the invitation letter", "接獲邀請信當日起計30日內"),
           td("One retake after 30 days from the result and before expiry; then renewal may be refused", "於成績通知發出30日後、期滿前重考一次；其後續期可被拒絕", GN("4.6"))),
        tr(rh("The only person with a pass leaves a partnership or corporation", "合夥或法團中唯一持有合格成績的人離任", GN("4.4(iii), 8.2")),
           td("Yes, once you have notified the change", "須在具報有關改變後提名"),
           td("Within 30 days of notifying the change in partnership or directorship. If renewal is due within 180 days, the renewal timetable applies instead", "具報合夥人或董事變更後30日內。如須於180日內續牌，則改按續牌安排"),
           td("One retake after 30 days from the result", "於成績通知發出30日後重考一次")),
        tr(rh("A sole proprietorship", "獨資經營", GN("8.2")),
           td("The 30-day chance above is offered only to partnerships and corporations", "上述30日的機會只適用於合夥及法團", post=flag()),
           dash_td(), dash_td()),
        tr(rh("Nobody holds a pass at all", "完全無人持有合格成績", GN("8.3")),
           dash_td(), dash_td(),
           td("The Commissioner may still let you trade, on licence conditions that make sure your AML/CFT systems work", "關長仍可酌情容許你繼續經營，並施加牌照條件以確保打擊洗錢制度有效")),
    ], minw=900)
    + numreq([
        (("14 days", "14日"),
         ("C&amp;ED emails the result, pass or fail only", "海關以電郵通知成績，只分合格或不合格"),
         ("After the Assessment", "評核後"),
         ("Keep the email: it is your certificate of the result", "保留該電郵：它是你的成績證明"),
         GN("12.1")),
        (("7 days", "7日"),
         ("Ask in writing for your paper to be re-checked", "以書面要求覆檢試卷"),
         ("From the date the result notice was issued, by letter to the Licensing Control Division or by email", "自成績通知發出當日起計，致函牌照管制課或發電郵"),
         ("Late requests are not considered", "逾期提出的要求不獲受理"),
         GN("12.2")),
        (("14 days", "14日"),
         ("C&amp;ED replies in writing", "海關以書面回覆"),
         ("From receiving the request. It checks only technical errors, such as wrong mark entries and inconsistent data", "自接獲要求起計。只檢查技術錯誤，例如分數輸入錯誤及數據前後不一"),
         ("The re-check result is final; scores, questions and answers are never disclosed", "覆檢結果為最終結果；實際分數、試題及答案概不披露"),
         GN("12.3–12.4")),
        (("8:00 a.m.", "上午8時"),
         ("If typhoon signal No. 8 or above, or the black rainstorm warning, is still in force at or after this time on the day, the Assessment will be suspended",
          "如八號或以上熱帶氣旋警告信號，或黑色暴雨警告信號，於當日上午8時或之後仍然生效，能力評核會改期"),
         ("Signal No. 3 or below, or an amber or red rainstorm warning: it goes ahead", "三號或以下信號，或黃色、紅色暴雨警告：如期舉行"),
         ("Alternative arrangements, if any, will be published on the licensing system's website on the first working day that follows", "如需另作安排，會於隨後首個工作日在牌照系統網頁公布"),
         GN("13.1")),
    ], heading=False)
    + table([th("Bring on the day", "當日須帶備"), th("Why it matters", "原因")], [
        tr(td("Your Hong Kong identity card, or another identity document with a photograph, such as a valid travel document", "香港身份證，或其他附有照片的身份證明文件，例如有效的旅遊證件", GN("9.1–9.3")),
           td("Without it you will not be allowed to sit, and a damaged or defaced one may be refused", "沒有證件不准應考；證件受損或曾遭塗改亦可能不獲准應考")),
        tr(td("A printed copy of the invitation letter", "邀請信的列印本", GN("9.1, 10.4")),
           td("Without it you will not be allowed to sit as scheduled. It is checked with your identity document, possibly more than once during the Assessment", "未能出示者不獲准於預約時間應考。邀請信會與身份證明文件一併核對，評核期間或會多次核對", GN("9.2, 10.4"))),
        tr(td("An authorization letter, for a partnership or corporation only", "授權書，只適用於合夥及法團", GN("9.1")),
           td("Required for a partnership or corporation; without it you will not be allowed to sit as scheduled", "合夥及法團須出示；未能出示者不獲准於預約時間應考", GN("9.1–9.2"))),
    ], note=B("Stationery is provided. Phones and other devices go under the chair, switched off, with phones uncovered and in view of the invigilators. Nothing from the question book may be copied onto the invitation letter, your belongings or your body, and no question book or answer sheet, used or unused, may leave the assessment centre.",
              "試場會提供文具。手機及其他電子裝置須關掉並放在椅下，手機不得遮蓋，須讓監考員清楚看見。不得將問卷的任何內容抄寫在邀請信、個人物品或身上；任何問卷或答題紙，不論是否曾經使用，均不得攜離試場。")
       + ' ' + cite_html(GN("10.5–10.9")), minw=680)
    + traps(
        trap(("Within 30 days to sit; after 30 days to retake", "30日內應考；30日後重考"), None, cc(GN("4.5–4.6, 8.2"), LG("6.2")),
             vs=[(("Within 30 days", "30日內"), ("The first sitting: of the interview for a new licence; of receiving the invitation letter for a renewal; of notifying the change when your only passed manager leaves.", "首次應考：新牌照自會面起計；續牌自接獲邀請信當日起計；唯一合格的管理人員離任時，自具報改變起計。")),
                 (("After 30 days", "30日後"), ("The retake: counted from the result notice, and for a renewal it must also come before expiry.", "重考：自成績通知發出起計；續牌個案亦須於期滿前進行。"))]),
        trap(("Two 7-day clocks, and two 14-day clocks", "兩個7日，兩個14日"), None, cc(LG("6.2"), GN("12.1–12.3")),
             vs=[(("7 days", "7日"), ("To nominate, from receiving a renewal invitation. To ask for a re-check, from the date the result notice was issued.", "提名：自接獲續牌邀請信起計。要求覆檢：自成績通知發出當日起計。")),
                 (("14 days", "14日"), ("For the result, after the Assessment. For the re-check reply, after C&amp;ED receives your request.", "成績：評核後14日內。覆檢回覆：海關接獲要求後14日內。"))]),
        trap(("A pass belongs to the company, and it is not a licence", "合格屬於公司，亦不等於牌照"),
             ("The pass is a company-based qualification. It lapses automatically when no sole proprietor, partner or director who passed remains. Passing does not make you eligible for a licence either: every other licensing requirement still has to be met.",
              "合格成績是以公司為單位的資格。當再沒有已合格的獨資經營者、合夥人或董事時，資格自動失效。合格亦不代表可獲發牌：其他所有發牌規定仍須符合。"),
             GN("8.1–8.2, 12.5, 14.1")),
        trap(("Up to three may sit; one must pass", "最多三人應考；最少一人合格"),
             ("A partnership or corporation may nominate no more than three partners or directors, all sitting the same session. The company needs only one of them to pass.",
              "合夥或法團最多可提名三名合夥人或董事，並須應考同一時段。公司只需其中一人合格。"),
             GN("3.1, 4.2–4.3")),
    ))

# ---------------------------------------------------------------- G. renewal
G_ = sec('renewal', [("Licensing Guide", "《牌照指引》"), ("¶6.1–6.4", "第6.1至6.4段"), ("CA Notes ¶4.6", "《能力評核須知》第4.6段")],
         ("Renewal: the 90-day countdown", "續牌：90日倒數"),
    P("Read the line from left to right, in days before expiry. The key tells your deadlines from C&amp;ED's own steps; the two boxes at the foot are the two ways the countdown can end.",
      "由左至右閱讀時間線，以期滿前日數計算。圖例分辨你的限期與海關的步驟；底部兩個方格是倒數的兩種結局。")
    + fig(fig_renew, ("The reminder at 90 days is a courtesy. The Licensing Guide is explicit that applying 45 days before expiry is your legal responsibility whether or not a reminder arrives.",
                        "90日的提示只屬提醒。《牌照指引》明言，不論有否收到提示，在期滿前45日申請續期是你的法律責任。"), RENEW_KEY)
    + numreq_c([
        (("7 days", "7日"),
         ("Nominate who will sit the Assessment", "提名應考能力評核的人選"),
         ("From receiving the invitation. It goes to every licensee, with no exception for one whose senior management already holds a pass",
          "自接獲邀請信當日起計。邀請信發給每名持牌人，高級管理層已有人持有合格成績的持牌人亦不例外", None, flag()),
         ("The renewal application is invalid", "續牌申請無效"),
         LG("6.2, 6.4(c)")),
        (("30 days", "30日"),
         ("Your nominees sit the Assessment", "獲提名人士應考能力評核"),
         ("From receiving the invitation letter", "自接獲邀請信當日起計"),
         ("Not attending the designated session will result in rejection of the application; for a new licence it may result in refusal (<a href=\"#route\">getting licensed</a>)",
          "未有出席指定時段的評核，會導致相關申請被拒絕；新申請亦然（見<a href=\"#route\">申領牌照</a>）",
          LG("5.4, 6.2"), FLAG_EN),
         LG("6.2")),
        (("45 days", "45日"),
         ("Lodge the renewal application, accompanied by the Schedule 3 fee: the duly completed Form 2, supplementary information sheet and relevant annex. The other papers go with them; anything missing is chased under the next row",
          "提出續牌申請，並附隨附表3指明的費用：已填妥的表格2、補充資料表格及相關附件。其他文件一併遞交；欠交的按下一行催交"),
         ("Before expiry: the statutory deadline", "期滿前：法定限期"),
         ("The application is invalid, the licence lapses automatically at expiry, and you must stop", "申請無效，牌照於期滿時自動失效，你必須停業"),
         cc("s.31(2)", LG("6.1, 6.3, 6.4(a)"))),
        (("specified period", "指明期限"),
         ("Produce every outstanding document C&amp;ED has chased", "交出海關催交的所有尚欠文件"),
         ("After the reminder for outstanding documents", "收到催交尚欠文件的信件後"),
         ("The application is invalid", "申請無效"),
         LG("6.3, 6.4(b)")),
    ])
    + traps(
        trap(("Invalid is worse than refused", "無效比被拒更糟"), None, cc(LG("6.4"), "s.31(9)–(10)"),
             vs=[(("An invalid renewal", "無效的續牌申請"), ("Not processed. The licence lapses automatically when it expires, and trading on is unlicensed operation.", "不獲處理。牌照期滿時自動失效，繼續經營即屬無牌經營。")),
                 (("A renewal refused after a valid, timely application", "按時提出有效申請但被拒"), ("The licence stays in force past expiry until the refusal takes effect, and the refusal can go to the Review Tribunal.", "牌照在期滿後仍然有效，直至拒絕的決定生效；你亦可就拒絕向覆核審裁處申請覆核。"))]),
        trap(("Letting a licence expire counts as ceasing", "讓牌照期滿亦屬停業"),
             ("The Licensing Guide treats expiry as a cessation: notify on Form 7 before the licence expires, and return the expired licence within 7 days.",
              "《牌照指引》把牌照期滿視作停業：須在牌照期滿前以表格7具報，並於期滿後7日內交回已期滿的牌照。"),
             LG("10.2")),
    ))

# ---------------------------------------------------------------- H. changes and forms
H_ = sec('changes', [("Licensing Guide", "《牌照指引》"), ("¶8.1–10.4", "第8.1至10.4段")],
         ("Changing something once you are licensed: which form, and when", "持牌後作出改變：用哪份表格，何時遞交"),
    P("Find the change you are making in the left column. The form and its timing are in the next two columns; the last says what has to go with it.",
      "在左欄找出你要作的改變。其後兩欄是表格及時限；最後一欄是須一併提交的文件。")
    + table([th("You want to", "你要"), th("Form", "表格"), th("When", "時限"), th("What goes with it", "須一併提交")], [
        tr(td("Bring in a new director, partner or ultimate owner", "委任新董事、合夥人或最終擁有人", LG("8.1–8.3")),
           td("Form 4", "表格4"),
           td("<b>Before</b> the person takes the role: written approval comes first", "該人就任<b>之前</b>：須先取得書面批准", post=flag()),
           td("The person's fit-and-proper declaration, and the fee for each person", "該人的適當人選聲明表格，以及每人的費用")),
        tr(td("Trade at more premises", "增加經營處所", LG("8.4")),
           td("Form 5", "表格5"), td("Before you trade there", "在該處經營之前"), td("The fee for each new premises", "每個新處所的費用")),
        tr(td("Move from no particular premises to particular premises", "由沒有特定處所改為在特定處所經營", LG("8.4")),
           td("Form 5", "表格5"), td("Before you trade there", "在該處經營之前"), td("A Business Plan and an updated AML/CFT Policy as well", "另須提交業務計劃及經更新的打擊洗錢政策")),
        tr(td("Move from particular premises to none", "由特定處所改為沒有特定處所", LG("10.1")),
           td("Form 7, then a new application", "表格7，然後提出新申請"), td("Notify cessation of the existing business first", "先具報停止現有業務"),
           td("A fresh application to operate without particular premises", "以沒有特定處所的方式經營的新申請")),
        tr(td("Change the service, such as money changing to remittance", "改變服務性質，例如由貨幣兌換改為匯款", LG("9.4")),
           td("A written submission", "書面陳詞"), td("Not fixed; the Commissioner reviews your fitness for the new service", "沒有訂明；關長會檢視你就新服務的適當人選資格"),
           td("An updated Business Plan and AML/CFT Policy, with supporting documents", "經更新的業務計劃及打擊洗錢政策，連同證明文件")),
        tr(td("Change the legal entity that holds the licence", "改變持牌的法律實體", LG("9.4")),
           td("A fresh licence application", "新的牌照申請"), dash_td(), td("Everything a new applicant files", "新申請人須提交的全部文件")),
        tr(td("Change any of the particulars in the next table", "改變下表所列的任何詳情", LG("9.1–9.2")),
           td("Form 6", "表格6"), td("Within one month beginning on the day the change takes place", "自改變發生之日起計的一個月內"),
           td("Some changes, such as a change in fitness status, can prompt a review of the licence itself", "某些改變（例如適當人選身分的改變）可引致牌照本身被檢視")),
        tr(td("Stop trading, entirely or at some premises, including letting the licence expire", "全面停業或停止在部分處所經營，包括讓牌照期滿", LG("10.2–10.3")),
           td("Form 7", "表格7"), td("Before the date of cessation", "在停業日期之前"),
           td("Return the licence, valid or expired, within 7 days beginning on the date of cessation or expiry. No fee is refunded", "於停業或期滿日期起計的7日內交回有效或已期滿的牌照。費用概不退還")),
    ], minw=900)
    + table([th("Group", "類別"), th("The fourteen changes that go on Form 6", "須以表格6具報的十四項改變")], [
        tr(rh("Identity", "身分"), td("Business or corporation name; principal or correspondence address; contact details", "業務或法團名稱；主要（通訊）地址；聯絡資料")),
        tr(rh("Premises", "處所"), td("Business premises information, and their telephone or fax number; any other business run there; the occupants of particular premises in a mixed commercial and residential building; the local management office; the local place for storage of books and records",
                                     "業務處所資料及其電話或傳真號碼；在處所內經營的其他業務；位於混合式商住樓宇的特定處所的佔用人；本地管理辦事處；本地儲存帳目及紀錄地點")),
        tr(rh("People", "人員"), td("Particulars of the sole proprietor, partners, directors and ultimate owners; a change among partners, directors or ultimate owners; a change in any of their fit-and-proper status; the compliance officer or MLRO",
                                   "獨資經營者、合夥人、董事及最終擁有人的詳情；合夥人、董事或最終擁有人的改變；他們適當人選身分的改變；合規主任或洗錢報告主任的改變")),
        tr(rh("Money", "資金"), td("The bank account used for the money service business", "用以經營金錢服務業務的銀行帳戶")),
    ], note=cite_html(LG("9.1")), minw=640)
    + traps(
        trap(("Joining needs approval first; other changes are notified after", "加入須先獲批准；其他改變則事後具報"),
             ("A new director, partner or ultimate owner needs Form 4 approval before taking the role. Other changes among them, such as one leaving, go on Form 6 within a month of the change.",
              "新董事、合夥人或最終擁有人須在就任前取得表格4的批准。他們之間的其他改變（例如有人離任），則須在改變後一個月內以表格6具報。"),
             cc(LG("8.1–8.3"), LG("9.1(i)"))),
        trap(("Premises and no premises are not mirror images", "有處所與沒有處所之間的轉變並不對稱"), None, cc(LG("8.4"), LG("10.1")),
             vs=[(("Towards particular premises", "改為特定處所"), ("Form 5, plus a Business Plan and an updated AML/CFT Policy.", "表格5，另加業務計劃及經更新的打擊洗錢政策。")),
                 (("Away from particular premises", "放棄特定處所"), ("Notify cessation of the existing business, then apply for a new licence.", "具報停止現有業務，然後申請新牌照。"))]),
    ))

# ---------------------------------------------------------------- I. refusal and revocation
I_ = sec('endings', [("Licensing Guide", "《牌照指引》"), ("¶5.10 · ¶7.1", "第5.10、7.1段")],
         ("What gets an application refused or a licence revoked", "甚麼會令申請被拒或牌照被撤銷"),
    P("Each row pairs a reason the Commissioner may refuse an application with its counterpart once you hold the licence. Both lists are examples, not complete; a dash means the guide gives no example at that stage.",
      "每一行把關長可拒絕申請的理由，與持牌後的相應情況並列。兩份清單均屬例子，並非詳盡無遺；橫線表示指引沒有就該階段舉例。")
    + table([th("Theme", "主題"), th("Refusing an application", "拒絕申請"), th("Suspending or revoking a licence", "暫時吊銷或撤銷牌照")], [
        tr(rh("Fitness", "適當人選"),
           td("You, or anyone in your business who must pass it, fail the fit-and-proper test", "你或你業務中須通過判定的人未能通過適當人選判定", LG("5.10(a)")),
           td("You, a partner, a director or an ultimate owner is no longer fit and proper", "你、任何合夥人、董事或最終擁有人不再是適當人選", LG("7.1(a)"))),
        tr(rh("Premises", "處所"),
           td("The premises are unsuitable, or domestic premises lack every occupant's written consent", "處所不適合，或住宅處所未取得每名佔用人的書面同意", LG("5.10(b)–(c)")),
           td("An occupant withdraws consent, or a new occupant refuses to give it", "佔用人撤回同意，或新佔用人拒絕給予同意", LG("7.1(b)–(c)"))),
        tr(rh("Local place for storage of books and records", "本地儲存帳目及紀錄地點"),
           td("No information on the local place for storage of books and records", "未有就本地儲存帳目及紀錄地點提交資料", LG("5.10(d)")),
           td("Not kept, or no longer meeting the guide", "未能維持，或不再符合指引的要求", LG("7.1(d)"))),
        tr(rh("Management office", "本地管理辦事處"),
           td("Trading without premises, and no information on the management office", "在沒有特定處所的情況下經營，但未有提供本地管理辦事處的資料", LG("5.10(e)")),
           td("Not kept, or no longer meeting the guide", "未能維持，或不再符合指引的要求", LG("7.1(e)"))),
        tr(rh("Papers", "文件"),
           td("No Business Plan and AML/CFT Policy that follow the guidelines; an incomplete or invalid application", "未按指引提交業務計劃及打擊洗錢政策；申請不完整或無效", LG("5.10(f), (h)")),
           dash_td()),
        tr(rh("Key staff", "主要人員"),
           td("No competent compliance officer or MLRO appointed", "未有委任合資格的合規主任或洗錢報告主任", LG("5.10(g)")),
           td("Failing to appoint or keep a competent compliance officer or MLRO", "未能委任或維持合資格的合規主任或洗錢報告主任", LG("7.1(i)"))),
        tr(rh("The Assessment", "能力評核"),
           td("None of the senior management attends, or none passes", "高級管理層中沒有人應考，或沒有人合格", LG("5.10(i)–(j)")),
           dash_td()),
        tr(rh("Using the licence", "使用牌照"),
           dash_td(),
           td("A periodic return filed late; a licence never used for a money service", "逾期遞交定期申報表；從未用於提供金錢服務的牌照", LG("7.1(f)–(g)"), post=flag())),
        tr(rh("The law", "法律"),
           td("You are exempt from licensing under section 25 anyway", "你根據第25條本已獲豁免領牌", LG("5.10(k)")),
           td("Any failure to comply with the Ordinance, Part 5 included", "未有遵從條例的任何規定，包括第5部", LG("7.1(h)"))),
    ], note=B("How this list sits beside the Ordinance: section 34(1) itself names only two situations in which the Commissioner may revoke or suspend. One is that he is of the opinion that the licensee, a partner, a director or an ultimate owner is no longer a fit and proper person. The other is that a licensee operating at domestic premises loses consent to entry, because an occupant revokes it or a new occupant refuses to give it. The Licensing Guide's right-hand column is a non-exhaustive list of examples, and it ends by referring to the fit-and-proper guidelines; the Supplementary Guideline says that failing the fit and proper criteria may reflect adversely on fitness and would be a ground for suspension or revocation by virtue of section 34. The statutory rule is on the <a href=\"#p5-losing\">Part 5 page</a>.",
              "這份清單與條例的關係：第34(1)條本身只列出兩種關長可撤銷或暫時吊銷牌照的情況。一是關長認為持牌人、任何合夥人、董事或最終擁有人不再是適當人選；二是在住宅處所經營金錢服務的持牌人失去准許進入的同意，即佔用人撤銷其書面同意，或新佔用人拒絕給予同意。《牌照指引》右欄所列屬例子，並非詳盡無遺，並在結尾提述適當人選的指引；《補充指引》則指持牌人如未能符合適當人選準則，或會對其適當人選資格造成負面影響，並可構成根據第34條暫時吊銷或撤銷牌照的理由。法定規則見<a href=\"#p5-losing\">第5部一頁</a>。")
       + ' ' + cite_html(cc("s.34(1)", LG("7.1"), FPS("5"))), minw=820)
    + traps(
        trap(("A licence you never use can be taken away", "從不使用的牌照可被撤銷"),
             ("Holding a licence without providing any money service defeats the purpose it was issued for, and the Licensing Guide lists that as a ground for suspension or revocation. The fit-and-proper supplement makes the same point from the other side: nil service for a long time after the grant questions your intention to trade.",
              "持有牌照但從不提供金錢服務，違背了發牌的目的，《牌照指引》把此列為暫時吊銷或撤銷牌照的理由。適當人選補充指引亦從另一角度指出：批給後長期沒有提供服務，會令人質疑你是否確實有意經營。"),
             cc(LG("7.1(g)"), FPS("6(f)"))),
    ))

# ---------------------------------------------------------------- J. penalties
PEN_TBL = table([th("", ""), th("Disciplinary Fining Guideline, May 2018", "《紀律處分罰款指引》（2018年5月）"),
                 th("Disciplinary Action Guideline on Imposition of Pecuniary Penalty, April 2018", "《施加罰款紀律行動指引》（2018年4月）")], [
    tr(rh("The power it guides", "所規管的權力"),
       td("A penalty under section 21 for breaching a Schedule 2 specified provision; published under section 23", "根據第21條就違反附表2指明的條文施加的罰款；根據第23條發布", DFG("1–2")),
       td("A penalty under section 43 for breaching a Part 5 regulation, a licence condition, or sections 35(1) to 41(1); published under section 45", "根據第43條就違反第5部規例、牌照條件或第35(1)至41(1)條施加的罰款；根據第45條發布", DAG("1–3"))),
    tr(rh("Three times the profit", "利潤的三倍"),
       td("The Commissioner will <b>not automatically link</b> the fine to the profit gained or cost avoided, even though three times that amount is one of the two statutory maximums",
          "雖然所獲取的利潤或所避免的開支的3倍是兩個法定上限之一，關長<b>不會自動</b>把罰款與該金額掛鈎", DFG("6"), post=flag()),
       td("Not mentioned: the Part 5 maximum is a flat $1,000,000", "沒有提及：第5部的上限劃一為$1,000,000")),
    tr(rh("The harm it looks at", "考慮的損害"),
       td("Damage to Hong Kong's reputation as an international financial centre", "損害香港作為國際金融中心的聲譽", DFG("9(a)(iii)")),
       td("Damage to the integrity of the operation of money services in Hong Kong, or to that reputation", "損害在香港經營金錢服務業務的廉潔穩健，或上述聲譽", DAG("9(a)(iii)"), post=flag())),
    tr(rh("With other sanctions", "與其他制裁"),
       td("A penalty may be imposed on its own or together with other disciplinary sanctions", "可以純粹實施罰款，或同時實施其他紀律制裁", DFG("1")),
       td("Besides other disciplinary actions, the Commissioner may impose a penalty", "除其他紀律行動外，關長亦可施加罰款", DAG("1"))),
    tr(rh("Whom it means to deter", "阻嚇對象"),
       td("The MSO concerned, and other MSOs from breaching the same or similar provisions", "有關金錢服務經營者，以及防止其他經營者違反相同或類似條文", DFG("5")),
       td("The licensee concerned, and other licensees generally", "有關持牌人，以及一般的其他持牌人", DAG("6"))),
    '<tr>' + rh("In common", "兩者相同") + '<td colspan="2">'
    + B("Decisions are usually publicised; a penalty should not be likely to put you in financial jeopardy; the more serious the breach, the likelier and larger the penalty; and the same four groups of factors in the figure above.",
        "決定通常會公布；罰款不應令你陷入財政困境；違規越嚴重，越可能被罰且罰款越高；以及上圖所示相同的四組因素。")
    + cite_html(cc(DFG("3, 7–9"), DAG("4, 7–9"))) + '</td></tr>',
], note=B("What each guideline is in law, and why they share a name, is on the <a href=\"#p2-guidelines\">Part 2 page</a>.", "兩份指引在法律上的地位，以及名稱為何相近，見<a href=\"#p2-guidelines\">第2部一頁</a>。"), minw=820, cls='cmp')

J_ = sec('penalty', [("Disciplinary Fining Guideline", "《紀律處分罰款指引》"), ("May 2018 · s.23", "2018年5月 · 第23條"),
                     ("Disciplinary Action Guideline", "《施加罰款紀律行動指引》"), ("April 2018 · s.45", "2018年4月 · 第45條")],
         ("How the Commissioner sets a pecuniary penalty", "關長如何釐定罰款"),
    P("The two guidelines list the same factors, numbered the same way in paragraph 9. On the left are those that make a penalty heavier, on the right those that make it lighter. Both columns feed the grey box where seriousness is weighed. Of the other grey boxes, the ceiling and \"Not your ruin\" (paragraph 7) are limits that hold whatever the factors say. \"Consistency\" is not a limit, and its arrow runs up into the seriousness box: it is itself among the factors weighed in judging seriousness (paragraphs 9(c)(iii) and 9(d)(ii)). What was done in similar cases, and what other authorities did about the same incident, count too.",
      "兩份指引列出相同的因素，並同樣編號於第9段。左邊令罰款較重，右邊令罰款較輕。兩邊的因素都導向衡量嚴重程度的灰色方格。其餘灰色方格中，「上限」及「不致令你陷入困境」（第7段）是不論因素為何都適用的限制。「一致」並非限制，故其箭頭向上導向衡量嚴重程度的方格：它同屬第9段衡量嚴重程度時考慮的因素（第9(c)(iii)及9(d)(ii)段）。過往類似個案的處理，以及其他有關當局就相同事件採取的行動，亦會納入考慮。")
    + fig(fig_scale, ("Paragraph references are to either guideline. Neither list is complete: the Commissioner considers all the circumstances, some factors may not apply, and others not listed may.",
                        "段落編號適用於兩份指引。兩份清單均非詳盡無遺：關長會考慮所有情況，部分因素未必適用，未列出的因素亦可能相關。"), SCALE_KEY)
    + PEN_TBL
    + traps(
        trap(("Following the guidance of the day is close to a shield", "遵從當時的指引近乎一面盾牌"),
             ("Both guidelines say the Commissioner will generally not take disciplinary action for conduct in line with the guidance current at the time. What counts is the guidance in force then, not the version you are reading now.",
              "兩份指引均指出，關長一般不會就符合當時有效指引的行為採取紀律行動。關鍵是當時有效的指引，而非你現在閱讀的版本。"),
             cc(DFG("9(d)(i)"), DAG("9(d)(i)"))),
        trap(("Self-reporting counts when it is prompt, effective and complete", "主動舉報須迅速、有效及完整才算數"),
             ("The mitigating factor is bringing the breach, or a possible breach, to the Commissioner's attention promptly, effectively and completely. A late or partial disclosure falls short of it.",
              "減輕因素是迅速、有效及完整地把違規或可能的違規告知關長。延遲或只作部分披露，即未符合此因素。"),
             cc(DFG("9(d)(iv)"), DAG("9(d)(iv)"))),
    ))

GL_NAV = [('route', 'Getting licensed', '申領牌照'), ('premises', 'Premises and offices', '處所與辦事處'),
          ('standing', 'Standing requirements', '持續要求'), ('plans', 'Business Plan and Policy', '業務計劃與政策'),
          ('fitproper', 'Fit and proper', '適當人選'), ('ca', 'The Assessment', '能力評核'),
          ('renewal', 'Renewal countdown', '續牌倒數'), ('changes', 'Changes and forms', '改變與表格'),
          ('endings', 'Refusal and revocation', '拒絕與撤銷'), ('penalty', 'Setting a penalty', '釐定罰款')]
GL_BODY = A + B_ + C_ + D_ + E_ + F_ + G_ + H_ + I_ + J_
