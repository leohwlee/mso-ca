"""Source-authored bilingual manuscript. Review scope: depth-review-2026-10-20/REPORT.md."""
from model import p, ref, block, section

PART = dict(title=p('金錢服務經營者的系統及管控措施（三）：證明符合規定及監察合規水平', 'MSO systems and controls (iii): demonstrating and monitoring compliance'),
intro=p('合規不止是有政策：須能展示已執行、已檢查及已處理問題的證據。把舉報、紀錄、審核、培訓和監管申報分開記。', 'Compliance requires evidence that controls were performed, checked and deficiencies addressed. Distinguish reporting, records, audit, training and regulatory returns.'), sections=[
section('reporting-duty', '可疑交易舉報：觸發條件及時間', 'Suspicious transaction reporting: trigger and timing', [
    block('知悉、懷疑與法定義務', 'Knowledge, suspicion and the statutory duty', [
        ('若知悉或懷疑財產全部或部分、直接或間接代表販毒／可公訴罪行得益，曾用於或擬用於該等罪行，或屬恐怖分子財產，須在合理情況下盡快向JFIU披露，並交代懷疑依據。 財產不限現金，也包括貨品、土地及權利；完整定義見第1部分「洗錢」。', 'Disclose to the JFIU as soon as reasonable where the MSO knows or suspects that property wholly/partly, directly/indirectly represents proceeds of drug trafficking/an indictable offence, was or is intended to be used in it, or is terrorist property. Include the basis of knowledge or suspicion. Property extends beyond cash to goods, land and rights; see Part 1 Money laundering for the full definition.'),
        ('知悉可包括實際知道、合理人士會據以認知事實的情況，或會促使合理人士進一步查詢的情況。懷疑較主觀，低於以確實證據證明；不必先知道確切上游罪行或證實資金必定來自犯罪。', 'Knowledge includes actual knowledge and circumstances that indicate facts to, or put on inquiry, a reasonable person. Suspicion is more subjective and falls short of firm proof. Identifying the exact predicate crime or proving criminal origin is not a prerequisite.'),
        ('金額沒有最低門檻；未完成、被拒絕或只是嘗試的交易也可觸發舉報。不能因沒有交易入帳或金額低於CDD門檻而不報。', 'There is no minimum reporting amount. Attempted, rejected or uncompleted transactions may trigger reporting. Neither absence of a completed transaction nor an amount below CDD thresholds removes the duty.'),
        ('不披露知悉或懷疑的最高刑罰為監禁3個月及罰款港幣50,000元；這與洗錢罪及通風報訊的刑罰不同。', 'Failure to disclose knowledge/suspicion carries a maximum of three months’ imprisonment and HK$50,000. Distinguish this from laundering and tipping-off penalties.'),
    ], [
        ref('03', '第7.1–7.5段及註60', '¶7.1–7.5; footnotes 60', 'Suspicion is personal and falls short of proof'),
    ], kind='list'),
    block('理解：情報分析、調查與檢控各有角色', 'Understand: intelligence analysis, investigation and prosecution', [
        ('按2022年報告，聯合財富情報組（JFIU，Joint Financial Intelligence Unit）由警務處及海關共同運作，接收、分析和發布可疑交易報告（STR）情報。收到報告後會按可疑程度、嚴重性及風險分析，再發展或轉交有價值情報予調查單位／其他機構；提交STR不等於已證明犯罪或必然提出檢控。', 'The 2022 report describes the Joint Financial Intelligence Unit (JFIU), jointly operated by the Police and Customs, as receiving, analysing and disseminating suspicious transaction report (STR) intelligence. It assesses suspicion, severity and risk, then develops or disseminates valuable intelligence to investigative units/other agencies. Filing an STR does not establish crime or guarantee prosecution.'),
        ('律政司刑事檢控科的檢控考慮是：證據顯示有合理機會定罪，並且檢控符合公眾利益；決定須獨立作出。這與本節「知悉或懷疑」便須盡快披露的責任不同，MSO不能等到掌握足以定罪的證據才報告。', 'The Department of Justice Prosecutions Division considers whether evidence shows a reasonable prospect of conviction AND prosecution is in the public interest, making decisions independently. This differs from the knowledge-or-suspicion disclosure duty described above; an MSO must not wait for evidence sufficient to convict before reporting.'),
        ('STR數量也不是犯罪宗數。2022年報告指出數量受合規文化、報告質素及把多名嫌疑人／多個帳戶／多宗交易放入同一份大型報告等因素影響。學習重點是提供有用資料與可疑理由，不是把歷年STR升跌直接解作犯罪升跌。', 'STR totals are not crime counts. The 2022 report links volumes to compliance culture, report quality and large reports combining multiple suspects, accounts and transactions. The learning point is useful information and reasons for suspicion, rather than equating historical STR changes with changes in crime.'),
    ], [
        ref('25', '2022年版，第3.38–3.39、3.46–3.47段', '2022 edition, ¶3.38–3.39, 3.46–3.47', 'reasonable prospect of conviction'),
        ref('03', '第7.1、7.12段', '¶7.1, 7.12', 'as soon as it is reasonable'),
    ], kind='list'),
]),
section('internal-report', '內部報告與MLRO評估', 'Internal reporting and MLRO assessment', [
    block('從員工到JFIU', 'From staff to the JFIU', [
        ('員工應知道MLRO是誰及如何報告；內部報告須不受不當延誤地送達。非負責洗錢舉報／合規職能的主管不得把員工報告篩走，匯報線應盡量短。', 'The MSO should ensure staff know the MLRO and reporting procedure. Reports must reach the MLRO without undue delay. Under no circumstances should managers without reporting/compliance responsibility filter them out; reporting lines should be as short as possible.'),
        ('員工按機構程序向MLRO報告懷疑後，已履行相關個人法定舉報義務。內部報告應包括充分客戶詳情及引起懷疑的資料；MLRO必須確認收妥並提醒避免通風報訊（該句英文為should）。', 'Staff who report suspicion to the MLRO under the MSO’s procedures discharge the relevant personal statutory duty. Internal reports should include full customer details and grounds; the MLRO should acknowledge receipt and remind staff about tipping off (the Chinese uses 必須).'),
        ('MLRO須採取合理步驟考慮全部相關資料，包括CDD、持續監察、關連戶口的交易、歷史指示和關係年期。資料搜尋須與及時舉報取得平衡，不能無限等待收齊所有資料。', 'The MLRO takes reasonable steps to consider all relevant CDD, monitoring, connected-account activity, historical instructions and relationship duration. Balance information gathering with prompt reporting rather than waiting indefinitely for completeness.'),
        ('評估後有知悉或懷疑，應盡快向JFIU披露；即使決定不報，也須保留考慮過程、理由及行動紀錄。緊急移走款項、關戶等情況應在報告標明，特殊緊急情況應考慮先電話通知。', 'If knowledge/suspicion remains, disclose promptly to the JFIU. If deciding not to report, retain deliberations, reasons and actions. Flag urgent fund movements/account closure; initial telephone notification should be considered in exceptional urgent cases.'),
        ('同時控制電傳轉帳兩端的機構，亦應在受該可疑轉帳影響的司法管轄區提交報告，並向財富情報組（JFIU）提供相關交易資料。', 'An MSO controlling both sides of a wire transfer should also report in jurisdictions affected by the suspicious transfer and make relevant transaction information available to their FIUs.'),
    ], [
        ref('03', '第7.12–7.23段', '¶7.12–7.23', 'under no circumstances should reports raised by staff be filtered out'),
    ], kind='flow'),
    block('以回饋持續改善STR質素', 'Use feedback to improve STR quality', [
        ('應確保STR質素，考慮JFIU季度報告的分析、關注事項及回饋，以及海關不時發出的指引。這項季度回饋不是MSO半年定期申報，兩者目的及周期不同。', 'Ensure high-quality STRs by considering JFIU quarterly analysis, matters of interest/feedback and CCE guidance. This quarterly feedback is distinct from an MSO’s half-yearly periodic return; they serve different purposes and cycles.'),
    ], [
        ref('03', '第7.23段及註65', '¶7.23; footnotes 65', 'taking into account feedback and guidance provided by the JFIU in its quarterly report'),
    ], kind='list'),
    block('真誠評估後決定不報告的條件', 'Conditions when deciding in good faith not to report', [
        ('第7.20段說，MLRO真誠行事，考慮全部可得資料後結論是沒有懷疑，則一般不大可能因不報STR而負刑責；必須妥存考慮及行動紀錄，證明合理行事。這不是只要寫「不懷疑」便絕對免責，也不是可以忽略未查明的警號。', 'Paragraph 7.20 says criminal liability for non-reporting is unlikely where the MLRO acts in good faith and concludes there is no suspicion after considering all available information. Proper records of deliberations/actions are vital to demonstrate reasonableness. Merely recording “no suspicion” is not absolute immunity or permission to disregard unresolved indicators.'),
    ], [
        ref('03', '第7.20段', '¶7.20', 'it is unlikely that there will be any criminal liability'),
    ], kind='list'),
]),
section('tipping-off', '通風報訊與向客戶查詢的界線', 'Tipping off and enquiries to customers', [
    block('避免妨礙調查', 'Avoid prejudicing an investigation', [
        ('知道或懷疑已作披露而再透露可能妨礙調查的資料，可構成通風報訊；最高刑罰為監禁3年及罰款。內部已提出懷疑、但尚未報JFIU的情況亦在範圍內。', 'Revealing information likely to prejudice an investigation after knowing/suspecting a disclosure has been made may constitute tipping off, punishable by up to three years and a fine. The rule includes internal suspicion before an STR reaches the JFIU.'),
        ('適當而真誠的查詢本身不構成通風報訊。但若合理相信繼續CDD會令客戶察覺，可停止追查，記錄判斷依據並提交STR。', 'Proper good-faith enquiries are not themselves tipping off. If further CDD is reasonably believed to tip off the customer, the MSO may stop pursuing it, document its assessment and file an STR.'),
    ], [
        ref('03', '第1.25、5.13、7.6段', '¶1.25, 5.13, 7.6', 'has not yet been reported to the JFIU'),
    ], kind='list'),
]),
section('after-report', '報告之後：同意、抗辯與持續風險', 'After reporting: consent, defence and continuing risk', [
    block('報告不會自動清除風險', 'Reporting does not clear the relationship', [
        ('JFIU會確認收到STR。若無需立即行動（例如就戶口發限制令），一般會給予同意運作戶口；否則MSO應採取適當行動，並按需要徵詢法律意見。這是第7.24段所述處理方式，不是每份STR都必然獲同意或自動解除限制。', 'The JFIU acknowledges STR receipt. If imminent action, such as an account restraint order, is unnecessary, consent to operate the account will usually be given; otherwise the MSO should act appropriately and seek legal advice where necessary. This describes paragraph 7.24, not guaranteed consent or automatic removal of restrictions for every STR.'),
        ('法定抗辯有條件：在披露行為前報告並取得JFIU同意後才行事；或行為後主動在合理情況下盡快報告。不能把「有交STR」當作無條件免責。', 'The statutory defence is conditional: report before the disclosed acts and act with JFIU consent, or report afterwards on the MSO’s own initiative as soon as reasonable. Filing an STR is not unconditional immunity.'),
        ('提交STR後應立即適當覆核關係及採取風險緩減，必要時交高級管理層決定，不能等JFIU回覆才處理。JFIU同意不是戶口無風險證明，亦不免除其他法律、監管及聲譽風險。', 'The MSO should promptly review the relationship and apply appropriate mitigation upon filing an STR, escalating to senior management where necessary rather than waiting for JFIU feedback. Consent is not a clean bill of health and does not remove other legal, regulatory or reputational risks.'),
        ('計劃終止關係，建議在初次STR說明；之後再出現同類或不同的可疑事件，仍須向MLRO報告，由其決定是否進一步報JFIU。', 'It is recommended to indicate intended termination in the initial STR. Later suspicious events, whether similar or different, must still reach the MLRO for consideration of further JFIU reports.'),
    ], [
        ref('03', '第7.22、7.24–7.28段', '¶7.22, 7.24–7.28', 'should not be construed as a'),
    ], kind='list'),
]),
section('evidence-records', '紀錄內容：建立可重組的審計線索', 'Record content: a reconstructable audit trail', [
    block('應保存甚麼', 'Records to retain', [
        ('CDD紀錄包括客戶、實益擁有人、受款人、代表客戶行事者及關連人士的識別／核實文件、資料，簡化及加強審查、風險評估、關係目的及性質、重要業務通訊，以及異常交易背景與目的分析結果。', 'CDD records include identity/verification documents and data for customers, beneficial owners, recipients, representatives and connected parties; SDD/EDD, risk assessments, relationship purpose/nature, material correspondence and analysis of unusual transactions.'),
        ('每項本地及國際交易的文件與資料應足以重組個別交易，展示資金流及在需要時提供檢控證據。備存紀錄亦是證明合規，不只為執法而設。', 'Documents/data for each domestic and international transaction should allow reconstruction of the individual transaction and fund trail and support prosecution if needed. Records also demonstrate regulatory compliance.'),
        ('必須保存全部向MLRO作出的內部報告紀錄，亦須保留向JFIU提交的全部報告。內報紀錄應包括日期、經手職員、評估結果、有否報JFIU及文件定位；STR登記應包括日期、報告人及文件定位。兩份登記可合併。', 'All internal reports made to the MLRO and all reports to the JFIU must be retained. Internal records should show dates, handlers, assessment, whether an STR followed and document locators; the STR register should show date, reporter and document locators. The registers may be combined.'),
        ('文件可保留正本，或以微縮膠片／電腦資料庫保存副本；資料及資訊可保存在微縮膠片或電腦資料庫。應完整清晰、可迅速交予獲授權的海關、其他機關及審核人員。', 'Keep original documents or copies on microfilm/computer database; data/information may be held on microfilm or computer database. The MSO should preserve a clear, complete trail retrievable swiftly for authorised regulators, authorities and auditors.'),
        ('第8.3(d)段的「業務通訊」至少包括與CDD措施或戶口運作重大改變有關的重要通信；註66說不要求保存每一項通信，例如每封來往電郵，而是保存足以證明符合AMLO的通信。', 'Business correspondence under paragraph 8.3(d) includes, at minimum, correspondence material to CDD measures or significant account-operation changes. Note 66 does not expect every communication, such as each email, to be retained; keep enough to demonstrate AMLO compliance.'),
    ], [
        ref('03', '第7.29–7.30、8.1–8.3、8.5、8.7段', '¶7.29–7.30, 8.1–8.3, 8.5, 8.7', 'permit reconstruction of individual transactions'),
        ref('03', '第8.3(d)段及註66', '¶8.3(d); footnotes 66', 'not expected to keep each and every correspondence'),
    ], kind='list'),
]),
section('retention', '保存期限：起算點不同', 'Retention periods: different starting points', [
    block('五年與三年的分別', 'Distinguish five years from three', [
        ('業務關係CDD：整段關係期間保存，並在關係結束後至少5年繼續保存。', 'Relationship CDD: retain throughout the relationship and for at least five years after it ends.'),
        ('達CDD門檻的非經常交易CDD：自交易完成起至少5年。門檻為電傳／虛擬資產轉帳港幣8,000元，其他類型交易港幣120,000元。', 'CDD for threshold occasional transactions: retain for at least five years after transaction completion. Thresholds are HK$8,000 for wire/virtual-asset transfers and HK$120,000 for other transactions.'),
        ('交易紀錄：每宗交易完成後至少5年，期間關係結束不會縮短保存期。培訓紀錄則至少保存3年。', 'Transaction records: at least five years after completion of each transaction; ending the relationship does not shorten that period. Training records are retained for at least three years.'),
        ('關長可書面要求就指定客戶／交易延長保存期，原因包括進行中的調查或通知指定的其他目的。紀錄存放境外亦須符合香港要求。', 'The CCE may require longer retention by written notice for specified customers/transactions, including ongoing investigations or other specified purposes. Offshore storage does not remove Hong Kong requirements.'),
        ('由中介人代做CDD，機構仍負責備存紀錄。須立即取得審查資料，並確保可按要求盡快取得文件；中介服務終止時亦應確保取回文件及紀錄。', 'The MSO remains responsible when intermediaries perform CDD. CDD information must be obtained immediately and requested documents supplied as soon as reasonably practicable. The MSO should ensure records are obtained when intermediary services end.'),
    ], [
        ref('03', '第8.4、8.6、8.8–8.12、9.7段', '¶8.4, 8.6, 8.8–8.12, 9.7', 'Records should be maintained for a minimum of 3 years'),
        ref('04', '附表2第18(4)(a)–(b)條', 'Schedule 2 s.18(4)(a)–(b)', 'immediately after the intermediary has carried out'),
    ], kind='comparison'),
    block('非經常交易及未獲接納申請', 'Occasional transactions and unsuccessful applications', [
        ('依第04份綜合條例附表2第20(3A)條，相關非經常交易CDD資料的5年從交易完成起計。未獲接納申請一般沒有AMLO通常備存紀錄責任，但可疑交易報告等其他責任仍可能要求保留有用紀錄，不能一律銷毀。', 'Under consolidated Schedule 2 section 20(3A), the five years for relevant occasional-transaction CDD records start at completion. Unsuccessful applications generally do not attract the ordinary AMLO record duty, but other obligations such as STR reporting may require useful records; do not automatically destroy everything.'),
    ], [
        ref('04', '附表2第20(3A)條', 'Schedule 2 s.20(3A)', 'occasional transaction is completed'),
        ref('06', '打擊洗錢問答A28', 'AML/CFT FAQ A28', 'unsuccessful'),
    ], kind='list'),
]),
section('independent-audit', '獨立審核：範圍及匯報', 'Independent audit: scope and reporting', [
    block('審核要有獨立性及資源', 'Independence and resources', [
        ('設獨立審核職能，直接向高級管理層溝通，具足夠專長及資源；需要時亦應尋求外部覆核。', 'Establish an independent audit function with direct senior-management access and sufficient expertise/resources. Seek external review where appropriate.'),
        ('定期覆核制度、風險評估框架及RBA是否足夠；可疑交易報告制度及合規職能是否有效；相關員工的認知是否足夠。', 'Regularly review control/assessment/RBA adequacy, effectiveness of suspicious-reporting and compliance functions, and awareness of staff with AML responsibilities.'),
        ('覆核頻率及程度按業務性質、規模、複雜程度及風險決定；指引沒有為所有機構訂一個相同的固定審核週期。', 'Set review frequency and extent according to nature, size, complexity and risk; the Guideline does not impose one universal audit interval.'),
        ('交易監察參數及門檻應有紀錄、定期檢視，並經獨立驗證，確保適合機構業務及環境。', 'Document and regularly review monitoring parameters/thresholds, with independent validation of their suitability for the MSO’s operations and context.'),
    ], [
        ref('03', '第3.11–3.13、5.8段', '¶3.11–3.13, 5.8', 'direct line of communication to the senior management'),
    ], kind='list'),
    block('獨立性而非一律外聘', 'Independence does not always mean outsourcing', [
        ('獨立驗證可由外聘審核人員或具足夠專業、經驗及資源的內部職能執行；內部人員須與制度設計／實施職責適當分隔，不能自己檢查自己的工作便稱為獨立。', 'Independent validation may use external auditors or an internal function with sufficient expertise, experience and resources. Internal staff require adequate separation from design/implementation; checking one’s own work is not independence.'),
    ], [
        ref('06', '打擊洗錢問答A23', 'AML/CFT FAQ A23', 'segregation'),
    ], kind='list'),
]),
section('training', '僱員甄選、培訓及成效證據', 'Screening, training and evidence of effectiveness', [
    block('培訓政策、時間及成效', 'Training policy, timing and effectiveness', [
        ('聘用員工應有適當甄選程序，確保高標準。新員工獲聘／任命後應盡早接受初始培訓，並定期接受更新培訓；範圍及頻率按機構風險、職責和經驗調整。', 'MSOs should use appropriate recruitment screening to ensure high standards. Give new staff initial training as soon as possible after hiring/appointment and regular refreshers, tailored to institutional risk, duties and experience.'),
        ('機構應有清晰明確的培訓政策。應考慮按資源及學習需要混合網上、課堂、影片及手冊等方法；可納入FATF文章／案例，並應能向關長證明材料最新及符合現行要求。應至少保存3年紀錄，顯示誰人受訓、何時及培訓類別。', 'Maintain a clear, well-articulated training policy. MSOs are encouraged to consider a mix of online, classroom, video and manual-based methods suited to resources and learning needs; FATF papers/typologies may be included. MSOs should demonstrate to the CCE that materials are current and aligned with requirements. They should keep records of who was trained, when and what type for at least three years.'),
        ('應監察培訓成效，可採用以下三類方法：測試員工對內部程序、法定／監管責任及辨認可疑交易的理解；監察實際合規及內部報告質量／數量，以識別額外培訓需要並採行動；監察出席，跟進沒有合理原因的缺席。', 'MSOs should monitor training effectiveness. This may be achieved by: test understanding of internal procedures, statutory/regulatory obligations and suspicious-transaction recognition; monitor compliance and internal-report quality/quantity to identify further training needs and act; monitor attendance and follow up absence without reasonable cause.'),
    ], [
        ref('03', '第3.14、9.1–9.8段', '¶3.14, 9.1–9.8', 'initial training as soon as possible'),
    ], kind='list'),
    block('須記五項共同內容：第9.4段', 'Remember five common topics: paragraph 9.4', [
        ('（a）機構及個人在AMLO下的CDD和紀錄責任，以及不遵守的後果；（b）在DTROP、OSCO及UNATMO下舉報可疑交易的責任及不舉報的後果。', '(a) Institutional and personal AMLO CDD/record duties and consequences of non-compliance; (b) suspicious-reporting duties under DTROP, OSCO and UNATMO and consequences of failure.'),
        ('（c）DTROP、OSCO、UNATMO、UNSO、WMD(CPS)O及AMLO下其他與機構／個人相關的法定監管責任及違規後果；（d）內部政策程序，包括識別及舉報；（e）履行該職責所需的新興技巧、方法及趨勢。完整法例名稱見第1部分「香港法例」。', '(c) Other relevant institutional/personal statutory and regulatory duties and breach consequences under DTROP, OSCO, UNATMO, UNSO, WMD(CPS)O and AMLO; (d) internal policies/procedures, including identification/reporting; (e) emerging techniques, methods and trends needed for the role. Full ordinance names appear in Part 1’s legal framework.'),
    ], [
        ref('03', '第9.4段', '¶9.4', 'Staff should be made aware of'),
    ], kind='list'),
    block('五類職員：應理解的培訓重點', 'Five staff groups: training content to understand', [
        ('第9.5段列出或適用於不同職員的範疇，須配合職責。所有新職員，不論資歷：洗錢／恐怖分子資金籌集背景及機構重視程度；識別並向MLRO舉報可疑交易的必要，以及通風報訊罪。', 'Paragraph 9.5 gives areas that may be appropriate to different staff, tailored to roles. All new staff, irrespective of seniority: ML/TF background and its importance to the MSO; the need to identify/report suspicion to the MLRO; and tipping off.'),
        ('前線：作為與潛在洗錢人的第一接觸點，在機構策略中的重要性；與職責相關的CDD及紀錄政策程序；可疑情況、報告路線，以及何時須格外警覺。', 'Frontline: their strategic importance as the first contact with potential money launderers; role-relevant CDD and record procedures; suspicious circumstances, reporting lines and when extra vigilance is needed.'),
        ('後勤（按職責）：客戶核實及處理程序；辨識不尋常活動，尤其異常結算、付款或交付指示。', 'Back office, according to role: customer verification and processing procedures; recognition of unusual activity, especially abnormal settlement, payment or delivery instructions.'),
        ('管理人員，包括內部審計人員及CO：涵蓋制度各方面的較高層次培訓；監督／管理員工、審核制度、隨機抽查及向JFIU舉報的職責培訓。', 'Management, including internal auditors and COs: higher-level training across the whole regime; responsibilities for supervising/managing staff, auditing systems, random checks and JFIU reporting.'),
        ('MLRO：評估收到的可疑交易報告及向JFIU舉報的特定職責；並持續掌握一般打擊洗錢要求及發展。', 'MLRO: specific responsibilities for assessing reports received and reporting to the JFIU; staying current with general AML/CFT requirements and developments.'),
    ], [
        ref('03', '第9.5段', '¶9.5', 'all new staff, irrespective of seniority'),
    ], kind='list'),
]),
section('law-enforcement', '執法要求：命令與風險覆核', 'Law-enforcement requests: orders and risk review', [
    block('依命令範圍及時回應', 'Respond within the order’s scope and deadline', [
        ('設清晰程序，指派聯絡人及足夠資源處理搜查令、提交令、限制令及沒收令。搜查／提交令要求的範圍內資料須在指定期限提供；有困難時及早聯絡負責調查的人員。', 'Use clear procedures, a contact person and sufficient resources for search warrants, production, restraint and confiscation orders. Provide all material within a search/production order’s scope by its deadline; contact the investigator early if difficulties arise.'),
        ('限制令在調查期間禁止處置指定財產；MSO必須確保能扣留命令涉及的財產；命令並非必然涵蓋關係內所有資產，應考慮香港法律下仍可動用哪些資產（如有）。定罪後法院可沒收犯罪得益；恐怖分子財產亦可能被充公。', 'A restraint order prohibits dealing with specified property pending investigation; the MSO must ensure it can withhold the property covered. The order need not cover every relationship asset; consider what, if any, assets may still be used under Hong Kong law. Courts may confiscate criminal proceeds after conviction and forfeit terrorist property.'),
        ('收到法院文件或涉罪情報要求後，及時評估客戶／關係風險並判斷有否懷疑；被提及的客戶也可能是受害人，不能單憑收到文件便視為罪犯。', 'After court documents or crime-related intelligence requests, promptly assess relationship/customer risk and possible suspicion. The named customer may be a victim; receipt alone does not establish guilt.'),
    ], [
        ref('03', '第7.31–7.35段', '¶7.31–7.35', 'the customer to whom the court document relates can be a victim'),
    ], kind='list'),
    block('參考：跨境情報與正式法律協助', 'Reference: cross-border intelligence and formal legal assistance', [
        ('2022年報告所述埃格蒙特組織（Egmont Group）是各地財富情報單位（FIU）合作的網絡，支援跨境情報交換。JFIU依OSCO、DTROP及UNATMO有權交換情報，香港一方不以事先簽訂諒解備忘錄（MOU）為必要條件；若對方司法管轄區法律要求，則會考慮簽訂。', 'The 2022 report describes the Egmont Group as a network of financial intelligence units (FIUs) supporting cross-border intelligence exchange. JFIU can exchange information under OSCO, DTROP and UNATMO without an MOU being a prerequisite on the Hong Kong side; it will consider one if the counterpart jurisdiction’s law requires it.'),
        ('情報交換並不等於刑事事宜相互法律協助（MLA）：正式取證、搜查及執行境外沒收等須依適用法律協助框架處理。第25份第3.55段另說明，MLAO及FOO不適用於中國內地、澳門及台灣；當時可循法院請求書及《證據條例》處理取證／提交文件等，不能把一般境外程序一概套用。這是2022年報告的制度背景。', 'Intelligence exchange is distinct from mutual legal assistance in criminal matters (MLA): formal evidence-taking, searches and enforcement of external confiscation orders follow applicable legal frameworks. Paragraph 3.55 separately states that the Mutual Legal Assistance in Criminal Matters Ordinance (MLAO) and Fugitive Offenders Ordinance (FOO) do not apply to the Mainland, Macao or Taiwan; the report describes court letters of request and the Evidence Ordinance for evidence-taking/document production. Do not apply a single overseas procedure indiscriminately. This is the 2022 report’s institutional background.'),
    ], [
        ref('25', '2022年版，第3.49–3.57段', '2022 edition, ¶3.49–3.57', 'Financial intelligence exchange'),
    ], kind='reference'),
]),
section('periodic-return', '定期申報：半年一次及電子提交', 'Periodic returns: half-yearly electronic submission', [
    block('2025年6月30日起的安排', 'Arrangement effective 30 June 2025', [
        ('每年兩次，涵蓋1月1日至6月30日及7月1日至12月31日。原有每季四次安排已由第15份通函改為半年制；不要把舊機制當作現行安排。', 'Submit twice yearly for 1 January–30 June and 1 July–31 December. Document 15 replaces the former quarterly/four-per-year mechanism with half-yearly returns.'),
        ('必須透過金錢服務經營者牌照系統（MSOS）電子提交，不再接受紙本，應預先開立帳戶。首份新版申報涵蓋2025年上半年，2025年7月1日起提交。', 'Submit electronically through MSOS; paper submissions are no longer accepted. Set up an account in advance. The first revamped return covers the first half of 2025 and opens for submission on 1 July 2025.'),
        ('新增資料包括兌換涉及的外幣、匯款涉及的司法管轄區及交付渠道。兌換部分只填兌換資料，不混入匯款；按要求以金額遞減排列。匯款渠道及客戶類型的各組比例合計須為100%。', 'Additional data include foreign currencies exchanged, remittance jurisdictions and delivery channels. Money-changing fields exclude remittance amounts and use descending amounts where requested. Each set of remittance channel/customer-type ratios totals 100%.'),
        ('另填CDD／EDD及拒絕交易數字、向JFIU報告的可疑交易數目、收到的不予同意通知／限制令／沒收令，以及提交日香港金錢服務業務的估計資產總額（港幣）。', 'Also report CDD/EDD and rejected-transaction counts, suspicious transactions reported to the JFIU, no-consent letters/restraint/confiscation orders received, and estimated Hong Kong money-service assets in HKD at submission date.'),
        ('須按關長指定形式及時提交；逾期可導致牌照暫時吊銷及／或撤銷。半年是資料涵蓋期，不能自行當作提交截止日。', 'Submit on time in the CCE’s specified form; late submission may lead to suspension/revocation. The half-year is the reporting period, not an inferred filing deadline.'),
    ], [
        ref('15', '正文第1–2頁及附件第3–5頁', 'Main text pp.1–2; annex pp.3–5', 'The new lodgement arrangement is on a half-yearly basis'),
    ], kind='list'),
    block('提交期限', 'Filing deadline', [
        ('第05份2026年5月發牌指引第11.2段訂明：除非關長另以書面指定，須在每個半年度開始起兩星期內提交。申報涵蓋上半年度／下半年度資料；不能把半年資料期間誤作可等半年才提交。', 'Paragraph 11.2 of the May 2026 Licensing Guide requires submission within 2 weeks beginning each half-year, unless otherwise specified in writing by the CCE. Returns cover the preceding half-year’s data; the reporting period does not grant a further six months to file.'),
    ], [
        ref('05', '第11.2段', '¶11.2', 'within 2 weeks'),
    ], kind='list'),
]),
section('safe', '懷疑的評估與呈報流程', 'Assessing and reporting suspicion', [
    block('SAFE四步', 'The four SAFE steps', [
        ('S：篩查交易／客戶，找出可疑指標。', 'S — Screen the customer/transaction for suspicious indicators.'),
        ('A：在適當及不致通風報訊的範圍內向客戶查詢，了解理由。', 'A — Ask appropriate questions to understand the rationale without tipping off.'),
        ('F：找出並考慮所有已知及可合理取得的紀錄，包括客戶資料及其他關連交易。', 'F — Find and consider known/reasonably available records, including customer information and linked transactions.'),
        ('E：評估全部資料；懷疑仍在則按內部及法定程序呈報，記錄結論及理由。此流程不可用作拖延已須作出的披露。', 'E — Evaluate all information; report remaining suspicion through internal/statutory procedures and record conclusions/reasons. The process cannot justify delaying disclosure already due.'),
    ], [
        ref('03', '第7.11–7.14段', '¶7.11–7.14', 'SAFE'),
    ], kind='flow'),
]),
])
