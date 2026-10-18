"""Validate and render the source-based terminology and responsibility audit.

python -X utf8 bank/audit/terms_report.py [--check]
The JSON is a reviewed snapshot, not a keyword search or an exam coverage score.
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
STATUS = {'covered': '列示要点已考', 'partial': '部分覆盖', 'missing': '未直接测试', 'reference': '参考／范围边界'}
CATEGORIES = {'external': '机构及外部角色', 'internal': '内部角色与责任分工', 'concept': '名词定义及易混概念', 'instrument': '法例、指引及工具的用途'}

def norm(s):
    return re.sub(r'\s+', '', unicodedata.normalize('NFKC', s))

def cell(s):
    return str(s).replace('|', '／').replace('\n', ' ')

def table(headers, rows):
    return ['| ' + ' | '.join(headers) + ' |', '|' + '|'.join(['---'] * len(headers)) + '|'] + [
        '| ' + ' | '.join(cell(c) for c in row) + ' |' for row in rows]

def validate(d):
    source_ids = {d['id'] for d in json.loads((ROOT/'docs/catalog.json').read_text(encoding='utf8'))['documents'] if d['original_bank_source']}
    state = load_state()
    for path, sha in d['snapshot']['sha256'].items():
        verify_hash(path, sha, state)
    bank = state['bank']; qb = state['evidence']
    baseline = (state['implementation'] or {}).get('baseline')
    assert (baseline['questions'] if baseline else len(bank)) == d['snapshot']['questions']
    assert (baseline['statements'] if baseline else sum(len(q['truth']) for q in bank)) == d['snapshot']['statements']
    assert {s['doc'] for s in d['source_accounting']} == source_ids
    rows = {r['id']: r for r in d['rows']}
    assert len(rows) == len(d['rows'])
    texts = {(l, num): norm((ROOT / f'docs/text/{l}/{num}.txt').read_text(encoding='utf8'))
             for l in ['EN', 'TC'] for num in source_ids}
    quote_count = evidence_count = 0
    for r in d['rows']:
        assert r['status'] in STATUS and r['category'] in CATEGORIES, r['id']
        assert r['source_units'], r['id']
        for s in r['source_units']:
            assert s['doc'] in source_ids and s['locator'] and s['points'], r['id']
        if r['status'] in ['partial', 'missing']:
            assert r['untested'], r['id']
        if r['status'] == 'covered':
            assert r['tested'] and not r['untested'], r['id']
        for e in r['tested'] + r.get('context_mentions', []):
            q = qb[e['qid']]
            assert len(e['snapshot']) == len(e['statements'])
            for i, snapshot in zip(e['statements'], e['snapshot']):
                assert 1 <= i <= len(q['truth'])
                assert snapshot == dict(statement=i, truth=q['truth'][i-1], en=q['en']['statements'][i-1], tc=q['tc']['statements'][i-1]), (r['id'], e['qid'], i)
                assert (e['qid'], i) != ('m3-261', 3), 'Known incorrect statement cannot establish coverage'
                evidence_count += 1
        for p in r['untested'] + r.get('reference_points', []):
            assert p['priority'] in ['P1', 'P2', 'P3', 'reference'], r['id']
            for lang, key in [('EN', 'quote_en'), ('TC', 'quote_tc')]:
                assert p.get(key) and norm(p[key]) in texts[lang, p['doc']], (r['id'], lang, p.get(key))
                quote_count += 1
    for group in d['priority_groups']:
        assert group['row_ids'] and set(group['row_ids']) <= rows.keys(), group['id']
    return dict(rows=len(rows), quotes=quote_count, evidence=evidence_count,
                statuses=dict(collections.Counter(r['status'] for r in d['rows'])),
                implementation=state['implementation'], p1_implementation=state.get('p1_implementation'),
                remaining_implementation=state.get('remaining_implementation'),
                current_questions=len(bank), current_statements=sum(len(q['truth']) for q in bank))

def render(d, v):
    implementation = v['implementation']
    fulfilled = collections.defaultdict(list)
    if implementation:
        for link in implementation['coverage']:
            fulfilled[link['row_id'], link['gap_index']].append(link)
    completion=v.get('remaining_implementation')
    if completion:
        for link in completion['specialist_coverage']:
            fulfilled[link['row_id'],link['gap_index']].append(link)
    lines = ['# 名词、机构职能及角色分工专项覆盖检查', '',
        '**结论：这类题已有实质覆盖，但覆盖不均；主要短板是完整职能、主体区别和定义条件。不能由 FATF 一例推断整类缺题，也不能由机构名称出现过就判定职能已考全。**', '',
        f'检查对象：现有 {d["snapshot"]["questions"]} 道题、{d["snapshot"]["statements"]:,} 个题句，对照既定 23 份官方归档资料。已包含先前新增的 `m1-152`、`m6-385`。本专项是覆盖盘点及补题排序；下述缺口尚未据此新增题目。', '',
        '[总体审核](README.md) · [逐条证据与双语原文](terms-and-roles.json)', '',
        '## 怎样判断', '',
        '- 先从资料正文、附表、脚注和 FAQ 列出机构、角色、概念及文件用途，再对照七个单元的实际题句。',
        '- 正确题句及确实考查该区别的错误题句都可提供覆盖。只在解释、引文或题干背景中出现，不能证明该点作为判断内容被测试。',
        '- “列示要点已考”只针对本行明列的内容；不表示该机构所有法定职能或本章每一细节都已考全。',
        '- 区分基本概念缺口、原有题的条件细节、资料只提名称、以及其他行业的范围边界。不同法律身份不能因为定义相似而互相顶替。', '',
        '## 主要发现', '']
    lines += table(['类别', '基线已经考到', '基线缺口／边界（本轮落实见下）'], [
        ['国际机构', 'FATF 的标准制定、推动实施、评估跟进及合作；APG 类型学报告的发布者区别', '资料没有列出的 IMF、世银、Egmont 全部职能不能算缺题；只按归档资料列明的作用检查'],
        ['香港监管及报告机构', '海关关长的发牌／监管；JFIU 的接报、反馈与联络；相关机关的部分制裁职能', '行政长官、保安局局长、法庭的部分权限及相互区别'],
        ['内部责任分工', 'CO 监督制度；MLRO 处理内部报告、决定向 JFIU 报告；高层审批和员工报告线', 'CO 对高层的支持导引、高层保障资源；前政治人物停止加强尽调的批准；依赖中介的持续监察边界'],
        ['客户及相关人士', '客户与公司代表的区别；BO／PEP 的主要类别；部分 connected parties 定义', '合伙／信托的有关连者及身份重叠；BO 与 ultimate owner 分开判断；代他人行事与其他类别的 BO 认定'],
        ['基本名词', '洗钱／恐怖融资、三阶段、知悉／怀疑、财富来源／资金来源、业务关系／非经常交易', '恐怖分子财产的定义；兑换／汇款服务的部分范围；信托、国际组织及识别号码的定义细节'],
        ['文件用途及证明角色', '主要条例和指引用途、发牌与纪律制度、部分证明人职责', '适当人选声明见证人、身份文件认证人的完整职责和适用资格；面见代表与应考代表区别'],
    ])
    lines += ['', '## 建议补题顺序', '',
        '先补实务判断会改变的主体和概念，再补完整清单及定义细节，最后才考虑低价值考务名词。优先级是教学判断，不代表官方出题频率。以下是跨来源合并的工作包，不是“一行一题”。', '']
    lines += table(['顺序', '补题方向', '具体目标', '对应记录', '落实状态'], [
        [g['id'] + ' ' + g['priority'], g['title'], g['reason'], '、'.join(g['row_ids']),
         ('P1/P2已补；P3按下列明细保留' if any(p['priority'] in ['P1','P2'] for r in d['rows'] if r['id'] in g['row_ids'] for p in r['untested']) else 'P3可选，保留') if implementation else '待补'] for g in d['priority_groups']])
    lines += ['', '其他记录中的 P2／P3 细节保留在下面，按学习价值选择，不能为了让每个机关都出题而机械扩充。原总体审核的 40 项补题任务与本表有重叠，**不得把两张清单的数量相加**。', '',
        '## 全部专项映射', '',
        f'共 {v["rows"]} 行来源映射：列示要点已考 {v["statuses"].get("covered",0)} 行、部分覆盖 {v["statuses"].get("partial",0)} 行、未直接测试 {v["statuses"].get("missing",0)} 行、参考／范围边界 {v["statuses"].get("reference",0)} 行。同一主体可在不同来源承担不同职责，因此这些不是独立机构数或考试覆盖率。题号后的 `#` 是当前文件中的句序；练习时会重新排序。', '']
    for category, title in CATEGORIES.items():
        lines += ['### ' + title, '']
        for r in d['rows']:
            if r['category'] != category:
                continue
            points = '；'.join(p for s in r['source_units'] for p in s['points'])
            locators = '；'.join(s['doc'] + ' ' + s['locator'] for s in r['source_units'])
            evidence = '；'.join('`' + e['qid'] + '#' + ','.join(str(i) for i in e['statements']) + '`：' + e['point'] for e in r['tested']) or '没有用于证明本行覆盖的实际题句。'
            lines += [f'**{r["id"]} · {r["name"]} — {STATUS[r["status"]]}**', '',
                      f'- 来源与检查要点：{locators}。{points}', f'- 已考内容：{evidence}']
            for index, p in enumerate(r['untested']):
                refs = fulfilled[r['id'], index]
                if refs:
                    links = '、'.join('`' + e['question_id'] + '#' + ','.join(map(str,e['statements'])) + '`' for e in refs)
                    lines += [f'- 已补（原{p["priority"]}缺口）：{p["point"]}。题句：{links}。依据：{p["doc"]} {p["locator"]}。']
                else:
                    lines += [f'- 待补（{p["priority"]}）：{p["point"]}。依据：{p["doc"]} {p["locator"]}。']
            if r.get('context_mentions'):
                lines += ['- 仅作背景出现：' + '；'.join('`' + e['qid'] + '#' + ','.join(str(i) for i in e['statements']) + '`：' + e['point'] for e in r['context_mentions'])]
            if r.get('notes'):
                lines += ['- 边界／说明：' + r['notes']]
            lines += ['']
    lines += ['## 资料范围和核验', '',
        '沿用总体审核的归档版本及范围决定。专项逐份检查与机构、角色、概念和工具用途有关的内容；不把其他行业的完整监管制度或没有来源支持的机构百科搬入 MSO 题库。', '']
    lines += table(['资料', '文件', '专项处理'], [[s['doc'], s['title'], s['note']] for s in d['source_accounting']])
    lines += ['', f'核验：{v["evidence"]} 条题句引用与当前双语题句、真假值逐一保存快照；{v["quotes"]} 段双语缺口／边界引文与归档原文匹配。机械核验用于防止错题号、错引文和版本漂移，不能取代实质判断。', '',
        '保留限制：这是对既定 23 份归档资料的检查，未重查官网是否已更新；未对全部旧题重做双语盲答。“未直接测试”不代表从来没有在解释中讲过。原审核发现的 `m3-261#3` 错误和 `m1-142#5` 范围问题仍待处理，本专项没有将已知错误题句当成有效覆盖。', '',
        '维护：运行 `python -X utf8 bank/audit/terms_report.py --check` 检查本报告。题库、来源或范围决定变化时必须重判映射；不能仅替换摘要值。', '']
    if implementation:
        lines[2] = '**结论：本轮已补齐专项清单全部P1/P2来源缺口，新增21题、92个题句，并修订替换两道旧题。P3可选内容及总体审核中的其他流程、条件例外仍保留。**'
        lines[4] = f'审核基线：299道题、1,507个题句，对照既定23份官方归档资料。补题后现为{implementation["current"]["questions"]}题、{implementation["current"]["statements"]:,}个题句。下表保留原188行映射及基线状态，并在每项原缺口下列明最终补题。'
        lines[6] += ' · [补题、盲答与修订实施记录](implementation.json)'
        lines.insert(8, '本轮落实77条P1/P2来源缺口映射，涉及59行；重叠来源已合并为21道新题。77不是独立考点数，也不是考试覆盖率。新增及替代题均由另一审核者分别按英、繁原文盲答，最终文字与审核快照一致；同会话模型审核的局限保留在实施记录。\n')
        for i,line in enumerate(lines):
            if line.startswith('其他记录中的 P2／P3'):lines[i]='P1/P2专项缺口已落实；剩余P3细节保留在下面。总体审核另有一般流程和条件例外缺口，**不得把两张清单的数量相加**。'
            elif line.startswith('共 ') and '行来源映射' in line:lines[i]=line.replace('共 ', '原审核基线共 ',1).replace('是当前文件中的句序','是对应快照中的句序')
            elif line.startswith('保留限制：'):lines[i]='保留限制：仍以既定23份归档为范围。2026年10月17日重新下载03、05、10–15、21、23、32的双语文件，均与归档完全一致；FAQ实质段落与官网匹配。其他资料保留原核验日期，条例官网被客户端检查页阻挡，未确认最新版本。未对全部旧题重做双语盲答。`m3-261`已由`m3-322`替换，`m1-142`已由`m1-177`替换；原题及引文保留于实施记录，旧成绩保留。'
    if v.get('p1_implementation'):
        lines[4]=f'专项审核基线为299题、1,507个题句；职责／定义补题后为320题。后续P1流程补题完成后，现为{v["current_questions"]}题、{v["current_statements"]:,}个题句。本表保留原188行专项映射及逐项落实，后续流程补题见[P1流程记录](P1-PROCESSES.md)。'
        lines[2]='**结论：专项P1/P2来源缺口及后续P1流程任务已补成题。P2流程细节与P3可选内容仍按总体清单保留。**'
        lines=[line.replace('总体审核另有一般流程和条件例外缺口','总体审核另有P2流程细节及P3可选内容') for line in lines]
    if completion:
        lines[2]='**结论：专项P1／P2及原清单的P3缺口均有直接题句覆盖；相关流程任务也已完成。以下保留基线判断，并另列落实证据，不声称覆盖所有真实考题。**'
        lines[4]=f'专项审核基线为299题、1,507个题句；当前为{v["current_questions"]}题、{v["current_statements"]:,}个题句。原188行映射及基线状态保留，最终落实见[完成记录](REMAINING.md)。'
        lines=[line.replace('P1/P2已补；P3按下列明细保留','已落实，见下列逐项证据').replace('P3可选，保留','已落实，见下列逐项证据') for line in lines]
        lines=[('全部专项缺口已按下列证据落实。总体清单与专项内容重叠，不能相加计算独立考点数。' if line.startswith('P1/P2专项缺口已落实；') else line) for line in lines]
        lines=[('保留限制：18日重新下载条例以外的42个双语PDF版本及核对FAQ正文，均与归档一致；条例官网仍受客户端检查限制，未确认最新版本。未对全部未变旧题重新盲答。部分已补题后来扩写替换，题号关系和旧题快照见[最终记录](REMAINING.md)。' if line.startswith('保留限制：') else line) for line in lines]
    return '\n'.join(lines)

if __name__ == '__main__':
    data = json.loads((HERE / 'terms-and-roles.json').read_text(encoding='utf8'))
    result = validate(data)
    expected = render(data, result)
    target = HERE / 'TERMS-AND-ROLES.md'
    if '--check' in sys.argv:
        assert target.read_text(encoding='utf8') == expected, 'Generated report differs'
    else:
        target.write_text(expected, encoding='utf8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['implementation','p1_implementation','remaining_implementation']}, ensure_ascii=False))
