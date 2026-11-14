"""Source-authored bilingual manuscript. Review scope: depth-review-2026-10-20/REPORT.md."""
from model import p, ref, block, section

PART = dict(title=p('有關打擊洗錢及恐怖分子資金籌集與打擊擴散資金籌集的常識', 'General knowledge on AML/CFT and Counter Proliferation Financing'),
intro=p('理解資金如何被濫用、香港的法律與風險背景，以及制裁和跨境現金申報的作用。', 'Understand how funds are misused, Hong Kong’s legal and risk context, and the roles of sanctions and cross-boundary cash declarations.'), sections=[
section('money-laundering', '洗錢：犯罪得益及三個階段', 'Money laundering: criminal proceeds and three stages', [
    block('定義與過程', 'Definition and process', [
        ('洗錢的法定定義著重行為的意圖：令犯罪得益或全部／部分、直接／間接代表該得益的財產，表面上不像犯罪得益。另須區分DTROP／OSCO第25條的處理犯罪得益罪：處理財產時知道或有合理理由相信它代表犯罪得益。財產不限現金，亦不必表面可疑。', 'The statutory ML definition concerns an act intended to make crime proceeds, or property wholly/partly and directly/indirectly representing them, appear not to be such proceeds. Distinguish the DTROP/OSCO section 25 dealing offence: dealing while knowing or having reasonable grounds to believe the property represents crime proceeds. Property is not limited to cash and need not look suspicious.'),
        ('存放：把犯罪現金放入金融體系，例如分拆存款或兌換。分層：透過多次轉移、不同帳戶或司法管轄區掩藏來源。整合：使資金以投資、資產或業務收益等形式重新出現為合法財富。', 'Placement introduces criminal cash into the financial system, for example through split deposits or exchange. Layering obscures its origin through transfers, accounts or jurisdictions. Integration returns it as apparently legitimate investments, assets or business income.'),
        ('三個階段是理解典型模式的工具，實際交易可同時涉及多個階段。匯款或兌換業務可能協助存放及分層，交易有商業外觀也不表示資金合法。', 'The stages explain typical patterns; actual transactions can overlap them. Remittance and exchange can facilitate placement and layering, and a commercial appearance does not establish legitimacy.'),
    ], [
        ref('03', '第1.9–1.10段', '¶1.9–1.10', 'Placement - the disposal'),
    ], kind='list'),
    block('財產及境外犯罪得益的涵義', 'Property and proceeds from overseas conduct', [
        ('AMLO的財產不限於現金，也包括貨品、據法權產及土地，不論在香港或境外；以及由該等財產產生的義務、地役權、各類產業／權益／收益，無論現在或將來、既得或或有。洗錢不能只以有沒有實體鈔票判斷。', 'AMLO property includes money, goods, choses in action and land in Hong Kong or elsewhere, and associated obligations, easements, estates, interests and profits, present/future and vested/contingent. Choses in action are rights enforceable by legal action; laundering is not limited to physical banknotes.'),
        ('洗錢定義涵蓋香港可公訴罪行所得，以及若在香港發生便會構成可公訴罪行的境外行為所得；財產可全部／部分、直接／間接代表得益。「境外所得」並不自動免除香港洗錢風險。', 'The ML definition covers proceeds of Hong Kong indictable offences and overseas conduct that would constitute an indictable offence in Hong Kong. Property may represent proceeds wholly/partly and directly/indirectly. Overseas origin does not by itself remove Hong Kong laundering risk.'),
    ], [
        ref('04', '附表1第1部第1條', 'Schedule 1 Part 1 s.1', 'choses in action'),
        ref('03', '第1.9段', '¶1.9', 'not to appear to be or so represent such proceeds'),
    ], kind='list'),
]),
section('terrorist-financing', '恐怖分子資金籌集：合法資金也可被濫用', 'Terrorist financing: legitimate funds can also be misused', [
    block('與洗錢的分別', 'Distinction from money laundering', [
        ('恐怖分子資金籌集包括：有意圖或知道財產會全部／部分用於恐怖主義行為而提供／籌集財產，不論是否實際使用；向某人提供財產／金融或相關服務，或為其利益籌集財產／要求服務，而知道或罔顧該人是否恐怖分子或聯繫者。可直接或間接進行，不能只看資金來源。', 'TF includes providing/collecting property intending or knowing it will be used wholly/partly for terrorist acts, whether actually used or not; making property or financial/related services available to a person, or collecting property/soliciting services for their benefit, knowing or reckless as to whether they are a terrorist/associate. Direct and indirect activity is covered; origin alone is insufficient.'),
        ('洗錢著重犯罪得益的來源；恐怖活動可以由合法收入、捐款或犯罪收入資助。金額小、來源合法或經註冊組織轉移，均不能自動排除恐怖分子資金籌集風險。', 'Money laundering concerns the criminal origin of proceeds. Terrorist activity may be funded by legitimate income, donations or crime. Small amounts, lawful origins or transfers through registered organisations do not automatically exclude TF risk.'),
    ], [
        ref('03', '第1.11–1.12、1.23–1.25段', '¶1.11–1.12, 1.23–1.25', 'terrorist financing'),
    ], kind='list'),
]),
section('legal-framework', '香港法律：各條例處理的問題', 'Hong Kong’s laws: the role of each ordinance', [
    block('六組核心法例', 'Six core legal frameworks', [
        ('第615章《打擊洗錢及恐怖分子資金籌集條例》（AMLO）：訂明客戶盡職審查、備存紀錄、監管及金錢服務經營者發牌制度。第405章《販毒（追討得益）條例》（DTROP）及第455章《有組織及嚴重罪行條例》（OSCO）：處理犯罪得益、披露、調查、限制及沒收。', 'Cap.615 AMLO establishes CDD, record-keeping, supervision and MSO licensing. Cap.405 DTROP and Cap.455 OSCO address criminal proceeds, disclosure, investigation, restraint and confiscation.'),
        ('第575章《聯合國（反恐怖主義措施）條例》（UNATMO）：恐怖分子財產、相關服務及披露。第537章《聯合國制裁條例》（UNSO）：在香港實施聯合國安全理事會決議所要求的制裁。第526章《大規模毀滅武器（提供服務的管制）條例》：管制可能協助大規模毀滅武器發展、生產、獲取、儲存及運載方式的服務；有合理理由相信或懷疑服務可能涉及擴散融資時，禁止提供。', 'Cap.575 UNATMO addresses terrorist property, related services and disclosure. Cap.537 UNSO implements sanctions required by UN Security Council resolutions. Cap.526 controls services that will/may assist WMD development, production, acquisition, stockpiling or delivery, and prohibits services where the provider believes or suspects on reasonable grounds that they may be connected to PF.'),
        ('第405／455章的洗錢罪最高可罰款500萬元及監禁14年；不披露知悉／懷疑事項最高可罰款5萬元及監禁3個月；通風報訊最高可監禁3年。恐怖分子資金籌集相關罪行可監禁14年及罰款。須分清犯罪、披露及監管處分是不同責任。', 'The DTROP/OSCO laundering offence carries up to HK$5 million and 14 years. Failure to disclose carries up to HK$50,000 and three months; tipping-off up to three years. Relevant TF offences carry up to 14 years and a fine. Criminal liability, disclosure duties and regulatory sanctions are distinct.'),
        ('第1.20段：除其他事項外，OSCO (a) 賦予香港警方及香港海關人員調查有組織罪行及三合會活動的權力；(b) 賦予法院司法管轄權，沒收有組織及嚴重罪行的得益，並就被告人的財產發出限制令及押記令；(c) 增訂一項有關可公訴罪行得益的洗錢罪行；(d) 容許法院在適當情況下收取違法者及罪行的資料，以決定是否適宜作出更重的判刑。', 'Paragraph 1.20: among other things, OSCO (a) gives Police and Customs and Excise officers powers to investigate organized crime and triad activities; (b) gives the Courts jurisdiction to confiscate proceeds of organized and serious crimes and to issue restraint and charging orders over a defendant’s property; (c) creates an ML offence for proceeds of indictable offences; and (d) enables the Courts, in appropriate circumstances, to receive information about an offender and an offence to decide whether a greater sentence is appropriate.'),
    ], [
        ref('03', '第1.14–1.27、6.1–6.4段', '¶1.14–1.27, 6.1–6.4', 'imprisonment for 14 years'),
    ], kind='list'),
    block('六項法例的英文全名及常用縮寫', 'Full names behind the six legal abbreviations', [
        ('AMLO是第615章《打擊洗錢及恐怖分子資金籌集條例》；DTROP是第405章《販毒（追討得益）條例》；OSCO是第455章《有組織及嚴重罪行條例》。不要把一般犯罪得益的洗錢責任只限於毒品得益。', 'AMLO: Anti-Money Laundering and Counter-Terrorist Financing Ordinance, Cap.615. DTROP: Drug Trafficking (Recovery of Proceeds) Ordinance, Cap.405. OSCO: Organized and Serious Crimes Ordinance, Cap.455. Laundering liability for indictable-crime proceeds is not confined to drug proceeds.'),
        ('UNATMO是第575章《聯合國（反恐怖主義措施）條例》；UNSO是第537章《聯合國制裁條例》；WMD(CPS)O是第526章《大規模毀滅武器（提供服務的管制）條例》。三者分別涉及反恐措施、聯合國制裁及可能協助大規模毀滅武器的服務，不能混成同一項禁令。', 'UNATMO: United Nations (Anti-Terrorism Measures) Ordinance, Cap.575. UNSO: United Nations Sanctions Ordinance, Cap.537. WMD(CPS)O: Weapons of Mass Destruction (Control of Provision of Services) Ordinance, Cap.526. Their counter-terrorism, UN-sanctions and WMD-service controls are distinct.'),
    ], [
        ref('03', '第1.14、1.19–1.27段', '¶1.14, 1.19–1.27', 'Drug Trafficking (Recovery of Proceeds)'),
    ], kind='list'),
    block('用語邊界：指引中的金融機構', 'Terminology boundary: financial institutions in the Guideline', [
        ('第03份的用語一般沿用AMLO涵義；詞彙表特別說明，FI（Financial Institution，金融機構）除另有指明外，採FATF建議的定義。寫明「AMLO所界定的金融機構」時，才用該法定範圍。不能把指引所有FI字眼都直接當成同一份香港機構牌照清單；本地電傳、合資格中介人及SDD各有具體定義／條件，見第3部分及第6部分。', 'Terms in document 03 generally follow AMLO meanings. Its glossary specifically says FI (Financial Institution) follows the FATF Recommendations unless otherwise specified, for example “an FI as defined in the AMLO”. Do not read every FI reference as the same list of Hong Kong licensed institutions. Domestic wires, eligible intermediaries and SDD have their own specified definitions/conditions in Parts 3 and 6.'),
    ], [
        ref('03', '第1.2段及「主要用語及縮寫詞彙」金融機構條目', '¶1.2 and Glossary, Financial institution(s)', 'unless specified otherwise'),
    ], kind='list'),
]),
section('international', 'FATF與司法管轄區風險', 'FATF and jurisdiction risk', [
    block('標準、名單與法律須分開理解', 'Distinguish standards, lists and law', [
        ('財務行動特別組織（FATF）是1989年成立的跨政府組織，制定標準並推動法律、監管及操作措施的有效實施，以打擊洗錢、恐怖分子資金籌集及擴散資金籌集。香港是成員，須實施最新建議。特別組織透過司法管轄區相互評估及嚴格跟進監察合規，並識別高風險及其他受監察地區；建議不是香港法例的替代品。', 'The Financial Action Task Force (FATF), an inter-governmental body formed in 1989, sets standards and promotes effective legal, regulatory and operational measures against ML, TF and PF. Hong Kong is a member obliged to implement its latest Recommendations. FATF monitors compliance through jurisdiction evaluations and stringent follow-up, including identifying high-risk and other monitored jurisdictions; its Recommendations do not replace Hong Kong law.'),
        ('「呼籲採取行動」類別要求加強盡職審查；特定高風險地區另有反制措施。「加強監察」類別須納入風險評估，但並非單憑列名便一律要求加強盡職審查。FATF風險名單亦不是聯合國的指定人士制裁名單。', 'The call-for-action category requires enhanced due diligence, with countermeasures for specified high-risk jurisdictions. Increased monitoring informs risk assessment but does not by itself require EDD in every case. FATF risk lists are distinct from UN designated-person sanctions lists.'),
        ('第19份2026年7月3日通函記錄：朝鮮及伊朗須採取反制措施；緬甸須採取與風險相稱的加強措施；加強監察新增波斯尼亞和黑塞哥維那及伊拉克。這是該通函日期的名單，運作時須使用最新官方更新。', 'Document 19, dated 3 July 2026, records countermeasures for DPRK and Iran, proportionate enhanced measures for Myanmar, and additions of Bosnia and Herzegovina and Iraq to increased monitoring. This is the circular’s dated snapshot; operations require current official updates.'),
    ], [
        ref('03', '第1.13段', '¶1.13', 'As a member of the FATF'),
        ref('06', '打擊洗錢問答A17', 'AML/CFT FAQ A17', 'conducting EDD is not mandatory'),
        ref('19', '正文第1–3頁', 'Main text pp.1–3', 'Myanmar'),
    ], kind='list'),
    block('反制措施不是加強審查的另一個名稱', 'Countermeasures are more than another name for EDD', [
        ('第19份2026年7月3日通函所舉朝鮮反制措施包括終止與其銀行的往來關係、關閉其境內分行／附屬機構及限制與朝鮮人士的業務／交易；須按適用機構及法律框架執行。加強審查則包括提高監察程度及性質。不要把通函所述緬甸未來可能面對的反制，寫成當時已實施的同一措施。', 'The 3 July 2026 circular gives DPRK countermeasure examples including terminating its banks’ correspondent relationships, closing local branches/subsidiaries and limiting DPRK-person business/transactions, within the applicable institutional/legal framework. EDD includes increasing monitoring degree/nature. The circular’s possible future Myanmar countermeasures are not the same as already-operative snapshot measures.'),
    ], [
        ref('19', '第1頁註2、第2頁註5', 'p.1 note 2; p.2 note 5', 'terminating correspondent relationships with DPRK banks'),
    ], kind='list'),
]),
section('sanctions', '恐怖主義及擴散融資的定向金融制裁', 'Targeted financial sanctions for terrorism and proliferation', [
    block('禁止、凍結及許可', 'Prohibitions, freezing and licences', [
        ('定向金融制裁通常包括凍結指定人士／實體的資金或其他資產，及禁止直接或間接向其提供資金、資產或相關服務。篩查不只看國籍或姓名，也須涵蓋有關實體、國家、活動及交易參與者。', 'Targeted financial sanctions generally freeze designated persons’/entities’ funds or other assets and prohibit direct or indirect provision of funds, assets or related services. Screening concerns relevant entities, countries, activities and transaction parties, not just nationality or names.'),
        ('第575章下，行政長官在憲報刊登有關指定；保安局局長可依權力凍結財產及處理有關許可。第537章下，實際限制及豁免須看適用規例；行政長官可批出法定特許，申請者須向商務及經濟發展局提出書面申請。不要把不同法例的主管人員混為一談。', 'Under Cap.575 the Chief Executive publishes relevant designations in the Gazette; the Secretary for Security exercises relevant freezing/licensing powers. Under Cap.537 restrictions and exemptions depend on applicable regulations, with licences granted by the Chief Executive; applicants write to the Commerce and Economic Development Bureau. These roles differ.'),
        ('不得把法定禁止交易當成可以自行接受的高風險業務。只有符合適用法例的豁免或有效許可，才可在其範圍內處理；有需要時須報告懷疑及保存處理紀錄。', 'A prohibited transaction is not simply a high-risk business choice. Deal only within an applicable statutory exemption or valid licence where available, and report suspicion and retain handling records where required.'),
        ('聯合國指定與香港落實之間可能有時間差；第26份通函指出，在本地制裁實施前，相關活動已可能觸犯現有洗錢、恐怖分子資金籌集或擴散融資相關罪行。須及早更新風險及監察，不能一律等待本地規例生效。', 'There may be a gap between UN designation and local implementation. Document 26 explains that activity before implementation may already breach existing ML/TF/PF-related offences. Update risk and monitoring promptly rather than automatically waiting for local regulations.'),
        ('第09份通函要求盡快把擴散融資納入機構風險評估，包括現有業務及客戶；留意指定對象利用空殼、貿易、代理及複雜付款鏈規避制裁的風險。', 'Document 09 calls for prompt inclusion of PF in institutional assessment, covering existing business/customers. Consider evasion through shells, trade, agents and complex payment chains.'),
    ], [
        ref('03', '第6.1–6.8段', '¶6.1–6.8', 'Secretary for Security'),
        ref('09', '正文第1–2頁', 'Main text pp.1–2', 'proliferation financing'),
        ref('26', '正文第1–3頁', 'Main text pp.1–3', 'time gap'),
    ], kind='list'),
    block('全球措施、特定地區與境外制裁', 'Global measures, country-specific measures and foreign sanctions', [
        ('指引以聯合國安理會第1540號及其後決議說明全球擴散防制，並以朝鮮第1718號、伊朗第2231號及其後決議說明特定國家措施。實際禁止及特許須按適用香港法例及更新名單判斷，決議年份本身不是現行名單證明。', 'The Guideline illustrates global counter-proliferation through UNSCR1540/successors and country-specific measures through DPRK1718 and Iran2231/successors. Actual prohibitions/licences follow applicable Hong Kong laws and updated lists; resolution years do not prove a current list.'),
        ('其他司法管轄區的單邊制裁一般不直接成為香港法下的義務，但跨境經營仍可能受境外法規、交易對手及業務限制影響，須理解及管理其風險。', 'Foreign unilateral sanctions generally do not directly impose Hong Kong-law duties, but international operations can face overseas law, counterpart and business restrictions; understand/manage that exposure.'),
    ], [
        ref('03', '第6.9–6.11段', '¶6.9–6.11', 'two-tiered approach'),
    ], kind='list'),
    block('第1373號決議與兩項制裁法例', 'Resolution 1373 and the two sanctions frameworks', [
        ('聯合國制裁一般透過UNSO第537章下的規例在港落實；涉及恐怖主義的安理會第1373號決議則由UNATMO第575章處理。行政長官的指明及憲報更新使相關指定在港生效；仍須留意前述時間差，不能一概等到本地規例更新才留意風險。', 'UN sanctions are generally implemented through regulations under UNSO, Cap.537; terrorism-related UNSCR1373 is covered by UNATMO, Cap.575. Chief Executive specifications and Gazette updates give effect to relevant designations locally. The timing-gap risks above still apply; do not wait indiscriminately for local regulations before addressing risk.'),
    ], [
        ref('26', '預期監管標準第1頁', 'Expected regulatory standards, p.1', 'except for UNSC Resolution 1373'),
    ], kind='list'),
    block('恐怖分子財產、跨國旅行及間接控制', 'Terrorist property, inter-state travel and indirect control', [
        ('恐怖分子財產包括恐怖分子或其有聯繫者的財產，以及擬用於或曾用於資助／協助恐怖行為的其他財產。來源合法的財產亦可符合，不能把恐怖分子財產只理解成犯罪所得。', 'Terrorist property includes property of a terrorist/associate and other property intended or used to finance/assist terrorist acts. Lawful-source property can qualify; it is not confined to criminal proceeds.'),
        ('UNATMO第8A條禁止明知或罔顧財產是否指明恐怖分子財產，或指明恐怖分子／有聯繫者財產而處理。第11L條禁止提供／籌集財產資助跨國旅行，意圖或明知旅行用於實施、計劃、準備、參與恐怖行為或相關訓練；不必實際發生恐怖行為。', 'UNATMO section 8A prohibits dealing knowing or reckless as to whether property is specified terrorist property or property of a specified terrorist/associate. Section 11L prohibits providing/collecting property for inter-state travel intending or knowing the terrorist-act/planning/preparation/participation or related-training purpose; an actual terrorist act need not occur.'),
        ('保安局局長可在UNATMO適用範圍發牌准許例外，例如合理生活／法律開支及法定僱傭款項；MSO須向保安局提出申請。不可把此許可與UNSO下向商經局申請、由行政長官批准的特許混為一談。', 'The Secretary for Security can license exceptions within UNATMO’s scope, such as reasonable living/legal expenses and statutory employment payments; an MSO applies to the Security Bureau. This differs from UNSO applications to the Commerce and Economic Development Bureau for a Chief Executive licence.'),
        ('UNSO適用規例的禁令不限於直接列名者，也涵蓋代其／按其指示行事、由其擁有或控制的人士／實體，以及由上述人士／實體擁有的實體。除有效法定特許外，禁止直接／間接為其利益提供資金、金融資產或經濟資源，或處理屬於或由其擁有／控制的資產。', 'Applicable UNSO prohibitions extend beyond named designees to persons/entities acting for or at their direction or owned/controlled by them, and entities owned by the foregoing. Subject to a valid statutory licence, prohibitions cover direct/indirect availability of funds, financial assets or economic resources for their benefit and dealing with assets belonging to or owned/controlled by them.'),
    ], [
        ref('03', '第6.5–6.8段及註56', '¶6.5–6.8; footnotes 56', 'section 11L prohibits any person from providing or collecting any property to'),
    ], kind='list'),
    block('第03份所列兩層反擴散框架', 'The two-tier counter-proliferation framework in document 03', [
        ('第03份第6.9段說明：全球層面為安理會第1540(2004)號及後續決議；國別層面為針對朝鮮的第1718(2006)號、針對伊朗的第2231(2015)號及其後續決議。這是該版原文的框架及決議對應，不能把它當成已核實至今的完整制裁名單或現行限制。', 'Document 03 paragraph 6.9 describes a global tier under UNSCR1540(2004)/successors and country-specific tiers under UNSCR1718(2006) for DPRK and UNSCR2231(2015) for Iran/their successors. This is the stored edition’s framework mapping, not a verified-current complete sanctions list or set of restrictions.'),
    ], [
        ref('03', '第6.9段', '¶6.9', 'a two-tiered approach'),
    ], kind='list'),
]),
section('cross-boundary-cash', '跨境現金類物品：超過12萬元的申報制度', 'Cross-boundary CBNIs: declarations above HK$120,000', [
    block('物品、門檻與旅客', 'Items, threshold and travellers', [
        ('現金類物品（CBNIs）包括香港或外地的法定貨幣紙幣／硬幣，以及不記名或其他可透過交付轉移權利的可轉讓票據，例如不記名支票、匯票、旅行支票及本票。按面值合計，總值超過港幣120,000元才是「大量」；正好120,000元並不超過。', 'CBNIs include legal-tender notes/coins of Hong Kong or elsewhere and bearer or other negotiable instruments transferable by delivery, such as bearer cheques, bills, travellers’ cheques and promissory notes. Aggregate nominal value must exceed HK$120,000 to be a large quantity; exactly HK$120,000 does not exceed it.'),
        ('從指明管制站入境而管有大量CBNIs的人須使用紅通道並作書面申報；從其他地方入境及離境人士，須應獲授權人員要求披露，披露管有大量CBNIs後須按要求作申報。', 'At specified entry points, persons possessing large quantities use the red channel and make a written declaration. Arrivals elsewhere and departing persons disclose on an authorized officer’s request and then declare where large quantities are disclosed.'),
        ('管有包括隨身物品、由該運輸工具運載的個人物品，以及托運行李；托運行李不論是否由或將會由同一運輸工具運載，均可計入。陪同未滿16歲人士的成人，在知道該幼年人管有大量CBNIs時承擔相應責任。純粹過境、在香港機場未通過入境檢查的法定情況獲豁免。', 'Possession includes personal belongings carried by the person, belongings on the conveyance and checked baggage. Checked baggage counts whether or not carried, or to be carried, on the same conveyance. An accompanying adult has relevant duties when aware that a person under 16 possesses large quantities. The statutory airport-transit case without immigration clearance is exempt.'),
        ('旅客外幣按有關事件當日的參考匯價；非公布日或公布前使用前一公布日。未能按該方法計算時，按法定指定國際機構匯價，再無則用管有人通常採用的匯價。', 'For travellers, use the reference rate on the relevant-event date; use the preceding publication day if no rate is published that day or the event precedes publication. Statutory fallbacks are a specified international institution’s rate and then the holder’s ordinarily used rate.'),
    ], [
        ref('22', '正文第1頁', 'Main text p.1', 'HK$120,000'),
        ref('23', '第2–7條及附表4', 'ss.2–7; Schedule 4', 'nominal value'),
    ], kind='list'),
    block('貨物輸入／輸出與違規', 'Cargo imports/exports and breaches', [
        ('非旅客方式以跨境運輸工具輸入／輸出大量CBNIs，負責人須事先透過指定電子系統申報；須依第10條處理同一運輸工具及同一客戶等合併情況。系統產生接受申報的參考編號才視為申報。不要自行添加法例沒有訂出的統一24小時期限。', 'For non-traveller imports/exports of large quantities on cross-boundary conveyances, the responsible person declares in advance through the designated electronic system. Apply section 10 aggregation rules, including same-conveyance/customer cases. Declaration occurs when the system generates the acceptance reference; there is no invented universal 24-hour deadline.'),
        ('例外包括適用旅客物品、只經香港而全程留在飛機／船上的貨物、航空轉運貨物及郵包等法定情況。貨物外幣通常用上月15日的參考匯價（非公布日用之前公布日），與旅客的當日基準不同。', 'Statutory exclusions include covered travellers’ belongings, goods remaining aboard aircraft/vessels solely transiting Hong Kong, air-transhipment cargo and postal packets. Cargo normally uses the previous month’s 15th-day reference rate, or preceding publication day, unlike the traveller’s event-date basis.'),
        ('沒有遵從申報／披露或作出在要項上虛假的申報可罰款500,000元及監禁2年。部分指明罪行可由關長發通知，以2,000元在指定合理時間內繳付而不提控；並非人人都有此權利：既往相關定罪／繳付紀錄、指定洗錢或恐怖主義定罪或按第17條檢取等情況不適用。', 'Non-compliance or materially false declarations/disclosures can carry HK$500,000 and two years. For specified offences the Commissioner may issue a notice allowing HK$2,000 payment within a specified reasonable time instead of prosecution. This is not an entitlement: relevant prior convictions/payment records, specified ML/terrorism convictions or section 17 seizure exclude it.'),
    ], [
        ref('23', '第8–14條、附表5', 'ss.8–14; Schedule 5', 'Written notice about not instituting criminal proceedings on payment'),
    ], kind='list'),
    block('現金類物品的五類票據及匯價日期', 'Five instrument forms and the exchange-rate event', [
        ('可轉讓票據包括：持有人形式、無限制背書、向虛構受款人付款、所有權隨交付轉移，以及已簽署但未寫受款人姓名的票據。例子有不記名支票、本票、匯票及旅行支票，須符合上述票據形式；法定貨幣紙幣／硬幣是另一類，並非只有現金及不記名支票才計算。', 'Negotiable instruments include bearer form, unrestricted endorsement, a fictitious payee, title passing on delivery, and signed instruments without a named payee. Examples include bearer cheques, promissory notes, bills and travellers’ cheques meeting those instrument-form conditions; legal-tender notes/coins form the other limb. CBNIs are not limited to cash and bearer cheques.'),
        ('旅客的「有關事件」：第4條是抵達指明管制站；第5／6條是獲授權人員要求披露。參考匯價指香港銀行公會公布的外匯賣出開市參考牌價。套用前文的公布日／公布前及後備方法；貨物仍採上月15日基準，不可混用。', 'The traveller’s relevant event is arrival at the specified control point for section 4, and the officer’s disclosure request for sections 5/6. Reference rates are the Hong Kong Association of Banks opening indicative counter exchange selling rates. Apply the publication-day/time and fallback rules above; cargo retains its previous-month 15th-day basis.'),
    ], [
        ref('23', '第2(1)、7(6)條', 'ss.2(1), 7(6)', 'signed but does not state a payee’s name'),
        ref('23', '第7條', 's.7', 'means the person arrives at the specified control point concerned'),
    ], kind='list'),
    block('檢取與扣留：十個工作日、三個月、兩年', 'Seizure and detention: ten working days, three months, two years', [
        ('行使第16(1)條權力而發現現金類物品，獲授權人員合理懷疑屬第455章第25(1)條犯罪得益，或第575章所指恐怖分子財產，可依第17條檢取。此項權力針對懷疑財產，不能套用申報制度的超過12萬元門檻。', 'CBNIs found through section 16(1) powers may be seized under section 17 on reasonable suspicion that they represent OSCO section 25(1) crime proceeds or UNATMO terrorist property. This suspected-property power does not import the declaration regime’s above-HK$120,000 threshold.'),
        ('在第18、19條規限下，第17條通常准許扣留至檢取日後不超過10個工作日。此處工作日排除星期六、公眾假期、黑色暴雨警告日及烈風警告日；不要直接套用AMLO的營業日定義。這是物品扣留期，不是拘捕後扣留人的期限。', 'Subject to sections 18/19, section 17 ordinarily allows detention for no more than ten working days after the seizure day. Here working days exclude Saturdays, general holidays and black-rainstorm/gale-warning days. Do not substitute AMLO business days. This is detention of property, not a period of personal custody after arrest.'),
        ('懷疑犯罪得益，獲授權人員可在上述期間內向原訟法庭或區域法院申請第18條繼續扣留令。法院須信納合理懷疑及扣留有理據，例如進一步調查來源、考慮相關刑事程序或沒收／充公程序。每次命令期不超過自命令日起3個月；新命令不得令總扣留超過首個法院命令日起2年。', 'For suspected crime proceeds, an authorized officer may apply within that period to the Court of First Instance or District Court under section 18. The court must be satisfied of reasonable suspicion and justification, such as source investigation or consideration of relevant criminal/forfeiture/confiscation proceedings. Each order permits no more than three months from its date; renewals must not take total detention beyond two years from the first court order.'),
        ('第19條所列相關程序在扣留期間提起時，可扣至程序完結，故兩年不是沒有例外的絕對上限。第18條扣留條件不存在／不再存在或再無理據時，法院可按關係人／人員申請指示發還。第18條延長機制針對懷疑犯罪得益，不應不加區分地當成恐怖分子財產的相同延長程序。', 'If the relevant section 19 proceedings are instituted during detention, detention may continue until they conclude, so two years is not an exception-free absolute limit. Under section 18, the court may direct return on an interested person’s/officer’s application when conditions do not/no longer exist or detention is no longer justified. Section 18 continuation concerns suspected crime proceeds; do not indiscriminately apply it as the same terrorist-property extension mechanism.'),
    ], [
        ref('23', '第17–19條', 'ss.17–19', 'not more than 10 working days after the day of seizure'),
    ], kind='list'),
    block('申報內容的基本清單', 'Basic declaration information', [
        ('旅客申報須提供適用的身分、聯絡及運輸工具資料，現金類物品種類／面值，日期、來源及目的地，以及不是本人擁有時的擁有人等資料。非旅客方式申報包括負責人／客戶資料、運輸工具、物品種類及價值、日期及來源／目的地，並在適用時列收受人及貨單識別資料。須按附表2／3相應表格填報，不能只報一個總額。', 'Traveller declarations require applicable identity/contact/conveyance details, CBNI type/value, dates/source/destination and ownership particulars where not owned by the holder. Non-traveller declarations include responsible-person/customer details, conveyance, type/value, dates/source/destination and applicable recipient/consignment identifiers. Follow the corresponding Schedule 2/3 information requirements; reporting a total alone is insufficient.'),
    ], [
        ref('23', '附表2–3', 'Schedules 2–3', 'If applicable, the name and address of the recipient of the CBNIs'),
    ], kind='list'),
    block('貨物的合併與申報責任', 'Cargo aggregation and declaration responsibility', [
        ('非承運人：合併同一人以同一跨境運輸工具輸入／輸出的現金類物品。承運人：合併同一承運人為同一客戶在同一運輸工具運送的物品；客戶須直接聘用承運人，或直接聘用把物品運送或安排運送給承運人的代運人。同一客戶聘用多名代運人時，只有同一代運人運送或安排運送予同一承運人的物品才按這項規則合併。客戶指非承運人，不能把物流代運人自行當成客戶。', 'For a non-carrier, aggregate CBNIs imported/exported by the same person on the same cross-boundary conveyance. For a carrier, aggregate CBNIs carried by the same carrier for the same customer on that conveyance. The customer must directly engage the carrier, or directly engage the forwarder who transports or arranges transport of the CBNIs to the carrier. Where that customer engages multiple forwarders, this rule aggregates only items transported, or whose transport is arranged, by the same forwarder to the same carrier. Customer means a person who is not a carrier; do not automatically substitute the freight forwarder for the customer.'),
        ('輸入、輸出或安排輸入／輸出的人須確保事前已有合規申報；僅掌管運輸工具而無其他輸入／輸出責任者有第9(2)條例外。通常以電子方式申報；獲系統接納及編配參考編號才算完成。關長認為電子傳送並非切實可行時，可依關長指示採另一方式；不是自行改用任意紙本程序。旅客、郵包及法定過境／航空轉運貨物豁除另按第8條判斷。', 'A person importing/exporting or causing import/export must ensure a compliant declaration has been made beforehand; section 9(2) excepts a conveyance operator with no other responsibility for the import/export. Normally declare electronically; acceptance and allocation of a reference number complete submission. Where the CCE considers electronic transmission impracticable, use an alternative manner directed by the CCE, not an arbitrary paper route. Apply section 8 exclusions for travellers, postal packets and the specified transit/air-transhipment cargo separately.'),
    ], [
        ref('23', '第8–11條', 'ss.8–11', 'same carrier for the same customer'),
    ], kind='list'),
    block('參考：申報資料的完整分類', 'Reference: declaration-information checklist', [
        ('旅客申報：管有人全名、身分證號碼或旅行證件號碼及簽發地、國籍、出生日期及地點、永久地址（境外者另填在港地址）；運輸工具識別、現金類物品種類及價值、出入境方向、日期及來源／目的地。如不是物品擁有人，填擁有人姓名／名稱及地址；代報者另填相同個人資料。', 'Traveller declaration: possessor’s full name, ID number or travel-document number and issuing place, nationality, birth date/place, permanent address (plus Hong Kong address if the permanent address is overseas); conveyance identifier, CBNI type/value, direction, date and origin/destination. If not the owner, give owner name/address; a separate declarant supplies the same personal particulars.'),
        ('貨物申報：非承運輸入／輸出人或承運人客戶的基本資料；自然人為上述個人資料但不另列在港地址，非自然人為名稱、適用商業登記號碼及業務地址。另填運輸工具、物品種類／價值、方向、日期、來源／目的地，以及適用收受人姓名／名稱及地址、貨單等批次識別。', 'Cargo declaration: basic information of the non-carrier importer/exporter or carrier’s customer. Individuals provide the above personal particulars without a separate Hong Kong-address item; entities provide name, applicable BR number and business address. Add conveyance, type/value, direction, date, origin/destination and, where applicable, recipient name/address and consignment identifier such as waybill number.'),
    ], [
        ref('23', '附表2、3', 'Schedules 2–3', 'Information to be Provided in Declaration'),
    ], kind='reference'),
]),
])
