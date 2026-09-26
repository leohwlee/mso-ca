# AML/CFT Guideline Chapter 3: AML/CFT Systems. Who answers for the systems, what
# the compliance officer and MLRO need and do, how the systems are audited and staffed,
# and how they follow a Hong Kong-incorporated MSO overseas. The statutory duties in
# Schedule 2 ss.15-23 live on the Schedule 2 page and are linked, not repeated.
from ui import *
from bl_core import _runs
from g3_fig import (fig_build, BUILD_KEY, fig_simplify, SIMPLIFY_KEY, fig_lines, LINES_KEY,
                    fig_mlro, MLRO_KEY, fig_group, GROUP_KEY)


def LG(p):
    return (f"Licensing Guide ¶{p}", f"《牌照指引》第{_runs(p)}段")


def FPS(p):
    return (f"Supplementary F&P Guideline ¶{p}", f"《有關適當人選準則的補充指引》第{_runs(p)}段")


def FAQ(q):
    return (f"FAQ Q{q}", f"常見問題第{q}問")


def cc(*cs):
    """Join several citations into one."""
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


def who(en, tc):
    return f'<td class="verdict">{chip(en, tc, "ink")}</td>'


def firm(en, tc, strong=True, post=''):
    return f'<td class="verdict">{chip(en, tc, "ink" if strong else "")}{post}</td>'


def Pc(en, tc, cite):
    """A paragraph with its citation trailing inside it."""
    return f'<p>{B(en, tc)} {cite_html(cite)}</p>'


def th_nw(en, tc):
    return f'<th style="white-space:nowrap">{B(en, tc)}</th>'


# ---------------------------------------------------------------- 1. the four parts
S1 = sec('build', ["s.23 Sch. 2", "¶3.1–3.4", "¶1.6"],
         ("Your AML/CFT Systems: approved at the top, built from four parts", "你的打擊洗錢／恐怖分子資金籌集制度：由高層審批，由四個部分組成"),
    P("Read the figure from the top. The red boxes are duties on you: first the statute's, then the Guideline's. The four grey boxes are the parts every system should contain; select (a) to (c) to jump to the section that covers each.",
      "由上而下閱讀。紅色方格是你的責任：先是條例的，再是指引的。四個灰色方格是每套制度應包括的部分；點選(a)至(c)即跳往下文相關部分。")
    + fig(fig_build, ("The statute sets the goal in one sentence; Chapter 3 turns it into people and functions. The four parts are scaled to your business, but a small MSO still needs all four.",
                        "條例用一句訂明目標；第3章把它化為人員及職能。四個部分按業務規模釐定，但規模細小的金錢服務經營者仍須具備全部四項。"), BUILD_KEY)
    + table([th("The situation", "情況"), th("What the Guideline expects", "指引的要求")], [
        tr(td("You set up the systems", "你建立制度"),
           td("Have them approved by senior management, so that they let you manage and mitigate the risks relevant to you effectively",
              "制度應經高級管理層審批，確保你能有效管理和減低與你相關的風險", "¶3.2(a)")),
        tr(td("The systems are running", "制度正在運作"),
           td("Monitor how they are implemented, and enhance them if necessary", "監察制度的推行情況，並視乎需要優化", "¶3.2(b)")),
        tr(td("Higher risks are identified", "識別出較高風險"),
           td("Take enhanced measures to manage and mitigate those risks", "採取更嚴格的措施以管理和減低風險", "¶3.2(c)")),
        tr(td("Your business is small or simple", "你的業務規模細小或簡單"),
           td("Size the systems to the nature, size and complexity of the business and its ML/TF risks. They should still include the four parts",
              "制度應顧及業務的性質、規模及複雜程度，以及其洗錢／恐怖分子資金籌集風險；但仍應包括四個部分", "¶3.4", post=flag())),
        tr(td("Your risks are lower", "你的風險較低"),
           td("You may simplify the systems, but only on the three conditions in the <a href=\"#simplify\">next section</a>",
              "你可簡化制度，但只限於符合<a href=\"#simplify\">下一節</a>的三項條件", "¶3.3")),
    ], note=B("The statutory duty behind all of this, section 23 of Schedule 2, is set out with the other closing duties of the Schedule on the <a href=\"#s2-systems\">Schedule 2 page</a>.",
              "這一切背後的法定責任（附表2第23條），連同附表的其他最後幾條責任，見<a href=\"#s2-systems\">附表2一頁</a>。"), minw=720)
    + traps(
        trap(("In this Guideline, “should” is as mandatory as “must”", "在本指引中，「應」與「必須」同樣屬強制規定"),
             ("Paragraph 1.6 says either word marks a mandatory requirement. What softens a Chapter 3 duty is a qualifier written into it, so learn the qualifiers word for word.",
              "第1.6段指出，兩個字詞均表示該項屬強制規定。第3章某項責任之所以較寬鬆，是因為條文本身加入了限定字眼，所以要逐字記住這些限定字眼。"),
             cc("¶1.6", "¶3.8, 3.9(c), 3.13", "¶3.5 fn 9"),
             vs=[(("No qualifier", "沒有限定"), ("Senior management approves the systems; the four parts; an independent audit function; employee screening; a CO and an MLRO.",
                                                "高級管理層審批制度；四個部分；獨立的審核職能；僱員甄選；合規主任及洗錢報告主任。")),
                 (("Qualified", "有限定"), ("“as far as practicable”, “subject to constraint of size”, “normally based in Hong Kong”, “when required”, “where practicable”, “where appropriate”, “depending on the size”.",
                                          "「在切實可行的範圍內」、「視乎規模的限制」、「通常長駐香港」、「在有需要時」、「如切實可行的話」、「如適用」、「在適當情況下」、「視乎規模而定」。"))]),
        trap(("The four parts do not include the risk assessment", "四個部分並不包括風險評估"),
             ("The list is compliance management arrangements, an independent audit function, employee screening procedures, and an ongoing employee training programme. The institutional ML/TF risk assessment is Chapter 2's basis for the risk-based approach. It is also the Guideline's example of the appropriate risk assessment that condition (b) for simplifying requires. It is not a fifth part.",
              "清單是：合規管理安排、獨立的審核職能、僱員甄選程序，以及持續的僱員培訓計劃。機構層面的洗錢／恐怖分子資金籌集風險評估是第2章風險為本方法的基礎，亦是簡化制度條件(b)所要求的適當風險評估的例子，並非第五個部分。"),
             cc("¶3.4", "¶2.2", "¶3.3(b)")),
    ))

