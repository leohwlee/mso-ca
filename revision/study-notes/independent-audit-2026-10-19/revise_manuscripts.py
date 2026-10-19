"""One-time, source-led revision. Input is the 450-point baseline, never the bank.

The emitted manuscripts are the editable source. This script is an audit record,
not part of the production build, and deliberately refuses a second application.
"""
import copy, json, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
import build
from model import p, block, ref, g
parts=copy.deepcopy(build.PARTS)
assert sum(len(b['points']) for v in parts.values() for s in v['sections'] for b in s['blocks'])==450
findings=[]
def section(n,sid):return next(s for s in parts[n]['sections'] if s['id']==sid)
def log(n,sid,issue,impact,before,after,refs,priority='P1'):
    findings.append(dict(id=f'F{len(findings)+1:02d}',part=n,section=sid,priority=priority,issue=issue,impact=impact,before=before,after=after,refs=copy.deepcopy(refs),status='fixed'))
def change(n,sid,bi,pi,tc,en,issue,impact,priority='P1'):
    b=section(n,sid)['blocks'][bi]; old=b['points'][pi]; new=p(tc,en)
    b['points'][pi]=new;log(n,sid,issue,impact,old,new,b['refs'],priority)
def add(n,sid,tc,en,points,refs,issue,impact,kind='list'):
    b=block(tc,en,points,refs,kind);section(n,sid)['blocks'].append(b)
    log(n,sid,issue,impact,None,b,refs)
def remove_block(n,sid,bi,why):
    b=section(n,sid)['blocks'].pop(bi)
    log(n,sid,why,'保留同節較完整解釋，減少重讀。',b,None,b['refs'],'P2')

change(2,'licence-scope',0,0,
 '金錢服務包括在香港作為業務經營貨幣兌換或匯款。匯款的三種法定安排及豁除條件見下文；不能只因資金沒有經過自己的銀行戶口便認為毋須牌照。',
 'Money service means operating a money-changing or remittance service as a business in Hong Kong. The three remittance arrangements and exclusions are set out below; absence of a flow through the operator’s own bank account does not itself remove licensing requirements.',
 '原稿聲稱「純粹通訊設施支援」有法定豁除，所引定義無此內容。','刪除無原文支持的豁除，避免錯誤縮窄發牌範圍。')
change(2,'grant-renewal',0,0,
 '獨資經營者本人及合夥人須是經營金錢服務的適當人選；獨資／合夥的最終擁有人，以及公司的每名董事及最終擁有人，須是與經營金錢服務相關聯的適當人選。最終擁有人按經營者的法律形式判定，不能一概限於自然人：個人經營者代另一人行事的分支使用「人」；詳見下方定義。',
 'The proprietor and partners must be fit and proper to operate money service. Ultimate owners of an individual/partnership, and every director and ultimate owner of a corporation, must be fit and proper to be associated with it. Determine ultimate ownership by legal form: it is not invariably limited to individuals, because the individual-operator acting-on-behalf limb uses “person”. See the definitions below.',
 '最終擁有人被一概限為自然人。','恢復第24條個人經營者代他人行事的分支。')
change(2,'grant-renewal',0,1,
 '申請涉及特定營業處所時，處所須合適；如屬住宅處所，每名佔用人須書面同意獲授權人士進入行使法定權力。這不表示每名MSO都必須有特定營業處所；沒有特定處所者的LMO／LPS要求見Part 4。獲批牌照一般兩年或關長指定其他期間；附加、修改或撤銷條件須依通知、理由及覆核程序。',
 'Where an application concerns particular business premises, they must be suitable; for domestic premises every occupant must consent in writing to authorized entry. This does not require every MSO to have particular business premises; Part 4 explains the LMO/LPS requirements for operators without them. A grant normally lasts two years or another CCE-specified period; imposing, amending or removing conditions follows statutory notice, reasons and review procedures.',
 '合適處所要求未附「申請涉及特定處所」條件。','避免把無特定處所的合法營運模式排除。')
