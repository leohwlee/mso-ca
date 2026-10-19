"""Apply the source-checked Chinese follow-up once; preserve prior audit evidence."""
from pathlib import Path
import sys, json, copy, hashlib, pprint
HERE=Path(__file__).resolve().parent
NOTES=HERE.parent
sys.path.insert(0,str(NOTES))
import build, memory_panels
from model import p, ref, block
parts=copy.deepcopy(build.PARTS)
panels=copy.deepcopy(memory_panels.PANELS)
findings=[]
baseline=json.loads((HERE/'baseline.json').read_text(encoding='utf-8'))
for n in (1,2,3,6):
    path=NOTES/f'part{n}.py'
    assert hashlib.sha256(path.read_bytes()).hexdigest()==baseline[f'revision\\study-notes\\part{n}.py'], path
def sec(n,sid):return next(s for s in parts[n]['sections'] if s['id']==sid)
def b(n,sid,i):return sec(n,sid)['blocks'][i]
def point(n,sid,bi,pi,tc,en):b(n,sid,bi)['points'][pi]=p(tc,en)
def record(fid,priority,location,problem,evidence,result):
    findings.append(dict(id=fid,priority=priority,location=location,problem=problem,evidence=evidence,result=result,status='已修正並重新生成'))

point(1,'risk-assessment',1,0,
 '香港2018年發表首份評估。第二次評估於2021年完成，報告於2022年發表；主要分析2016–2020年的五年數據，並載有其後部分發展。資料來自政府、監管、執法及私人業界。世界銀行方法結合數據及專家判斷分析威脅與脆弱性，先收集／分析及採取中期措施，再覆核更新。',
 'Hong Kong published its first assessment in 2018. The second assessment was completed in 2021 and published in 2022, primarily analysing five-year data for 2016–2020 and also reporting some later developments. Government, regulators, law enforcement and the private sector contributed. The World Bank methodology combines data and expert judgement on threats/vulnerabilities, with initial analysis/interim measures followed by review/update.')
b(1,'risk-assessment',1)['refs'][0]['locator']=p('2022年版，前言；行政摘要第3–5、24–29段；第2.4–2.9、5.4.1–5.4.12段','2022 edition, Foreword; Executive summary ¶3–5, 24–29; ¶2.4–2.9, 5.4.1–5.4.12')
record('C01','P2','Part 1 #risk-assessment／研究背景','未區分報告發表年、評估完成年及主要數據期。','25 前言、2.7–2.8（TC PDF5、27；EN同名段落）','兩語明列2021完成／2022發表／2016–2020主要數據，不把所有資料硬限在這五年。')
point(1,'risk-assessment',2,1,
 '2022年報告第8.5段的恐怖襲擊威脅為「中等（moderate）」：屬高／中等／低的三級警戒，意思是可能發生襲擊，但沒有具體情報顯示很可能發生。這與五級風險尺度下的恐怖分子資金籌集威脅／風險「中低」不同；襲擊威脅與籌資／轉資風險不可互換，亦不是現時已核實的安全判斷。',
 'Paragraph 8.5 of the 2022 report rates terrorist-attack threat “moderate” on a three-level high/moderate/low alert scale: an attack is possible, but there is no specific intelligence suggesting it is likely. This differs from medium-low TF threat/risk on the five-level risk scale. Attack threat and fund-raising/movement risk are distinct, and these dated findings are not a verified current security assessment.')
b(1,'risk-assessment',2)['refs'][0]['locator']=p('2022年版，第2.4–2.5、8.5段；行政摘要第18–23段','2022 edition, ¶2.4–2.5, 8.5; Executive summary ¶18–23')
record('C02','P2','Part 1 #risk-assessment／五級風險尺度','中文未譯moderate，也未說明恐襲採三級警戒。','25 8.5（TC PDF149）；2.4–2.5；行政摘要18–23','補中文名稱、三級尺度及具體意思，與TF五級評估分開。')
b(1,'risk-assessment',0)['refs'][0]['locator']['tc']='行政摘要；第2.1–2.10、5.4.1–5.4.29段'
for lang in ('tc','en'):
    r=b(1,'risk-assessment',4)['refs'][0]['locator']
    r[lang]=r[lang].replace('5.6.7–5.6.15','5.6.7–5.6.15'+('、5.6.21' if lang=='tc' else ', 5.6.21'))
