"""Validate and render the additive P1 process/condition/exception wave."""
import json
import pathlib
import sys
from state import load_state, emit

HERE = pathlib.Path(__file__).resolve().parent

def render(d):
    added = set(d['added_question_ids'])
    lines = ['# P1流程、条件及例外补题', '',
             f'本轮落实剩余{len(d["task_results"])}项P1任务，新增{d["statistics"]["new_questions"]}道组合题、{d["statistics"]["new_statements"]}个题句；当时题库由{d["baseline"]["questions"]}题增至{d["current"]["questions"]}题、{d["current"]["statements"]:,}个题句。后续更新另见[最终完成记录](REMAINING.md)。', '',
             '任务来自[总体覆盖清单](README.md)。先核对320题的直接题句，沿用已覆盖部分，只对剩余内容补题。原297题及299题审核基线均保留，不能把不同来源的映射行数当成独立考点或考试覆盖率。', '',
             '[逐句快照、双语盲答与实施证据](p1-implementation.json) · [专项名词及职责审核](TERMS-AND-ROLES.md)', '',
             '## 逐项落实', '',
             '| 任务 | 内容 | 状态 |', '|---|---|---|']
    for task in d['task_results']:
        lines.append(f'| {task["backlog_id"]} P1 | {task["title"]} | 已完成 |')
    for task in d['task_results']:
        lines += ['', f'## {task["backlog_id"]} · {task["title"]}', '']
        grouped = {}
        for row in d['coverage']:
            if row['task_id'] != task['backlog_id']:
                continue
            key = row['point']
            qid = row['question_id']
            ref = '`' + qid + '#' + ','.join(map(str,row['statements'])) + '`'
            item = grouped.setdefault(key, dict(topics=set(),refs=set()))
            item['topics'].add(row['topic_id'])
            item['refs'].add(('新增' if qid in added else '沿用现题') + ref)
        for point, item in grouped.items():
            lines.append(f'- {"、".join(sorted(item["topics"]))}：{point}。' + '；'.join(sorted(item['refs'])) + '。')
        if task.get('boundary'):
            lines += ['', '边界：' + task['boundary']]
    lines += ['', '## 审核与限制', '',
              '- 新题先由另一审核者遮住答案及解释，分别按英文及繁体原文判定；所有最终题句与审核快照一致，歧义及差异均已处理。',
              '- 将新题与全库及同批题做语义去重，并与温习资料逐项对照；引文命中只是来源核验，不能代替条件、主体和例外的实质判断。',
              '- 检查组合选项、逐句引文、双语术语和整库质量规则；原有320题内容及答案保持不变，旧作答记录无需迁移。',
              '- 审核者使用同一会话模型；没有把未做的异模型对抗或跨语言嵌入检查写成已完成。未对全部旧题重做盲答。',
              '- 本轮仍按归档23份官方资料及已定来源关系出题。沿用上一轮来源核验日期及条例官网访问限制，没有声称全部资料已重新确认最新版本。',
              '- 本报告保留P1轮次的审核结论；其后P2／P3及部分扩写替换另见最终完成记录。本报告的“完成”针对列明的任务，不保证覆盖真实考试的全部内容。', '',
              '维护：运行 `python -X utf8 bank/audit/p1_report.py --check`；题句、来源或覆盖判断改变时需重新审核，不能只更新摘要值。', '']
    return '\n'.join(lines)

if __name__ == '__main__':
    state = load_state()
    d = state.get('p1_implementation')
    assert d, 'No verified P1 implementation record'
    emit(HERE / 'P1-PROCESSES.md', render(d), '--check' in sys.argv)
    print(json.dumps(dict(tasks=len(d['task_results']), **d['statistics']), ensure_ascii=False))
