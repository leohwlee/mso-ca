"""Bank-concept prompts rechecked in 03, 21, 24 and 25; no bank prose input."""
from pathlib import Path
exec(compile((Path(__file__).with_name('edit_guideline.py')).read_text(encoding='utf-8').split('\ndef ml(s):')[0],__file__,'exec'))
from model import g
def reports(s):
    s['blocks'].append(block('真誠評估後決定不報告的條件','Conditions when deciding in good faith not to report',[
        ('第7.20段說，MLRO真誠行事，考慮全部可得資料後結論是沒有懷疑，則一般不大可能因不報STR而負刑責；必須妥存考慮及行動紀錄，證明合理行事。這不是只要寫「不懷疑」便絕對免責，也不是可以忽略未查明的警號。','Paragraph 7.20 says criminal liability for non-reporting is unlikely where the MLRO acts in good faith and concludes there is no suspicion after considering all available information. Proper records of deliberations/actions are vital to demonstrate reasonableness. Merely recording “no suspicion” is not absolute immunity or permission to disregard unresolved indicators.'),
    ],[g('7.20','it is unlikely that there will be any criminal liability')]))
def after(s):
    s['blocks'][0]['points'].insert(0,p('JFIU會確認收到STR。若無需立即行動（例如就戶口發限制令），一般會給予同意運作戶口；否則MSO應採取適當行動，並按需要徵詢法律意見。這是第7.24段所述處理方式，不是每份STR都必然獲同意或自動解除限制。','The JFIU acknowledges STR receipt. If imminent action, such as an account restraint order, is unnecessary, consent to operate the account will usually be given; otherwise the MSO should act appropriately and seek legal advice where necessary. This describes paragraph 7.24, not guaranteed consent or automatic removal of restrictions for every STR.'))
def records(s):
    s['blocks'][0]['points'].append(p('第8.3(d)段的「業務通訊」至少包括與CDD措施或戶口運作重大改變有關的重要通信；註66說不要求保存每一項通信，例如每封來往電郵，而是保存足以證明符合AMLO的通信。','Business correspondence under paragraph 8.3(d) includes, at minimum, correspondence material to CDD measures or significant account-operation changes. Note 66 does not expect every communication, such as each email, to be retained; keep enough to demonstrate AMLO compliance.'))
    s['blocks'][0]['refs'].append(g('8.3(d)及註66','not expected to keep each and every correspondence'))
def law(s):
    a=s['blocks'][0]['points'][1]
    a['tc']=a['tc'].replace('並非必然涵蓋關係內所有資產。','MSO必須確保能扣留命令涉及的財產；命令並非必然涵蓋關係內所有資產，應考慮香港法律下仍可動用哪些資產（如有）。')
    a['en']=a['en'].replace('it does not necessarily cover every asset in the relationship.','the MSO must ensure it can withhold the property covered. The order need not cover every relationship asset; consider what, if any, assets may still be used under Hong Kong law.')
def duty(s):
    s['blocks'][0]['points'][0]['tc']+=' 財產不限現金，也包括貨品、土地及權利；完整定義見Part 1「洗錢」。'
    s['blocks'][0]['points'][0]['en']+=' Property extends beyond cash to goods, land and rights; see Part 1 Money laundering for the full definition.'
def policy(s):
    a=s['blocks'][0]['points'][2]
    a['tc']=a['tc'].replace('匯款地區','分別列明匯入／匯出的目標司法管轄區').replace('以及制裁與政治人物篩查。','以及制裁與政治人物篩查。渠道說明須包括面對面及非面對面交易所佔百分比。')
    a['en']=a['en'].replace('remittance jurisdictions','separate inward/outward target jurisdictions').replace('and sanctions/PEP screening.','and sanctions/PEP screening. Describe channels with the percentages of face-to-face and non-face-to-face transactions.')
def trade(s):
    a=s['blocks'][2]['points'][0];a['tc']=a['tc'].replace('進口貿易價值與相應對外銀行轉帳不符','進口貨值與相應對外銀行轉帳不符，或出口貨值與境外來款不符');a['en']=a['en'].replace('imported trade values inconsistent with the corresponding foreign bank transfers','imported trade values inconsistent with corresponding outward bank transfers, or exported trade values inconsistent with incoming foreign transfers')
def history(s):
    s['blocks'].append(block('2022年參考：更新監管評級及非實地監察','2022 reference: updating supervisory ratings and off-site monitoring',[
        ('第5.4.16段列評級更新資料的例子：定期風險狀況評估、業務計劃及AML/CFT政策、定期業務報表、實地面談意見。第5.4.20段說非實地監察也用於非高風險MSO的常規查核，或為其後實地視察先收資料／初評；選定者須到海關辦事處面談及在指定期內交文件。「非實地」不等於不用面談，「非高風險」不等於免受監察。這是2022報告的程序描述，申報頻率按Part 7所列較後文件理解。','Paragraph 5.4.16 gives rating-update inputs: periodic risk profiling, business plans and AML/CFT policies, regular business returns, and on-site interview feedback. Paragraph 5.4.20 describes off-site monitoring for routine checks of non-high-risk MSOs or advance information/preliminary assessment before an on-site inspection; selected MSOs attend interviews at Customs offices and submit documents within a specified period. Off-site does not mean no interview, nor does non-high risk mean no supervision. This describes the 2022 report; later reporting-frequency requirements appear in Part 7.'),
    ],[ref('25','2022年版，第5.4.16、5.4.20段','2022 edition, ¶5.4.16, 5.4.20','off-site monitoring is strategically deployed')],kind='reference'))
write_sections(7,{'internal-report':reports,'after-report':after,'evidence-records':records,'law-enforcement':law,'reporting-duty':duty})
write_sections(5,{'policy':policy})
write_sections(6,{'trade-based-laundering':trade})
write_sections(1,{'risk-assessment':history})
