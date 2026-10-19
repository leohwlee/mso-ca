"""Apply the final original-first review of 04 and 25; no question-bank input."""
import csv, importlib, json, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
from model import block, ref, section
parts={n:importlib.import_module(f'part{n}').PART for n in (1,2,3)}
new_titles=('參考：第5A部信託或公司服務提供者（TCSP）','參考：第5B部虛擬資產服務','參考：第5C部貴金屬及寶石交易商（DPMS）')
for s in parts[2]['sections']:
    s['blocks']=[b for b in s['blocks'] if b['title']['tc'] not in new_titles]
if not any(s['id']=='other-sector-regimes' for s in parts[2]['sections']):
    parts[2]['sections'].append(section('other-sector-regimes','參考：其他行業制度與MSO的界線','Reference: other sector regimes and MSO boundaries',[]))
findings=json.loads((HERE/'findings.json').read_text(encoding='utf-8'))
def add(fid,n,sid,b,issue,impact):
    if fid in ('F30','F31','F32'):sid='other-sector-regimes'
    s=next(s for s in parts[n]['sections'] if s['id']==sid)
    s['blocks']=[x for x in s['blocks'] if x['title']!=b['title']]+[b]
    findings[:]=[x for x in findings if x['id']!=fid]
    findings.append(dict(id=fid,part=n,section=sid,priority='P2',issue=issue,impact=impact,before=None,after=[b],refs=b['refs'],status='fixed'))

add('F30',2,'statutory-map',block('參考：第5A部信託或公司服務提供者（TCSP）', 'Reference: Part 5A trust or company service providers (TCSPs)',[
('信託或公司服務指在香港以業務形式向他人提供一項或以上：成立法團／其他法人；擔任或安排他人擔任董事、秘書、合夥人或其他法人類似職位；向法人／法律安排提供註冊辦事處、營業、通訊或行政地址；擔任或安排他人擔任明示信託／類似法律安排的受託人，或代名股東（不包括證券於認可證券市場上市的法團的代名股東）。第5A部由公司註冊處處長執行。第53B條豁除政府、認可機構、以該業務附屬於主要業務的持牌法團、會計及法律專業人士和訂明類別；豁除本部不等於豁除其他適用AML責任。','Trust or company service means providing, in Hong Kong by way of business to others, one or more of: formation of corporations/other legal persons; acting or arranging directors, secretaries, partners or similar positions for legal persons; registered, business, correspondence or administrative addresses for legal persons/arrangements; acting or arranging trustees of express trusts/similar arrangements or nominee shareholders, excluding nominees for corporations listed on a recognized stock market. Part 5A is administered by the Registrar of Companies. Section 53B excludes government, authorized institutions, licensed corporations whose TCSP business is ancillary to their principal business, accounting/legal professionals and prescribed classes; exclusion from this Part is not exclusion from other applicable AML duties.'),
('一般牌照及續期為3年，處長可在個案訂較短期間；續期須在到期前至少60日提出。及時申請後仍待決時，除申請撤回或牌照撤銷／暫時吊銷外，牌照延續至續期或拒絕決定生效。不能套用MSO的2年。','Grant and renewal normally last three years, with a shorter period possible in a particular case. Apply at least 60 days before expiry. While a timely renewal is pending, the licence continues until renewal or the refusal takes effect, unless the application is withdrawn or licence revoked/suspended. Do not substitute the MSO two-year term.'),
('適當人選審查及最終擁有人／合夥人／董事事前書面批准有獨立條文。無牌經營最高第6級罰款及6個月；第53Z條紀律措施包括公開譴責、補救及最高50萬元罰款，未按時補救另可每日最高1萬元。這些不是MSO第21／43條的罰額。','Separate provisions govern fitness and propriety and prior written approval of ultimate owners/partners/directors. Unlicensed business carries up to a level 6 fine and six months. Section 53Z discipline includes public reprimand, remediation and a penalty up to HK$500,000, with a further daily penalty up to HK$10,000 for overdue remediation. These are not the MSO section 21/43 ceilings.'),
],[ref('04','附表1信託或公司服務定義；第53B、53F–53K、53O、53S–53U、53Z條','Schedule 1 trust or company service definition; ss.53B, 53F–53K, 53O, 53S–53U, 53Z','Regulation of Trust or Company Service Providers')],kind='reference'),
'其他行業制度只有名稱，無法辨別TCSP與MSO的監管及牌照差異。','完成第5A部原文閱讀後補監管對象、豁除、期限及責任層級；低關聯行政細節保留原文索引。')