change(3,'definitions',1,0,
 '公司：自然人直接／間接擁有或控制超過25%已發行股本、行使／控制超過25%股東大會投票權，或最終控制管理。合夥：自然人直接／間接超過25%資本／利潤或投票權，或最終控制管理。兩類也包括交易為其進行的另一「人」，不能把這個分支一概限於自然人。正好25%未達百分比門檻，仍須檢查控制。',
 'For corporations: individuals directly/indirectly owning or controlling more than 25% of issued capital or general-meeting votes, or exercising ultimate management control. For partnerships: individuals with directly/indirectly more than 25% of capital, profits or votes, or ultimate management control. Both also include another “person” on whose behalf the transaction is conducted; that limb is not universally limited to individuals. Exactly 25% misses the percentage test, but control must still be examined.',
 '附表2的on-behalf分支被誤寫為individual。','與原文person及既有衝突裁定B14一致。')
s=section(6,'beneficial-owners');old=s['title'];s['title']=p('實益擁有人：擁有權、控制與代他人行事','Beneficial owners: ownership, control and acting for another')
log(6,s['id'],'標題「追至最終自然人」掩蓋法定例外。','避免以標題代替各類定義。',old,s['title'],s['blocks'][0]['refs'])
add(6,'beneficial-owners','自然人與「人」的界線','Individuals versus “persons”',[
 ('公司／合夥的擁有權及控制分支追查自然人；但交易為其進行的人，以及信託的財產授予人、受託人、保障人／執行人等，須按各自定義識別，不能一律排除法人。替代識別高級管理人員，也不是把該人自動重新定義為BO。','Ownership/control limbs for corporations and partnerships trace individuals. But the person for whom a transaction is conducted and trust roles such as settlor, trustee and protector/enforcer must be identified under their respective definitions; legal persons are not universally excluded. Identifying senior managing officials as a fallback does not automatically redefine them as BOs.')
],[ref('04','附表2第1條','Schedule 2 s.1','beneficial owner'),g('4.4.6–4.4.12','senior managing official')],
 '標題、正文與法定person／individual界線不一致。','清楚說明法人可能出現的角色及高管替代措施。')

# Precision fixes whose source conditions were already read independently.
b=section(2,'inspection-investigation')['blocks'][0]
for i,x in enumerate(b['points']):
    if '7日' in x['tc'] or 'seven days' in x['en']:
        change(2,'inspection-investigation',0,i,
          '第17條搜查令自發出日期起7日內可執行。取走的紀錄／文件通常可自取走日起保留不超過6個月；相關刑事程序開始後可按法定條件延長。須盡快發收據，並依第19條提供免費查閱及複製安排。',
          'A section 17 warrant is executable within seven days from its date. Removed records/documents may normally be retained for up to six months from removal, with statutory extensions where relevant criminal proceedings begin. Give a receipt as soon as practicable and permit access/copying without charge under section 19.',
          '搜查令及扣取紀錄的期限缺起算事件。','分清發出日期與取走日期。')
for s in parts[2]['sections']:
 for b in s['blocks']:
  for x in b['points']:
   if 'Detention without charge before a magistrate' in x['en']:
    old=copy.deepcopy(x); x['en']=x['en'].replace('Detention without charge before a magistrate','Detention without being charged and brought before a magistrate')
    log(2,s['id'],'拘留句子的英文欠清楚。','保留48小時及控罪／帶到裁判官席前的條件。',old,x,b['refs'],'P2')
change(4,'exchange-display',0,0,
 '淨匯率是已包括全部收費及佣金的每單位外幣港幣價格。對附表3內自己準備買入／賣出的貨幣，須在清楚、光線足夠及無遮擋的告示牌展示相應淨率；不是強制買賣全部17種貨幣。多塊牌的匯率須相同，可按10或100單位列示。展示的是最不利率，可以給顧客更佳率。',
 'The net rate is the HKD price per foreign-currency unit inclusive of all charges and commission. Display the applicable net rates for Schedule 3 currencies the changer is prepared to buy or sell, clearly, visibly and with adequate lighting; there is no requirement to trade all 17 currencies. Multiple boards must show identical rates; units of 10 or 100 may be used. Display the least favourable rate; better rates may be offered.',
 '匯率展示缺「準備買入／賣出」限制。','避免誤以為必須提供全部17種貨幣。')
