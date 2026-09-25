# AML/CFT Guideline Chapter 5, ongoing monitoring: what the Guideline adds to the
# Schedule 2 loop (review policies, the monitoring system and its checks, the
# risk-based extent, and handling an unusual transaction, tipping off in CDD included).
# The statutory loop itself is on the Schedule 2 page (#s2-monitoring).
from ui import *
from g5_fig import cc, FAQ, fig_system, SYSTEM_KEY, fig_unusual, UNUSUAL_KEY


def dash_td():
    return '<td class="faint">—</td>'


S2 = ("Schedule 2 page", "附表2一頁")


def link(anchor, pair):
    return tuple(f'<a href="#{anchor}">{x}</a>' for x in pair)


def only(lang, block):
    """A callout shown only in one language's view (and in the combined view), for a point
    that only that language's text makes. pack_css.css hides .only-en in the Chinese view
    and .only-tc in the English view."""
    return block.replace('<div class="trap">', f'<div class="trap only-{lang}">', 1)


L_MON = link("s2-monitoring", S2)
L_SDD = link("s2-sdd-edd", S2)
L_PEP = link("s2-pep", ("PEP section", "政治人物一節"))
L_RELY = link("s2-rely", S2)

# ---------------------------------------------------------------- A. keeping the file current
A = sec('files', ["¶5.2–5.3", "fn 53", FAQ(22)],
        ("Keeping the customer file current, and what your review policy should settle", "保持客戶資料反映現況，以及覆核政策應訂明的事項"),
    P(f"Find your situation in the left column. The middle column is what you should do; the right-hand column is what your policies and procedures should set out. The monitoring loop as a whole is drawn on the {L_MON[0]}.",
      f"在左欄找出你的情況。中欄是你應怎樣做；右欄是你的政策及程序應訂明的事項。整個持續監察循環見{L_MON[1]}。")
    + table([th("The situation", "情況"), th("What you should do", "你應怎樣做"),
             th("What your policies and procedures should set out", "政策及程序應訂明甚麼")], [
        tr(rh("A periodic review falls due", "定期覆核到期", "¶5.2"),
           td("Review the customer's existing CDD records, so that the documents, data and information stay up to date and relevant",
              "覆核客戶現存的盡職審查紀錄，確保有關文件、數據及資料反映現況及仍屬相關", "¶5.2"),
           td(f"How often periodic reviews take place. The Guideline sets the floor: a high-risk customer should be reviewed at least once a year, or more often if you consider it necessary. See the {L_MON[0]}",
              f"定期覆核的頻密程度。指引訂明的最低要求：高風險客戶最低限度應每年覆核一次，如認為有需要則更頻密。見{L_MON[1]}", "¶5.2–5.3")),
        tr(rh("A trigger event occurs", "出現觸發事件", "¶5.2"),
           td("Review the records on the event. You should review on a regular basis, on trigger events, or both: the Guideline says &lsquo;and/or&rsquo;",
              "遇有觸發事件時覆核紀錄。應定期及／或遇有觸發事件時覆核", "¶5.2"),
           td("What counts as a trigger event", "何謂觸發事件", "¶5.2")),
        tr(rh("A customer has gone dormant", "客戶成為不動客戶", "fn 53"),
           td(f"When a dormant customer's records are reviewed is on the {L_MON[0]}",
              f"不動客戶的紀錄何時覆核，見{L_MON[1]}", "fn 53"),
           td("A clear definition of what counts as a dormant customer", "清晰界定何謂不動客戶", "fn 53")),
    ], note=B(f"Whether you may use an intermediary for CDD at all, and on what terms, is on the {L_RELY[0]}.",
              f"可否藉中介人執行盡職審查及有關條件，見{L_RELY[1]}。"), minw=820)
    + traps(
        trap(("An intermediary can fetch documents, but cannot do your monitoring", "中介人可代收文件，但不可代你監察"), None, cc(FAQ(22), "s.18 Sch. 2"),
             vs=[(("It may", "可以"),
                  ("Collect further documents, data and information for you, and provide or coordinate updates to them, to help keep your CDD records up to date and relevant.",
                   "代你收集進一步的文件、數據和資料，及提供或協調相關更新，以協助確保你的盡職審查紀錄反映現況及仍屬相關。")),
                 (("It may not", "不可以"),
                  ("Be relied on for ongoing monitoring, neither ongoing CDD nor transaction monitoring. Schedule 2 lets an intermediary carry out only the CDD measures in its section 2.",
                   "被依賴進行持續監察，包括持續的客戶盡職審查及交易監察。附表2只容許藉中介人執行其第2條所載的客戶盡職審查措施。"))]),
    ))