# ---------------------------------------------------------------- 2. simplifying
S2 = sec('simplify', ["¶3.3", "¶4.1.2"],
         ("A lower-risk business may run simpler systems, on three conditions", "風險較低的業務可簡化制度，但須符合三項條件"),
    P("Start at the top and follow the left-hand column. Every question has to come out on the downward path; a single answer that sends you right ends at the black box.",
      "由頂部開始，沿左欄向下走。每一個問題都須沿向下的路徑前進；只要有一個答案把你帶往右方，即以黑色方格告終。")
    + fig(fig_simplify, ("Only the nature, scale and complexity of the systems are simplified. The Schedule 2 duties themselves stay in full, which is condition (a).",
                           "可簡化的只是制度的性質、規模及複雜程度；附表2的責任本身仍須全面遵守，這正是條件(a)。"), SIMPLIFY_KEY)
    + traps(
        trap(("Simplified systems are not simplified due diligence", "簡化制度不等於簡化盡職審查"), None, cc("¶3.3", "¶4.1.2"),
             vs=[(("Simplified AML/CFT Systems", "簡化打擊洗錢／恐怖分子資金籌集制度"),
                  ("The design of your whole system, on the three conditions above, and never while ML/TF is suspected.", "整套制度的設計，須符合上述三項條件，而且在懷疑有洗錢／恐怖分子資金籌集時一概不准。")),
                 (("Simplified due diligence", "簡化盡職審查"),
                  ("Lighter CDD measures for a particular low-risk situation. The rules are on the <a href=\"#s2-sdd-edd\">Schedule 2 page</a>.", "在低風險情況下可採取的簡化盡職審查措施。有關規則見<a href=\"#s2-sdd-edd\">附表2一頁</a>。"))]),
        trap(("Senior management approves the simplified version too", "簡化後的制度同樣須經高級管理層審批"),
             ("Condition (c) needs both: approval by senior management, and review from time to time. The Guideline sets no fixed interval for that review.",
              "條件(c)須兩者兼備：經高級管理層審批，以及不時覆核。指引沒有為該覆核訂明固定的相隔時間。"),
             "¶3.3(c)"),
    ))

