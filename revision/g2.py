# AML/CFT Guideline Chapter 2: the risk-based approach. The institutional ML/TF risk
# assessment (scope, steps, factors, sources, groups, review, new products) and the
# customer risk assessment (timing, what it decides, framework, records).
# SDD/EDD consequences stay on the Schedule 2 page.
from ui import *
from bl_core import _runs
from gl_fig import LG
from ci_fig import CI
from g2_fig import fig_ira, IRA_KEY, fig_lists, LISTS_KEY, fig_cra, CRA_KEY


def cc(*cs):
    """Join several citations into one."""
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


SAMPLE1 = ("Sample question 1", "參考試題1")
INFER = chip("our inference", "本頁推論")

# ---------------------------------------------------------------- A. two levels
A = sec('rba', ["¶2.1", ("¶2.2 · ¶2.13", "第2.2、2.13段")],
        ("Risk decides how far each control goes: one assessment of your business, one of each customer",
         "風險決定每項管控措施做到甚麼程度：一項評估你的業務，一項評估每名客戶"),
    P("Under a risk-based approach, jurisdictions, competent authorities and MSOs alike are expected to identify, assess and understand the ML/TF risks they are exposed to, then take AML/CFT measures commensurate with them. For you, that means your resources go where the risk is. The Guideline expects you to design and run your AML/CFT policies, procedures and controls this way, and calls the three together your <b>AML/CFT Systems</b>. The approach works at two levels. Read the table across to tell them apart.",
      "在風險為本的方法下，司法管轄區、主管當局及金錢服務經營者均預期要識別、評估和了解本身面對的洗錢／恐怖分子資金籌集風險，繼而採取與有關風險相稱的打擊洗錢／恐怖分子資金籌集措施。對你而言，這表示資源用於風險所在。指引期望你以此方法制訂和執行打擊洗錢／恐怖分子資金籌集政策、程序及管控措施，三者統稱為<b>打擊洗錢／恐怖分子資金籌集制度</b>。這方法在兩個層面運作，橫向閱讀下表即可分辨。")
    + table([th("", ""), th("Institutional ML/TF risk assessment", "機構層面的洗錢／恐怖分子資金籌集風險評估"), th("Customer risk assessment", "客戶風險評估")], [
        tr(rh("What it looks at", "評估對象"),
           td("How, and how far, your business is vulnerable to ML/TF: your customers, the countries they are from or in, the countries you operate in, and your products, services, transactions and delivery channels",
              "你的業務如何受到洗錢／恐怖分子資金籌集的影響及受影響的程度：你的客戶、客戶所屬或所在的國家或司法管轄區、你業務所在的國家或司法管轄區，以及你的產品、服務、交易及交付渠道", "¶2.2"),
           td("The ML/TF risks of one customer, or of a proposed business relationship", "與個別客戶或擬開展的業務關係有關的洗錢／恐怖分子資金籌集風險", "¶2.13")),
        tr(rh("When it is done", "何時進行"),
           td("Every two years, and on trigger events material to your business and risk exposure. A new product, business practice or technology gets its own risk assessment before launch",
              "每兩年一次，以及遇有顯著影響你的業務及所面對風險的觸發事件時。新產品、新經營方法或嶄新科技須在推出前另行進行風險評估", "¶2.9 · ¶2.12"),
           td("At the initial stage of CDD; finalised once the CDD information is in; reviewed and updated from time to time, particularly during ongoing monitoring",
              "在盡職審查程序初期進行；綜合審視盡職審查資料後敲定；其後不時覆核和更新，尤以持續監察時為然", "¶2.13–2.14")),
        tr(rh("What it decides", "決定甚麼"),
           td("The level of overall risk, and the level and type of mitigation. The customer risk assessment framework is designed on its results",
              "整體風險水平，以及減低風險措施的程度和類別。客戶風險評估框架應根據其結果制訂", "¶2.3(b) · ¶2.15"),
           td("The extent of CDD and the level and type of ongoing monitoring. It also supports the decision to enter into, continue or terminate the relationship",
              "盡職審查措施的程度，以及持續監察的程度和類別。它亦支持建立、繼續或終止業務關係的決定", "¶2.13–2.14")),
        tr(rh("The factors", "風險因素"),
           td("Five groups: customer; country; product, service or transaction; delivery or distribution channel; other",
              "五組：客戶；國家；產品、服務或交易；交付或分銷渠道；其他", "¶2.4", post=flag()),
           td("Generally three groups: customer; country; product, service, transaction or delivery channel",
              "一般包含三組：客戶；國家；產品、服務、交易或交付渠道", "¶2.15", post=flag())),
        tr(rh("How elaborate", "繁簡程度"),
           td("Scale and scope commensurate with the nature, size and complexity of your business", "規模和範圍與你的業務性質、規模及複雜程度相稱", "¶2.5"),
           td("Complexity commensurate with the nature and size of your business", "框架的複雜程度與你的業務性質和規模相稱", "¶2.15")),
        tr(rh("Senior management", "高級管理層"),
           td("Approves the results, and the results of every review", "審批評估結果，以及每次覆核的結果", "¶2.3(c) · ¶2.9"),
           td("Chapter 2 sets no approval for the rating itself. Approval to take on or keep a high-risk relationship is an EDD step: see the <a href=\"#s2-sdd-edd\">Schedule 2 page</a>",
              "第2章沒有就評級本身訂明審批。建立或維持高風險業務關係須獲批准，屬更嚴格的盡職審查措施：見<a href=\"#s2-sdd-edd\">附表2一頁</a>", "¶4.9.3", post=flag())),
        tr(rh("Records", "紀錄"),
           td("The risk factors identified and assessed, the information sources taken into account, and your evaluation of your AML/CFT Systems; with mechanisms to provide the assessment to the CCE when required",
              "所識別及評估的風險因素、所考慮的資料來源，以及對打擊洗錢／恐怖分子資金籌集制度的評估；並設有機制應關長要求提供風險評估結果", "¶2.3(e) · ¶2.10"),
           td("Enough to demonstrate to the CCE how you assess a customer's risk, and that the extent of CDD and ongoing monitoring is appropriate to it",
              "足以向關長證明你如何評估客戶的風險，以及基於該風險，所執行的盡職審查措施及持續監察程度是合適的", "¶2.16")),
    ], note=B("The Guideline uses should for both: an MSO should conduct an institutional ML/TF risk assessment, and should assess the ML/TF risks associated with a customer or a proposed business relationship.",
              "指引對兩者均用「應」字：金錢服務經營者應進行機構層面的洗錢／恐怖分子資金籌集風險評估，亦應評估與客戶或擬開展的業務關係有關的洗錢／恐怖分子資金籌集風險。") + ' ' + cite_html(("¶2.2 · ¶2.13", "第2.2、2.13段")),
       minw=820, cls='cmp')
    + traps(
        trap(("Each assessment feeds the other", "兩項評估互相影響"), None, cc("¶2.15", "¶2.4(a)(ii)"),
             vs=[(("Institutional into customer", "由機構層面到客戶層面"),
                  ("The customer risk assessment framework should be designed on the results of the institutional assessment.",
                   "客戶風險評估框架應根據你在機構層面進行洗錢／恐怖分子資金籌集風險評估的結果制訂。")),
                 (("Customer into institutional", "由客戶層面到機構層面"),
                  ("The number and proportion of customers identified as high risk is one of the customer risk factors the institutional assessment weighs.",
                   "識別為高風險的客戶數目及比例，是機構層面的評估須考慮的客戶風險因素之一。"))]),
    ))

