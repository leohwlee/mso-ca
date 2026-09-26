# AML/CFT Guideline Chapter 8 (record-keeping), beyond the retention clocks already on the
# Schedule 2 page, and Chapter 9 (staff training) in full.
from ui import *
from g8_fig import cc, fig_uses, USES_KEY, fig_roles, ROLES_KEY, fig_cycle, CYCLE_KEY

SAMPLE6 = ("Sample question 6", "參考試題6")
APG16 = ("AML/CFT Policy guidelines item 16", "《打擊洗錢政策指引》第16項")
KEEP = chip("keep", "備存", 'ink')
ENOUGH = chip("enough of it", "足夠即可")
WHERE = chip("where applicable", "如適用")


def vd(ch):
    return f'<td class="verdict">{ch}</td>'


SHOULD = chip("should", "應", 'ink')

# ---------------------------------------------------------------- A. what goes in the file
A = sec('file', ["¶8.1–8.3", "¶8.5", "fn 66", "¶2.3, 2.16, 5.14", "¶6.18, 7.29–7.30"],
        ("Keep enough to rebuild each transaction and to show each check", "備存足以重組每宗交易、證明每項審查的紀錄"),
    P("Start from the box on the left. The red boxes are what the Guideline says your records should achieve; the dashed boxes are the others who rely on them. How long each record is kept, and in what form, is on the <a href=\"#s2-records\">Schedule 2 page</a>.",
      "由左邊的方格開始看。紅色方格是指引指你的紀錄應做到的事；虛線方格是還有誰依賴這些紀錄。每類紀錄須保存多久及以甚麼形式保存，見<a href=\"#s2-records\">附表2一頁</a>。")
    + fig(fig_uses, ("The same records serve both sides: they are how you demonstrate compliance, and they are the audit trail investigators and the Court work from.",
                     "同一批紀錄服務兩方面：你靠它證明合規，調查當局及法院亦靠它作為審計線索。"), USES_KEY)
    + h3("What goes in the file", "檔案內備存甚麼")
    + table([th("You hold", "你持有"), th("Keep it?", "備存？"), th("What the Guideline asks for", "指引的要求")], [
        tr(rh("Identity documents and data", "身分識別文件及資料"),
           vd(KEEP),
           td("The original or a copy of the documents, and a record of the data and information, obtained in identifying and, where applicable, verifying the customer, its beneficial owner, the beneficiary, anyone who purports to act for the customer, and other connected parties",
              "在識別及（如適用）核實客戶、客戶的實益擁有人、受益人、看似是代表客戶行事的人及客戶的其他有關連者的身分時，取得的文件的正本或複本，及如此取得的數據及資料的紀錄",
              "¶8.3(a) · s.20(1)(b)(i) Sch. 2", post=flag())),
        tr(rh("Other CDD and monitoring records", "其他盡職審查及監察紀錄"),
           vd(KEEP),
           td("Other documents and records obtained throughout the CDD and ongoing monitoring process, simplified and enhanced due diligence included",
              "在執行盡職審查或持續監察程序（包括簡化的盡職審查及更嚴格的盡職審查）期間取得的其他文件及紀錄",
              "¶8.3(b) · s.20(1)(b)(ii) Sch. 2")),
        tr(rh("Purpose of the relationship", "業務關係的目的"),
           vd(WHERE),
           td("The original or a copy of the documents, and a record of the data and information, on the purpose and intended nature of the business relationship",
              "業務關係的目的及擬具有的性質的文件的正本或複本，以及有關數據及資料的紀錄", "¶8.3(c)")),
        tr(rh("The account file", "戶口檔案"),
           vd(KEEP),
           td("The original or a copy of the records and documents relating to the customer's account, such as the account opening form or the risk assessment form",
              "關乎客戶戶口的紀錄及文件的正本或複本，例如開戶表格或風險評估表格", "¶8.3(d)")),
        tr(rh("Correspondence", "業務通訊"),
           vd(ENOUGH),
           td("Business correspondence with the customer and any beneficial owner, including at a minimum what is material to CDD measures or to significant changes in how the account operates. You are not expected to keep every piece, such as a series of emails; keep enough to demonstrate compliance with the AMLO",
              "與客戶及客戶的實益擁有人的業務通訊，最低限度包括與盡職審查措施或戶口運作有顯著改變有關的通訊。不要求保存每一封通訊，例如與客戶的連串電郵；但應保存足夠通訊，顯示已遵守《打擊洗錢條例》的規定",
              "¶8.3(d) · fn 66", post=flag())),
        tr(rh("The results of any analysis you undertook", "你所作任何分析的結果"),
           vd(KEEP),
           td("The results of any analysis undertaken, such as enquiries to establish the background and purpose of transactions that are complex, unusually large or of unusual pattern and have no apparent economic or lawful purpose. The duty to write the findings down is on the <a href=\"#s2-monitoring\">Schedule 2 page</a>",
              "任何已作分析的結果，例如當交易複雜、款額大得異乎尋常或進行模式異乎尋常，並無明顯經濟或合法目的時，為確立其背景及目的而作出的詢問。以書面記錄調查結果的責任，見<a href=\"#s2-monitoring\">附表2一頁</a>",
              "¶8.3(e)", post=flag())),
        tr(rh("Each transaction, domestic or international", "每宗交易，不論本地或國際"),
           vd(KEEP),
           td("The original or a copy of the documents, and a record of the data and information, obtained or generated in connection with it: enough to reconstruct the individual transaction and, if necessary, to provide evidence for the prosecution of criminal activity",
              "與該交易有關而取得或產生的文件的正本或複本，及數據及資料的紀錄：應足以重組個別交易，以便在有需要時為檢控犯罪活動提供證據",
              "¶8.5 · s.20(1)(a) Sch. 2", post=flag())),
    ], note=B("The customer records are kept for the whole relationship and at least five years after it ends, or at least five years after an occasional transaction equal to or above the CDD threshold; transaction records for at least five years after completion. The clocks are drawn on the <a href=\"#s2-records\">Schedule 2 page</a>.",
              "第8.3段提述的所有文件及紀錄應在與有關客戶的業務關係繼續期間備存，並在關係終止後最少五年，或在總值相等於或超過盡職審查門檻的非經常交易後最少五年；交易紀錄則在交易完成後最少五年。各時限見<a href=\"#s2-records\">附表2一頁</a>。") + ' ' + cite_html("¶8.4, 8.6"), minw=820)
    + h3("Beyond the customer file: other records to keep", "客戶檔案以外：其他備存的紀錄")
    + table([th("The record", "紀錄"), th("What to keep, and why", "備存甚麼及其目的")], [
        tr(rh("Your institutional ML/TF risk assessment", "機構層面的洗錢／恐怖分子資金籌集風險評估"),
           td("The appropriate steps should include documenting the risk assessment process, including the identification and assessment of relevant risks, supported by qualitative and quantitative analysis and information obtained from relevant internal and external sources; and having appropriate mechanisms to provide the risk assessment to the Commissioner when required to do so",
              "適當步驟應包括記錄風險評估程序，包括識別和評估有關風險的程序，並輔以從相關內部與外部來源取得的定質與定量分析及資料；以及設有適當機制應關長要求提供風險評估結果", "¶2.3(a), (e)")),
        tr(rh("Each customer risk assessment", "每項客戶風險評估"),
           td("Records and relevant documents of your customer risk assessments, so that you can demonstrate to the Commissioner, among others, how you assess the customer's ML/TF risks, and that the extent of CDD measures and ongoing monitoring is appropriate based on that customer's ML/TF risks",
              "就客戶風險評估備存紀錄及相關文件，以便向關長證明（其中包括）：你如何評估客戶的洗錢／恐怖分子資金籌集風險；及基於該客戶的洗錢／恐怖分子資金籌集風險，所執行的盡職審查措施及持續監察程度是合適的", "¶2.16")),
        tr(rh("Steps taken to identify grounds for suspicion", "為識辨有否懷疑的理由而採取的步驟"),
           td("The findings and outcomes of the steps taken, such as examining the background and purposes of the transactions, and the rationale of any decision made after taking them, should be properly documented in writing and be available to the Commissioner, other competent authorities and auditors",
              "所採取步驟（例如審查交易的背景及目的）的發現及結果、採取步驟後作出任何決定的理由，應以書面方式妥為記錄在案，以便提交予關長、其他主管當局及核數師", "¶5.10, 5.14")),
        tr(rh("Internal reports and STRs", "內部報告及可疑交易報告"),
           td("You must establish and maintain a record of all ML/TF reports made to the MLRO, and a record of all STRs made to the JFIU",
              "你必須建立及保存向洗錢報告主任作出的所有洗錢／恐怖分子資金籌集報告的完整紀錄，以及向財富情報組提交的所有可疑交易報告的紀錄", "¶7.29–7.30")),
        tr(rh("Screening", "篩查"),
           td("Records of enhanced checking results, together with all screening records, should be documented, or recorded electronically",
              "更嚴格查核的結果（連同篩查紀錄）應記錄在案或以電子方式記錄", "¶6.18")),
        tr(rh("Staff training", "職員培訓"),
           td("Who was trained, when, and in what type of training, whatever the training approach, and for how long: see <a href=\"#cycle\">the training cycle</a> below",
              "誰人、何時接受了哪類培訓（不論採用哪種培訓方法），以及須保存多久：見下文<a href=\"#cycle\">培訓循環</a>", "¶9.7")),
    ], note=B("Behind the whole list is the statutory duty to take all reasonable measures to ensure that proper safeguards exist to prevent a contravention of any requirement under Part 2 or 3 of Schedule 2, Part 3 being record-keeping: see the <a href=\"#s2-systems\">Schedule 2 page</a>.",
              "整張清單背後是法定責任：必須採取一切合理措施，確保設有合適的保障措施，以防止違反附表2第2或3部的任何規定，而第3部即備存紀錄：見<a href=\"#s2-systems\">附表2一頁</a>。") + ' ' + cite_html("¶3.1 · s.23 Sch. 2"), minw=720)
    + traps(
        trap(("An analysis you carried out is a record to keep, like the identity documents you collected", "你所作的分析與收集的身分證明文件一樣須備存"),
             ("Sample question 6 lists the beneficial owner's identity document, the results of any analysis undertaken, the customer's residential address, and the account opening record. The answer is all of the above: an analysis you carried out is a record, just like the documents you collected.",
              "參考試題6列出客戶的實益擁有人的身分證明文件、任何已作分析的結果、客戶的住址資料，以及客戶的開戶紀錄。答案是以上全部：你所作的分析與你收集的文件一樣，都是須備存的紀錄。"),
             cc("¶8.3", SAMPLE6)),
        trap(("Correspondence is selective; analysis results are not", "通訊可以取捨，分析結果不可以"), None, "¶8.3(d)–(e) · fn 66",
             vs=[(("Business correspondence", "業務通訊"),
                  ("At least what is material to CDD or to significant changes in the account. Not every email: enough to show you complied with the AMLO.",
                   "最低限度包括與盡職審查或戶口運作有顯著改變有關的通訊。毋須保存每一封電郵，但應足以顯示你已遵守《打擊洗錢條例》。")),
                 (("Results of analysis", "分析結果"),
                  ("The results of any analysis undertaken. No 'enough of it' allowance applies here.",
                   "任何已作分析的結果。這裏沒有「足夠即可」的寬限。"))]),
        trap(("Transaction records include what you generate, and domestic transactions count too", "交易紀錄包括你產生的資料，本地交易同樣涵蓋"),
             ("Transaction records are not only what the customer gives you: what is generated in connection with the transaction counts too, and domestic transactions are covered as fully as international ones. The test is whether the individual transaction could be reconstructed.",
              "交易紀錄不只是客戶交給你的文件：與交易有關而產生的文件及資料同樣須備存，而本地交易與國際交易一樣涵蓋在內。準則是能否重組個別交易。"),
             "¶8.5"),
    ))

