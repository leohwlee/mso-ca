# The C&ED circulars to MSOs that are still current, and the C&ED's FAQ for all MSOs.
# Only what they add to the AMLO and the AML/CFT Guideline is kept. Circulars whose
# content a later official document now covers are not sources.
from ui import *
from bl_core import _runs
from gl_fig import LG
from ci_fig import (CI, TP, TPF, TB, cc_ as cc, fig_tpp, TPP_KEY, fig_tbml, TBML_KEY, fig_pr, PR_KEY)


def FAQ(q, par=None):
    en, tc = f"FAQ Q{q}", f"常見問題第{q}問"
    if par:
        en, tc = en + f" · ¶{par}", tc + f" · 第{_runs(par)}段"
    return (en, tc)


def dcell(en, tc):
    return f'<td class="numreq"><span class="answer" tabindex="0">{B(en, tc)}</span></td>'


def dash_td():
    return '<td class="faint">—</td>'


# Superseded by Guideline Chapter 7, but five of its filing points appear in no current document.


# ---------------------------------------------------------------- A. dates
def drow(d, what, who, cite, post=''):
    return '<tr>' + dcell(*d) + td(what[0], what[1], cite, post=post) + td(*who) + '</tr>'


A = sec('dates', [("C&ED circulars", "海關通函"), ("2018 to 2026", "2018至2026年")],
        ("What took effect, and when", "何時生效，生效了甚麼"),
    P("The left column is the day a rule began to apply, or a statement was issued, not the date of the circular that announced it; the source is cited under each row. The last row is a date still ahead. Rows with more to say link to their section.",
      "左欄是規則開始適用或聲明發出的日期，而非公布該規則的通函日期；每行下方註明出處。最後一行是尚未到來的日期。有更多內容的行設有連結，可跳至相關小節。")
    + table([th("From", "生效日期"), th("What took effect", "生效內容"), th("Who it reaches", "適用對象")], [
        drow(("16 Jul 2018", "2018年7月16日"),
             ("The Cross-boundary Movement of Physical Currency and Bearer Negotiable Instruments Ordinance (Cap. 629): currency or bearer negotiable instruments worth more than HK$120,000 must be declared at the boundary. <a href=\"#laws\">How</a>",
              "《實體貨幣及不記名可轉讓票據跨境流動條例》（第629章）：總值超過港幣120,000元的貨幣或不記名可轉讓票據須在跨境時申報。<a href=\"#laws\">申報方式</a>"),
             ("Anyone crossing the boundary, your staff and couriers included", "所有跨境人士，包括你的員工及運送人員"), CI("31 Jul 2018")),
        drow(("23 Jun 2025", "2025年6月23日"),
             ("An optional e-form for travellers carrying currency and bearer negotiable instruments worth more than HK$120,000: they may pre-fill it before arriving or leaving, get a QR code, and show it to a Customs officer to declare. <a href=\"#laws\">Crossing the boundary</a>",
              "旅客如攜帶總值高於12萬港元的貨幣及不記名可轉讓票據，可在抵達或離開香港前使用電子表格預先填寫資料，獲取二維碼，再向海關人員出示以完成申報。<a href=\"#laws\">跨境申報</a>"),
             ("Any MSO that moves currency across the boundary through a passenger channel", "經旅客通道跨境運送現金類物品的金錢服務經營者"), CI("23 Jun 2025")),
        drow(("30 Jun 2025", "2025年6月30日"),
             ("Periodic returns move from quarterly, counted from the licence's start date, to half-yearly by the calendar, lodged online only. <a href=\"#returns\">Periodic returns</a>",
              "定期申報表由按牌照生效日期起計的每季遞交，改為按曆年每半年遞交，並只接受網上遞交。<a href=\"#returns\">定期申報表</a>"),
             ("Every licensee", "所有持牌人"), CI("30 May 2025")),
        drow(("1 Jul 2025", "2025年7月1日"),
             ("The first half-yearly return, covering 1 January to 30 June 2025, is lodged from this day", "首份半年度申報表（涵蓋2025年1月1日至6月30日）由此日起遞交"),
             ("Every licensee", "所有持牌人"), CI("30 May 2025")),
        drow(("24 Aug 2025", "2025年8月24日"),
             ("Amendments to the Money Changers Ordinance (Cap. 34): the transaction notes and display of rates required by its Schedules 2 and 3",
              "《貨幣兌換商條例》（第34章）的修訂：該條例附表2及3有關交易單據及展示匯率的規定"),
             ("MSOs that change money", "經營貨幣兌換服務的金錢服務經營者"), CI("17 Nov 2025")),
        drow(("15 May 2026", "2026年5月15日"),
             ("New licence fees: Schedule 3 to the Ordinance as amended by L.N. 22 of 2026. The Licensing Guide fee schedule lists the same figures. <a href=\"#s3-fees\">The fee table</a>",
              "新牌照費用生效：經2026年第22號法律公告修訂的條例附表3。《牌照指引》的收費表列出相同的數字。<a href=\"#s3-fees\">費用表</a>"),
             ("Every applicant and licensee", "所有申請人及持牌人"), cc(("Sch. 3", "附表3"), ("Licensing Guide fee schedule", "《牌照指引》收費表"))),
        drow(("19 Jun 2026", "2026年6月19日"),
             ("The FATF's Call for Action statement of 19 June 2026, with countermeasures called for on the DPRK and Iran and EDD proportionate to the risk for Myanmar; and its updated statement on increased monitoring, which the circular does not date, adding Bosnia and Herzegovina and Iraq. The FATF also published the outcomes of its plenary of 17 to 19 June 2026. <a href=\"#edd\">The two lists</a>",
              "特別組織於2026年6月19日發出的呼籲採取行動聲明，要求對朝鮮民主主義人民共和國及伊朗採取針對措施，對緬甸採取與風險相稱的更嚴格的盡職審查措施；以及其有關被加強監察的司法管轄區的最新聲明（通函未註明其日期），把波斯尼亞和黑塞哥維那及伊拉克加入名單。特別組織亦發表了其2026年6月17至19日全體會議的成果。<a href=\"#edd\">兩份名單</a>"),
             ("Every MSO with customers or transactions connected to these jurisdictions", "客戶或交易與這些司法管轄區有關連的金錢服務經營者"), CI("3 Jul 2026")),
        drow(("End of 2030", "2030年底"),
             ("All jurisdictions are expected to be ready to implement the FATF's revised Recommendation 16 on payment transparency, agreed in June 2025, by the end of 2030. The FATF consulted on guidance for it until 21 August 2026. <a href=\"#edd\">What it changes</a>",
              "所有司法區預計需於2030年底前實施特別組織於2025年6月通過的第16項建議修訂（支付透明度）。特別組織就相關指引的諮詢於2026年8月21日截止。<a href=\"#edd\">修訂內容</a>"),
             ("Every MSO; the FATF invited feedback from industry", "所有金錢服務經營者；特別組織邀請業界提出意見"), CI("16 Jul 2026")),
    ], minw=820)
    + traps(
        trap(("A circular's date is rarely the start date", "通函日期往往不是生效日期"),
             ("Cap. 629 began on 16 July 2018; its circular is dated 31 July. The Money Changers Ordinance amendments began on 24 August 2025; the circular came on 17 November. The FATF issued its Call for Action statement on 19 June 2026; the circular passing it on is dated 3 July. Learn the start date, not the letterhead.",
              "第629章於2018年7月16日實施，相關通函卻於7月31日發出。《貨幣兌換商條例》的修訂於2025年8月24日生效，通函於11月17日才發出。特別組織於2026年6月19日發出呼籲採取行動的聲明，轉達聲明的通函則於7月3日發出。要記的是生效日期，而非通函日期。"),
             cc(CI("31 Jul 2018"), CI("17 Nov 2025"), CI("3 Jul 2026"))),
    ))