# ---------------------------------------------------------------- B. the institutional assessment
B_ = sec('ira', [("¶2.2–2.6", "第2.2至2.6段"), ("¶2.9–2.12", "第2.9至2.12段"), "¶1.6"],
         ("Assessing your own business: five steps, then keep it current", "評估你自己的業務：五個步驟，然後保持評估反映現況"),
    P("Follow the left-hand column down: what you draw on, the first three steps, the records, then the two routes into a review, which loops back to the top. The right-hand column holds the factors you weigh and the duties that sit beside the steps. The five steps are the boxes citing ¶2.3.",
      "沿左欄由上而下：資料來源、首三個步驟、備存紀錄，然後是引致覆核的兩條途徑，覆核後回到頂部。右欄是須考慮的因素，以及與步驟並行的責任。五個步驟即引用第2.3段的方格。")
    + fig(fig_ira, None, IRA_KEY)
    + h3("How elaborate the assessment needs to be", "風險評估需要多精密")
    + table([th("Your business", "你的業務"), th("What the Guideline says", "指引的說法")], [
        tr(td("Smaller or less complex: for example a very limited range of products and services, or customers with a homogeneous risk profile",
              "規模較小或複雜性較低：例如所提供的產品和服務種類非常有限，或客戶的風險狀況相若", "¶2.5"),
           td("A simpler risk assessment approach <b>might suffice</b>", "較為簡單的風險評估方法<b>可能已經足夠</b>", post=flag())),
        tr(td("More varied and complex products and services, or customers with more diverse risk profiles",
              "產品和服務較為多樣及複雜，或客戶的風險狀況差異較大", "¶2.5"),
           td("A more sophisticated risk assessment process <b>will be required</b>", "<b>須</b>進行較為精密的風險評估程序")),
    ], note=B("Either way, the scale and scope of the assessment should be commensurate with the nature, size and complexity of the business.",
              "無論如何，風險評估的規模和範圍應與業務的性質、規模及複雜程度相稱。") + ' ' + cite_html("¶2.5"), minw=680)
    + traps(
        trap(("Four places where Chapter 2 gives you room", "第2章給予你彈性的四處地方"),
             ("Chapter 2 is written in should, which is mandatory (see the <a href=\"#g1-status\">Chapter 1 page</a>). The chapter gives you room in four places, and uses softer words when it does. Its lists of factors, information sources and trigger events are also examples, not closed lists: they come with \"for example\" or \"may include\".",
              "第2章用「應」字，屬強制規定（見<a href=\"#g1-status\">第1章一頁</a>）。本章在以下四處給予你較大彈性，並以較寬鬆的字眼表達。本章所列的風險因素、資料來源及觸發事件亦屬例子，並非完整清單：指引以「例如」、「可能包括」或「可包括」引出。"),
             cc("¶1.6", "¶2.4", "¶2.5", "¶2.6", "¶2.8", "¶2.9", "¶2.13", "fn 2"),
             vs=[(("Might suffice", "可能已經足夠"), ("A simpler assessment, for a smaller or less complex business.", "業務規模較小或複雜性較低時，較簡單的評估方法。")),
                 (("May rely", "可依賴"), ("On a group-wide or regional assessment, if it reflects your local risks.", "集團或地區層面的評估，前提是該評估反映你在本地的風險。")),
                 (("May be simplified", "可簡化"), ("CDD, where a customer's risks are lower.", "客戶風險較低時的盡職審查。")),
                 (("May refer", "可參考"), ("To the FATF's 2016 guidance for money or value transfer services, for risk indicators.", "特別組織2016年有關金錢或價值轉帳服務的指引，以了解風險指標。"))]),
        trap(("Senior management approves twice", "高級管理層須審批兩次"), None, cc("¶2.3(c)", "¶2.9"),
             vs=[(("The assessment", "評估"), ("Approval of the risk assessment results is one of the five steps.", "由高級管理層審批風險評估結果，是五個步驟之一。")),
                 (("Each review", "每次覆核"), ("The results of every review are documented and approved by senior management too.", "每次覆核的結果亦須記錄在案，並由高級管理層審批。"))]),
    ))

