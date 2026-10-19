"""Source-authored manuscript helpers. No question-bank dependency."""

def p(tc, en):
    return {'tc': tc, 'en': en}


def ref(doc, tc, en, anchor):
    return {'doc': doc, 'locator': p(tc, en), 'anchor': anchor}


def g(paragraphs, anchor):
    main, sep, foot = paragraphs.partition('及註')
    tc = '第' + main + '段' + ('及註' + foot if sep else '')
    en = '¶' + main.replace('、', ', ') + ('; footnotes ' + foot if sep else '')
    return ref('03', tc, en, anchor)


def block(tc, en, points, refs, kind='list'):
    return {'title': p(tc, en), 'kind': kind, 'points': [p(*x) for x in points], 'refs': refs}


def section(key, tc, en, blocks):
    return {'id': key, 'title': p(tc, en), 'blocks': blocks}