# ---------------------------------------------------------------- B. three warnings
B_ = sec('warnings', [("Circulars", "通函"), ("13 Dec 2021", "2021年12月13日"), ("17 Sep 2024", "2024年9月17日"), ("24 Apr 2025", "2025年4月24日"), ("20 Jan 2026", "2026年1月20日")],
         ("Risk warnings the C&amp;ED has sent", "海關發出的風險警示"),
    P("Each column is a warning the C&amp;ED sent after something went wrong in the market. Read down a column for the threat and what is expected of you; the next two sections take the second and third further.",
      "每一欄是海關在市場出現問題後發出的一項警示。沿欄向下閱讀，可見威脅所在及對你的期望；其後兩節進一步說明第二及第三項。")
    + table([th("", ""), th("Delivery channels, 13 Dec 2021", "交付渠道（2021年12月13日）"),
             th("Third-party payments, 17 Sep 2024", "第三方支付（2024年9月17日）"), th("Trade-based laundering, 20 Jan 2026", "以貿易進行洗錢（2026年1月20日）")], [
        tr(rh("What prompted it", "起因"),
           td("Cross-border remittances left unfulfilled because customers' funds were frozen by regulators or law enforcement in other jurisdictions", "客戶資金遭其他司法管轄區的監管或執法機構凍結，以致跨境匯款未能完成"),
           td("A Mainland press briefing on Macao's money exchange gangs and cross-boundary money exchange syndicates", "內地公安部就澳門「換錢黨」及跨境貨幣兌換集團舉行的新聞發布會"),
           td("Syndicates using falsified trade documents, such as fake contracts and invoices, to create bogus transaction records", "犯罪集團使用偽造的貿易文件（例如假合同及發票）製造虛假交易紀錄")),
        tr(rh("How it reaches you", "如何牽涉你"),
           td("Through the customers, business partners and counterparties that make up your delivery channel for remittances", "經由構成你匯款交付渠道的客戶、業務夥伴及交易對手"),
           td("Cross-boundary remittance, particularly inward remittance initiated by transient customers, as a conduit for crime proceeds; and payments from someone other than the customer, used to hide the beneficial owner or the source of illicit funds", "跨境匯款服務（尤其是短期客戶要求進行的匯入服務）可被利用作犯罪得益的轉帳管道；以及來自客戶以外人士的第三方支付，藉以掩飾實益擁有人的身分或非法資金的來源"),
           td("Cross-boundary remittance as one of the conduits for trade-based proceeds, where shell companies may be the originator or the recipient", "以跨境匯款作為轉移貿易犯罪得益的其中一種渠道，匯款人或收款人可能是空殼公司")),
        tr(rh("What is expected", "對你的期望"),
           td("A comprehensive risk assessment before you bring any party into your business model, and regular reviews of the channels against the rules of the places they touch", "在任何一方加入你的業務模式前進行全面風險評估，並定期按所涉司法管轄區的最新規定覆核有關渠道"),
           td("Serious thought to refusing them; if you do accept, a written policy, due diligence, senior management approval and closer monitoring. <a href=\"#thirdparty\">The decision</a>", "認真考慮拒絕接受；如接受，應有書面政策、盡職審查、高級管理層批准及加強監察。<a href=\"#thirdparty\">決策流程</a>"),
           td("Flag and escalate customers with several risk indicators; EDD for high risk, and source of funds and wealth to consider; anti-fraud checks to consider; no alert closed without sufficient justification and analysis; an STR whatever the amount, attempts included; a gap analysis of your controls. <a href=\"#tbml\">The chain</a>", "為出現多項風險指標的客戶作標記並上報；對高風險客戶施加更嚴格的盡職審查要求，並考慮索取資金及財富來源資料；考慮採取反欺詐程序；不可在沒有充分理由及分析下消除警報；不論金額、包括試圖進行的交易，均須提交可疑交易報告；就管控措施進行差距分析。<a href=\"#tbml\">洗錢鏈條</a>")),
        tr(rh("The duties it points to", "所援引的責任"),
           td("Procedures for each kind of customer, relationship, product and transaction (s.19(3) Sch. 2); EDD for high-risk customers or transactions; and, where you know or suspect that property in a transaction or relationship you have or have had represents the proceeds of drug trafficking or an indictable offence, or is terrorist property, an STR to the JFIU as soon as reasonably practicable",
              "就每類客戶、業務關係、產品及交易設立的有效措施（附表2第19(3)條）；遇高風險客戶或交易時採取更嚴格的盡職審查措施；以及如知道或懷疑現時或過往牽涉任何財產的交易或關係，而該財產代表販毒或可公訴罪行的得益，或是恐怖分子財產，須在切實可行範圍內盡快向聯合財富情報組提交可疑交易報告", CI("13 Dec 2021")),
           td("Ongoing monitoring and unusual transactions; all reasonable measures to prevent contraventions; enhanced measures, and enquiries where an individual customer seems not to act for himself", "持續監察及不尋常交易；採取一切合理措施防止違反規定；更嚴格措施，以及在個人客戶看似並非代表本身行事時作出查詢", "s.5(1)(b)–(c), 23 Sch. 2 · ¶3.2, 4.4.5"),
           td("The CDD, monitoring and reporting duties in the Ordinance and the Guideline, read with the FATF's trade-based risk indicators", "條例及指引的盡職審查、監察及舉報責任，並參考特別組織的貿易洗錢風險指標")),
    ], note=B("The delivery-channel warning reiterates the importance of your institutional risk assessment, particularly on delivery channel risks outside Hong Kong. Under the Guideline you should conduct that assessment to identify, assess and understand your ML/TF risks in relation to your customers, the countries or jurisdictions your customers are from or in, the countries or jurisdictions you have operations in, and your products, services, transactions and delivery channels; the appropriate steps should include documenting the process, considering all the relevant risk factors, obtaining senior management approval of the results, having a process to keep it up to date, and having appropriate mechanisms to provide it to the Commissioner when required. The detail is on the <a href=\"#g2-ira\">Guideline Chapter 2 page</a>.",
              "交付渠道警示再次強調機構層面風險評估至為重要，尤其是評估在香港以外的交付渠道風險。根據指引，你應進行機構層面的風險評估，以識別、評估和了解與你的客戶、客戶所屬或所在的國家或司法管轄區、你業務所在的國家或司法管轄區，以及你的產品、服務、交易及交付渠道有關的洗錢／恐怖分子資金籌集風險；適當步驟應包括記錄風險評估程序、事先考慮所有相關風險因素、由高級管理層審批風險評估結果、設有程序確保風險評估反映現況，以及設有適當機制應關長要求提供風險評估結果。詳情見<a href=\"#g2-ira\">指引第2章一頁</a>。") + ' ' + cite_html(cc(CI("13 Dec 2021"), "¶2.2–2.3")), minw=900, cls='cmp')
    + traps(
        trap(("Conduct abroad counts if it would be indictable in Hong Kong, whatever the local law", "在香港以外發生的行為，若在香港發生即屬可公訴罪行，便受涵蓋，不論當地法律如何"),
             ("The reporting duty covers property that represents the proceeds of an indictable offence. Under the Organized and Serious Crimes Ordinance that includes conduct outside Hong Kong which would be indictable had it happened here, whatever the law is where it happened.",
              "舉報責任涵蓋代表可公訴罪行得益的財產。根據《有組織及嚴重罪行條例》，可公訴罪行包括在香港以外發生、但假若在香港發生即屬可公訴罪行的行為，不論當地法律如何規定。"),
             cc(CI("13 Dec 2021"), ("OSCO s.25(4)", "《有組織及嚴重罪行條例》第25(4)條"))),
    )
    + h3("Another warning: fake websites and social media posing as MSOs", "另一項警示：仿冒金錢服務經營者的欺詐網站及社交媒體")
    + P("The C&amp;ED has seen more fraudulent websites and bogus social media advertisements that take on an MSO's identity to run illegal money services or frauds. Each row is a stage; the right column keeps the circular's own strength of wording.",
        "海關察悉，越來越多欺詐網站和偽造社交媒體平台廣告仿冒金錢服務經營者，以經營非法金錢服務業務或進行欺詐。每一行是一個階段；右欄保留通函原有的語氣強弱。")
    + table([th("When", "何時"), th("What the circular says", "通函內容")], [
        tr(rh("Before anything happens", "未發生事故時"),
           td("You are reminded to take appropriate security measures to protect personal data, and to stay vigilant about any website or social media platform getting hold of your business information without your permission",
              "金錢服務經營者應採取適當的保安措施以保護個人資料，並對未經其批准取得其業務資料的任何網站及社交媒體平台保持警覺", post=flag())),
        tr(rh("You find a suspected fake site using your business identity", "發現與你業務身分有關的疑似欺詐網站"),
           td("You are recommended to notify the public, and to report the case to the C&amp;ED and to the Hong Kong Police Force",
              "建議向公眾發出通知，並向海關及香港警務處報案")),
    ], note=cite_html(CI("24 Apr 2025")), minw=640)
    + traps(
        trap(("Reminded to protect; recommended to report", "「應」保護資料；「建議」報案"), None, CI("24 Apr 2025"),
             vs=[(("Reminded", "應採取"), ("Security measures for personal data, and vigilance about sites using your business information without permission.", "以適當的保安措施保護個人資料，並對未經批准取得業務資料的網站保持警覺。")),
                 (("Recommended", "建議"), ("Telling the public, and reporting to the C&amp;ED and the Police, once you find a suspected fake site in your name.", "發現與自己業務身分有關的疑似欺詐網站時，向公眾發出通知，並向海關及警方報案。"))])))