add('F31',2,'statutory-map',block('參考：第5B部虛擬資產服務', 'Reference: Part 5B virtual asset services',[
('VA（virtual asset，虛擬資產）的基本定義是加密保護的數碼價值，表述為計算單位或經濟價值儲存形式；具備公眾接受的交易媒介用途，或相關管理／運作／管治的投票權，並可電子轉移、儲存或買賣；另受訂明特徵及指定／排除權規限。央行／政府發行貨幣、有限用途代幣、證券／期貨及儲值支付工具儲值金額／按金等有法定排除，不能把所有數碼資產當同一類。','VA means virtual asset. The basic definition concerns cryptographically secured digital value expressed as a unit of account or store of economic value, with a public medium-of-exchange use OR relevant management/operation/governance voting rights, and capable of electronic transfer, storage or trading; prescribed characteristics and designation/exclusion powers also apply. Statutory exclusions include central-bank/government-issued currency, limited-purpose tokens, securities/futures and SVF float/deposits. Not all digital assets are the same legal category.'),
('所存附表3B列「經營虛擬資產交易所」：電子設施經常接受／提出買賣要約或介紹交易各方，以形成具約束力交易，並且服務提供者直接或間接管有客戶金錢或虛擬資產。上述交易設施條件與管有條件須同時成立。不得僅因涉及虛擬資產便推定所有服務均是此項；也須考慮第53ZRB條向香港公眾積極推廣的規則。','Stored Schedule 3B specifies operating a VA exchange: electronic facilities regularly make/accept offers or introduce trading parties in a manner producing binding transactions, AND the provider directly or indirectly possesses client money or VAs. Both the trading-facility and possession conditions matter. VA involvement alone does not make every service this scheduled activity; section 53ZRB active marketing to the Hong Kong public also matters.'),
('證監會發牌；提供者須為《公司條例》所指公司或註冊非香港公司，並符合適當人選及紀錄處所批准等條件。每項服務至少2名獲批負責人員，其中至少1名執行董事、至少1名通常居港；每名屬個人的執行董事均須獲批為負責人員，且任何時間至少1名負責人員可供監督。這些條件須並行符合。','The SFC licenses providers. A provider must be a Companies Ordinance company or registered non-Hong Kong company and meet fitness, record-premises approval and other conditions. Each service needs at least two approved responsible officers, including at least one executive director and at least one ordinarily resident in Hong Kong; every individual executive director must be approved, and at least one responsible officer must be available at all times to supervise. These are concurrent requirements.'),
('客戶資產有獨立保障；牌照／批准、審計、介入及紀律制度均另有規定。無合理辯解無牌提供服務，循公訴最高500萬元及7年（持續罪行另計）；第53ZSP條紀律罰款上限為1,000萬元或所得利潤／避免損失的3倍，以較高者為準。不要把服務提供者、代表的罪行或MSO規則混用。','Client assets have separate protection, alongside distinct approval, audit, intervention and disciplinary regimes. Unlicensed provision without reasonable excuse carries, on indictment, up to HK$5 million and seven years, plus a continuing-offence penalty. Section 53ZSP disciplinary penalties can reach the greater of HK$10 million and three times profit gained/loss avoided. Do not mix provider offences with representative offences or MSO rules.'),
],[ref('04','第53ZRA–53ZRD、53ZRK、53ZRO、53ZRT、53ZSP條；附表3B','ss.53ZRA–53ZRD, 53ZRK, 53ZRO, 53ZRT, 53ZSP; Schedule 3B','Operating a VA exchange')],kind='reference'),
'第5B部僅作制度名稱提示，缺少活動定義及與MSO制度的界線。','補定義、AND條件、監管者、負責人員及責任概覽；不引用範圍外新法或把2022年提案當現行制度。')

