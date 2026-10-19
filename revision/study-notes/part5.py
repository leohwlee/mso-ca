"""Source-authored bilingual manuscript; source-checked 2026-10-19. No bank input."""
from model import p, ref, block, section

PART = dict(title=p('金錢服務經營者的系統及管控措施（一）：機構管治及策略', 'MSO systems and controls (i): institutional governance and strategy'),
intro=p('先理解機構承受甚麼風險，再把管理責任、資源、制度及覆核連起來。風險為本不代表可以免除法定責任。', 'Start with the risks faced by the institution, then connect management accountability, resources, controls and review. A risk-based approach does not waive statutory duties.'), sections=[
section('risk-based', '風險為本方法：資源與風險相稱', 'Risk-based approach: match resources to risk', [
    block('核心概念', 'Core concept', [
        ('風險為本方法（RBA）是識別、評估和了解洗錢／恐怖分子資金籌集風險，然後採取相稱措施管理及減低風險。資源應優先放在較高風險範疇。', 'The risk-based approach (RBA) means identifying, assessing and understanding ML/TF risks, then managing and mitigating them with proportionate measures. Resources should focus on higher-risk areas.'),
        ('機構風險評估針對整個業務；客戶風險評估針對某客戶或擬建立的關係。前者決定制度設計，後者決定盡職審查及持續監察的程度。', 'Institutional assessment concerns the business as a whole; customer assessment concerns an individual customer or proposed relationship. The former shapes the control framework; the latter determines the extent of CDD and ongoing monitoring.'),
        ('低風險可支持相稱的簡化措施，但一般仍須完成四項盡職審查及持續監察；有懷疑時不可簡化制度。', 'Low risk can support proportionate simplification, but the four CDD measures and ongoing monitoring generally remain necessary. Systems cannot be simplified where ML/TF is suspected.'),
    ], [
        ref('03', '第2.1、2.13–2.16、3.3段', '¶2.1, 2.13–2.16, 3.3', 'allocate its resources more effectively'),
    ], kind='list'),
    block('理解：風險管理與迴避風險', 'Understand: risk management and de-risking', [
        ('2022年報告專題5.6指出，迴避風險（de-risking）與風險為本的核心理念相悖；銀行的打擊洗錢制度也應顧及正當企業及居民取得必要服務。學習上須分清：評估個別風險並採相稱措施，與單憑所屬類別便籠統排除客戶。這不代表MSO必須接受所有客戶；無法完成CDD或法律禁止交易等情況，仍須按適用規則拒絕／終止及考慮STR（見Part 6核實時間與審查失敗）。', 'Box 5.6 of the 2022 report explains that de-risking conflicts with the core RBA philosophy and that banking AML controls should preserve legitimate businesses’ and residents’ access to essential services. Distinguish individual risk assessment and proportionate mitigation from blanket exclusion based on category alone. This does not require an MSO to accept every customer: inability to complete CDD or legal transaction prohibitions still require the applicable refusal/termination and STR consideration (see Part 6 on timing and failed CDD).'),
    ], [
        ref('25', '2022年版，第5.2節專題5.6（中文第61頁）', '2022 edition, section 5.2 Box 5.6 (English p.72)', 'Box 5.6 - De-risking'),
        ref('03', '第2.1、4.13.1段', '¶2.1, 4.13.1', 'allocate its resources more effectively'),
    ], kind='list'),
]),
section('institutional-assessment', '機構風險評估：因素、程序及更新', 'Institutional assessment: factors, process and updates', [
    block('評估涵蓋甚麼', 'Assessment scope', [
        ('客戶：目標市場及客戶組別，以及高風險客戶的數目和比例。國家：客戶來自／所在的司法管轄區，以及機構營運地點。', 'Customers: target markets and segments, and the number and proportion of high-risk customers. Countries: customer origins/locations and the jurisdictions where the MSO operates.'),
        ('產品、服務及交易：業務的性質、規模、多樣性和複雜程度；非經常交易、匿名性、交易量與客戶背景是否相符，以及科技可能受濫用的程度。', 'Products, services and transactions: nature, scale, diversity and complexity; occasional transactions, anonymity, consistency of volumes with customer profiles, and vulnerability of technology to abuse.'),
        ('交付渠道：直接接觸客戶的程度、依賴第三方執行審查的程度、代理／對手機構網絡，以及付款鏈和結算系統的複雜性。', 'Delivery channels: direct customer contact, reliance on third parties for CDD, agent/counterpart networks, and the complexity of payment chains and settlement systems.'),
        ('其他因素包括人手及培訓資源的質素、監管及合規發現，以及內外審核結果。國家風險亦應考慮貪污／有組織罪行、執法、制度效能及實益擁有權透明度；必須納入關長通知的較高風險，並按第09份通函盡快評估擴散融資風險。', 'Other factors include staff/training resources, regulatory/compliance findings and audits. Country risk also considers corruption/organised crime, enforcement, regime effectiveness and beneficial-ownership transparency. Include higher risks notified by the CCE and assess PF promptly under document 09.'),
    ], [
        ref('03', '第2.2–2.6段', '¶2.2–2.6', 'the number and proportion of customers identified as high risk'),
        ref('09', '正文第1–2頁', 'Main text pp.1–2', 'proliferation financing'),
    ], kind='list'),
    block('完成及維持評估', 'Complete and maintain the assessment', [
        ('記錄識別及評估程序，結合內外來源的定量及定性資料；先考慮全部相關因素，再判定整體風險及緩解措施。評估結果須獲高級管理層批准。', 'Document identification and assessment using quantitative and qualitative internal/external information. Consider all relevant factors before determining overall risk and mitigation. Senior management must approve the results.'),
        ('至少每兩年評估一次，並在重大觸發事件發生時重做，例如嚴重制度違規、新客戶組別／渠道／產品，或流程、目標客戶及業務對手出現重大改變。覆核結果須記錄及獲管理層批准。', 'Assess every two years and upon material triggers: significant control breaches, new customer segments/channels/products, or significant changes to processes, target customers or counterparties. Document the review and obtain management approval.'),
        ('保存風險因素、資料來源、制度是否足夠及適當的評價，並設機制在海關關長要求時提供評估。小型、簡單業務可用較簡單的方法，並非免做評估。', 'Keep the factors, information sources and evaluation of control adequacy/appropriateness, and be able to provide the assessment to the CCE. Smaller, simpler businesses may use a simpler method; they are not exempt from assessment.'),
        ('本地成立而有分行或附屬公司的機構須作集團評估。可參考或依賴集團／地區評估，但必須充分反映本地機構的風險。', 'A locally incorporated MSO with branches/subsidiaries must assess group-wide risk. Group/regional assessments may be used only where they adequately reflect the MSO’s local risks.'),
    ], [
        ref('03', '第2.3、2.5–2.10段', '¶2.3, 2.5–2.10', 'conduct its assessment every two years'),
    ], kind='list'),
]),
section('customer-assessment', '客戶風險評估：初評、定案及持續更新', 'Customer risk assessment: initial rating, finalisation and updates', [
    block('建立有依據的分級框架', 'An evidence-based rating framework', [
        ('機構應建立客戶風險評估框架，判定每位客戶的洗錢／恐怖分子資金籌集風險及CDD／持續監察程度。CDD初期先評估以決定審查程度，再統合審查、交易及背景資料定案，支持是否建立、繼續或終止關係的決定。', 'Maintain a framework determining each customer’s ML/TF risk and CDD/monitoring intensity. Assess at the initial CDD stage to set its extent, then finalise using the holistic CDD, transaction and background information to support whether to enter, continue or terminate the relationship.'),
        ('綜合客戶背景、業務關係目的／性質、產品／服務、交易規模／數量／複雜性、地理及交付渠道等因素；國籍或單一數值不能代替整體分析。各因素權重、分級界線及例外須有合理依據。', 'Consider background, relationship purpose/nature, products/services, transaction size/volume/complexity, geography and channels. Nationality or one score cannot replace holistic analysis. Weights, rating boundaries and exceptions need a reasonable basis.'),
        ('記錄評估、資料及理由，適當時記錄管理層批准；隨審查、交易及客戶變化持續更新。機構分級須可理解及一致，不能為降低CDD程度而任意把高風險改為低風險。', 'Document assessments, information and reasons, including management approval where appropriate; update with CDD, transactions and customer changes. Ratings must be understandable/consistent, not arbitrarily lowered to reduce CDD.'),
    ], [
        ref('03', '第2.13–2.16段', '¶2.13–2.16', 'finalise the customer risk assessment'),
    ], kind='list'),
]),
section('new-business', '新產品、渠道與科技：推出前評估', 'New products, channels and technology: assess before launch', [
    block('時間與責任', 'Timing and responsibility', [
        ('在發展新產品、新業務做法或新交付機制，以及為新／現有產品使用新或發展中的科技之前，先識別及評估風險，並採取適當管理及緩解措施。', 'Before launching new products, business practices or delivery mechanisms, or using new/developing technology for new or existing products, identify and assess the risks and put appropriate mitigation in place.'),
        ('新渠道投入使用後，重大業務改變亦是更新機構風險評估的觸發事件；不能只在產品獲批時評估一次。', 'After launch, material business changes also trigger institutional reassessment; assessment is not confined to initial product approval.'),
    ], [
        ref('03', '第2.9、2.11–2.12段', '¶2.9, 2.11–2.12', 'prior to the launch of the new'),
    ], kind='list'),
]),
section('control-framework', '內控制度的組成與簡化條件', 'Control framework and conditions for simplification', [
    block('制度最低架構', 'Minimum framework', [
        ('按業務性質、規模、複雜程度及風險建立制度，至少包括合規管理安排、獨立審核、僱員甄選及持續培訓。制度須由高級管理層批准，監察執行情況並在需要時改善。', 'Build systems proportionate to nature, size, complexity and risk, including compliance management, independent audit, employee screening and continuing training. Senior management approves them; implementation is monitored and improved when necessary.'),
        ('機構須採取一切合理措施，確保有適當保障防止違反附表2第2或3部，並減低洗錢及恐怖分子資金籌集風險。', 'Take all reasonable measures to provide safeguards against contraventions of Schedule 2 Parts 2 or 3 and to mitigate ML/TF risks.'),
        ('制度簡化須同時符合：仍遵守法定及指定評估／管理要求、由適當評估識別較低風險，以及簡化制度獲管理層批准並不時覆核。有洗錢／恐怖分子資金籌集懷疑時不得簡化。', 'Simplification requires continued statutory and specified assessment/management compliance, lower risk established by appropriate assessment, and management-approved simplified systems subject to review. Suspicion bars simplification.'),
    ], [
        ref('03', '第3.1–3.4段', '¶3.1–3.4', 'an independent audit function'),
    ], kind='list'),
]),
section('roles', '高級管理層、合規主任與洗錢報告主任', 'Senior management, CO and MLRO', [
    block('三個角色的分工', 'Responsibilities of the three roles', [
        ('高級管理層須了解及有效管理機構風險，實施制度；任命管理層級的合規主任（Compliance Officer，CO）建立及維持制度，並任命高級職員為洗錢報告主任（Money Laundering Reporting Officer，MLRO），作可疑交易報告聯絡點。', 'Senior management understands and manages risk and implements systems. It appoints a management-level Compliance Officer (CO) to establish and maintain controls, and a senior Money Laundering Reporting Officer (MLRO) as the suspicious-reporting focal point.'),
        ('合規主任：制定及持續覆核制度、監察效能及改善措施、向高級管理層傳達重大合規問題，並確保培訓足夠、適當和有效。', 'CO: develops and continually reviews systems, monitors effectiveness and improvements, communicates significant compliance issues to management, and ensures adequate, appropriate and effective training.'),
        ('洗錢報告主任：評估內部披露及例外報告，結合全部相關資料決定是否向聯合財富情報組（JFIU）舉報；保存評估紀錄及提供避免通風報訊的指引。', 'MLRO: assesses internal disclosures and exception reports with all relevant information, decides whether to report to the JFIU, keeps review records and guides staff on avoiding tipping off.'),
        ('視機構規模，CO與MLRO可以由同一人兼任；兼任不會免除任一角色的職責。', 'Depending on size, the same person may be CO and MLRO; both sets of responsibilities remain.'),
    ], [
        ref('03', '第3.5–3.10段及註9', '¶3.5–3.10; footnotes 9', 'functions of CO and MLRO may be performed by the same'),
    ], kind='comparison'),
    block('職位履職條件', 'Conditions enabling the roles', [
        ('在切實可行範圍內，確保資格及知識足夠、具適當資歷與權力、通常在香港工作，並在規模限制下獨立於營運和業務職能。', 'As far as practicable, ensure suitable qualifications/knowledge, seniority and authority, normal Hong Kong location and, subject to size constraints, independence from operational/business functions.'),
        ('須能及時取得內部審查及外部監管資料、定期接觸並在需要時直接接觸高級管理層；提供足夠人手、資源及缺席時的替代安排。管理資訊要及時、完整、清晰及準確。', 'Enable timely access to internal CDD and external regulatory information, regular/direct management access when needed, sufficient resources/staff and absence cover. Management information must be timely, complete, understandable and accurate.'),
    ], [
        ref('03', '第3.6、3.8段', '¶3.6, 3.8', 'normally based in Hong Kong'),
    ], kind='list'),
    block('任職形式', 'Appointment basis', [
        ('合規主任及洗錢報告主任須為僱員，但由獨資經營者、合夥人、董事或最終擁有人擔任者除外。不能只借用外部顧問名銜而無實際職權與投入。', 'CO and MLRO must be employees unless the role is held by the proprietor, partner, director or ultimate owner. An external adviser’s title alone does not provide actual authority or engagement.'),
    ], [
        ref('05', '第4.15(a)段', '¶4.15(a)', 'employee under the definition'),
    ], kind='list'),
    block('管理資料的接收人及替補安排', 'Management-information recipients and deputy cover', [
        ('管理資料須及時、完整、易明及準確地向高級管理層傳達。應在切實可行範圍提供足夠資源及缺席替補安排；如切實可行，應安排替代／代理CO及MLRO，而其應具相同地位。', 'Timely, complete, understandable and accurate management information goes to the board/delegated committee where applicable and senior management. As far as practicable provide sufficient resources and absence cover; an alternate/deputy CO and MLRO should, where practicable, have the same status.'),
    ], [
        ref('03', '第3.6、3.8(h)段', '¶3.6, 3.8(h)', 'an alternate or deputy CO and MLRO'),
    ], kind='list'),
]),
section('group-controls', '海外分行及附屬公司：集團制度', 'Overseas branches and subsidiaries: group controls', [
    block('適用範圍與較高標準', 'Scope and higher standards', [
        ('香港成立的機構，其海外分行或附屬公司從事與條例所界定金融機構相同的業務，須在適用範圍內實施集團打擊洗錢制度，包括類似附表2的盡職審查及備存紀錄程序。', 'A Hong Kong-incorporated MSO applies group-wide controls to overseas branches/subsidiaries carrying on the same business as an AMLO financial institution, where relevant, including comparable CDD and record-keeping procedures.'),
        ('在當地法律容許範圍內，採用香港與所在地兩套規定中較高的標準。當地法律不容許採用較高標準時，通知海關關長，並採取額外措施有效減低由此產生的風險。', 'Apply the higher of Hong Kong and host requirements to the extent host law permits. If host law prevents that, inform the CCE and take additional measures effectively mitigating the resulting risks.'),
        ('集團內可為盡職審查及風險管理分享資料，並在需要時向集團合規、審核及打擊洗錢職能提供客戶、戶口和交易資料；須符合法律及保密、用途限制、避免通風報訊等保障。', 'Share information for CDD/risk management and, where necessary, customer/account/transaction information with group compliance, audit and AML functions, subject to law and safeguards for confidentiality, permitted use and prevention of tipping off.'),
    ], [
        ref('03', '第3.15–3.19段', '¶3.15–3.19', 'apply the higher of the two sets of requirements'),
    ], kind='list'),
    block('遷冊來港實體', 'Re-domiciled entities', [
        ('第04份綜合條例附表2第22條亦涵蓋遷冊來港實體的海外分行／附屬公司要求；不能因較早指引只提香港成立機構，便忽略此法定適用範圍。', 'Schedule 2 section 22 in the consolidated Ordinance also covers re-domiciled entities’ overseas branches/subsidiaries. The older Guideline’s reference to Hong Kong incorporation does not remove that statutory scope.'),
    ], [
        ref('04', '附表2第22條', 'Schedule 2 s.22', 'a re-domiciled entity'),
    ], kind='list'),
    block('異常交易分析與集團雙向分享', 'Unusual-transaction analysis and two-way group sharing', [
        ('在法律容許、保密／用途及防通風報訊保障下，集團分享應包括已完成的異常交易／活動分析；可包括STR、底層資料或已呈報事實，並非一律強制分享每份STR。集團職能亦應在風險管理相關及適當時，向分行／附屬公司回傳資料。', 'Subject to law and confidentiality/use/tipping-off safeguards, sharing should include unusual-transaction/activity analysis if done. It could include an STR, underlying information or the fact of reporting, rather than requiring every STR to be shared. Group functions should also return relevant/appropriate risk-management information to branches/subsidiaries.'),
    ], [
        ref('03', '第3.17段及註11', '¶3.17; footnotes 11', 'This should include information and analysis of transactions or activities which appear unusual'),
    ], kind='list'),
]),
section('business-plan', '業務計劃：把營運模式交代完整', 'Business plan: explain the complete operating model', [
    block('提交內容', 'Required content', [
        ('業務計劃讓金錢服務監理科了解擬議業務及運作模式，須同時處理營運與合規目標，並有足夠資源執行。資料不足可延誤或妨礙牌照申請。', 'The plan enables the MSSB to understand the proposed business and operating model. It addresses operational and compliance objectives with resources to execute them. Missing information may delay or hinder licensing.'),
        ('機構背景：公司／業務名稱、網站、標誌及商標；歷史、資本來源和集團關係；高級管理人員國籍、經驗、資格及教育；決策地點及境內外後勤辦事處。', 'Background: company/business names, website, logo/trademark; history, capital sources and group links; senior executives’ nationality, experience, qualifications and education; decision-making location and local/overseas back offices.'),
        ('客戶及交易：預期客戶的所在地、國籍及接觸方式；在港業務和申請牌照原因；由落單、處理、資金流、合規至會計／備存紀錄的完整流程。', 'Customers and transactions: expected customer location, nationality and contact methods; Hong Kong operations and reasons for licensing; the entire process from instructions and processing through fund flows, compliance, accounting and records.'),
        ('產品及渠道：產品服務與推出時間、各地代理／海外經營者及服務協議、對手不履約時保護客戶資金的措施。交代銀行戶口號碼及擁有人，不可用第三方銀行戶口；不用銀行戶口者須說明如何經營。', 'Products/channels: services and launch dates, overseas agents/MSOs and agreements, and protection of customer funds against counterparty non-performance. Identify business bank accounts and owners; third-party bank accounts are not allowed. Explain operations if no bank account is needed.'),
        ('財務及架構：未來兩年各產品的預期利潤率及營業額、日常營運資本、本地及海外集團架構圖、共用處所其他業務的性質及關係，以及本地管理層／僱員的職責、人數、全兼職與匯報線。', 'Finance/structure: two-year expected margins and turnover by product, working capital, local/international group charts, other businesses sharing premises and their relationships, and local management/staff numbers, duties, full/part-time status and reporting lines.'),
        ('其他安排：外判服務、自動化／篩查系統、作代理或主事人的角色、第三方付款平台、實體現金運送，以及其他監管機構的監管情況。計劃須書面確認：申請資料變更後一個月內通知關長。', 'Other arrangements: outsourcing, automated/screening systems, agency/principal roles, third-party payment platforms, physical cash movements and other regulatory supervision. Confirm in writing that changes to licensing particulars will be notified within one month.'),
    ], [
        ref('20', '第1–17項及引言', 'Introduction and items 1–17', 'No third party bank account is allowed'),
    ], kind='list'),
]),
section('policy', '打擊洗錢政策：與本身業務及風險連接', 'AML/CFT policy: connect controls to the actual business', [
    block('政策須可以實際執行', 'An operational policy', [
        ('先做自身風險評估，再按產品、渠道、架構、客戶及地理風險制定政策、程序和管控措施。提交指引的清單不是盡列，不能直接套用與本身業務不符的範本。', 'Assess the MSO’s own risks first, then design policies, procedures and controls for its products, channels, structure, customers and geographical risks. The submission checklist is non-exhaustive; a generic template is insufficient.'),
        ('政策須交代法律框架、CO／MLRO及匯報線、CDD觸發門檻與相連交易、客戶風險評估、簡化／加強審查、政治人物、非親身渠道、高風險國家、財富及資金來源，以及審查失敗的處理。', 'Explain the legal framework, CO/MLRO/reporting lines, CDD thresholds and linked transactions, customer risk assessment, SDD/EDD, PEPs, non-face-to-face channels, higher-risk countries, wealth/fund sources and failed CDD.'),
        ('說明持續客戶及交易監察、紀錄保存與檢索、產品／貨幣／目標客戶／匯款地區／收入模式、付款及結算流程、代理／海外分支監察，以及制裁與政治人物篩查。', 'Describe ongoing customer/transaction monitoring, record retention/retrieval, products/currencies/target customers/remittance jurisdictions/revenue, payment and settlement flows, overseas branch/agent supervision and sanctions/PEP screening.'),
        ('列出合規管理、可疑交易辨識及舉報、獨立審核、按職責提供培訓及成效監察、其他內控和配合海關／執法機構的安排。可附開戶、風險評估及內部報告表格，展示如何落實。', 'Set out compliance management, suspicious-transaction detection/reporting, independent audit, role-based training and effectiveness monitoring, other controls and cooperation with regulators/law enforcement. Attach onboarding, risk-assessment and internal-report forms to demonstrate implementation.'),
        ('政策文件中的「例如一天內檢索紀錄」是檢索能力示例，不是把所有法定期限統一改成一天；實際法律及個別命令的期限仍須分開遵守。', 'The policy guide’s example of retrieving records within one day illustrates retrieval capability; it does not replace every legal deadline with a one-day rule. Apply the relevant law and individual orders separately.'),
    ], [
        ref('21', '引言、第1–19項', 'Introduction; items 1–19', 'say one day'),
    ], kind='list'),
]),
])