# ---------------------------------------------------------------- C. third-party payments
C_ = sec('thirdparty', [("Circular", "通函"), ("17 Sep 2024", "2024年9月17日")],
         ("A payment from someone other than your customer", "來自客戶以外人士的付款"),
    P("Start at the top with a payment that did not come from your customer. Each hexagon is a question the circular expects you to answer before the money is accepted.",
      "由頂部開始：有一筆款項並非來自你的客戶。每個六邊形都是通函要求你在接納款項前回答的問題。")
    + fig(fig_tpp, ("To spot these payments early, the C&amp;ED strongly encourages you to have customers designate bank accounts in their own names for all payments; you should also obtain supporting documents such as bank statements and advice slips to check whether a payment came from a third party.",
                      "為及早識辨這類付款，海關強烈鼓勵你要求客戶指定其本人名下的銀行帳戶進行所有支付；你亦應向客戶取得證明文件（如銀行結單及通知書），以確定款項是否來自第三方。"), TPP_KEY)
    + table([th("Red flag", "可疑交易訊號"), th("What it looks like", "表現形式")], [
        tr(rh("A mismatch", "不相稱"), td("Transactions that do not fit what you know of the customer or the purpose of the business, such as remittances out of line with the economic activity, place of origin or person", "交易不符合你對客戶的認知或相關業務交易的目的，例如收發的匯款與相關經濟活動、來源地或人士不相稱")),
        tr(rh("Splitting", "拆分交易"), td("Several customers seemingly working together to break one transaction into two or more below the CDD thresholds", "多名客戶看似合謀，把一項交易拆分為兩項或以上低於客戶盡職審查門檻的交易")),
        tr(rh("Clustering", "模式一致"), td("Seemingly unrelated customers sharing one pattern, such as sending money to the same individual's account", "多名看似沒有關連的客戶採用相同的交易模式，例如將資金轉帳至同一人的帳戶")),
        tr(rh("Cash at the far end", "另一端以現金支付"), td("Large sums to or from outside Hong Kong with instructions to pay in cash; more suspicious still when a walk-in, non-resident customer asks for a one-off transaction", "指示以現金支付方式從香港以外地方轉入或向外轉出大額金錢；如屬非居民街客的一次過交易，則更為可疑", post=flag())),
        tr(rh("Acting for someone", "代他人行事"), td("A customer transacting for a third party with no appropriate business relationship to it", "客戶代表第三方進行交易，卻與該第三方沒有適當的業務關係")),
        tr(rh("One voice for many", "一人代多人指示"), td("Many unrelated customers authorising the same unregulated third party to instruct you", "多名看似沒有關連的客戶授權同一個非受規管的第三方向你作出指示")),
        tr(rh("Funded by others", "由他人出資"), td("Frequent or large transfers funded by a third party with no credible commercial reason", "在沒有可信商業理由或解釋的情況下，由第三方資助頻繁或大額的資金轉帳")),
        tr(rh("No papers to hand", "未能即時出示文件"), td("A customer who cannot immediately produce additional identification documents when asked", "客戶不能應要求立即提供額外的身分證明文件")),
    ], note=B("In general, if a transaction names a third party as the payer, or otherwise does not seem to fit the customer's usual business or activity, ask the customer to explain the nature of the remittance further. The list is illustrative, not exhaustive.",
              "一般而言，若交易付款人是第三方的姓名或名稱，或匯款似乎與該客戶的慣常業務或活動不符，便應要求客戶就匯款的性質作進一步解釋。以上清單僅屬例子，並非詳盡無遺。") + ' ' + cite_html(CI("17 Sep 2024")), minw=640)
    + table([th("Your written policy, approved by senior management, covers", "經高級管理層批准的書面政策涵蓋"), th("What it should cover", "應涵蓋的內容")], [
        tr(rh("When you accept", "何時接納"), td("The exceptional and legitimate circumstances in which third-party payments may be accepted, and how you judge them", "可接納第三方支付的特殊及合法情況，以及評估準則")),
        tr(rh("How you spot them", "如何識辨"), td("Monitoring systems and controls that pick out payments from third parties, for example by asking for bank statements and advice slips", "用以識辨第三方付款的監察系統及管控措施，例如要求客戶提供銀行結單及通知書")),
        tr(rh("How you vet them", "如何審查"), td("The due diligence process for deciding whether a payment meets your criteria", "判斷付款是否符合接納準則的盡職審查程序")),
        tr(rh("How you watch them", "如何監察"), td("Enhanced monitoring of accounts with third-party payments, and reporting suspicion to the JFIU", "加強監察涉及第三方支付的帳戶，並向財富情報組報告懷疑")),
        tr(rh("Who does it", "由誰執行"), td("The designated managers or staff responsible for carrying the policy out", "負責執行政策的指定經理或職員")),
        tr(rh("How it is run", "如何推行"), td("Acceptance of each third-party payment subject to stringent management approval; the policies and procedures approved by senior management, effectively communicated to all relevant staff, and enforced through robust compliance monitoring programmes", "接受每宗第三方支付均須經管理層嚴格審批；有關政策及程序由高級管理層審批、有效傳達所有有關職員，並經嚴格合規監察計劃執行")),
        tr(rh("Around it", "配套"), td("Clear guidance for the staff who evaluate payments, with examples of acceptable payers; documented enquiries, evidence and approvals; customers told of your policy and of the documents they must provide", "為評估付款的職員提供清晰指引，包括可接納付款人的例子；記錄查詢結果、證據及批准；告知客戶你的政策及須提供的文件")),
    ], note=cite_html(TP("2, 4, 10–12")), minw=680)
    + traps(
        trap(("Family is lower risk, not no risk", "家人風險較低，並非沒有風險"),
             ("A third party is anyone other than the customer, so a spouse, parent or child paying is still a third-party payment. Immediate family, the customer's beneficial owners or affiliated companies, and regulated financial institutions are generally lower risk, which scales the checks; it does not remove them.",
              "第三方指客戶以外的任何人，因此配偶、父母或子女代付仍屬第三方支付。直系親屬、客戶的實益擁有人或聯繫公司，以及受規管金融機構一般屬較低風險，影響的是審查的程度，而非免除審查。"),
             cc(TPF("3, 6"), TP("6–7"))),
        trap(("Encouraged, or expected", "鼓勵，還是應該做到"), None, TP("1–3, 5, 6(d), 11"),
             vs=[(("Strongly encouraged", "強烈鼓勵"), ("Customers paying from bank accounts held in their own names (standard 5). That is the only point the circular puts this way.", "客戶以本人名下的銀行帳戶付款（標準第5項）。通函只以這種語氣表達這一點。")),
                 (("Expected: \"should\"", "期望做到：「應」"), ("Serious consideration to refusing third-party payments (standard 1); no third-party payment at all if your controls cannot handle the risk (standard 3); for any you accept, stringent management approval (standard 2) and a documented record (standards 6(d) and 11).", "認真考慮拒絕第三方支付（標準第1項）；如管控措施無法應付風險，則不應接受任何第三方支付（標準第3項）；接納的每一宗均須經管理層嚴格審批（標準第2項）並妥為記錄（標準第6(d)及11項）。"))]),
        trap(("Missing the red flags counts too", "未能察覺可疑訊號同樣要負責"),
             ("The C&amp;ED says it will investigate all material issues and deficiencies, including where there is reason to suspect that operators knowingly facilitated third-party payments, and where operators appear to have failed to detect and act on any red flags, for reasons that include inadequate procedures and controls, with enforcement, discipline, suspension or revocation to follow where appropriate. Failing to take reasonable steps on apparent red flags may also breach legal or regulatory requirements, and involvement in the laundering may bring civil and criminal liability.",
              "海關表示會調查所有重要事項及不足之處，包括有理由懷疑經營者明知而促成第三方支付的情況，以及經營者因程序及管控措施不足等原因而看似未能偵察任何可疑交易訊號並作出相應行動的情況，並會按情況採取執法行動、紀律處分、暫時吊銷或撤銷牌照。沒有採取合理步驟偵察或妥為處理明顯的可疑交易訊號，亦可能違反法律規定或規管性規定，並可能因涉及有關洗錢活動而須負上民事或刑事責任。"),
             CI("17 Sep 2024")),
    ))

# ---------------------------------------------------------------- D. trade-based laundering
D_ = sec('tbml', [("Circular", "通函"), ("20 Jan 2026", "2026年1月20日")],
         ("Trade-based money laundering through a remittance counter", "經匯款櫃位進行的貿易洗錢"),
    P("The circular defines trade-based money laundering as disguising the proceeds of crime and moving value through trade activities, to legitimise their illegal origins or to finance criminal activities. In the figure, the top row is how the scheme moves value; the four boxes below are the circular's four numbered areas for enhancement, all aimed at the chain above.",
      "通函把貿易洗錢界定為通過利用貿易活動掩飾犯罪得益或轉移價值，以試圖合法化其非法來源，或為其非法活動提供資金。圖中上排是這類手法轉移價值的過程；下方四格是通函列出的四個編號優化範疇，全部針對上方的鏈條。")
    + fig(fig_tbml, ("The circular points you to the FATF's trade-based money laundering risk indicators, and asks you to review your existing controls through a gap analysis and to consider optimising them based on the four areas.",
                       "通函指你應參閱特別組織的貿易洗錢風險指標，並要求你透過差距分析覆核現有的管控措施，並考慮根據上述四個範疇作出優化。"), TBML_KEY)
    + traps(
        trap(("Closing an alert is a decision that needs reasons", "消除警報是須有理由的決定"),
             ("The circular singles out alerts closed without sufficient justification and analysis. Before closing one, examine the background and purpose, ask the customer or collect more CDD information, and weigh the risk profile, source of funds or wealth, and past transactions.",
              "通函特別指出，不可在沒有充分理由及分析的情況下消除警報。消除前須審查交易背景及目的、向客戶查詢或索取額外盡職審查資料，並考慮風險狀況、資金或財富來源及交易歷史。"),
             TB("3")),
        trap(("A new company with nothing behind it is a warning in itself", "毫無實質的新公司本身已是警號"),
             ("Newly established legal entities without significant assets, employees or active operations pose a much higher ML/TF risk. The circular asks you to proactively consider anti-fraud procedures to scrutinise what they give you, verifying the transaction is genuine and assessing how likely it is that a shell company is the originator or recipient.",
              "新成立且缺乏顯著資產、員工或活躍業務運作的法律實體，帶來較高的洗錢及恐怖分子資金籌集風險。通函要求你主動考慮採取反欺詐程序審查它們提供的資料，以核實交易的真實性，並評估匯款人或收款人為空殼公司的可能性。"),
             TB("2")),
        trap(("Both lines of defence need the training", "兩道防線都需要培訓"),
             ("The circular expects adequate staff training and guidance so that both the first and the second lines of defence have sufficient ML/TF risk awareness. It does not say who sits in each line; in common usage the first is front-line staff, such as your counter, and the second is compliance.",
              "通函期望透過足夠的員工培訓及指導，使第一及第二道防線均具備充足的洗錢及恐怖分子資金籌集風險意識。通函沒有說明各道防線由誰組成；一般理解第一道防線指前線員工（例如櫃位），第二道防線指合規職能。"),
             TB("1")),
        trap(("No amount is too small, and an attempt counts", "金額多少都要報，未完成的交易亦然"),
             ("The circular reiterates that the reporting duty applies whatever the amount involved, whether or not the transaction was actually carried out, and to attempted transactions. Where you hold information on both the originator and the recipient, take all of it into account in deciding whether to file.",
              "通函重申，舉報責任不論所涉金額，亦不論交易事實上有否進行，並涵蓋試圖進行的交易。如你掌握匯款人及收款人的資料，便應考慮所有有關資料，以決定是否提交可疑交易報告。"),
             TB("4")),
    ))

