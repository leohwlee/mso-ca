# Figures for the Guideline Chapter 6 page: the three laws side by side, the
# sanctions database, whom to screen, and what to do with a possible match.
import re
from ui import *
from bl_core import tokens as _tokens
from bl_figs import lines_down


# ---------------------------------------------------------------- local line breaking
# The shared wrap() may split '第5條' across lines or leave '（' / '《' at a line end.
# These figures use a local variant so the shared helpers stay untouched.
NOEND = set('（《「『【')
GLUE = re.compile(r'第[0-9A-Za-z()至、.]+[條章段號問款]|《[^《》]{1,24}》')


def tokens6(text):
    out, i = [], 0
    for m in GLUE.finditer(text):
        out += _tokens(text[i:m.start()])
        out.append(m.group(0))
        i = m.end()
    return out + _tokens(text[i:])


def _wrap6(text, width_px, size):
    """Like the shared wrap(), but a line never starts with closing punctuation or ends with an
    opening bracket: tokens are carried over to the next line instead of overflowing."""
    lines, cur = [], []

    def width(ts):
        return sum(w for _, w in ts)

    def flush(ts):
        line = ''.join(t for t, _ in ts).strip()
        if line:
            lines.append(line)

    toks = []
    for tok in tokens6(text):   # a glued run too wide for the measure falls back to single characters
        toks += _tokens(tok) if len(tok) > 1 and tw(tok, size) > width_px else [tok]
    for tok in toks:
        w = tw(tok, size)
        if tok == ' ':
            if cur:
                cur.append((tok, w))
            continue
        if not cur or width(cur) + w <= width_px:
            cur.append((tok, w))
            continue
        carry = [(tok, w)]
        if tok in NOSTART:
            # pull back until the carried group starts with a token that may start a line
            while len(cur) > 1 and carry[0][0] in NOSTART:
                carry.insert(0, cur.pop())
        while len(cur) > 1 and (cur[-1][0] == ' ' or cur[-1][0][-1] in NOEND):
            t = cur.pop()
            if t[0] != ' ':
                carry.insert(0, t)
        if carry[0][0] in NOSTART:      # nothing could be pulled back: let it overhang
            cur += carry
            continue
        flush(cur)
        cur = carry
    flush(cur)
    return lines


def wrap6(text, width_px, size):
    """_wrap6, then, if the last line is a short orphan, narrow the measure as far as the line
    count allows so the lines come out even."""
    lines = _wrap6(text, width_px, size)
    if len(lines) < 2 or tw(lines[-1], size) >= 0.4 * width_px:
        return lines
    lo, hi = width_px * 0.6, width_px
    for _ in range(12):
        mid = (lo + hi) / 2
        if len(_wrap6(text, mid, size)) == len(lines):
            hi = mid
        else:
            lo = mid
    return _wrap6(text, hi, size)


class C6(Card):
    """Card whose lines are broken with wrap6; a title or body entry may be a list of explicit lines."""

    def __init__(self, x, w, title, body=None, kind='plain', cite=None, href=None,
                 size=11.5, tsize=12.5, minh=0, answer=False):
        def flat(pair):
            return tuple(''.join(t) if isinstance(t, list) else t for t in pair) if pair else pair
        super().__init__(x, w, flat(title), flat(body), kind, cite, href, size, tsize, minh, answer)
        size, tsize = size * FS, tsize * FS
        inner = w - 24
        for i, v in enumerate(('en', 'tc')):
            tl = (title[i] if isinstance(title[i], list) else wrap6(title[i], inner, tsize)) if title and title[i] else []
            bl = (body[i] if isinstance(body[i], list) else wrap6(body[i], inner, size)) if body and body[i] else []
            tcls = 't-inv t-b' if kind == 'stop' else ('t t-b t-faint' if kind == 'faint' else 't t-b')
            bcls = 't-inv' if kind == 'stop' else ('t t-faint' if kind == 'faint' else 't')
            self.seg[v] = [(l, tcls, tsize) for l in tl] + [(l, bcls, size) for l in bl]
        self.seg['both'] = self.seg['en'] + self.seg['tc']
        self.h = max(minh, sum(s * LH for _, _, s in self.seg[lay()]) + 16 + (CS * LH if cite else 0))


