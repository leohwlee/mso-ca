"""Read-only bank gap audit, run after source-first manuscript authoring.

Source overlap is a navigation aid, not proof every bank statement is explained.
No question text, options or explanations are rendered into the study pages.
"""
import argparse, hashlib, json
from pathlib import Path
from build import HERE, ROOT, PARTS, manifest

ADDITIONS=[
    dict(topic='Customer assessment framework and finalisation',source='03 ¶2.13–2.16',notes='part-5.html#customer-assessment'),
    dict(topic='Tribunal evidence, costs, privacy and written orders',source='04 ss.61–68',notes='part-2.html#statutory-administration'),
    dict(topic='Tribunal panel, sittings, consent and chair-alone powers',source='04 Schedule 4 ss.2–9',notes='part-3.html#tribunal-schedule'),
    dict(topic='Supporting evidence by legal form and premises use',source='05 ¶16.1–16.3',notes='part-4.html#application'),
    dict(topic='CO/MLRO employment exception and permitted account names',source='05 ¶4.15(a), ¶11.1(j)',notes='part-5.html#roles; part-4.html#licensing-actions'),
    dict(topic='FAQ practical verification and full cross-border screening parties',source='06 A3–A15, A24',notes='part-6.html#identity; part-6.html#screening'),
    dict(topic='Half-year return filing deadline',source='05 ¶11.2; 15 main text and annex',notes='part-7.html#periodic-return'),
    dict(topic='Occasional CDD completion-date retention and unsuccessful applications',source='04 Schedule 2 s.20(3A); 06 A28',notes='part-7.html#retention'),
]

def audit():
    bank_path=ROOT/'web/questions.json';quotes_path=ROOT/'docs/quotes.json'
    bank=json.loads(bank_path.read_text(encoding='utf-8'));quotes=json.loads(quotes_path.read_text(encoding='utf-8'))
    source_routes=manifest()['documents']; rows=[]
    for q in bank:
        docs=sorted({r['doc'] for lang in ('tc','en') for r in quotes[q['id']][lang]})
        assert all(source_routes[d] for d in docs),(q['id'],docs)
        # Keep identifiers and source routes only. Content generation imports none of this.
        rows.append(dict(id=q['id'],part=q['module'],source_documents=docs))
    assert len(rows)==len({r['id'] for r in rows})==525
    return dict(method='Post-authoring identifier/source-route check only. This tool does not assess bank-statement semantics or prove completeness. Manual concept review is recorded separately.',bank_sha256=hashlib.sha256(bank_path.read_bytes()).hexdigest(),quotes_sha256=hashlib.sha256(quotes_path.read_bytes()).hexdigest(),manuscripts=manifest()['manuscripts'],essentials=manifest()['essentials'],recall=manifest()['recall'],questions_checked=len(rows),historical_supplements=ADDITIONS,source_routes=source_routes,source_overlap=rows)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');ap.add_argument('--output',type=Path,default=HERE/'visual-upgrade-2026-10-19'/'bank-source-routes.json');args=ap.parse_args()
    text=json.dumps(audit(),ensure_ascii=False,indent=2)+'\n';path=args.output
    if args.check:assert path.read_text(encoding='utf-8')==text,'Stale gap audit'
    else:path.write_text(text,encoding='utf-8',newline='\n')
    print('Bank gap audit: 525 identifiers checked; no bank content supplied to notes.')
if __name__=='__main__':main()
