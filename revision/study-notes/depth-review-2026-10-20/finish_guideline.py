"""Source-based follow-up edits; not imported by the page builder."""
from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(HERE))
# Reuse only the editing helpers, without rerunning the earlier amendments.
exec(compile((Path(__file__).with_name('edit_guideline.py')).read_text(encoding='utf-8').split('\ndef ml(s):')[0],__file__,'exec'))
from model import g

def trade(s):
    s['blocks'][1]['points'][0]=p('結構：不合理複雜架構或空殼、在打擊洗錢合規薄弱地區設立／設辦事處；地址似供大量公司登記（例如密集住宅、郵箱、商業／工業大廈，尤其沒有單位號碼），或與業務不符且無合理解釋；人手與貿易量不稱、名義擁有人不了解業務、網站空泛／欠缺、名稱模仿知名企業、無法解釋的休眠期，或有負面情報。這裏「集中註冊地址」不是「短期大量註冊」。','Structure: illogical complexity or shells; registration/offices in a jurisdiction with weak AML/CFT compliance; an apparent mass-registration address (dense housing, a post box or commercial/industrial building, especially without a unit number), or an address inappropriate for the business without explanation; staffing inconsistent with trade volume; uninformed nominees, generic/absent websites, imitation names, unexplained dormancy or adverse information. A mass-registration address is not a claim about numerous recent registrations.')
    s['blocks'][2]['points'][0]=p('單據／貨物：合約、發票及付款的名稱不同；數量、品質或市場價格不符；描述過於籠統；單據偽造、遺失、反覆修改或被拒後重交；進口貿易價值與相應對外銀行轉帳不符。另兩項須分清：貨物在暫時進口／進料加工制度下進口，之後以偽造單據出口；以及沒有明顯經濟理由而經多個司法管轄區運送。','Documents/goods: inconsistent names across contracts, invoices and payments; quantity, quality or market-value discrepancies; vague descriptions; false, missing, repeatedly modified or resubmitted documents; imported trade values inconsistent with the corresponding foreign bank transfers. Distinguish goods imported under temporary-importation/inward-processing arrangements and later exported using falsified documents, from goods routed through jurisdictions without apparent economic justification.')