# ---------------------------------------------------------------- 3. oversight
S3 = sec('oversight', ["¶3.5–3.7", "¶3.11", ("Licensing Guide ¶4.15, 11.3", "牌照指引第4.15、11.3段")],
         ("Senior management owns the risk and appoints the two officers", "高級管理層承擔風險，並委任兩名主任"),
    P("The top box carries the responsibility. Arrows pointing down are appointments; arrows pointing up are the lines the officers and the audit function use to reach senior management. Select a grey box to jump to its section.",
      "頂部方格承擔責任。向下的箭咀代表委任；向上的箭咀是主任及審核職能聯絡高級管理層的途徑。點選灰色方格即跳往相關部分。")
    + fig(fig_lines, ("Compliance management arrangements, at a minimum, are senior management oversight plus the appointment of the two officers (paragraph 3.5). The audit function sits outside that minimum, with its own direct line to senior management.",
                        "合規管理安排最低限度包括高級管理層的監督，以及委任兩名主任（第3.5段）。審核職能不在這個最低限度之內，並有自己與高級管理層直接溝通的途徑。"), LINES_KEY)
    + table([th("", ""), th("Compliance officer", "合規主任"), th("Money laundering reporting officer", "洗錢報告主任")], [
        tr(rh("Who appoints", "誰委任"),
           td("Senior management", "高級管理層", "¶3.7"), td("Senior management", "高級管理層", "¶3.7")),
        tr(rh("What the Licensing Guide adds", "《牌照指引》的補充"),
           td("Must be your employee under the Employment Ordinance, unless the sole proprietor, a partner, a director or an ultimate owner is also the CO and MLRO; the appointment is notified to C&amp;ED. See the <a href=\"#gl-standing\">Guidelines page</a>",
              "須為按《僱傭條例》受聘於你的僱員，除非由獨資經營者、合夥人、董事或最終擁有人同時擔任合規主任及洗錢報告主任；委任須向關長具報。見<a href=\"#gl-standing\">指引一頁</a>", LG("4.15(a), 11.3")),
           td("The same employment rule and notification", "同樣的受聘規定及具報要求", LG("4.15(a), 11.3"))),
    ], minw=760, cls='cmp')
    + traps(
        trap(("Senior management implements; the CO establishes and maintains", "高級管理層負責推行；合規主任全面負責建立及維持"), None, "¶3.7",
             vs=[(("Senior management", "高級管理層"), ("Responsible for implementing effective AML/CFT Systems that can adequately manage the ML/TF risks identified. It appoints both officers.",
                                                      "有責任推行有效的制度，以妥善管理已識別的洗錢／恐怖分子資金籌集風險；並委任兩名主任。")),
                 (("Compliance officer", "合規主任"), ("Appointed at the management level, with the overall responsibility for establishing and maintaining the systems.",
                                                      "屬管理層，全面負責建立及維持制度。"))]),
        trap(("Management information: four qualities", "管理資料：四項要求"),
             ("Information on ML/TF risks and the systems should be communicated to the board or its delegated committee (where applicable) and senior management in a timely, complete, understandable and accurate manner, so that decisions are made on full information. The paragraph sets no reporting frequency.",
              "關於洗錢／恐怖分子資金籌集風險及制度的管理資料，應以合時、完整、易於理解及準確方式通知高級管理層，讓他們能夠在掌握充足資料的情況下作出決定。該段沒有訂明匯報頻密程度。"),
             "¶3.6"),
    ))

# ---------------------------------------------------------------- 4. equipping the officers
EIGHT = [
    ("(a)", ("Qualified", "資格"), ("Appropriately qualified, with sufficient AML/CFT knowledge", "擁有合適資格及具備充足的打擊洗錢／恐怖分子資金籌集知識"), None),
    ("(b)", ("Independent", "獨立"), ("Independent of all operational and business functions", "獨立於所有營運及業務職能"),
     ("“Subject to constraint of size” of the MSO", "「視乎金錢服務經營者規模的限制」")),
    ("(c)", ("Location", "所在地"), ("Based in Hong Kong", "長駐香港"), ("“<b>Normally</b>”", "「<b>通常</b>」")),
    ("(d)", ("Standing", "地位"), ("A sufficient level of seniority and authority within the MSO", "在金錢服務經營者具有一定的資歷及權力"), None),
    ("(e)", ("Access", "聯絡"), ("Regular contact with, and direct access to, senior management, so that senior management can satisfy itself the statutory obligations are met and the business is taking sufficiently effective measures against ML/TF",
                              "與高級管理層保持定期聯絡，並能直接聯絡高級管理層，確保高級管理層信納已符合各項法定責任，以及機構已採取充分有效的保護措施抵禦洗錢／恐怖分子資金籌集風險"),
     ("“<b>when required</b>” (direct access only)", "「<b>在有需要時</b>」（只限直接聯絡）")),
    ("(f)", ("Conversant", "熟悉"), ("Fully conversant with the MSO's statutory and regulatory requirements and the ML/TF risks from its business",
                                   "完全熟悉適用於金錢服務經營者的法定及監管規定，以及其業務所產生的洗錢／恐怖分子資金籌集風險"), None),
    ("(g)", ("Information", "資料"), ("Able to reach all available information on a timely basis: internal, such as CDD records, and external, such as circulars from the CCE",
                                    "能夠及時取得一切可取得的資料：內部來源如盡職審查紀錄，外部來源如關長通函"), None),
    ("(h)", ("Resources", "資源"), ("Sufficient resources, including staff, and appropriate cover for the absence of the CO and MLRO: an alternate or deputy CO and MLRO, who should have the same status",
                                  "配備充足資源，包括職員，以及合規主任及洗錢報告主任的適當替補人選：即替代或代理合規主任及洗錢報告主任，而他們應具有相同地位"),
     ("“<b>where practicable</b>” (the same status only)", "「<b>如切實可行的話</b>」（替代或代理人選及其相同地位）")),
]
rows4 = []
for letter, lab, text, qual in EIGHT:
    q = td(qual[0], qual[1], f"¶3.8{letter}") if qual else '<td class="faint">—</td>'
    rows4.append(tr(rh(f"{letter} {lab[0]}", f"{letter} {lab[1]}"), td(text[0], text[1], f"¶3.8{letter}"), q))

