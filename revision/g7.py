# AML/CFT Guideline Chapter 7: suspicious transaction reports and law
# enforcement requests. The duty and its offences, spotting suspicion, the route
# from staff to the MLRO, filing with the JFIU, what follows an STR, and the court
# documents an MSO may be served with. Ongoing monitoring stays on the Schedule 2 page.
from ui import *
from g7_fig import (DO, UN, cc, fig_safe, SAFE_KEY, fig_internal, INTERNAL_KEY, fig_after, AFTER_KEY,
                    fig_lea, LEA_KEY)


CIR26 = ("Circular 20 Jan 2026, area 4", "2026年1月20日通函，範疇4")
SAMPLE5 = ("Sample question 5", "參考試題5")
CAP1 = ("fn 60 · Cap. 1 s.3", "註60 · 第1章第3條")

# ---------------------------------------------------------------- A. the duty
LINKED = ('<td rowspan="3">' + B("Drug trafficking or an indictable offence", "販毒或可公訴罪行") + '</td>'
          + '<td rowspan="3">' + B("DTROP and OSCO s.25A(1)", "《販毒（追討得益）條例》及《有組織及嚴重罪行條例》第25A(1)條") + cite_html("¶7.1") + '</td>')

A_ = sec('duty', [("Guideline Ch. 7", "指引第7章"), ("¶7.1–7.6", "第7.1至7.6段"), ("fn 59–60", "註59至60"), ("¶1.22–1.25", "第1.22至1.25段")],
         ("You know or suspect: the duty to report, and the duty to keep quiet", "你知悉或懷疑：舉報的責任，以及保密的責任"),
    P("The duty is not the MSO's alone: it falls on any person who knows or suspects. Read the first table for what must be reported and how, the second to tell knowledge from suspicion, and the third for the situations where the duty is easily assumed away.",
      "這項責任不只屬於金錢服務經營者：任何知悉或懷疑的人均須舉報。第一個表說明須舉報甚麼及如何舉報，第二個表分辨知悉與懷疑，第三個表列出容易被誤以為毋須舉報的情況。")
    + table([th("You know or suspect that property", "你知悉或懷疑某財產"), th("Linked to", "涉及"), th("The law", "法例")], [
        tr(td("In whole or in part, directly or indirectly, <b>represents</b> any person's proceeds", "全部或部分、直接或間接<b>代表</b>任何人的得益", "¶7.1(a)"), LINKED),
        tr(td("<b>Was used</b> in connection with", "<b>曾</b>在有關的情況下<b>使用</b>", "¶7.1(b)")),
        tr(td("<b>Is intended to be used</b> in connection with", "<b>擬</b>在有關的情況下<b>使用</b>", "¶7.1(c)", post=flag())),
        tr(td("<b>Is</b> terrorist property", "<b>是</b>恐怖分子財產", "¶7.1"),
           td("Terrorism", "恐怖主義"),
           td("UNATMO s.12(1)", "《聯合國（反恐怖主義措施）條例》第12(1)條", "¶7.1")),
    ], note=B("<b>What you do:</b> file an STR with the JFIU as soon as it is reasonable to do so, together with any matter on which the knowledge or suspicion is based. <b>Any property</b> includes both movable and immovable property within the meaning of section 3 of the Interpretation and General Clauses Ordinance (Cap. 1), which says property includes money, goods, choses in action and land; and obligations, easements and every description of estate, interest and profit, present or future, vested or contingent, arising out of or incident to such property.",
              "<b>你須做的：</b>在合理範圍內盡快向財富情報組提交可疑交易報告，並連同該項知悉或懷疑所根據的任何事宜。<b>任何財產</b>包括《釋義及通則條例》（第1章）第3條所指的動產及不動產；根據該條，「財產」包括金錢、貨物、法據動產和土地；以及由此產生或附帶的義務、地役權以及各類產業、利益和利潤，不論是現存的或將來的、既得的或待確定的。")
            + ' ' + cite_html(cc("¶7.1", CAP1)), minw=760)
    + table([th("", ""), th("Knowledge", "知悉"), th("Suspicion", "懷疑")], [
        tr(rh("What it is", "是甚麼"),
           td("Generally likely to include (a) actual knowledge; (b) knowledge of circumstances which would indicate facts to a reasonable person; and (c) knowledge of circumstances which would put a reasonable person on inquiry",
              "一般而言可能包括(a)實際知悉；(b)知悉一個合理的人會認為是事實的情況；及(c)知悉某些會令合理的人提出查詢的情況", "¶7.2", post=flag()),
           td("More subjective. It is personal, and falls short of proof based on firm evidence",
              "較為主觀。懷疑是個人的，並且缺乏確鑿的證據作證明", "¶7.3")),
        '<tr>' + rh("What you need not know, for either", "兩者均無需知道") + '<td colspan="2">'
        + B("The nature of the criminal activity behind the money laundering, or that the funds themselves definitely came from the crime. The same holds for terrorist financing.",
            "涉及洗錢的相關犯罪活動的性質，或資金本身是否確實從犯罪而來。此原則同樣適用於恐怖分子資金籌集。")
        + cite_html("¶7.4") + '</td></tr>',
    ], note=B("<b>At your counter:</b> where a customer's transaction, or series of transactions, does not fit what you know of the customer or is unusual, for example a pattern with no apparent economic or lawful purpose, you should take appropriate steps to examine it further and see whether there is any suspicion. How to examine it is on the <a href=\"#s2-monitoring\">Schedule 2 page</a>.",
              "<b>在你的櫃位：</b>如客戶的某項交易或連串交易不符合你對該客戶的認知或異乎尋常（例如模式並無明顯經濟或合法目的），應採取適當步驟進一步審查，識辨是否有可懷疑之處。審查方法見<a href=\"#s2-monitoring\">附表2一頁</a>。")
            + ' ' + cite_html("¶7.3 · ¶5.10–5.14"), minw=760, cls='cmp')
    + h3("Situations where the duty still applies", "舉報責任仍然適用的情況")
    + table([th("The situation", "情況"), th("Why the duty still applies", "為何仍須舉報")], [
        tr(td("No transaction was conducted by or through you", "你沒有進行交易，亦沒有交易透過你進行", "¶7.5(a)"),
           td("Once knowledge or suspicion has formed, you should file even where nothing passed through you", "知悉或懷疑一旦確立，即使沒有交易經你進行，也應提交報告", "¶7.5(a)")),
        tr(td("The customer only tried: the transaction was attempted, not completed", "客戶只是試圖進行交易，交易並未完成", "fn 60", post=flag()),
           td("The duty arises whenever a suspicion does, without reference to transactions as such, so attempted transactions are covered", "只要產生懷疑即確立舉報責任，無需考慮交易本身，因此涵蓋試圖進行的交易", "fn 60")),
        tr(td("The amount is small, below every CDD threshold", "款額細小，低於所有盡職審查門檻", "fn 60"),
           td("Suspicions must be reported irrespective of the amount involved. The thresholds are on the <a href=\"#s2-thresholds\">Schedule 2 page</a>", "不論所涉金額，均須舉報懷疑。門檻見<a href=\"#s2-thresholds\">附表2一頁</a>", cc("fn 60", CIR26))),
        tr(td("The property is not money: goods, land, an interest in property", "財產不是金錢：貨物、土地、財產權益", CAP1),
           td("The duty applies to any property, movable or immovable", "舉報責任適用於任何財產，包括動產及不動產", CAP1)),
        tr(td("You cannot tell which crime lies behind it", "你不能判斷背後涉及哪種罪行", "¶7.4"),
           td("Knowledge or suspicion does not need the nature of the underlying crime", "知悉或懷疑無需知道相關犯罪活動的性質", "¶7.4")),
        tr(td("The crime happened outside Hong Kong", "罪行在香港以外發生", ("Circular 13 Dec 2021", "2021年12月13日通函")),
           td("Conduct abroad that would be indictable here counts: see the <a href=\"#ci-warnings\">Circulars page</a>", "在外地發生、假若在香港發生即屬可公訴罪行的行為亦計算在內：見<a href=\"#ci-warnings\">通函一頁</a>",
              ("OSCO s.25(4)", "《有組織及嚴重罪行條例》第25(4)條"))),
        tr(td("You have already reported this customer once", "你已就此客戶舉報一次", "¶7.28"),
           td("Each further suspicion, of the same nature or not, is reported again: see <a href=\"#after\">After the report</a>", "其後每項可疑情況，不論是否屬同一性質，均須再次報告：見<a href=\"#after\">提交報告後</a>", "¶7.28")),
    ], minw=760)
    + numreq([
        (("3 months and $50,000", "監禁3個月及罰款50,000元"),
         ("Report knowledge or suspicion to the JFIU as soon as it is reasonable", "在合理範圍內盡快向財富情報組舉報所知悉或懷疑的事項"),
         ("Any person, under DTROP, OSCO or UNATMO", "任何人，根據《販毒（追討得益）條例》、《有組織及嚴重罪行條例》或《聯合國（反恐怖主義措施）條例》"),
         ("An offence: failing to disclose as soon as it is reasonable", "即屬犯罪：未能在合理範圍內盡快作出披露"),
         cc("¶7.1", "¶1.24", DO("25A(7)"), UN("14(5)"))),
        (("3 years and a fine", "監禁3年及罰款"),
         ("Disclose nothing likely to prejudice an investigation, such as telling the customer a report has been made", "不得披露任何可能影響調查的事宜，例如告知客戶已作出報告"),
         ("Once a report has been made, and also where a suspicion has been raised inside your business but not yet reported to the JFIU", "已作出報告後，或已在內部提出、但尚未向財富情報組報告懷疑時"),
         ("An offence: tipping off", "即屬犯罪：通風報訊"),
         cc("¶1.25", "¶7.6", DO("25A(5)"), UN("12(5)"))),
        (("14 years and $5,000,000", "監禁14年及罰款五百萬元"),
         ("Do not deal with property you know, or have reasonable grounds to believe, represents proceeds of drug trafficking or an indictable offence", "不得處理你知道或有合理理由相信代表販毒或可公訴罪行得益的財產"),
         ("Under DTROP and OSCO. An STR made on the conditions in ¶7.25 gives a defence for the acts it discloses", "根據《販毒（追討得益）條例》及《有組織及嚴重罪行條例》。符合第7.25段條件的可疑交易報告，可就其所披露的作為提供免責辯護"),
         ("An offence: dealing with the proceeds, the money laundering offence", "即屬犯罪：處理有關得益，即洗錢罪行"),
         cc("¶1.22", "¶7.25", ("DTROP & OSCO s.25", "《販毒（追討得益）條例》及《有組織及嚴重罪行條例》第25條"))),
    ])
    + traps(
        trap(("Tipping off starts before the JFIU hears anything", "通風報訊在財富情報組收到報告前已可構成"),
             ("Revealing to anyone information that might prejudice an investigation is an offence, and telling a customer that a report has been made is the plain example. The provision also covers a suspicion raised internally within the MSO that has not yet been reported to the JFIU.",
              "向任何人士透露任何可能會對調查工作有影響的資訊，即屬犯罪；告知客戶已作出報告便是明顯例子。有關條文亦包括已於金錢服務經營者內部提出懷疑、但尚未向財富情報組報告的情況。"),
             cc("¶7.6", DO("25A(5)"), UN("12(5)"))),
        trap(("A reasonable person's view can amount to knowledge", "合理的人的看法亦可構成知悉"),
             ("Knowledge is not only what you actually know. Knowing circumstances that would indicate the facts to a reasonable person, or that would put a reasonable person on inquiry, is likely to count as knowledge too. Suspicion is the personal, subjective state that falls short of proof.",
              "知悉不只是實際知悉。知悉一個合理的人會認為是事實的情況，或知悉某些會令合理的人提出查詢的情況，亦可能屬知悉。懷疑則是個人及主觀的，並且缺乏確鑿的證據作證明。"),
             "¶7.2–7.3"),
        trap(("Two ways of saying how fast", "兩種關於「多快」的說法"), None, cc("¶7.1", "¶7.5(b)"),
             vs=[(("The statute, as the Guideline puts it", "指引轉述的法例"), ("File the STR as soon as it is reasonable for you to do so.", "在合理範圍內盡快提交可疑交易報告。")),
                 (("The Guideline's own wording", "指引本身的用語"), ("The STR must be made as soon as reasonably practical after the suspicion was first identified.", "經最初識辨有關懷疑後，必須在切實可行範圍內盡快提交可疑交易報告。"))]),
    ))