def indicators(s):
    s['blocks']=[
        block('使用方法：記住分類，理解具體警號','Use: remember the groups and understand the indicators',[
            ('第7.10段分六組列出43項非盡列警號。學習時要能認識具體模式及其可疑之處，毋須逐字背例句；單一警號不是定罪或自動必報STR的充分條件。按第7.9段跟進背景、目的及資金來源，取得支持資料；形成知悉／懷疑時，按Part 7的法定及內部程序盡快報告。','Paragraph 7.10 gives 43 non-exhaustive indicators in six groups. Recognise the specific patterns and why they matter; verbatim memorisation of examples is unnecessary. A single indicator is not proof or an automatic STR trigger. Follow up context, purpose and SOF with supporting information under paragraph 7.9; report knowledge/suspicion promptly through the statutory/internal procedures in Part 7.'),
        ],[g('7.9–7.11','list of non-exhaustive red flag indicators')]),
        block('一、一般交易：九項','1. General transactions: nine indicators',[
            ('（1）模式與客戶正常活動不符；（2）金額／次數與已知背景或交易目的不符；（3）頻密交易刻意分拆至CDD門檻以下以免留下紀錄；（4）化整為零／分拆（Structuring／Smurfing）：本可用一宗或幾宗大額，卻作多宗小額。相連操作仍須合併考慮門檻。','(1) A pattern inconsistent with normal activity; (2) size/frequency inconsistent with known background or purpose; (3) frequent deliberate splitting below CDD thresholds to avoid records; (4) structuring/smurfing: many smaller transactions where one or a few larger ones could be used. Apparently linked operations still require threshold aggregation.'),
            ('（5）折返交易（U-turn）：境外某人／公司的來款，再匯至同一境外司法管轄區另一人／公司，或原匯款人在另一司法管轄區的戶口；（6）不必要地經多間金融機構轉款。','(5) A U-turn: funds from a foreign person/company are remitted to another person/company in that same foreign jurisdiction or to the sender’s account in another jurisdiction; (6) unnecessary routing through multiple financial institutions.'),
            ('（7）交易頻率／金額突然增加，無合理解釋，尤其涉及新收款人／目的地；（8）多名匯款人匯入一個戶口；（9）客戶與收款人無明顯關係，或匯款地點與客戶沒有個人、地理、家庭或商業聯繫，亦無合理解釋。','(7) Unexplained sudden increases in frequency/value, particularly new destinations/people; (8) many senders to one account; (9) no apparent customer-recipient relationship, or no personal, geographic, family or business ties to the destination, without a reasonable explanation.'),
        ],[g('7.10(a)','“Structuring” or “Smurfing”')]),
        block('二、現金：七項','2. Cash: seven indicators',[
            ('（1）與個人／業務背景不符的頻密大額現金交易；（2）大額或頻密匯款似與客戶業務無關；（3）大量小面額鈔票換另一貨幣大面額鈔票。','(1) Frequent large cash transactions unjustified by the individual/business background; (2) large/frequent remittances apparently unrelated to the business; (3) unusually large small-note exchanges for high-denomination notes in another currency.'),
            ('（4）短期內多宗低於CDD門檻的交易合計龐大；（5）同時在多間分行進行大額現金交易；（6）假鈔／偽造金融票據；（7）定期向／從高風險地區作大額付款，而沒有明確真正交易基礎。','(4) Numerous below-CDD-threshold transactions over a short period with a large aggregate; (5) simultaneous large cash transactions at multiple branches; (6) counterfeit notes/forged financial instruments; (7) regular large payments to/from higher-risk jurisdictions without clear genuine underlying transactions.'),
        ],[g('7.10(b)','Cash transactions')]),
        block('三、貿易洗錢：十一項','3. Trade-based laundering: eleven indicators',[
            ('（1）高風險起點／目的地；（2）高風險貨物，例如高價低體積電子產品、軍民兩用貨物、周轉快或難估公允價值的貨物；（3）貿易單據的貨物描述不一致；（4）報稱貨價與市場價值不符。','(1) Higher-risk origin/destination; (2) higher-risk goods, e.g. high-value low-volume electronics, dual-use goods, rapid-turnover goods or goods difficult to value fairly; (3) inconsistent goods descriptions across trade documents; (4) stated prices inconsistent with market value.'),
            ('（5）交易規模與業務不符；（6）付款方式增加風險，例如向高風險地區的新供應商預付款；（7）無關第三方付款；（8）信用證反覆延長／修改。','(5) Size inconsistent with the business; (6) a payment method increasing risk, e.g. advance payment to a new supplier in a higher-risk jurisdiction; (7) unrelated third-party payments; (8) repeatedly extended/amended letters of credit.'),
            ('（9）交易方似為幌子／空殼公司；（10）付運地點無合理理由經其他地區轉運；（11）付運貨物不合經濟常理。Part 6「貿易洗錢」另載第24份的四類指標，兩套分類不要混為同一清單。','(9) Apparent front/shell-company trading parties; (10) unjustified trans-shipment through other locations; (11) shipments that make no economic sense. The TBML section separately explains document 24’s four indicator groups; these are distinct lists.'),
        ],[g('7.10(c)及註62–63','Advance payment for goods')]),
        block('四、恐怖分子資金籌集：七項','4. Terrorist financing: seven indicators',[
            ('（1）活動與年齡、職業或收入不符；（2）客戶與已知恐怖分子／組織有關；（3）經常改地址或獲授權簽署人；（4）向衝突區慈善／非牟利組織，或在與恐怖活動有關地區營運的組織捐款。','(1) Activity inconsistent with age, occupation or income; (2) links to known terrorists/organisations; (3) frequent changes of address or authorised signatories; (4) donations to charities/NPOs in conflict zones or organisations operating in areas associated with terrorism.'),
            ('（5）用虛假資料／第三方掩飾付款人或收款人；（6）向／從避稅天堂或與犯罪活動／高風險業務有關地區反覆付款，金額未必大；（7）與正常業務不符、沒有明顯經濟理由而匯至／來自高風險地區。','(5) False information/third parties conceal payers or recipients; (6) repeated payments to/from tax havens or areas associated with crime/high-risk business, not necessarily large; (7) unexplained transfers to/from higher-risk jurisdictions inconsistent with normal business.'),
        ],[g('7.10(d)','Transactions related to terrorist financing')]),
        block('五、代理／對手：四項','5. Agents/counterparties: four indicators',[
            ('（1）拒絕提供識別資料；（2）相較同區其他代理，交易量過大或可疑；（3）一段時間內，原來相同的客戶資料逐漸改變拼寫、地址或其他局部身分資料；（4）同一客戶同日在多個代理地點匯款至同一或不同收款人。','(1) Refusal to provide identification; (2) excessive/suspicious volume compared with other agents in the locality; (3) initially identical customer details evolve through spelling, address or other partial identity changes; (4) the same customer sends to the same or different recipients at multiple agent locations on the same day.'),
        ],[g('7.10(e)','Agents/counterparties')]),
        block('六、客戶行為：五項','6. Customer behaviour: five indicators',[
            ('（1）由保持低調或在外等候的人陪同，或猶豫才提供資料；（2）催促交易，承諾之後才補文件；（3）不在乎手續費／匯率；（4）不同客戶合作分拆；（5）不能為交易提供合理解釋。','(1) Companions keep a low profile/wait outside, or the customer hesitates to provide details; (2) urgency to transact with promised later documents; (3) no interest in charges/exchange rates; (4) customers cooperate in splitting; (5) inability to justify the transaction.'),
        ],[g('7.10(f)','Customer behaviour')]),
    ]

write_sections(6,{'trade-based-laundering':trade,'suspicion-indicators':indicators})
path=HERE/'part1.py'
path.write_text(path.read_text(encoding='utf-8').replace('1.14–1.28','1.14–1.27'),encoding='utf-8',newline='\n')
path=HERE/'part6.py'
txt=path.read_text(encoding='utf-8')
for n,foot in [('4.9.5','35'),('4.9.6','36')]:
    txt=txt.replace('第'+n+'及註'+foot+'段','第'+n+'段及註'+foot).replace('¶'+n+'及註'+foot,'¶'+n+'; footnote '+foot)
path.write_text(txt,encoding='utf-8',newline='\n')
