"""One-off source-first depth amendments. Inputs are manuscripts and document 03 only."""
import ast
import importlib
from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(HERE))
from model import block, ref, p

def source(loc, anchor):
    return [ref('03','第'+loc+'段','¶'+loc,anchor)]

def write_sections(number, changes):
    path=HERE/f'part{number}.py'
    text=path.read_text(encoding='utf-8')
    part=importlib.import_module(f'part{number}').PART
    tree=ast.parse(text); edits=[]; lines=text.splitlines(keepends=True)
    for node in ast.walk(tree):
        if not isinstance(node,ast.Call) or not isinstance(node.func,ast.Name) or node.func.id!='section':continue
        key=ast.literal_eval(node.args[0])
        if key not in changes:continue
        section=next(s for s in part['sections'] if s['id']==key)
        changes[key](section)
        out=[f"section({key!r}, {section['title']['tc']!r}, {section['title']['en']!r}, [\n"]
        for b in section['blocks']:
            out.append(f"    block({b['title']['tc']!r}, {b['title']['en']!r}, [\n")
            for v in b['points']:out.append(f"        ({v['tc']!r}, {v['en']!r}),\n")
            out.append('    ], [\n')
            for r in b['refs']:out.append(f"        ref({r['doc']!r}, {r['locator']['tc']!r}, {r['locator']['en']!r}, {r['anchor']!r}),\n")
            out.append(f"    ], kind={b['kind']!r}),\n")
        out.append('])')
        a=sum(len(x) for x in lines[:node.lineno-1])+node.col_offset
        z=sum(len(x) for x in lines[:node.end_lineno-1])+node.end_col_offset
        # Section calls end in ASCII, so the AST byte/character offset is identical there.
        edits.append((a,z,''.join(out)))
    assert len(edits)==len(changes),(number,changes)
    for a,z,new in sorted(edits,reverse=True):text=text[:a]+new+text[z:]
    path.write_text(text,encoding='utf-8',newline='\n')

def ml(s):
    s['blocks'][0]['points'][0]=p('洗錢的法定定義著重行為的意圖：令犯罪得益或全部／部分、直接／間接代表該得益的財產，表面上不像犯罪得益。另須區分DTROP／OSCO第25條的處理犯罪得益罪：處理財產時知道或有合理理由相信它代表犯罪得益。財產不限現金，亦不必表面可疑。','The statutory ML definition concerns an act intended to make crime proceeds, or property wholly/partly and directly/indirectly representing them, appear not to be such proceeds. Distinguish the DTROP/OSCO section 25 dealing offence: dealing while knowing or having reasonable grounds to believe the property represents crime proceeds. Property is not limited to cash and need not look suspicious.')

def international(s):
    s['blocks'][0]['points'][0]=p('財務行動特別組織（FATF）是1989年成立的跨政府組織，制定標準並推動法律、監管及操作措施的有效實施，以打擊洗錢、恐怖分子資金籌集及擴散資金籌集。香港是成員，須實施最新建議。特別組織透過司法管轄區相互評估及嚴格跟進監察合規，並識別高風險及其他受監察地區；建議不是香港法例的替代品。','The Financial Action Task Force (FATF), an inter-governmental body formed in 1989, sets standards and promotes effective legal, regulatory and operational measures against ML, TF and PF. Hong Kong is a member obliged to implement its latest Recommendations. FATF monitors compliance through jurisdiction evaluations and stringent follow-up, including identifying high-risk and other monitored jurisdictions; its Recommendations do not replace Hong Kong law.')

def controls(s):
    s['blocks'][0]['points'][2]=p('簡化制度須同時符合三組條件：（1）繼續遵守附表2，並履行第2.2段的機構風險評估、第2.3段的評估程序及第3.2段的管理要求；（2）已透過適當評估識別支持簡化的較低風險；（3）簡化制度經高級管理層批准，並不時覆核。第3.2段包括批准制度、監察實施及必要時改善，以及對較高風險採加強措施；有洗錢／恐怖分子資金籌集懷疑時不得簡化。','Simplified systems require all three groups of conditions: (1) continued Schedule 2 compliance, institutional assessment under paragraph 2.2, the assessment process in 2.3 and management requirements in 3.2; (2) lower risks identified through an appropriate assessment; and (3) senior-management approval and periodic review of the simplified systems. Paragraph 3.2 requires approved systems, monitoring and necessary enhancement, and enhanced measures for higher risks. Suspicion of ML/TF bars simplification.')