# ---------------------------------------------------------------- B. the monitoring system
TH_BIZ = ('<th style="width:50%">' + B("About your business: the system's design, degree of automation and sophistication should be developed having regard to these",
                     "關於你的業務：系統的設計、自動化程度及精密程度應適當地因應這些因素開發") + cite_html("¶5.4") + '</th>')
TH_TX = ('<th style="width:50%">' + B("About the transactions: take these characteristics into account in the design, parameters and thresholds included. The list is what they &lsquo;may include&rsquo;, not a closed one",
                    "關於交易：設計系統（包括設定參數及門檻）時應顧及這些特徵。清單列出的是交易「可能」具有的特徵，並非完整清單")
         + flag() + cite_html("¶5.7") + '</th>')
B_ = sec('system', ["¶5.4–5.8", "s.19(3) Sch. 2", FAQ(23)],
         ("Building a monitoring system that fits your business, and checking it", "建立切合業務的交易監察系統，並加以查核"),
    P("The upper frame is what the system should do; the lower frame is the two checks on it. The arrows show what each check covers: validation is of the parameters and thresholds, while the regular review covers the whole system.",
      "上框是系統應能做到的事；下框是對系統的兩項查核。箭嘴顯示每項查核的對象：驗證針對參數及門檻，定期覆核則涵蓋整個系統。")
    + fig(fig_system, ("The Guideline hangs this on section 19(3) of Schedule 2: establish and maintain effective procedures for each kind of customer, business relationship, product and transaction. The FAQ answer on who may validate is also in the <a href=\"#ci-edd\">FAQ table on the Circulars page</a>.",
                        "指引把這些要求連繫至附表2第19(3)條：須就每種類別的客戶、業務關係、產品及交易，設立及維持有效措施。誰可進行獨立驗證的常見問題答案，亦見<a href=\"#ci-edd\">通函一頁的常見問題表</a>。"), SYSTEM_KEY)
    + h3("Two lists of five: one about your business, one about the transactions", "兩份五項清單：一份關於你的業務，一份關於交易")
    + table([TH_BIZ, TH_TX], [
        tr(td("The size and complexity of your business", "業務的規模及複雜程度", "¶5.4(a)"),
           td("The nature and type of transactions, such as abnormal size or frequency", "交易性質及類別，例如不尋常金額或頻密程度", "¶5.7(a)")),
        tr(td("The ML/TF risks arising from your business", "業務所產生的洗錢／恐怖分子資金籌集風險", "¶5.4(b)"),
           td("The nature of a series of transactions, such as splitting a single transaction into a number of cash deposits", "一連串交易的性質，例如將單一交易分成多次現金存款", "¶5.7(b)")),
        tr(td("The nature of your systems and controls", "系統及管控措施的性質", "¶5.4(c)"),
           td("The counterparties of transactions", "交易對手", "¶5.7(c)")),
        tr(td("The monitoring procedures that already exist to satisfy other business needs", "滿足其他業務需要的現存監察程序", "¶5.4(d)"),
           td("The geographical origin or destination of a payment or receipt", "付款／收款的地點", "¶5.7(d)")),
        tr(td("The nature of the products and services you provide, including the means of delivery or communication", "產品及服務的性質（包括交付或溝通途徑）", "¶5.4(e)"),
           td("The customer's normal account activity or turnover", "該客戶的正常戶口活動或營業額", "¶5.7(e)")),
    ], minw=760, cls='cmp')
    + traps(
        trap(("Reviewed, documented, validated: which applies to what", "覆核、記錄、驗證：各自針對甚麼"), None, cc("¶5.8", FAQ(23)),
             vs=[(("Reviewed regularly", "定期覆核"),
                  ("The adequacy and effectiveness of the whole monitoring system and process, the parameters and thresholds included.",
                   "整個交易監察系統及程序（包括採用的參數及門檻）是否合適及有效。")),
                 (("Documented and independently validated", "妥為記錄並經獨立驗證"),
                  ("The parameters and thresholds, to make sure they are appropriate to your operations and context. The validator can be an external party, or your internal audit function if duties are properly segregated and it has enough expertise and resources.",
                   "參數及門檻，以確保其有效運作及符合實際情況。驗證者可以是外界人士，或在適當分工下具備足夠專業知識和資源的內部審核職能。"))]),
    ))

