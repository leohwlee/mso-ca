# Two figures for AMLO Part 5: the licence lifecycle, and the approval gate.
from bl_core import *
from bl_figs import lines_down
from ui import legend

LIFE_KEY = legend([('', ("a step", "步驟")),
                   ('hex', ("a test the Commissioner applies", "關長進行的測試")),
                   ('must', ("a duty or deadline on you", "你的責任或限期")),
                   ('may', ("a power the Commissioner holds", "關長持有的權力")),
                   ('ok', ("the licence is granted or continues", "牌照獲批給或延續")),
                   ('stop', ("refused, or the licence ends", "拒絕批給，或牌照終結"))])

GATE_KEY = legend([('', ("a step", "步驟")),
                   ('hex', ("the Commissioner's test", "關長的測試")),
                   ('ok', ("approved", "獲批准")),
                   ('stop', ("refused", "拒絕批准")),
                   ('must', ("the offence if the gate is skipped", "繞過此關即屬犯罪"))])
# the shortcut is keyed by a line swatch, not a box: the figure draws it as a dashed red line
GATE_KEY = GATE_KEY[:-len('</div>')] + (
    '<span><i style="width:24px;height:0;border:0;border-top:2px dashed var(--red);border-radius:0;background:none"></i>'
    + B("the unlawful shortcut (dashed red line)", "違法的捷徑（紅色虛線）", True) + '</span></div>')