# ---------------------------------------------------------------- C. the factors
def tdf(*parts):
    """A table cell whose flag() sits right after the confusable item: parts are (en, tc) pairs,
    with the flag placed after every pair except the last."""
    body = flag().join(B(en, tc) for en, tc in parts)
    return f'<td>{body}</td>'


FACTORS = table([th("Factor group", "因素組別"), th("The examples the Guideline gives", "指引所舉的例子")], [
    tr(rh("(a) Customer risk factors", "(a) 客戶風險因素", "¶2.4(a)"),
       tdf(("(i) Your target market and customer segments<br>(ii) The number and proportion of customers identified as high risk",
            "(i) 目標市場及客戶類別<br>(ii) 識別為高風險的客戶數目及比例"), ("", ""))),
    tr(rh("(b) Country risk factors", "(b) 國家風險因素", "¶2.4(b)"),
       td("The countries or jurisdictions you are exposed to, through your own activities or your customers', especially those that credible sources identify as more vulnerable because of contextual and other risk factors such as:<br>(i) the prevalence of corruption, organised crime or TF<br>(ii) the general level and quality of the jurisdiction's law enforcement efforts on AML/CFT<br>(iii) the effectiveness of AML/CFT regulatory regimes and controls<br>(iv) the transparency of beneficial ownership",
          "你所面對的國家或司法管轄區（不論是透過本身的活動抑或客戶的活動），尤其是由各可靠消息來源識別為因環境性及其他風險因素而具有較大漏洞的國家或司法管轄區，例如：<br>(i) 貪污、有組織罪行或恐怖分子資金籌集的普遍程度<br>(ii) 該司法管轄區就打擊洗錢／恐怖分子資金籌集而採取的執法工作的一般水平及質素<br>(iii) 打擊洗錢／恐怖分子資金籌集監管制度和管控措施的成效<br>(iv) 實益擁有權的透明度")),
    tr(rh("(c) Product, service or transaction risk factors", "(c) 產品、服務或交易風險因素", "¶2.4(c)"),
       tdf(("(i) The nature, scale, diversity and complexity of your business<br>(ii) The characteristics of the products and services you offer, and how far they are vulnerable to ML/TF abuse, for example the extent of occasional transactions<br>(iii) Whether the volume and size of your transactions are in line with your usual activity and your customers' profile<br>(iv) The extent to which you use technology, and how far these channels are vulnerable to ML/TF abuse",
            "(i) 業務的性質、規模、多元程度及複雜程度<br>(ii) 所提供產品及服務的特點，以及它們所面對的洗錢／恐怖分子資金籌集風險程度，例如進行非經常交易的程度<br>(iii) 交易量及交易規模是否與你的慣常活動及客戶概況一致<br>(iv) 你運用科技的程度，以及此等渠道所面對的洗錢／恐怖分子資金籌集風險程度"),
           ("(v) Whether products or services may inherently favour anonymity", "(v) 產品或服務是否本身可能有利於以匿名行事"))),
    tr(rh("(d) Delivery or distribution channel risk factors", "(d) 交付或分銷渠道風險因素", "¶2.4(d)"),
       tdf(("The channels through which you distribute your products or services, including:<br>(i) how far you deal with customers directly, and how far you rely, or are allowed to rely, on a third party to conduct CDD or other AML/CFT obligations",
            "你藉以分銷產品或服務的渠道，包括：<br>(i) 你直接與客戶往來的程度；你依賴（或獲准依賴）第三者進行盡職審查或履行其他打擊洗錢／恐怖分子資金籌集責任的程度"),
           ("(ii) how far agent or counterpart networks are used<br>(iii) the complexity of the payment chain, and of the settlement systems used among operators in it",
            "(ii) 代理人或交易對手網絡的使用程度<br>(iii) 支付鏈的複雜程度，以及支付鏈中各經營者之間使用的交收系統的複雜程度"))),
    tr(rh("(e) Other risk factors", "(e) 其他風險因素", "¶2.4(e)"),
       td("(i) The nature, scale and quality of the ML/TF risk management resources available, including appropriately qualified staff with access to ongoing AML/CFT training and development<br>(ii) Compliance and regulatory findings<br>(iii) The results of internal or external audits",
          "(i) 可供運用的洗錢／恐怖分子資金籌集風險管理資源的性質、規模及質素，包括可在打擊洗錢／恐怖分子資金籌集方面持續接受培訓及進修並具備合適資格的員工<br>(ii) 合規及監管的發現<br>(iii) 內部或外部審計的結果")),
], note=B("You should consider these factors holistically.", "你應全面考慮這些因素。") + ' ' + cite_html("¶2.4"),
   minw=760)