add('F32',2,'statutory-map',block('參考：第5C部貴金屬及寶石交易商（DPMS）', 'Reference: Part 5C dealers in precious metals and stones (DPMS)',[
('DPMS業務包括買賣、進出口、生產／提煉／增值加工貴金屬、寶石、貴重產品，發行／贖回／買賣貴重資產支持工具，以及相關中介活動。物流業者僅在通常業務中代客進出口貨物，不因此單獨成為DPMS。第53ZUA條另豁除政府、認可機構、持牌當押商及符合附屬業務條件的指定金融機構等。','DPMS business includes trading, import/export, manufacture/refining/value-adding work on precious metals, stones or precious products, issuing/redeeming/trading precious-asset-backed instruments, and related intermediary activity. Ordinary logistics import/export for others alone does not make the operator a DPMS. Section 53ZUA separately excludes government, authorized institutions, licensed pawnbrokers and specified financial institutions satisfying ancillary-business conditions, among others.'),
('海關關長管理A／B類註冊。指明現金交易是在香港支付或收取的現金總額≥120,000港元（或等值外幣）；指明交易是非現金付款總額達同一門檻，而且不屬指明現金交易。均須合併有關連或看來有關連的操作。A類可作指明交易但不可作指明現金交易；B類可作兩者。這是DPMS交易分類，不是跨境CBNI的「>120,000」界線。','The CCE administers A/B registration. A specified cash transaction involves cash payments made/received in Hong Kong totalling ≥HK$120,000 or foreign-currency equivalent. A specified transaction reaches that threshold in non-cash payments AND is not a specified cash transaction. Aggregate linked or apparently linked operations. Category A covers specified transactions but excludes specified cash transactions; Category B covers both. This DPMS classification differs from the cross-boundary CBNI >HK$120,000 boundary.'),
('B類須作適當人選審查；一般有效3年，關長可按個案決定其他期間，續期至少在到期前60日申請。A類設週年費，不能把B類3年期限套給A類。無註冊進行受限制交易或作不實註冊聲稱，最高第6級罰款及6個月。','Category B requires fitness and propriety assessment; registration normally lasts three years, or another period determined for the particular case, with renewal applied for at least 60 days before expiry. Category A has an annual fee; do not apply the B three-year term to A. Restricted transactions without registration or false holding-out carry up to a level 6 fine and six months.'),
('非香港交易商的特別制度須同時符合：非通常居港個人，或境外設立且非註冊非香港公司／經遷冊公司的法人；在港無營業地點；每公曆年在港經營≤60日。其指明現金交易須盡快向關長報告，無論如何在交易翌日屆滿與相關個人最早離港兩者較早之前；相關個人包括交易時在港的個人交易商及代其交易的個人。此例外不是任何海外客戶均免註冊。','The special non-Hong Kong dealer regime requires all of these: a non-ordinarily-resident individual, or an overseas-established legal person that is neither a registered non-Hong Kong company nor a re-domiciled company; no Hong Kong place of business; and Hong Kong business on ≤60 days per calendar year. Report specified cash transactions to the CCE as soon as practicable and before the earlier of expiry of the day after the transaction and the earliest departure of a specified individual: the individual dealer present at the transaction or an individual acting for it. This is not a blanket exception for overseas customers.'),
],[ref('04','第53ZTZ–53ZUA、53ZUE、53ZUH、53ZUO–53ZUQ、53ZVK條；附表3H–3J','ss.53ZTZ–53ZUA, 53ZUE, 53ZUH, 53ZUO–53ZUQ, 53ZVK; Schedules 3H–3J','specified cash transaction')],kind='reference'),
'DPMS只列名稱，12萬元可能與CBNI或MSO門檻混淆。','補A/B分類、相連操作、≥門檻、年期與非香港交易商AND條件；詳細申請行政事項維持參考優先級。')

