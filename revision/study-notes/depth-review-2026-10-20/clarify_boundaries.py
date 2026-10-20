"""Source-backed boundary clarifications and owner decision of 20 October."""
from pathlib import Path
exec(compile((Path(__file__).with_name('edit_guideline.py')).read_text(encoding='utf-8').split('\ndef ml(s):')[0],__file__,'exec'))

def identity(s):
    s['blocks'][0]['points'][0]=p('附錄A第1段先說，身在香港的個人以香港身分證或旅行證件核實；再特別說香港居民「應經常」以香港身分證或簽證身分書識別／核實，英文為should always。依既定裁決，學習兩語措辭，實務以香港身分證／簽證身分書處理香港居民；這項居民規則不只限於親身在港者。非居民親身在香港時用有效旅行證件。','Appendix A paragraph 1 first addresses individuals present in Hong Kong, then specifically says Hong Kong residents should always be identified/verified using an HK identity card or document of identity. The Chinese says 應經常 (usually). Retain the language difference under the settled decision and use HKID/document of identity for Hong Kong residents in practice; the resident rule is not confined to physical presence in Hong Kong. A non-resident present in Hong Kong uses a valid travel document.')
    s['blocks'][0]['points'].insert(1,p('非居民沒有親身在香港時，應使用有效護照／其他旅行證件、有照片的國民身分證，或由主管國家／政府機構簽發的有效附照片國民駕駛執照。國際駕駛許可證／執照不獲接受；不應把這個境外非居民例子套用到所有客戶。','For non-residents not physically present in Hong Kong, use a valid passport/other travel document, photo national ID, or valid photo national driving licence issued by a competent national/government agency. International driving permits/licences are unacceptable; this remote non-resident list does not apply indiscriminately to every customer.'))
    s['blocks'][1]['points'][2]=p('接受核證副本不會轉移CDD責任。對來自高風險地區或任何地區不受規管實體的核證副本須特別審慎；不能確定真確性或懷疑文件並非關乎該客戶時，應採取額外風險緩減措施。','Certified copies do not transfer CDD responsibility. Exercise particular care with copies from higher-risk countries or unregulated entities in any jurisdiction. If authenticity is uncertain or the document may not relate to the customer, additional risk-mitigation measures should be taken.')

def wire(s):
    point=s['blocks'][1]['points'][1]
    point['tc']=point['tc'].replace('取不到時，考慮限制／終止與該機構的關係，或採合理緩減措施。','取不到時，中介機構「應考慮」、收款機構「須考慮」限制／終止與該機構的關係，或採合理緩減措施。')
    point['en']=point['en'].replace('if unavailable, consider restricting/ending that institutional relationship or reasonable mitigation.','if unavailable, the intermediary should consider, and the beneficiary institution must consider, restricting/ending that institutional relationship or reasonable mitigation.')

def screening(s):
    s['blocks'].append(block('2018年制裁通函：兩語強度差異及共同要求','2018 sanctions circular: language difference and common requirements',[
        ('第26份第2頁的中文寫，列入聯合國安理會制裁決議／名單「已足以構成知悉或懷疑的理由」，法定責任（包括呈報）及罪行條文隨即適用；英文寫may constitute grounds（可能構成理由）。依擁有人2026年10月20日決定，保留兩語原文的強度差異，不擅自改成相同措辭，也不把「可能」理解為可以忽略名單。','Page 2 of document 26 says inclusion in a UNSC sanctions resolution/list “may constitute grounds for knowledge or suspicion”, triggering statutory obligations (including reporting) and offence provisions. The Chinese says inclusion is already sufficient grounds and those provisions immediately apply. Under the owner’s 20 October 2026 decision, retain this difference rather than silently harmonising the wording; “may” is not permission to disregard a list.'),
        ('兩語共同要求：聯合國公布後，在實際可行情況下盡快篩查所列國家、個人、實體及活動，不論香港是否已實施相應制裁；保持CDD、持續監察及法定知悉／懷疑報告責任。名單資料庫由內部或外部供應，MSO均須負責及時更新。單純同名須先查明是否真正命中，見本節上文。','Both versions require screening listed countries, people, entities and activities as soon as practicable after UN promulgation, regardless of Hong Kong implementation, alongside CDD, ongoing monitoring and statutory knowledge/suspicion reporting duties. The MSO remains responsible for timely database updates whether maintained internally or by a provider. Investigate a mere name match to establish a genuine hit as explained above.'),
    ],[ref('26','第2頁，(d)後段落及第2節末段（續第3頁）','p.2, paragraph after (d), and end of section 2 (continuing on p.3)','may constitute grounds for knowledge or suspicion')]))

write_sections(6,{'identity-evidence':identity,'wire-receiving':wire,'screening':screening})