S4 = sec('officers', ["¶3.8", "¶3.5 fn 9", ("Licensing Guide ¶4.15(a)", "牌照指引第4.15(a)段"), ("Supp. F&P ¶6(g)", "補充指引第6(g)段")],
         ("Equipping the CO and MLRO: eight things senior management should secure", "讓合規主任及洗錢報告主任有效履行職責：高級管理層應確保的八項條件"),
    P("Senior management should secure all eight for both officers “as far as practicable”. The right-hand column holds the extra qualifier written into four of them; a question that drops one of those words, or hardens it into an absolute, is testing you.",
      "高級管理層應在切實可行的範圍內，為兩名主任確保全部八項條件。右欄列出其中四項額外附加的限定字眼；試題如刪去這些字眼，或把它改寫成絕對要求，正是考你的地方。")
    + table([th("Attribute", "條件"), th("What senior management should ensure", "高級管理層應確保的事項"), th("Extra qualifier in the text", "條文附加的限定字眼")],
            rows4, note=B("The whole list is introduced by “as far as practicable”, so that the CO and MLRO can discharge their responsibilities effectively.",
                          "整份清單以「在切實可行的範圍內」開首，目的是讓合規主任及洗錢報告主任能有效地履行職責。") + ' ' + cite_html("¶3.8"), minw=780)
    + traps(
        trap(("One person may be both CO and MLRO", "合規主任及洗錢報告主任可由同一人擔任"),
             ("Depending on the size of the MSO, the two functions may be performed by the same person. The Licensing Guide's exception, where the sole proprietor, a partner, a director or an ultimate owner is the CO and MLRO, fits the same picture.",
              "視乎金錢服務經營者的規模，兩項職能可由同一人執行。《牌照指引》的例外情況，即由獨資經營者、合夥人、董事或最終擁有人擔任合規主任及洗錢報告主任，亦與此一致。"),
             cc("¶3.5 fn 9", LG("4.15(a)"))),
        trap(("Normally based in Hong Kong, not must live in Hong Kong", "通常長駐香港，而非必須居於香港"), None, "¶3.8(c)",
             vs=[(("What the Guideline says", "指引的說法"), ("“Normally based in Hong Kong”.", "「通常長駐香港」。")),
                 (("Overstated", "誇大的說法"), ("“The officers must reside in Hong Kong.” An answer worded like this goes beyond the text.", "「主任必須居於香港。」答案如此表述，即超出條文。"))]),
    )
    + Pc("A competent CO of sufficient seniority and authority is also a fit-and-proper factor: see the <a href=\"#gl-fitproper\">fit and proper section</a>.",
        "具一定資歷及權力的合資格合規主任，亦是適當人選的考慮因素：見<a href=\"#gl-fitproper\">適當人選一節</a>。", FPS("6(g)")))

