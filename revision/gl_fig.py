# Figures for the Guidelines page: the application route, the Assessment's pass
# rule, the renewal countdown, and what moves a pecuniary penalty.
from ui import *
from bl_core import _runs
from bl_figs import lines_down


def LG(p):
    return (f"Licensing Guide ¶{p}", f"《牌照指引》第{_runs(p)}段")


def GN(p):
    return (f"CA Guidance Notes ¶{p}", f"《能力評核須知》第{_runs(p)}段")


class BCard(Card):
    """A Card whose texts may carry manual line breaks ('\\n'), so Chinese lines break
    between words; in the combined view a small gap separates the English block from
    the Chinese one."""

    def __init__(self, x, w, title, body=None, kind='plain', cite=None, href=None,
                 size=11.5, tsize=12.5, minh=0, answer=False):
        super().__init__(x, w, title, body, kind, cite, href, size, tsize, minh, answer)
        size, tsize = size * FS, tsize * FS
        inner = w - 24

        def wr(t, s):
            out = []
            for part in t.split('\n'):
                out += wrap(part, inner, s)
            return out
        tcls = 't-inv t-b' if kind == 'stop' else ('t t-b t-faint' if kind == 'faint' else 't t-b')
        bcls = 't-inv' if kind == 'stop' else ('t t-faint' if kind == 'faint' else 't')
        for i, v in enumerate(('en', 'tc')):
            tl = wr(title[i], tsize) if title and title[i] else []
            bl = wr(body[i], size) if body and body[i] else []
            self.seg[v] = [(l, tcls, tsize) for l in tl] + [(l, bcls, size) for l in bl]
        self.seg['both'] = self.seg['en'] + [('', bcls, 6)] + self.seg['tc']
        self.h = max(minh, sum(s * LH for _, _, s in self.seg[lay()]) + 16 + (CS * LH if cite else 0))


def tick_text(x, y, en, tc, cls='c-sans', size=10.5, anchor='start'):
    """One-line axis label; identical text is drawn once for every language view."""
    size = size * FS
    a = f' text-anchor="{anchor}"'
    if en == tc:
        return f'<text class="{cls}" font-size="{size}"{a}><tspan x="{x:.1f}" y="{y:.1f}">{esc(en)}</tspan></text>'
    return (f'<text class="{cls} s-en" font-size="{size}"{a}><tspan x="{x:.1f}" y="{y:.1f}">{esc(en)}</tspan></text>'
            f'<text class="{cls} s-tc" font-size="{size}"{a}><tspan x="{x:.1f}" y="{y:.1f}">{esc(tc)}</tspan></text>'
            f'<text class="{cls} s-both" font-size="{size}"{a}><tspan x="{x:.1f}" y="{y:.1f}">{esc(en)} / {esc(tc)}</tspan></text>')


