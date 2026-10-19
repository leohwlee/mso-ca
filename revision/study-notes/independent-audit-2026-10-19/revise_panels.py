"""One-time design revision; every original panel gets an explicit disposition."""
import copy,json,sys,pprint
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
import memory_panels as old
from model import p
panels=copy.deepcopy(old.PANELS)
assert sum(len(v) for ss in panels.values() for v in ss.values())==27
changes=[]
remove={
 'cash-routes':'路徑表省略影響適用的條件，與完整正文重複；保留正文及跨制度金額表。',
 'review-clocks':'把期限、決定生效和暫緩混成兩行；正文分開說明更清楚。',
 'governance-roles':'三個職責清單與緊接正文重複，並非同一維度比較。',
 'four-cdd-measures':'四項措施本身已是清楚清單，沒有必要再逐項重寫一張表。',
 'due-diligence-levels':'把風險程度、法定豁免和AND／OR條件混在同表，容易誤認互斥分類。',
 'report-consent-defence':'STR、同意、抗辯並非平行選項，正文對時間和條件的說明較完整。',
 'return-period-deadline':'資料期間及截止日只需兩句相連說明，表格沒有增加理解。',
}
for n,ss in panels.items():
 for sid,items in list(ss.items()):
  for v in items:
   changes.append(dict(part=n,section=sid,id=v['id'],action='remove' if v['id'] in remove else 'retain',reason=remove.get(v['id'],'同一維度對照有助辨識概念或適用規則；保留條件、來源及手機欄名。')))
  ss[sid]=[v for v in items if v['id'] not in remove]
def get(key):return next(v for ss in panels.values() for vv in ss.values() for v in vv if v['id']==key)
def revise(key,why):
 c=next(x for x in changes if x['id']==key);c.update(action='replace',reason=why)
def cells(*pairs):return [p(*x) for x in pairs]

v=get('three-stages');v['kind']='stages'
v['title']=p('三個常見階段：可重疊，不是固定步驟','Three common stages: overlapping, not a fixed sequence')
revise('three-stages','改用無箭頭的並列概念圖；保留名稱、作用及可重疊說明，避免誤導必須逐步發生。')
v=get('party-roles');v['rows'][1][1]=p('最終擁有／控制客戶，或交易為其進行的人；須按各類定義判斷。','Ultimate ownership/control or the person for whom a transaction occurs, under the applicable definition.')
v['rows'][1][2]=p('公司／合夥的持股及控制分支指自然人；代他人交易及信託角色不能一概排除法人。','Corporate/partnership ownership and control limbs concern individuals; acting-on-behalf and trust roles do not universally exclude legal persons.')
revise('party-roles','修正BO一概為individual的錯誤；以角色／識別對象／責任比較。')

v=get('money-boundaries')
v['headers']=cells(('對象及交易','Person / transaction'),('金額界線','Amount boundary'),('觸發甚麼','What it triggers'),('合併、條件及例外','Aggregation, conditions and exceptions'))
v['rows']=[
 cells(('MSO的非經常交易（一般非電傳）','MSO occasional transaction (general non-wire)'),('≥ HK$120,000\n等於亦包括','≥ HK$120,000\nAt least HK$120,000; includes equality.'),('執行前CDD','CDD before execution'),('沒有業務關係；單次或看來相連操作合併。建立關係、懷疑或資料疑問另有不限金額觸發。','No business relationship; aggregate apparently linked operations. Relationship, suspicion and information doubts separately trigger CDD regardless of amount.')),
 cells(('金融機構非經常電傳／VA轉移','FI occasional wire / VA transfer'),('≥ HK$8,000','≥ HK$8,000'),('執行前CDD','CDD before execution'),('相連操作合併；低於8,000元仍有電傳資料要求。持牌VASP非轉移交易另有8,000元規則，不套用所有MSO。','Aggregate linked operations; below HK$8,000 wire information duties remain. Licensed-VASP non-transfer transactions have a separate HK$8,000 rule, not a universal MSO rule.')),
 cells(('非電傳外匯款發款人','Non-wire outward-remittance originator'),('≥ HK$8,000','≥ HK$8,000'),('第13條核實及紀錄','Section 13 verification and records'),('指定識別文件及資料；不把所有一般交易CDD門檻改成8,000元。','Use specified identity documents and records; this does not lower the general CDD threshold for every transaction.')),
 cells(('跨境實體現金類物品','Cross-boundary physical CBNIs'),('> HK$120,000\n恰好不包括','> HK$120,000\nAggregate value above HK$120,000; equality excluded.'),('第629章申報／披露制度','Cap.629 declaration / disclosure regime'),('按旅客／貨物、管有、批次及豁除判斷；與CDD是兩套制度。','Apply traveller/cargo routes, possession, batches and exclusions; this is a separate regime from CDD.')),
 cells(('兌換顧客交付的款額','Amount tendered by exchange customer'),('> HK$100,000\n恰好不豁除','> HK$100,000\nMore than HK$100,000; equality not excluded.'),('不適用第34章','Cap.34 monetary exclusion'),('Exactly／恰好100,000元仍在金額範圍，其他豁除另論；不是AMLO的CDD豁免。','Exactly HK$100,000 remains within monetary scope, subject to other exclusions; this is not an AMLO CDD exemption.')),
]
revise('money-boundaries','把對象／交易、比較符號及金額、法律效果、合併及例外分欄；直接比較恰好等於門檻的不同結果。')

