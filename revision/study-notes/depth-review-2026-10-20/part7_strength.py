"""Complete independent source-modality corrections without changing legal duties."""
from pathlib import Path
exec(compile((Path(__file__).with_name('edit_guideline.py')).read_text(encoding='utf-8').split('\ndef ml(s):')[0],__file__,'exec'))
def internal(s):
    b=s['blocks'][0]['points']
    b[0]['en']=b[0]['en'].replace('Staff must know','The MSO should ensure staff know').replace('Managers without reporting/compliance responsibility must not filter them out','Under no circumstances should managers without reporting/compliance responsibility filter them out')
    b[1]['tc']=b[1]['tc'].replace('報告須有客戶詳情及引起懷疑的資料；MLRO應確認收妥並提醒避免通風報訊','內部報告應包括充分客戶詳情及引起懷疑的資料；MLRO必須確認收妥並提醒避免通風報訊（該句英文為should）')
    b[1]['en']=b[1]['en'].replace('Include customer details and grounds; the MLRO acknowledges receipt and reminds staff about tipping off.','Internal reports should include full customer details and grounds; the MLRO should acknowledge receipt and remind staff about tipping off (the Chinese uses 必須).')
    b[3]['tc']=b[3]['tc'].replace('特殊緊急情況可考慮先電話通知','特殊緊急情況應考慮先電話通知');b[3]['en']=b[3]['en'].replace('consider initial telephone notification in exceptional urgent cases','initial telephone notification should be considered in exceptional urgent cases')
def after(s):
    b=s['blocks'][0]['points']
    b[1]['tc']=b[1]['tc'].replace('提交STR時即須適當覆核','提交STR後應立即適當覆核');b[1]['en']=b[1]['en'].replace('Review the relationship and apply appropriate mitigation upon filing','The MSO should promptly review the relationship and apply appropriate mitigation upon filing')
    b[2]['tc']=b[2]['tc'].replace('可在初次STR說明','建議在初次STR說明');b[2]['en']=b[2]['en'].replace('Indicate intended termination in the initial STR where appropriate.','It is recommended to indicate intended termination in the initial STR.')
def records(s):
    b=s['blocks'][0]['points']
    b[1]['tc']=b[1]['tc'].replace('文件與資料須足以','文件與資料應足以');b[1]['en']=b[1]['en'].replace('must allow reconstruction','should allow reconstruction')
    b[2]=p('必須保存全部向MLRO作出的內部報告紀錄，亦須保留向JFIU提交的全部報告。內報紀錄應包括日期、經手職員、評估結果、有否報JFIU及文件定位；STR登記應包括日期、報告人及文件定位。兩份登記可合併。','All internal reports made to the MLRO and all reports to the JFIU must be retained. Internal records should show dates, handlers, assessment, whether an STR followed and document locators; the STR register should show date, reporter and document locators. The registers may be combined.')
    b[3]['tc']=b[3]['tc'].replace('須完整清晰','應完整清晰');b[3]['en']=b[3]['en'].replace('Preserve a clear, complete trail','The MSO should preserve a clear, complete trail')
def retention(s):
    b=s['blocks'][0]
    b['points'][4]['tc']=b['points'][4]['tc'].replace('中介服務終止時亦須取回','中介服務終止時亦應確保取回')
    b['points'][4]['en']=b['points'][4]['en'].replace('Obtain CDD data immediately, ensure documents are supplied as soon as reasonably practicable on request, and obtain records when intermediary services end.','CDD information must be obtained immediately and requested documents supplied as soon as reasonably practicable. The MSO should ensure records are obtained when intermediary services end.')
    b['refs'].append(ref('04','附表2第18(4)(a)–(b)條','Schedule 2 s.18(4)(a)–(b)','immediately after the intermediary has carried out'))
def audit(s):
    for b in s['blocks']:
        for a in b['points']:
            a['tc']=a['tc'].replace('須有紀錄','應有紀錄')

write_sections(7,{'internal-report':internal,'after-report':after,'evidence-records':records,'retention':retention,'independent-audit':audit})