# ---------------------------------------------------------------- F. CDD questions
F_ = sec('cdd', [("FAQ", "常見問題"), ("with the circular of", "另參考"), ("22 Nov 2023", "2023年11月22日通函"), ("and Guideline Ch. 2, 4", "及指引第2、4章")],
         ("Customer due diligence: questions the FAQ, circulars and Guideline settle", "客戶盡職審查：常見問題、通函及指引解答的疑問"),
    P("Find the situation at your counter in the left column. Answers from the FAQ and circulars clarify the Guideline rather than replacing it; the rules themselves are on the <a href=\"#s2-map\">Schedule 2 page</a>.",
      "在左欄找出你在櫃位遇到的情況。來自常見問題及通函的答案是對指引的澄清，而非取代；規則本身見<a href=\"#s2-map\">附表2一頁</a>。")
    + h3("Identity documents", "身分證明文件")
    + table([th("The situation", "情況"), th("The answer", "答案")], [
        tr(td("The customer is not a Hong Kong resident: which documents are reliable and independent?", "客戶並非香港居民：哪些文件屬可靠及獨立？", FAQ(1)),
           td("A non-resident's identity should be verified by reference to a valid travel document. For a non-resident who is not physically present in Hong Kong, you may identify and/or verify identity by reference to a valid international passport or other travel document; a current national identity card bearing the person's photograph; or a current valid national driving licence with photographic evidence of identity, issued by a competent national or state authority. International driving permits and licences are not acceptable for this purpose. The Guideline's main text also gives a Hong Kong identity card or other national identity card as an example for verifying any customer who is a natural person",
              "非居民的身分應根據其有效旅遊證件核實。至於沒有現身香港的非香港居民，你應根據有效的國際護照或其他旅遊證件；附有有關個人照片的有效國民身分證；或由主管的國家或政府機構簽發、執照上有照片證明其身分的有效國家駕駛執照，識別及／或核實其身分。國際駕駛許可證及執照不能用於此目的。《打擊洗錢指引》正文亦把香港身份證或其他國家的身份證列為核實屬自然人的客戶身分的例子", cc(("Guideline App. A ¶1–2, n.72", "《打擊洗錢指引》附錄A第1至2段、註72"), "¶4.3.3(a)"), post=flag())),
        tr(td("Which documents count as travel documents?", "哪些文件屬旅遊證件？", FAQ(2)),
           td("The FAQ lists: a passport; the Mainland Travel Permit for Taiwan Residents; a Seaman's Identity Document issued under the International Labour Organisation Convention / Seafarers Identity Document Convention 1958; the Taiwan Travel Permit for Mainland Residents; the Permit for residents of Macau issued by the Director of Immigration; and the Exit-entry Permit for Travelling to and from Hong Kong and Macau, including the one for official purposes. The Guideline's Appendix A has the same list except that its first item is the Permanent Resident Identity Card of the Macau SAR, and it defines a travel document as a passport or other document with the holder's photograph establishing identity and nationality, domicile or place of permanent residence",
              "常見問題列出：護照；台灣居民往來內地通行證；海員身分證明文件（根據《國際勞工組織公約》╱《1958年海員身分證件公約》簽發）；內地居民的台灣旅遊許可證；由入境事務處處長簽發的澳門居民旅遊證；以及往來港澳通行證，包括因公往來香港澳門特別行政區通行證。《打擊洗錢指引》附錄A的清單相同，唯第一項是澳門特別行政區永久居民身分證；附錄A並把旅遊證件界定為附有持有人照片，能確定持有人的身分及國籍、原居地或永久居留地的護照或其他證件", ("Guideline App. A ¶1–3, n.72", "《打擊洗錢指引》附錄A第1至3段、註72"), post=flag())),
        tr(td("A travel document was used to verify a customer: what goes on file?", "以旅遊證件核實客戶身分：須存檔甚麼？", FAQ(3)),
           td("A copy of the biodata page, the one with the holder's photograph and personal details", "載有持證人照片及個人資料的「個人資料頁」的複本")),
        tr(td("The customer's name has changed", "客戶已更改姓名", FAQ(4)),
           td("Verify the new name from a reliable and independent source, and check other details on the new document, such as date of birth and identity card number, against your records to guard against impersonation. If in doubt, you may ask for the marriage certificate or deed poll. A change made before the relationship began needs only the current name verified",
              "根據可靠及獨立來源核實新姓名，並以現有紀錄核對新證件上的其他資料（例如出生日期及身份證號碼），以防假冒。如有疑問，可索取結婚證書或改名契。如姓名於建立業務關係前已更改，只須核實現時的姓名")),
        tr(td("An identity document you verified has since expired", "你核實過的身分證明文件已過期", FAQ(15)),
           td("No need to re-verify just because it expired. Keep the information current through periodic and trigger-event reviews", "毋須僅因證件過期而再次核實身分。應透過定期及觸發事件覆核，確保資料反映現況", post=flag())),
        tr(td("You are handed a print-out of an electronic certificate of incorporation", "客戶交來電子公司註冊證書的印刷本", FAQ(13)),
           td("You can corroborate it against another document or source, such as the Companies Registry's record. There is nothing to corroborate if you downloaded it yourself from a reliable source", "可核對其他識別文件或資料（例如公司註冊紀錄）。如是你自行從可靠來源下載的，則毋須核對")),
        tr(td("A document is in a foreign language", "文件以外語書寫", FAQ(14)),
           td("The translation need not come from a professional such as a solicitor; any reliable source will do, including technology and common translation tools", "翻譯毋須由律師等專業人士進行；任何可靠來源均可，包括科技方案及常用翻譯工具")),
        tr(td("You use certification as a supplementary measure for a customer who is not physically present", "客戶沒有現身，你以認證作為增補措施", FAQ(27)),
           td("Certify the identification document itself: identity card, passport, certificate of incorporation or incumbency. Not every other CDD document, and not documents you can check against public sources. Customers may always show you the originals instead", "應認證用作核實身分的文件本身：身份證、護照、公司註冊證書或職權證明書。毋須認證所有其他盡職審查文件，亦毋須認證可與公開來源核對的文件。一般而言，你應盡量容許客戶（如客戶有意）向你的職員出示文件正本")),
        tr(td("A customer onboards remotely with iAM Smart", "客戶以關長認可的數碼識別系統遙距開戶", cc(FAQ(9), "¶4.3.1(d), 4.10.2")),
           td("A digital identification system recognised by the Commissioner is one of the reliable and independent sources for identifying and verifying a customer. If you verified the customer's identity on data or information it provided, you are not required to carry out the additional measures for a customer who is not physically present. The FAQ gives iAM Smart as an example of such a system",
              "關長認可的數碼識別系統屬識別和核實客戶身分的可靠及獨立來源之一。如你根據該系統所提供的數據或資料核實客戶的身分，便無須執行就客戶沒有現身而須採取的額外措施", post=flag())),
    ], minw=760)
    + h3("Companies, owners and the people acting for them", "公司、擁有人及代表行事的人")
    + table([th("The situation", "情況"), th("The answer", "答案")], [
        tr(td("The principal place of business does not fit what you know of the customer", "主要營業地點與你對客戶的了解不符", FAQ(5)),
           td("It is where the entity mainly operates, the same as or different from its registered office. Find out why that address was given", "指法人營運主要所在地，可與註冊辦事處地址相同或不同。應找出提供該地址的理據")),
        tr(td("The registered office address is on a reliable document you already hold, such as a certificate of incumbency", "註冊辦事處地址已載於你持有的可靠文件（例如職權證明書）", FAQ(6)),
           td("You may accept it as evidence of the address unless you know it is out of date; there is no need to ask again", "可接納為地址證明，除非你知悉該地址不能反映現況；毋須另行索取")),
        tr(td("You must verify a partnership", "須核實合夥的身分", FAQ(7)),
           td("A record of registration, or a partnership agreement or deed, which may be an extract or redacted where the risk is not high; more may be needed to see the powers that bind it. For a well-known, long-established partnership with plenty of public information, confirming its membership of a professional or trade body is likely to be enough",
              "註冊記錄，或合夥協議或契約（風險不高時可接納摘錄或刪節本）；可能需要額外文件以了解約束該合夥的權力。如屬眾所周知、歷史悠久且有大量公開資料的合夥，確認其專業或行業團體會籍可能已足夠")),
        tr(td("A corporate customer has not given you an ownership chart", "法團客戶沒有提供擁有權架構表", FAQ(8)),
           td("It is not mandatory; decide by risk and complexity. Identify every intermediate layer, but you need not verify the intermediate companies as a matter of routine", "並非強制；按風險及結構的複雜程度決定。須識別所有中介層，但毋須例行核實中介層公司的細節", post=flag())),
        tr(td("Who counts as exercising ultimate control over management?", "誰屬行使對管理的最終控制權的人？", FAQ(10)),
           td("For example, someone controlling through personal ties to the over-25% owners, or without ownership through financing, close family, historical or contractual links, or a company's default on payments. Control can be presumed even if never exercised. If nothing in CDD points to such a person, you need not go looking",
              "例如透過與持股超過25%人士的私人關連施加控制，或在沒有擁有權下透過參與融資、密切家庭關係、歷史或合約聯繫，或因公司違反支付約定而施加控制。即使從未實際行使，控制亦可被推定存在。如盡職審查中沒有跡象顯示有此人，則毋須主動識別")),
        tr(td("Must directors or owners be present to open a corporate account?", "開立公司帳戶時，董事或擁有人是否須在場？", FAQ(9)),
           td("No. The account is opened by a natural person properly authorised to act for the company, identified and verified, with written authority. Face to face, at least one authorised person should be physically present; otherwise mitigate the increased risk, for example with the additional due diligence measures of the Guideline or a digital identification system recognised by the Commissioner (the FAQ gives iAM Smart as an example)",
              "毋須。帳戶由獲妥善授權代表公司行事的自然人開立，須識別及核實其身分並取得授權書。如以面對面方式建立關係，最少一名獲授權人士應在場；否則應減低任何增加的風險，例如採取指引所述的額外盡職審查措施，或應用獲關長認可並屬可靠及獨立來源的數碼識別系統")),
        tr(td("The company lists many authorised signatories", "公司列出多名獲授權簽署人", FAQ(12)),
           td("Identify and verify only those who are persons purporting to act on its behalf. In a low-risk relationship, a list of them confirmed by an independent department of the customer, such as compliance, audit or human resources, can do", "只須識別及核實屬看似代表客戶行事的人。低風險的業務關係中，可依據由客戶內部獨立部門（例如合規、審計或人力資源部）核實的名單", post=flag())),
        tr(td("Who is a person purporting to act on the customer's behalf?", "誰屬看似代表客戶行事的人？", cc(FAQ(11), CI("22 Nov 2023"))),
           td("Decided by the person's role, what they are authorised to do and the risk, using a framework per customer segment that is consistent across departments. Every legal-person customer should have at least one. Verify authority with a board resolution or similar written authorisation, and never treat that person as the customer in place of the company",
              "按該人的角色、獲授權進行的活動及相關風險判斷，並應按客戶類別採用在各部門之間保持一致的框架程序。每名法人客戶最少應有一名看似代表客戶行事的人。須以董事局決議或類似書面授權核實其權力，且不可把該人當成客戶而忽略公司本身")),
    ], minw=760)
    + h3("Customer risk assessment", "客戶風險評估")
    + table([th("The situation", "情況"), th("What the C&amp;ED expects", "海關的期望")], [
        tr(td("An individual says the remittances are personal, gives a company address as proof of address, and says they pay for goods", "個人客戶聲稱匯款屬私人用途，卻以公司地址作地址證明，並聲稱交易是支付貨款", CI("22 Nov 2023")),
           td("Follow the inconsistency up before treating CDD as done. If the customer misled you, or the transactions do not fit the profile, enquire promptly; with no satisfactory explanation there may be grounds for suspicion, and suspicion means a report to the JFIU",
              "在視為已完成盡職審查前須跟進不一致之處。如客戶誤導你，或交易與其狀況不符，須盡快查詢；如未能取得滿意解釋，可能已有懷疑理由，而有懷疑即須向財富情報組報告")),
        tr(td("Customers with similar risk factors ended up with inconsistent risk ratings", "有同類風險因素的客戶獲給予不一的風險水平", CI("22 Nov 2023")),
           td("Give staff guidance on deriving the overall rating from your pre-defined factors, and keep a record of how each rating was reached", "向員工提供指引，說明如何按預設因素得出整體風險水平，並記錄每個風險水平如何得出")),
        tr(td("A risk factor you rely on is now judged higher risk than before", "你所依據的某項風險因素現被評為風險較前為高", CI("22 Nov 2023")),
           td("Review whether the existing customers associated with it should have their overall risk raised", "覆核與該因素有關的現有客戶，其整體風險水平是否應予提高")),
        tr(td("Can you apply the same extent of CDD to every customer, whatever the risk?", "可否不論風險，對所有客戶劃一採用同一程度的盡職審查？", "¶2.13 · ¶4.1.2"),
           td("No. The customer risk assessment determines the extent of CDD measures: the information obtained, and how far it is verified, should be increased where the risks are higher and may be simplified where they are lower, and the assessment helps you differentiate between the risks of individual customers. Where the risks are high you should conduct EDD; in low-risk situations you may apply SDD",
              "不可以。客戶風險評估決定需採取何種程度的盡職審查措施：風險較高便需索取數量及類別更多的資料，並以更嚴謹方式核實；風險較低則可簡化審查程序；評估亦有助你分辨個別客戶所涉的風險。如風險屬於高，應採取更嚴格的盡職審查措施；在低風險的情況下，可採取簡化盡職審查措施")),
    ], minw=760)
    + traps(
        trap(("An expired passport is not an unverified customer", "護照過期不等於客戶身分未經核實"),
             ("Once identity has been satisfactorily verified there is no duty to re-verify, outside the circumstances the Guideline specifies. Expiry of the document alone does not trigger it; keeping the file current at periodic or trigger reviews does the job.",
              "身分一經圓滿核實，除指引訂明的情況外，毋須再次核實。證件過期本身不會觸發再次核實；在定期或觸發事件覆核時更新資料即可。"),
             FAQ(15, "5.2")),
        trap(("Signatories are not automatically people to verify", "獲授權簽署人不一定須核實"),
             ("Only a signatory who is a person purporting to act on the customer's behalf has to be identified and verified. The rest are outside that duty.",
              "只有屬看似代表客戶行事的人的簽署人，才須識別及核實身分。其餘簽署人不在此責任範圍內。"),
             FAQ(12)),
        trap(("A recognised digital identification system verifies who someone is, not everything about them", "認可數碼識別系統核實身分，而非全部盡職審查"),
             ("It is a source for identifying and verifying the customer, and it spares you the additional measures for a customer who is not physically present. The other CDD measures remain: identifying any beneficial owner and taking reasonable measures to verify their identity; obtaining information on the purpose and intended nature of the relationship unless obvious; and identifying anyone purporting to act for the customer, taking reasonable measures to verify their identity, and verifying their authority to act.",
              "它是識別和核實客戶身分的來源，並讓你無須就客戶沒有現身而執行額外措施。其他盡職審查措施仍然適用：識別任何實益擁有人，並採取合理措施核實其身分；取得業務關係的目的及擬具有的性質的資料，除非顯而易見；以及識別看似代表客戶行事的人，採取合理措施核實其身分，並核實其代表客戶行事的授權。"),
             cc("¶4.1.3", "¶4.3.1(d), 4.10.2")),
    ))