def tick_stack(x, y, en, tc, size=10.5):
    """Axis tick label; the combined view stacks the Chinese under the English."""
    size = size * FS
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en] if en == tc else [en, tc])):
        g = [f'<text class="t s-{v}" font-size="{size}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x:.1f}" y="{y + i * size * 1.2:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def mlab(x, y, en, tc, anchor='middle'):
    """Edge label like ui.mlabel, but the combined view stacks English over Chinese at a
    16-unit pitch (about 1.2 x the 13.5px label size), so the halo of one line does not
    touch the other; the bottom line stays at y."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        n = len(ls)
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (n - 1 - i) * 16:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def dash(pts):
    d = ' '.join(f'{x:.0f},{y:.0f}' for x, y in pts)
    return f'<polyline class="e e-dash" points="{d}"/>'


# ---------------------------------------------------------------- 1. application route
def fig_route():
    W = 1000
    S1 = BCard(40, 540, ("You submit the application, with the Schedule 3 fee", "你遞交申請，並附隨附表3指明的費用"),
               ("Form 1 with the supplementary information sheet and annex; a Business Plan and an AML/CFT Policy; a fit-and-proper declaration for each person to be tested; copies of the listed documents; two 4R photographs for each premises",
                "表格1連同補充資料表格及附件；業務計劃及打擊洗錢政策；\n每名須接受判定人士的適當人選聲明表格；\n所列文件的複本；每個處所兩張4R照片"),
               cite=("s.30(1)(b) · Licensing Guide ¶5.1, 5.8", "第30(1)(b)條 · 《牌照指引》第5.1、5.8段"))
    S2 = BCard(40, 540, ("C&ED acknowledges receipt, and chases anything outstanding", "海關確認收件，並催交尚欠文件"), None, cite=LG("5.4"))
    R2 = BCard(655, 315, ("Not produced within\nthe specified period", "未能在指明期限內遞交"),
               ("The application is invalid\nand is not processed", "申請視作無效，不獲處理"), 'stop', LG("5.4"), answer=True)
    S3 = BCard(40, 540, ("Everything is in: C&ED sends two things", "文件齊備：海關發出兩份文件"),
               ("A notice of interview;\nan invitation to nominate who will sit the Assessment",
                "會面通知；\n提名應考能力評核人選的邀請信"), cite=LG("5.4"))
    V = BCard(655, 315, ("Running alongside", "同步進行"),
              ("Fit-and-proper checks against C&ED,\nother government and law-enforcement\nrecords, and an on-site inspection\nof the premises",
               "將適當人選資料與海關、\n其他政府部門及執法機構的紀錄核對，\n並實地視察業務處所"), 'faint', LG("5.6, 5.9"))
    S4 = BCard(40, 540, ("The interview with C&ED officers", "與海關人員會面"),
               ("Originals and the payment record are checked; you sign the application in front of the officers;\nyou explain your Business Plan and AML/CFT Policy;\nyou are briefed on the licensing and compliance rules",
                "查驗文件正本及繳費紀錄；你須在人員面前簽署申請書；\n你須闡釋業務計劃及打擊洗錢政策；\n人員向你簡介發牌及合規規定"),
               cite=LG("5.4–5.5"))
    S5 = BCard(40, 540, ("Your nominees sit the Assessment\nwithin 30 days of the interview", "獲提名人士須於會面後30日內應考能力評核"),
               ("Every candidate from the company sits the same session", "同一公司的應考者須應考同一時段"), 'must', GN("4.3, 4.5"))
    R5 = BCard(655, 315, ("Nobody passes: one more try", "無人合格：再有一次機會"),
               ("A retake after 30 days from\nthe result notice. Still no pass:\nthe application may be refused",
                "於成績通知發出30日後重考。\n仍無人合格：申請可被拒絕"), 'must', GN("4.5"), answer=True)
    D = Node(70, 480, ("Is the Commissioner satisfied on every test?", "關長是否信納各項測試？"), None, shape='hex')
    G = BCard(40, 250, ("Licence granted", "批給牌照"), ("Normally valid for 2 years", "有效期一般為2年"), 'ok', LG("2.10"), answer=True)
    F = BCard(330, 330, ("Refused by written notice", "以書面通知拒絕"),
              ("You can take it to the Review\nTribunal within 21 days of the notice", "可於通知送出後21日內\n向覆核審裁處申請覆核"), 'stop', LG("5.10–5.11"),
              href="#p6-clock", answer=True)
    H = place([([S1], 30), ([S2, R2], 30), ([S3, V], 30), ([S4], 30), ([S5, R5], 40), ([D], 44), ([G, F], 0)], y0=14)
    b = [n.render() for n in (S1, S2, R2, S3, V, S4, S5, R5, D, G, F)]
    m = 'glr'
    for a, c in ((S1, S2), (S2, S3), (S3, S4), (S4, S5)):
        b.append(edge([a.bottom, c.top], mid=m))
    b.append(edge([S5.bottom, D.top], mid=m))
    b.append(mlab(S5.cx + 10, (S5.bottom[1] + D.top[1]) / 2 + 5, "pass", "合格", 'start'))
    b.append(edge([S2.right, R2.left], mid=m))
    b.append(mlab((S2.x + S2.w + R2.x) / 2, S2.cy - 8, "missing", "欠交"))
    b.append(edge([S5.right, R5.left], mid=m))
    b.append(mlab((S5.x + S5.w + R5.x) / 2, S5.cy - 8, "fail", "不合格"))
    b.append(dash([S3.right, V.left]))
    b.append(edge([R5.bottom, (R5.cx, D.cy), D.right], mid=m))
    b.append(mlab((D.x + D.w + R5.cx) / 2, D.cy - 8, "after the retake", "重考後"))
    jy = D.bottom[1] + 22
    b.append(edge([D.bottom, (D.cx, jy), (G.cx, jy), G.top], ("yes", "是"), G.cx - 8, jy + 14, 'end', mid=m))
    b.append(edge([D.bottom, (D.cx, jy), (F.cx, jy), F.top], ("no", "否"), F.cx + 8, jy + 14, 'start', mid=m))
    aria = ("The route to a licence. You submit Form 1 with the supporting papers, and the application must be accompanied by the Schedule 3 fee; C&ED acknowledges and chases anything missing, and an application still incomplete after the specified period is invalid and not processed. Once everything is in, C&ED sends a notice of interview and an invitation to nominate candidates for the Assessment. At the interview originals are checked, you sign the application and explain your plans. Your nominees sit the Assessment within 30 days, with one retake after 30 days from the result if nobody passes. Fit-and-proper checks and a premises inspection run alongside. The Commissioner then grants a licence, normally for two years, or refuses by written notice, which you can take to the Review Tribunal within 21 days of the notice.",
            "申領牌照的流程。你遞交表格1及證明文件，申請須附隨附表3指明的費用；海關確認收件並催交尚欠文件，逾指明期限仍不齊備的申請視作無效，不獲處理。文件齊備後，海關發出會面通知及提名應考能力評核人選的邀請信。會面時查驗正本，你須簽署申請書並闡釋計劃。獲提名人士須於30日內應考，如無人合格，可於成績通知發出30日後重考一次。適當人選判定及處所視察同步進行。其後關長批給牌照（有效期一般為2年），或以書面通知拒絕，你可於通知送出後21日內向覆核審裁處申請覆核。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


ROUTE_KEY = legend([('', ("a step on the way", "流程中的步驟")), ('must', ("a deadline or test you must meet", "你必須符合的限期或測試")),
                    ('faint', ("C&ED's own checks", "海關自行進行的查核")), ('hex', ("the Commissioner's decision", "關長的決定")),
                    ('ok', ("licence granted", "批給牌照")), ('stop', ("the application ends: invalid, or refused", "申請終結：無效或被拒"))])


# ---------------------------------------------------------------- 2. pass rule
# Module labels with hand-set line breaks, so no Chinese word is split.
MODS = [(["AML/CFT and", "CPF basics"], ["打擊洗錢／", "恐怖分子", "資金籌集及", "擴散資金", "籌集常識"]),
        (["AMLO Parts", "1 to 7"], ["條例", "第1至7部"]),
        (["AMLO", "Schedules"], ["條例附表"]),
        (["C&ED", "guidelines"], ["海關指引"]),
        (["Governance", "and strategy"], ["管治及策略"]),
        (["AML/CFT", "control areas"], ["管控範疇"]),
        (["Showing and", "monitoring", "compliance"], ["證明及", "監察合規"])]


def fig_pass():
    W = 1000
    X0, SQ, SG, GAP = 140, 15, 3, 11
    GW = 5 * SQ + 4 * SG
    HS = 10.5 * FS          # module label size
    rows = [
        (("Candidate A", "應考者甲"), [0, 1, 3, 0, 1, 0, 0],
         BCard(822, 172, ("Fail", "不合格"), ("30 marks, but\nmodule 3 has 3 wrong", "得30分，\n但單元3答錯3題"), 'stop', answer=True)),
        (("Candidate B", "應考者乙"), [2, 2, 2, 0, 2, 2, 0],
         BCard(822, 172, ("Pass", "合格"), ("Exactly 25, and no\nmodule has more\nthan 2 wrong", "剛好25分，\n而且沒有單元\n答錯超過2題"), 'ok', answer=True)),
        (("Candidate C", "應考者丙"), [2, 2, 2, 2, 2, 2, 0],
         BCard(822, 172, ("Fail", "不合格"), ("No module has more\nthan 2 wrong, but\nonly 23 marks", "沒有單元答錯\n超過2題，\n但只得23分"), 'stop', answer=True)),
    ]
    b = []
    hy = 12
    MG = 8                  # gap between the English and Chinese labels in the combined view
    nlines = max(len(en if lay() == 'en' else tc if lay() == 'tc' else en + tc) for en, tc in MODS)
    for i, (en, tc) in enumerate(MODS):
        cx = X0 + i * (GW + GAP) + GW / 2
        b.append(f'<text class="t t-b" font-size="{12.5 * FS}" text-anchor="middle"><tspan x="{cx:.1f}" y="{hy + 14:.1f}">{i + 1}</tspan></text>')
        for v, ls in (('en', en), ('tc', tc), ('both', en + tc)):
            g = [f'<text class="c-sans s-{v}" font-size="{HS}" text-anchor="middle">']
            for k, l in enumerate(ls):
                gap = MG if v == 'both' and k >= len(en) else 0
                g.append(f'<tspan x="{cx:.1f}" y="{hy + 20 + HS + k * HS * 1.3 + gap:.1f}">{esc(l)}</tspan>')
            g.append('</text>')
            b.append(''.join(g))
    b.append(tick_text(X0 - 12, hy + 14, "module →", "單元 →", 't', 11, 'end'))
    y = hy + 20 + nlines * HS * 1.3 + (MG if lay() == 'both' else 0) + 22
    for n, (lab, wrong, verdict) in enumerate(rows):
        verdict.y = y
        cy = y + verdict.h / 2
        score = 35 - sum(wrong)
        ls = 11.5 * FS
        for v, name, sc in (('en', lab[0], f"{score} of 35"), ('tc', lab[1], f"35分中得{score}分")):
            b.append(f'<text class="t t-b s-{v}" font-size="{ls}" text-anchor="middle"><tspan x="70" y="{cy - 4:.1f}">{esc(name)}</tspan></text>')
            b.append(f'<text class="t s-{v}" font-size="{ls}" text-anchor="middle"><tspan x="70" y="{cy + ls:.1f}">{esc(sc)}</tspan></text>')
        p = ls * 1.3
        y0 = cy - 1.5 * p + ls * 0.35
        b.append(f'<text class="t t-b s-both" font-size="{ls}" text-anchor="middle"><tspan x="70" y="{y0:.1f}">{esc(lab[0])}</tspan><tspan x="70" y="{y0 + p:.1f}">{esc(lab[1])}</tspan></text>')
        b.append(f'<text class="t s-both" font-size="{ls}" text-anchor="middle"><tspan x="70" y="{y0 + 2 * p + 4:.1f}">{esc(f"{score} of 35")}</tspan><tspan x="70" y="{y0 + 3 * p + 4:.1f}">{esc(f"35分中得{score}分")}</tspan></text>')
        for i, w in enumerate(wrong):
            gx = X0 + i * (GW + GAP)
            for k in range(5):
                cls = 'n n-must' if k >= 5 - w else 'n n-plain'
                b.append(f'<rect class="{cls}" x="{gx + k * (SQ + SG)}" y="{cy - SQ / 2:.1f}" width="{SQ}" height="{SQ}" rx="2"/>')
            if w > 2:
                b.append(f'<rect x="{gx - 5}" y="{cy - SQ / 2 - 5:.1f}" width="{GW + 10}" height="{SQ + 10}" rx="4" style="fill:none;stroke:var(--red);stroke-width:2"/>')
                b.append(tick_text(gx + GW / 2, cy + SQ / 2 + 20, "3 wrong", "錯3題", 't t-red t-b', 11, 'middle'))
        b.append(verdict.render())
        y += verdict.h + 18
    aria = ("The pass rule has two conditions. Seven modules of five questions each: no module may have more than two wrong answers, and the total must be at least 25 out of 35. Candidate A scores 30 but fails because module 3 has three wrong. Candidate B passes with exactly 25 and at most two wrong in every module. Candidate C fails with 23 even though no module has more than two wrong.",
            "合格準則有兩個條件。共七個單元，每單元五題：每個單元答錯不可超過兩題，而總分須達35分中的25分或以上。應考者甲得30分，但單元3答錯三題，不合格。應考者乙剛好得25分，且每個單元最多答錯兩題，合格。應考者丙沒有單元答錯超過兩題，但只得23分，不合格。")
    return svg(W, y, ''.join(b), aria, 'glp', 860)


PASS_KEY = legend([('', ("answered correctly", "答對")), ('must', ("answered wrongly", "答錯")),
                   ('ok', ("pass", "合格")), ('stop', ("fail", "不合格"))])


# ---------------------------------------------------------------- 3. renewal countdown
def fig_renew():
    W = 1000
    X0, X1 = 70, 930

    def xd(day):
        return X0 + (day + 90) * (X1 - X0) / 90

    N = BCard(20, 262, ("① Nominate within 7 days", "① 7日內提名"),
              ("Of receiving the invitation.\nLate: the renewal is invalid", "自接獲邀請信起計。\n逾期：續牌申請無效"), 'must', LG("6.2, 6.4(c)"), answer=True)
    # wide enough for its one-line statute and Guide citation; it still spans the 45-day drop line (x = 500)
    L = BCard(376, 384, ("② Lodge Form 2 by 45 days before expiry", "② 期滿前45日遞交表格2"),
              ("With the supplementary sheet and annex, and accompanied by the Schedule 3 fee; late: invalid. The other papers go with it, and anything missing is chased",
               "連同補充資料表格及相關附件，\n並附隨附表3指明的費用；逾期：申請無效。\n其他文件一併遞交，欠交的會獲發信催交"), 'must',
              ("s.31(2) · Licensing Guide ¶6.1, 6.3, 6.4(a)", "第31(2)條 · 《牌照指引》第6.1、6.3、6.4(a)段"), answer=True)
    # kept left of the 45-day drop line (x = 500) and right of the 83-day one (x = 137)
    S = BCard(150, 326, ("Sit within 30 days", "30日內應考"),
              ("Of receiving the invitation.\nMissing the session: the application\nwill be rejected",
               "自接獲邀請信當日起計。\n未有出席指定時段的評核，\n會導致相關申請被拒絕"), 'must', LG("6.2"), answer=True)
    R = BCard(672, 290, ("Nobody passes: one retake", "無人合格：可重考一次"),
              ("After 30 days from the result notice and before expiry. Still nobody: renewal may be refused",
               "於成績通知發出30日後、\n期滿前重考。仍無人合格：\n續期可被拒絕"), 'must', GN("4.6"), answer=True)
    N.y = L.y = 14
    top1 = max(N.h, L.h)
    # row 2: the first sitting, and the retake that follows a fail
    y2 = 14 + top1 + 16
    rowh = max(S.h, R.h)
    S.y = y2 + (rowh - S.h) / 2
    R.y = y2 + (rowh - R.h) / 2
    ay = y2 + rowh + 34
    b = [N.render(), L.render(), S.render(), R.render()]
    m = 'glw'
    b.append(edge([S.right, R.left], mid=m))
    b.append(mlab((xd(-45) + R.x) / 2, S.cy - 8, "fail", "不合格"))
    b.append(f'<line class="e" x1="{X0 - 20}" y1="{ay}" x2="{X1 + 34}" y2="{ay}"/>')
    tlabels = []
    ticks = [(-90, "90", "90"), (-83, "83", "83"), (-60, "60", "60"), (-45, "45", "45"), (0, "expiry", "期滿")]
    for d, en, tc in ticks:
        x = xd(d)
        b.append(f'<line class="e" x1="{x:.1f}" y1="{ay - 7}" x2="{x:.1f}" y2="{ay + 7}"/>')
        # drawn last, with the label halo, so the drop lines through 90 and 45 pass behind them
        tlabels.append(tick_text(x, ay + 22, en, tc, 'lbl', 11, 'middle'))
    # one caption for the whole axis, above its left end (clear of the 83-day drop line)
    cap = {'en': ["days before", "expiry"], 'tc': ["期滿前", "日數"], 'both': ["days before", "expiry", "期滿前日數"]}
    for v, ls in cap.items():
        g = [f'<text class="c-sans s-{v}" font-size="{10.5 * FS}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{X0 - 20}" y="{ay - 10 - (len(ls) - 1 - i) * 10.5 * FS * 1.2:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        b.append(''.join(g))
    for n, d in ((N, -83), (L, -45), (S, -60)):
        x = xd(d)
        if n is L:   # break the line where the fail arrow crosses it
            b.append(f'<line class="e" x1="{x:.1f}" y1="{n.y + n.h:.1f}" x2="{x:.1f}" y2="{S.cy - 6:.1f}"/>')
            b.append(f'<line class="e" x1="{x:.1f}" y1="{S.cy + 6:.1f}" x2="{x:.1f}" y2="{ay:.1f}"/>')
        else:
            b.append(f'<line class="e" x1="{x:.1f}" y1="{n.y + n.h:.1f}" x2="{x:.1f}" y2="{ay:.1f}"/>')
        b.append(f'<circle cx="{x:.1f}" cy="{ay}" r="3.2" class="dot"/>')
    by = ay + 50
    REM = BCard(20, 262, ("C&ED's reminder, 90 days out", "海關於期滿前90日發出提示"),
                ("Sent to every licensee with the invitation to nominate. Applying on time stays your legal duty",
                 "向每名持牌人發出，\n並夾附提名邀請信。\n按時申請仍是你的法定責任"), 'plain', LG("6.2"))
    INT = BCard(345, 310, ("③ Produce chased documents in the specified period", "③ 在指明期限內交出催交的文件"),
                ("Miss it: invalid. Once all is in\norder, C&ED sends the interview\nnotice. Fees are not refunded",
                 "逾期：申請無效。文件齊備後，\n海關發出會面通知。費用概不退還"), 'must', LG("6.3, 6.4(b)"), answer=True)
    for n in (REM, INT):
        n.y = by
    b += [REM.render(), INT.render()]
    for x in (xd(-90), xd(-45)):
        b.append(f'<line class="e" x1="{x:.1f}" y1="{ay:.1f}" x2="{x:.1f}" y2="{by:.1f}"/>')
    b.append(f'<circle cx="{xd(-90):.1f}" cy="{ay}" r="3.2" class="dot"/>')
    b += tlabels
    oy = by + max(REM.h, INT.h) + 30
    BAD = BCard(20, 470, ("Miss ①, ② or ③: the renewal is invalid", "①、②或③任何一項未能做到：續牌申請無效"),
                ("It is not processed, the licence lapses automatically\nat expiry, and you must stop;\ncarrying on is unlicensed operation",
                 "申請不獲處理，牌照於期滿時自動失效，\n你必須停止經營；繼續經營即屬無牌經營"), 'stop', LG("6.2, 6.4"), answer=True)
    GOOD = BCard(510, 470, ("A valid application, lodged in time", "按時遞交的有效申請"),
                 ("The licence stays in force past expiry until it is renewed or, if renewal is refused, until the refusal takes effect, unless the application is withdrawn or the licence is revoked or suspended under section 34",
                  "牌照在期滿後仍然有效，直至獲續期；如續期被拒絕，\n則直至拒絕的決定生效為止；除非申請被撤回，\n或牌照根據第34條被撤銷或暫時吊銷"), 'ok', "s.31(10)", href="#p5-losing", answer=True)
    BAD.y = GOOD.y = oy
    b += [BAD.render(), GOOD.render()]
    H = oy + max(BAD.h, GOOD.h) + 14
    aria = ("The renewal countdown, in days before expiry. At 90 days C&ED sends every licensee a reminder with an invitation to nominate. You nominate within 7 days of receiving it, and your nominees sit within 30 days of receiving it; missing the session means the application will be rejected. If nobody passes, one retake is allowed after 30 days from the result and before expiry. Form 2, the supplementary sheet and the annex must be lodged not later than 45 days before expiry, accompanied by the Schedule 3 fee. C&ED then chases missing documents, which must arrive within the specified period, and interviews you. Missing any of the three invalidity deadlines, the 7-day nomination, the 45-day lodging or the specified period for chased documents, makes the application invalid, so the licence lapses at expiry. A valid application in time keeps the licence in force until it is renewed or, if refused, until the refusal takes effect, unless the application is withdrawn or the licence is revoked or suspended under section 34.",
            "續牌倒數，以期滿前日數計算。第90日海關向每名持牌人發出提示，並夾附提名邀請信。你須在接獲邀請信當日起計7日內提名，獲提名人士須在接獲邀請信當日起計30日內應考；未有出席指定時段的評核，會導致相關申請被拒絕。如無人合格，可於成績通知發出30日後、期滿前重考一次。表格2、補充資料表格及相關附件須在期滿前45日或之前遞交，並附隨附表3指明的費用。其後海關催交尚欠文件，須在指明期限內交出，然後與你會面。7日內提名、期滿前45日遞交、在指明期限內交出尚欠文件，任何一項未能做到，申請即屬無效，牌照於期滿時失效。按時遞交有效申請，牌照會持續有效，直至獲續期；如續期被拒絕，則直至拒絕的決定生效為止；除非申請被撤回，或牌照根據第34條被撤銷或暫時吊銷。")
    return svg(W, H, ''.join(b), aria, m, 860)


RENEW_KEY = legend([('must', ("your deadline; ①②③ make the renewal invalid if missed", "你的限期；①②③未能做到，續牌申請即屬無效")),
                    ('', ("C&ED's step", "海關的步驟")),
                    ('stop', ("the licence lapses", "牌照失效")), ('ok', ("the licence continues", "牌照繼續有效"))])


# ---------------------------------------------------------------- 4. penalty factors
def fig_scale():
    W = 1000
    LX, LW, MX, MW, RX, RW = 20, 285, 362, 276, 695, 285
    up = [
        BCard(LX, LW, ("Intent or recklessness", "蓄意或罔顧後果"), ("Rather than negligence or a\nmerely technical breach", "而非純粹因疏忽或只屬\n技術性違規"), 'must', "¶9(a)(i)"),
        BCard(LX, LW, ("Long, frequent, or a pattern", "持續、頻密或成為模式"),
              ("Also many small issues that\ntogether justify a penalty", "亦包括多項個別不足以施罰、\n合起來卻足以施罰的小問題"), 'must', "¶9(a)(ii), (vii)–(viii)"),
        BCard(LX, LW, ("Harm done", "造成的損害"),
              ("To the integrity of money services or Hong Kong's standing as a financial centre; loss or cost to others; financial crime it helped",
               "損害在香港經營金錢服務業務\n的廉潔穩健，或香港作為\n國際金融中心的聲譽；\n令他人蒙受損失或承擔支出；\n由此促成的金融罪行"), 'must', "¶9(a)(iii)–(iv), (ix)"),
        BCard(LX, LW, ("Systemic weakness,\nor a group effort", "系統性缺失或集體違規"),
              ("Serious or systemic gaps in CDD and record-keeping controls; a breach done as part of a group, weighed by your role in it",
               "客戶盡職審查及備存紀錄的\n管控有嚴重或系統性缺失；\n屬集團違規的，\n按你在其中的角色考慮"), 'must', "¶9(a)(v)–(vi)"),
        BCard(LX, LW, ("Hiding it, or likely\nto repeat it", "隱瞞違規，或相當可能再犯"), None, 'must', "¶9(b)(i), (iv)"),
        BCard(LX, LW, ("History and gain", "過往紀錄及得益"),
              ("Earlier similar breaches; breaking an undertaking; the benefit gained or cost avoided by you, your directors or staff",
               "過往類似違規；違反先前的承諾；\n你、你的董事或僱員從違規行為中\n所獲得的利益或所避免開支的數額"), 'must', "¶9(c)(i)–(ii), (d)(iii)"),
    ]
    down = [
        BCard(RX, RW, ("Negligence, or a\ntechnical breach", "疏忽或技術性違規"), ("Generally regarded as less serious", "一般視作嚴重性較低"), 'ok', "¶9(a)(i)"),
        BCard(RX, RW, ("Putting it right", "作出補救"),
              ("Remedial steps once the breach\nsurfaced, action against those\ninvolved, steps against a repeat", "發現違規後採取補救措施、\n對涉事人員採取行動、防止再犯"), 'ok', "¶9(b)(ii)"),
        BCard(RX, RW, ("Cooperating", "合作"), ("With the Commissioner, other authorities and law enforcement during the investigation", "在調查期間與關長、\n其他有關當局及執法機構合作"), 'ok', "¶9(b)(iii)"),
        BCard(RX, RW, ("Reporting it yourself", "主動舉報"), ("Promptly, effectively and completely", "迅速、有效及完整"), 'ok', "¶9(d)(iv)"),
        BCard(RX, RW, ("Following current guidance", "遵從當時的指引"),
              ("Conduct in line with the guidance current at the time is generally not disciplined at all", "符合當時適用指引的行為，\n一般不會招致紀律行動"), 'ok', "¶9(d)(i)"),
    ]
    CEIL = BCard(MX, MW, ("The ceiling", "上限"),
                 ("Part 4: $10,000,000 or 3 times the profit gained or cost avoided, whichever is greater.\nPart 5: $1,000,000",
                  "第4部：$10,000,000或所獲取的\n利潤或所避免的開支的3倍，\n以較大者為準。\n第5部：$1,000,000"), 'plain', ("s.21(2)(c) and s.43(2)(c)", "第21(2)(c)條及第43(2)(c)條"))
    SER = BCard(MX, MW, ("Seriousness decides", "取決於嚴重程度"),
                ("The more serious, the likelier a penalty and the larger it is. It is meant to deter you and every other operator",
                 "越嚴重，越可能被罰，罰款亦越高。\n目的是阻嚇你及所有其他經營者"), 'plain', ("¶8; deterrence ¶5 or ¶6", "第8段；阻嚇見第5或第6段"))
    CONS = BCard(MX, MW, ("Consistency", "一致"),
                 ("Like cases treated alike; what other authorities did about the same incident is weighed",
                  "相若的個案一般貫徹一致處理；\n其他當局就同一事件的行動\n亦會考慮"), 'plain', "¶9(c)(iii), (d)(ii)")
    FLOOR = BCard(MX, MW, ("Not your ruin", "不致令你陷入困境"),
                  ("It should not be likely to put you in financial jeopardy; your size and financial resources are weighed",
                   "罰款不應令你陷入財政困境；\n會考慮你的規模及財政資源"), 'plain', "¶7")
    top = 60
    y = top
    for n in up:
        n.y = y
        y += n.h + 14
    bottom = y - 14

    def spread(nodes):
        g = (bottom - top - sum(n.h for n in nodes)) / (len(nodes) - 1)
        yy = top
        for n in nodes:
            n.y = yy
            yy += n.h + g
    spread(down)
    mid = [CEIL, SER, CONS, FLOOR]
    spread(mid)
    b = [n.render() for n in up + down + mid]
    m = 'gls'
    b.append(lines_down(LX + LW / 2, 8, ["Heavier"], ["較重"], 't t-b', 13))
    b.append(lines_down(RX + RW / 2, 8, ["Lighter"], ["較輕"], 't t-b', 13))
    b.append(lines_down(MX + MW / 2, 8, ["How it is set, and limits"], ["如何釐定及限制"], 't t-b', 13))
    # brackets gather each column and feed the seriousness box
    for side, nodes, xb, xin in (('l', up, LX + LW + 18, MX), ('r', down, RX - 18, MX + MW)):
        y1, y2 = nodes[0].cy, nodes[-1].cy
        b.append(f'<line class="e" x1="{xb}" y1="{y1:.1f}" x2="{xb}" y2="{y2:.1f}"/>')
        for n in nodes:
            xe = n.x + n.w if side == 'l' else n.x
            b.append(f'<line class="e" x1="{xe}" y1="{n.cy:.1f}" x2="{xb}" y2="{n.cy:.1f}"/>')
        # enter the seriousness box at the height inside it farthest from every connector
        # of this column, so no single factor seems to feed it on its own
        cands = [SER.y + 14 + k for k in range(int(SER.h - 28) + 1)]
        ya = max(cands, key=lambda yy: (min(abs(yy - n.cy) for n in nodes), -abs(yy - SER.cy)))
        b.append(edge([(xb, ya), (xin, ya)], mid=m))
    # consistency is itself a ¶9 factor, so it feeds the seriousness box from below
    b.append(edge([CONS.top, SER.bottom], mid=m))
    aria = ("What moves a pecuniary penalty. On the left, factors that make it heavier: intent or recklessness; long, frequent or patterned breaches; harm to the integrity of money services, Hong Kong's reputation or other people; systemic weaknesses in CDD and record keeping; concealment or likely repetition; previous breaches, broken undertakings and gains. On the right, factors that make it lighter: negligence or a technical breach, remediation, cooperation, prompt and complete self-reporting, and conduct in line with the guidance current at the time. Both columns feed the seriousness of the breach, which decides the penalty. Consistency is also weighed in judging seriousness: like cases treated alike, and what other authorities did about the same incident. In the middle are also the limits that apply whatever the factors: a statutory ceiling, and never so heavy as to put the operator in financial jeopardy.",
            "影響罰款的因素。左邊令罰款較重：蓄意或罔顧後果；持續、頻密或成為模式的違規；損害在香港經營金錢服務業務的廉潔穩健、香港的聲譽或他人；客戶盡職審查及備存紀錄的系統性缺失；隱瞞或相當可能再犯；過往違規、違反承諾及得益。右邊令罰款較輕：疏忽或技術性違規、補救、合作、迅速而完整地主動舉報，以及符合當時有效指引的行為。兩邊的因素都用來衡量違規的嚴重程度，由嚴重程度決定罰款。衡量嚴重程度時亦會考慮一致性：相若的個案一般貫徹一致處理，以及其他有關當局就相同事件採取的行動。中間亦列出不論因素為何都適用的限制：法定上限，以及不致令經營者陷入財政困境。")
    return svg(W, bottom + 14, ''.join(b), aria, m, 860)


SCALE_KEY = legend([('must', ("pushes the penalty up", "令罰款較重")), ('ok', ("pulls it down", "令罰款較輕")),
                    ('', ("how the penalty is set, and the limits on it", "罰款如何釐定及其限制"))])