# ---------------------------------------------------------------- 5. CO or MLRO
S5 = sec('roles', ["¶3.9–3.10", "¶7.7, 7.9, 7.12–7.13, 7.31"],
         ("Which officer handles what: the CO runs the system, the MLRO handles suspicion", "兩名主任的分工：合規主任管制度，洗錢報告主任管可疑交易"),
    h3("Whose job is it? Illustrative situations", "由誰負責？示例情況")
    + table([th("The situation (an illustration)", "情況（示例）"), th_nw("Whose job", "由誰負責"), th("The duty it falls under", "所屬職責")], [
        tr(td("A change in the law or the Guideline leaves your procedures out of date", "法例或指引有變，令你的程序過時"),
           who("CO", "合規主任"), td("Develop and/or continuously review the systems, including any group-wide systems of a Hong Kong-incorporated MSO, so they stay up to date, meet current requirements and manage the risks effectively",
                                     "制訂及／或持續覆核制度（在香港成立為法團者包括任何集團層面的制度），確保制度反映現況、符合當前規定並能有效管理風險", "¶3.9(a)")),
        tr(td("Monitoring shows a control is not working as intended", "監察發現某項管控未能如預期運作"),
           who("CO", "合規主任"), td("Oversee all aspects of the systems, including monitoring their effectiveness and enhancing controls and procedures where necessary",
                                     "全方位監督制度，包括監察成效及在有需要時執行更嚴格的管控及程序", "¶3.9(b)")),
        tr(td("A review finds a significant compliance deficiency", "覆核發現重大的合規不足情況"),
           who("CO", "合規主任"), td("Communicate key AML/CFT issues to senior management, including significant compliance deficiencies <b>where appropriate</b>",
                                     "與高級管理層就主要問題進行溝通，包括<b>（如適用）</b>重大的合規不足情況", "¶3.9(c)", post=flag())),
        tr(td("Staff do not seem to understand what they were trained on", "職員似乎不明白培訓內容"),
           who("CO", "合規主任"), td("Make sure staff training is adequate, appropriate and effective", "確保職員培訓充足、適當及有效", "¶3.9(d)")),
        tr(td("A cashier raises a concern about a customer's transaction", "收銀員對某客戶的交易提出關注"),
           who("MLRO", "洗錢報告主任"), td("Oversee the review of the internal disclosure and the decision whether a report to the JFIU is necessary", "監督覆核內部披露，並決定是否有需要向財富情報組作出報告", "¶3.10(a)")),
        tr(td("The review of that disclosure is finished", "該內部披露已覆核完畢"),
           who("MLRO", "洗錢報告主任"), td("Oversee keeping all records of the internal review", "監督備存該等內部覆核的所有紀錄", "¶3.10(b)")),
        tr(td("The JFIU follows up with the MSO on a suspicious transaction report", "財富情報組就可疑交易報告跟進聯絡金錢服務經營者"),
           who("MLRO", "洗錢報告主任"), td("The main point of contact with the JFIU and law enforcement agencies", "與財富情報組及執法機構的主要聯絡點", "¶3.10")),
        tr(td("A colleague asks what may be said to a customer whose transaction is being looked at", "同事詢問可以向交易正被審視的客戶說些甚麼"),
           who("MLRO", "洗錢報告主任"), td("Oversee guidance on how to avoid tipping off", "監督提供有關如何避免「通風報訊」的導引", "¶3.10(c)")),
    ], note=B("The situations are illustrations written for this pack; the duty in the right-hand column is the Guideline's own. Court documents served by law enforcement agencies, such as search warrants and production orders, are handled under your own policies and procedures, which include appointing a staff member as the main point of contact with law enforcement agencies; paragraph 7.31 does not say that person must be the MLRO. See the <a href=\"#g7-lea\">Chapter 7 page</a>.",
              "上述情況是本資料冊自擬的示例；右欄所列的職責則取自指引原文。執法機構送達的法庭文件（例如搜查令、提交令），按你的政策和程序處理，其中包括委任一名人員作為與執法機構的中央聯絡點；第7.31段沒有規定該人員必須是洗錢報告主任。見<a href=\"#g7-lea\">第7章一頁</a>。") + ' ' + cite_html("¶7.31"), minw=760)
    + h3("The MLRO's review of an internal report", "洗錢報告主任如何覆核內部報告")
    + P("Follow the column down from the incoming report. The box on the right is the third item the MLRO oversees; it is not a step in the sequence.",
        "由收到報告開始，沿欄向下走。右方的方格是洗錢報告主任監督的第三項職能，並非流程中的一個步驟。")
    + fig(fig_mlro, ("Paragraph 3.10 sets who oversees each step, and paragraph 7.9 repeats it almost word for word. When and how a report is filed, and what the MLRO must do before deciding, are on the <a href=\"#g7-internal\">Chapter 7 page</a>.",
                       "第3.10段訂明每一步由誰監督，第7.9段以幾乎相同的字眼重複。實際何時及如何作出報告，以及洗錢報告主任決定前須做的事，見<a href=\"#g7-internal\">第7章一頁</a>。"), MLRO_KEY)
    + traps(
        trap(("Focal point (CO) vs central reference point (MLRO)", "中心點（合規主任）與中央聯絡點（洗錢報告主任）"), None, "¶3.7, 3.9–3.10",
             vs=[(("CO: the focal point", "合規主任：中心點"),
                  ("For the oversight of all activities relating to the prevention and detection of ML/TF, and for supporting and guiding senior management so that ML/TF risks are adequately identified, understood and managed.",
                   "監督一切防止及偵察洗錢／恐怖分子資金籌集的活動，並向高級管理層提供支援及導引，確保妥為識別、了解和管理有關風險。")),
                 (("MLRO: the central reference point", "洗錢報告主任：中央聯絡點"),
                  ("For reporting suspicious transactions, and also the main point of contact with the JFIU and law enforcement agencies. A senior staff member who plays an active role in identifying and reporting suspicious transactions.",
                   "報告可疑交易的中央聯絡點，亦是與財富情報組及執法機構的主要聯絡點；由一名高級職員擔任，在識別及報告可疑交易方面擔當積極的角色。"))]),
        trap(("Tipping-off guidance is the MLRO's; staff training is the CO's", "通風報訊的導引屬洗錢報告主任；職員培訓屬合規主任"), None, "¶3.9(d), 3.10(c)",
             vs=[(("MLRO", "洗錢報告主任"), ("Oversees guidance on how to avoid tipping off.", "監督有關如何避免通風報訊的導引。")),
                 (("CO", "合規主任"), ("Ensures AML/CFT staff training is adequate, appropriate and effective.", "確保打擊洗錢方面的職員培訓充足、適當及有效。"))]),
    )
    + Pc("Every internal report must reach the MLRO without undue delay, and under no circumstances should a supervisor or manager with no reporting or compliance role filter it out: see the <a href=\"#g7-internal\">Chapter 7 page</a>.",
        "所有內部報告必須送達洗錢報告主任，不得無故延誤；非負責洗錢報告／合規職能的主管或經理均不得過濾職員所提交的報告：見<a href=\"#g7-internal\">第7章一頁</a>。", "¶7.12(b), 7.13"))