def loop_label(x, y, en, tc):
    """A label above a line; the combined view stacks English over Chinese with room between."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        n = len(ls)
        g = [f'<text class="lbl s-{v}" text-anchor="middle">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (n - 1 - i) * 18:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def fig_life():
    W = 1010
    APPLY = Node(370, 460, ("Apply to the Commissioner, in the form and manner he specifies, with the Schedule 3 fee",
                            "以關長指明的格式及方式向關長申請，並附隨附表3指明的費用"), "s.30(1)")
    TEST = Node(330, 540, ("Is everyone who must be fit and proper actually fit and proper? Are the premises suitable?",
                           "所有須屬適當人選的人是否適當人選？處所是否適合？"), "s.30(3) · s.30(4)", shape='hex')
    REFUSE = Node(48, 252, ("Refused. Written notice giving reasons, and telling you about the Review Tribunal.",
                            "拒絕批給。發出書面通知載明理由，並告知可向覆核審裁處申請覆核。"), "s.30(8)–(9)", 'stop', answer=True)
    GRANT = Node(330, 540, ("Licence granted, valid for 2 years unless the Commissioner sets another period. Any condition he thinks fit may be endorsed on it.",
                            "批給牌照：有效期2年，除非關長另定期間；並可批註關長認為合適的條件。"), "s.30(5), (10) · s.33", 'ok', answer=True)
    OPER = Node(330, 540, ("Operating. Display the original at the specified premises and notify changes within one month. Get written approval before anyone becomes a director, partner or ultimate owner, and have new premises added to the licence first.",
                           "經營期間：在指明處所的顯眼地方展示牌照正本；詳情改變後的一個月內須具報。新董事、合夥人或最終擁有人須先獲書面批准；新處所須先加入牌照。"),
                "s.39A · s.40 · s.35–39", 'must', answer=True)
    BW, BX = 184, (34, 228, 422, 616, 810)
    outs = [
        (("Renew: apply not later than 45 days before expiry",
          "續期：申請須於期滿前45日或之前提出"), "s.31(2)(a)", 'ok'),
        (("It expires: not renewed, so it lapses when its period runs out. Trading on is unlicensed operation",
          "期滿失效：牌照未獲續期，即於有效期屆滿時失效；其後繼續經營即屬無牌經營"), "s.30(10) · s.29(1)", 'stop'),
        (("Revoked, or suspended for a time: no longer fit and proper, or consent to enter domestic premises revoked or refused",
          "撤銷或暫時吊銷一段時間：有人已不再是適當人選；或住宅處所的進入同意被撤銷或遭拒絕給予"), "s.34(1)–(2)", 'may'),
        (("You stop: notify in writing before the date, and return the licence within 7 days beginning on it",
          "主動停業：須在停業日期前以書面向關長具報該意向，並在自停業日期起計7日內交回牌照"), "s.41(1)", 'must'),
        (("It simply ends: death, dissolution of the partnership, or commencement of winding up",
          "牌照不再有效：持牌個人去世、合夥解散，或法團開始清盤"), "s.42", 'stop'),
    ]
    # measure the five outcomes, then give them one height so the row lines up
    hh = max(Node(x, BW, t, c).h for x, (t, c, k) in zip(BX, outs))
    BOTTOM = tuple(Node(x, BW, t, c, k, answer=True, minh=hh) for x, (t, c, k) in zip(BX, outs))
    RENEW, EXPIRE, REVOKE, CEASE, AUTO = BOTTOM
    H = place([([APPLY], 34), ([TEST], 40), ([REFUSE, GRANT], 34), ([OPER], 44), (list(BOTTOM), 0)])
    b = [n.render() for n in (APPLY, TEST, REFUSE, GRANT, OPER) + BOTTOM]
    m = 'p5a'
    b.append(edge([APPLY.bottom, TEST.top], mid=m))
    b.append(edge([TEST.left, (REFUSE.cx, TEST.cy), REFUSE.top], ("no", "否"), TEST.x - 14, TEST.cy - 8, 'end', mid=m))
    b.append(edge([TEST.bottom, GRANT.top], ("yes", "是"), TEST.cx + 10, (TEST.bottom[1] + GRANT.top[1]) / 2 + 5, 'start', mid=m))
    b.append(edge([GRANT.bottom, OPER.top], mid=m))
    # one trunk, one bus, then a short drop into each outcome
    fy = OPER.bottom[1] + 22
    b.append(edge([OPER.bottom, (OPER.cx, fy)], marker=False, mid=m))
    b.append(edge([(RENEW.cx, fy), (AUTO.cx, fy)], marker=False, mid=m))
    for n in BOTTOM:
        b.append(edge([(n.cx, fy), n.top], mid=m))
    # renewal goes back through the same test
    b.append(edge([RENEW.left, (16, RENEW.cy), (16, APPLY.cy), (APPLY.x, APPLY.cy)], mid=m))
    b.append(loop_label((16 + APPLY.x) / 2, APPLY.cy - 8, "renewal re-runs the same test · s.31(4)", "續期時重做同一測試 · 第31(4)條"))
    aria = ("The licence lifecycle. An application with the Schedule 3 fee is tested on whether everyone who must be a fit and proper person is one, and whether the premises are suitable. Refusal comes with reasons and a Review Tribunal route. A grant normally lasts two years, and any conditions are endorsed on it. While operating you display the licence and notify changes within a month; new directors, partners and ultimate owners need prior written approval, and new premises must be added to the licence first. The licence is then either renewed, on an application made not later than 45 days before expiry and on the same test, or it expires unrenewed, is revoked or suspended by the Commissioner, ends by your own cessation, or ends automatically on death, dissolution or winding up.",
            "牌照的生命周期。申請連同附表3費用，須經測試：所有須屬適當人選的人是否適當人選，以及處所是否適合。拒絕批給須附理由，並可向覆核審裁處申請覆核。批給的牌照一般有效兩年（關長可另定期間），如有條件須批註在牌照上。經營期間須展示牌照，並於一個月內具報改變；新董事、合夥人及最終擁有人須事先取得書面批准，新處所須先加入牌照。其後牌照或予續期（續期申請須在期滿前45日或之前提出，並再次通過同一測試），或因沒有續期而期滿失效、被關長撤銷或暫時吊銷、主動停業，或因持牌人去世、合夥解散、法團開始清盤而不再有效。")
    return svg(W, H + 16, ''.join(b), aria, m, 860)


def fig_gate():
    W = 1000
    WANT = Node(300, 400, ("Someone is to become a director, an ultimate owner, or a partner of the licensee",
                           "某人將成為持牌人的董事、最終擁有人或合夥人"), "s.35(1) · s.36(1) · s.37(1)")
    APP = Node(300, 400, ("The licensee applies, in the specified form and manner, with the Schedule 3 fee",
                          "由持牌人以指明格式及方式提出申請，並附隨附表3費用"), "s.35(2) · s.36(2) · s.37(2)")
    SAT = Node(230, 540, ("Is that person fit and proper? The Commissioner weighs the same s.30(4) factors",
                          "該人是否適當人選？關長按第30(4)條同一組因素判斷"), "s.35(3)–(4) · s.36(3)–(4) · s.37(3)–(4)", shape='hex')
    yes_t = ("Approval in writing: only then may the person become a director, ultimate owner or partner", "書面批准後，該人方可成為董事、最終擁有人或合夥人")
    no_t = ("Refused. Written notice giving reasons, and the Review Tribunal route.", "拒絕批准。關長須發出書面通知，載明作出該項決定的理由，並提示你可向覆核審裁處申請覆核。")
    # measure both outcome boxes, then give them one height so the pair lines up
    yc, nc = "s.35(1) · s.36(1) · s.37(1)", "s.35(5)–(6) · s.36(5)–(6) · s.37(5)–(6)"
    # boxes set inward so the yes/no legs leave the flat bottom edge of the hexagon, not its corners
    hh = max(Node(70, 410, yes_t, yc).h, Node(520, 410, no_t, nc).h)
    YES = Node(70, 410, yes_t, yc, 'ok', answer=True, minh=hh)
    NO = Node(520, 410, no_t, nc, 'stop', answer=True, minh=hh)
    OFF = Node(230, 540, ("Taking office first is an offence: a fine at level 5 and 6 months, unless there is a reasonable excuse",
                          "未獲批准而先行就任即屬犯罪：第5級罰款及監禁6個月，除非有合理辯解"), "s.35(7) · s.36(7) · s.37(7)", 'must', answer=True)
    H = place([([WANT], 32), ([APP], 36), ([SAT], 44), ([YES, NO], 44), ([OFF], 0)])
    b = [n.render() for n in (WANT, APP, SAT, YES, NO, OFF)]
    m = 'p5b'
    b.append(edge([WANT.bottom, APP.top], mid=m))
    b.append(edge([APP.bottom, SAT.top], mid=m))
    sb = SAT.y + SAT.h
    ly = (sb + YES.y) / 2 + 5
    b.append(edge([(YES.cx, sb), YES.top], ("yes", "是"), YES.cx + 10, ly, 'start', mid=m))
    b.append(edge([(NO.cx, sb), NO.top], ("no", "否"), NO.cx - 10, ly, 'end', mid=m))
    # the shortcut that skips the gate: dashed red, straight into the offence
    pts = [WANT.left, (16, WANT.cy), (16, OFF.cy), (OFF.x, OFF.cy)]
    d = ' '.join(f'{x:.0f},{y:.0f}' for x, y in pts)
    red = mref(m) + 'r'
    b.append(f'<defs><marker id="{red}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
             f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--red)"/></marker></defs>')
    b.append(f'<polyline class="e e-dash" style="stroke:var(--red)" points="{d}" marker-end="url(#{red})"/>')
    b.append(loop_label(123, OFF.cy - 8, "skipping the gate", "繞過此關"))
    aria = ("The approval gate. A new director, ultimate owner or partner needs the Commissioner's written approval before taking office. The licensee applies with the fee, the Commissioner applies the same fit and proper factors as on a licence application, and a refusal carries reasons and a Review Tribunal route. Taking office without approval is an offence punishable by a level 5 fine and six months.",
            "批准關卡。新的董事、最終擁有人或合夥人須先取得關長書面批准方可就任。由持牌人繳費申請，關長按與牌照申請相同的適當人選因素審核；拒絕時須附理由，並可向覆核審裁處申請覆核。未獲批准而就任即屬犯罪，可處第5級罰款及監禁6個月。")
    return svg(W, H + 16, ''.join(b), aria, m, 820)