# ---------------------------------------------------------------- G. higher risk, monitoring, transfers, records
G_ = sec('edd', [("FAQ", "常見問題"), ("with circulars of", "另參考"), ("3 and 16 Jul 2026", "2026年7月3日及16日通函"), ("and Guideline ¶6.16–6.18 · ¶8.5", "及指引第6.16至6.18、8.5段")],
         ("Higher risk, monitoring, transfers and records: what the FAQ, circulars and Guideline settle", "高風險、監察、轉帳及紀錄：常見問題、通函及指引的解答"),
    P("The same layout as the section before, for the questions that come after onboarding.", "編排與上一節相同，處理開戶以後的疑問。")
    + table([th("The situation", "情況"), th("The answer", "答案")], [
        tr(td("Do you need the source of wealth of every customer?", "是否須確立每名客戶的財富來源？", FAQ(16)),
           td("No, only in high-risk situations: a customer or beneficial owner who is a non-Hong Kong PEP; a high-risk relationship with a Hong Kong or international-organisation PEP; other situations high risk by their nature. For everyone else, occupation or business nature usually gives enough of a profile, and even for a high-risk customer you need not collect evidence going back decades where the risk does not justify it",
              "不需要，只在高風險情況下才須確立：客戶或其實益擁有人屬非香港政治人物；與香港或國際組織政治人物建立的高風險業務關係；其他本質上屬高風險的情況。其他客戶的職業或業務性質通常已足以了解其狀況；即使屬高風險客戶，如風險水平不足以支持，亦毋須收集數十年前的證據", post=flag())),
        tr(td("Which jurisdictions are the ones the FATF calls for measures on, where EDD proportionate to the risk should be applied?", "哪些司法管轄區屬特別組織呼籲採取措施、應採取與風險相稱的更嚴格的盡職審查措施？", FAQ(17, "4.15.1")),
           td("Only those in the FATF Public Statement: apply EDD proportionate to the risk to relationships and transactions with customers from them. For the list in the statement Improving Global AML/CFT Compliance: On-going Process, EDD is not mandatory, but the link should be taken into account in the customer's overall risk profile",
              "只限「特別組織公開聲明」所列的司法管轄區：應對涉及來自這些司法管轄區的客戶的業務關係和交易，採取與風險相稱的更嚴格的客戶盡職審查。「改善全球打擊洗錢及恐怖分子資金籌集的合規情況：持續進展」聲明所列的司法管轄區，毋須強制採取更嚴格的盡職審查措施，但在釐定客戶整體風險狀況時應顧及有關連繫", post=flag())),
        tr(td("A customer works for a United Nations agency", "客戶任職聯合國機構", FAQ(18)),
           td("UN agencies are international organisations, so a prominent function there makes the person an international-organisation PEP", "聯合國機構屬國際組織，因此在該等機構擔任重要職位的人屬國際組織政治人物")),
        tr(td("A customer holds a senior post at an international sports association", "客戶在國際體育協會擔任高層職位", FAQ(19)),
           td("Not an international-organisation PEP. An international organisation must meet all three tests: set up by formal political agreements between member States that have the status of international treaties; its existence recognised by law in its member countries; and not treated as a resident institutional unit of the country where it is located. A sports association does not. Still consider whether the role affects the customer's risk",
              "不屬國際組織政治人物。國際組織須同時符合三項條件：由成員國根據具有國際條約地位的正式政治協議成立；其地位獲成員國的法律認可；以及不會被視作所處國家的常駐機構單位。體育協會並不符合。但仍應考慮該職位會否影響客戶的風險狀況", cc(FAQ(19), "¶4.9.15"))),
        tr(td("Who is senior management for approving a PEP relationship?", "誰屬可批准與政治人物建立關係的高級管理層？", FAQ(21)),
           td("You decide, in a clear written policy naming who may approve. They should be senior enough; their number and titles depend on your size, type and risk assessment, and they may sit in another jurisdiction if that reflects your structure", "由你自行決定，並以清晰的書面政策列明誰可批准。有關人選須具足夠資歷；人數及職銜視乎你的規模、類別及機構風險評估而定；如能反映你的組織架構，亦可包括其他司法管轄區的人員")),
        tr(td("Who may independently validate your transaction monitoring?", "誰可獨立核實你的交易監察系統？", FAQ(23)),
           td("An external party, or your internal audit function if it is properly segregated and has enough expertise and resources", "外界人士，或具適當分工、並有足夠專業知識及資源的內部審核職能")),
        tr(td("Whom to screen in a cross-border wire transfer or remittance", "跨境電傳轉帳或匯款須篩查誰", FAQ(24)),
           td("At a minimum the originator, the recipient, the ordering, intermediary and beneficiary institutions, and every party named in the payment message", "最低限度須篩查匯款人、收款人、匯款機構、中介機構、收款機構，以及撥付訊息中被具名的所有人士", post=flag())),
        tr(td("How accurate must the originator information be?", "匯款人資料須準確到甚麼程度？", FAQ(25)),
           td("It is deemed accurate once the originator's identity has been verified under the Ordinance and the Guideline; no further verification is normally needed", "只要已按條例及指引核實匯款人身分，所需資料即視為準確；一般毋須再作核實")),
        tr(td("For a wire transfer or remittance of $8,000 or more, the originator gives a PO box as the address that accompanies it", "就款額相等於8,000元或以上的電傳轉帳及匯款交易，匯款人以郵政信箱作為附隨的匯款人地址", FAQ(26)),
           td("Avoid it unless there is no alternative: the address must locate the party clearly for sanctions screening and monitoring. The address is only one option: for a wire transfer of $8,000 or more the originator information can instead carry a customer identification number, an identification document number or, for an individual, the date and place of birth. The wire transfer and remittance rules both apply to amounts equal to or above $8,000, so a transaction of exactly $8,000 is caught",
              "除非別無選擇，否則應避免：地址須足以清楚識別有關人士的位置，以便篩查受制裁名單及進行監察。地址只是選項之一：款額相等於8,000元或以上的電傳轉帳，匯款人資料亦可改為附上客戶識別號碼、識別文件號碼，或（如匯款人為個人）出生日期及地方。有關電傳轉帳及匯款交易的規定均適用於相等於8,000元或以上的款額，因此款額剛好為8,000元的交易亦受涵蓋", cc(FAQ(26), "¶10.5", "s.12(5)(a), 13(1) Sch. 2"), post=flag())),
        tr(td("The FATF has revised Recommendation 16 on payment transparency and consulted on guidance to implement it", "特別組織已修訂有關支付透明度的第16項建議，並就實施指引進行諮詢", CI("16 Jul 2026")),
           td("The revisions, agreed in June 2025, increase the transparency of the information that accompanies cross-border payments and require tools to protect against fraud and error. All jurisdictions are expected to be ready to implement them by the end of 2030. The FATF consulted on draft guidance until 21 August 2026, with a copy of responses to the C&amp;ED, on misdirected payments and the three options for alignment checks, newer payment methods such as digital wallets and mobile money, and data protection and privacy",
              "修訂於2025年6月通過，旨在提升跨境支付資訊的透明度，並要求引入防止詐騙及錯誤的工具。所有司法區預計需於2030年底前實施相關變更。特別組織就指引草案進行諮詢，回覆須於2026年8月21日前提交並抄送海關，範圍包括偵測及防止錯誤支付（包含三種校正檢查選項）、電子錢包與移動支付等新興支付方式，以及資料保護及隱私")),
        tr(td("Records of an applicant you turned away", "被拒申請人的紀錄", FAQ(28)),
           td("The Ordinance does not require you to keep them, though you may keep them to meet other obligations", "條例並無規定須保存，但你可為履行其他法定責任而保留")),
        tr(td("A transaction instruction arrives by instant messaging, email or phone", "交易指示經即時通訊、電郵或電話傳來", "¶8.5"),
           td("The Guideline names no channel. It covers the original or a copy of every document, and a record of the data and information, obtained or generated in connection with each transaction, sufficient to permit reconstruction of individual transactions; an instruction for the transaction, however it arrives, is information obtained in connection with it, so keep a record of it with the transaction",
              "指引沒有指明任何渠道。它涵蓋與每項交易有關連的情況下取得或產生的文件的正本或複本，及如此取得或產生的數據及資料的紀錄，並應足以重組個別交易；交易指示不論經何種渠道傳來，都是與該交易有關連而取得的資料，因此應連同該交易保存其紀錄")),
        tr(td("Which screening records to keep", "須保存哪些篩查紀錄", "¶6.16–6.18"),
           td("All screening records, including the screening of customers, their beneficial owners and all relevant parties in a cross-border wire transfer, together with the results of enhanced checks on possible name matches, documented or recorded electronically",
              "篩查紀錄，包括對客戶、客戶的實益擁有人及跨境電傳轉帳相關各方的篩查，連同就可能吻合的姓名／名稱所作更嚴格查核的結果，應記錄在案或以電子方式記錄")),
    ], minw=760)
    + traps(
        trap(("The FATF's two lists do different jobs", "特別組織的兩份名單作用不同"), None, FAQ(17, "4.15.1"),
             vs=[(("FATF Public Statement", "特別組織公開聲明"), ("The jurisdictions \"for which this is called for by the FATF\". EDD proportionate to the risk should be applied.", "屬「特別組織對其作出呼籲的司法管轄區」。應採取與風險相稱的更嚴格的盡職審查措施。")),
                 (("On-going Process statement", "持續進展聲明"), ("EDD is not mandatory; the connection should be taken into account in the customer's overall risk profile.", "毋須強制採取更嚴格的盡職審查措施；有關連繫應計入客戶的整體風險狀況。"))]),
    )
    + h3("The lists as the FATF left them in June 2026", "特別組織於2026年6月公布的名單")
    + P("The lists change whenever the FATF issues updated statements. This version comes from the Call for Action statement of 19 June 2026 and an updated statement on increased monitoring; the FATF also published the outcomes of its plenary of 17 to 19 June 2026. They reached MSOs by a circular of 3 July 2026 that followed an earlier one of 20 March 2026. The circular reminds you to check the FATF website for the latest statements. Each row is a jurisdiction or group; read across for what the FATF asks.",
        "每當特別組織發出最新聲明，名單便會改變。以下版本來自特別組織於2026年6月19日發出的呼籲採取行動聲明，以及一份有關被加強監察的司法管轄區的最新聲明；特別組織亦發表了其2026年6月17至19日全體會議的成果。有關內容經2026年7月3日的通函轉達金錢服務經營者（此前一份通函於2026年3月20日發出）。通函指你應瀏覽特別組織網站，查閱最新聲明。每一行是一個或一組司法管轄區；橫向閱讀可見特別組織的要求。")
    + table([th("Jurisdiction", "司法管轄區"), th("Which statement", "所屬聲明"), th("What the FATF calls for", "特別組織的要求")], [
        tr(rh("Democratic People's Republic of Korea", "朝鮮民主主義人民共和國"),
           td("High-Risk Jurisdictions subject to a Call for Action", "呼籲各方對高風險司法管轄區採取行動的聲明"),
           td("Countermeasures, with greater vigilance and renewed implementation and enforcement. The FATF's listed countermeasures include ending correspondent relationships with DPRK banks, closing their subsidiaries or branches, and limiting business relationships and financial transactions with DPRK persons. The FATF also highlights that, as set out in UNSCR 2270, the DPRK frequently uses front companies, shell companies, joint ventures and complex, opaque ownership structures to violate sanctions; whom to screen is on the <a href=\"#g6-screening\">Guideline Chapter 6 page</a>",
              "採取針對措施，並需要更多的警覺性和重新實施和執行有關措施。特別組織列出的針對措施包括終止與該國銀行的代理關係、關閉該國銀行的任何子公司或分行，以及限制與該國人士的業務關係和金融交易。特別組織亦強調，正如聯合國安全理事會第2270號決議中所述，朝鮮民主主義人民共和國經常使用前置公司、空殼公司、合營公司以及複雜且不透明的擁有權結構，以達到違反制裁的目的；須篩查的對象見<a href=\"#g6-screening\">指引第6章一頁</a>", CI("3 Jul 2026", ("notes 2, 3", "註2、3")))),
        tr(rh("Iran", "伊朗"),
           td("High-Risk Jurisdictions subject to a Call for Action", "呼籲各方對高風險司法管轄區採取行動的聲明"),
           td("Effective countermeasures; the FATF remains concerned about terrorist financing threats from Iran", "採取有效的針對措施；特別組織繼續關注來自伊朗的恐怖分子資金籌集風險")),
        tr(rh("Myanmar", "緬甸"),
           td("High-Risk Jurisdictions subject to a Call for Action", "呼籲各方對高風險司法管轄區採取行動的聲明"),
           td("EDD proportionate to the risk, called for since October 2022. As part of that EDD, the FATF requires financial institutions to increase the degree and nature of monitoring of the business relationship, to determine whether its transactions or activities appear unusual or suspicious. If no further progress is made by October 2026, the FATF will consider countermeasures", "採取與風險相稱的更嚴格的盡職審查措施，自2022年10月起已有此要求。特別組織要求金融機構在執行更嚴格的盡職審查時，應增強對業務關係的監控程度和性質，以釐清該等交易或活動是否有看似不尋常或可疑的情況。若緬甸於2026年10月或之前仍沒有取得進展，特別組織將會考慮採取針對措施", CI("3 Jul 2026", ("note 5", "註5")), post=flag())),
        tr(rh("Jurisdictions under increased monitoring, with Bosnia and Herzegovina and Iraq newly added", "被加強監察的司法管轄區，新加入波斯尼亞和黑塞哥維那及伊拉克"),
           td("Jurisdictions under Increased Monitoring", "有關被加強監察的司法管轄區的聲明"),
           td("They have committed to resolve strategic deficiencies swiftly within agreed timeframes; the FATF monitors their progress and encourages its members to take the statement into account in their risk analysis", "這些司法管轄區承諾於協定時間內迅速解決策略性缺失；特別組織會密切監察其進展，並鼓勵成員在進行風險分析時參考該聲明")),
    ], note=B("For every jurisdiction identified as high-risk, the FATF calls for enhanced due diligence and, in the most serious cases, countermeasures. The circular names only the two jurisdictions added to the increased-monitoring list; the full list is on the FATF website.",
              "就所有被識別為高風險的國家而言，特別組織要求採取更嚴格的盡職審查，並在最嚴重的情況下採取針對措施。通函只列出新加入被加強監察名單的兩個司法管轄區；完整名單載於特別組織網站。") + ' ' + cite_html(CI("3 Jul 2026")), minw=820)
    + traps(
        trap(("Two sets of names for the lists", "兩套名單名稱"), ("Match a list by what it asks for, not by its title: the FAQ and the circular of July 2026 name the FATF statements differently.", "應按名單的要求而非名稱辨認：常見問題與2026年7月的通函對特別組織聲明的稱呼不同。"),
             cc(FAQ(17), CI("3 Jul 2026")),
             vs=[(("The FAQ's titles", "常見問題的名稱"), ("\"FATF Public Statement\" and \"Improving Global AML/CFT Compliance: On-going Process\".", "「特別組織公開聲明」及「改善全球打擊洗錢及恐怖分子資金籌集的合規情況：持續進展」。")),
                 (("The 2026 circular's titles", "2026年通函的名稱"), ("\"High-Risk Jurisdictions subject to a Call for Action\" and \"Jurisdictions under Increased Monitoring\".", "「呼籲各方對高風險司法管轄區採取行動的聲明」及「被加強監察的司法管轄區的聲明」。"))]),
    ))