# ---------------------------------------------------------------- B. records held elsewhere
B_ = sec('elsewhere', ["¶8.9–8.12", "Sch. 2 Pt 3", "s.18(4) Sch. 2"],
         ("Records held overseas or by an intermediary are still your records", "存放於海外或由中介人持有的紀錄，仍是你的紀錄"),
    P("Each row is a place your records might sit other than your own files. Choosing and relying on an intermediary is on the <a href=\"#s2-rely\">Schedule 2 page</a>; this is what the record-keeping chapter adds.",
      "每一行是紀錄可能存放在你自己的檔案以外的地方。如何選擇及依賴中介人，見<a href=\"#s2-rely\">附表2一頁</a>；本節是備存紀錄一章補充的內容。")
    + table([th("Where the records are", "紀錄在哪裏"), th("What the Guideline asks for", "指引的要求")], [
        tr(rh("Anywhere, including outside Hong Kong", "任何地方，包括香港以外"),
           td("Comply with all of Hong Kong's legal and regulatory requirements wherever the CDD and transaction records are held, especially the record-keeping rules in Part 3 of Schedule 2. The Licensing Guide separately requires a local place for storage of books and records in Hong Kong, a physical place holding the full set of books and records of your money service transactions: see the <a href=\"#gl-premises\">Guidelines page</a>",
              "不論在何處保存盡職審查及交易紀錄，均須符合香港的所有法律及監管規定，特別是附表2第3部的備存紀錄規定。《牌照指引》另外要求在香港設有本地儲存帳目及紀錄地點，用作儲存完整金錢服務交易帳目及紀錄：見<a href=\"#gl-premises\">指引一頁</a>",
              cc("¶8.9", ("Licensing Guide ¶4.10–4.11", "《牌照指引》第4.10至4.11段")))),
        tr(rh("With an intermediary you rely on for CDD, which holds the identification and verification documents", "由你藉以執行客戶盡職審查的中介人持有客戶的識別及核實文件"),
           td("You remain responsible for all the record-keeping requirements. Make sure the intermediary has systems to meet every record-keeping requirement of the AMLO and the Guideline, ¶8.3 to 8.9 included",
              "你仍有責任遵守所有備存紀錄的規定。應確保該中介人已設立系統，以遵從《打擊洗錢條例》及指引下所有備存紀錄的規定，包括第8.3至8.9段",
              "¶8.10 · s.18(4) Sch. 2", post=flag())),
        tr(rh("The intermediary stops providing its services", "中介人終止提供服務"),
           td("Make sure it will pass the documents and records to you", "應確保中介人會將文件及紀錄交回你", "¶8.12")),
    ], minw=720)
    + '<p>' + B("The data itself comes from the intermediary immediately after each measure, and before relying on it you must be satisfied that copies will come without delay: see the <a href=\"#s2-rely\">Schedule 2 page</a>. The record-keeping chapter adds the speed for copies you ask for later.",
        "數據須在中介人執行每項措施後立刻取得；依賴中介人之前，你須信納複本會沒有延誤地提供：見<a href=\"#s2-rely\">附表2一頁</a>。備存紀錄一章補充的是你其後索取複本時的速度。") + ' ' + cite_html("¶8.10–8.11 · s.18(1)(b), (4)(a)–(b) Sch. 2") + '</p>'
    + numreq([
        (("as soon as reasonably practicable", "盡快在合理地切實可行的範圍內"),
         ("The intermediary provides the documents and records you request", "中介人提供你所要求的文件及紀錄"),
         ("After it receives your request, made within the Schedule 2 retention periods", "在中介人收到你於附表2訂明的備存期內提出的要求後"),
         ("You must ensure it, and you remain responsible for the records. Section 18(4) of Schedule 2 is a specified provision: see the <a href=\"#p2-specified\">Part 2 page</a> for what a breach opens", "你須確保做到，並仍須為紀錄負責。附表2第18(4)條屬指明的條文：違反的後果見<a href=\"#p2-specified\">第2部一頁</a>"),
         "¶8.10 · s.18(4)(b) Sch. 2"),
    ])
    + traps(
        trap(("Two speeds for the same copies, and both are in the Ordinance", "同一批複本有兩種速度，兩者都出自條例"), None, "s.18(1)(b), (4)(b) Sch. 2 · ¶4.11.3, 8.10",
             vs=[(("Before you rely", "依賴之前"),
                  ("You must be satisfied the intermediary will provide copies on request without delay. The Guideline repeats this in its reliance section.",
                   "你須信納中介人會應要求沒有延誤地提供複本。指引在依賴中介人一節重申此點。")),
                 (("While you rely", "依賴期間"),
                  ("You must ensure copies come as soon as reasonably practicable after the intermediary receives your request. The record-keeping chapter uses this wording.",
                   "你須確保中介人在收到要求後，盡快在合理地切實可行的範圍內提供複本。備存紀錄一章採用此措辭。"))]),
    ))

