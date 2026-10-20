"""Audit-only source map, preservation proof and local screenshot gallery."""
from pathlib import Path
import hashlib, html, json, sys
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent
ROOT = NOTES.parents[1]
sys.path.insert(0, str(NOTES))
import build

actions = {
 'three-stages':'保留可重疊機制及教學例子；中等寬度提早重排箭頭。',
 'ml-tf-pf':'保留相同維度比較；窄欄重排，語意表頭保留。',
 'risk-lists':'保留風險處理與法律制裁區分；不把名單畫成同一流程。',
 'cash-scope':'保留旅客／貨物途徑及緊貼的例外；比較符號連同金額不分行。',
 'cross-sector-mechanisms':'保留2022年份及例子性質；不新增順序。',
 'licence-clocks':'保留各自起點；當月改為1個月，雙語標籤緊湊。',
 'penalty-ceilings':'保留兩套制度；去掉似除法的斜線，明示乘數範圍。',
 'review-commencement':'保留真正決策樹；否分支指向具體下一項。',
 'inspection-versus-investigation':'兩個對等欄位等寬及同等字重。',
 'money-boundaries':'保留三組不同制度；比較符號不分行、窄欄重排及緊湊標籤。',
 'ownership-boundary':'保留百分比及控制權的獨立條件；改善跨Part跳轉。',
 'fee-components':'保留可相加但非全數普遍適用的費用；改用具體欄名。',
 'shell-bank-and':'保留四項外層AND；否定隸屬條件內的三個AND明確包含。',
 'three-places':'保留用途、對象及限制；使用具體比較欄名。',
 'assessment-pass':'保留兩個及格要求的AND，沒有改成先後步驟。',
 'assessment-clocks':'保留三組事項及各自起點；縮短標籤距離，完整條件不隱藏。',
 'exchange-rights':'保留未完成／已完成與第4條違反的條件區分。',
 'risk-levels':'保留機構／客戶兩層關係及回饋說明；窄欄重排。',
 'review-frequency':'保留定期、事前與事件觸發區分；表頭語意及密度改善。',
 'control-responsibilities':'保留角色關係與可兼任說明；依實際寬度重排。',
 'party-roles':'保留公司／BO／代表／董事與可重疊角色；跨Part定位改善。',
 'sow-sof':'保留來源與銀行渠道的差別；例子不變成強制清單。',
 'cdd-extent-tree':'保留真正的程度分支；明確下一項及其他要求獨立適用。',
 'pep-categories':'保留類別、風險和前PEP跨類別狀態；表頭及窄欄改善。',
 'pep-common-and':'保留三組AND；SOW AND SOF作包含的雙條件。',
 'transfer-information':'保留共同資料加額外OR；出生日期AND出生地點維持一個選項。',
 'reliance-outsourcing':'保留法律責任區分；改善語意表頭和窄欄。',
 'cdd-trigger-tree':'替換互斥樹為跨情況要求加關係／交易情況圖；舊錨點保留。',
 'wire-responsibilities':'保留真實付款鏈及缺漏資料的風險為本處理；窄欄重排。',
 'trade-value-paths':'保留不一致符號與實際流向箭頭的差別；教學例子標示保留。',
 'retention-clocks':'保留獨立起點；培訓三年明示應／指引，標籤緊湊。',
 'after-report-parallel':'保留並行職責；不改成步驟或答題套路。',
 'reporting-route':'保留內部披露及MLRO兩種判斷結果的明確標籤；不增加複雜總流程。',
}
panels=[(n,s,p) for n,sections in build.PANELS.items() for s,items in sections.items() for p in items]
assert len(panels)==33 and {p['id'] for _,_,p in panels}==set(actions)
lines=['# 33個圖表：處理及原文對應','',
       '圖表逐項判斷來自本輪A評審、B實測及主審核對。以下引用直接取自本版內容源，解析至catalog的實際檔名；引用定位成功本身不代表所有內容已完成獨立含義覆核。','']
for n,s,p in panels:
    lines += [f'## Part {n} · {p["title"]["tc"]}', '',
              f'[正式位置](../part-{n}.html#{p["id"] if p["id"].startswith("memory-") else "memory-"+p["id"]}) · `{p["kind"]}`','',
              actions[p['id']],'']
    grouped={}
    for r in p['refs']:
        for lang in ('tc','en'):
            ed=build.DOCS[r['doc']]['editions']['EN' if r['doc']=='24' else lang.upper()]
            key=(r['doc'],lang,ed['file'],ed['path'])
            grouped.setdefault(key,[])
            if r['locator'][lang] not in grouped[key]:grouped[key].append(r['locator'][lang])
    for (doc,lang,name,path),locators in grouped.items():
        link='../../../docs/'+quote(path,safe='/')
        lines.append(f'- [{name}]({link})：{"；".join(locators)}'+('（中文為學習譯文）' if doc=='24' and lang=='tc' else ''))
    lines.append('')