# ---------------------------------------------------------------- B. spotting suspicion
# ¶7.10's indicators, each cut to a short phrase that keeps its point; True marks the ones a callout explains
FLAGS = [
    (("Transactions that make no economic sense", "不合乎經濟原則的交易"), "¶7.10(a)", [
        ("Out of line with the customer's usual activities", "與客戶的慣常活動不符", False),
        ("At odds with what you know of the customer, or with the transaction's purpose", "與你對客戶的認知或交易目的不符", False),
        ("Frequent or several transactions, each below the CDD thresholds", "頻繁或分數次進行、每宗低於盡職審查門檻的交易", True),
        ("<b>Structuring or smurfing</b>: many small transactions where one or a few large ones would do", "<b>「分拆整合」或「化整為零」</b>：可一次或數次過進行的大額款項，分成多項小額交易", True),
        ("<b>U-turn</b>: funds from abroad sent on to another person or company in that same jurisdiction, or to the sender's account elsewhere", "<b>「掉頭式」</b>：從外地匯入的款項，再轉帳至同一司法管轄區的其他人或公司，或匯往匯款人在另一司法管轄區的帳戶", True),
        ("Funds routed through various institutions or persons for no need", "不必要地經不同金融機構或人士調度資金", False),
        ("A sharp rise in number, frequency or amount without apparent cause", "交易數量、頻密程度或款額無故大幅上升", False),
        ("Many senders paying into one person's account", "多名匯款人轉帳至同一人的帳戶", False),
        ("No apparent link between originator and recipient, or between the customer and the jurisdiction the money goes to or comes from", "匯款人與收款人沒有明顯關係，或客戶與其匯款／收款的司法管轄區沒有明顯連繫", False),
    ]),
    (("Cash-intensive, with abnormal patterns", "模式異常的現金密集型交易"), "¶7.10(b)", [
        ("Frequent large cash deals the customer's business or background does not justify", "客戶業務或背景無法解釋的頻繁大額現金交易", False),
        ("Large or frequent remittances to persons and companies unconnected with the business", "大額或頻繁匯款給與其業務通常沒有關連的個人及公司", False),
        ("An unusually large amount of small notes exchanged for large notes in another currency", "將異常大量的小額鈔票，兌換成另一貨幣的較大額鈔票", False),
        ("Numerous transactions by one customer, each small, together substantial or over the threshold", "客戶進行多宗交易，每宗細小，累積總額龐大或超過門檻", True),
        ("Customers together and at the same time using separate branches for large cash transactions", "多名客戶一起在同一時間使用不同分行處理大額現金交易", False),
        ("Counterfeit notes or forged instruments", "涉及偽鈔或偽造工具", False),
        ("Large regular payments with higher-risk jurisdictions, not clearly genuine", "與「較高風險」司法管轄區之間、無法清楚識別為真正交易的定期大額支付", False),
    ]),
    (("Trade-based transactions", "貿易相關的交易"), ("¶7.10(c) · fn 62–63", "第7.10(c)段 · 註62至63"), [
        ("Goods shipped to or from a higher-risk jurisdiction", "商品付運往返「較高風險」的司法管轄區", False),
        ("Goods of a higher-risk type, e.g. high-value low-volume goods, or dual-use goods that turn over fast and are hard to value", "屬「較高風險」類別的商品，例如價值高、體積小的產品，或轉讓速度快、難以估值的兩用物品", False),
        ("Goods on the bill of lading or invoice differ from what is shipped", "提單或發票上的商品說明與實際付運的商品不符", False),
        ("Invoice value far from fair market value", "發票價值與市場價值有重大差異", False),
        ("Shipment size out of line with the trader's usual business", "裝運大小與進出口商的常規業務規模不相稱", False),
        ("Payment method out of line with the risk, e.g. advance payment for a shipment from a new supplier in a high-risk jurisdiction", "支付方法與風險特徵不相稱，例如向高風險司法管轄區的新供應商預繳貨款", False),
        ("Cash or payments from unconnected third parties", "從與交易沒明顯聯繫的第三方收取現金或款項", False),
        ("Letters of credit repeatedly amended or extended", "信用證經反覆修改或頻密延期", False),
        ("Front or shell companies", "掛名或空殼公司", False),
        ("Transhipment for no apparent economic reason", "無明顯經濟原因的轉運", False),
        ("A shipment that makes no economic sense", "裝運不合乎經濟原則", False),
    ]),
    (("Other types of transactions", "其他類別的交易"), "¶7.10(d)", [
        ("Activity out of line with age, occupation or income", "帳戶活動或交易量與年齡、職業或收入不相稱", False),
        ("Links to terrorism-associated jurisdictions or entities, or designated terrorists", "涉及據稱與恐怖主義活動有關的司法管轄區或實體，或被指認為恐怖分子的人", False),
        ("Frequent changes of address or authorised signatories", "頻繁地改變地址或獲授權簽署人", False),
        ("Donations to charities in conflict zones or terrorism-linked jurisdictions", "向衝突地區或據稱有恐怖主義活動的司法管轄區的慈善團體捐款", False),
        ("False identification, or third parties used to hide the sender or receiver", "虛假識別資料，或藉第三方隱藏匯款人或收款人", False),
        ("(Regular) payments with tax havens or jurisdictions exposed to serious crime or high-risk business; the amounts need not be large", "定期與「稅務天堂」或可能面對嚴重罪行或高風險業務的司法管轄區收付款項；交易額未必很大", False),
        ("Unexplained remittances with high-risk jurisdictions, out of line with usual foreign dealings", "與高風險司法管轄區之間沒有合理解釋、與慣常外地業務往來不相稱的匯款", False),
    ]),
    (("Your agents or counterparts", "你的代理人或交易對手"), "¶7.10(e)", [
        ("Reluctant to provide customers' identification", "不願提供客戶的識別資料", False),
        ("Far more large or suspicious transactions than others in the same area", "大額或可疑交易遠多於同一地區的其他代理人或交易對手", False),
        ("Many transactions for one customer, with varied name spellings, false addresses or “evolving” identification", "為同一客戶進行大量交易，名稱拼寫不一、地址虛假或識別資料不斷「演變」", False),
        ("One customer, one day, funds sent via several agent or counterpart locations", "同一客戶於同一日經多個代理人或交易對手地點傳送資金", False),
    ]),
    (("The customer's behaviour", "客戶的行為"), "¶7.10(f)", [
        ("Accompanied by others who keep a low profile, or hesitant when asked for details", "由刻意保持低調的人陪同，或被問及詳情時顯得猶豫", False),
        ("In a hurry, promising the supporting information later", "急於完成交易，並承諾稍後補交證明資料", False),
        ("No interest in comparing costs or exchange rates", "無意比較收費或兌換率", False),
        ("Several customers working together to split one transaction below the threshold", "多名客戶合謀將一項交易拆分至門檻以下", True),
        ("Cannot justify the purpose of a transaction when asked", "被詢問時未能就交易目的提供合理解釋", False),
    ]),
]


