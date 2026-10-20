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
    else:
        raise AssertionError(kind)
    return out