def institution(s):
    b=s['blocks'][0]
    b['points'][3]=p('其他因素包括風險管理資源的性質、規模及質素（包括具適當資格並可持續受訓的人員）、合規／監管發現及內外部審核結果。國家風險須考慮貪污、有組織罪行或恐怖分子資金籌集的普遍程度、執法水平／質素、監管制度／控制成效，以及實益擁有權透明度。納入關長通知的較高風險，並按第09份及時評估擴散資金籌集風險。','Other factors include the nature, scale and quality of risk-management resources, including qualified staff with continuing training, compliance/regulatory findings and internal/external audits. Country risk considers prevalence of corruption, organised crime or TF; law-enforcement level/quality; regulatory regime/control effectiveness; and beneficial-ownership transparency. Include higher risks notified by the CCE and assess PF promptly under document 09.')

def roles(s):
    b=next(b for b in s['blocks'] if b['title']['en']=='Conditions enabling the roles')
    b['points']=[p(*x) for x in [
        ('高級管理層應在切實可行範圍內確保CO／MLRO具備第3.8段的八項條件：（a）適當資格及充足打擊洗錢知識；（b）在機構規模容許下，獨立於所有營運及業務職能；（c）通常在香港工作；（d）有足夠資歷及權限。','As far as practicable, senior management should ensure the eight conditions in paragraph 3.8: (a) appropriate qualifications and sufficient AML/CFT knowledge; (b) independence from all operational/business functions, subject to the MSO’s size; (c) normally based in Hong Kong; (d) sufficient seniority and authority.'),
        ('（e）可定期接觸高級管理層，並在需要時直接接觸；（f）充分熟悉機構的法定／監管規定及業務產生的風險；（g）能及時取得所有可得資料，包括內部CDD紀錄及外部海關通函；（h）有充足資源、人員及缺勤替代安排。副手的具體措辭見本節下文。','(e) regular contact with, and direct access when needed to, senior management; (f) full familiarity with the MSO’s statutory/regulatory requirements and business risks; (g) timely access to all available information, including internal CDD and external Customs circulars; (h) sufficient resources, staff and absence cover. See the specific deputy wording below.'),
    ]]
    s['blocks'][0]['points'][2]=p('MLRO是可疑交易報告的中央聯絡點，也是與聯合財富情報組（JFIU）及執法機關的主要聯絡人，須積極參與識別及舉報。三項主要職能：根據全部相關可得資料覆核內部披露及例外報告並決定是否報JFIU；保存所有內部覆核紀錄；指導避免通風報訊。','The MLRO is the central suspicious-reporting point and main contact with the Joint Financial Intelligence Unit (JFIU) and law-enforcement agencies, with an active identification/reporting role. The three principal functions are reviewing internal disclosures and exception reports using all available relevant information and deciding on JFIU reporting; maintaining all internal-review records; and guiding staff on avoiding tipping off.')

