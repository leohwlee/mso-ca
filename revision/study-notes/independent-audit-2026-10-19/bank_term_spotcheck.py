"""Post-authoring candidate check only; distractors are not facts or writing sources."""
import collections, importlib, json, re, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
sys.path.insert(0,str(HERE.parent))
bank=json.loads((ROOT/'web/questions.json').read_text(encoding='utf-8'))
notes=json.dumps([importlib.import_module(f'part{n}').PART for n in range(1,8)],ensure_ascii=False)
candidates=collections.defaultdict(set)
statements=0
for q in bank:
    # Deliberately exclude answer keys, truth flags and explanations.
    texts=[q['en']['q'],*q['en']['statements']]
    statements+=len(q['en']['statements'])
    for term in set(re.findall(r'\b[A-Z][A-Z0-9/&-]{1,15}\b',' '.join(texts))):
        if term not in notes:candidates[term].add(q['id'])
result=dict(method='All English stems/statements scanned for capitalised abbreviations absent verbatim from manuscript. Candidate/distractor scan, not semantic coverage or a claim the terms are correct.',questions=len(bank),statements=statements,candidates={k:sorted(v) for k,v in sorted(candidates.items())})
(HERE/'bank-term-candidates.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