# ---------------------------------------------------------------- H. periodic returns
H_ = sec('returns', [("Circular", "通函"), ("30 May 2025", "2025年5月30日"), ("Licensing Guide ¶11.2", "《牌照指引》第11.2段")],
         ("Periodic returns: twice a year, online", "定期申報表：每年兩次，網上遞交"),
    P("The strip runs from January to the end of February of the next year. Each half-year has its own return, lodged within two weeks of the start of the next half; the dashed row at the bottom is the old quarterly cycle it replaced, drawn for a licence that began on 1 March.",
      "橫條由1月開始，至翌年2月底為止。每半年各有一份申報表，於下一個半年開始後兩星期內遞交；最下方虛線一行是被取代的舊有每季周期，以一個於3月1日生效的牌照為例。")
    + fig(fig_pr, ("Paper returns are no longer accepted. Create a user account on the Money Service Operators Licensing System before your first lodgement.",
                     "海關不再接受紙本申報表。首次遞交前，須先在金錢服務經營者牌照系統建立使用者帳戶。"), PR_KEY)
    + numreq([
        (("2 a year", "每年2份"),
         ("One return for 1 January to 30 June, one for 1 July to 31 December", "一份涵蓋1月1日至6月30日，一份涵蓋7月1日至12月31日"),
         ("From 30 June 2025; the first covered January to June 2025 and was lodged from 1 July 2025", "由2025年6月30日起；首份涵蓋2025年1月至6月，於2025年7月1日起遞交"),
         ("A late return may result in suspension and/or revocation of the licence", "逾期遞交將會導致牌照被暫時吊銷及／或撤銷"),
         cc(CI("30 May 2025"), LG("11.2"))),
        (("2 weeks", "兩星期"),
         ("Lodge each return", "遞交每份申報表"),
         ("Within 2 weeks beginning from the start of each half year, for the half year just ended: the January to June return from 1 July, the July to December return from 1 January; unless the Commissioner specifies otherwise by written notice",
          "每半年開始起計兩星期內遞交，涵蓋剛結束的半年：1月至6月的申報表於7月1日起遞交，7月至12月的於翌年1月1日起遞交；除非關長以書面通知另作指定"),
         ("As in the row above: it may result in suspension and/or revocation", "與上一行相同：將會導致牌照被暫時吊銷及／或撤銷"),
         LG("11.2")),
    ])
    + table([th("Part of the return", "申報表部分"), th("What goes in", "須填報的內容")], [
        tr(rh("Money changing", "貨幣兌換"), td("Money changing data only, leaving out the amounts of remittances; the amounts of every foreign currency involved, largest first", "只填報貨幣兌換數據，不包括匯款交易金額；所涉全部外幣的金額，由多至少排列", post=flag())),
        tr(rh("Remittance", "匯款"), td("Amounts by jurisdiction, largest first; the share of each delivery channel used and of each type of customer served, each set totalling 100%", "按司法管轄區列出的金額，由多至少排列；所用各交付渠道及所服務各類客戶的比例，各自總和須為100%")),
        tr(rh("Assets", "資產"), td("An estimate of your total assets", "估計資產總值")),
        tr(rh("How", "遞交方式"), td("Only through the Money Service Operators Licensing System; no paper", "只可經金錢服務經營者牌照系統遞交；不接受紙本")),
    ], note=cite_html(CI("30 May 2025", ("Annex", "附件"))), minw=640)
    + traps(
        trap(("Half-years by the calendar, not by your licence date", "按曆年劃分半年，而非按牌照日期"), None, CI("30 May 2025"),
             vs=[(("Until 30 June 2025", "2025年6月30日前"), ("Quarterly, four a year, counted from the start date of your licence.", "每季一次，每年四次，由牌照生效日期起計。")),
                 (("From 30 June 2025", "2025年6月30日起"), ("Half-yearly, two a year, January to June and July to December for every licensee alike, with three new kinds of data: currencies changed, jurisdictions remitted to or from, and delivery channels.", "每半年一次，每年兩次，所有持牌人劃一為1月至6月及7月至12月；並新增三類資料：兌換的外幣、匯款所涉司法管轄區，以及交付渠道。"))]),
        trap(("A late return is one of the Licensing Guide's examples, not one of the two grounds in section 34(1)", "逾期遞交是《牌照指引》所舉的例子之一，並非第34(1)條所列的兩項理由之一"),
             ("A late return may result in suspension and/or revocation of the licence, and the Licensing Guide lists failing to submit a periodic return on time among the grounds on which the Commissioner may revoke or suspend a licence. That list is a non-exhaustive set of examples; section 34(1) of the Ordinance itself names two grounds, a person who must be fit and proper no longer being so, or consent to entry of domestic premises being revoked or refused. How the two fit together is on the <a href=\"#gl-endings\">Guidelines page</a> and the <a href=\"#p5-losing\">Part 5 page</a>.",
              "逾期遞交將會導致牌照被暫時吊銷及／或撤銷；《牌照指引》亦把未能按時遞交定期申報表，列為關長可撤銷或暫時吊銷牌照的情況之一。該清單只列舉例子，並非詳盡無遺；條例第34(1)條本身列明兩項理由：本須屬適當人選的人不再是適當人選，或住宅處所的進入同意被撤銷或拒絕給予。兩者如何配合，見<a href=\"#gl-endings\">「指引」一頁</a>及<a href=\"#p5-losing\">第5部一頁</a>。"),
             cc(CI("30 May 2025"), LG("7.1(f), 11.2"), "s.34(1)")),
    ))