# ---------------------------------------------------------------- C. training content
ORD3 = ("the Drug Trafficking (Recovery of Proceeds) Ordinance (DTROP), the Organized and Serious Crimes Ordinance (OSCO) and the United Nations (Anti-Terrorism Measures) Ordinance (UNATMO)",
        "《販毒（追討得益）條例》、《有組織及嚴重罪行條例》及《聯合國（反恐怖主義措施）條例》")

C_ = sec('who', ["¶9.1", "¶9.4–9.5"],
         ("What every member of staff should know, and what each role adds", "每名職員應知道甚麼，以及各職位須額外學習甚麼"),
    '<p>' + B("Read the figure from the top. The red band applies to everyone, the next band to every newcomer, and the boxes below to particular groups. The arrows are the reporting line: every internal report reaches the MLRO, who assesses it and reports suspicious transactions to the JFIU.",
      "由上而下看圖。紅色橫條適用於所有職員，下一條適用於每名新職員，下方各方格則適用於特定類別的職員。箭頭是舉報流程：所有內部報告均交予洗錢報告主任，由其評估並向財富情報組舉報可疑交易。") + ' ' + cite_html("¶7.9, 7.12(b), 9.5(e)") + '</p>'
    + fig(fig_roles, ("The group lists are areas the Guideline says may be appropriate, in addition to the five points for everyone. The groups overlap: a new front-line recruit is both a new joiner and a member of staff dealing with the public.",
                      "各類職員的清單，是指引指在五項共同事項以外「或適用」的培訓範疇。各類別會重疊：新入職的前線工作人員既是新職員，也是與公眾有直接接觸的職員。"), ROLES_KEY)
    + h3("The five points every member of staff should be made aware of", "應促使每名職員留意的五項事項")
    + table([th("Staff should be made aware of", "應促使職員留意"), th("Whose", "誰的"), th("Source", "出處")], [
        tr(td("The statutory obligations, and the possible consequences of failing to comply with the CDD and record-keeping requirements",
              "法定責任，以及因未能遵守盡職審查及備存紀錄規定而可能需要承擔的後果", "¶9.4(a)"),
           td("Yours as the MSO, and their own personally", "金錢服務經營者的，以及職員本身的"),
           td("The AMLO", "《打擊洗錢條例》")),
        tr(td("The statutory obligations, and the possible consequences of failing to report suspicious transactions",
              "法定責任，以及因未能舉報可疑交易而可能需要承擔的後果", "¶9.4(b)"),
           td("Yours as the MSO, and their own personally", "金錢服務經營者的，以及職員本身的"),
           td(f"Three ordinances: {ORD3[0]}", f"三條條例：{ORD3[1]}", post=flag())),
        tr(td("Any other statutory and regulatory obligations that concern the MSO and themselves, and the possible consequences of breaching them",
              "任何與金錢服務經營者及職員本身有關的其他法定及監管責任，以及違反此等責任而可能需要承擔的後果", "¶9.4(c)"),
           td("Yours as the MSO, and their own", "金錢服務經營者的，以及職員本身的"),
           td("Six: those three, plus the United Nations Sanctions Ordinance (UNSO), the Weapons of Mass Destruction (Control of Provision of Services) Ordinance (WMD(CPS)O) and the AMLO",
              "六條：上述三條，加上《聯合國制裁條例》、《大規模毀滅武器（提供服務的管制）條例》及《打擊洗錢條例》", post=flag())),
        tr(td("Your AML/CFT policies and procedures, including identifying and reporting suspicious transactions",
              "你在打擊洗錢／恐怖分子資金籌集方面的政策及程序，包括識別及舉報可疑交易", "¶9.4(d)"),
           td("Your firm's", "你的機構的"),
           td("Your own policies and procedures, not a statute", "你本身的政策及程序，並非法例")),
        tr(td("New and emerging ML/TF techniques, methods and trends, to the extent staff need them for their particular AML/CFT role",
              "洗錢／恐怖分子資金籌集的嶄新及新興技巧、方法及趨勢，以職員履行其特定職責所需為限", "¶9.4(e)"),
           td("Theirs, as far as their role needs", "職員的，以履行其職責所需為限"),
           td("None named", "沒有指明")),
    ], note=B("Why the Guideline insists: even a well-designed internal control system can be compromised if the staff using it are not adequately trained.",
              "指引堅持培訓的原因：如沒有為使用系統的職員提供充分培訓，即使是設計精湛的內部監控系統，其成效也會受到影響。") + ' ' + cite_html("¶9.1"), minw=820)
    + traps(
        trap(("Three ordinances for failing to report; six for everything else", "未有舉報涉及三條條例；其他責任涉及六條"), None, "¶9.4(b)–(c)",
             vs=[(("Failing to report suspicious transactions", "未能舉報可疑交易"),
                  ("DTROP, OSCO and UNATMO. The AMLO is not on this list: under it, the item is failing CDD and record-keeping.",
                   "《販毒（追討得益）條例》、《有組織及嚴重罪行條例》及《聯合國（反恐怖主義措施）條例》。《打擊洗錢條例》不在此列：該條例所涉的是未能遵守盡職審查及備存紀錄規定。")),
                 (("Any other obligations", "任何其他責任"),
                  ("Those three, plus UNSO, WMD(CPS)O and the AMLO.",
                   "上述三條，加上《聯合國制裁條例》、《大規模毀滅武器（提供服務的管制）條例》及《打擊洗錢條例》。"))]),
        trap(("New staff learn to report to the MLRO; JFIU reporting is in the lists for managers and the MLRO", "新職員學習向洗錢報告主任舉報；向財富情報組舉報列於經理級人員及洗錢報告主任的清單"), None, "¶9.5(a), (d)–(e)",
             vs=[(("All new staff", "所有新職員"),
                  ("Identify suspicious transactions and report them to the MLRO, and know the offence of tipping off.",
                   "識別可疑交易並向洗錢報告主任舉報，以及認識「通風報訊」的罪行。")),
                 (("Managerial staff, including internal audit officers and compliance officers", "經理級人員，包括內部審計人員及合規主任"),
                  ("Higher-level training on every aspect of the regime, plus their duties to supervise or manage staff, audit the system, perform random checks, and report suspicious transactions to the JFIU.",
                   "涵蓋整個制度各方面的更高層次培訓，以及監督或管理職員、系統審查、進行隨機抽查，以及向財富情報組舉報可疑交易的職責。")),
                 (("The MLRO, a group of its own", "洗錢報告主任（自成一類）"),
                  ("Assessing the suspicious transaction reports submitted to them and reporting suspicious transactions to the JFIU; keeping abreast of AML/CFT requirements and developments generally.",
                   "評估所收到的可疑交易報告及向財富情報組報告可疑交易；掌握打擊洗錢／恐怖分子資金籌集的一般規定及發展。"))]),
        trap(("'Should be made aware' is for everyone; the group lists 'may be appropriate'", "「應促使留意」適用於所有人；各類清單屬「或適用」"), None, "¶9.4–9.5",
             vs=[(("The five points", "五項事項"), ("Staff should be made aware of them, whatever their role.", "不論職位，應促使職員留意。")),
                 (("The group lists", "各類清單"), ("In addition, these areas of training may be appropriate for certain groups of staff.", "此外，這些培訓範疇或適用於特定類別的職員。"))]),
    ))

