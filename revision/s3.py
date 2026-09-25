# AMLO Schedule 3: fees, with the lettered Schedules 3A to 3K that follow it.
from ui import *

FEE_SRC = (("Sch. 3", "附表3"), ("Licensing Guide fee schedule", "《牌照指引》收費表"))


def cc(*cs):
    """Join several citations into one."""
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


def fee_row(item, now, cite=None, sub=False, flagit=False):
    cls = ' class="sub"' if sub else ''
    name = f'<td{cls}>{B(*item)}{flag() if flagit else ""}{cite_html(cite)}</td>'
    return f'<tr>{name}<td class="fee"><span class="answer" tabindex="0">{B(*now)}</span></td></tr>'


FEES = table([th("The application or service", "申請或服務"), th("Fee from 15 May 2026", "2026年5月15日起的費用")], [
    '<tr class="divhead"><td colspan="2">' + B("Your licence", "你的牌照") + '</td></tr>',
    fee_row(("Apply for a licence", "申請批給牌照"), ("$3,810", "$3,810"), "item 4 Sch. 3"),
    fee_row(("plus, for each additional business premises", "就每多一個營業處所，另加"), ("$2,440", "$2,440"), sub=True, flagit=True),
    fee_row(("plus, for each person subject to the fit and proper test", "就每一個須判定是否適當人選的人，另加"), ("$945", "$945"), sub=True),
    fee_row(("Renew a licence", "申請牌照續期"), ("$910", "$910"), "item 5 Sch. 3"),
    fee_row(("plus, for each additional business premises", "就每多一個營業處所，另加"), ("$410", "$410"), sub=True, flagit=True),
    fee_row(("plus, for each person subject to the fit and proper test", "就每一個須判定是否適當人選的人，另加"), ("$945", "$945"), sub=True),
    '<tr class="divhead"><td colspan="2">' + B("Changes while you hold it", "持牌期間的改變") + '</td></tr>',
    fee_row(("Approval for a new director, ultimate owner or partner", "批准擔任董事、最終擁有人或合夥人"), ("$945 for each person", "每人$945"), "items 6–8 Sch. 3"),
    fee_row(("Add new business premises", "加入新的營業處所"), ("$2,440 for each premises", "每一新處所$2,440"), "item 9 Sch. 3"),
    fee_row(("Operate a money service at particular premises", "在特定處所經營金錢服務"), ("$2,440 for each premises", "每一處所$2,440"), "item 10 Sch. 3"),
    '<tr class="divhead"><td colspan="2">' + B("The public register", "公開登記冊") + '</td></tr>',
    fee_row(("Certified copy of an entry in, or extract from, the register", "核證登記冊內記項或其摘錄的複本"), ("$160 per copy", "每份$160"), "item 1 Sch. 3"),
    fee_row(("Uncertified copy, charged for each page or part of a page", "未經核證複本，按每頁或每頁的部分收費"), ("$1.5 per page", "每頁$1.5"), "item 2 Sch. 3"),
    fee_row(("The Commissioner's certificate that a name was entered, removed or never entered", "關長就某姓名曾記入、已刪除或從未記入登記冊而發出的證明書"), ("$160 per copy", "每份$160"), "item 3 Sch. 3 · s.28(1)(b)"),
], note=B("These are the Schedule 3 fees as amended by L.N. 22 of 2026, in force from 15 May 2026. The Licensing Guide fee schedule lists the same figures for the licence and approval fees (items 4 to 10); the register fees (items 1 to 3) appear only in Schedule 3.",
          "上表為經2026年第22號法律公告修訂、自2026年5月15日起實施的附表3費用。《牌照指引》的收費表就牌照及批准申請的費用（第4至10項）列出相同的數字；登記冊的收費（第1至3項）只見於附表3。") + ' ' + cite_html(cc(*FEE_SRC)), minw=320, cls='fees')