# ---------------------------------------------------------------- I. other laws
I_ = sec('laws', [("Circulars", "通函"), ("31 Jul 2018 · 23 Jun 2025", "2018年7月31日、2025年6月23日"), ("17 Nov 2025", "2025年11月17日"), ("AMLO Parts 5B, 5C", "《打擊洗錢條例》第5B、5C部")],
         ("Other laws, and side businesses, that reach your counter", "與你的櫃位相關的其他法例及兼營業務"),
    P("Each row is something you might do besides running the money service, or a law outside the AMLO that a circular flagged. Read across for what it requires and since when.",
      "每一行是你在經營金錢服務以外可能做的事，或通函提醒的條例以外法例。橫向閱讀可見其要求及生效日期。")
    + table([th("If you", "如你"), th("What you must do", "你必須"), th("Since", "生效日期"), th("Law and penalty", "法例及罰則")], [
        tr(td("Arrive in Hong Kong through a specified control point carrying currency or bearer negotiable instruments worth more than HK$120,000", "經指明管制站抵港，並攜帶總值超過港幣120,000元的貨幣或不記名可轉讓票據", CI("31 Jul 2018")),
           td("Make a written declaration to a Customs officer, using the Red Channel", "使用紅通道，向海關人員作出書面申報"),
           td("16 Jul 2018", "2018年7月16日"), td("Cap. 629: up to $500,000 and 2 years", "第629章：最高罰款$500,000及監禁2年", cls='pen')),
        tr(td("Arrive any other way, or leave Hong Kong, with that much", "以其他方式抵港或離港，並攜帶上述款額", CI("31 Jul 2018")),
           td("Disclose it when a Customs officer asks, and then declare it in writing", "在海關人員要求時披露，並作出書面申報"),
           td("16 Jul 2018", "2018年7月16日"), td("Cap. 629: up to $500,000 and 2 years", "第629章：最高罰款$500,000及監禁2年", cls='pen')),
        tr(td("Import or export that much in a cargo consignment", "以貨物形式進口或出口上述款額", CI("31 Jul 2018")),
           td("Declare it in advance through the C&amp;ED's Currency and Bearer Negotiable Instruments Declaration System", "預先透過海關的現金類物品申報系統作出申報"),
           td("16 Jul 2018", "2018年7月16日"), td("Cap. 629: up to $500,000 and 2 years", "第629章：最高罰款$500,000及監禁2年", cls='pen')),
        tr(td("Carry that much through a passenger channel, arriving or leaving, and want to clear faster", "經旅客通道抵港或離港時攜帶上述款額，並希望加快清關", CI("23 Jun 2025")),
           td("You may pre-fill the C&amp;ED's online e-form before you travel, get a QR code, and show it to a Customs officer on the spot to make the declaration. The C&amp;ED invites MSOs to use it, which may reduce clearance time on the spot; travellers may use it, so it is optional",
              "可在出發前使用海關的網上電子表格預先填寫資料，獲取二維碼，再在現場向海關人員出示以完成申報。海關誠邀金錢服務經營者使用，以節省現場清關時間；旅客可選擇使用", post=flag()),
           td("23 Jun 2025", "2025年6月23日"), td("Cap. 629 declaration, made by e-form and QR code", "第629章的申報，以電子表格及二維碼作出")),
        tr(td("Change money", "經營貨幣兌換", CI("17 Nov 2025")),
           td("Meet the Money Changers Ordinance's rules on transaction notes and the display of rates, in its Schedules 2 and 3 as amended", "遵守經修訂的《貨幣兌換商條例》附表2及3有關交易單據及展示匯率的法定責任"),
           td("Amended with effect from 24 Aug 2025", "修訂於2025年8月24日生效"), td("Money Changers Ordinance, Cap. 34", "《貨幣兌換商條例》（第34章）")),
        tr(td("Also carry on a precious metals and stones business, in transactions with payments of at least $120,000", "兼營貴金屬及寶石業務，並進行付款總額不少於$120,000的交易", ("s.53ZUE · Sch. 3H · Sch. 3I", "第5C部「未經註冊而進行某些交易屬罪行」的條文 · 附表3H · 附表3I")),
           td("Register with the Commissioner: no person other than a registrant may carry out such a transaction in Hong Kong", "向關長註冊：除註冊人以外，任何人均不得在香港進行這類交易"),
           dash_td(), td("AMLO Part 5C, not covered further in this pack", "《打擊洗錢條例》第5C部，本資料包不再詳述")),
        tr(td("Also carry on a business of providing a VA service, that is, operating a virtual asset exchange", "兼營提供虛擬資產服務的業務，即經營虛擬資產交易所", ("s.53ZRD · s.53ZRK · Sch. 3B", "第5B部「經營虛擬資產服務業務須領牌照」及「申請及批給牌照」的條文 · 附表3B")),
           td("Be licensed by the SFC. Only a licensed provider for the VA service is outside the prohibition, so your money service operator licence does not cover it", "向證監會領取牌照。只有有關虛擬資產服務的持牌提供者不受此禁止所限，因此你的金錢服務經營者牌照並不涵蓋此業務"),
           dash_td(), td("AMLO Part 5B", "《打擊洗錢條例》第5B部")),
        tr(td("Carry out virtual asset transfers for customers", "為客戶進行虛擬資產轉帳", "s.13A, 20(3A) Sch. 2"),
           td("Meet Schedule 2's special requirements for virtual asset transfers and its record-keeping rules: see the <a href=\"#s3-lettered\">Schedule 3 page</a>", "遵守附表2有關虛擬資產轉帳的特別規定及備存紀錄的規定：見<a href=\"#s3-lettered\">附表3一頁</a>"),
           dash_td(), td("Schedule 2, sections 13A and 20(3A)", "附表2第13A及20(3A)條")),
    ], minw=900)
    + traps(
        trap(("Three $120,000 lines, and 'more than' is not 'at or above'", "三條$120,000界線，「超過」不等於「或以上」"), None,
             cc(CI("31 Jul 2018"), "s.3(1)(b) Sch. 2", ("s.53ZUE · Sch. 3H · Sch. 3I", "第5C部「未經註冊而進行某些交易屬罪行」的條文 · 附表3H · 附表3I")),
             vs=[(("Crossing the boundary", "跨境"), ("More than HK$120,000 in currency or bearer negotiable instruments carried or shipped: declare it.", "攜帶或運送的貨幣或不記名可轉讓票據總值超過港幣120,000元：須申報。")),
                 (("Your own CDD", "你的盡職審查"), ("An occasional transaction of $120,000 or more, unless it is a wire transfer or a virtual asset transfer, which have their own $8,000 line.", "非經常交易款額達$120,000或以上即須進行；電傳轉帳及虛擬資產轉帳則另有$8,000的界線。")),
                 (("A precious metals sideline", "兼營貴金屬"), ("Transactions with payments of at least $120,000: only a registrant may carry them out.", "付款總額不少於$120,000的交易：只有註冊人才可進行。"))]),
    ))