record('C03','P2','Part 1 #risk-assessment／來源定位','中文MSO章引用不存在的5.4.30；SVF整體評級未定位至結論段。','25 TC5.4.29／EN5.4.30；兩語5.6.21','分語言保留正確段號，補SVF結論定位。')
point(1,'terrorist-financing',1,1,
 '報告把香港非牟利組織（NPO）的TF脆弱程度評為低；較易被濫用的是在香港運作及籌款、支援衝突地區人道服務的組織。原文也列出緩減因素：不少屬國際網絡、具內部盡職審查，捐款大多可追蹤，並有匿名捐款風險評估及銀行監察。這是2022年報告的評估，不能因此把所有慈善團體列為高風險，亦不是現時地區評級。',
 'The report rates Hong Kong non-profit organisations’ (NPOs’) inherent TF vulnerability low. Greater exposure concerns organisations operating and raising funds in Hong Kong to support humanitarian services in conflict zones. It also identifies mitigation: many belong to international networks with internal due diligence, donations are mostly traceable, and anonymous-donation risk assessment and bank monitoring apply. These are findings in the 2022 report, not grounds to classify every charity as high risk or current geographical ratings.')
record('C04','P1','Part 1 #terrorist-financing／合法資金與NPO','把衝突地區人道服務擴成恐怖威脅／衝突地區，並省去在港運作籌款及緩減背景。','25 8.27–8.32，尤其8.30（TC PDF152；EN同段）','兩語收窄到原文場景並補緩減措施；TC使用中文原文脆弱程度，EN保留inherent。')
x=b(1,'risk-assessment',3)['points'][2]
x['tc']=x['tc'].replace('但藉此取得的欺詐貸款可以是','但藉欺詐取得的額外貸款／信貸款項會被視作犯罪得益')
x['en']=x['en'].replace('the fraudulently generated loan can be','money generated from the additional loan/credit obtained through the fraud would be considered crime proceeds')
record('C05','P1','Part 1 #risk-assessment／cash kiting','「可以是／can be」弱化欺詐額外貸款款項屬犯罪得益的結論。','25 4.41及註94（TC PDF62；EN同段）','改為會被視作犯罪得益，仍保留最初循環款項未必是得益的區別。')

point(2,'inspection-investigation',1,0,
 '第9條獲授權人可在合理時間進入法定業務處所，查閱及複製紀錄、要求資料及解釋；對MSO，該條業務處所指第27條登記冊所示可經營金錢服務的處所。有關當局須向獲授權人提供書面授權的文本；獲授權人行使權力時須在合理切實可行範圍內盡快出示供查閱。這不是向受查人交付副本的規定。',
 'Section 9 authorized persons may enter statutory business premises at reasonable times, inspect/copy records and require information/explanations. For MSOs, these premises are those shown in the section 27 register as permitted for money service. The authority supplies its written authorization to the authorized person, who must produce a copy for inspection as soon as reasonably practicable when exercising the power. This does not require giving a copy to the inspected person.')
b(2,'inspection-investigation',1)['points'].append(p(
 '向MSO以外的資料持有人行使第9條的相關索取權，須有合理因由相信該人持有相關指明業務紀錄或交易資料，並有合理因由相信不能藉向受查MSO行使相應索取權而取得。與MSO沒有聯繫，不會單獨排除其資料持有人身分。',
 'For the relevant section 9 demands on another information holder, there must be reasonable cause to believe the person holds relevant specified business records or transaction information AND reasonable cause to believe these cannot be obtained through the corresponding powers concerning the inspected MSO. Lack of a connection with the MSO does not itself exclude information-holder status.'))