change(5,'roles',0,0,
 '高級管理層須了解及有效管理機構風險，實施制度；任命管理層級的合規主任（Compliance Officer，CO）建立及維持制度，並任命高級職員為洗錢報告主任（Money Laundering Reporting Officer，MLRO），作可疑交易報告聯絡點。',
 'Senior management understands and manages risk and implements systems. It appoints a management-level Compliance Officer (CO) to establish and maintain controls, and a senior Money Laundering Reporting Officer (MLRO) as the suspicious-reporting focal point.',
 'MLRO英文首次出現未寫全名。','讓本Part可獨立閱讀。','P2')
change(6,'cdd',0,2,
 '取得業務關係目的及擬具有的性質資料；若已顯而易見，毋須另行取得。客戶不是自然人時，亦須了解其業務性質。',
 'Obtain information on the purpose and intended nature of the relationship unless obvious. Where the customer is not a natural person, also understand the nature of its business.',
 '「非法人自然人以外」難以理解。','改為直接說明適用對象。','P2')
change(6,'remote',0,3,
 '補充措施可包括合資格人士核證、可靠資料庫／登記冊或適當科技，須逐案確保足以防冒認。非自然人客戶由遠端代表建立關係，或只提供公司文件副本，也須緩減增加的風險。',
 'Supplementary measures may use suitable certification, reliable databases/registers or technology, assessed case by case against impersonation risk. Also mitigate increased risk for non-individual customers onboarded through remote representatives or document copies.',
 '「非法人自然人以外」用詞含混。','避免誤解公司客戶的適用範圍。','P2')

# Remove true duplicate supplements; preserve the more complete source-bound text.
remove_block(6,'peps',2,'國際組織定義與下一段完整重複。')
remove_block(6,'screening',1,'跨境篩查六類人士與下一段完整重複。')
remove_block(7,'after-report',1,'提交STR時覆核的補充與主段重複；整合入主段。')
change(7,'after-report',0,1,
 '提交STR時即須適當覆核關係及採取風險緩減，必要時交高級管理層決定，不能等JFIU回覆才處理。JFIU同意不是戶口無風險證明，亦不免除其他法律、監管及聲譽風險。',
 'Review the relationship and apply appropriate mitigation upon filing an STR, escalating to senior management where necessary rather than waiting for JFIU feedback. Consent is not a clean bill of health and does not remove other legal, regulatory or reputational risks.',
 '相關風險覆核分散於重複段落。','合併而保留upon filing的時間條件。','P2')

add(2,'criminal-liability','參考：第5(11)條所指的條文','Reference: provisions specified by section 5(11)',[
 ('這是刑事及紀律責任的指定清單，不等於附表2每一行文字本身都構成同一罪行。內容涵蓋CDD及時機、持續監察、特別情況、轉帳、依賴中介人、程序、紀錄及集團措施；仍須分清責任人及知情／意圖詐騙等犯罪要素。','This is the specified list for criminal and disciplinary liability, not a rule making every sentence in Schedule 2 the same offence. It covers CDD and timing, monitoring, special cases, transfers, reliance, procedures, records and group measures. Apply the relevant actor and knowledge/intent-to-defraud elements.'),
 ('所存版本的完整定位：附表2第3(1)、(1A)、(1B)、(3)、(4)；5(1)、(3)；6(1)、(2)；7(2)；9；10(1)、(2)；11(1)、(2)；12(3)、(5)、(6)、(8)、(9)、(10)；13(2)；13A(2)、(4)、(5)、(6)、(7)；14(1)、(2)；15；16；17(1)；18(4)；19(1)、(2)、(2A)、(3)；20(1)、(2)、(3)、(3A)、(5)；21；22(1)、(2)；23條。','Full stored-edition reference list: Schedule 2 ss.3(1), (1A), (1B), (3), (4); 5(1), (3); 6(1), (2); 7(2); 9; 10(1), (2); 11(1), (2); 12(3), (5), (6), (8), (9), (10); 13(2); 13A(2), (4), (5), (6), (7); 14(1), (2); 15; 16; 17(1); 18(4); 19(1), (2), (2A), (3); 20(1), (2), (3), (3A), (5); 21; 22(1), (2); and 23.')
],[ref('04','第5(11)條','s.5(11)','specified provision')],
 '反覆提指明條文，沒有可直接查閱的完整清單。','補可見參考清單，主要學習仍是責任類型與犯罪要素。',kind='reference')