# ---------------------------------------------------------------- C. the extent of monitoring
C_ = sec('extent', ["¶5.9", "fn 54"],
         ("How closely to watch: the extent follows the customer's risk", "監察多嚴密：程度與客戶的風險相稱"),
    P("Transaction monitoring covers every business relationship, following the risk-based approach. What changes with the risk is its extent, for example how often and how intensely you monitor. Find the customer's risk in the left column.",
      "交易監察涵蓋所有業務關係，並採用風險為本的方法。隨風險而改變的是監察程度，例如監察的頻密程度及強度。在左欄找出客戶的風險。")
    + table([th("The customer's ML/TF risk", "客戶的洗錢／恐怖分子資金籌集風險"), th("The extent of transaction monitoring", "交易監察的程度"),
             th("Situations the Guideline gives as examples", "指引所舉的情況例子")], [
        tr(rh("Any customer", "任何客戶", "¶5.9"),
           td("Commensurate with the customer's ML/TF risk profile, for example in frequency and intensity", "與客戶的洗錢／恐怖分子資金籌集風險狀況相稱，例如監察的頻密程度及強度", "¶5.9"),
           dash_td()),
        tr(rh("High", "高", "¶5.9"),
           td("You should conduct <b>enhanced</b> transaction monitoring", "應<b>更嚴格</b>執行交易監察", "¶5.9"),
           td("A customer or a beneficial owner of a customer who is a non-Hong Kong PEP; a business relationship presenting a high ML/TF risk under section 15 of Schedule 2",
              "客戶或客戶的實益擁有人屬非香港政治人物；根據附表2第15條會引致洗錢／恐怖分子資金籌集的高度風險的業務關係", "fn 54")),
        tr(rh("Low", "低", "¶5.9"),
           td(f"You <b>may</b> reduce the extent of monitoring; the relationship is still monitored: see the {L_MON[0]}",
              f"<b>可</b>下調監察的程度；業務關係仍須受監察：見{L_MON[1]}", "¶5.9 · 4.8.6", post=flag()),
           td(f"Low-risk situations: examples of potentially lower risk factors are listed under simplified due diligence on the {L_SDD[0]}",
              f"低風險的情況：潛在較低風險因素的例子，列於{L_SDD[1]}的簡化盡職審查部分", "¶4.8.7")),
    ], note=B(f"The enhanced and simplified measures themselves, and when simplified due diligence must stop, are on the {L_SDD[0]}; how PEPs are identified is in its {L_PEP[0]}.",
              f"更嚴格及簡化措施的具體內容，以及何時必須停止簡化盡職審查，見{L_SDD[1]}；如何識別政治人物，見該頁的{L_PEP[1]}。"), minw=820)
    + traps(
        trap(("The yearly review and enhanced monitoring are two different things", "每年覆核與更嚴格監察是兩回事"), None, "¶5.1 · 5.3 · 5.9",
             vs=[(("At least once a year", "最少每年一次"),
                  ("The review of a high-risk customer's CDD information, to keep it up to date and relevant. This is ongoing CDD, one of the two aspects of monitoring.",
                   "覆核高風險客戶的盡職審查資料，確保其反映現況及仍屬相關。這是持續的盡職審查，即持續監察的兩個方面之一。")),
                 (("Enhanced", "更嚴格"),
                  ("The transaction monitoring of a high-risk relationship, the other aspect. The Guideline sets no number for it; what rises is the extent.",
                   "高風險業務關係的交易監察，即另一個方面。指引沒有為此訂明次數，提高的是監察程度。"))]),
    ))