record('C06','P1','Part 2 #inspection-investigation／權力及責任','授權文本的交付對象含糊；其他資料持有人僅寫「按條件」。','04 s.9(6)–(7)、(12)–(16)（TC PDF43–47；EN41–46）','分清當局交予獲授權人與出示查閱，列明資料持有人兩項合理相信條件。')
point(2,'inspection-investigation',1,1,
 '第11條啟動調查：有關當局有合理因由相信可能已犯本條例罪行；或就MSO而言，為考慮第21／43條權力而有理由查訊是否違反相關指明條文。當局可書面指示法定人員調查（關長對應海關公職人員）；委任其他人則須財政司司長同意。調查員首次提出第12條要求前，須出示指示／委任文本。可依法要求文件、到場回答、書面答覆及合理協助，也可要求法定聲明確認。',
 'Section 11 permits investigation where the authority has reasonable cause to believe an Ordinance offence may have been committed; or, for an MSO, has reason to inquire into relevant specified contraventions when considering section 21/43 powers. It may give written directions to statutory personnel (Customs public officers for the CCE); appointing others needs the Financial Secretary’s consent. Before the first section 12 requirement, the investigator must produce the direction/appointment. Statutory powers cover records, attendance/answers, written responses, reasonable assistance and statutory-declaration verification.')
record('C07','P1','Part 2 #inspection-investigation／啟動調查','混用懷疑與合理相信，未區分法定人員指示及其他人委任。','04 s.11(1)–(5)、12（TC PDF51–55；EN50–53）','保留兩條啟動路徑，補財政司司長同意及首次出示時點。')
point(2,'inspection-investigation',1,2,
 '不得無合理辯解不遵從法定要求，或明知／罔顧實情而提供在要項上虛假或誤導的資料。第20條的銷毀、捏改、隱藏或處置罪，針對已被要求交出的紀錄／文件，並須有向獲授權人／調查員隱瞞可由該文件揭示的事實或事宜的意圖。第14條下，原訟法庭可命令遵從，也可就無合理辯解的不遵從，對本人及明知牽涉其中的人按藐視法庭方式懲罰；不以先違反另一法院命令為必要。',
 'Do not fail without reasonable excuse to comply with statutory requirements, or knowingly/recklessly supply materially false/misleading information. Section 20 destruction, falsification, concealment or disposal concerns records/documents required to be produced, with intent to conceal from the authorized person/investigator facts or matters they could disclose. Under section 14 the CFI may order compliance and punish the unexcused failure, including another person knowingly involved, as contempt; a prior breach of a separate court order is not required.')
point(2,'inspection-investigation',1,4,
 '第15條適用於第12(2)／(3)條強制取得的答覆、解釋或詳情：調查員須先告知／提醒證據使用限制；如內容可能使本人入罪，且本人在提供前作此聲稱，該要求及相關問答／解釋／詳情不得在法院刑事程序中用作針對本人的證據。但就該答覆等被控第13(1)、(3)、(5)–(8)條罪行，或《刑事罪行條例》第V部罪行的程序除外。這不是全面拒答權，也不是所有現存文件的普遍豁免。',
 'Section 15 concerns answers, responses, explanations or particulars compelled under section 12(2)/(3). The investigator must first inform/remind the person of the evidential limits. If the material might incriminate that person and the person claims this before providing it, the requirement and relevant question/answer, explanation or particulars are inadmissible against that person in criminal court proceedings. Exceptions concern offences under section 13(1), (3), (5)–(8) or Part V of the Crimes Ordinance in respect of that material. This is neither a general refusal right nor blanket immunity for pre-existing documents.')