add(1,'cross-boundary-cash','貨物的合併與申報責任','Cargo aggregation and declaration responsibility',[
 ('非承運人：合併同一人以同一跨境運輸工具輸入／輸出的現金類物品。承運人：合併同一承運人為同一客戶在同一運輸工具運送的物品；客戶須直接聘用承運人，或直接聘用把物品交給承運人的代運人。同一客戶聘用多名代運人時，只有同一代運人交予同一承運人的物品才按這項規則合併。客戶指非承運人，不能把物流代運人自行當成客戶。','For a non-carrier, aggregate CBNIs imported/exported on the same carrier for the same customer. For a carrier, aggregate consignments for the same customer on that conveyance; where multiple consignors use the same freight forwarder, section 10 treats the forwarder as customer. Splitting consignments does not defeat aggregation.'),
 ('輸入、輸出或安排輸入／輸出的人須確保事前已有合規申報；僅掌管運輸工具而無其他輸入／輸出責任者有第9(2)條例外。通常以電子方式申報；獲系統接納及編配參考編號才算完成。關長認為電子傳送並非切實可行時，可依關長指示採另一方式；不是自行改用任意紙本程序。旅客、郵包及法定過境／航空轉運貨物豁除另按第8條判斷。','A person importing/exporting or causing import/export must ensure a compliant declaration has been made beforehand; section 9(2) excepts a conveyance operator with no other responsibility for the import/export. Normally declare electronically; acceptance and allocation of a reference number complete submission. Where the CCE considers electronic transmission impracticable, use an alternative manner directed by the CCE, not an arbitrary paper route. Apply section 8 exclusions for travellers, postal packets and the specified transit/air-transhipment cargo separately.')
],[ref('23','第8–11條','ss.8–11','same carrier for the same customer')],
 '貨物合併僅指向第10條，欠可直接理解的條件。','補足責任人、合併規則和電子例外。')
add(1,'cross-boundary-cash','參考：申報資料的完整分類','Reference: declaration-information checklist',[
 ('旅客申報：管有人全名、身分證號碼或旅行證件號碼及簽發地、國籍、出生日期及地點、永久地址（境外者另填在港地址）；運輸工具識別、現金類物品種類及價值、出入境方向、日期及來源／目的地。如不是物品擁有人，填擁有人姓名／名稱及地址；代報者另填相同個人資料。','Traveller declaration: possessor’s full name, ID number or travel-document number and issuing place, nationality, birth date/place, permanent address (plus Hong Kong address if the permanent address is overseas); conveyance identifier, CBNI type/value, direction, date and origin/destination. If not the owner, give owner name/address; a separate declarant supplies the same personal particulars.'),
 ('貨物申報：非承運輸入／輸出人或承運人客戶的基本資料；自然人為上述個人資料但不另列在港地址，非自然人為名稱、適用商業登記號碼及業務地址。另填運輸工具、物品種類／價值、方向、日期、來源／目的地，以及適用收受人姓名／名稱及地址、貨單等批次識別。','Cargo declaration: basic information of the non-carrier importer/exporter or carrier’s customer. Individuals provide the above personal particulars without a separate Hong Kong-address item; entities provide name, applicable BR number and business address. Add conveyance, type/value, direction, date, origin/destination and, where applicable, recipient name/address and consignment identifier such as waybill number.')
],[ref('23','附表2、3','Schedules 2–3','Information to be Provided in Declaration')],
 '指定申報資料只作概括，須反覆查原文。','完整分類置於參考層，不與主要申報門檻混排。',kind='reference')