# ---------------------------------------------------------------- D. the cycle
D_ = sec('cycle', ["¶9.2–9.3", "¶9.6–9.8", APG16],
         ("Train early, refresh regularly, keep records, and check that it worked", "及早培訓、定期複修、備存紀錄，並檢查成效"),
    P("Follow the left column down from the policy. The box on the right is the loop that brings every member of staff back for refresher training.",
      "由政策開始沿左欄向下看。右邊的方格是讓每名職員定期回來接受複修培訓的循環。")
    + fig(fig_cycle, ("How often refresher training runs is not fixed: the Guideline says 'regularly', with scope and frequency tailored to your risks and to each person's role.",
                      "複修培訓的頻密程度沒有固定：指引只說「定期」，而範疇及頻密程度應切合你的風險及每名職員的職務。"), CYCLE_KEY)
    + h3("How firmly the Guideline puts each point", "指引對每一點的語氣強弱")
    + table([th("How firmly", "語氣"), th("The point", "要點")], [
        tr(vd(chip("your responsibility", "你的責任", 'ink')),
           td("Providing adequate training so that staff can implement your AML/CFT Systems", "為職員提供充分培訓，確保他們受訓後足以執行打擊洗錢／恐怖分子資金籌集制度", "¶9.2")),
        tr(vd(SHOULD),
           td("Tailoring scope and frequency to your specific risks, pitched to staff's job functions, responsibilities and experience", "培訓的範疇及頻密程度切合你面對的特定風險，並顧及職員的職能、職責及經驗", "¶9.2")),
        tr(vd(SHOULD),
           td("Requiring new staff to attend initial training as soon as possible after being hired or appointed; and regular refresher training", "新職員獲聘用或委任後盡快接受初步培訓；以及定期舉辦複修培訓", "¶9.2")),
        tr(vd(SHOULD),
           td("A clear and well-articulated policy for ensuring relevant staff receive adequate AML/CFT training", "實施清晰及明確的政策，確保有關職員獲得充分的打擊洗錢培訓", "¶9.3")),
        tr(vd(chip("encouraged to consider", "應考慮") + flag()),
           td("Using a mix of training techniques and tools, depending on your resources and staff's learning needs", "視乎可運用的資源及職員的培訓需要，混合使用各種培訓技巧及工具", "¶9.6")),
        tr(vd(chip("may consider", "可考慮")),
           td("Including available FATF papers and typologies in the training materials", "使用特別組織的文章及典型案件作為培訓材料", "¶9.6")),
        tr(vd(SHOULD),
           td("Being able to show the Commissioner that all materials are up to date and in line with current requirements and standards", "能夠向關長證明所有培訓材料都是最新的，並符合現行規定及標準", "¶9.6")),
        tr(vd(SHOULD),
           td("Monitoring and keeping records of who was trained, when, and the type of training, whatever the approach", "不論使用哪種培訓方法，監察誰人已接受培訓、何時接受培訓及培訓的類別，並備存紀錄", "¶9.7")),
        tr(vd(SHOULD + flag()),
           td("Monitoring the effectiveness of training. The three methods in the figure are ways it may be achieved", "監察培訓的效用。圖中三種方法是可達致此目的的方式", "¶9.8")),
    ], note=B("Dark chips mark the Guideline's full-strength wording; light chips mark a qualified or weaker one.",
              "深色標籤表示指引用語的語氣最強；淺色標籤表示有保留或較弱的用語。"), minw=720)
    + numreq([
        (("as soon as possible", "盡快"),
         ("New staff attend initial training", "新職員接受初步培訓"),
         ("After being hired or appointed, whatever their seniority", "獲聘用或委任後，不論資歷"),
         ("The chapter states no sanction; how much a departure from the Guideline counts is on the <a href=\"#p2-guidelines\">Part 2 page</a>", "本章沒有訂明罰則；偏離指引的分量見<a href=\"#p2-guidelines\">第2部一頁</a>"),
         "¶9.2, 9.5(a)"),
        (("regularly", "定期"),
         ("Refresher training", "複修培訓"),
         ("After the initial training, for all staff; frequency tailored to your risks and each role", "初步培訓以後，適用於所有職員；頻密程度切合你的風險及各職務"),
         ("The chapter states no sanction. Its stated purpose is to remind staff of their responsibilities and keep them informed of new ML/TF developments", "本章沒有訂明罰則。指引所述的目的，是確保職員明白本身的責任，並掌握有關洗錢／恐怖分子資金籌集的最新發展"),
         "¶9.2"),
        (("at least 3 years", "最少3年"),
         ("Keep the training records: who was trained, when, and in what type of training", "備存培訓紀錄：誰人、何時接受了哪類培訓"),
         ("Whatever training approach you adopt. This period comes from the Guideline; the five-year clocks for CDD and transaction records are on the <a href=\"#s2-records\">Schedule 2 page</a>", "不論採用哪種培訓方法。此期間出自指引；盡職審查及交易紀錄的五年時限見<a href=\"#s2-records\">附表2一頁</a>"),
         ("The chapter states no sanction; see the <a href=\"#p2-guidelines\">Part 2 page</a>", "本章沒有訂明罰則；見<a href=\"#p2-guidelines\">第2部一頁</a>"),
         "¶9.7"),
    ])
    + traps(
        trap(("A mix of methods is encouraged; showing the materials are up to date is a should", "混合使用培訓方法是「應考慮」；證明培訓材料屬最新是「應」"), None, "¶9.6",
             vs=[(("Encouraged to consider", "應考慮"),
                  ("A mix of training techniques and tools, depending on your available resources and your staff's learning needs.",
                   "混合使用各種培訓技巧及工具，視乎你可運用的資源及職員的培訓需要。")),
                 (("Should", "應"),
                  ("Being able to demonstrate to the Commissioner that all materials are up to date and in line with current requirements and standards.",
                   "能夠向關長證明所有培訓材料都是最新的，並符合現行規定及標準。"))]),
        trap(("The 2019 AML/CFT Policy guidelines' training cross-reference does not match the 2023 Guideline", "2019年版《打擊洗錢政策指引》就培訓範疇引用的段落，與2023年版指引不符"),
             ("Item 16 of the AML/CFT Policy guidelines, Ver. (12/2019), lists the training topics and ends with other issues set out in paragraph 9.7 of the Guideline. In the June 2023 Guideline, ¶9.7 is about training records; the topics by staff group are in ¶9.5.",
              "《打擊洗錢政策指引》（2019年12月版）第16項列出培訓範疇，最後一項是「《打擊洗錢指引》第9.7段所載列的其他事宜」。在2023年6月版指引中，第9.7段關乎培訓紀錄；按職員類別劃分的培訓範疇則在第9.5段。"),
             cc(APG16, "¶9.5, 9.7")),
    ))