def simplified(s):
    s['blocks'][1]['points'][2]=p('擁有權鏈中的合資格實體，只豁免該實體背後的實益擁有人；與它無關的其他鏈仍須識別及合理核實。金融機構代名人／基金服務帳戶的額外條件另列於下文，不能只因名稱有「代名人」或「基金」便豁免。','A qualifying entity in an ownership chain exempts only its beneficial owners; unrelated chains still require identification and reasonable verification. Additional FI nominee/fund-service account conditions appear below: the labels “nominee” or “fund” alone do not qualify.')
    s['blocks'].extend([
        block('認識：較低風險因素與五類簡化方法','Recognise: lower-risk factors and five types of simplification',[
            ('第4.8.7(a)段的客戶例子：香港／對等司法管轄區政府或公共機構；受充分實益擁有權披露規定約束的上市法團；條例金融機構，或在對等司法管轄區成立、受符合FATF標準要求及監督的金融機構；以及在香港／對等地區獲准向公眾發售的集體投資計劃。','Paragraph 4.8.7(a) examples are Hong Kong/equivalent-jurisdiction government or public bodies; listed corporations subject to adequate beneficial-ownership transparency requirements; AMLO FIs or equivalent-jurisdiction FIs subject to and supervised for FATF-consistent requirements; and collective investment schemes authorised for public offering in Hong Kong/an equivalent jurisdiction.'),
            ('產品因素為下文已列的合資格僱員退休計劃、退休保單及低保費人壽保單，須保留其條件和金額。國家因素為可靠消息來源識別有有效打擊洗錢制度，或貪污／其他犯罪較少。這些只是潛在較低風險因素，須整體評估；不是一見某類客戶便免做CDD。','Product factors are the qualifying employee retirement schemes, retirement policies and low-premium life policies already listed, retaining their conditions and amounts. Country factors are credible-source findings of effective AML/CFT systems or lower corruption/other crime. These are potential lower-risk factors requiring a holistic assessment, not automatic CDD exemptions.'),
            ('第4.8.8段的五類可能方法：（a）對上述客戶接納其他可靠證據，例如金融機構牌照、上市或授權地位；（b）只在第4.8.9–4.8.20段條件下簡化BO審查；（c）降低身分資料更新頻率；（d）按合理金額門檻降低持續監察及交易審查程度；（e）由交易／關係類型推斷目的及擬具有性質。仍須持續監察，且有懷疑、資料疑問或不再低風險時停止簡化。','The five possible methods in paragraph 4.8.8 are: (a) alternative reliable evidence for those customers, such as FI licence, listed or authorisation status; (b) BO simplification only under paragraphs 4.8.9–4.8.20; (c) less frequent identity-information updates; (d) reduced monitoring/scrutiny based on a reasonable monetary threshold; (e) inferring purpose/nature from transaction or relationship type. Ongoing monitoring remains; suspicion, information doubts or loss of low-risk status stop simplification.'),
        ],source('4.8.2–4.8.8','Examples of possible SDD measures include')),
        block('須記條件：金融機構代名人及基金服務帳戶','Remember the conditions: FI nominee and fund-service accounts',[
            ('第4.8.13段以客戶是條例所界定的金融機構為前提。路徑一：以代名人公司名義開戶，代金融機構或其相關客戶持有基金單位；金融機構須已對其相關客戶進行CDD。','Paragraph 4.8.13 starts with a customer that is an AMLO FI. Route one: an account in a nominee company’s name holds fund units for the FI or its underlying customers; the FI must have conducted CDD on its underlying customers.'),
            ('路徑二：金融機構以投資公司的服務供應商（例如基金經理／保管人）身分，以投資公司名義開戶；相關投資者無權控制資產管理，而且金融機構已依AMLO對投資公司進行CDD。','Route two: the FI opens an account in an investment vehicle’s name as its service provider, such as manager/custodian; the underlying investors have no control over asset management, and the FI has conducted AMLO CDD on the investment vehicle.'),
            ('兩條路徑均另須有合約文件／協議證明金融機構獲授權操作帳戶。符合相應路徑及共同條件，MSO才可選擇不識別／合理核實該客戶的BO；其他適用CDD及監察仍然保留。','Both routes also require contractual documents/agreement evidencing the FI’s authority to operate the account. Only with the relevant route and common condition may the MSO omit identification/reasonable verification of that customer’s BOs; other applicable CDD and monitoring remain.'),
        ],source('4.8.13','in the name of a nominee company')),
    ])