TERMS = table([th("Term", "詞語"), th("What it means", "意思")], [
    tr(rh("Credible sources", "可靠消息來源", "¶2.4(b) fn 3"),
       td("Information produced by reputable and universally recognised international organisations and other bodies that make it publicly and widely available. Besides the FATF and FATF-style regional bodies, they may include, but are not limited to, supra-national or international bodies such as the International Monetary Fund, the World Bank and the Egmont Group of Financial Intelligence Units, and relevant national government bodies and non-government organisations",
          "由有良好聲譽和廣為人知的國際組織及其他組織所提供及廣泛流傳的資訊。除特別組織及執行與特別組織相類似職能的地區組織以外，亦可包括（但不限於）超國家或國際組織，例如國際貨幣基金組織、世界銀行及埃格蒙特金融情報組織，以及有關的政府組織和非政府機構")),
    tr(rh("Transparency of beneficial ownership", "實益擁有權的透明度", "¶2.4(b)(iv) fn 4"),
       td("For example, whether the competent authorities of the country or jurisdiction can obtain or access adequate, accurate and timely information on the beneficial ownership of legal persons and legal arrangements, in a timely fashion",
          "舉例來說，國家或司法管轄區的主管當局可否充分、準確和適時取得或查閱法人及法律安排的實益擁有權資料")),
], minw=720)

C_ = sec('factors', [("¶2.2 · ¶2.4", "第2.2、2.4段"), ("fn 3–4", "註3至4"), "¶2.15", ("Sample question 1", "參考試題1")],
         ("What the institutional assessment weighs, and what it does not", "機構層面的洗錢／恐怖分子資金籌集風險評估考慮甚麼，以及不考慮甚麼"),
    P("Chapter 2 has three lists that look alike. Read the figure across: each line pairs items that deal with the same thing, so you can keep the four areas, the five factor groups and the three customer factor groups apart. The table under it gives every factor in the five groups.",
      "第2章有三份相似的清單。橫向閱讀下圖：每條連線把處理同一事項的項目配對，讓你分清四個範疇、五組因素及三組客戶因素。圖下的表列出五組中的每一項因素。")
    + fig(fig_lists, ("The lines pair items by name; the Guideline does not draw them. The fifth group, other risk factors, has no counterpart in the customer framework's list.",
                      "連線按名稱配對項目，並非指引本身所繪。第五組「其他風險因素」在客戶框架的清單中沒有對應組別。"), LISTS_KEY)
    + FACTORS
    + h3("Two terms the country factors depend on", "與國家風險因素有關的兩個詞語")
    + TERMS
    + traps(
        trap(("Profitability is not on the list", "盈利能力不在清單上"), None, cc("¶2.4(a)(i), (c)(i), (d)", SAMPLE1),
             vs=[(("On the list", "在清單上"),
                  ("Your target market and customer segments; the nature, scale, diversity and complexity of your business; your delivery channels.",
                   "目標市場及客戶類別；業務的性質、規模、多元程度及複雜程度；交付渠道。")),
                 (("Not on the list", "不在清單上"),
                  ("The profitability of your business: the wrong option in the official sample question, whose answer is the other three.",
                   "業務的盈利能力：官方參考試題中的錯誤選項，答案是其餘三項。"))]),
        trap(("Three items that sit in an unexpected group", "三個容易放錯組別的項目"), None, "¶2.4(c)(iv), (d)(i), (e)",
             vs=[(("Relying on a third party for CDD", "依賴第三者進行盡職審查"),
                  ("A delivery or distribution channel factor, not a customer factor.", "屬交付或分銷渠道風險因素，而非客戶風險因素。")),
                 (("Your use of technology", "你運用科技的程度"),
                  ("A product, service or transaction factor, even though the Guideline calls these channels.", "屬產品、服務或交易風險因素，雖然指引稱之為「渠道」。")),
                 (("Staff, audits and regulatory findings", "員工、審計及監管發現"),
                  ("The fifth group, other risk factors.", "屬第五組「其他風險因素」。"))]),
        trap(("Two sets of countries, not one", "兩類國家，而非一類"), None, "¶2.2(b)–(c) · ¶2.4(b)",
             vs=[(("Where your customers are from or in", "客戶所屬或所在的國家"),
                  ("One of the four areas the assessment covers.", "評估涵蓋的四個範疇之一。")),
                 (("Where you have operations", "你業務所在的國家"),
                  ("A separate area. The country factors count exposure through your own activities as well as your customers'.",
                   "另一個範疇。國家風險因素同時計算透過你本身的活動及客戶的活動而面對的風險。"))]),
    ))