add('F33',3,'sector-specific',block('參考：其他行業的附表如何配對', 'Reference: pairing the other sector schedules',[
('附表3A是TCSP費用；3B界定虛擬資產服務；3C是其費用，3D是相聯實體的通知資料，3E是周年申報資料，3F是財務報表及核數師報告，3G是2023年開始的虛擬資產過渡安排。它們各有適用對象，不可把「周年申報」誤認為MSO第15份的半年申報。','Schedule 3A contains TCSP fees; 3B defines VA services; 3C contains VA fees, 3D associated-entity notifications, 3E annual-return information, 3F financial statements/auditor reports, and 3G VA transitional arrangements beginning in 2023. Each has its own subject; these annual returns are not the MSO half-yearly returns in document 15.'),
('附表3H／3I分別訂DPMS指明現金／非現金交易120,000元門檻；3J列非香港交易商現金報告所需資料：交易商及客戶基本資料、相關個人出入境資料、交易日期／貨品／現金金額／地點。3K為DPMS費用。上述制度條件見Part 2末節「其他行業制度與MSO的界線」；費用細目及已過啟動期的過渡程序保留原文查考，不當作MSO日常必背清單。','Schedules 3H/3I set the HK$120,000 DPMS cash/non-cash thresholds. Schedule 3J requires basic dealer/customer information, specified individuals’ travel details, and the transaction date, goods, cash amount and location. Schedule 3K contains DPMS fees. See the final Part 2 section, Other sector regimes, for applicability; itemised fees and transition procedures whose commencement periods have passed remain source references, not a daily MSO memorisation list.'),
],[ref('04','附表3A–3K；Part 2筆記末節','Schedules 3A–3K; Part 2 notes, final section','Information to be Provided in Cash Transaction Report')],kind='reference'),
'附表3A–3K未交代用途，官方「附表」模組與現有筆記之間有空白。','完成附表閱讀並補功能導航與資料類別；明示未逐項搬錄其他行業費表及歷史過渡程序的取捨。')

add('F34',1,'risk-assessment',block('2022年報告：跨行業風險如何連到MSO', '2022 report: how cross-sector risks connect to MSOs',[
('身分真實不等於實際使用者或用途真實。第5.2.13–5.2.17段區分遙距假冒身分風險與招募真人開傀儡戶口；可靠身分技術可減低前者，後者仍須靠客戶背景、控制者及交易行為辨識。傀儡戶口也存在於親身開戶，並非虛擬銀行特有。','A genuine identity does not prove the real user or purpose. Paragraphs 5.2.13–5.2.17 distinguish remote impersonation from recruiting real people to open stooge accounts. Reliable identity technology can reduce the former; the latter still requires attention to customer background, control and transaction behaviour. Stooge accounts also occur with face-to-face onboarding, not only virtual banks.'),
('多重支付中介可遮蔽最初匯款人及最終受益人；證券第三者付款、代名投資及TCSP成立多層公司，也可能掩蓋實益擁有權／資金來源。理解共同機制，不把「經銀行轉來」「由專業人士介紹」視為資金合法的證明。報告中的他業監管措施並不因此自動變成MSO的同一套法定程序。','Multiple payment intermediaries can obscure the original payer and ultimate recipient. Securities third-party payments, nominee investments and layered companies formed through TCSPs can also conceal beneficial ownership or source of funds. Understand the shared mechanism: a bank transfer or professional introduction is not proof of lawful funds. Other sectors’ controls in this report do not automatically become identical statutory MSO procedures.'),
('按產品功能看風險：本地小額交通／零售支付與可海外提款、跨境匯款、人對人轉撥的電子錢包，脆弱性不同。報告第5.6節的整體中等評級不能把每種產品或每名客戶都定為同一級，也不能用低額交易自動排除非法博彩或分拆操作。','Assess product functionality: small domestic transport/retail payments differ from wallets supporting overseas cash withdrawal, cross-border remittance and peer-to-peer transfers. The sector’s medium rating in section 5.6 does not assign every product/customer the same risk, nor do small transactions automatically exclude illegal bookmaking or structuring.'),
('理解例子：虛假投資可以先叫受害人在真實平台買入虛擬資產，再轉到騙徒錢包；也可能只收法幣到傀儡銀行戶口，根本沒有虛擬資產交易。不能只看「加密貨幣投資」名稱或網頁顯示的收益，須理解實際資金流。這是第5.7.5段的2022年案例機制，不是所有虛擬資產活動都屬詐騙。','Illustration: a fake investment may first send a victim to a genuine platform to buy VAs and then transfer them to a fraudster’s wallet; alternatively, it may collect fiat money into stooge bank accounts without any VA transaction. Understand the actual funds flow rather than relying on the crypto-investment label or displayed returns. This is the 2022 paragraph 5.7.5 typology, not a claim that all VA activity is fraud.'),
('版本分開：第25份在2022年把虛擬資產發牌及DPMS註冊寫為擬議制度；第04份所存2026年綜合條例已載第5B／5C部，Part 2的制度參考以第04份為據。第25份行業數量、風險評級、監管改革與下一步措施均保留2022年時點，不用來判定今天的名單或法律狀態。','Separate editions: document 25 in 2022 describes VA licensing and DPMS registration as proposed regimes; the stored 2026 consolidated document 04 contains Parts 5B/5C, which support the Part 2 reference notes. Sector counts, risk ratings, regulatory reforms and next steps in document 25 retain their 2022 date and do not establish today’s lists or legal position.'),
],[ref('25','第5.2.13–5.2.17、5.2.21、5.3.25–5.3.38、5.6.2、5.6.7–5.6.15、5.7.5、5.7.22、6.4.3、6.6.6–6.6.13段','¶5.2.13–5.2.17, 5.2.21, 5.3.25–5.3.38, 5.6.2, 5.6.7–5.6.15, 5.7.5, 5.7.22, 6.4.3, 6.6.6–6.6.13','Mule account networks'),ref('04','第5B、5C部','Parts 5B, 5C','Regulation of Dealings in Precious Metals and Stones')]),
'第25份其他行業未完成重評，遙距身分與傀儡帳戶、支付功能及2022年提案易被誤讀。','讀完英文全報告後補共同風險機制、例子與跨版本提示；其餘行業統計及行政沿革保留參考。')