def enhanced(s):
    s['blocks'][0]['points']=s['blocks'][0]['points'][:2]
    s['blocks'].extend([
        block('認識完整分類：潛在較高風險因素','Recognise the complete groups: potentially higher risks',[
            ('客戶因素（1–4）：業務關係異乎尋常（例如距離遙遠原因不明、特定組別跨地點／服務交易）；空殼安排沒有明確合法商業目的；有代名人股東／董事、持票人股份／認股權證；擁有或經營現金密集業務。','Customer factors (1–4): unusual circumstances, such as unexplained geographical distance or defined groups transacting across locations/services; shell arrangements without clear legitimate commercial purpose; nominee shareholders/directors or bearer shares/warrants; cash-intensive businesses.'),
            ('客戶因素（5–7）：架構相對業務性質異常或過度複雜；對匯款人／收款人詳情所知甚少或不願披露；客戶或BO屬政治人物。PEP的具體措施仍按本節下方的類別及風險條件決定。','Customer factors (5–7): ownership unusually/excessively complex for the business; little knowledge of, or reluctance to disclose, originator/recipient details; a PEP customer or BO. The specific PEP measures still depend on category and risk, as explained below.'),
            ('產品／交易／渠道因素（1–4）：匿名交易（可能涉及現金）；拆單規避CDD或匯款特別規定，從而避開審查／紀錄；多人匯一人或一人匯多人而無合理解釋；經常收到來歷不明或無聯繫第三方付款。','Product/transaction/channel factors (1–4): anonymous transactions, possibly cash; structuring to avoid CDD or special remittance requirements and thereby CDD/records; many-to-one or one-to-many transfers without reasonable explanation; frequent payments from unknown/unassociated third parties.'),
            ('產品／交易／渠道因素（5–7）：與資金來源／目的地無明顯聯繫且無合理解釋；代理／交易對手交易量與整體或過往一般水平不一致；代理合規計劃未達標準。','Product/transaction/channel factors (5–7): no apparent ties to origin/destination and no reasonable explanation; agent/counterpart volume inconsistent overall or relative to typical past volume; substandard agent compliance programmes.'),
            ('國家因素四項：可靠來源指出制度欠有效；貪污／其他犯罪程度高；受聯合國等的制裁、禁令或類似措施；或向恐怖活動提供資金／支持，或有指定恐怖組織活動。上述為非盡列的風險例子，要綜合評估，不是自動定罪規則。','The four country factors are credible-source findings of ineffective AML/CFT systems; significant corruption/other crime; sanctions, embargoes or similar measures, for example by the UN; or funding/support for terrorism or designated terrorist organisations operating there. These are non-exhaustive risk examples for holistic assessment, not automatic proof of crime.'),
        ],source('4.9.5及註35','Examples of potentially higher risk factors')),
        block('理解如何履行：六類可能的EDD措施','Understand implementation: six possible EDD measures',[
            ('（a）索取額外客戶資料，如職業、資產量及公開資料，用於風險分析，並更頻密更新客戶及BO資料；（b）補充了解關係擬具有的性質；（c）取得財富來源及資金來源資料。','(a) Obtain additional customer information, such as occupation, assets and public information, to inform risk profiling and update customer/BO information more frequently; (b) obtain additional information on intended relationship nature; (c) obtain source-of-wealth and source-of-funds information.'),
            ('（d）查明擬進行或已進行交易的原因；（e）評估資金目的地及交易原因資料；（f）要求首次付款經由客戶本人在遵守相類CDD標準的銀行帳戶。第4.9.6段及註36不要求每宗高風險關係做齊六例；按風險選擇相稱措施，但不能藉此略去PEP等另有規定的必須措施。','(d) Obtain reasons for intended/completed transactions; (e) evaluate destination-of-funds and transaction-reason information; (f) require the first payment through the customer’s own account at a bank subject to similar CDD standards. Paragraph 4.9.6 and note 36 do not require all six examples for every high-risk relationship; choose proportionate measures without omitting separately prescribed duties such as applicable PEP measures.'),
        ],source('4.9.6及註36','Examples of possible EDD measures')),
    ])

def peps(s):
    s['blocks'][0]['points'][1]=p('香港政治人物指在香港擔任或曾擔任重要公職者，例如政府首長、資深從政者、高級政府／司法官員、政府擁有企業的高級行政人員及重要政黨幹事；不包括中級或更低級官員。國際組織政治人物包括獲委重要職能的董事、副董事、董事會成員或同等高級管理人員，亦不包括中級或更低級官員。','Hong Kong PEPs hold/have held prominent public functions in Hong Kong, including heads of government, senior politicians, senior government/judicial officials, senior executives of government-owned corporations and important party officials; middle/junior ranks are excluded. International-organisation PEPs hold/have held prominent functions including directors, deputy directors, board members or equivalent senior management, likewise excluding middle/junior officials.')

def wire(s):
    s['blocks'][1]['points'][1]=p('中介機構須採與直通式處理一致的合理措施，識別跨境電傳欠缺的資料；收款機構則須識別本地或跨境電傳欠缺資料，可用事後監察等合理措施。兩者均須有按風險決定執行／拒絕／暫停及跟進的政策，並在合理可行範圍內盡快向上一手機構取得適用欠缺資料；取不到時，考慮限制／終止與該機構的關係，或採合理緩減措施。','Intermediaries use reasonable measures consistent with straight-through processing to identify missing data in cross-border wires; beneficiary institutions identify missing data in domestic or cross-border wires, for example through post-event monitoring. Both need risk-based execute/reject/suspend/follow-up policies and must obtain applicable missing data from the preceding institution as soon as reasonably practicable; if unavailable, consider restricting/ending that institutional relationship or reasonable mitigation.')