record('C08','P1','Part 2 #inspection-investigation／違規及自證其罪','銷毀罪少隱瞞意圖；藐視誤限先違法院命令；強制作答保障未列條件及例外。','04 ss.14–15、20（TC PDF65–68、72；EN66–68、72）','修正犯罪要素及藐視途徑，列明事前聲稱、提醒及刑事使用例外。')
point(2,'inspection-investigation',1,5,
 '第17條搜查令自發出日期起計7日內可執行。取走的紀錄／文件可自取走日起計保留不超過6個月；如屬或可能屬任何刑事程序或本條例下程序所需，可保留該程序所需的較長期間，不以刑事程序已開始為前提。取走後須在合理切實可行範圍內盡快發收據。第19條要求讓原本有權查閱的人在所有合理時間查閱、複製或記錄詳情，可施加合理保安或其他條件；該條沒有訂明免費。',
 'A section 17 warrant is executable within seven days beginning on its date. Removed records/documents may be retained for up to six months beginning on removal, or for a longer necessary period if they are or may be required for any criminal proceedings OR proceedings under the Ordinance. Criminal proceedings need not already have begun. Give a receipt as soon as reasonably practicable after removal. Section 19 requires access, copying or recording of details at all reasonable times for persons otherwise entitled to inspect, subject to reasonable security or other conditions; it does not specify free access.')
record('C09','P1','Part 2 #inspection-investigation／取走紀錄','錯加已開始刑事程序的延長前提及免費查閱字眼。','04 s.17(1)、(4)–(5)、19（TC PDF68–72；EN68–72）','按「屬或可能屬」及兩類程序改正；刪免費，補原有查閱權及合理條件。本項更正上一輪F07的錯誤判斷，原紀錄保留。')
sec(2,'inspection-investigation')['blocks'].append(block('參考：另一監管當局索取客戶資料','Reference: customer information sought by another authority',[
 ('第9A／12A條針對「訂明人士」被另一有關當局的獲授權人／調查員要求交出客戶事務資料。訂明人士包括金融機構、TCSP持牌人、DPMS註冊人及持牌虛擬資產服務提供者的有聯繫實體；「另一」指不是該受要求人士本身的有關當局。', 'Sections 9A/12A protect customer-affairs information where a prescribed person receives a demand from another authority’s authorized person/investigator. Prescribed persons include financial institutions, TCSP licensees, PMS registrants and associated entities of licensed VAS providers. “Another” means an authority other than that person’s own relevant authority.'),
 ('第9A條：除非另一當局認為披露／交出對第9條目的屬必要，並以書面證明此意見，否則不須據第9條交出客戶事務資料。第12A條須同時符合：調查員有合理因由相信該客戶可能提供與調查相關資料，及另一當局認為披露／交出對調查必要並書面證明。這是客戶事務資料的特定限制，不是整體免受查察。', 'Under section 9A, customer-affairs disclosure/production is not required unless the other authority considers it necessary for section 9 purposes and certifies that opinion in writing. Section 12A requires BOTH the investigator’s reasonable cause to believe the customer may provide investigation-relevant information AND the other authority’s written certification of its opinion that disclosure/production is necessary for the investigation. This is a specific customer-information restriction, not immunity from inspection.')
],[ref('04','第8、9A、12A條','ss.8, 9A, 12A','When power under section 9 invoked by other regulatory authority')],kind='reference'))
record('C10','P1','Part 2 #inspection-investigation／另一當局索取資料','欠跨當局客戶資料限制，容易誤解調查權無條件。','04 ss.8、9A、12A（TC PDF35–36、48、55–56；EN35–36、47、54–55）','補訂明人士、另一當局、書面必要性證明及12A的額外AND條件。')
x=b(2,'licence-scope',0)['points'][3]
x['tc']=x['tc'].replace('法院可另取消其經營資格。','法院可另命令取消其持有牌照資格，期間由命令日期起計並在命令中指明。')
x['en']=x['en'].replace('The court may also disqualify the person from operating.','The court may also disqualify the person from holding a licence for a period specified in its order and beginning on the order’s date.')
point(2,'enforcement',0,1,
 '第48條容許在法定合理懷疑下無手令拘捕，按要求出示委任證據。拘捕後須立即帶往警署；如為進一步查訊有必要，可先帶往海關辦事處，再帶往警署。無論已拘捕與否，均不得在沒有被落案控告並帶到裁判官席前的情況下扣留超過48小時。搜身須由同性別人員進行。',
 'Section 48 permits warrantless arrest on statutory reasonable suspicion, with appointment evidence produced on request. Immediately take the arrested person to a police station; where necessary for further inquiries, first take the person to a Customs office and then a police station. Whether arrested or not, no person may be detained for more than 48 hours without being charged and brought before a magistrate. Searches must be by a person of the same sex.')
