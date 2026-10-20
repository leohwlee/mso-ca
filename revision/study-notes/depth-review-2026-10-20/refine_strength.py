"""Preserve source modality and the complete compliance-officer functions."""
from pathlib import Path
exec(compile((Path(__file__).with_name('edit_guideline.py')).read_text(encoding='utf-8').split('\ndef ml(s):')[0],__file__,'exec'))

def controls(s):
    a=s['blocks'][0]['points'][0];a['tc']=a['tc'].replace('制度須由','制度應由');a['en']=a['en'].replace('Senior management approves them; implementation is monitored and improved when necessary.','The MSO should have senior-management-approved systems, monitor implementation and enhance them where necessary.')
    a=s['blocks'][0]['points'][1];a['en']=a['en'].replace('Take all reasonable measures','The MSO must take all reasonable measures')
def roles(s):
    a=s['blocks'][0]['points'][0];a['tc']=a['tc'].replace('高級管理層須了解','高級管理層應了解');a['en']=a['en'].replace('Senior management understands and manages risk and implements systems. It appoints','Senior management should understand and manage risk and implement systems. It should appoint')
    s['blocks'][0]['points'][1]=p('CO是監督所有預防及偵察洗錢／恐怖分子資金籌集活動的中心點，並支援及指導高級管理層。四項主要職能：（a）制定及／或持續覆核制度，香港成立MSO包括任何集團制度，確保最新、符合法定／監管要求及有效管理風險；（b）全面監察成效，有需要時加強管控／程序；（c）向高管傳達主要打擊洗錢問題，包括適用時的重大合規不足；（d）確保培訓足夠、適當及有效。','The CO is the focal point overseeing all ML/TF prevention/detection activities and supporting/guiding senior management. The CO should (a) develop and/or continuously review systems, including any group-wide systems for an HK-incorporated MSO, keeping them current, compliant and effective against risk; (b) oversee effectiveness and implement enhanced controls/procedures where necessary; (c) communicate key AML/CFT issues, including significant compliance deficiencies where appropriate; and (d) ensure adequate, appropriate and effective training.')
    a=s['blocks'][0]['points'][2];a['tc']=a['tc'].replace('須積極參與','應積極參與');a['en']=a['en'].replace('with an active identification/reporting role.','and should play an active identification/reporting role.')
    a=s['blocks'][-1]['points'][0];a['tc']=a['tc'].replace('管理資料須及時','管理資料應及時');a['en']=a['en'].replace('management information goes to','management information should go to')
def training(s):
    b=s['blocks'][0]['points']
    b[0]['tc']=b[0]['tc'].replace('聘用員工須有','聘用員工應有');b[0]['en']=b[0]['en'].replace('Use appropriate recruitment screening','MSOs should use appropriate recruitment screening')
    b[1]['tc']=b[1]['tc'].replace('並須能','並應能').replace('至少保存3年的紀錄須顯示','應至少保存3年紀錄，顯示');b[1]['en']=b[1]['en'].replace('Demonstrate to the CCE','MSOs should demonstrate to the CCE').replace('Keep records of who','They should keep records of who')
    b[2]['tc']=b[2]['tc'].replace('成效檢查三方面：','應監察培訓成效，可採用以下三類方法：');b[2]['en']=b[2]['en'].replace('Check effectiveness in three ways:','MSOs should monitor training effectiveness. This may be achieved by:')

write_sections(5,{'control-framework':controls,'roles':roles})
write_sections(7,{'training':training})
f=HERE/'part6.py';f.write_text(f.read_text(encoding='utf-8').replace("'Advance payment for goods'","'the use of an advance payment for a shipment'"),encoding='utf-8',newline='\n')
