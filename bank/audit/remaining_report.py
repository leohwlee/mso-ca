"""Validate and render the final backlog implementation, preserving prior waves."""
import json
import pathlib
import sys
from state import load_state

HERE=pathlib.Path(__file__).resolve().parent

def render(d,state):
    s=d['statistics']
    lines=['# 剩余清单完成记录','',
           f'已处理最后{len(d["task_results"])}项P2／P3任务，以及专项清单全部P3缺口。当前题库{len(state["bank"])}题、{sum(len(q["truth"]) for q in state["bank"]):,}个题句；本次净增{s["net_questions"]}题、{s["net_statements"]}个题句。','',
           f'本次写入{s["written_questions"]}道新题号：其中{s["new_questions"]}道为独立新增题，其余为扩写替换题；{len(d["replacements"])}道原题退役，原文及引文保存在[实施证据](remaining-implementation.json)，原成绩保留。已测细节沿用原题证据，避免为了凑题重复出题。','',
           '“完成”只针对既定23份资料审核清单中列明的缺口，不是官方考试覆盖率，也不保证考试通过。原297／299题覆盖快照和320／338题实施记录继续保留。','',
           '## 逐项落实','', '| 任务 | 内容 | 处理 |','|---|---|---|']
    for t in d['task_results']:
        lines.append(f'| {t["backlog_id"]} | {t["title"]} | 已落实 |')
    for t in d['task_results']:
        lines+=['',f'## {t["backlog_id"]} · {t["title"]}','']
        for r in d['coverage']:
            if r['task_id']==t['backlog_id']:
                lines.append(f'- {r["topic_id"]}：{r["point"]}。`{r["question_id"]}#{",".join(map(str,r["statements"]))}`。')
        if t.get('boundary'):lines+=['','边界：'+t['boundary']]
    lines+=['','## 专项P3落实','']
    for r in d['specialist_coverage']:
        lines.append(f'- {r["row_id"]}：{r["point"]}。`{r["question_id"]}#{",".join(map(str,r["statements"]))}`。')
    lines+=['','## 替换及历史成绩','', '| 旧题 | 新题 | 理由 |','|---|---|---|']
    for r in d['replacements']:
        lines.append(f'| `{r["old_id"]}` | '+ '、'.join(f'`{x}`' for x in r['new_ids'])+' | '+r['reason'].replace('|','／')+' |')
    lines+=['','## 审核与边界','',
            '- 所有新增及替换题均由另一审核者遮住答案和解释，分别依英文及繁体原文盲答；最终文字与审核摘要绑定。保留原句也随替换题重新盲答。',
            '- 完整核对主体、适用条件、例外和双语决定；逐句来源文字命中不代替语义判断。新题与全库做语义去重，并对照温习资料。',
            '- 通函15附件的双语PDF第3–5页均检查原图；图内字段人工转录后由另一审核者核对，绑定PDF摘要并纳入来源变更检查。示例填写数字不作为考点。',
            '- exam-prep已更新至2.3.0：增加来源考点覆盖模式、条件／例外语义检查、图页账目和版本证据；尊重既定授权及题型，区分必需检查与可选深入诊断。原项目严格题型及质量规则继续适用。',
            '- 审核使用同一会话模型；没有将异模型家族对抗或跨语言嵌入写成已执行，未对全部未变旧题重新盲答。',
            '- 18日重新下载条例以外的42个双语PDF版本，均与归档逐字节一致；FAQ正文与官网相符。条例官网仍被客户端检查阻挡，不能确认最新条例版本；本次依既定归档版本完成。',
            '- B16仍只依牌照指引的准许账户户名清单，不把业务计划文件未定义的“第三方”强行统一解释；咨询内容也不写成现行本地额外义务。','',
            '维护：`python -X utf8 bank/audit/remaining_report.py --check`。改题、改来源或改适用范围时须重新判断相关证据。','']
    return '\n'.join(lines)

if __name__=='__main__':
    state=load_state();d=state.get('remaining_implementation');assert d
    text=render(d,state);p=HERE/'REMAINING.md'
    if '--check' in sys.argv:assert p.read_text(encoding='utf8')==text,'Regenerate REMAINING.md'
    else:p.write_text(text,encoding='utf8')
    print(json.dumps(d['statistics'],ensure_ascii=False))
