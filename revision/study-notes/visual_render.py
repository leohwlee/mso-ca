"""Accessible, offline learning figures; all language content remains selectable text."""

def render(panel, pair):
    def para(v, cls=''):
        return '<p'+(' class="'+cls+'"' if cls else '')+'>'+pair(v)+'</p>'
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
            out+='<li class="decision-node"><div class="decision-condition"><span class="decision-number" aria-hidden="true">'+str(i+1)+'</span>'+pair(node['test'])+'</div><div class="decision-outcome"><b class="branch-label">'+pair(node.get('yes_label',dict(tc='是',en='YES')))+'</b>'+pair(node['yes'])+'</div><div class="decision-continue"><b>'+pair(node.get('no_label',dict(tc='否 ↓ 繼續',en='NO ↓ Continue')))+'</b>'+('<div>'+pair(node['no'])+'</div>' if node.get('no') else '')+'</div></li>'
        out+='</ol>'
        if panel.get('end'):out+=para(panel['end'],'decision-end')
    elif kind=='logic':
        out+='<div class="logic-group"><div class="logic-operator">'+pair(panel['operator'])+'</div><ul>'+''.join('<li>'+pair(v)+'</li>' for v in panel['items'])+'</ul></div>'
    elif kind=='packet':
        for group in panel['groups']:
            out+='<div class="data-packet"><h4>'+pair(group['title'])+'</h4><div class="logic-group"><div class="logic-operator">'+pair(group['operator'])+'</div><ul>'+''.join('<li>'+pair(v)+'</li>' for v in group['items'])+'</ul></div>'+para(group['note'],'path-note')+'</div>'
    elif kind=='formula':
        for row in panel['formulae']:
            out+='<div class="penalty-formula"><h4>'+pair(row['label'])+'</h4>'+para(row['expression'],'formula-expression')+para(row['note'])+'</div>'
    else:
        raise AssertionError(kind)
    return out