record('C11','P1','Part 2 #licence-scope、#enforcement','取消資格的對象錯寫經營；拘捕後「盡快」弱化立即，48小時條件含糊。','04 s.29(3)、48(2)–(6)（TC PDF80、101–102；EN同條）','改持有牌照資格；保留立即、先海關查訊必要性及不論已拘捕與否的48小時上限。')
x=b(2,'review',0)['points'][0]
x['tc']=x['tc'].replace('有充分因由可按程序申請延長','審裁處在給予覆核各方陳詞機會後，可基於充分因由延長')
x['en']=x['en'].replace('an extension may be granted for good cause through the statutory procedure','the tribunal may extend for good cause after giving the parties an opportunity to be heard')
point(2,'review',0,3,
 '向上訴法庭就法律、事實或混合問題上訴，須先獲上訴法庭許可：上訴有合理機會得直，或有其他有利於秉行公正的理由應予聆訊。上訴本身不自動暫緩審裁處裁定；審裁處可依第70條，或在已提出上訴後由上訴法庭依第73條，按申請命令暫緩。',
 'Appeal to the Court of Appeal on law, fact or mixed questions requires its leave: a reasonable prospect of success OR another reason in the interests of justice to hear it. Appeal does not itself stay the tribunal’s determination. On application, the tribunal may order a stay under section 70, or the Court of Appeal under section 73 once an appeal has been lodged.')
x=b(2,'statutory-administration',0)['points'][2]
x['tc']=x['tc'].replace('非刑事事項按民事證明標準處理','第78條所列的違反、行為、意圖等事宜，當局在非刑事程序中按民事舉證準則證明或信納即足夠')
x['en']=x['en'].replace('Non-criminal matters use the civil standard of proof.','For the contraventions, conduct, intentions and related matters listed in section 78, the authority need only prove or be satisfied on the civil standard in non-criminal proceedings.')
record('C12','P2','Part 2 #review、#statutory-administration','許可標準中文錯字、暫緩只提法院；延長覆核欠陳詞，民事標準說法太泛。','04 ss.59(2)、70–73、78（TC PDF302、312–315、330–331）','補雙方陳詞及兩種暫緩途徑，限定民事標準適用事宜。')
point(2,'statutory-administration',1,1,
 '受第9／12條要求或第76E條所列紀律通知而取得資料的人，不得任意披露。第76F條亦約束經其涵蓋的76C／76D／76E途徑取得資料的指明收取人及再收取人，但不包括76C(1)(b)、(2)(b)及76D(1)(a)、(f)、(i)的披露。',
 'Persons obtaining information through section 9/12 requirements or the disciplinary notices listed in section 76E may not freely disclose it. Section 76F also restricts specified and onward recipients through its covered 76C/76D/76E routes, excluding disclosures under 76C(1)(b), (2)(b) and 76D(1)(a), (f), (i).')
b(2,'statutory-administration',1)['points'].append(p(
 '准許披露的途徑是擇一（OR）：有關當局同意（可附條件）；資料已可供公眾取得（第76E條另要求源於不受76B禁止的披露）；就本條例事項徵詢／提供專業意見；披露者是相關司法或其他法律程序的一方並為該程序披露；或依香港法院、裁判官、審裁處命令或香港法律要求披露。不能把任意網上洩漏或外地要求直接當成同一例外。',
 'Permitted routes are alternatives (OR): authority consent, which may carry conditions; public availability (section 76E additionally requires availability resulting from disclosure not prohibited by 76B); professional advice on Ordinance matters; disclosure connected with proceedings to which the discloser is a party; or a Hong Kong court, magistrate or tribunal order or Hong Kong legal requirement. An arbitrary online leak or foreign demand is not automatically the same exception.'))