# ---------------------------------------------------------------- D. groups
D_ = sec('group', ["¶2.7–2.8", "s.22 Sch. 2"],
         ("Part of a group, or with branches and subsidiaries", "屬集團成員，或設有分行及附屬企業"),
    P("Find your structure in the left column. The first two rows are the Guideline's own; the last two, marked as our inference, follow from them.",
      "在左欄找出你的架構。首兩行是指引本身的規定；後兩行標明為本頁推論，由此推得。")
    + table([th("Your structure", "你的架構"), th("What the Guideline expects", "指引的期望")], [
        tr(td("Incorporated in Hong Kong, with branches or subsidiaries, including any outside Hong Kong",
              "在本地成立為法團，並設有分行或附屬企業（位於香港以外者亦計算在內）", "¶2.7"),
           td("Perform a group-wide ML/TF risk assessment", "進行集團層面的洗錢／恐怖分子資金籌集風險評估")),
        tr(td("Part of a financial group that has already carried out a group-wide or regional ML/TF risk assessment",
              "屬某金融集團的成員，而集團或地區層面已進行洗錢／恐怖分子資金籌集風險評估", "¶2.8"),
           td("You <b>may</b> refer to or rely on it, for your own institutional assessment and for a group-wide one, <b>provided</b> it adequately reflects the ML/TF risks posed to you in the local context",
              "你<b>可</b>參考或依賴有關評估，以施行本身在機構層面及集團層面的洗錢／恐怖分子資金籌集風險評估，<b>惟</b>有關評估須充分反映你在本地層面所面對的洗錢／恐怖分子資金籌集風險", post=flag())),
        tr(td("That group assessment does not adequately reflect your local risks", "該集團評估未能充分反映你在本地面對的風險", "¶2.8"),
           td("The condition for relying on it is not met, so the institutional assessment remains yours to carry out", "未符合依賴該評估的條件，因此機構層面的評估仍須由你自行進行", "¶2.2 · ¶2.8",
              pre=INFER + ' ')),
        tr(td("A stand-alone MSO, with no branches, no subsidiaries and no group", "獨立經營，沒有分行、附屬企業或所屬集團", "¶2.2 · ¶2.7"),
           td("Your own institutional assessment only; the group-wide assessment applies to MSOs with branches or subsidiaries", "只須進行本身機構層面的評估；集團層面的評估適用於設有分行或附屬企業的經營者", "¶2.2 · ¶2.7",
              pre=INFER + ' ')),
    ], minw=720)
    + traps(
        trap(("A group-wide assessment is not the overseas-branch duty", "集團層面評估不等於海外分行的責任"), None, cc("¶2.7", "s.22 Sch. 2"),
             vs=[(("Group-wide risk assessment", "集團層面風險評估"),
                  ("The Guideline: a locally-incorporated MSO with branches or subsidiaries, in or outside Hong Kong, assesses ML/TF risk across the group.",
                   "指引：在本地成立為法團並設有分行或附屬企業（不論是否位於香港）的經營者，須在集團層面評估洗錢／恐怖分子資金籌集風險。")),
                 (("Branches and subsidiaries outside Hong Kong", "香港以外的分行及附屬企業"),
                  ("The Ordinance: a financial institution incorporated in Hong Kong, or a re-domiciled entity, must ensure that its branches, and its subsidiary undertakings carrying on the same business as a financial institution outside Hong Kong, have procedures to comply with requirements similar to Parts 2 and 3 of Schedule 2, to the extent the local law permits. See the <a href=\"#s2-systems\">Schedule 2 page</a>.",
                   "條例：在香港成立為法團或屬經遷冊實體的金融機構，須確保其分行，以及在香港以外地方經營與金融機構相同業務的附屬企業設有程序，確保與附表2第2及3部相類似的規定在該地方法律准許的範圍內獲遵守。見<a href=\"#s2-systems\">附表2一頁</a>。"))]),
    ))

