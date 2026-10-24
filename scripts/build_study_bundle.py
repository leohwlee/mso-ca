"""Build a reproducible offline bundle without audit drafts or out-of-scope sources."""
from pathlib import Path, PurePosixPath
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import argparse,hashlib,json,zipfile,posixpath
ROOT=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and a.get('href'):self.links.append(a['href'])
def content():
    paths=[Path('dist/mso-ca.html'),Path('web/fonts/OFL.txt')]+[Path(f'revision/study-notes/{name}') for name in ['index.html','amounts.html']+[f'part-{n}.html' for n in range(1,8)]]
    catalog=json.loads((ROOT/'docs/catalog.json').read_text(encoding='utf-8'))
    for d in catalog['documents']:
        if 1<=int(d['id'])<=26:
            paths.extend(Path('docs')/e['path'] for e in d['editions'].values())
    files={p.as_posix():(ROOT/p).read_bytes() for p in sorted(set(paths))}
    # Markdown originals have canonical LF hashes in the catalog; make bundles
    # identical across Windows CRLF and Linux LF checkouts without editing sources.
    files={name:(data.replace(b'\r\n',b'\n') if name.endswith('.md') else data) for name,data in files.items()}
    files['index.html']=('''<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MSO Study / 溫習</title><style>body{background:#edf2f6;color:#263e52;font:18px/1.8 sans-serif;margin:0}main{max-width:700px;margin:48px auto;background:white;padding:32px}h1,a{color:#173f63}a{display:block;padding:16px 0}p{font-size:16px}@media(max-width:600px){main{margin:20px;padding:24px}}</style><main><h1>MSO Competence Assessment</h1><a href="revision/study-notes/index.html">閱讀七個部分 · Read seven-part notes</a><a href="dist/mso-ca.html">模擬試及自選練習 · Mock exam and custom practice</a><p>完整解壓後開啟此頁，保留資料夾結構。可離線使用；引用連到隨附01–26原件。</p><p>Extract the whole ZIP before opening this page. Keep the folders together. Notes, practice and the cited 01–26 originals work offline.</p><p>三種閱讀語言：繁體中文、English、雙語。選定的01–26並不等於完整官方考試範圍。第24份中文為學習譯文；歷史資料保留原版本日期。</p></main></html>''').encode()
    files['README.txt']=('MSO study bundle / MSO完整學習包\nVersion / 版本: v1.13.2\n\n75 topics; 626 bilingual point pairs; 79 visuals (14 tables, 65 diagrams, 35 of them list cards that count the items of a source list); a study-tier filter, 69 exam traps and 131 ruling marks (93 rulings, hidden until switched on); a numbers page with 70 amounts, periods, fees and penalties.\n75個主題、626組雙語要點、79個圖表（14張表、65個圖解，其中35張是標明項數的清單卡）；學習層次篩選、69項易錯提示及131處裁決標記（93項裁決，按鈕開啟才顯示）；另有數字總表，集中70項金額、期限、費用及刑罰；數量不是覆蓋率。\nThe CDD trigger map shows potentially overlapping cases. Counts are not coverage percentages.\nCDD觸發圖呈現可同時適用的情況。\n\nExtract the entire ZIP and open index.html. Keep all folders together.\n完整解壓ZIP，開啟index.html；不要只移走某個HTML檔。\n\nNotes: revision/study-notes/index.html\nNumbers: revision/study-notes/amounts.html\nPractice: dist/mso-ca.html (588 bilingual combination questions / 588道雙語組合題; the wrong-answer book keeps every question answered wrong until it is answered right twice / 錯題本記下答錯的題目，連續答對兩次才移除)\nOriginals 01–26: docs/TC and docs/EN\n\nSelected reading scope is not the full official syllabus. Archived source versions are retained.\n指定閱讀範圍不等於官方完整考綱，原件保留repo存檔版本。\n').encode()
    for name,data in list(files.items()):
        if name.startswith('revision/study-notes/') or name=='index.html':
            parser=Links();parser.feed(data.decode())
            for href in parser.links:
                u=urlsplit(href)
                if u.scheme or not u.path:continue
                target=posixpath.normpath(posixpath.join(posixpath.dirname(name),unquote(u.path)))
                assert target in files,(name,href,target)
    manifest={name:hashlib.sha256(data).hexdigest() for name,data in sorted(files.items())}
    files['SHA256SUMS.json']=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode()
    return files
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=ROOT/'dist/mso-study-bundle.zip');ap.add_argument('--check',action='store_true');args=ap.parse_args();files=content()
    if args.check:
        with zipfile.ZipFile(args.output) as z:
            assert set(z.namelist())==set(files)
            for n,b in files.items():assert z.read(n)==b,n
    else:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(args.output,'w',compression=zipfile.ZIP_STORED) as z:
            for name,data in sorted(files.items()):
                info=zipfile.ZipInfo(name,date_time=(2026,10,19,0,0,0));info.create_system=3;info.external_attr=0o100644<<16;z.writestr(info,data)
    print(json.dumps(dict(files=len(files),sha256=hashlib.sha256(args.output.read_bytes()).hexdigest(),bytes=args.output.stat().st_size)))
if __name__=='__main__':main()