record('C13','P2','Part 2 #statutory-administration／保密','概括所有再收取人及依法公開，未區分76E／F適用範圍和香港要求。','04 ss.76A、76E–76F（TC PDF317、325–328；EN同條）','列明排除途徑及五項OR例外，分開76E公開資料條件。')

sec(3,'sector-specific')['blocks'].append(block('參考：附表2何時適用於其他行業','Reference: when Schedule 2 applies to other sectors',[
 ('保險：第5(2)條就獲授權保險人只適用於長期業務；第5(3)條就保險代理／代理機構／經紀公司只適用於涉及《保險業條例》附表1第2部第3欄長期業務保險合約的交易。不是所有一般保險交易都直接套用同一範圍。', 'Insurance: section 5(2) applies Schedule 2 to an authorized insurer only for long-term business; section 5(3) applies to agents/agencies/broker companies only for transactions involving insurance contracts described in column 3 of Part 2 of Schedule 1 to the Insurance Ordinance (long-term business). Do not apply this scope indiscriminately to all general insurance.'),
 ('儲值支付工具發行：第5(4)條的條件須同時成立——可儲存最高價值>3,000元，AND屬發行人提供予使用者的實物裝置且價值儲存在該裝置。恰好3,000元不符合這項門檻。這是該條對發行的適用界線，不表示其他電子錢包完全不受監管。', 'SVF issuance: section 5(4) requires BOTH maximum stored value >HK$3,000 AND a physical device supplied by the issuer to the user with the value stored on that device. Exactly HK$3,000 does not satisfy the threshold. This is the section’s issuance boundary, not a statement that other electronic wallets are wholly unregulated.'),
 ('會計／法律專業人士：以業務形式在香港為客戶擬備或進行涉及以下一項或以上的交易才適用第5A(3)條：買賣地產；管理客戶款項、證券或其他資產；管理銀行、儲蓄或證券戶口；為成立／營運／管理法團組織資金；成立／營運／管理法人或法律安排；買賣業務實體；或法定信託／公司服務（完整服務類別見Part 2末節）。', 'Accounting/legal professionals: section 5A(3) applies when, by way of business in Hong Kong, they prepare or carry out for a client transactions involving one or more of: buying/selling real estate; managing client money, securities or other assets; managing bank/savings/securities accounts; organising contributions to create/operate/manage corporations; creating/operating/managing legal persons or arrangements; buying/selling business entities; or statutory trust/company services (the complete service categories are in the final Part 2 section).'),
 ('地產代理：在香港涉及為客戶買賣地產的交易；不是概括所有租賃。TCSP持牌人：以業務形式在香港為客戶擬備／進行法定信託或公司服務交易。以上會計、法律、地產及TCSP情況，交易標的在港或境外均無關重要。', 'Estate agents: involvement in Hong Kong in client real-estate purchase/sale transactions, not every tenancy. TCSP licensees: preparing/carrying out client transactions concerning statutory trust/company services by way of business in Hong Kong. For these accounting, legal, estate-agent and TCSP cases, the transaction’s subject matter may be in Hong Kong or elsewhere.'),
 ('DPMS B類：以業務形式在香港與客戶進行非豁除的指明現金交易，才適用第5A(5A)條。就付款B類註冊人，豁除須同時符合：現金付款純粹由該B類付予另一B類，AND交易只有這兩名B類當事人；不能把收款方或任何兩家交易商都一概當成豁除。A／B註冊及現金門檻見Part 2。', 'Category B DPMS: section 5A(5A) applies to non-excluded specified cash transactions with a customer by way of business in Hong Kong. For the paying Category B registrant, exclusion requires BOTH exclusively cash payments by that registrant to another Category B registrant AND those two registrants being the only transaction parties. Do not automatically exempt the recipient or every transaction between two dealers. See Part 2 for registration and cash thresholds.')
],[ref('04','第5(2)–(4)、5A(2)–(7)條；附表1第1部第1條','ss.5(2)–(4), 5A(2)–(7); Schedule 1 Part 1 s.1','maximum value that can be stored')],kind='reference'))
record('C14','P1','Part 3 #sector-specific／附表2適用界線','只有行業名稱而欠第5／5A決定適用性的交易條件及例外。','04 ss.5(2)–(4)、5A(2)–(7)（TC/EN PDF28–32）','補其他行業參考層：七類專業服務、香港活動／境外標的、實物SVF >3,000及雙B純付款AND兩交易方。')
point(3,'definitions',0,1,
 '業務關係是有持續性元素的業務、專業或商業關係，或機構在對方首次以準客戶身分接觸時預期有持續性元素的關係（OR）。非經常交易是機構與沒有業務關係的客戶之間的交易；一次交易金額小，不會消除本已存在的持續關係。',
 'A business relationship is a business, professional or commercial relationship with an element of duration OR one expected to have that element when the person first contacts the institution as a potential customer. An occasional transaction is with a customer who has no business relationship. A small transaction does not erase an existing ongoing relationship.')