G8_NAV = [('file', 'What to keep', '備存甚麼'), ('elsewhere', 'Records held elsewhere', '存放於別處的紀錄'),
          ('who', 'Training by role', '按職位培訓'), ('cycle', 'The training cycle', '培訓循環')]
G8_BODY = A + B_ + C_ + D_
G8_META = dict(
    tab=("8–9", "8–9"),
    short=("Guideline Ch. 8–9 · Records and training", "指引第8至9章 · 紀錄與培訓"),
    eyebrow=("AML/CFT Guideline · Chapters 8 and 9 · Modules 6 and 7", "《打擊洗錢指引》第8及9章 · 單元六及七"),
    title=("Record-keeping and Staff Training", "備存紀錄及職員培訓"),
    lede=("Records are how you prove every other duty was done, and how investigators and the Court follow the money; training is what makes your controls work, because even a well-designed system can be compromised if the staff using it are not adequately trained. This page covers what goes in the file beyond the retention clocks on the Schedule 2 page, who is answerable for records held elsewhere, what each member of staff should learn, and how you show the training happened and worked.",
          "紀錄是你證明已履行其他所有責任的方法，也是調查當局及法院追查資金的依據；培訓則令監控措施真正運作，因為如職員未受充分培訓，即使是設計精湛的系統，其成效也會受到影響。本頁講述附表2一頁的備存時限以外檔案須載有甚麼、存放於別處的紀錄由誰負責、每名職員應學習甚麼，以及你如何證明培訓已進行並具成效。"),
    foot=("Drawn from the Customs and Excise Department's Guideline on Anti-Money Laundering and Counter-Financing of Terrorism (For Money Service Operators), June 2023, Chapters 8 and 9 with ¶2.3, 2.16, 3.1, 4.11.3, 5.10, 5.14, 6.18 and 7.29–7.30; sections 18 and 23 and Part 3 of Schedule 2 to the AMLO; the AML/CFT Policy guidelines, version 12/2019, item 16; and the official sample questions of 12 May 2021.",
          "取材自香港海關《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》（2023年6月）第8及9章，並參考第2.3、2.16、3.1、4.11.3、5.10、5.14、6.18及7.29至7.30段；《打擊洗錢條例》附表2第18及23條及第3部；《打擊洗錢政策指引》（2019年12月版）第16項；以及2021年5月12日發出的官方參考試題。"),
)
