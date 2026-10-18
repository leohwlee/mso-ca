"""Generate current source/question accounting, independently of historical audits."""
import collections
import json
import pathlib
import sys

ROOT=pathlib.Path(__file__).resolve().parents[2]

def load(p):return json.loads((ROOT/p).read_text(encoding='utf8'))

def outputs():
    bank=load('web/questions.json'); quotes=load('docs/quotes.json')
    catalog=load('docs/catalog.json'); docs=catalog['documents'][:26]
    counts=collections.Counter(q['module'] for q in bank)
    bydoc={d['id']:set() for d in docs}
    for qid,sides in quotes.items():
        for side in sides.values():
            for quote in side:
                assert quote['doc'] in bydoc, f'Out-of-scope quote: {qid}'
                bydoc[quote['doc']].add(qid)
    record_path=ROOT/'bank/audit/active26-implementation.json'
    record=load('bank/audit/active26-implementation.json') if record_path.exists() else None
    def mapping(tc):
        lang='TC' if tc else 'EN'
        lines=['# '+('現行題庫來源：01–26' if tc else 'Active question sources: 01–26'),'',
          ('只使用以下26份本地原件；27–47不屬有效題庫。數字按逐句決定答案的引文計算，不代表整份文件已全面考核。每題可使用多份文件。' if tc else
           'Only these 26 local publications may support active questions. Documents 27–47 are excluded. Counts use deciding statement quotes, not a claim of complete document coverage. A question can use several documents.'),'',
          '| '+('部分 | 題數' if tc else 'Part | Questions')+' |','|---|---|']
        lines += [f'| {m} | {counts[m]} |' for m in range(1,8)]
        lines += [f'| **'+('總數' if tc else 'Total')+f'** | **{len(bank)}** |','',
          '| '+('文件 | 原件 | 引用題數' if tc else 'Document | Original | Questions with deciding quotes')+' |','|---|---|---|']
        for d in docs:
            p=d['editions'][lang]['path'].replace(' ','%20')
            lines.append(f'| {d["id"]} | [{d["title"][lang]}]({p}) | {len(bydoc[d["id"]])} |')
        lines += ['',('第24項只有英文原件，中文題目明確標示「學習譯文」，引文保留英文。通函內未收錄的外部文件不構成出題依據。' if tc else
          'Document 24 is English-only: Chinese questions are labelled study translations and retain English quotes. External publications merely linked by a circular do not become sources.'),'',
          ('[現行覆核記錄](../bank/audit/ACTIVE-SCOPE.md) · [完整資料目錄](catalog.json)' if tc else
           '[Current review record](../bank/audit/ACTIVE-SCOPE.md) · [Complete catalog](catalog.json)'),'']
        return '\n'.join(lines)
    report=['# Active 01–26 question-bank scope','',
      'Owner decision: 18 October 2026. Approximately 525 bilingual combination questions; seven parts; mock exam and custom practice only. This personal practice scope is not the official exam syllabus.','',
      f'Active questions: **{len(bank)}**. Statements: **{sum(len(q["truth"]) for q in bank)}**.','',
      '| Part | Questions | Mock draw |','|---|---|---|']
    report += [f'| {m} | {counts[m]} | 5 |' for m in range(1,8)]
    report += ['','## Review and provenance','',
      'The 357-question baseline is preserved byte-for-byte in `history/2026-10-18-before-active26.zip`. Three archived-circular items (m1-140, m1-141, m1-181) are retired, with their IDs reserved. All other baseline questions and their quotes are unchanged.','',
      'The four original audit reports describe the original 23-source checklist. They validate a reconstructed historical bank; they do not claim to cover this expansion. The new record validates retained content, retirements, final blind answers, source hashes and topic mappings separately.','']
    if record:
        report += [f'New questions: **{len(record["added_question_ids"])}**. Final bilingual blind review records: **{len(record["blind_review"]["items"])}**.','',
          'Reviewers answered without keys or explanations. Agents inherited the parent model; this is independent context review, not a claimed different-model-family panel. Every recorded verdict is bound to the final stem, statements and citation by a text hash.','']
    report += ['## Coverage boundaries','',
      '- Only local publications 01–26 support answers, including exceptions and distractors. Numbering does not import documents linked by a circular.',
      '- Coverage maps distinguish a new rule from a new application. Decision-changing scenarios may reuse a rule; decorative variants and repeated statements are excluded.',
      '- Document 24 has no official Chinese edition. Its Chinese questions and explanations are study translations, visibly labelled; deciding quotes remain English.',
      '- Report 25 findings are explicitly dated to the 2022 report, not presented as a live country-risk assessment.',
      '- Source quote checks verify occurrence, not legal meaning. Blind answers and explanation review provide the semantic checks; no claim of perfect accuracy or complete official exam coverage is made.',
      '', '[Source-by-source accounting](../../docs/QUESTION-SOURCES.md) · [Machine-readable evidence](active26-implementation.json)','']
    return {'docs/QUESTION-SOURCES.md':mapping(False),'docs/QUESTION-SOURCES.zh-Hant.md':mapping(True),'bank/audit/ACTIVE-SCOPE.md':'\n'.join(report)}

if __name__=='__main__':
    for p,s in outputs().items():
        if '--check' in sys.argv:
            assert (ROOT/p).read_text(encoding='utf8')==s, f'Regenerate {p}'
        else:
            (ROOT/p).write_text(s,encoding='utf8',newline='\n')
    print('Current source accounting is consistent.')