point(3,'definitions',1,1,
 '信託實益擁有人包括：有權享有信託財產既得權益的受益人或某類別受益人（不論管有權、剩餘權或復歸權，亦不論可否廢除）；財產授予人；受託人；保護人／執行人；或最終控制信託的自然人。不得把受益人類別漏掉或限成個人。對公司、合夥、信託以外的人，第1條涵蓋最終擁有／控制的自然人，或該人代其行事的另一人。',
 'Trust BOs include a beneficiary or class of beneficiaries entitled to a vested interest in trust property, whether in possession, remainder or reversion and whether defeasible or not; the settlor; trustee; protector/enforcer; or an individual with ultimate control. Do not omit beneficiary classes or limit beneficiaries to individuals. For a person other than a corporation, partnership or trust, section 1 covers an individual ultimately owning/controlling it or another person on whose behalf it acts.')
b(3,'definitions',0)['points'][2]['tc']=b(3,'definitions',0)['points'][2]['tc'].replace('業務日','營業日')
b(3,'definitions',3)['refs'][0]['locator']=p('附表1第2部第1條；附表2第1條','Schedule 1 Part 2 s.1; Schedule 2 s.1')
panel=panels[3]['definitions'][0]
panel['rows'][2][1]=p('享有信託財產既得權益的受益人／受益人類別；授予人、受託人、保護人／執行人；最終控制的自然人。','Beneficiaries/classes with vested interests in trust property; settlors, trustees, protectors/enforcers; individuals with ultimate control.')
record('C15','P1','Part 3 #definitions及實益擁有人對照表','信託BO誤限個人／資本；業務關係漏實際持續性OR；營業日術語及DNFBP定位錯。','04 附表1第2部第1條；附表2第1條（TC PDF345–356；EN352–354）','修正文稿與表格，完整保留受益人類別、財產權益及各分支自然人／人的差別；不更動Part 6本已正確的定義。')
point(3,'simplification',0,1,
 '合資格類別：金融機構；在對等司法管轄區成立、經營相若金融業務、有相若措施且受相類當局監管的機構；在任何證券市場上市的法團；合資格投資公司；香港政府／公共機構；對等司法管轄區政府／相若公共機構。投資公司須由以下人士為全部投資者做相類CDD：金融機構，OR在香港／對等司法管轄區成立、有相類合規措施並受遵從監管的機構。',
 'Qualifying categories: financial institutions; equivalent-jurisdiction institutions with similar financial business, similar compliance measures and comparable-authority supervision; corporations listed on any stock market; qualifying investment companies; Hong Kong Government/public bodies; and equivalent-jurisdiction governments/similar bodies. For an investment company, all investors must receive similar CDD from an FI OR an institution established in Hong Kong/an equivalent jurisdiction with similar compliance measures and supervision for compliance.')