def flag_cell(items, cite):
    lines = ''.join(f'<div style="margin:0 0 6px">{B(en, tc)}{flag() if f else ""}</div>' for en, tc, f in items)
    return f'<td style="width:50%">{lines}{cite_html(cite)}</td>'


def flag_head(g):
    return f'<th style="width:50%;background:var(--panel)">{B(*g[0])}</th>'


def flag_rows():
    rows = []
    for k in range(0, 6, 2):
        a, b = FLAGS[k], FLAGS[k + 1]
        if k:
            rows.append('<tr>' + flag_head(a) + flag_head(b) + '</tr>')
        rows.append('<tr>' + flag_cell(a[2], a[1]) + flag_cell(b[2], b[1]) + '</tr>')
    return rows


FLAG_TBL = table([f'<th style="width:50%">{B(*FLAGS[0][0])}</th>', f'<th style="width:50%">{B(*FLAGS[1][0])}</th>'], flag_rows(),
                 note=B("Each line condenses one indicator of ¶7.10. The list is not exhaustive. For more indicators the Guideline points to the FATF's “Money Laundering through Money Remittance and Currency Exchange Providers” (June 2010) and “Guidance for Financial Institutions in Detecting Terrorist Financing” (April 2002), and the Asia/Pacific Group on Money Laundering's “Yearly ML/TF Typologies Report”. The circulars add their own signs for <a href=\"#ci-thirdparty\">third-party payments</a> and <a href=\"#ci-tbml\">trade-based laundering</a>.",
                        "每行濃縮第7.10段的一項指標。上述清單並非詳盡無遺。指引指出，可參考特別組織的《藉匯款和貨幣兌換供應商洗錢》（2010年6月）及《金融機構偵測恐怖分子資金籌集指引》（2002年4月），以及亞洲／太平洋反清洗黑錢組織的《洗錢／恐怖分子資金籌集案例分析年度報告》。通函另就<a href=\"#ci-thirdparty\">第三方支付</a>及<a href=\"#ci-tbml\">以貿易進行洗錢</a>列出警示跡象。")
                 + ' ' + cite_html("¶7.10 fn 61"), minw=760)

