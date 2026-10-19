"""Complete the banking/securities omitted-content pass from document 25."""
from pathlib import Path
import ast,copy,json,sys
HERE=Path(__file__).resolve().parent;NOTES=HERE.parent
sys.path.insert(0,str(NOTES))
import build
from model import block,ref
parts=copy.deepcopy(build.PARTS)
findings=json.loads((HERE/'findings.json').read_text(encoding='utf-8'))
assert len(findings)==12
def add(code,n,key,tc,en,points,refs,impact):
    next(s for s in parts[n]['sections'] if s['id']==key)['blocks'].append(block(tc,en,points,refs))
    findings.append(dict(id=code,part=n,section=key,title=tc,impact=impact,priority='P2',action='added',refs=refs,status='closed'))
add('O13',5,'risk-based','理解：風險管理與迴避風險','Understand: risk management and de-risking',[
 ('2022年報告專題5.6指出，迴避風險（de-risking）與風險為本的核心理念相悖；銀行的打擊洗錢制度也應顧及正當企業及居民取得必要服務。學習上須分清：評估個別風險並採相稱措施，與單憑所屬類別便籠統排除客戶。這不代表MSO必須接受所有客戶；無法完成CDD或法律禁止交易等情況，仍須按適用規則拒絕／終止及考慮STR（見Part 6核實時間與審查失敗）。','Box 5.6 of the 2022 report explains that de-risking conflicts with the core RBA philosophy and that banking AML controls should preserve legitimate businesses’ and residents’ access to essential services. Distinguish individual risk assessment and proportionate mitigation from blanket exclusion based on category alone. This does not require an MSO to accept every customer: inability to complete CDD or legal transaction prohibitions still require the applicable refusal/termination and STR consideration (see Part 6 on timing and failed CDD).'),
],[ref('25','2022年版，第5.2節專題5.6（中文第61頁）','2022 edition, section 5.2 Box 5.6 (English p.72)','Box 5.6 - De-risking'),ref('03','第2.1、4.13.1段','¶2.1, 4.13.1','allocate its resources more effectively')],'補RBA與一概排除的分別，不把銀行倡議當成MSO必須開戶。')
add('O14',1,'risk-assessment','例子：證券詐騙與掩藏實益擁有權','Examples: securities fraud and concealed beneficial ownership',[
 ('2022年報告的「唱高散貨」（ramp and dump）例子：騙徒先買入並人為推高股票價格，再以社交媒體的投資群組、冒稱投資導師或朋友／戀人關係誘使受害人高價接貨，最後大量沽出令股價下跌。這是市場操縱衍生犯罪得益的途徑；與把其他罪行得益轉入證券帳戶清洗，是不同方向。','The 2022 report’s ramp-and-dump example involves buying shares and artificially increasing the price, then using social-media investment groups, supposed investment experts or friendship/romance to induce victims to buy at inflated prices, before dumping shares and causing the price to fall. This generates proceeds through market manipulation, distinct from moving proceeds of other crimes into securities accounts to launder them.'),
 ('可疑代名投資例子包括：同一主謀指示多名表面客戶買賣同一證券；設立多個只投資同一股票、由關連人或同一資金來源認購的基金；或沒有商業／其他合理原因，以基金僅持有個人原有資產。重點是誰實際指示、出資、控制及受益，以及是否符合聲稱的關係目的；不能把所有代名或基金安排一律當成違法。','Dubious nominee-investment examples include one mastermind instructing apparent customers to trade the same security; multiple single-stock funds subscribed by related persons or funded from one source; or a fund merely holding an individual’s existing assets without a commercial/other valid reason. Examine who actually instructs, funds, controls and benefits, and consistency with the stated relationship purpose; not every nominee or fund arrangement is unlawful.'),
],[ref('25','2022年版，第5.3.9、5.3.12–5.3.14、5.3.25–5.3.29段及專題5.9–5.10','2022 edition, ¶5.3.9, 5.3.12–5.3.14, 5.3.25–5.3.29 and Boxes 5.9–5.10','Examples of red flags that may indicate')],'補上游罪行產生得益與利用金融產品清洗得益的方向差別。')

# Keep the existing manuscript formatting; execute only the pure serializer definition.
tree=ast.parse((HERE/'revise.py').read_text(encoding='utf-8'))
fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='emit')
exec(compile(ast.Module(body=[fn],type_ignores=[]),str(HERE/'revise.py'),'exec'))
for n in (1,5):emit(n,parts[n])
(HERE/'findings.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
path=NOTES/'README.md';text=path.read_text(encoding='utf-8').replace('adds 12 source-backed groups','adds 14 source-backed groups').replace('(32 bilingual point pairs)','(35 bilingual point pairs)').replace('529 bilingual','532 bilingual').replace('12組補充，共32組','14組補充，共35組').replace('529組雙語','532組雙語');path.write_text(text,encoding='utf-8')
print('Completed source-first banking/securities supplements: 14 groups, +35 pairs')