point(3,'special-cases',0,0,
 '非親身識別至少加一項：用未曾使用的第2(1)(a)／(ab)條資料再核實；補充核實已取得資料；或確保付款（多次時為首筆）經客戶同名戶口。該戶口須在認可機構，或同時符合四條件的境外機構：在對等司法管轄區成立、經營相若銀行業務、有相類合規措施、並受當地相當於金管局的主管當局監管。已按認可數碼識別系統資料完成第2(1)(a)／(ab)條措施者有第9(2)條例外，不是所有視像／電子程序都符合。',
 'Non-face-to-face identification requires at least one: further verification with previously unused section 2(1)(a)/(ab) material; supplementary verification of obtained information; or payment (the first if multiple) through the customer’s same-name account. That account must be at an authorized institution OR an overseas institution meeting ALL four conditions: equivalent-jurisdiction establishment, similar banking business, similar compliance measures and supervision by a local authority with HKMA-like functions. Section 9(2) excepts customers whose section 2(1)(a)/(ab) measures use a recognized digital-ID system, not every video/electronic process.')
x=b(3,'ongoing-and-records',0)['points'][0]
x['tc']+='第5(4)／(5)條分別保留認可數碼識別、經適當評估不屬高風險的前政治人物例外；一般CDD及監察仍適用。'
x['en']+=' Sections 5(4)/(5) preserve the recognized-digital-ID and appropriately assessed non-high-risk former-PEP exceptions respectively; ordinary CDD and monitoring still apply.'
record('C16','P1','Part 3 #simplification、#special-cases、#ongoing-and-records','投資公司及首筆付款機構仍以「合資格／四項條件」代替內容；額外監察略去法定例外。','04 附表2s.4(3)(d)、5(3)–(5)、9（TC PDF364、367–368、371；EN同條）','列清兩種合資格機構條件及兩項額外監察例外。')
# Remove an unsupported present-tense edition label in the related-foreign-FI definition.
x=b(6,'intermediaries',2)['points'][0]
x['tc']=x['tc'].replace('符合現行條例的經遷冊MSO','第04份所存版本所指經遷冊MSO')
record('C17','P2','Part 6 #intermediaries／相關境外金融機構','「現行條例」把存檔核對說成已核實現行法例。','04 附表2s.18(7)，2026-09-24存檔；本輪沒有另行現行法例核實','改為第04份所存版本，實質三種關係及條件不變。')

def emit(n,v):
    pair=lambda x:'p('+repr(x['tc'])+', '+repr(x['en'])+')'
    lines=['"""Source-authored bilingual manuscript; source-checked 2026-10-19. No bank input."""','from model import p, ref, block, section','','PART = dict(title='+pair(v['title'])+',','intro='+pair(v['intro'])+', sections=[']
    for s in v['sections']:
        lines.append('section('+repr(s['id'])+', '+repr(s['title']['tc'])+', '+repr(s['title']['en'])+', [')
        for vblock in s['blocks']:
            lines.append('    block('+repr(vblock['title']['tc'])+', '+repr(vblock['title']['en'])+', [')
            for x in vblock['points']:lines.append('        ('+repr(x['tc'])+', '+repr(x['en'])+'),')
            lines.append('    ], [')
            for r in vblock['refs']:lines.append('        ref('+', '.join(repr(x) for x in [r['doc'],r['locator']['tc'],r['locator']['en'],r['anchor']])+'),')
            lines.append('    ], kind='+repr(vblock['kind'])+'),')
        lines.append(']),')
    lines.append('])\n')
    (NOTES/f'part{n}.py').write_text('\n'.join(lines),encoding='utf-8')
assert not (HERE/'findings.json').exists(), 'Do not overwrite completed findings'
for n in (1,2,3,6):emit(n,parts[n])
text=(NOTES/'memory_panels.py').read_text(encoding='utf-8')
start=text.index('PANELS = ');end=text.index('\nEMPHASIS = ')
(NOTES/'memory_panels.py').write_text(text[:start]+'PANELS = '+pprint.pformat(panels,width=140,sort_dicts=False)+'\n'+text[end:],encoding='utf-8')
(HERE/'findings.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Applied',len(findings),'source-checked finding groups; prior audit preserved.')