B_ = sec('spot', [("Guideline Ch. 7", "指引第7章"), ("¶7.3 · ¶7.10–7.11", "第7.3、7.10至7.11段"), ("fn 61–63", "註61至63"), ("¶5.11–5.13", "第5.11至5.13段")],
         ("Something at the counter does not add up", "櫃位上的交易有點不對勁"),
    P("Start at the top box and follow the arrows. The four boxes in the dashed frame are the JFIU's SAFE approach, which you may adopt where it applies. The red flags in the table after the figure are what should start you down this path.",
      "由頂部方格開始，順着箭嘴閱讀。虛線框內的四個方格是財富情報組推廣的ＳＡＦＥ方法，你可按情況採用。圖後表內的可疑交易指標，正是引發這個流程的訊號。")
    + fig(fig_safe, ("The guidance you give staff and agents should let them form a suspicion or recognise the signs, taking account of the transactions and customer instructions they are likely to meet, the product or service, and the means of delivery (¶7.10). Details of SAFE are on the JFIU's website (¶7.11).",
                     "你為職員及代理人提供的導引，應讓他們能產生懷疑或辨別有關跡象，並應顧及他們可能遇到的交易及客戶指示的性質、產品或服務類別及交付方式（第7.10段）。ＳＡＦＥ方法的詳情載於財富情報組網站（第7.11段）。"), SAFE_KEY)
    + h3("The red flags, in six groups", "可疑交易指標：六個類別")
    + FLAG_TBL
    + traps(
        trap(("One red flag is not proof, but it is never nothing", "單一指標不是證明，但絕不可置之不理"), None, "¶7.10",
             vs=[(("What one indicator shows", "單一指標顯示甚麼"), ("On its own it may not be enough to establish ML, TF or PF activity; several together may point to a suspicious transaction.", "個別指標或未足以確立洗錢、恐怖分子資金籌集或擴散資金籌集活動；不同情況一併出現，則可能顯示有可疑交易。")),
                 (("What it should set off", "應觸發甚麼"), ("Any relevant red flag should prompt further investigation: at least initial enquiries about the source of funds, and a request for more documents for CDD.", "偵察到任何相關訊號，應及時作進一步調查，這至少可促使對資金來源作出初步查詢，並要求提供更多關於盡職審查的證明文件。"))]),
        trap(("Splitting below the threshold: one customer or several", "拆分至門檻以下：一名客戶還是多名"), None, "¶7.10(a)(iii)–(iv), (b)(iv), (f)(iv)",
             vs=[(("One customer", "一名客戶"), ("Frequent or several transactions, each under the CDD thresholds; many small transactions where one large one would do, “structuring” or “smurfing”; numerous transactions in a short period that add up to a substantial sum or pass the threshold.", "頻繁或分數次進行、每宗低於盡職審查門檻的交易；可一次過進行卻分成多項小額交易，即「分拆整合」或「化整為零」；短時間內多宗交易，累積總額龐大或超過門檻。")),
                 (("Several customers", "多名客戶"), ("Customers working together to break one transaction into two or more below the threshold, to avoid reporting requirements.", "多名客戶看似試圖規避申報規定，合謀將一項交易拆分為兩項或更多低於門檻的交易。"))]),
        trap(("A U-turn is about where the money goes next", "「掉頭式」交易看的是款項其後流向"),
             ("Funds received from a person or company in a foreign jurisdiction are remitted out again: to another person or company in that same foreign jurisdiction, or to the sender's own account in another jurisdiction.",
              "從外地司法管轄區的某人或公司匯入的款項，再轉帳回同一外地司法管轄區的其他人或公司，或匯往匯款人在另一司法管轄區的帳戶。"),
             "¶7.10(a)(v)"),
        trap(("SAFE is a may; reporting to the MLRO is not", "採用ＳＡＦＥ方法是「可」；向洗錢報告主任報告則不是"),
             ("You may adopt the JFIU's SAFE approach where it applies. Once a suspicion forms, the internal report is not optional: your procedures should ensure that every internal report must reach the MLRO without undue delay.",
              "你可按情況採用財富情報組推廣的ＳＡＦＥ方法。懷疑一旦產生，內部報告便不是可有可無：你的程序應確保所有內部報告必須送達洗錢報告主任，不得無故延誤。"),
             "¶7.11 · ¶7.12(b)"),
        trap(("Asking questions is not tipping off", "詢問客戶並不構成通風報訊"),
             ("Enquiries made properly and in good faith do not tip the customer off. If you reasonably believe that carrying on with CDD would tip the customer off, you may stop it, but you should document the basis for that assessment and file an STR with the JFIU.",
              "憑誠信適當地詢問客戶並不構成通風報訊。如你合理地相信執行盡職審查程序會向客戶通風報訊，可停止該程序，但應把評估的基礎記錄在案，並向財富情報組提交可疑交易報告。"),
             "¶5.13"),
    ))