A = sec('fees', [("Schedule 3", "附表3"), ("fees", "費用"), ("from 15 May 2026", "2026年5月15日起")],
        ("What each application costs", "每項申請的收費"),
    P("The right-hand column is the fee to learn. Base fees cover the first premises, so the add-ons are for each <b>additional</b> one.",
      "右欄是要記的費用。基本費用已包括第一個處所，故附加費按每一個<b>額外</b>處所計算。")
    + FEES
    + traps(
        trap(("$945 appears three times", "$945出現三次"),
             ("It is the add-on for each person subject to the fit and proper test on a new licence, charged again for each of them with every renewal, and the fee for each person named in an approval application. One number, three uses.",
              "它是申請批給牌照時就每一個須判定是否適當人選的人另加的費用；每次申請續期時，須再就每一人繳付；它亦是申請批准時就申請所關乎的每一人收取的費用。同一數字，三種用途。"),
             cc("items 4–8 Sch. 3", FEE_SRC[1])),
        trap(("Renewal is cheaper per premises", "續期時每個處所收費較低"), None, "items 4–5, 9 Sch. 3",
             vs=[(("Grant, or adding premises mid-term", "批給，或在有效期內加入處所"), ("$2,440 for each additional premises.", "每多一個處所$2,440。")),
                 (("Renewal", "續期"), ("$410 for each additional premises.", "每多一個處所$410。"))]),
    ))

# ---------------------------------------------------------------- B. working out a bill
def term(amount, en, tc, cls=''):
    k = f' {cls}' if cls else ''
    return f'<span class="term{k}"><b>{esc(amount)}</b>{B(en, tc)}</span>'


OP = '<span class="op">+</span>'
EQ = '<span class="op">=</span>'


def eq(label_en, label_tc, parts):
    return f'<div class="eqrow"><p class="eqlab">{B(label_en, label_tc)}</p><div class="eq">{"".join(parts)}</div></div>'


BILL = ('<figure class="eqfig">'
        + eq("A new licence", "新牌照", [term("$3,810", "base, covering the first premises", "基本費用，已包括第一個處所"), OP,
                                        term("$2,440 ×", "each additional premises", "每一個額外處所"), OP,
                                        term("$945 ×", "each person subject to the fit and proper test", "每一個須判定是否適當人選的人")])
        + eq("A renewal", "續期", [term("$910", "base", "基本費用"), OP, term("$410 ×", "each additional premises", "每一個額外處所"), OP,
                                  term("$945 ×", "each person subject to the fit and proper test", "每一個須判定是否適當人選的人")])
        + '<p class="eqlab ex">' + B("Worked example: a company with 2 premises, 3 directors and 1 ultimate owner, so 4 people are tested",
                                     "例子：一間公司有2個處所、3名董事及1名最終擁有人，即4人須接受測試") + '</p>'
        + eq("Applying", "申請批給", [term("$3,810", "base", "基本費用"), OP, term("$2,440", "1 additional premises", "1個額外處所"), OP,
                                     term("$3,780", "4 people × $945", "4人 × $945"), EQ, term("$10,030", "to apply", "申請費用", 'total')])
        + eq("Renewing", "續期", [term("$910", "base", "基本費用"), OP, term("$410", "1 additional premises", "1個額外處所"), OP,
                                  term("$3,780", "4 people × $945", "4人 × $945"), EQ, term("$5,100", "to renew", "續期費用", 'total')])
        + '<figcaption>' + B("The corporation itself is never counted: for a company, the people tested are each director and any ultimate owner. For a partnership, each partner and any ultimate owner; for an individual, the individual and any ultimate owner.",
                             "法團本身從不計算在內：就公司而言，受測試的是每名董事及任何最終擁有人；就合夥而言，是每名合夥人及任何最終擁有人；就個人而言，是該名個人及任何最終擁有人。") + ' ' + cite_html("s.30(3)(a)") + '</figcaption></figure>')

B_ = sec('bill', ["items 4–5 Sch. 3", "s.30(3)"],
         ("Working out a bill", "計算費用"),
    P("Each line is a formula: a base fee, then two add-ons you multiply. The two lines below them work one real case through both formulas, so the difference between applying and renewing is visible.",
      "每一行都是一條公式：基本費用，加上兩項須乘算的附加費。下面兩行以同一個案例套用兩條公式，讓你看清申請與續期的分別。")
    + BILL
    + numreq([
        (("$3,810 / $910", "$3,810／$910"),
         ("The base fee that must accompany a grant or a renewal application", "批給或續期申請須隨附的基本費用"),
         ("Every grant or renewal application, whatever its size, before the add-ons. The fee goes in with the application, and a renewal application must be made not later than 45 days before the licence expires", "每宗批給或續期申請，不論規模，未計附加費。申請須附隨該費用；續期申請須在牌照期滿前45日或之前提出"),
         ("The application does not meet the Ordinance's requirements for a grant or renewal application", "該申請即不符合條例對批給或續期申請的規定"),
         "s.30(1)(b) · s.31(2)(a), (c) · items 4–5 Sch. 3"),
        (("$945", "$945"),
         ("The fee for each person whose approval, as director, ultimate owner or partner, you apply for", "就每名申請批准擔任董事、最終擁有人或合夥人的人士須繳的費用"),
         ("Before that person takes up the role", "在該人就任之前"),
         ("A person who, without reasonable excuse, becomes a director, ultimate owner or partner without the Commissioner's written approval commits an offence: level 5 fine and 6 months' imprisonment. The licensee may also face disciplinary action",
          "任何人無合理辯解而未獲關長書面批准即成為董事、最終擁有人或合夥人，即屬犯罪：可處第5級罰款及監禁6個月。關長亦可對持牌人採取紀律行動"),
         "s.35(1), (2), (7) · s.36(1), (2), (7) · s.37(1), (2), (7) · items 6–8 Sch. 3 · s.43(1)(c)"),
    ]))

