"""Validate coverage.json and reproduce the two readable audit reports.

python -X utf8 bank/audit/report.py          # validate and render
python -X utf8 bank/audit/report.py --check  # validate and compare saved reports

Coverage statuses describe the recorded baseline, not an official syllabus score.
Follow-ups record subsequent additions without rewriting that baseline.
"""
import collections
import hashlib
import json
import pathlib
import re
import sys
import unicodedata
from state import load_state, verify_hash

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
STATUS = {'covered':'已覆盖','partial':'部分覆盖','missing':'未覆盖','reference':'参考／范围边界'}
MODULES = {1:'一般知识',2:'条例正文',3:'条例附表',4:'海关指引',5:'管治与策略',6:'合规控制',7:'合规监察与证明'}

def norm(text):
    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', text))

def cell(value):
    return str(value).replace('|', '／').replace('\n','；')

def table(headers, rows):
    return ['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|'] + [
        '| '+' | '.join(cell(c) for c in row)+' |' for row in rows]

def read():
    return json.loads((HERE/'coverage.json').read_text(encoding='utf8'))

def validate(d):
    state = load_state()
    bank = state['bank']; qb = state['evidence']
    assert {s['doc'] for s in d['source_accounting']} == {f'{i:02}' for i in range(1,24)}
    assert len(d['source_accounting']) == 23
    ts = d['topics']; tb = {t['id']:t for t in ts}
    assert len(ts) == len(tb)
    assert {t['module'] for t in ts} == set(range(1,8))
    texts = {(lang,f'{i:02}'): (ROOT/f'docs/text/{lang}/{i:02}.txt').read_text(encoding='utf8')
             for lang in ['EN','TC'] for i in range(1,24)}
    normalized = {key:norm(s) for key,s in texts.items()}
    count_quotes=0; mapped=set(); count_evidence=0
    for path, sha in d['source_hashes'].items():
        verify_hash(path, sha, state)
    for t in ts:
        assert t['status'] in STATUS
        assert set(t['docs']) <= {f'{i:02}' for i in range(1,24)}
        assert t['missing_aspects'] or t['status'] not in ['partial','missing'], t['id']
        for e in t['evidence']:
            q=qb[e['question_id']]; mapped.add(q['id'])
            assert len(e['snapshot']) == len(e['statements'])
            for i,s in zip(e['statements'],e['snapshot']):
                assert 1<=i<=len(q['truth']),(t['id'],q['id'],i)
                assert s==dict(statement=i,truth=q['truth'][i-1],en=q['en']['statements'][i-1],tc=q['tc']['statements'][i-1]),f'changed evidence: {t["id"]} {q["id"]} #{i}'
                count_evidence+=1
        for p in t['source_pages']:
            assert all(1<=n<=len(texts[p['language'],p['doc']].split('\f')) for n in p['pages']),t['id']
        for quote in t['source_quotes']:
            assert norm(quote['text']) in normalized[quote['language'],quote['doc']],f'quote mismatch {t["id"]}: {quote["text"][:70]}'
            count_quotes+=1
    for finding in d['correctness_findings']:
        for quote in finding['source_quotes']:
            assert norm(quote['text']) in normalized[quote['language'],quote['doc']]
    linked = [tid for b in d['backlog'] for tid in b['topic_ids']]
    assert len(linked)==len(set(linked))
    assert set(linked)=={t['id'] for t in ts if t['status'] in ['partial','missing']}
    assert len(mapped)==d['baseline']['questions'],f'{len(mapped)} baseline questions mapped, expected {d["baseline"]["questions"]}'
    for b in d['backlog']:
        assert b['action'] in ['add','repair']
        for tid in b['topic_ids']:
            assert tb[tid]['backlog_id']==b['id']
    added=[]
    for f in d['implemented_followups']:
        verify_hash('web/questions.json', f['questions_sha256'], state)
        for qid in f['question_ids']:
            assert qid in qb and qid not in mapped
            added.append(qid)
    assert len(added)==len(set(added))
    retired = {r['old_id'] for r in (state['implementation'] or {}).get('replacements', [])}
    assert set(state['current'])==(mapped-retired)|set(added), 'unrecorded bank addition/removal'
    return dict(topic_count=len(ts),mapped_questions=len(mapped),source_quotes=count_quotes,
                evidence_references=count_evidence,current_questions=len(bank),
                current_statements=sum(len(q['truth']) for q in bank),
                module_counts=dict(collections.Counter(str(q['module']) for q in bank)))