# ---------------------------------------------------------------- C. staff to MLRO
C_ = sec('internal', [("Guideline Ch. 7", "指引第7章"), ("¶7.7–7.9 · ¶7.12–7.20", "第7.7至7.9、7.12至7.20段"), SAMPLE5],
         ("A member of staff is suspicious: straight to the MLRO, unfiltered", "職員有懷疑：直接報告洗錢報告主任，不得過濾"),
    P("The left-hand column is the report's path from the counter to the MLRO's decision; each box on the right hangs off the step beside it, and the word on the dashed line says how. Colour tells you whose duty it is and whether it protects you.",
      "左欄是報告由櫃位到洗錢報告主任作出決定的路徑；右邊每個方格附屬於同一行的步驟，虛線上的字說明兩者的關係。顏色顯示那是誰的責任，以及是否為你提供保障。")
    + fig(fig_internal, ("Reporting lines should be as short as possible, with the fewest people between the staff member with the suspicion and the MLRO: that keeps the report fast, confidential and accessible to the MLRO (¶7.13).",
                         "報告流程應盡可能縮短，令發現可疑交易的職員與洗錢報告主任之間涉及的人數越少越好，從而確保報告迅速、保密及無障礙地送交洗錢報告主任（第7.13段）。"), INTERNAL_KEY)
    + h3("The system you should have for reporting", "你應具備的舉報制度")
    + table([th("Part of the system", "制度的組成部分"), th("What it involves", "內容")], [
        tr(rh("An MLRO", "洗錢報告主任", "¶7.7(a)"),
           td("Appointed as the central reference point for reporting suspicious transactions and the main point of contact with the JFIU and law enforcement agencies, playing an active role in identifying and reporting them. The MLRO's principal functions should include oversight of: reviewing internal disclosures and exception reports and deciding, on all available relevant information, whether a report to the JFIU is necessary; keeping all records of those internal reviews; and guidance on how to avoid tipping off. Chapter 3 of the Guideline covers the appointment",
              "獲委任為報告可疑交易的中央聯絡點，並作為與財富情報組及執法機構的主要聯絡點，在識別及報告可疑交易方面擔當積極的角色。洗錢報告主任的主要職能應包括監督：覆核所有內部披露及例外情況報告，並根據一切知悉的資料，決定是否有需要向財富情報組作出報告；備存該等內部覆核的所有紀錄；以及提供有關如何避免通風報訊的導引。委任事宜載於指引第3章", "¶7.9")),
        tr(rh("Clear policies and procedures", "清晰的政策和程序", "¶7.7(b)"),
           td("Over four things: internal reporting; reporting to the JFIU; post-reporting risk mitigation; and prevention of tipping off. You should establish and maintain them to ensure that every member of staff knows who the MLRO is and how to make an internal report, and that all internal reports must reach the MLRO without undue delay",
              "涵蓋四方面：內部報告；向財富情報組作出報告；作出報告後如何減低風險；及防止通風報訊。你應設立及維持有關政策和程序，以確保全體職員均知悉洗錢報告主任的身分及作出內部報告的程序，以及所有內部報告必須送達洗錢報告主任，不得無故延誤", cc("¶7.7(b)", "¶7.12"))),
        tr(rh("Proper records", "妥善紀錄", "¶7.7(c)"),
           td("Of internal reports and of STRs: the two registers are compared in <a href=\"#after\">After the report</a>", "內部報告及可疑交易報告的紀錄：兩個紀錄冊的比較見<a href=\"#after\">提交報告後</a>", "¶7.29–7.30")),
        tr(rh("Checking it works", "查核制度是否有效", "¶7.8"),
           td("Measures to check, on an ongoing basis, that the system complies with legal and regulatory requirements and operates effectively. Their type and extent should suit the ML/TF risk and the nature and size of your business",
              "制訂措施，持續查核有關制度符合法律及監管規定並且行之有效。措施的類別及程度，應與洗錢／恐怖分子資金籌集風險及業務的性質和規模配合")),
    ], minw=760)
    + traps(
        trap(("Frontline shortlisting is the planted wrong answer", "前線人員篩選報告是刻意設下的錯誤答案"),
             ("The official sample paper lists four items for an MSO's reporting system and plants “shortlisting internal reports by the frontline staff before reporting to the MLRO” among them. The Guideline's three parts are the MLRO, clear policies and procedures, and proper records. Nothing lets reports be screened before they reach the MLRO: every internal report must reach the MLRO without undue delay, and supervisors or managers without a reporting or compliance role may never filter them out.",
              "官方參考試題就經營者的舉報制度列出四項，其中刻意加入「向洗錢報告主任報告前，先由前線人員篩選內部報告」。指引所列的三個組成部分是洗錢報告主任、清晰的政策和程序，以及妥善紀錄。指引不容許在報告送達洗錢報告主任前先行篩選：所有內部報告必須不得無故延誤地送達洗錢報告主任，而非負責洗錢報告／合規職能的主管或經理在任何情況下均不得過濾報告。"),
             cc("¶7.7", "¶7.12(b)", "¶7.13", SAMPLE5)),
        trap(("The staff member's duty ends at the MLRO; the MLRO's begins", "職員的責任止於洗錢報告主任，洗錢報告主任的責任由此開始"), None, cc("¶7.14", "¶7.19", DO("25A(4)"), UN("12(4)")),
             vs=[(("The staff member", "職員"), ("Reporting to the MLRO under the MSO's procedures fully satisfies the statutory obligation. There is no personal duty to go to the JFIU as well.", "按經營者的程序向洗錢報告主任報告，即已完全履行法定責任，無需另行向財富情報組報告。")),
                 (("The MLRO", "洗錢報告主任"), ("Evaluates the report and, if there are grounds for knowledge or suspicion, discloses to the JFIU as soon as reasonable after the evaluation is complete.", "評估報告；如有知悉或懷疑的理由，須在評估完成後在合理範圍內盡快向財富情報組披露。"))]),
    ))