# ---------------------------------------------------------------- 6. audit and screening
AUDIT_ITEMS = [
    ("(a)", ("The adequacy of the AML/CFT Systems, the ML/TF risk assessment framework and the application of the risk-based approach",
             "制度、洗錢／恐怖分子資金籌集風險評估框架及風險為本方法的應用情況是否合適"), False),
    ("(b)", ("The effectiveness of the suspicious transaction reporting systems", "報告可疑交易的制度是否有效"), False),
    ("(c)", ("The effectiveness of the compliance function", "合規職能是否有效"), True),
    ("(d)", ("The level of awareness of staff having AML/CFT responsibilities", "職員對負責打擊洗錢／恐怖分子資金籌集的意識水平"), False),
]
rows6 = [tr(rh(f"Review item {l}", f"覆核範圍{l}"), td(t[0], t[1], f"¶3.12{l}", post=flag() if f else '')) for l, t, f in AUDIT_ITEMS]

S6 = sec('audit', ["¶3.11–3.14", ("FAQ Q23", "常見問題第23問")],
         ("Checking the system works: independent audit, and hiring standards", "檢查制度是否奏效：獨立審核及聘用標準"),
    table([th("The audit function", "審核職能"), th("What the Guideline expects", "指引的要求")], [
        tr(rh("Set up", "設立"),
           td("An independent audit function with a <b>direct line of communication to senior management</b>", "設立獨立的審核職能，並能<b>與高級管理層直接溝通</b>", "¶3.11")),
        tr(rh("Equipped", "配備"),
           td("Sufficient expertise and resources to carry out its responsibilities, including independent reviews of the AML/CFT Systems", "具備充足的專門知識及資源以履行職責，包括對制度作出獨立覆核", "¶3.11")),
        tr(rh("How it reviews", "如何覆核"),
           td("Regularly, to ensure effectiveness. The review includes, but is not limited to, the four items below", "定期覆核以確保成效；覆核範圍包括但不限於下列四項", "¶3.12")),
    ] + rows6 + [
        tr(rh("How often, how deep", "頻密程度及範圍"),
           td("Commensurate with the nature, size and complexity of the business and its ML/TF risks. No fixed interval is set", "與業務的性質、規模及複雜程度，以及其洗錢／恐怖分子資金籌集風險相稱；沒有訂明固定的相隔時間", "¶3.13", post=flag())),
        tr(rh("Outside eyes", "外界覆核"),
           td("<b>Where appropriate</b>, also seek a review from external parties", "<b>在適當情況下</b>，亦應尋求外界進行覆核", "¶3.13")),
        tr(rh("Validating transaction monitoring", "核實交易監察"),
           td("See the <a href=\"#ci-edd\">Circulars page</a>", "見<a href=\"#ci-edd\">通函一頁</a>", FAQ(23))),
    ], minw=720)
    + traps(
        trap(("External review is “where appropriate”, not a standing requirement", "外界覆核屬「在適當情況下」，並非固定要求"),
             ("Chapter 3 requires an independent audit function and regular reviews sized to your business. It adds an external review only where appropriate, and names no frequency.",
              "第3章要求設立獨立的審核職能，並按業務規模定期覆核；外界覆核只屬在適當情況下的補充，亦沒有訂明頻密程度。"),
             "¶3.11–3.13"),
        trap(("The audit function reviews the compliance function", "審核職能須覆核合規職能"),
             ("Item (c) of the review is the effectiveness of the compliance function itself, and the audit function has its own direct line of communication to senior management. A list of review items that leaves out the compliance function is incomplete.",
              "覆核範圍第(c)項正是合規職能本身是否有效，而審核職能能與高級管理層直接溝通。覆核範圍的清單如遺漏合規職能，即不完整。"),
             "¶3.11–3.12(c)"),
        trap(("Employee screening is about hiring, not customers", "僱員甄選關乎聘用僱員，而非客戶"), None, cc("¶3.14", "¶6.16"),
             vs=[(("Employee screening", "僱員甄選"), ("Adequate and appropriate screening procedures, to ensure high standards when hiring employees. One of the four parts of the system.", "設立妥善而適當的甄選程序，確保聘用僱員時採用崇高標準；是制度四個部分之一。")),
                 (("Screening mechanism", "篩查機制"), ("Screening customers and any beneficial owners against the current database, a separate control in Chapter 6.", "根據當時的數據庫對客戶及該等客戶的任何實益擁有人進行篩查，是第6章另一項管控措施。"))]),
    ))