CI_NAV = [('dates', 'What took effect when', '生效日期'), ('warnings', 'Risk warnings', '風險警示'),
          ('thirdparty', 'Third-party payments', '第三方支付'), ('tbml', 'Trade-based laundering', '貿易洗錢'),
          ('cdd', 'CDD questions', '盡職審查疑問'),
          ('edd', 'Higher risk and transfers', '高風險與轉帳'), ('returns', 'Periodic returns', '定期申報表'),
          ('laws', 'Other laws', '其他法例')]
CI_BODY = A + B_ + C_ + D_ + F_ + G_ + H_ + I_

# The page footer, used by the ci entry in pack_build.py. It names only the circulars that are
# still current sources, plus the one superseded circular whose five STR filing points are kept.
CI_FOOT = ("Drawn from the C&amp;ED circulars to money service operators dated 31 July 2018, 13 December 2021, 22 November 2023, 17 September 2024, 24 April 2025 (fraudulent websites and social media), 30 May 2025, 23 June 2025 (the e-form for declaring currency and bearer negotiable instruments), 17 November 2025, 20 January 2026, 3 July 2026 (the FATF statements of June 2026) and 16 July 2026 (the FATF consultation on Recommendation 16 guidance), and the FAQ applicable to all money service operators on the C&amp;ED portal, with paragraphs 7.1(f) and 11.2 and the fee schedule of the Licensing Guide; paragraphs 2.2, 2.3, 2.13, 3.2, 4.1.2, 4.1.3, 4.3.1, 4.3.3, 4.4.5, 4.9.15, 4.10.2, 4.15.1, 5.2, 6.16 to 6.18, 8.5, 10.5 and Appendix A of the AML/CFT Guideline; sections 34(1), 53ZRD, 53ZRK and 53ZUE of, and Schedules 2, 3, 3B, 3H and 3I to, the Ordinance; and section 25(4) of the Organized and Serious Crimes Ordinance.",
           "取材自海關致金錢服務經營者的通函（日期為2018年7月31日、2021年12月13日、2023年11月22日、2024年9月17日、2025年4月24日（欺詐網站及社交媒體）、2025年5月30日、2025年6月23日（申報現金類物品的電子表格）、2025年11月17日、2026年1月20日、2026年7月3日（特別組織2026年6月的聲明）及2026年7月16日（特別組織就第16項建議指引的諮詢）），以及海關網站上適用於所有金錢服務經營者的常見問題，並參考《牌照指引》第7.1(f)及11.2段及收費表、《打擊洗錢指引》第2.2、2.3、2.13、3.2、4.1.2、4.1.3、4.3.1、4.3.3、4.4.5、4.9.15、4.10.2、4.15.1、5.2、6.16至6.18、8.5、10.5段及附錄A、條例第34(1)條、第5B部有關虛擬資產服務牌照的條文、第5C部有關貴金屬及寶石交易註冊的條文，以及附表2、3、3B、3H及3I，以及《有組織及嚴重罪行條例》第25(4)條。")