# ---------------------------------------------------------------- D. an unusual transaction
D_ = sec('unusual', ["¶5.10–5.14", "fn 55", ("Circular 20 Jan 2026", "2026年1月20日通函")],
         ("A transaction does not add up: from trigger to decision", "交易不合情理：由觸發到決定"),
    P("Start at the three boxes at the top: the situations that call for steps. Hexagons are questions; follow yes or no. The two boxes at the foot apply to every route, stopping the CDD process included.",
      "由頂部三個方格開始，即應採取步驟的情況。六角形是問題，按「是」或「否」前進。底部兩個方格適用於每條路線，包括停止盡職審查程序。")
    + fig(fig_unusual, ("The alert box comes from the C&amp;ED circular of 20 January 2026; what else it expects before an alert is closed is on the <a href=\"#ci-tbml\">Circulars page</a>. What counts as tipping off, and the offence behind it, is on the <a href=\"#g7-duty\">Guideline Chapter 7 page</a>.",
                        "警報一格出自海關2026年1月20日的通函；消除警報前的其他要求，見<a href=\"#ci-tbml\">通函一頁</a>。何謂通風報訊及有關罪行，見<a href=\"#g7-duty\">指引第7章</a>。"), UNUSUAL_KEY)
    + traps(
        # ¶5.10 joins its two situations with 'or' in the English text and 及 in the Chinese:
        # the English view keeps the whole callout, the Chinese view only the point about (b)
        only('en', trap(("Either situation is enough; the second needs both halves", ""), None,
             cc("¶5.10", "s.5(1)(b), (c) Sch. 2"),
             vs=[(("Between the two situations: or", ""),
                  ("Transactions that do not fit what you know of the customer, or transactions that are complex or unusual with no apparent economic or lawful purpose: either one on its own calls for the steps to find out whether there are grounds for suspicion. The statutory duties behind them, section 5(1)(b) and (c) of Schedule 2, are separate limbs of the monitoring duty.",
                   "")),
                 (("Inside the second situation: and", ""),
                  ("The transaction must be complex, unusually large in amount or of an unusual pattern, and also have no apparent economic or lawful purpose. A large transaction with an evident lawful purpose does not meet it on size alone, though it can still meet the first situation if it does not fit what you know of the customer.",
                   ""))])),
        only('tc', trap(("", "第二種情況須同時符合兩部分"),
             ("", "交易須屬複雜、款額大得異乎尋常或進行模式異乎尋常，並且沒有明顯經濟或合法目的。款額龐大但有明顯合法目的之交易，單憑金額並不符合此情況。"),
             cc("¶5.10(b)", "s.5(1)(c) Sch. 2"))),
    )
    + traps(
        trap(("An STR is not only for a failed explanation", "可疑交易報告不只在未能取得解釋時才提交"), None, "¶5.12",
             vs=[(("After enquiries fail", "查詢未能取得解釋"),
                  ("Without a satisfactory explanation, you <b>may</b> conclude there are grounds for suspicion.",
                   "未能取得可信納的解釋，<b>可</b>斷定為有懷疑的理由。")),
                 (("Any suspicion, at any point", "任何時候出現任何懷疑"),
                  ("In any event, wherever suspicion is identified during transaction monitoring, an STR <b>should</b> be made to the JFIU.",
                   "在任何情況下，如在交易監察的過程中識別出可懷疑之處，便<b>應</b>向財富情報組提交可疑交易報告。"))]),
        trap(("Asking is allowed; stopping is the narrow exception", "可以詢問；停止程序只屬狹窄的例外"), None, "¶5.13",
             vs=[(("Enquiries", "詢問"),
                  ("Made properly and in good faith, enquiries of the customer do not constitute tipping off, so the steps above stay open to you.",
                   "憑誠信適當地詢問客戶並不構成通風報訊，因此上述步驟仍可進行。")),
                 (("Stopping the CDD process", "停止盡職審查程序"),
                  ("Only where you reasonably believe that performing it will tip off the customer. You should still document the basis for your assessment and file an STR with the JFIU.",
                   "只限於你合理地相信執行該程序會向客戶通風報訊的情況；你仍應把評估的基礎記錄在案，並向財富情報組提交可疑交易報告。"))]),
    ))

G5_NAV = [('files', 'Keeping files current', '保持資料更新'), ('system', 'Monitoring systems', '交易監察系統'),
          ('extent', 'Monitoring by risk', '按風險監察'), ('unusual', 'Unusual transactions', '異常交易')]
G5_BODY = A + B_ + C_ + D_

G5_META = dict(
    tab=("5", "5"),
    short=("Guideline Ch. 5 · Monitoring", "指引第5章 · 持續監察"),
    eyebrow=("AML/CFT Guideline · Chapter 5 · Module 6", "《打擊洗錢指引》第5章 · 單元六"),
    title=("Ongoing monitoring", "持續監察"),
    lede=("Taking a customer on is the start of the work, not the end. Chapter 5 turns the Schedule 2 duty to keep watching into working rules: clear review policies; a monitoring system that fits your business, is reviewed regularly and has its parameters and thresholds independently validated; a watch that tightens or relaxes with the risk; and a written trail from every transaction that does not add up to a decision or a report.",
          "接納客戶只是工作的開始，而非終結。第5章把附表2持續監察的責任化為實際規則：清晰的覆核政策；切合你的業務並定期覆核，且參數及門檻經獨立驗證的監察系統；隨風險收緊或放寬的監察；以及由每宗不合情理的交易到決定或報告的書面紀錄。"),
    foot=("Drawn from the Customs and Excise Department's Guideline on Anti-Money Laundering and Counter-Financing of Terrorism (For Money Service Operators), June 2023, Chapter 5 with paragraphs 4.8.6 and 4.8.7; Schedule 2 to the Anti-Money Laundering and Counter-Terrorist Financing Ordinance (Cap. 615), sections 5, 18 and 19; the FAQ applicable to all MSOs, Q22 and Q23; and the C&amp;ED circular of 20 January 2026.",
          "取材自香港海關《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》（2023年6月）第5章，以及第4.8.6及4.8.7段；《打擊洗錢及恐怖分子資金籌集條例》（第615章）附表2第5、18及19條；適用於所有金錢服務經營者的常見問題第22及23問；以及海關2026年1月20日的通函。"),
)
