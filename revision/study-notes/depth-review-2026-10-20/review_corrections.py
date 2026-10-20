"""Corrections after independent comparison against document 03 originals."""
from pathlib import Path
exec(compile((Path(__file__).with_name('edit_guideline.py')).read_text(encoding='utf-8').split('\ndef ml(s):')[0],__file__,'exec'))

def flags(s):
    b=s['blocks']
    b[0]['points'][0]['tc']=b[0]['points'][0]['tc'].replace('按第7.9段跟進背景、目的及資金來源，取得支持資料','依第7.10段末的要求作進一步調查，至少初步查詢資金來源及要求額外CDD佐證')
    b[0]['points'][0]['en']=b[0]['points'][0]['en'].replace('Follow up context, purpose and SOF with supporting information under paragraph 7.9','Under the end of paragraph 7.10, investigate further, at least making initial SOF enquiries and requesting additional CDD evidence')
    b[1]['title']=p('一、不合經濟常理的交易：九項','1. Transactions without economic sense: nine indicators')
    a=b[1]['points'][0]
    a['tc']=a['tc'].replace('（2）金額／次數與已知背景或交易目的不符','（2）與對客戶的認知／經驗或交易目的不符，例如經濟活動、來源地或人士與所收匯款不相稱')
    a['en']=a['en'].replace('(2) size/frequency inconsistent with known background or purpose','(2) incompatibility with customer knowledge/experience or purpose, e.g. a mismatch between economic activity, origin or person and remittances received')
    a=b[1]['points'][1];a['tc']=a['tc'].replace('多間金融機構轉款','多間金融機構或人士轉款');a['en']=a['en'].replace('multiple financial institutions','multiple financial institutions or people')
    a=b[1]['points'][2];a['tc']=a['tc'].replace('一個戶口','同一個人戶口').replace('或匯款地點與客戶沒有個人、地理、家庭或商業聯繫，亦無合理解釋','及／或私人匯款地與客戶無明顯家庭／商業聯繫，及／或匯出／收款地與客戶無關且不能充分解釋原因');a['en']=a['en'].replace('one account','one individual’s account').replace('or no personal, geographic, family or business ties to the destination, without a reasonable explanation','and/or personal remittances lack apparent family/business ties to the destination, and/or the customer has no connection with the sending/receiving jurisdiction and cannot sufficiently explain why')
    a=b[2]['points'][1];a['tc']=a['tc'].replace('短期內多宗低於CDD門檻的交易合計龐大','尤其短期內多宗交易各低於CDD門檻或金額不大，但合計龐大或超過門檻').replace('同時在多間分行進行大額現金交易','多名客戶一起同時在不同分行進行大額現金交易');a['en']=a['en'].replace('Numerous below-CDD-threshold transactions over a short period with a large aggregate','Numerous transactions, especially over a short period, each below the CDD threshold or not substantial but cumulatively substantial or over the threshold').replace('simultaneous large cash transactions at multiple branches','customers together making simultaneous large cash transactions at separate branches')
    a=b[3]['points'][0];a['tc']=a['tc'].replace('高價低體積電子產品、軍民兩用貨物、周轉快或難估公允價值的貨物','高價低體積貨物（如電子產品），以及周轉快且難估值的軍民兩用貨物').replace('貿易單據的貨物描述不一致','提單／發票的貨物描述與實際付運貨物有重大差異').replace('報稱貨價與市場價值不符','發票貨價與公平市場價值有重大差異');a['en']=a['en'].replace('high-value low-volume electronics, dual-use goods, rapid-turnover goods or goods difficult to value fairly','high-value low-volume goods (such as electronics) and dual-use goods with high turnover and valuation difficulties').replace('inconsistent goods descriptions across trade documents','significant discrepancies between bill-of-lading/invoice descriptions and actual goods shipped').replace('stated prices inconsistent with market value','significant discrepancies between invoice values and fair market value')
    b[4]['title']=p('四、其他類型交易：七項','4. Other types of transactions: seven indicators')
    b[4]['refs'][0]['anchor']='other types of transactions'
    a=b[4]['points'][0];a['tc']=a['tc'].replace('客戶與已知恐怖分子／組織有關','交易涉及據報與恐怖活動或指定恐怖分子有關的司法管轄區／實體');a['en']=a['en'].replace('links to known terrorists/organisations','transactions with jurisdictions/entities reported to be associated with terrorist activities or designated terrorists')
    b[5]['points'][0]=p('（1）不願提供客戶識別資料；（2）相較同區其他代理／對手，有大量大額或可疑交易；（3）同一客戶大量交易中，多次出現不同姓名拼寫、虛假地址，或識別資料部分改變、部分維持不變；（4）同一客戶同日向多個代理／對手地點傳送資金，聲稱給同一或不同收款人。','(1) Reluctance to provide customer identification information; (2) a high volume of large or suspicious transactions compared with local agents/counterparts; (3) a large volume for one customer with repeated different name spellings, false addresses or identification that changes in part while other parts remain the same; (4) funds sent by the same customer on the same day to several agent/counterpart locations for purportedly the same or different recipients.')
    b[5]['refs'][0]['anchor']='agents or counterparts of MSO'
    b[6]['refs'][0]['anchor']='customer’s behaviour'
    a=b[6]['points'][0];a['tc']=a['tc'].replace('不同客戶合作分拆','多名客戶似合作把一項交易拆成兩項或以上門檻以下交易，以規避申報要求');a['en']=a['en'].replace('customers cooperate in splitting','customers appear to cooperate in splitting one transaction into two or more below-threshold transactions to avoid reporting requirements')

def enhanced(s):
    b=next(b for b in s['blocks'] if b['title']['en']=='Recognise the complete groups: potentially higher risks')
    b['points'][0]['tc']=b['points'][0]['tc'].replace('特定組別跨地點／服務交易','特定組別在一個或多個地點或多項服務交易')
    b['points'][0]['en']=b['points'][0]['en'].replace('defined groups transacting across locations/services','defined groups transacting at one or more locations or across multiple services')
    b['points'][4]['tc']=b['points'][4]['tc'].replace('或向恐怖活動提供資金／支持，或有指定恐怖組織活動','向恐怖活動提供資金／支持，以及有指定恐怖組織活動（該項英文連詞為or）')

def wire(s):
    b=s['blocks'][1]
    b['points'][0]['tc']=b['points'][0]['tc'].replace('須至少保存所收資料5年','應至少保存所收資料5年')
    b['points'][0]['en']=b['points'][0]['en'].replace('keep received information for at least five years','received information should be kept for at least five years')
    b['points'][1]['en']=b['points'][1]['en'].replace('the beneficiary institution must consider','the beneficiary institution should consider (Chinese: 須考慮)')
    b['points'][2]['tc']=b['points'][2]['tc'].replace('須核實其身分','應核實其身分')
    b['points'][2]['en']=b['points'][2]['en'].replace('verifies a recipient not already verified','should verify a recipient not already verified')

write_sections(6,{'suspicion-indicators':flags,'enhanced':enhanced,'wire-receiving':wire})
