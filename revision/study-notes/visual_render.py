"""Accessible, offline learning figures; all language content remains selectable text."""

def render(panel, pair):
    def para(v, cls=''):
        return '<p'+(' class="'+cls+'"' if cls else '')+'>'+pair(v)+'</p>'
    def logic_item(value):
        if 'tc' in value:
            return pair(value)
        # The whole contained group is ONE option in the surrounding AND/OR list.
        return '<div class="nested-logic">'+para(value['lead'],'nested-lead')+'<div class="nested-members">'+''.join(('<b class="nested-join">AND</b>' if i else '')+'<div>'+pair(item)+'</div>' for i,item in enumerate(value['all']))+'</div></div>'
    def paths(rows):
        out='<div class="visual-paths">'
        for row in rows:
            out+='<div class="visual-path"><h4>'+pair(row['label'])+'</h4><div class="path-track">'
            for i, node in enumerate(row['nodes']):
                if i:
                    symbol=row.get('symbols',['→']*len(row['edges']))[i-1]
                    out+='<span class="path-edge'+(' comparison-edge' if symbol=='≠' else '')+'">'+pair(row['edges'][i-1])+'<span aria-hidden="true"> '+symbol+' </span></span>'
                out+='<div class="path-node">'+pair(node)+'</div>'
            out+='</div>'+para(row['note'],'path-note')+'</div>'
        return out+'</div>'
    kind=panel['kind']
    out=para(panel['intro'],'visual-intro') if panel.get('intro') else ''
    if kind=='paths':
        out+=paths(panel['paths'])
    elif kind=='relationships':
        out+='<div class="relation-map">'
        for row in panel['relations']:
            out+='<div class="relation-row"><div class="relation-entity">'+pair(row['from'])+'</div><div class="relation-verb">'+pair(row['verb'])+'<span aria-hidden="true"> → </span></div><div class="relation-entity">'+pair(row['to'])+'</div>'+para(row['note'],'relation-note')+'</div>'
        out+='</div>'
    elif kind=='clocks':
        out+='<div class="independent-clocks">'
        for row in panel['clocks']:
            out+='<div class="clock-row"><h4>'+pair(row['label'])+'</h4><div class="clock-origin"><b class="clock-label">'+pair(dict(tc='起算／對照事件',en='Starting / reference event'))+'</b>'+pair(row['start'])+'</div><div class="clock-duration"><b class="clock-label">'+pair(dict(tc='時間要求',en='Timing requirement'))+'</b>'+pair(row['duration'])+'</div>'+para(row['note'],'clock-note')+'</div>'
        out+='</div>'
    elif kind=='decision':
        out+='<ol class="decision-tree">'
        for i,node in enumerate(panel['nodes']):
            next_label=dict(tc=f'否 → 第{i+2}項',en=f'NO → step {i+2}')
            out+='<li class="decision-node"><div class="decision-condition"><span class="decision-number" aria-hidden="true">'+str(i+1)+'</span>'+pair(node['test'])+'</div><div class="decision-outcome"><b class="branch-label">'+pair(node.get('yes_label',dict(tc='是',en='YES')))+'</b>'+pair(node['yes'])+'</div><div class="decision-continue"><b>'+pair(node.get('no_label',next_label))+'</b>'+('<div>'+pair(node['no'])+'</div>' if node.get('no') else '')+'</div></li>'
        out+='</ol>'
        if panel.get('end'):out+=para(panel['end'],'decision-end')
    elif kind=='trigger-cases':
        out+='<div class="trigger-cases">'
        for row in panel['cases']:
            out+='<div class="trigger-case'+(' cross-cutting' if row.get('cross_cutting') else '')+'"><h4>'+pair(row['label'])+'</h4><div class="trigger-condition">'+pair(row['condition'])+'</div>'+para(row['action'],'trigger-action')+'</div>'
        out+='</div>'
        if panel.get('end'):out+=para(panel['end'],'memory-note')
    elif kind=='logic':
        out+='<div class="logic-group"><div class="logic-operator">'+pair(panel['operator'])+'</div><ul>'+''.join('<li>'+logic_item(v)+'</li>' for v in panel['items'])+'</ul></div>'
    elif kind=='packet':
        for group in panel['groups']:
            out+='<div class="data-packet"><h4>'+pair(group['title'])+'</h4><div class="logic-group"><div class="logic-operator">'+pair(group['operator'])+'</div><ul>'+''.join('<li>'+logic_item(v)+'</li>' for v in group['items'])+'</ul></div>'+para(group['note'],'path-note')+'</div>'
    elif kind=='formula':
        for row in panel['formulae']:
            out+='<div class="penalty-formula"><h4>'+pair(row['label'])+'</h4>'+para(row['expression'],'formula-expression')+para(row['note'])+'</div>'
    elif kind=='thresholds':
        # Ordinal amount line: position shows order only; the marker shows whether equality counts.
        ticks={t['key']:t for t in panel['ticks']}
        def track(lane):
            at=ticks[lane['tick']]['at']
            guides=''.join('<span class="lane-guide" style="--at:'+str(t['at'])+'%"></span>' for t in panel['ticks'])
            return '<div class="lane-track" aria-hidden="true">'+guides+'<span class="lane-bar'+(' exclusion' if lane.get('exclusion') else '')+'" style="--at:'+str(at)+'%"></span><span class="lane-marker '+('inclusive' if lane['inclusive'] else 'exclusive')+'" style="--at:'+str(at)+'%"></span><span class="lane-value" style="--at:'+str(at)+'%">'+('≥ ' if lane['inclusive'] else '> ')+ticks[lane['tick']]['label']['en']+'</span></div>'
        out+='<div class="threshold-legend"><span><i class="lane-marker inclusive" aria-hidden="true"></i>'+pair(dict(tc='實心：等於門檻亦適用（≥）',en='Filled: applies at exactly the amount (≥)'))+'</span><span><i class="lane-marker exclusive" aria-hidden="true"></i>'+pair(dict(tc='空心：須超過門檻（>）',en='Hollow: must exceed the amount (>)'))+'</span></div>'
        out+='<div class="threshold-chart"><div class="threshold-axis" aria-hidden="true"><span></span><div class="axis-track">'+''.join('<b class="axis-tick" style="--at:'+str(t['at'])+'%">'+pair(t['label'])+'</b>' for t in panel['ticks'])+'</div></div>'
        for group in panel['lane_groups']:
            out+='<div class="threshold-group"><h4>'+pair(group['title'])+'</h4>'
            for lane in group['lanes']:
                out+='<div class="threshold-lane"><div class="lane-label"><p class="lane-name">'+pair(lane['label'])+'</p><p class="lane-boundary">'+pair(lane['boundary'])+'</p></div>'+track(lane)+'<p class="lane-trigger"><b>'+pair(dict(tc='觸發',en='Triggers'))+'</b>'+pair(lane['trigger'])+'</p>'+para(lane['detail'],'lane-detail')+'</div>'
            out+='</div>'
        out+='</div>'+para(panel['scale_note'],'threshold-scale-note')
    elif kind=='deadlines':
        # Every row keeps its own starting event; segment lengths illustrate direction, never a shared time scale.
        def edge(at):return ' edge-left' if at<18 else ' edge-right' if at>82 else ''
        def track(row):
            out='<div class="deadline-track" aria-hidden="true">'
            for seg in row['segments']:
                centre=(seg['from']+seg['to'])/2
                out+='<span class="deadline-seg '+seg['kind']+'" style="--from:'+str(seg['from'])+'%;--to:'+str(seg['to'])+'%"></span>'
                if seg.get('label'):out+='<b class="deadline-seg-label '+seg['kind']+edge(centre)+'" style="--at:'+str(centre)+'%">'+pair(seg['label'])+'</b>'
            return out+'<span class="deadline-anchor" style="--at:'+str(row['at'])+'%"></span><em class="deadline-anchor-label'+edge(row['at'])+'" style="--at:'+str(row['at'])+'%">'+pair(row['anchor'])+'</em></div>'
        def rows(items):
            return ''.join('<div class="deadline-row"><div class="deadline-label"><h4>'+pair(r['label'])+'</h4><p class="deadline-start"><b>'+pair(dict(tc='起算',en='Starts'))+'</b>'+pair(r['start'])+'</p><p class="deadline-rule">'+pair(r['duration'])+'</p></div>'+track(r)+para(r['note'],'deadline-note')+'</div>' for r in items)
        out+='<div class="deadline-legend"><span><i class="deadline-key window" aria-hidden="true"></i>'+pair(dict(tc='實線：須在此期間辦理',en='Solid: act within this period'))+'</span><span><i class="deadline-key late" aria-hidden="true"></i>'+pair(dict(tc='斜紋：太遲或不可',en='Hatched: too late or not allowed'))+'</span><span><i class="deadline-key anchor" aria-hidden="true"></i>'+pair(dict(tc='圓圈：起算事件',en='Ring: starting event'))+'</span></div>'
        if panel.get('deadline_groups'):
            out+=''.join('<div class="deadline-group"><h4 class="deadline-group-title">'+pair(g['title'])+'</h4><div class="deadline-chart">'+rows(g['rows'])+'</div></div>' for g in panel['deadline_groups'])
        else:out+='<div class="deadline-chart">'+rows(panel['deadlines'])+'</div>'
        out+=para(panel['scale_note'],'threshold-scale-note')
    elif kind=='checklist':
        # A source list with its length made explicit, so a candidate can count the items.
        def group(title,items,operator=None):
            head='<p class="checklist-head"><b class="checklist-count">'+str(len(items))+'</b>'+(pair(title) if title else '')+(('<span class="checklist-operator">'+pair(operator)+'</span>') if operator else '')+'</p>'
            return '<div class="checklist-group">'+head+'<ol class="checklist-items'+(' long' if len(items)>=8 else '')+'">'+''.join('<li>'+pair(x)+'</li>' for x in items)+'</ol></div>'
        out+='<div class="checklist">'
        if panel.get('groups'):out+=''.join(group(g['title'],g['items'],g.get('operator')) for g in panel['groups'])
        else:out+=group(panel.get('lead'),panel['items'],panel.get('operator'))
        if panel.get('confuse'):out+='<p class="checklist-confuse"><b>'+pair(dict(tc='易混項',en='Easily confused'))+'</b>'+''.join('<span>'+pair(x)+'</span>' for x in panel['confuse'])+'</p>'
        out+='</div>'
    elif kind=='id-columns':
        def numbered(title,items,cls=''):
            return '<p class="id-step"><b class="id-count">'+str(len(items))+'</b>'+pair(title)+'</p><ol class="id-list'+cls+'">'+''.join('<li>'+pair(x)+'</li>' for x in items)+'</ol>'
        out+='<div class="id-columns">'
        for col in panel['columns']:
            out+='<section class="id-column"><h4>'+pair(col['title'])+'<span class="id-para">'+pair(col['paras'])+'</span></h4>'
            out+=numbered(dict(tc='最低限度收集',en='Collect at least'),col['collect'])
            out+=numbered(dict(tc='須核實',en='Verify'),col['verify'],' verify')
            out+=numbered(dict(tc='核實來源例子',en='Example sources'),col['sources'],' sources')
            out+=para(col['note'],'id-note')+'</section>'
        out+='</div>'
    else:
        raise AssertionError(kind)
    return out