add(1,'risk-assessment','理解：2022年報告中的公司及戶口濫用','Understand: company and account misuse in the 2022 report',[
 ('空殼公司（shell company）可沒有實質營運而被用作隱藏擁有人或轉款；掛名公司（front company）則以貌似或實際合法業務及收支掩飾犯罪得益。2022年報告提到單一股東／董事、與香港無關連、業務含糊及資金頻繁大額進出而結餘低的組合警號；單一特徵不等於犯罪。','A shell company may lack substantive operations and be used to hide ownership or move funds. A front company uses apparently or actually legitimate business and receipts/payments to disguise criminal proceeds. The 2022 report describes combinations of sole ownership/directorship, no Hong Kong nexus, vague business and frequent large flows with low balances; no single feature proves crime.'),
 ('錢騾／傀儡戶口（money mule／stooge account）：由他人名義持有或控制、被用來接收及轉移犯罪得益的戶口；應留意持有人是否真正控制及了解交易。報告所述高速收轉款、小額試轉及更換戶口／裝置等，是需要與客戶背景一起評估的手法。','Money-mule or stooge accounts are accounts in other persons’ names or control used to receive and move criminal proceeds. Examine whether the holder genuinely controls and understands the activity. Rapid receipt and dissipation, small test transfers and changing accounts/devices described in the report need assessment alongside the customer profile.'),
 ('挪用現金補空（cash kiting，循環轉款）：在同一方控制的多個個人／公司之間循環轉款，虛增營業額或薪酬以取得未獲授權的額外貸款／信貸。最初循環的款項未必是犯罪得益，但藉此取得的欺詐貸款可以是；不是每個循環轉帳都自動構成這種手法。','Cash kiting circulates funds among individuals/entities under common control to inflate turnover or payroll and obtain unauthorized additional loans/credit. The initial circulating money need not be criminal proceeds; the fraudulently generated loan can be. Not every circular transfer automatically constitutes this method.')
],[ref('25','2022年版，第4.39–4.41、4.52–4.59、4.63、7.11–7.12段及註94','2022 edition, ¶4.39–4.41, 4.52–4.59, 4.63, 7.11–7.12 and footnote 94','Cash kiting')],
 '第25份只集中摘要、方法及MSO，缺直接支援CDD／監察的機制。','補概念及有界線的例子，不增添歷史統計背誦。')
add(6,'trade-based-laundering','例子：貿易如何轉移價值','Examples: how trade moves value',[
 ('2022年風險報告列出的手法包括高報／低報發票價值、同一貨物重複開票、超額／不足付運及虛構付運。重點是貨物、價格、數量及付款的真實關係，不能只因有發票就視為合理。這些是手法例子，不是完整定罪清單。','The 2022 risk report describes over/under-invoicing, multiple invoicing, over/under-shipment and phantom shipment. Examine the real relationship among goods, prices, quantities and payments; an invoice alone does not establish legitimacy. These are typology examples, not an exhaustive criminal test.'),
 ('報告專題4.5：走私汽車的內地買款先進入主腦帳戶，再轉往香港MSO在內地的帳戶，主腦最後在香港取回主要為現金的款項。學習重點是兩地安排可轉移犯罪得益的價值，不必見到同一筆銀行匯款直接跨境；毋須背案例金額或人名。','Box 4.5 describes Mainland proceeds from smuggled cars moving through the mastermind’s account into a Hong Kong MSO’s Mainland account, followed by mainly cash collection in Hong Kong. The learning point is that coordinated arrangements can transfer value without a directly observed cross-border bank transfer of the same funds; names and case amounts are reference details.')
],[ref('25','2022年版，第4.44、4.57–4.59段及專題4.5','2022 edition, ¶4.44, 4.57–4.59 and Box 4.5','Box 4.5')],
 '缺少把抽象TBML指標連到資金移動的來源例子。','補兩個簡短解釋，不把例子當唯一手法。')
add(1,'terrorist-financing','理解：合法資金也可被用於恐怖融資','Understand: lawful funds can finance terrorism',[
 ('2022年報告第8章說明，資金可來自捐款、會員費、商業收益或犯罪；轉移可經銀行、MSO、現金攜帶者或其他渠道。資金來源合法不代表用途或受益對象合法，評估仍須連同人物、目的、地區及交易背景。','Chapter 8 of the 2022 report discusses donations, membership fees, commercial income and crime as possible sources, with banks, MSOs, cash couriers and other channels for movement. Lawful origin does not establish lawful purpose or beneficiary; assess persons, purpose, geography and transaction context together.'),
 ('報告區分恐怖襲擊威脅與恐怖融資風險，兩者不能互換。它把香港非牟利組織的固有TF脆弱程度評為低，但指出在恐怖威脅／衝突地區從事人道援助者較易被濫用。這是2022年評估，不是所有慈善團體自動高風險，也不是現時已核實的地區評級。','The report distinguishes terrorist-attack threat from TF risk. It rates Hong Kong NPO inherent TF vulnerability low while identifying greater exposure for humanitarian activity in terrorism/conflict areas. These are 2022 findings, not automatic high-risk treatment of every charity or verified current geographical ratings.')
],[ref('25','2022年版，第8.5、8.11、8.27–8.32段','2022 edition, ¶8.5, 8.11, 8.27–8.32','CHAPTER 8')],
 'TF基礎欠報告對資金來源、渠道及NPO差異的說明。','補理解而不把歷史評級寫成現行規則。')