def training(s):
    old=s['blocks'][0]
    old['title']=p('培訓政策、時間及成效','Training policy, timing and effectiveness')
    old['points']=[old['points'][0],p('機構應有清晰明確的培訓政策。應考慮按資源及學習需要混合網上、課堂、影片及手冊等方法；可納入FATF文章／案例，並須能向關長證明材料最新及符合現行要求。至少保存3年的紀錄須顯示誰人受訓、何時及培訓類別。','Maintain a clear, well-articulated training policy. MSOs are encouraged to consider a mix of online, classroom, video and manual-based methods suited to resources and learning needs; FATF papers/typologies may be included. Demonstrate to the CCE that materials are current and aligned with requirements. Keep records of who was trained, when and what type for at least three years.'),p('成效檢查三方面：測試員工對內部程序、法定／監管責任及辨認可疑交易的理解；監察實際合規及內部報告質量／數量，以識別額外培訓需要並採行動；監察出席，跟進沒有合理原因的缺席。','Check effectiveness in three ways: test understanding of internal procedures, statutory/regulatory obligations and suspicious-transaction recognition; monitor compliance and internal-report quality/quantity to identify further training needs and act; monitor attendance and follow up absence without reasonable cause.')]
    s['blocks'].extend([
        block('須記五項共同內容：第9.4段','Remember five common topics: paragraph 9.4',[
            ('（a）機構及個人在AMLO下的CDD和紀錄責任，以及不遵守的後果；（b）在DTROP、OSCO及UNATMO下舉報可疑交易的責任及不舉報的後果。','(a) Institutional and personal AMLO CDD/record duties and consequences of non-compliance; (b) suspicious-reporting duties under DTROP, OSCO and UNATMO and consequences of failure.'),
            ('（c）DTROP、OSCO、UNATMO、UNSO、WMD(CPS)O及AMLO下其他與機構／個人相關的法定監管責任及違規後果；（d）內部政策程序，包括識別及舉報；（e）履行該職責所需的新興技巧、方法及趨勢。完整法例名稱見Part 1「香港法例」。','(c) Other relevant institutional/personal statutory and regulatory duties and breach consequences under DTROP, OSCO, UNATMO, UNSO, WMD(CPS)O and AMLO; (d) internal policies/procedures, including identification/reporting; (e) emerging techniques, methods and trends needed for the role. Full ordinance names appear in Part 1’s legal framework.'),
        ],source('9.4','Staff should be made aware of')),
        block('五類職員：應理解的培訓重點','Five staff groups: training content to understand',[
            ('第9.5段列出或適用於不同職員的範疇，須配合職責。所有新職員，不論資歷：洗錢／恐怖分子資金籌集背景及機構重視程度；識別並向MLRO舉報可疑交易的必要，以及通風報訊罪。','Paragraph 9.5 gives areas that may be appropriate to different staff, tailored to roles. All new staff, irrespective of seniority: ML/TF background and its importance to the MSO; the need to identify/report suspicion to the MLRO; and tipping off.'),
            ('前線：作為與潛在洗錢人的第一接觸點，在機構策略中的重要性；與職責相關的CDD及紀錄政策程序；可疑情況、報告路線，以及何時須格外警覺。','Frontline: their strategic importance as the first contact with potential money launderers; role-relevant CDD and record procedures; suspicious circumstances, reporting lines and when extra vigilance is needed.'),
            ('後勤（按職責）：客戶核實及處理程序；辨識不尋常活動，尤其異常結算、付款或交付指示。','Back office, according to role: customer verification and processing procedures; recognition of unusual activity, especially abnormal settlement, payment or delivery instructions.'),
            ('管理人員，包括內部審計人員及CO：涵蓋制度各方面的較高層次培訓；監督／管理員工、審核制度、隨機抽查及向JFIU舉報的職責培訓。','Management, including internal auditors and COs: higher-level training across the whole regime; responsibilities for supervising/managing staff, auditing systems, random checks and JFIU reporting.'),
            ('MLRO：評估收到的可疑交易報告及向JFIU舉報的特定職責；並持續掌握一般打擊洗錢要求及發展。','MLRO: specific responsibilities for assessing reports received and reporting to the JFIU; staying current with general AML/CFT requirements and developments.'),
        ],source('9.5','all new staff, irrespective of seniority')),
    ])

write_sections(1,{'money-laundering':ml,'international':international})
write_sections(5,{'institutional-assessment':institution,'control-framework':controls,'roles':roles})
write_sections(6,{'simplified':simplified,'enhanced':enhanced,'peps':peps,'wire-receiving':wire})
write_sections(7,{'training':training})