# ---------------------------------------------------------------- 7. the group
S7 = sec('group', ["¶3.15–3.19", ("fn 10–11", "註10至11"), "s.22 Sch. 2"],
         ("Overseas branches and subsidiary undertakings: one group standard, and the higher rule wins", "外地分行及附屬企業：集團統一標準，以較嚴格者為準"),
    P("Follow the left-hand column down. The box on the right of the group-wide systems runs alongside them; the two questions below decide which box at the foot applies.",
      "沿左欄向下走。集團層面制度右方的方格與制度同步進行；其下兩個問題決定底部哪一個方格適用。")
    + fig(fig_group, ("The statutory core, section 22 of Schedule 2, covers CDD and record keeping only and is on the Schedule 2 page. The Guideline stretches the group standard to its other requirements and adds the higher-of-the-two rule.",
                        "法定核心（附表2第22條）只涵蓋盡職審查及備存紀錄，見附表2一頁。指引把集團標準擴展至其他規定，並加入「兩者中較嚴格者」的規則。"), GROUP_KEY)
    + h3("What the group shares, and in which direction", "集團共用甚麼資料，以及流向")
    + table([th_nw("How firm", "要求程度"), th("Information", "資料"), th("Goes to", "交予")], [
        tr(firm("Should", "應"),
           td("Information required for CDD and for managing ML/TF risk", "為盡職審查及管理洗錢／恐怖分子資金籌集風險所需的資料", "¶3.17(a)"),
           td("Shared within the group", "在集團內共用")),
        tr(firm("Should", "應"),
           td("Customer, account and transaction information from overseas branches and subsidiary undertakings in the same business as a financial institution, when necessary for AML/CFT purposes",
              "外地分行及經營與金融機構相同業務的附屬企業的客戶、帳戶及交易資料（在有需要時，為打擊洗錢／恐怖分子資金籌集的目的）", "¶3.17(b)"),
           td("The group-level compliance, audit and/or AML/CFT functions", "集團層面的合規、審核及／或打擊洗錢／恐怖分子資金籌集職能")),
        tr(firm("Should include", "應包括"),
           td("Information on, and analysis of, transactions or activities that appear unusual, if such analysis was done", "似乎異常的交易或活動的資料及分析（如已作這類分析）", "fn 11"),
           td("Part of what goes up to the group-level functions", "屬交予集團層面職能的資料之一")),
        tr(firm("Could include", "可以包括", strong=False, post=flag()),
           td("A suspicious transaction report, its underlying information, or the fact that one was submitted", "可疑交易報告、相關資料，或已提交可疑交易報告一事", "fn 11"),
           td("Part of what goes up to the group-level functions", "屬交予集團層面職能的資料之一")),
        tr(firm("Should receive", "應能取得"),
           td("Such information, when relevant and appropriate to risk management", "在與風險管理有關及適用時的這類資料", "fn 11"),
           td("Back down to the branches and subsidiary undertakings", "反向交予分行及附屬企業")),
    ], note=B("Every row is subject to two conditions: the laws and regulations of the jurisdictions involved must permit it, and there must be adequate safeguards on the confidentiality and use of the information, including safeguards to prevent tipping off.",
              "每一行均受兩項條件限制：所涉司法管轄區的法律及規例須准許；以及須妥善保障共用資料的保密需要及用途，包括防止通風報訊。") + ' ' + cite_html("¶3.17"), minw=760)
    + traps(
        trap(("The Guideline says Hong Kong-incorporated; the Ordinance now also names re-domiciled entities", "指引只提在香港成立為法團；條例現時亦涵蓋經遷冊實體"),
             ("The June 2023 Guideline addresses a Hong Kong-incorporated MSO. Section 22(1) of Schedule 2, as amended in 2025, applies to a financial institution incorporated in Hong Kong or that is a re-domiciled entity. The two texts differ on this point.",
              "2023年6月的指引針對在香港成立為法團的金錢服務經營者。附表2第22(1)條經2025年修訂後，適用於在香港成立為法團或屬經遷冊實體的金融機構。兩份文本在這一點上並不相同。"),
             cc("¶3.15", "s.22(1) Sch. 2")),
        trap(("The CO's review covers the group-wide systems too", "合規主任的覆核亦涵蓋集團層面的制度"),
             ("For a Hong Kong-incorporated MSO, developing and continuously reviewing the systems includes any group-wide AML/CFT Systems.",
              "就在香港成立為法團的金錢服務經營者而言，制訂及持續覆核制度包括任何集團層面的打擊洗錢／恐怖分子資金籌集制度。"),
             "¶3.9(a)"),
    ))