# ---------------------------------------------------------------- D. filing with the JFIU
D_ = sec('jfiu', [("Guideline Ch. 7", "指引第7章"), ("¶7.5 · ¶7.12 · ¶7.18–7.23", "第7.5、7.12、7.18至7.23段"), ("fn 59 · fn 65", "註59 · 註65")],
         ("The MLRO files: what the report must say, and when", "洗錢報告主任提交報告：須說明甚麼，何時提交"),
    P("Each row is a situation the MLRO may face when filing, and what the Guideline expects in it. The table after it sets out every time limit in the chain from the counter to the JFIU.",
      "每一行是洗錢報告主任提交報告時可能遇到的情況，以及指引對該情況的期望。其後的表列出由櫃位至財富情報組整條鏈上的每個時限。")
    + table([th("The situation", "情況"), th("What the Guideline expects", "指引的期望")], [
        tr(td("The suspicion arises before the transaction", "懷疑在交易前出現", "¶7.19"),
           td("The STR may be made before the transaction or activity occurs, whether or not the intended transaction ultimately takes place", "可在可疑交易或活動發生前提交報告，而不論該擬作交易最終有否成事", "¶7.19")),
        tr(td("It only looks suspicious once completed", "交易完成後才看似可疑", "¶7.19"),
           td("The STR is made after the transaction or activity has been completed", "在交易或活動完成後才作披露", "¶7.19")),
        tr(td("It is urgent: the customer has told you to move funds or other property, close the account, make cash available for collection, or make significant changes to the relationship", "情況緊急：客戶已指示你移動資金或其他財產、結束戶口、安排現金備取，或對業務關係作出重大變動", "¶7.21"),
           td("Say so in the STR, particularly when the account is part of an ongoing law enforcement investigation", "在可疑交易報告中述明，特別是當有關戶口是執法機構正在進行調查的一部分", "¶7.21")),
        tr(td("Urgent, and the circumstances are exceptional", "情況緊急而且特殊", "¶7.21"),
           td("Consider an initial notification to the JFIU by telephone", "應考慮初步以電話通知財富情報組", "¶7.21", post=flag())),
        tr(td("You intend to end the relationship", "你有意終止業務關係", "¶7.22"),
           td("Recommended: say so in your initial STR", "建議在初次提交的可疑交易報告中表明", "¶7.22")),
        tr(td("You control both the ordering and the beneficiary sides of a suspicious wire transfer", "你同時控制可疑電傳轉帳的匯款方和收款方", "¶7.19"),
           td("Also file an STR in any jurisdiction affected by it, and make the relevant transaction information available to the Financial Intelligence Unit",
              "應在受可疑電傳轉帳影響的司法管轄區提交可疑交易報告，並向財富情報組提供相關交易資料", "¶7.19")),
        tr(td("You hold information on both the originator and the recipient", "你同時掌握匯款人和收款人的資料", "fn 59"),
           td("Take all of it into account in deciding whether an STR has to be filed", "應考慮所有有關資料，以決定是否提交可疑交易報告", cc("fn 59", CIR26))),
    ], minw=760)
    + h3("Every clock in the chain, from the counter to the JFIU", "由櫃位至財富情報組：鏈上的每個時限")
    + numreq([
        (("Without undue delay", "不得無故延誤"),
         ("Every internal report reaches the MLRO", "所有內部報告送達洗錢報告主任"),
         ("From the staff member, through the shortest reporting line", "由職員經最短的報告流程送交"),
         ("Your procedures fall short of what the Guideline requires; the legal duty is to report as soon as reasonable, which is why reporting lines are kept short", "你的程序未達指引的要求；法律責任是在合理範圍內盡快報告，因此報告流程應盡量縮短"),
         "¶7.12(b) · ¶7.13"),
        (("As soon as reasonably practical", "在切實可行範圍內盡快"),
         ("The STR is made", "提交可疑交易報告"),
         ("Counted from when the suspicion was first identified", "由最初識辨有關懷疑時起計"),
         ("A departure from the Guideline's standard. Separately, under the statute, failing to disclose as soon as it is reasonable is the offence of failing to report (up to 3 months and $50,000)", "未符合指引的標準；另外，根據法例，未能在合理範圍內盡快作出披露屬沒有舉報的罪行（最高監禁3個月及罰款50,000元）"),
         cc("¶7.5(b)", "¶1.24")),
        (("As soon as reasonable after the evaluation", "評估完成後在合理範圍內盡快"),
         ("The MLRO discloses to the JFIU, with the information the suspicion rests on", "洗錢報告主任向財富情報組披露，連同懷疑所根據的資料"),
         ("Once the MLRO's review of the internal report is complete and there are grounds for knowledge or suspicion", "洗錢報告主任完成覆核內部報告，並判定有知悉或懷疑的理由"),
         ("The same offence applies to a late report; any further searching of connected accounts should be balanced against reporting in time, and the review and its conclusions documented", "延遲報告同樣涉及該罪行；進一步搜尋有關連戶口，應與及時報告的要求取得平衡，並記錄覆核過程及結論"),
         cc("¶7.19", "¶7.18")),
        (("As soon as reasonable, on your own initiative", "主動及在合理範圍內盡快"),
         ("The STR, when you have already done the acts it discloses", "你已作出所披露的作為後提交的報告"),
         ("After the transaction", "在交易之後"),
         ("Outside this condition, the after-the-event defence in ¶7.25(b) does not cover you", "不符合此條件，便不能以第7.25(b)段的事後免責辯護保障自己"),
         "¶7.25(b)"),
    ], heading=False)
    + P("You should ensure the STRs you file with the JFIU are of high quality, taking into account the feedback and guidance provided by the JFIU in its quarterly report and by the Commissioner from time to time. "
        + cite_html(cc("¶7.23", "fn 65")),
        "你應留意由財富情報組在季度報告及關長不時提供的反饋意見及導引，以確保向財富情報組提交的可疑交易報告屬高水平。"
        + cite_html(cc("¶7.23", "fn 65")))
    + traps(
        trap(("Urgent is said in the report; only the exceptional gets a phone call", "緊急情況在報告中述明；特殊情況才考慮致電"), None, "¶7.21",
             vs=[(("Urgent", "緊急"), ("Indicate the urgency in the STR itself, for instance a customer's instruction to move funds, close the account or have cash ready for collection.", "在可疑交易報告中述明情況緊急，例如客戶指示移動資金、結束戶口或安排現金備取。")),
                 (("Exceptional as well as urgent", "緊急而且特殊"), ("An initial telephone notification to the JFIU should be considered.", "應考慮初步以電話通知財富情報組。"))]),
        trap(("Ending the relationship: recommended, and said up front", "終止業務關係：屬建議，並應一開始說明"),
             ("Stating an intention to terminate is recommended, not required, and the place for it is the initial STR, not a later follow-up.",
              "表明終止業務關係的意向屬建議而非規定，而且應在初次提交的報告中表明，而非其後補充。"),
             "¶7.22"),
    ))