# ---------------------------------------------------------------- E. keeping it current
E_ = sec('review', [("¶2.3(d) · ¶2.9", "第2.3(d)、2.9段"), ("¶2.11–2.12", "第2.11至2.12段"), "¶1.3", "¶5.3"],
         ("Keeping it current: every two years, on trigger events, and before any launch", "保持評估反映現況：每兩年一次、遇觸發事件時，以及推出新事物前"),
    P("Find what has happened in the left column. The first two rows send you back to review the institutional assessment; the last three call for a separate risk assessment of the new thing, done before launch.",
      "在左欄找出發生了甚麼。首兩行須覆核機構層面的洗錢／恐怖分子資金籌集風險評估；最後三行須在推出前，就新事物另行進行風險評估。")
    + table([th("What has happened", "發生了甚麼"), th("What the Guideline expects", "指引的期望")], [
        tr(td("Two years have passed since the last assessment", "距上次評估已兩年", "¶2.9"),
           td("Conduct the assessment again", "再次進行評估")),
        tr(td("An event material to your business and risk exposure. The Guideline's examples: a significant breach of your AML/CFT Systems; the acquisition of new customer segments or delivery channels; significant changes of your operational processes, target customers and business counterparts",
              "顯著影響你的業務及所面對風險的事件。指引所舉的例子：嚴重違反你的打擊洗錢／恐怖分子資金籌集制度；收購新的客戶類別或交付渠道；你的營運程序、目標客戶及交易對手有重大改變", "¶2.9"),
           td("A trigger event: review the assessment", "屬觸發事件：覆核評估")),
        tr(td("You launch new products and services", "你推出新的產品及服務", "¶2.9 · ¶2.11(a) · ¶2.12"),
           td("Both duties. Assess the new product's ML/TF risks before launch and take measures to manage and mitigate them; the launch is also a trigger event for reviewing the institutional assessment",
              "兩項責任同時適用。推出前先評估新產品的洗錢／恐怖分子資金籌集風險，並採取措施管理和減低風險；推出新產品亦屬觸發事件，須覆核機構層面的評估", post=flag())),
        tr(td("You develop a new business practice, including a new delivery mechanism", "你開發新經營方法，包括新的交付機制", "¶2.11(a) · ¶2.12"),
           td("Identify and assess its ML/TF risks before launch, and take appropriate measures to manage and mitigate them",
              "推出前先識別和評估其洗錢／恐怖分子資金籌集風險，並採取適當措施管理和減低風險")),
        tr(td("You start using a new or developing technology, for a new product or an existing one", "你開始使用嶄新或開發中的科技，不論用於新產品或既有產品", "¶2.11(b) · ¶2.12"),
           td("The same: assess before you start using it, then manage and mitigate", "同上：開始使用前先評估，然後管理和減低風險", post=flag())),
    ], note=B("The trigger-event list \"may include\" its examples, so it is open. On our reading, a new business practice or technology that is material to your business and risk exposure can be a trigger event too; the list itself names the acquisition of new delivery channels. After every review, document the results and have senior management approve them.",
              "觸發事件清單以「可包括」引出例子，屬開放清單。按本頁理解，顯著影響你的業務及所面對風險的新經營方法或新科技，亦可屬觸發事件；清單本身亦列明收購新的交付渠道。每次覆核後，須把結果記錄在案，並由高級管理層審批。") + ' ' + cite_html("¶2.9"),
       minw=760)
    + numreq([
        (("every 2 years", "每兩年一次"),
         ("Conduct the institutional ML/TF risk assessment again, and document and approve the results", "再次進行機構層面的洗錢／恐怖分子資金籌集風險評估，並記錄及審批結果"),
         ("Always, in addition to reviews on trigger events", "任何情況下均適用，另加遇觸發事件時的覆核"),
         ("A breach of the Guideline: you may face disciplinary and other action under the AMLO, and it may also reflect adversely on the fitness and properness of your sole proprietor, partners, directors and ultimate owner, where applicable (¶1.3; see the <a href=\"#g1-status\">Chapter 1 page</a>)",
          "未有遵守指引：或會面對根據打擊洗錢條例採取的紀律行動及其他行動；不遵從指引，將對獨資經營者、合夥人、董事和最終擁有人（如適用）作為適當人選帶有負面影響（第1.3段；見<a href=\"#g1-status\">第1章一頁</a>）"),
         "¶2.3(d) · ¶2.9"),
        (("before launch", "推出前"),
         ("Assess the ML/TF risks, and take appropriate measures to manage and mitigate them", "評估洗錢／恐怖分子資金籌集風險，並採取適當措施管理和減低風險"),
         ("New products; new business practices, including new delivery mechanisms; new or developing technologies for new or existing products", "新產品；新經營方法，包括新的交付機制；新產品及既有產品使用的嶄新或開發中科技"),
         ("The same as any breach of the Guideline (¶1.3). A launch of new products and services is also a trigger event for reviewing the whole assessment", "與任何未有遵守指引的情況相同（第1.3段）。推出新的產品及服務亦屬觸發事件，須覆核整體評估"),
         "¶2.9 · ¶2.11–2.12"),
    ])
    + traps(
        trap(("Three review periods not to mix up", "三個容易混淆的周期"), None, cc("¶2.9", "¶5.3", LG("2.10")),
             vs=[(("Institutional assessment", "機構層面的評估"), ("Every two years, and on trigger events.", "每兩年一次，以及遇觸發事件時。")),
                 (("High-risk customers", "高風險客戶"), ("A review of their CDD information at least once a year, more often if you consider it necessary (<a href=\"#s2-sdd-edd\">Schedule 2 page</a>).", "最少每年覆核一次其盡職審查資料，如認為有需要則更頻密（見<a href=\"#s2-sdd-edd\">附表2一頁</a>）。")),
                 (("Your licence", "你的牌照"), ("Normally valid for two years, then renewed (<a href=\"#gl-route\">Licensing page</a>).", "有效期一般為兩年，其後須續期（見<a href=\"#gl-route\">牌照一頁</a>）。"))]),
        trap(("New technology on an old product still needs assessing", "既有產品使用嶄新科技亦須評估"),
             ("The duty covers new or developing technologies used for both new and pre-existing products, not only brand-new products.",
              "此責任涵蓋新產品及既有產品所使用的嶄新或開發中科技，而不限於全新產品。"), "¶2.11(b)"),
    ))