def pair(v):return 'p('+repr(v['tc'])+', '+repr(v['en'])+')'
for n,v in parts.items():
    lines=['"""Source-authored bilingual manuscript; independently revised 2026-10-19. No bank input."""','from model import p, ref, block, section','',f"PART = dict(title={pair(v['title'])},",f"intro={pair(v['intro'])}, sections=["]
    for s in v['sections']:
        lines.append('section('+repr(s['id'])+', '+repr(s['title']['tc'])+', '+repr(s['title']['en'])+', [')
        for b in s['blocks']:
            lines.append('    block('+repr(b['title']['tc'])+', '+repr(b['title']['en'])+', [')
            for x in b['points']:lines.append('        ('+repr(x['tc'])+', '+repr(x['en'])+'),')
            lines.append('    ], [')
            for r in b['refs']:lines.append('        ref('+', '.join(repr(x) for x in [r['doc'],r['locator']['tc'],r['locator']['en'],r['anchor']])+'),')
            lines.append('    ], kind='+repr(b['kind'])+'),')
        lines.append(']),')
    lines.append('])\n')
    (HERE.parent/f'part{n}.py').write_text('\n'.join(lines),encoding='utf-8')
(HERE/'findings.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rows=list(csv.DictReader((HERE/'source-inventory.tsv').open(encoding='utf-8'),delimiter='\t'))
for n,topic,docs,loc,sid in [
    (2,'TCSP監管對象、豁除及與MSO期限責任差異','04','Part 5A; Sch.1','other-sector-regimes'),
    (2,'虛擬資產與服務定義、牌照及負責人員AND條件','04','Part 5B; Sch.3B','other-sector-regimes'),
    (2,'DPMS A/B分類、門檻與非香港交易商條件','04','Part 5C; Sch.3H–3J','other-sector-regimes'),
    (3,'其他行業附表用途、申報資料及過渡時點','04','Sch.3A–3K','sector-specific'),
    (1,'跨行業傀儡帳戶、第三者資金流、支付功能與2022年提案','25,04','25 Ch.5–6;04 Parts 5B/5C','risk-assessment'),
]:
    rows=[r for r in rows if r['topic']!=topic]
    row={k:'' for k in rows[0]};row.update(part=str(n),topic=topic,priority='中',learning='理解界線及參考；非官方權重',original=docs,locator=loc,note_section=sid);rows.append(row)
with (HERE/'source-inventory.tsv').open('w',encoding='utf-8',newline='') as out:
    w=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print('Added 5 source-reviewed blocks and findings F30-F34.')