# ---------------------------------------------------------------- C. who sets fees, and refunds
C_ = sec('rules', ["s.50", "s.34(7) · s.41(3)", "s.27–s.28"],
         ("Who sets the fees, and when money is not returned", "誰訂定費用，以及何時不獲退還"),
    P("Five short questions with fixed answers.", "五條答案固定的簡短問題。")
    + table([th("The question", "問題"), th("The answer", "答案")], [
        tr(rh("Who can change the fees?", "誰可修改費用？", "s.50 · s.26"),
           td("The Commissioner, by notice in the Gazette. Unlike making Part 5 regulations, this is a power he may delegate", "關長，藉憲報公告修改。與訂立第5部規例不同，這是一項他可以轉授的權力")),
        tr(rh("If the licence is revoked or suspended, is any licence fee refunded?", "牌照被撤銷或暫時吊銷，牌照費會否退還？", "s.34(7)"),
           td("No. No fee paid for the grant or renewal is refunded", "不會。批給或續期所繳的費用一概不獲退還")),
        tr(rh("If you cease business and return the licence?", "如你停業並交回牌照？", "s.41(3)"),
           td("No. The same rule applies", "不會。適用同一規則")),
        tr(rh("Can the Commissioner waive a money service fee?", "關長可否寬免金錢服務的費用？", ("Part 5 · s.53ZTN · s.53ZVR", "第5部 · 第5B部證監會可寬免費用的條文 · 第5C部關長可寬免費用的條文")),
           td("Part 5 gives him no such power. The fee waivers in the Ordinance sit in the virtual asset and precious metals regimes", "第5部並無賦予此權力。條例中的寬免費用條文，只見於虛擬資產及貴金屬制度", post=flag())),
        tr(rh("Does inspecting the register cost anything?", "查閱登記冊是否收費？", "s.27(4) · s.28(1)"),
           td("No: the public may inspect it free during normal office hours. Copies and certificates are charged at the Schedule 3 rates", "不收費：公眾可在正常辦公時間內免費查閱。複本及證明書則按附表3收費")),
    ], minw=720))