v=get('licence-clocks');v['headers']=cells(('事項／責任人','Action / responsible person'),('起算事件','Starting event'),('期限','Time requirement'),('條件及例外','Conditions and exceptions'))
oldrows=v['rows'];v['rows']=[
 [oldrows[0][0],p('擬加入持牌人','Proposed appointment / ownership'),p('事先書面批准','Written approval beforehand'),oldrows[0][2]],
 [oldrows[1][0],p('擬在該處所營業','Proposed operation there'),p('營業前獲批及登記','Approval and registration before operation'),oldrows[1][2]],
 [p('持牌人續牌','Licensee renewal'),p('現有牌照屆滿日（向前計）','Existing expiry date (count backwards)'),p('最少提前45日','At least 45 days before expiry'),oldrows[2][2]],
 [p('持牌人資料改變','Licensee particulars change'),p('改變當日','Date of change'),p('起計1個月內書面通知','Written notice within one month beginning on that date'),oldrows[3][2]],
 [p('持牌人全部／指定處所停業','Licensee ceases all / specified-premises business'),p('停止當日','Cessation date'),p('停止前通知；當日起7日內交還牌照','Notify beforehand; surrender within seven days beginning on cessation'),oldrows[4][2]],
]
revise('licence-clocks','分開事前批准和以事件起算的通知期限；明示責任人，不畫共用時間軸。')
v=get('assessment-clocks');v['headers']=cells(('事項／人士','Event / person'),('起算事件','Starting event'),('期限','Time requirement'),('條件及例外','Conditions and exceptions'))
starts=[('海關面見後','After Customs interview'),('收到提名邀請','Receipt of nomination invitation'),('收到評核邀請','Receipt of assessment invitation'),('通知海關合夥人／董事變更後','After notifying Customs of partner/director change'),('結果通知後','After result notification'),('評核後','After assessment'),('結果通知發出後','After result-notification issue'),('收到覆核要求後','After receipt of rechecking request')]
durations=[('30日內應考','Attend within 30 days'),('7日內提名','Nominate within seven days'),('30日內應考','Attend within 30 days'),('30日內安排評核','Arrange assessment within 30 days'),('30日後才重考','Retake after 30 days'),('14日內電郵通知','Email within 14 days'),('7日內書面要求','Written request within seven days'),('14日內書面回覆','Written reply within 14 days')]
v['rows']=[[r[0],p(*a),p(*b),r[2]] for r,a,b in zip(v['rows'],starts,durations)]
revise('assessment-clocks','每行獨立列起算事件及期限；把收到、發出、面見和30日後分清。')
v=get('retention-clocks');v['headers']=cells(('紀錄（MSO負責）','Record (MSO responsible)'),('起算事件','Starting event'),('最短保存期','Minimum retention'),('條件及例外','Conditions and exceptions'))
starts=[('關係結束時','When it ends'),('交易完成時','Transaction completion'),('每宗交易完成時','Completion of each transaction'),('培訓紀錄形成後','After the training record is made')]
durations=[('關係持續期間，另加至少5年','Throughout the relationship plus at least five years'),('至少5年','At least five years'),('至少5年','At least five years'),('至少3年','At least three years')]
v['rows']=[[r[0],p(*a),p(*b),r[2]] for r,a,b in zip(v['rows'],starts,durations)]
v['rows'][3][1]=p('指引沒有另訂起算公式；按培訓日期保留紀錄','No separate statutory starting formula is stated; keep dated training records')
revise('retention-clocks','分開紀錄、起算事件與最短期間；培訓指引未明訂起算公式，不虛構法律時間點。')
v=get('transfer-information');oldrows=v['rows'];v['title']=p('跨境電傳：8,000元上下的資料及核實','Cross-border wires: information and verification around HK$8,000')
v['headers']=cells(('金額','Amount'),('兩者均須隨附','Required at both levels'),('額外資料／核實','Extra information / verification'),('條件','Conditions'))
v['rows']=[
 cells(('≥ HK$8,000','≥ HK$8,000'),('雙方姓名＋各自戶口號碼；無戶口時用可追蹤編號。','Both names plus respective account numbers; traceable references only where no account exists.'),('另附發款人地址 OR 客戶識別碼 OR 證件號碼 OR（自然人出生日期 AND 地點）；發款人資料須準確。','Add originator address OR customer ID OR document number OR (individual birth date AND place); originator data must be accurate.'),('須完成適用CDD。批量檔案例外及本地電傳簡化另見下文。','Complete applicable CDD. Batch-file and domestic-wire exceptions are explained below.')),
 cells(('< HK$8,000','< HK$8,000'),('雙方姓名＋各自戶口號碼；無戶口時用可追蹤編號。','Both names plus respective account numbers; traceable references only where no account exists.'),('非經常交易發款人一般毋須核實；不是毋須資料。','An occasional originator generally need not be verified; information is still required.'),('相連總額達門檻、懷疑或原資料疑問仍須CDD；受益機構對達門檻受款人另有核實責任。','Linked totals reaching the threshold, suspicion or doubts still trigger CDD; beneficiaries separately verify threshold recipients where needed.')),
]
v['note']=p('本表只比較跨境電傳資料。非電傳外匯款的第13條文件及紀錄要求、本地轉帳3個業務日及立即提供資料條件，均在正文分開說明。','This table compares cross-border wire information only. The text separately explains section 13 non-wire documents/records and domestic-wire three-business-day/immediate information provision.')
revise('transfer-information','原表混合交易種類、例外和缺漏處理；改為相同維度比較門檻上下，OR／AND直接寫在資料旁。')

(HERE.parent/'memory_panels.py').write_text('"""Source-bound comparisons. Dispositions: independent-audit-2026-10-19/visual-review.json."""\nPANELS = '+pprint.pformat(panels,width=140,sort_dicts=False)+'\n\nEMPHASIS = '+repr(old.EMPHASIS)+'\n',encoding='utf-8')
(HERE/'visual-review.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Reviewed',len(changes),'original visuals;',sum(x['action']=='remove' for x in changes),'removed.')