# ---------------------------------------------------------------- F. customer risk assessment
F_ = sec('cra', [("¶2.13–2.16", "第2.13至2.16段"), ("fn 5–8", "註5至8"), ("Circular 22 Nov 2023", "2023年11月22日通函")],
         ("Rating each customer: when it is done and what it decides", "為每名客戶評估風險：何時進行及決定甚麼"),
    P("Start at the top with the customer in front of you and follow the arrows down. The question has three answers, and all three lead on to the finalised assessment. The records box on the right applies beside it, and the line up the left edge is the review, which returns to the finalised assessment.",
      "由頂部面前的客戶開始，沿箭頭向下。問題有三個答案，三者均通往敲定評估。右邊的紀錄方格與之並行適用；沿左邊向上的線是覆核，會回到敲定評估的一步。")
    + fig(fig_cra, ("How CDD is carried out at each level of risk is left to Chapter 4 and the <a href=\"#s2-sdd-edd\">Schedule 2 page</a>; this figure shows only what Chapter 2 decides.",
                    "在不同風險水平下如何執行盡職審查，載於第4章及<a href=\"#s2-sdd-edd\">附表2一頁</a>；本圖只顯示第2章所決定的事項。"), CRA_KEY)
    + table([th("The question", "問題"), th("Chapter 2's answer", "第2章的答案")], [
        tr(rh("Where are the factors spelled out?", "風險因素的詳情在哪裏？", "¶2.15 fn 8"),
           td("Chapter 2 names only the three groups. Further guidance is in Chapter 4, and the <a href=\"#s2-sdd-edd\">Schedule 2 page</a> lists the lower- and higher-risk factors it names",
              "第2章只列出三組因素。進一步導引載於第4章；第4章列出的較低及較高風險因素見<a href=\"#s2-sdd-edd\">附表2一頁</a>")),
        tr(rh("What else is the rating for?", "評估客戶風險還有甚麼作用？", "¶2.13"),
           td("It helps you tell apart the risks of individual customers and business relationships, and apply CDD and risk-mitigating measures that are appropriate and proportionate",
              "評估風險有助你分辨個別客戶與業務關係所涉的風險，並採取適當及相稱的盡職審查及減低風險措施")),
        tr(rh("How hard should you be on a genuine customer?", "對真正的客戶應嚴格到甚麼程度？", "fn 6"),
           td("Take a balanced and common-sense approach: the risk assessment and CDD should not put an unreasonable barrier in the way of bona fide businesses and individuals seeking your services",
              "應採取均衡而合乎常理的原則，不應無理妨礙正當的業務及個人接受你提供的服務", post=flag())),
        tr(rh("What should the records show?", "紀錄應顯示甚麼？", "¶2.16 · s.20(1)(b)(ii) Sch. 2"),
           td("Among other things, (a) how you assess the customer's ML/TF risks, and (b) that the extent of CDD and ongoing monitoring is appropriate to those risks. The Guideline's margin ties this to the customer records duty in Schedule 2; retention periods are in the <a href=\"#s2-records\">records section</a>",
              "其中包括：(a)你如何評估客戶的洗錢／恐怖分子資金籌集風險；及(b)基於該風險，所執行的盡職審查措施及持續監察程度是合適的。指引旁註把此要求連繫至附表2就每名客戶備存紀錄的責任；保存期見<a href=\"#s2-records\">紀錄一節</a>")),
        tr(rh("What has the C&amp;ED found going wrong?", "海關發現甚麼問題？", CI("22 Nov 2023")),
           td("Its supervisory findings on customer risk assessment, and what it expects instead, are on the <a href=\"#ci-cdd\">Circulars page</a>",
              "海關在監管工作中就客戶風險評估的發現，以及預期的規管標準，見<a href=\"#ci-cdd\">通函一頁</a>")),
    ], minw=760)
    + traps(
        trap(("Initial, then final: two moments, two decisions", "初步與敲定：兩個時刻，兩項決定"), None, "¶2.13–2.14",
             vs=[(("At the initial stage of CDD", "盡職審查程序初期"),
                  ("Decides the extent of CDD: how much information, of what type, and how thoroughly it is verified.", "決定盡職審查措施的程度：索取多少、哪類資料，以及以多嚴謹的方式核實。")),
                 (("Once the CDD information is in", "取得盡職審查資料後"),
                  ("Finalised from a holistic view. Decides the level and type of ongoing monitoring, and supports the decision to enter into, continue or terminate the relationship.",
                   "綜合審視後敲定。決定持續監察的程度和類別，並支持建立、繼續或終止業務關係的決定。"))]),
        trap(("Higher risk: should increase. Lower risk: may simplify", "風險較高：需加強；風險較低：可簡化"),
             ("Where risk is higher, the amount and type of information and the extent of verification should be increased. Where it is lower, CDD may be simplified: a permission, not a duty. Either way all the CDD measures and ongoing monitoring still apply, outside the situations Chapter 4 specifies, as the <a href=\"#s2-map\">CDD map</a> shows.",
              "風險較高時，便需索取數量及類別更多的資料，並以更嚴謹方式核實；風險較低時，可簡化審查程序：這是准許，而非責任。無論如何，除第4章指明的情況外，仍須執行所有盡職審查措施並持續監察，見<a href=\"#s2-map\">盡職審查流程圖</a>。"),
             cc("¶2.13", "fn 5")),
        trap(("\"Customer risk profile\" is the same thing", "「客戶風險狀況」是同一回事"),
             ("The Guideline notes that the customer risk assessment is sometimes called the customer risk profile, so a question using either term is asking about the same rating.",
              "指引指出，客戶風險評估有時亦稱為「客戶風險狀況」，因此題目用任何一個詞語，所指的都是同一項評級。"), "fn 7"),
    ))