# ---------------------------------------------------------------- E. after the report
REG_TBL = table([th("The register records", "紀錄冊記錄"), th("Register of internal reports, to the MLRO", "內部報告紀錄冊（向洗錢報告主任作出的報告）"),
                 th("Register of STRs, to the JFIU", "可疑交易報告紀錄冊（向財富情報組提交的報告）")], [
    tr(rh("Covers", "涵蓋"), td("All ML/TF reports made to the MLRO", "向洗錢報告主任作出的所有洗錢／恐怖分子資金籌集報告", "¶7.29"),
       td("All STRs made to the JFIU", "向財富情報組提交的所有可疑交易報告", "¶7.30")),
    tr(rh("The date", "日期"), td("The date the report was made", "作出報告日期", "¶7.29"), td("The date of the STR", "提交可疑交易報告日期", "¶7.30")),
    tr(rh("A person", "人員"), td("The staff members who subsequently handled the report", "其後處理報告的人員", "¶7.29"),
       td("The person who made the STR", "提交可疑交易報告的人", "¶7.30", post=flag())),
    tr(rh("The outcome", "結果"), td("The results of the assessment, and whether the report led to an STR", "評估結果，以及內部報告有否導致須提交可疑交易報告", "¶7.29"),
       td("Not listed", "沒有列出", "¶7.30", post=flag())),
    tr(rh("The papers", "文件"), td("Information to locate the papers relevant to the report", "報告的相關文件存放何處", "¶7.29"),
       td("Information to locate the papers relevant to the STR", "可疑交易報告的相關文件存放何處", "¶7.30")),
    tr(rh("Combining them", "合併處理"), '<td colspan="2">' + B("The STR register may be combined with the register of internal reports, if considered appropriate. Both are a <b>must</b>: establish and maintain.",
                                                            "如認為恰當，可疑交易報告紀錄冊可與內部報告紀錄冊合併處理。兩者均屬<b>必須</b>建立及保存。") + cite_html("¶7.29–7.30") + '</td>'),
], minw=760, cls='cmp')

E_ = sec('after', [("Guideline Ch. 7", "指引第7章"), ("¶7.24–7.30", "第7.24至7.30段")],
         ("The report is in: consent, the defence, and a relationship you should review", "報告已提交：同意、免責辯護，以及應覆核的業務關係"),
    P("Read the figure from the top. The decision box is the JFIU's; every red box is yours, including the “yes” branch, and the review at the foot applies whichever way the decision goes. The green column on the right is the defence the filing gives you.",
      "由上而下閱讀。決策方格屬財富情報組的考慮；每個紅色方格都是你的責任，包括「是」的分支，而底部的覆核不論決定如何都適用。右邊的綠色方格是提交報告為你帶來的免責辯護。")
    + fig(fig_after, ("Acknowledgement and consent come under section 25A of DTROP and OSCO and section 12 of UNATMO (¶7.24). The defence is under DTROP and OSCO s.25A(2) and UNATMO s.12(2) (¶7.25).",
                      "確認收到報告及給予同意，是根據《販毒（追討得益）條例》及《有組織及嚴重罪行條例》第25A條，以及《聯合國（反恐怖主義措施）條例》第12條（第7.24段）。免責辯護見《販毒（追討得益）條例》及《有組織及嚴重罪行條例》第25A(2)條，以及《聯合國（反恐怖主義措施）條例》第12(2)條（第7.25段）。"), AFTER_KEY)
    + traps(
        trap(("Consent belongs to one door only", "「同意」只屬其中一道門"),
             ("Only a report made before the acts relies on the JFIU's consent. A report made after the acts has no consent condition; instead it must be made on your own initiative and as soon as it is reasonable. Either way the defence is for the acts disclosed in the report.",
              "只有在作為之前作出的報告，才以財富情報組的同意為條件。在作為之後作出的報告沒有「同意」這項條件，但必須由你主動及在合理範圍內盡快作出。不論哪一種，免責辯護都是就報告中所披露的作為而言。"),
             cc("¶7.25", DO("25A(2)"), UN("12(2)"))),
        trap(("Consent is not a clean bill of health", "「同意」不等於「健康證明」"),
             ("The defence does not absolve you from the legal, reputational or regulatory risks of keeping the account running. A “consent” reply to a pre-transaction report does not mean the account is fine to continue, or that it poses no risk to you.",
              "法定免責辯護不會免除你因帳戶持續運作而涉及的法律、聲譽或監管風險。財富情報組就交易前的報告作出「同意」的回應，不應被解釋為該戶口持續運作的「健康證明」，或顯示該帳戶不會令你涉及風險。"),
             "¶7.26"),
        trap(("Review the relationship whatever the JFIU says", "不論財富情報組怎樣回應，都要覆核業務關係"),
             ("The review follows the filing itself, irrespective of any later feedback from the JFIU. Filing and carrying on without further consideration of the risks is not acceptable. You should conduct the review upon the filing of the STR.",
              "覆核源於提交報告本身，不論財富情報組其後有否給予反饋。提交報告後繼續運作而不再進一步考慮風險，是不可接受的。提交報告後應立即覆核。"),
             "¶7.27"),
    )
    + h3("Two registers you must keep", "必須保存的兩個紀錄冊")
    + REG_TBL)