def render(d,v):
    state=load_state()
    implementation=state['implementation']
    p1=state.get('p1_implementation')
    ts=d['topics']; stats=collections.Counter(t['status'] for t in ts)
    pending=[b for b in d['backlog'] if b['status']!='completed']
    new=[b for b in pending if b['action']=='add']
    estimated=sum(b['suggested_questions'] for b in new)
    readme=['# 七个单元考点覆盖审核','',
      ('职责边界、相关人士身份及关键定义专项的P1/P2缺口已补成题，两道既有问题已修订替换。其余一般流程及条件例外继续按下表跟进。' if implementation else '建议先处理已确认的错题，再补客户尽调、实益拥有人、政治人物及中介责任的条件和例外。机构职能专项按实际考试反馈单独检查，避免将“出现过名称”误作“职能已考全”。'),'',
      f'审核基线：`{d["baseline"]["commit"][:7]}`，297 道组合题、1,499 个题句。对照本地归档的 23 份官方资料，整理 **{len(ts)} 个来源考点组**：{stats["covered"]} 已覆盖、{stats["partial"]} 部分覆盖、{stats["missing"]} 未覆盖、{stats["reference"]} 参考或范围边界。不同来源可描述同一规则，因此这些是映射行数，不是独立考点总数，也不是考试覆盖率。','',
      f'跨来源合并后，尚有 **{len(new)} 项补题任务**（原工作量粗估合计 {estimated} 道组合题，部分任务已补，实际应按剩余内容调整）。'+('优先修题及范围收缩问题已处理。' if implementation else '另有1项优先修题及1项范围收缩建议。')+'优先级依据义务、条件和错误影响，不代表官方出题频率。','',
      '- [逐项覆盖表与23份资料阅读范围](COVERAGE.md)','- [结构化依据及版本摘要](coverage.json)',
      '- [名词、机构职能及角色分工专项检查](TERMS-AND-ROLES.md)',
      '- [exam-prep 审核规范优化建议](EXAM-PREP-REVIEW.md)','',
      '## 机构职能专项及本轮补充','',
      'FATF并非完全缺题：`m1-134`已测标准制定、推动实施、司法管辖区评估及跟进、高风险地区和香港责任。最初发现的具体措施范围、全球合作网络及成员交流细节已由下列补充处理。','',
      '用户进一步明确FATF只是例子后，检查已扩大为整类名词、机构职能和角色分工，详见专项报告。该报告以补充后的299题为快照，逐项区分直接测试、背景提及、具体缺口及来源／范围边界；不是只计算机构名称出现次数。专项清单与下方原补题清单有重叠，不能相加当作待补题数。','']
    if d['implemented_followups']:
        for f in d['implemented_followups']:
            readme += [f'本轮已补：{f["summary"]}。新增题号：'+ '、'.join(f'`{x}`' for x in f['question_ids'])+'。', '',f'检查：{f["validation"]}。','']
            readme += [f'审核边界：{f["limitations"]}','']
        readme += [f'补充后题库为 **{v["current_questions"]} 题、{v["current_statements"]} 个题句**。下表仍保留补题前的覆盖基线；已完成的任务在补题清单中另有标记。','']
    else:
        readme += ['专项补题尚在审核，未计为已完成。','']
    readme += ['## 七个单元概况','', '题数是题库现况；覆盖状态按本表的主要归属单元统计。跨单元的有效题句也计入来源覆盖，不能据此推断每个单元的练习深度相同。','']
    rows=[]
    for m in range(1,8):
        c=collections.Counter(t['status'] for t in ts if t['module']==m)
        rows.append([f'{m} · {MODULES[m]}',d['baseline']['module_counts'][str(m)],v['module_counts'][str(m)],c['covered'],c['partial'],c['missing'],c['reference']])
    readme+=table(['单元','基线题数','现题数','已覆盖','部分','未覆盖','参考'],rows)
    readme+=['','## 先处理的既有问题','',
      '1. **`m3-261`第3句及解释有误。** 把8,000元或以上电传转账必须附汇款人地址判为正确；条例附表2第12(3)(c)条允许客户识别号码／识别文件号码、或个人出生日期及地点等替代，第12(5)条还受本地／批量例外限制。本次已核对双语原文。修正时需同步解释、答案与旧作答记录，另做盲答；本轮未改此题。',
      '2. **`m1-142`第5句超出既定范围。** 咨询回应日期及邮箱在决定E25中已排除，建议下次修题替换；不是新增题缺口。','',
      '## 按重要程度排序的补题清单','',
      'P1优先补：重要义务、条件或易误判边界。P2补细节及执行程序。P3可选背景。同一任务已合并条例、指引、FAQ和通函的重叠规则；下列题数只是工作量估计。','']
    rows=[]
    for b in d['backlog']:
        if b['action']=='repair':
            continue
        ids='、'.join(b['topic_ids'])
        state={'completed':'本轮已补','partial':'部分已补','pending':'待补'}[b['status']]
        reason=b['reason']
        if b.get('followup_note'):
            reason+=' '+b['followup_note']
        rows.append([b['id']+' '+b['priority'],b['title'],b['suggested_questions'],state,reason,ids])
    readme+=table(['顺序／优先级','补题内容','估计题数','状态','为何补／边界','来源映射行'],rows)
    readme+=['','经营账户任务B16尚有03与06用语关系需厘清；此项不是已经定案的双语题目，不应在冲突未解决前写成统一答案。','',
      '## 方法和限制','',
      '- 从资料的正文、附表、FAQ、样题及通函附件建立考点，再搜索七个单元的实际题句。引用文档、长引文或解释提到某点，本身不算已测试。',
      '- “已覆盖”只指该行明确列出的核心内容，不能理解为所在章节每句话均有题。假句也可提供覆盖，但必须确实测试该规则。',
      '- 英文核心材料按各文件记录的范围阅读；中文重点核对缺口、术语和冲突，没有对全部旧题重新做双语独立盲答。完整边界见覆盖表。',
      '- 通函16附件的英文PDF第3–5页已查看原页截图；中文核对提取文本的关键标签。示例填写数字不作为考点。',
      '- 本次针对23份归档材料，没有重新确认官网最新版本。尤其FATF地区名单及咨询材料发布前需重查；咨询建议不等于本地现行强制要求。',
      '- 官方资料01只列七个单元名称及五类来源，未分配每个细项。这里的单元归属、优先级和建议题数均为教学判断。',
      '- 题库格式、引用核验、覆盖审核、答案盲答分别证明不同事情；自动检查通过不能推导出全部答案正确或保证通过考试。','',
      f'记录验证：23份资料均有阅读账目，{v["mapped_questions"]}道基线题均有实际题句映射；{v["evidence_references"]}条题句引用通过题号、句序及快照文本核验，{v["source_quotes"]}段引文通过归档原文文字核验。源文件保存SHA-256摘要，用于识别审核后的变更。','',
      '维护：编辑结构化记录后运行 `python -X utf8 bank/audit/report.py`；用 `--check` 验证记录与生成文档一致。原始题句、来源或既定范围变化后须重新判断相关映射，不能只更新摘要值。','']
    details=['# 逐项考点覆盖表','', '[返回结论与补题顺序](README.md)','',
      f'基线 `{d["baseline"]["commit"][:7]}`；状态描述补题前的297题。题号后的#表示本次快照中的第几句，应用显示时会重新排列。引文原文、页码、题句文本与真假值保存在 [coverage.json](coverage.json)。','']
    for m in range(1,8):
        details += [f'## 单元{m} · {MODULES[m]}','']
        rows=[]
        for t in ts:
            if t['module']!=m: continue
            evidence='；'.join(e['question_id']+'#'+','.join(map(str,e['statements'])) for e in t['evidence']) or '无直接题句'
            rows.append([t['id']+' '+t['topic'],'、'.join(t['docs'])+' '+t['locators'],STATUS[t['status']],
                '；'.join(t['covered_aspects']) or '—',evidence,'；'.join(t['missing_aspects']) or '—',t['backlog_id'] or '—'])
        details += table(['考点组','来源／位置','基线状态','已测内容','题句证据','缺少的内容','任务'],rows)+['']
    details += ['## 23份资料阅读账目','',
      '文件编号对应 [官方资料目录](../../docs/README.md)。排除范围依据本项目MSO适用边界，不能表述为官方逐条声明不考。','']
    details += table(['资料','已审核部分','参考／排除部分','限制及说明'],[
        [s['doc']+' '+s['title'],s['reviewed_units'],s['excluded_units'],s['note']] for s in d['source_accounting']])
    details += ['','## 阅读和判断记录','']+[f'- {n}' for n in d['method_notes']]+['']
    if implementation:
        for i,line in enumerate(readme):
            if line=='## 先处理的既有问题':readme[i]='## 既有问题修正'
            elif line.startswith('1. **`m3-261`'):readme[i]='1. **已以`m3-322`替换`m3-261`。** 正确区分地址与替代资料，并说明本地／群组转账例外；通过双语盲答。旧题退出抽题，交卷时的历史成绩保留。'
            elif line.startswith('2. **`m1-142`'):readme[i]='2. **已以`m1-177`替换`m1-142`。** 删除E25排除的咨询截止日期及邮箱，改考咨询的实质议题；通过双语盲答。原题及引文保存于实施记录。'
            elif line.startswith('用户进一步明确'):readme[i]='专项报告保留299题审核基线，并另列本轮21题／92个新增题句、两道修订替代题及逐项落实状态。该专项与总体补题任务有重叠，不可将两张清单的数量相加。'
            elif line.startswith('- 本次针对23份归档材料'):readme[i]='- 23份归档仍为既定范围。17日重新下载的02–09、19–21双语文件与归档完全一致，FAQ实质段落与官网一致；其他资料保留原核验日期。条例官网被客户端检查页阻挡，未确认其最新版本；此次仍按已归档条例出题。'
        readme+=['','新增题、最终盲答、改动裁决、退役快照及覆盖依据见[实施记录](implementation.json)。本轮77条P1/P2来源缺口映射均有直接题句支持；不是77个独立考点或77道题。','']
    if p1:
        readme[2]='剩余P1流程、条件及例外任务已逐项落实。职责、身份与定义专项及已知旧题修正继续保留原记录；下一批为P2细节及P3可选内容。'
        readme.insert(readme.index('- [名词、机构职能及角色分工专项检查](TERMS-AND-ROLES.md)')+1,
                      '- [P1流程、条件及例外逐项补题](P1-PROCESSES.md)')
        readme+=['','## P1流程、条件及例外补题','',
                 f'本轮核对{len(p1["task_results"])}项剩余P1任务，新增{p1["statistics"]["new_questions"]}题、{p1["statistics"]["new_statements"]}个题句。已覆盖的细节沿用现题句证据，未重复出题。',
                 '', '[逐项落实、剩余边界及审核结果](P1-PROCESSES.md) · [最终盲答与快照](p1-implementation.json)', '']
        for i,line in enumerate(readme):
            if line.startswith('经营账户任务B16尚有'):readme[i]='B16已按《牌照指引》第11.1(j)段直接测试准许户名清单。新题不解释或扩张《业务计划指引》第8项未定义的“第三方”一词；此跨文件边界仍如实保留。'
        details[4]+=' 本轮P1任务的后续落实另见[P1流程补题记录](P1-PROCESSES.md)；下表不改写历史基线。'
    return {'README.md':'\n'.join(readme),'COVERAGE.md':'\n'.join(details)}

def main():
    d=read(); v=validate(d); outputs=render(d,v)
    if '--check' in sys.argv:
        assert d['validation']==v, 'saved validation counts differ'
    else:
        d['validation']=v
        (HERE/'coverage.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    for filename, text in outputs.items():
        p=HERE/filename
        if '--check' in sys.argv:
            assert p.read_text(encoding='utf8')==text,f'regenerate {filename}'
        else:
            p.write_text(text,encoding='utf8')
    print(json.dumps(v,ensure_ascii=False))

if __name__=='__main__':
    main()