G2_NAV = [('rba', 'Two levels of risk', '兩個層面的風險'), ('ira', 'Assessing your business', '評估你的業務'),
          ('factors', 'The risk factors', '風險因素'), ('group', 'Groups and branches', '集團與分行'),
          ('review', 'Keeping it current', '保持反映現況'), ('cra', 'Rating each customer', '為客戶評估風險')]
G2_BODY = A + B_ + C_ + D_ + E_ + F_

G2_META = dict(
    tab=("2", "2"),
    short=("Guideline Ch. 2 · Risk-based approach", "指引第2章 · 風險為本的方法"),
    eyebrow=("AML/CFT Guideline · Chapter 2 · Modules 5 and 6", "《打擊洗錢指引》第2章 · 單元五及六"),
    title=("The Risk-based Approach", "風險為本的方法"),
    lede=("Chapter 2 decides where your AML/CFT effort goes. You assess the ML/TF risk of your whole business, keep that assessment current and approved by senior management, and build on it the framework that rates each customer. Each customer's rating then sets how far CDD goes and how closely you monitor.",
          "第2章決定你的打擊洗錢／恐怖分子資金籌集工作應放在哪裏。你須評估整體業務的洗錢／恐怖分子資金籌集風險，確保評估反映現況並經高級管理層審批，再以此為基礎制訂為每名客戶評估風險的框架。每名客戶的評級其後決定盡職審查做到甚麼程度，以及監察有多密切。"),
    foot=("Drawn from Chapter 2 of the Customs and Excise Department's Guideline on Anti-Money Laundering and Counter-Financing of Terrorism (For Money Service Operators), June 2023, with paragraphs 1.3, 1.6, 4.9.3 and 5.3; sections 20 and 22 of Schedule 2 to the AMLO; the C&amp;ED circular of 22 November 2023; paragraph 2.10 of the Licensing Guide; and official sample question 1 of 12 May 2021.",
          "取材自香港海關《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》（2023年6月）第2章，並參考第1.3、1.6、4.9.3及5.3段；《打擊洗錢條例》附表2第20及22條；海關2023年11月22日的通函；《牌照指引》第2.10段；以及2021年5月12日官方參考試題第1題。"),
)