# ---------------------------------------------------------------- F. court documents
F_ = sec('lea', [("Guideline Ch. 7", "指引第7章"), ("¶7.31–7.35", "第7.31至7.35段"), ("¶7.9", "第7.9段")],
         ("Law enforcement serves a court order, or asks about a customer", "執法機構送達法庭文件，或查詢某客戶"),
    P("The three columns follow a case from investigation to the court's final orders: the top box is the document, the box beneath it is what it asks of you. The band at the top is what you set up before anything arrives; the band at the foot applies whatever arrives.",
      "三欄按案件由調查至法院最終命令的次序排列：上方格是文件，下方格是它對你的要求。頂部橫額是收到任何文件前須做好的準備；底部橫額不論收到甚麼都適用。")
    + fig(fig_lea, ("These court documents help law enforcement agencies investigate, and restrain and confiscate illicit proceeds (¶7.31). For the restraint order, the Guideline's margin cites DTROP s.10–11, OSCO s.15–16 and UNATMO s.6 (¶7.33). Elsewhere the Guideline says UNATMO s.6 empowers the Secretary for Security to freeze suspected terrorist property (¶6.5(a)): see <a href=\"#g6-regimes\">Three laws</a>.",
                    "這類法庭文件對於協助執法機構進行調查，以至限制及沒收非法得益，至為重要（第7.31段）。就限制令，指引在旁註引述《販毒（追討得益）條例》第10及11條、《有組織及嚴重罪行條例》第15及16條及《聯合國（反恐怖主義措施）條例》第6條（第7.33段）。指引另指出，《聯合國（反恐怖主義措施）條例》第6條授權保安局局長凍結懷疑是恐怖分子的財產（第6.5(a)段）：見<a href=\"#g6-regimes\">三條法例</a>。"), LEA_KEY)
    + traps(
        trap(("Confiscation and forfeiture are different orders", "沒收與充公是不同的命令"), None, "¶7.34",
             vs=[(("Confiscation", "沒收"), ("Follows the conviction of a defendant and takes his criminal proceeds, under DTROP s.3 or OSCO s.8. You may be served with the order if you hold funds or other property of his that the court deems to represent his benefit from the crime.",
                                            "在被告定罪後沒收其犯罪所得，根據《販毒（追討得益）條例》第3條或《有組織及嚴重罪行條例》第8條。如你持有屬於該被告、法院認為代表其犯罪得益的資金或其他財產，便可能收到沒收令。")),
                 (("Forfeiture", "充公"), ("Ordered where the court is satisfied that the property is terrorist property, under UNATMO s.13.",
                                        "法院如信納某些財產屬恐怖分子財產，可下令充公，根據《聯合國（反恐怖主義措施）條例》第13條。"))]),
        trap(("Two contact points for law enforcement", "與執法機構的兩個聯絡點"), None, cc("¶7.9", "¶7.31"),
             vs=[(("The MLRO", "洗錢報告主任"), ("The main point of contact with the JFIU and law enforcement agencies, as the central reference point for suspicious transaction reporting.", "作為報告可疑交易的中央聯絡點，亦是與財富情報組及執法機構的主要聯絡點。")),
                 (("For court documents", "處理法庭文件"), ("Your procedures should appoint a staff member as the main point of contact with law enforcement agencies. ¶7.31 does not say who; ¶7.9 already gives the MLRO the role of main point of contact with law enforcement, and the Guideline does not say whether these must be the same person.",
                                                        "你的程序應委任一名人員作為與執法機構的中央聯絡點。第7.31段沒有指明由誰擔任；第7.9段已訂明洗錢報告主任是與執法機構的主要聯絡點，指引沒有說明兩者是否須為同一人。"))]),
    ))

G7_NAV = [('duty', 'The duty to report', '舉報責任'), ('spot', 'Spotting suspicion', '識辨可疑交易'),
          ('internal', 'Staff to the MLRO', '由職員至洗錢報告主任'), ('jfiu', 'Filing with the JFIU', '向財富情報組舉報'),
          ('after', 'After the report', '提交報告後'), ('lea', 'Court orders', '法庭文件')]
G7_BODY = A_ + B_ + C_ + D_ + E_ + F_
G7_META = dict(
    tab=("7", "7"),
    short=("Guideline Ch. 7 · STR", "指引第7章 · 可疑交易報告"),
    eyebrow=("AML/CFT Guideline · Chapter 7 · Modules 1, 6 and 7", "《打擊洗錢指引》第7章 · 單元一、六及七"),
    title=("Suspicious Transaction Reports", "可疑交易報告"),
    lede=("Chapter 7 decides what happens between a doubt at your counter and a report on the JFIU's desk: who must speak, to whom, how fast, and what they must not say. It also sets what you owe after the report is in, and when law enforcement comes to you with a court order.",
          "第7章決定由櫃位上的一個疑問，到財富情報組收到報告之間發生甚麼：誰須舉報、向誰舉報、要多快，以及不可說甚麼。本章亦訂明報告提交後你須承擔的責任，以及執法機構帶同法庭文件前來時你須怎樣做。"),
    foot=("Drawn from Chapter 7 of the Customs and Excise Department's Guideline on Anti-Money Laundering and Counter-Financing of Terrorism (For Money Service Operators), June 2023, with paragraphs 1.22 to 1.25 and 5.10 to 5.14, the C&amp;ED circulars of 13 December 2021 and 20 January 2026, and sample question 5 of 12 May 2021.",
          "取材自香港海關《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》（2023年6月）第7章，另參考第1.22至1.25段及第5.10至5.14段、海關2021年12月13日及2026年1月20日的通函，以及2021年5月12日的參考試題5。"),
)