G3_NAV = [('build', 'Four parts', '四個部分'), ('simplify', 'Simplifying', '簡化制度'),
          ('oversight', 'Senior management', '高級管理層'), ('officers', 'Equipping the officers', '主任的條件'),
          ('roles', 'CO or MLRO', '兩名主任的分工'), ('audit', 'Audit and screening', '審核與甄選'),
          ('group', 'Overseas group', '海外集團')]
G3_BODY = S1 + S2 + S3 + S4 + S5 + S6 + S7

G3_META = dict(
    tab=("3", "3"),
    short=("Guideline Ch. 3 · AML/CFT Systems", "指引第3章 · 打擊洗錢／恐怖分子資金籌集制度"),
    eyebrow=("AML/CFT Guideline · Chapter 3 · Modules 5 and 7", "《打擊洗錢指引》第3章 · 單元五及七"),
    title=("AML/CFT Systems and who answers for them", "打擊洗錢／恐怖分子資金籌集制度及其負責人"),
    lede=("Chapter 3 decides who in your business answers for AML/CFT, and what they need to do it. Senior management approves the systems and appoints a compliance officer and an MLRO; an independent audit function checks that the systems work; staff are screened when hired and trained throughout. If you are a Hong Kong-incorporated MSO with overseas branches, or subsidiary undertakings in the same business as a financial institution, the same standard follows them wherever it is relevant and applicable. Where the rules differ, you require them to apply the higher one as far as host law permits; if host law does not permit it, you inform the CCE and take additional measures.",
          "第3章決定你的業務中由誰為打擊洗錢／恐怖分子資金籌集負責，以及他們需要甚麼條件。高級管理層審批制度，並委任合規主任及洗錢報告主任；獨立的審核職能檢查制度是否奏效；僱員在聘用時經甄選，並持續接受培訓。如你是在香港成立為法團的金錢服務經營者，並設有外地分行或經營與金融機構相同業務的附屬企業，在本指引的規定關乎及適用於它們時，同一標準亦適用於它們。如規定有所不同，你應規定它們在當地法律准許的範圍內執行較嚴格者；如當地法律不准許，應通知關長並採取額外措施。"),
    foot=("Drawn from Chapter 3, paragraphs 3.1 to 3.19 and footnotes 9 to 11, of the Customs and Excise Department's Guideline on Anti-Money Laundering and Counter-Financing of Terrorism (For Money Service Operators), June 2023, with paragraphs 1.6, 2.2–2.3, 4.1.2, 6.16, 7.7, 7.9, 7.12–7.13 and 7.31; sections 22 and 23 of Schedule 2 to the Anti-Money Laundering and Counter-Terrorist Financing Ordinance, Cap. 615 (consolidated 15 May 2026); the Licensing Guide for Money Service Operators (May 2026), paragraphs 4.15 and 11.3; the Supplementary Guideline on Criteria for Determining Fitness and Propriety (January 2020), paragraph 6(g); and FAQ Q23.",
          "取材自海關《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》（2023年6月）第3章第3.1至3.19段及註9至11，以及第1.6、2.2至2.3、4.1.2、6.16、7.7、7.9、7.12至7.13及7.31段；《打擊洗錢及恐怖分子資金籌集條例》（第615章）（2026年5月15日綜合版）附表2第22及23條；《金錢服務經營者牌照指引》（2026年5月）第4.15及11.3段；《有關適當人選準則的補充指引》（2020年1月）第6(g)段；以及常見問題第23問。"),
)