add(1,'sanctions','2022年PF評估範圍與PACE','The 2022 PF assessment and PACE',[
 ('就報告引用的FATF第1項建議而言，PF風險嚴格限於可能違反、沒有實施或逃避第7項建議的針對性財政制裁（TFS）責任。這個評估範圍與更廣的擴散活動概念須分開；不能只找「資金直接購買武器」，而漏看代名人、受控公司或制裁規避。','For FATF Recommendation 1 as discussed in the report, PF risk refers strictly to potential breach, non-implementation or evasion of the targeted financial sanctions (TFS) obligations in Recommendation 7. Distinguish this assessment scope from the broader proliferation concept; focusing only on direct weapon purchases can miss nominees, controlled entities or sanctions evasion.'),
 ('PACE是報告列明的四項策略，沒有先後流程：Prevention預防——法律制度、培訓及認識責任；Alert警報——及時傳遞制裁更新；Coordination協調——跨部門及監管合作、情報分享；Enforcement執法——調查及監督遵從。須記名稱並理解各自作用；不把2022年當時的制裁名單數字當作現況。','PACE names four strategy elements, not sequential steps: Prevention—legal controls, training and awareness; Alert—timely sanctions updates; Coordination—inter-agency/regulatory cooperation and intelligence sharing; Enforcement—investigation and compliance supervision. Recognize the names and purposes; the report’s 2022 sanctions-list counts are not current facts.')
],[ref('25','2022年版，第9.1、9.17、9.26、9.45–9.46段','2022 edition, ¶9.1, 9.17, 9.26, 9.45–9.46','Prevention')],
 'PF只列法例及評級，缺評估範圍與PACE。','補完整名稱和關係，防止把四類策略畫成流程。')

# Reference layers remain visible; no hidden answers or new interaction modes.
for n,sid in [(1,'risk-assessment'),(4,'application')]:
 for b in section(n,sid)['blocks']:
  if ('統計' in b['title']['tc'] or '數字' in b['title']['tc'] or b['title']['en']=='Evidence by legal form and purpose'):
   b['kind']='reference'

# Keep prior standalone supplements as baseline history, consolidate the editable prose.
def pair_call(v):return 'p('+repr(v['tc'])+', '+repr(v['en'])+')'
def emit(n,v):
 lines=['"""Source-authored bilingual manuscript; independently revised 2026-10-19. No bank input."""','from model import p, ref, block, section','','PART = dict(title='+pair_call(v['title'])+',','intro='+pair_call(v['intro'])+', sections=[']
 for s in v['sections']:
  lines.append('section('+repr(s['id'])+', '+repr(s['title']['tc'])+', '+repr(s['title']['en'])+', [')
  for b in s['blocks']:
   lines.append('    block('+repr(b['title']['tc'])+', '+repr(b['title']['en'])+', [')
   for x in b['points']:lines.append('        ('+repr(x['tc'])+', '+repr(x['en'])+'),')
   lines.append('    ], [')
   for r in b['refs']:lines.append('        ref('+', '.join(repr(x) for x in [r['doc'],r['locator']['tc'],r['locator']['en'],r['anchor']])+'),')
   lines.append('    ], kind='+repr(b['kind'])+'),')
  lines.append(']),')
 lines.append('])\n');(HERE.parent/f'part{n}.py').write_text('\n'.join(lines),encoding='utf-8')
for n,v in parts.items():emit(n,v)
(HERE.parent/'essentials.py').write_text('"""Compatibility entry: supplements consolidated into part1.py–part7.py on 2026-10-19.\nThe pre-consolidation source is preserved in independent-audit-2026-10-19/baseline.zip.\n"""\nADDITIONS = {}\n',encoding='utf-8')
(HERE/'findings.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Revised seven manuscripts;',len(findings),'traceable findings.')