# ---------------------------------------------------------------- D. the lettered schedules
D_ = sec('lettered', [("Schedules", "附表"), "3A–3K", ("other regimes", "其他制度")],
         ("Schedules 3A to 3K: the other regimes' schedules", "附表3A至3K：其他制度的附表"),
    P("These eleven schedules sit between Schedule 3 and Schedule 4 because they were added later for Parts 5A to 5C. None places a duty on a money service operator; knowing what each one is protects you from a distractor that borrows its number.",
      "這十一個附表位於附表3與附表4之間，是其後為第5A至5C部而增補的。它們都不對金錢服務經營者施加責任；知道每個附表的內容，可避免被借用其編號的干擾選項誤導。")
    + table([th("Schedule", "附表"), th("What it contains", "內容"), th("The regime", "所屬制度")], [
        tr(rh("3A", "3A"), td("Fees", "費用"), td("Trust or company service providers, Part 5A", "信託或公司服務提供者（第5A部）")),
        tr(rh("3B", "3B"), td("The list of virtual asset services", "虛擬資產服務的清單"), td("Virtual asset service providers, Part 5B", "虛擬資產服務提供者（第5B部）")),
        tr(rh("3C", "3C"), td("Fees", "費用"), td("Virtual asset service providers, Part 5B", "虛擬資產服務提供者（第5B部）")),
        tr(rh("3D", "3D"), td("Prescribed particulars of associated entities", "有聯繫實體的訂明詳情"), td("Virtual asset service providers, Part 5B", "虛擬資產服務提供者（第5B部）")),
        tr(rh("3E", "3E"), td("What an annual return must contain", "周年申報表的資料"), td("Virtual asset service providers, Part 5B", "虛擬資產服務提供者（第5B部）")),
        tr(rh("3F", "3F"), td("Prescribed financial statements and other documents of auditable entities", "須予審計實體的訂明財務報表及其他訂明文件"), td("Virtual asset service providers, Part 5B", "虛擬資產服務提供者（第5B部）")),
        tr(rh("3G", "3G"), td("Transitional arrangements for the 2022 amending Ordinance", "《2022年修訂條例》的過渡安排"), td("Virtual asset service providers, Part 5B", "虛擬資產服務提供者（第5B部）")),
        tr(rh("3H", "3H"), td("$120,000: the amount in the definition of a specified cash transaction", "$120,000：指明現金交易定義中的款額"), td("Dealers in precious metals and stones, Part 5C", "貴金屬及寶石交易商（第5C部）", post=flag())),
        tr(rh("3I", "3I"), td("$120,000: the amount in the definition of a specified transaction", "$120,000：指明交易定義中的款額"), td("Dealers in precious metals and stones, Part 5C", "貴金屬及寶石交易商（第5C部）")),
        tr(rh("3J", "3J"), td("What a cash transaction report must contain", "現金交易報告須提供的資料"), td("Dealers in precious metals and stones, Part 5C", "貴金屬及寶石交易商（第5C部）")),
        tr(rh("3K", "3K"), td("Fees", "費用"), td("Dealers in precious metals and stones, Part 5C", "貴金屬及寶石交易商（第5C部）")),
    ], minw=700)
    + traps(
        trap(("Two $120,000 figures, in two different places", "兩個$120,000，位於兩個不同地方"), None, cc("s.3(1)(b) Sch. 2", "Sch. 3H", "Sch. 3I", ("s.53ZTZ", "第5C部的釋義條文")),
             vs=[(("Yours", "你的"), ("The CDD threshold for an occasional transaction other than a wire or virtual asset transfer, in Schedule 2. The other Schedule 2 thresholds are on the <a href=\"#s2-thresholds\">Schedule 2 page</a>.", "附表2中，電傳轉帳及虛擬資產轉帳以外的非經常交易的客戶盡職審查門檻。附表2的其他門檻見<a href=\"#s2-thresholds\">附表2一頁</a>。")),
                 (("Not yours", "不是你的"), ("The precious metals and stones dealers' amounts for a specified cash transaction (Schedule 3H, paid in cash) and a specified transaction (Schedule 3I, paid other than in cash).", "附表3H（指明現金交易，以現金付款）及附表3I（指明交易，藉現金以外方式付款）中，貴金屬及寶石交易商適用的款額。"))]),
        trap(("Virtual asset transfers still reach you through Schedule 2", "虛擬資產轉帳仍經附表2與你有關"),
             ("The virtual asset licensing schedules are not yours, but the Guideline's examples of occasional transactions include virtual asset transfers. An MSO must carry out CDD before one involving virtual assets that amount to no less than $8,000; section 13A of Schedule 2 sets special requirements for virtual asset transfers; and the records of such an occasional transaction must be kept for at least 5 years from the date it is completed.",
              "虛擬資產發牌制度的附表與你無關；但《打擊洗錢指引》所舉的非經常交易例子包括虛擬資產轉帳。金錢服務經營者在執行涉及不少於8,000元的款額的虛擬資產的虛擬資產轉帳之前，須執行客戶盡職審查；附表2第13A條訂明虛擬資產轉帳的特別規定；而該等非經常交易的紀錄，須在自交易完成之日起計的至少5年期間內備存。"),
             ("¶4.2.1, 8.4 · s.3(1A), 13A, 20(3A) Sch. 2", "第4.2.1及8.4段 · 附表2第3(1A)、13A、20(3A)條")),
    ))

S3_NAV = [('fees', 'The fee table', '費用表'), ('bill', 'Working out a bill', '計算費用'),
          ('rules', 'Who sets fees; refunds', '費用的訂定與退還'), ('lettered', 'Schedules 3A to 3K', '附表3A至3K')]
S3_BODY = A + B_ + C_ + D_