def heads(cols, y, size=13):
    """Bold column headings. cols: list of (cx, width, (en, tc)); en or tc may be a list of
    explicit lines. Returns (svg, height)."""
    out, nmax = [], 0
    for cx, w, (en, tc) in cols:
        le = en if isinstance(en, list) else wrap6(en, w, size * FS)
        lt = tc if isinstance(tc, list) else wrap6(tc, w, size * FS)
        n = {'en': len(le), 'tc': len(lt), 'both': len(le) + len(lt)}[lay()]
        nmax = max(nmax, n)
        out.append(lines_down(cx, y, le, lt, 't t-b', size))
    return ''.join(out), nmax * size * FS * 1.3 + 6


def even_rows(rows):
    """Give every card in a row the row's tallest height, so the rows line up as a grid."""
    for row in rows:
        h = max(n.h for n in row)
        for n in row:
            n.h = h


def mlabel6(x, y, en, tc, anchor='middle', step=17):
    """mlabel with a larger step between the stacked English and Chinese lines, so a descender
    in the English word does not touch the Chinese character below it."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        n = len(ls)
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (n - 1 - i) * step:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


# ---------------------------------------------------------------- 1. three laws
def fig_regimes():
    W = 1000
    X, CW = (16, 350, 684), 300
    hsvg, hh = heads([(X[i] + CW / 2, CW, t) for i, t in enumerate((
        (["Terrorism", "UNATMO, Cap. 575"], ["恐怖主義", "《聯合國（反恐怖主義措施）條例》", "（第575章）"]),
        (["UN sanctions", "UNSO, Cap. 537"], ["聯合國制裁", "《聯合國制裁條例》", "（第537章）"]),
        (["Proliferation", "WMD(CPS)O, Cap. 526"], ["擴散", "《大規模毀滅武器（提供服務的管制）條例》", "（第526章）"])))], 8, 12.5)
    a1 = C6(X[0], CW, ("The UN decisions behind it", "背後的聯合國決定"),
            ("UNSCR 1373 (2001) on preventing terrorist acts and UNSCR 2178 (2014) on travel for terrorist acts or training; also certain conventions and FATF Recommendations",
             "安理會第1373 (2001)號決議（防止恐怖主義行為）及第2178 (2014)號決議（以恐怖主義行為或培訓為目的的旅程）；以及若干多邊公約及特別組織的建議"),
            'faint', "¶6.3")
    b1 = C6(X[1], CW, ("The UN decisions behind it", "背後的聯合國決定"),
            ("Sanctions decided by the UNSC, targeted financial sanctions included. Its regulations specific to the DPRK and Iran are part of the counter-PF regime",
             "聯合國安理會所決定的制裁，包括針對性金融制裁。該條例下針對朝鮮及伊朗訂立的規例，屬打擊擴散資金籌集制度的一部分"),
            'faint', "¶6.7, 6.10")
    c1 = C6(X[2], CW, ("Where it sits", "定位"),
            ("Part of Hong Kong's counter-PF legislation, alongside the UNSO regulations specific to the DPRK and Iran",
             "香港打擊擴散資金籌集的法例之一，與《聯合國制裁條例》下針對朝鮮及伊朗的規例並列"),
            'faint', "¶6.10")
    a2 = C6(X[0], CW, ("Who names the target", "誰指明對象"),
            ("Where a UNSC Committee has designated, the Chief Executive may specify by Gazette notice (s.4). The Chief Executive may also apply to the Court of First Instance for an order, which is also gazetted (s.5). The Secretary for Security may freeze suspected terrorist property (s.6)",
             "如安理會委員會已作出指定，行政長官可在憲報刊登公告指明（第4條）。行政長官亦可向原訟法庭申請命令，命令亦會刊憲（第5條）。保安局局長可凍結懷疑是恐怖分子的財產（第6條）"),
            'may', "¶6.4–6.5")
    b2 = C6(X[1], CW, ("Who names the target", "誰指明對象"),
            ("Targets include persons and entities designated by the UNSC or its Committees. The Chief Executive makes the regulations; designated persons and entities are specified by notice in the Gazette or on the Commerce and Economic Development Bureau website",
             "對象包括聯合國安理會或其委員會指認的人士及實體。行政長官訂立規例；被指認的個人及實體透過在憲報或商務及經濟發展局網站刊登的公告指明"),
            'may', "¶6.7")
    c2 = C6(X[2], CW, ("Your belief, not a list", "準則在於你的判斷，而非名單"),
            ("The ban applies where you believe or suspect, on reasonable grounds, that a service may be connected to PF",
             "如你基於合理理由相信或懷疑某項服務可能與擴散資金籌集有關，禁令即適用"),
            'plain', "¶6.10")
    a3 = C6(X[0], CW, ("What you must not do", "你不可做的事"),
            ("Provide or collect property for terrorist acts (s.7); make property or financial services available to terrorists or associates (s.8); deal with specified terrorist property (s.8A); fund travel for terrorist acts or training (s.11L)",
             "提供或籌集財產以作出恐怖主義行為（第7條）；向恐怖分子或與恐怖分子有聯繫者提供財產或金融服務（第8條）；處理指明的恐怖分子財產（第8A條）；資助為恐怖主義行為或培訓而進行的旅程（第11L條）"),
            'must', "¶6.5")
    b3 = C6(X[1], CW, ("What you must not do", "你不可做的事"),
            ("Make funds, other financial assets or economic resources available, directly or indirectly, to or for the benefit of designated persons or entities, anyone acting on their behalf or at their direction or owned or controlled by them, or entities owned by any of these; or deal with funds belonging to, or owned or controlled by, them",
             "直接或間接向被指認的個人或實體、代表其或按其指示行事或由其擁有或控制者，或上述者擁有的實體，提供資金、其他財務資產或經濟資源，或為其利益而提供；或處理屬於他們或由他們擁有或控制的該等資金"),
            'must', "¶6.7")
    c3 = C6(X[2], CW, ("What you must not do", "你不可做的事"),
            ("Provide any such service. 'Services' is widely defined: lending money and any other financial assistance are included",
             "提供任何該等服務。「提供服務」的定義廣泛，包括借出款項或以其他方式提供金融資助"),
            'must', "¶6.10")
    a4 = C6(X[0], CW, ("The way round it: a licence", "例外：特許"),
            ("The Secretary for Security can license unfreezing, and payments such as reasonable living or legal expenses or sums due under the Employment Ordinance. Write to the Security Bureau",
             "保安局局長可批予特許，准許解凍財產或支付款項，例如合理生活開支／法律開支，或根據《僱傭條例》需要給予的費用。向保安局提出書面申請"),
            'may', "¶6.6")
    b4 = C6(X[1], CW, ("The way round it: a licence", "例外：特許"),
            ("The Chief Executive may grant one in circumstances the regulation specifies. Write to the Commerce and Economic Development Bureau",
             "行政長官可按有關規例在指明情況下批予特許。向商務及經濟發展局提出書面申請"),
            'may', "¶6.8")
    c4 = C6(X[2], CW, ("Licence: none described in the Guideline", "特許：指引沒有提及"), None, 'faint', "¶6.10")
    rows = [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3], [a4, b4, c4]]
    # c2 keeps its natural height (place() centres it on the row midline, so the arrows above and
    # below stay equal); c4 has nothing below it, so it keeps its natural height, top-aligned.
    even_rows([[a1, b1, c1], [a2, b2], [a3, b3, c3], [a4, b4]])
    H = place([(r, 34) for r in rows[:-1]] + [(rows[-1], 0)], y0=8 + hh + 8)
    c4.y = a4.y
    b = [hsvg] + [n.render() for r in rows for n in r]
    m = 'g6r'
    for col in zip(*rows):
        for p, q in zip(col, col[1:]):
            b.append(edge([p.bottom, q.top], mid=m))
    aria = ("Three laws compared column by column. UNATMO: behind it are UNSCR 1373 and 2178; where a UNSC Committee has designated, the Chief Executive may specify by Gazette notice, and may also apply for a Court of First Instance order, and the Secretary for Security may freeze; sections 7, 8, 8A and 11L set out what you must not do; the Secretary for Security can license exceptions, and you write to the Security Bureau. UNSO: behind it are UNSC sanctions including those on the DPRK and Iran; the UNSC or its Committees designate and names are specified by notice in the Gazette or on the Commerce and Economic Development Bureau website; you must not make funds available to designated persons, those acting for them or owned or controlled by them, or deal with their funds; the Chief Executive may grant a licence, and you write to that Bureau. WMD(CPS)O: part of the counter-PF legislation; the ban applies where you believe or suspect on reasonable grounds that a service may be connected to PF; you must not provide such a service, lending money included; the Guideline describes no licence.",
            "三條法例逐欄比較。《聯合國（反恐怖主義措施）條例》：背後是安理會第1373及2178號決議；如安理會委員會已作出指定，行政長官可在憲報公告指明，亦可申請原訟法庭命令指明，保安局局長可凍結財產；第7、8、8A及11L條訂明你不可做的事；保安局局長可批予特許，須向保安局提出書面申請。《聯合國制裁條例》：背後是安理會的制裁，包括針對朝鮮及伊朗的制裁；由安理會或其委員會指認，並在憲報或商務及經濟發展局網站公告指明；你不可向被指認人士、代表其行事或由其擁有或控制者提供資金，或處理其資金；行政長官可批予特許，應向該局提出書面申請。《大規模毀滅武器（提供服務的管制）條例》：屬打擊擴散資金籌集的法例；如你基於合理理由相信或懷疑服務可能與擴散資金籌集有關，禁令即適用；你不可提供該等服務，包括借出款項；指引沒有提及特許。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


REG_KEY = legend([('faint', ("background: the UN decision behind the law, or where the Guideline is silent", "背景：法例背後的聯合國決定，或指引沒有提及之處")),
                  ('may', ("a power the Government holds: naming, freezing, licensing", "政府持有的權力：指明、凍結、批予特許")),
                  ('', ("the test lies with you", "由你自行判斷")),
                  ('must', ("what you must not do", "你不可做的事"))])


# ---------------------------------------------------------------- 2. the database
def fig_db():
    W = 1000
    hsvg, hh = heads([(161, 290, ("What should go in", "應收錄的名單")), (847, 274, ("Ways to hold it", "備存方式"))], 6, 12)
    i1 = C6(16, 290, ("Lists published in the Gazette or on the Commerce and Economic Development Bureau website", ["在憲報或商務及經濟", "發展局網站刊登的名單"]), None, 'must', "¶6.15(a)")
    i2 = C6(16, 290, ("Lists the Commissioner draws to your attention", "關長不時告知的名單"), None, 'must', "¶6.15(b)")
    i3 = C6(16, 290, ("New UNSC listings, as soon as practicable", "安理會新列名：盡快加入"),
            ("Even if Hong Kong has not yet implemented the sanctions by legislation", ["在切實可行範圍內盡快；即使有關", "制裁尚未透過香港法例實施"]), 'must', "¶6.14")
    db = C6(356, 290, ("Your database of terrorists and designated parties", "恐怖分子及被指認各方的數據庫"),
            ("It consolidates every list made known to you, is updated in a timely way whenever there are changes, and is easy for relevant staff to reach",
             "綜合你所知的各種名單；資料有變即及時更新；讓相關職員易於查閱"), 'must', "¶6.13, 6.15")
    o1 = C6(710, 274, ("Keep it yourself", "自行備存"), None, 'plain', "¶6.13")
    o2 = C6(710, 274, ("Subscribe to a third-party provider's database", "登記使用第三者服務供應商的數據庫"),
            ("Take appropriate measures, such as periodic sample testing, to make sure it is complete and accurate",
             ["並採取適當措施（例如定期", "抽樣測試），確保數據庫完整而準確"]), 'plain', "¶6.13")
    o3 = C6(710, 274, ("Let your overseas office keep it or run the screening", ["由在外地的辦事處備存", "數據庫或執行篩查"]),
            ("The ultimate responsibility stays with you", "最終責任仍由你承擔"), 'plain', "¶6.19")
    y0 = 6 + hh + 10
    hl = place([([i1], 22), ([i2], 22), ([i3], 0)], y0=y0)
    hr = place([([o1], 22), ([o2], 22), ([o3], 0)], y0=y0)
    Hc = max(hl, hr)
    db.y = y0 + (Hc - y0 - db.h) / 2
    scr = C6(356, 290, ("Used for every screening", "用於每次篩查"), ("See the next section: when, and whom", "見下一節：何時篩查，篩查誰"),
             'faint', "¶6.16", href="#g6-screening")
    scr.y = Hc + 40
    b = [hsvg] + [n.render() for n in (i1, i2, i3, db, o1, o2, o3, scr)]
    m = 'g6d'
    jx = 331
    for n in (i1, i2, i3):
        b.append(f'<polyline class="e" points="{n.x + n.w:.0f},{n.cy:.0f} {jx},{n.cy:.0f} {jx},{db.cy:.0f}"/>')
    b.append(edge([(jx, db.cy), db.left], mid=m))
    kx = 680
    for n in (o1, o2, o3):
        b.append(f'<polyline class="e e-dash" points="{db.x + db.w:.0f},{db.cy:.0f} {kx},{db.cy:.0f} {kx},{n.cy:.0f} {n.x:.0f},{n.cy:.0f}"/>')
    b.append(edge([db.bottom, scr.top], mid=m))
    aria = ("What feeds the sanctions database and how it may be held. Three inputs, all of which should go in: lists published in the Gazette or on the Commerce and Economic Development Bureau website; lists the Commissioner draws to your attention; and new UNSC listings, added as soon as practicable even if Hong Kong has not yet legislated. They feed one database that consolidates every list, is updated promptly and is easy for staff to reach. Alternatives for holding it: keep it yourself; subscribe to a third-party provider's database and take appropriate measures, such as periodic sample testing, to make sure it is complete and accurate; or let your overseas office keep it or run the screening, with the ultimate responsibility staying with you. The database is used for every screening.",
            "制裁數據庫的來源及備存方式。三項來源均應收錄：在憲報或商務及經濟發展局網站刊登的名單；關長不時告知的名單；以及安理會新列名，即使香港尚未立法亦應在切實可行範圍內盡快加入。三者匯入同一數據庫，數據庫應綜合各種名單、及時更新並讓職員易於查閱。可選用的備存方式：自行備存；登記使用第三者服務供應商的數據庫，並採取適當措施（例如定期抽樣測試），確保數據庫完整而準確；或由在外地的辦事處備存或執行篩查，但最終責任仍由你承擔。每次篩查均使用此數據庫。")
    return svg(W, scr.y + scr.h + 14, ''.join(b), aria, m, 860)


DB_KEY = legend([('must', ("a duty on you: what should go in, and the database you keep", "你的責任：應收錄的名單及你備存的數據庫")),
                 ('', ("a way to hold it: the dashed lines are alternatives", "備存方式：虛線表示可選用的方式")),
                 ('faint', ("covered in the next section", "見下一節"))])


# ---------------------------------------------------------------- 3. whom to screen
def fig_who():
    W = 1000
    hsvg, hh = heads([(500, 900, ("At the start of the relationship, and against every new or updated designation",
                                   "建立關係當時，以及每次有新增或更新的指認時"))], 6, 12.5)
    c = C6(16, 300, ("The customer", "客戶"), ("Whatever its risk rating", "不論其風險評級"), 'must', "¶6.16(a)–(b) · fn 58")
    bo = C6(350, 300, ("Every beneficial owner of the customer", "客戶的任何實益擁有人"),
            ("Leaving them out was a C&ED supervisory finding in 2023", "海關2023年的巡查發現曾有經營者遺漏"), 'must',
            ("¶6.16 · Circular 22 Nov 2023", "第6.16段 · 2023年11月22日通函"))
    cp = C6(684, 300, ("Connected parties and persons purporting to act on the customer's behalf (PPTAs)", "有關連者及看似代表客戶行事的人"),
            ("Screened on a risk-based approach. Who they are: see the Schedule 2 page", "按風險為本的方法篩查；誰屬此類，見附表2一頁"), 'plain', "¶6.17",
            href="#s2-measures")
    even_rows([[c, bo, cp]])
    y1 = 6 + hh + 10
    h1 = place([([c, bo, cp], 0)], y0=y1)
    h2svg, hh2 = heads([(500, 900, ("At a minimum, before executing a cross-border or cross-boundary wire transfer or remittance: all relevant parties",
                                     "執行跨境電傳轉帳或匯款交易前：最低限度篩查以下相關各方"))], h1 + 30, 12.5)
    X = (16, 218, 420, 622, 824)
    names = [("Originator", "匯款人"), ("Ordering institution", "匯款機構"), ("Intermediary institution", "中介機構"),
             ("Beneficiary institution", "收款機構"), ("Recipient", "收款人")]
    chain = [C6(x, 170, t, None, 'must', ("FAQ Q24", "常見問題第24問")) for x, t in zip(X, names)]
    even_rows([chain])
    y2 = h1 + 30 + hh2 + 10
    h2 = place([(chain, 26)], y0=y2)
    named = C6(218, 574, ("Every party named in the payment message", "撥付訊息中被具名的人士"),
               ("Individuals, companies, banks and so on", "例如個人、公司、銀行等"), 'must', ("FAQ Q24 · ¶6.16(c)", "常見問題第24問 · 第6.16(c)段"))
    h3 = place([([named], 0)], y0=h2)
    b = [hsvg, h2svg] + [n.render() for n in [c, bo, cp] + chain + [named]]
    m = 'g6w'
    for p, q in zip(chain, chain[1:]):
        b.append(edge([p.right, q.left], mid=m))
    b.append(f'<line class="e e-dash" x1="16" y1="{h1 + 15:.0f}" x2="984" y2="{h1 + 15:.0f}"/>')
    aria = ("Whom to screen. At the start of the relationship and against every new or updated designation: the customer and every beneficial owner, always; connected parties and persons purporting to act for the customer, on a risk-based approach. Before executing a cross-border or cross-boundary wire transfer or remittance, at a minimum: the originator, ordering institution, intermediary institution, beneficiary institution and recipient, and every party named in the payment message.",
            "篩查對象。建立關係當時及每次有新增或更新的指認時：客戶及其任何實益擁有人，一律篩查；有關連者及看似代表客戶行事的人，按風險為本的方法篩查。執行跨境電傳轉帳或匯款交易前，最低限度篩查：匯款人、匯款機構、中介機構、收款機構、收款人，以及撥付訊息中被具名的人士。")
    return svg(W, h3 + 14, ''.join(b), aria, m, 860)


WHO_KEY = legend([('must', ("screen every time, whatever the customer's risk profile", "不論客戶的風險狀況為何，一律篩查")),
                  ('', ("screen on a risk-based approach", "按風險為本的方法篩查"))])


# ---------------------------------------------------------------- 4. a possible match
def fig_match():
    W = 1000
    S = C6(380, 300, ("Screening throws up a possible name match", "篩查期間識別出可能吻合的姓名／名稱"), None, 'plain', "¶6.18")
    E = C6(380, 300, ("Carry out enhanced checks", "執行更嚴格的查核"), ("to decide whether it is a genuine hit", "以斷定是否真正吻合"), 'must', "¶6.18")
    D1 = Node(380, 300, ("Is it a genuine hit?", "是否真正吻合？"), None, shape='hex')
    Y = C6(20, 330, ("Genuine hit: do not proceed", "真正吻合：不可繼續"),
           ("No relationship, no service. Making funds available to them, or dealing with their funds, is an offence unless licensed",
            "不可建立業務關係或提供服務。除非獲批特許，向其提供資金或處理其資金即屬犯罪"),
           'stop', "¶6.5, 6.7, 6.16", answer=True)
    L = C6(20, 330, ("If you must pay them: licence first", "如需向其付款：先取得特許"),
           ("Write to the Security Bureau (UNATMO) or the Commerce and Economic Development Bureau (UNSO)",
            "向保安局（《聯合國（反恐怖主義措施）條例》）或商務及經濟發展局（《聯合國制裁條例》）提出書面申請"),
           'may', "¶6.6, 6.8", answer=True)
    D2 = Node(395, 270, ("Any suspicion of TF, PF or a sanctions violation?", "是否懷疑涉及恐怖分子資金籌集、擴散資金籌集或違反制裁？"), None, shape='hex')
    R = C6(700, 290, ("Report to the JFIU", "向財富情報組作出報告"),
           ("For terrorist property this is also a statutory duty: an STR as soon as it is reasonable to do so", "如屬恐怖分子財產，這亦是法定責任：須在合理範圍內盡快提交可疑交易報告"),
           'must', "¶6.18, 7.1", answer=True)
    K = C6(150, 720, ("Record everything", "全部記錄在案"),
           ("The enhanced-check results, together with all screening records, documented or recorded electronically",
            "更嚴格查核的結果連同篩查紀錄，記錄在案或以電子方式記錄"), 'must', "¶6.18", answer=True)
    H = place([([S], 34), ([E], 34), ([D1], 40), ([Y], 40), ([L, D2, R], 44), ([K], 0)], y0=14)
    b = [n.render() for n in (S, E, D1, Y, L, D2, R, K)]
    m = 'g6m'
    both = lay() == 'both'
    ex = 17 if both else 0
    b.append(edge([S.bottom, E.top], mid=m))
    b.append(edge([E.bottom, D1.top], mid=m))
    b.append(edge([D1.left, (Y.cx, D1.cy), Y.top], mid=m))
    b.append(mlabel6(D1.x - 14, D1.cy - 8, "yes", "是", 'end'))
    b.append(edge([D1.bottom, D2.top], mid=m))
    b.append(mlabel6(D1.cx + 12, D1.bottom[1] + 18 + ex, "no", "否", 'start'))
    # a genuine hit also goes on to the suspicion question: join the trunk with an arrow
    b.append(edge([Y.right, (D2.cx - 1, Y.cy)], mid=m))
    b.append(mlabel6((Y.x + Y.w + D2.cx) / 2, Y.cy - 8, "also ask", "同時考慮"))
    b.append(edge([Y.bottom, L.top], mid=m))
    b.append(edge([D2.right, R.left], mid=m))
    b.append(mlabel6((D2.x + D2.w + R.x) / 2, D2.cy - 8 - ex, "yes", "是"))
    b.append(edge([D2.bottom, (D2.cx, K.y)], mid=m))
    b.append(mlabel6(D2.cx + 12, D2.bottom[1] + 18 + ex, "no", "否", 'start'))
    b.append(edge([R.bottom, (R.cx, K.y)], mid=m))
    b.append(edge([L.bottom, (L.cx, K.y)], mid=m))
    aria = ("What to do with a possible name match. Carry out enhanced checks to decide whether it is a genuine hit. If it is, do not establish the relationship or provide the service; making funds available or dealing with the party's funds is an offence unless licensed, and any payment you must make needs a licence: write to the Security Bureau under UNATMO or the Commerce and Economic Development Bureau under UNSO. A genuine hit also goes on to the next question. Whether or not it is a genuine hit, ask whether there is any suspicion of TF, PF or a sanctions violation. If there is, report to the JFIU, which for terrorist property is also a statutory duty. Every path ends with recording the enhanced-check results together with all screening records.",
            "如何處理可能吻合的姓名。執行更嚴格的查核，以斷定是否真正吻合。如屬真正吻合，不可建立業務關係或提供服務；除非獲批特許，向其提供資金或處理其資金即屬犯罪；如需向其付款，須先取得特許：循《聯合國（反恐怖主義措施）條例》向保安局或循《聯合國制裁條例》向商務及經濟發展局提出書面申請。真正吻合亦要接着考慮下一個問題。不論是否真正吻合，都要考慮是否懷疑涉及恐怖分子資金籌集、擴散資金籌集或違反制裁。如有懷疑，應向財富情報組報告；如屬恐怖分子財產，這亦是法定責任。所有路徑最後都把更嚴格查核的結果連同篩查紀錄記錄在案。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


MATCH_KEY = legend([('', ("what starts it", "起點")), ('hex', ("a question", "問題")), ('must', ("a duty on you", "你的責任")),
                    ('stop', ("you must not proceed with the relationship or service", "你不可繼續建立關係或提供服務")),
                    ('may', ("only with a licence someone else grants", "只可憑他人批予的特許"))])