(HERE/'VISUAL-SOURCE-MAP.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

baseline=json.loads((HERE/'baseline.json').read_text(encoding='utf-8'))
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
protected={p:dict(before=h,after=digest(ROOT/p)) for p,h in baseline['protected'].items()}
manuscripts={f'part{n}.py':dict(before=baseline['sha256'][f'revision/study-notes/part{n}.py'],after=digest(NOTES/f'part{n}.py')) for n in range(1,8)}
assert all(r['before']==r['after'] for r in [*protected.values(),*manuscripts.values()])
changed=[p for p,h in baseline['sha256'].items() if digest(ROOT/p)!=h]
allowed={'DESIGN.md',*[f'revision/study-notes/{name}' for name in ['build.py','gap_check.py','visual_panels.py','visual_render.py','style.css','README.md','coverage.json','index.html']+[f'part-{n}.html' for n in range(1,8)]]}
assert set(changed)<=allowed,(set(changed)-allowed)
(HERE/'preservation.json').write_text(json.dumps(dict(protected=protected,manuscripts=manuscripts,baseline_files_changed=changed,old_review_files_unchanged=True,source_of_truth='baseline.json and baseline.zip captured before this visual refinement'),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def image_link(src,caption):
    assert (HERE/src).is_file(),src
    return f'<figure><figcaption>{html.escape(caption)}</figcaption><a href="{src}"><img src="{src}" loading="lazy" alt="{html.escape(caption)}"></a><p class="small">首段縮圖；點擊圖片查看完整截圖。</p></figure>'

body=['<h1>七個Part · 可視化修正預覽</h1>',
      '<p>33個圖表已複核。保留完整條件與B風格，主要修正錯誤分支暗示、內層AND、窄欄比較及跳轉位置。</p>',
      '<nav><a href="../index.html">正式筆記</a><a href="REPORT.md">審核報告</a><a href="VISUAL-SOURCE-MAP.md">33項處理及來源</a></nav>',
      '<h2>CDD：移除互斥暗示</h2><p>懷疑／資料疑問可與業務關係並存。新圖將跨情況要求獨立列出，其他關係／交易要求仍須處理。</p><div class="compare">',
      image_link('assessment-a-evidence/p6-memory-cdd-trigger-tree-tc-desktop.png','修改前：只有「否」分支繼續'),
      image_link('previews-after/part-6-memory-cdd-trigger-tree-tc-1440.png','修改後：明確列出可同時適用的情況'),
      '</div><h2>七個Part代表預覽</h2>']
selection=[
 (1,'ml-tf-pf','ML／TF／PF：保留相同維度比較'),
 (2,'inspection-versus-investigation','查察／調查：對等列使用同等寬度及字重'),
 (3,'shell-bank-and','空殼銀行：外層四條件與內層三條件分清'),
 (4,'assessment-clocks','評核期限：分組及不同起算點仍完整保留'),
 (5,'control-responsibilities','管理責任：保留職能關係，窄欄清楚重排'),
 (6,'transfer-information','跨境電傳：出生日期與出生地點合為一個選項'),
 (7,'retention-clocks','保存紀錄：不同起點及培訓指引措辭'),
]
for n,key,title in selection:
    body += [f'<section><h3>Part {n} · {title}</h3><nav>'+''.join(f'<a href="../part-{n}.html?lang={lang}#memory-{key}">{label}</a>' for lang,label in [('tc','繁體中文'),('en','English'),('both','雙語')])+'</nav><div class="compare">',
             image_link(f'previews-after/part-{n}-memory-{key}-tc-1440.png','桌面 · 繁體中文'),
             image_link(f'previews-after/part-{n}-memory-{key}-en-390.png','手機 · English'),
             '</div></section>']
body += ['<p>截圖來自實際本地頁面；長圖匯出時只隱藏固定頂欄以免遮蓋內容。正常跳轉及語言切換另有實際視口驗證。這些是顯示證據，並非學習成效或考綱完整性保證。</p>']
css='''body{margin:0;background:#edf2f6;color:#263e52;font:17px/1.8 "Microsoft JhengHei",sans-serif}main{max-width:1180px;margin:32px auto;background:white;padding:40px}h1,h2,h3,a{color:#173f63}h1{font-size:28px}h2{margin-top:48px;font-size:24px}h3{font-size:21px}nav{display:flex;flex-wrap:wrap;gap:12px 24px;margin:20px 0}section{border-top:1px solid #d5e0e8;margin-top:36px;padding-top:20px}.compare{display:grid;grid-template-columns:1fr 1fr;gap:28px}figure{margin:0;min-width:0}figcaption{font-weight:600;margin:12px 0}img{display:block;width:100%;max-height:650px;object-fit:cover;object-position:top;border:1px solid #d5e0e8;box-sizing:border-box}.small{font-size:13px;color:#526a7e}a:focus-visible{outline:2px solid #173f63;outline-offset:4px}@media(max-width:760px){main{margin:12px;padding:24px 18px}.compare{grid-template-columns:1fr}h1{font-size:24px}}'''
(HERE/'preview.html').write_text('<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>七個Part可視化修正</title><style>'+css+'</style></head><body><main>'+''.join(body)+'</main></body></html>',encoding='utf-8')
print(json.dumps(dict(panels=len(panels),protected_unchanged=True,manuscripts_unchanged=True,baseline_files_changed=changed),ensure_ascii=False))
