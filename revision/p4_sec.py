# AMLO Part 4: disciplinary actions by relevant authorities. Figure plus content.
from bl_core import *
import ui as U
from ui import Card


LBL_LH = 17   # line step for the edge labels (13.5px bold on screen)


def side_label(x, y_top, en_lines, tc_lines, anchor='start'):
    """An edge label set beside a vertical drop, its first line starting just under y_top."""
    out = []
    for v, ls in (('en', en_lines), ('tc', tc_lines), ('both', en_lines + tc_lines)):
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x:.0f}" y="{y_top + 13 + i * LBL_LH:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


class LCard(Card):
    """A Card whose title and body may carry forced line breaks ('\\n'), so Chinese
    penalty figures break between phrases rather than inside a word."""

    def __init__(self, x, w, title, body=None, kind='plain', cite=None, size=11.5, tsize=12.5, answer=False):
        flat = lambda t: tuple(s.replace('\n', '') for s in t) if t else t
        super().__init__(x, w, flat(title), flat(body), kind, cite, size=size, tsize=tsize, answer=answer)
        size, tsize = size * FS, tsize * FS
        inner = w - 24

        def lines(text, sz):
            return [l for part in text.split('\n') for l in wrap(part, inner, sz)] if text else []
        for i, v in enumerate(('en', 'tc')):
            tcls = 't-inv t-b' if kind == 'stop' else 't t-b'
            bcls = 't-inv' if kind == 'stop' else 't'
            self.seg[v] = ([(l, tcls, tsize) for l in lines(title[i], tsize)]
                           + [(l, bcls, size) for l in lines(body[i] if body else '', size)])
        self.seg['both'] = self.seg['en'] + self.seg['tc']
        self.h = sum(s * LH for _, _, s in self.seg[lay()]) + 16 + (CS * LH if cite else 0)


def fig_doors():
    W = 1000
    m = 'p4'
    Card = LCard
    BR = Card(240, 520, ("A licensed money service operator breaches a rule",
                         "持牌金錢服務經營者違反某項規定"), None)
    SPEC = Card(10, 480, ("A Schedule 2 specified provision", "附表2的指明的條文"),
                ("Schedule 2 duties listed in s.5(11), including CDD, ongoing monitoring, wire transfers, remittance transactions, record keeping, AML/CFT systems",
                 "第5(11)條列明的附表2責任，包括\n客戶盡職審查、持續監察、電傳轉帳、\n匯款交易、備存紀錄及打擊洗錢制度"), 'plain', "s.5(11)")
    LIC = Card(510, 480, ("A licence condition, an s.51 regulation or a Part 5 duty", "牌照條件、第51條規例或第5部責任"),
               ("The duties in s.35(1), 36(1), 37(1), 38(1), 39(1), 39A(1), 40(1), 41(1)",
                "第5部責任指第35(1)、36(1)、37(1)、38(1)、39(1)、39A(1)、40(1)、41(1)條"), 'plain', "s.43(1)")
    S5 = Card(10, 230, ("Criminal offence", "刑事罪行"),
              ("On indictment.\nKnowing:\n$1,000,000 and 2 years.\nIntent to defraud:\n$1,000,000 and 7 years",
               "循公訴程序定罪。\n明知而違反：\n罰款$1,000,000及監禁2年。\n出於詐騙意圖：\n罰款$1,000,000及監禁7年"),
              'stop', "s.5(5)–(6)", answer=True)
    S21 = Card(255, 235, ("Part 4 discipline", "第4部紀律行動"),
               ("By the relevant authority. Up to the greater of $10,000,000 or 3× profit gained or costs avoided",
                "由有關當局執行。罰款上限：\n$10,000,000或因該項違反而\n獲取的利潤或避免的開支的\n金額的3倍，以較大者為準"),
               'must', "s.21", answer=True)
    S43 = Card(510, 235, ("Part 5 discipline", "第5部紀律行動"),
               ("By the Commissioner, over licensees only. Penalty up to $1,000,000",
                "由關長執行，只可針對持牌人。\n罰款上限為$1,000,000"),
               'may', "s.43", answer=True)
    OFF = Card(760, 230, ("A separate offence", "該責任所屬條文的罪行"),
               ("Level 5 fine;\nfor s.35 to 39 also\n6 months' imprisonment.\nUnder s.35 to 37 the offender is whoever becomes a director, ultimate owner or partner without approval",
                "第5級罰款；\n第35至39條另可處監禁6個月。\n第35至37條的犯罪者為未獲批准\n而成為董事、最終擁有人或\n合夥人的人"),
               'stop', "s.35–41", answer=True)
    HEARD = Card(255, 490, ("First a reasonable opportunity to be heard, then a written notice", "先給予合理的陳詞機會，再發出書面通知"),
                 ("Reasons, any reprimand, action required and penalty, and your right to seek review",
                  "理由、譴責內容、須採取的行動、罰款，以及可申請覆核的提示"), 'plain', "s.22 · s.44")
    TRIB = Card(110, 340, ("Review Tribunal", "覆核審裁處"),
                ("You may apply to it for a review", "你可申請覆核該決定"),
                'ok', "s.22(3)(e) · s.44(3)(e)", answer=True)
    CFI = Card(500, 390, ("Unpaid penalty: Court of First Instance", "未繳罰款：原訟法庭"),
               ("On the authority's application the court may register the order, which then counts as a court order for payment of money",
                "原訟法庭可應當局申請登記該命令；\n登記後即視為原訟法庭就繳付款項而作出的命令"),
               'plain', "s.21(5)–(6) · s.43(5)–(6)", answer=True)

    # the four branch labels; the gap under the second row is sized to the tallest one in this view
    labs = {
        'crim': (["if knowing, or", "intent to defraud"], ["如屬明知或意圖詐騙"]),
        'p4': (["any breach"], ["任何違反"]),
        'p5': (["any breach"], ["任何違反"]),
        'off': (["listed duty, without", "reasonable excuse"], ["所列責任，無合理辯解"]),
    }
    v = lay()
    nmax = max(len(en if v == 'en' else tc if v == 'tc' else en + tc) for en, tc in labs.values())
    gap2 = 30 + nmax * LBL_LH + 10
    H = place([([BR], 44), ([SPEC, LIC], gap2), ([S5, S21, S43, OFF], 48), ([HEARD], 48), ([TRIB, CFI], 0)])
    # top-align rows 2 and 3 so the forks, branch labels and the four "doors" sit on one line
    for row in ((SPEC, LIC), (S5, S21, S43, OFF)):
        top = min(n.y for n in row)
        for n in row:
            n.y = top
    b = [n.render() for n in (BR, SPEC, LIC, S5, S21, S43, OFF, HEARD, TRIB, CFI)]

    # top fork: what did you break
    jy = BR.bottom[1] + 20
    b.append(edge([BR.bottom, (BR.cx, jy), (SPEC.cx, jy), SPEC.top], mid=m))
    b.append(edge([BR.bottom, (BR.cx, jy), (LIC.cx, jy), LIC.top], mid=m))

    # second forks: each drop lands a quarter of the way into its box, its label just to its right
    fy = max(SPEC.bottom[1], LIC.bottom[1]) + 18   # one fork line for both parents

    def drops(parent, kids):
        for node, key in kids:
            x = node.x + 44
            b.append(edge([parent.bottom, (parent.cx, fy), (x, fy), (x, node.y)], mid=m))
            en, tc = labs[key]
            b.append(side_label(x + 7, fy + 4, en, tc))
    drops(SPEC, [(S5, 'crim'), (S21, 'p4')])
    drops(LIC, [(S43, 'p5'), (OFF, 'off')])

    # both disciplinary routes need a reasonable opportunity to be heard first; the criminal and offence boxes stop
    b.append(edge([S21.bottom, (S21.cx, HEARD.y)], mid=m))
    b.append(edge([S43.bottom, (S43.cx, HEARD.y)], mid=m))
    ey = HEARD.bottom[1] + 22
    b.append(edge([HEARD.bottom, (HEARD.cx, ey), (TRIB.cx, ey), TRIB.top], mid=m))
    b.append(edge([HEARD.bottom, (HEARD.cx, ey), (CFI.cx, ey), CFI.top], mid=m))
    aria = ("Breaching a Schedule 2 specified provision always exposes you to Part 4 disciplinary action by the relevant authority; if the breach was knowing or made with intent to defraud a relevant authority, it is also a criminal offence under section 5. Breaching a licence condition, a section 51 regulation or a listed Part 5 duty exposes you to the Commissioner's section 43 disciplinary power instead; each listed Part 5 duty is also an offence in its own section if broken without reasonable excuse. Both disciplinary routes require a reasonable opportunity to be heard and a written notice, and lead to the Review Tribunal and, for an unpaid penalty, to registration in the Court of First Instance.",
            "違反附表2的指明的條文，必定可招致有關當局根據第4部採取紀律行動；如屬明知而違反，或出於詐騙任何有關當局的意圖而違反，亦屬第5條的罪行。違反牌照條件、第51條規例或所列的第5部責任，則可招致關長根據第43條採取紀律行動；所列的每項第5部責任，如無合理辯解而違反，本身亦屬罪行。兩條紀律途徑都須先給予合理的陳詞機會及發出書面通知，其後可向覆核審裁處申請覆核；罰款未繳，可在原訟法庭登記。")
    return svg(W, H + 16, ''.join(b), aria, m, 860)


def h(en, tc):
    return f'<th>{B(en, tc)}</th>'


def rh(en, tc, cite=None):
    return f'<th class="rowh">{B(en, tc)}{cite_html(cite)}</th>'


def d(en, tc, cite=None, cls=''):
    k = f' class="{cls}"' if cls else ''
    body = f'<span class="answer" tabindex="0">{B(en, tc)}</span>' if cls == 'pen' else B(en, tc)
    return f'<td{k}>{body}{cite_html(cite)}</td>'


def table(head, rows, note=None, minw=760):
    t = '<thead><tr>' + head + '</tr></thead>' if head else ''
    n = f'<tr class="note"><td colspan="9">{note}</td></tr>' if note else ''
    return f'<div class="tbl"><table style="min-width:{minw}px">{t}<tbody>{rows}{n}</tbody></table></div>'


# ---------------------------------------------------------------- A. three doors
CMP = table(
    h("", "") + h("Part 4, section 21", "第4部第21條") + h("Part 5, section 43", "第5部第43條") + h("Section 5, the offence", "第5條：罪行"),
    ''.join([
        '<tr>' + rh("Who acts", "由誰執行")
        + d("The <b>relevant authority</b>. For a money service operator that is the Commissioner of Customs and Excise.", "<b>有關當局</b>。就金錢服務經營者而言，即海關關長。", "Sch. 1 Pt 2")
        + d("The <b>Commissioner</b>, and only over a licensee.", "<b>關長</b>，且只可針對持牌人。", "s.43(1)")
        + d("Prosecution in the criminal courts.", "在刑事法院提出檢控。", "s.5(5)–(8)") + '</tr>',
        '<tr>' + rh("What triggers it", "觸發條件")
        + d("Contravening a <b>specified provision</b>, which s.5(11) defines by listing Schedule 2 duties, including CDD, ongoing monitoring, wire transfers, remittance transactions, record keeping and AML/CFT systems. Unlike s.5, the breach need not be knowing.", "違反<b>指明的條文</b>；第5(11)條以列出附表2條文的方式界定，包括客戶盡職審查、持續監察、電傳轉帳、匯款交易、備存紀錄及打擊洗錢制度等責任。與第5條不同，毋須屬明知而違反。", "s.21(1) · s.5(11) · s.13 Sch. 2")
        + d("Contravening a regulation made under s.51, a <b>condition of the licence</b>, or one of the Part 5 duties in s.35(1), 36(1), 37(1), 38(1), 39(1), 39A(1), 40(1) or 41(1). Each of those eight duties is also an offence in its own section if broken without reasonable excuse; under s.35 to 37 the offender is the person who becomes a director, ultimate owner or partner without approval, who need not be the licensee.", "違反根據第51條訂立的規例、<b>牌照條件</b>，或第35(1)、36(1)、37(1)、38(1)、39(1)、39A(1)、40(1)或41(1)條所訂的第5部責任。該八項責任如無合理辯解而違反，本身亦各屬所屬條文的罪行；第35至37條的犯罪者為未獲批准而成為董事、最終擁有人或合夥人的人，該人不一定是持牌人。", "s.43(1) · s.35–41")
        + d("The same specified provision, but only when contravened <b>knowingly</b>, or with <b>intent to defraud</b> a relevant authority. Neither s.5 nor s.21 makes one route rule out the other.", "同樣是指明的條文，但須屬<b>明知而違反</b>，或<b>出於詐騙任何有關當局的意圖</b>而違反。第5條及第21條均沒有規定其中一條途徑排除另一條。", "s.5(5)–(6) · s.21(1)") + '</tr>',
        '<tr>' + rh("How many powers at once", "可同時行使多少項權力")
        + d("<b>Any one or more</b> of the three: public reprimand, remedial order, pecuniary penalty. One breach can bring all three.", "三項權力中的<b>一項或多於一項</b>：公開譴責、糾正命令、罰款。同一違反可招致全部三項。", "s.21(1)")
        + d("The same: any one or more of the three.", "相同：三項中的一項或多於一項。", "s.43(1)")
        + d("—", "—") + '</tr>',
        '<tr class="peak">' + rh("The ceiling", "上限")
        + d("The <b>greater</b> of $10,000,000 or <b>3 times</b> the profit gained or costs avoided as a result of the contravention.", "$10,000,000或因該項違反而令該機構獲取的利潤或避免的開支的金額的<b>3倍</b>，以<b>較大者</b>為準。", "s.21(2)(c)", 'pen')
        + d("<b>$1,000,000</b> flat. No multiple of profit gained or costs avoided.", "劃一為<b>$1,000,000</b>，不設按利潤或開支計算的倍數。", "s.43(2)(c)", 'pen')
        + d("<b>Knowing</b> breach: on indictment <b>$1,000,000 and 2 years</b>; summarily level 6 and 6 months. With <b>intent to defraud</b> a relevant authority: on indictment $1,000,000 and 7 years; summarily $500,000 and 1 year.", "<b>明知而違反</b>：循公訴程序定罪，<b>罰款$1,000,000及監禁2年</b>；簡易程序定罪，第6級罰款及監禁6個月。<b>出於詐騙任何有關當局的意圖</b>：循公訴程序定罪，罰款$1,000,000及監禁7年；簡易程序定罪，罰款$500,000及監禁1年。", "s.5(5)–(6)", 'pen') + '</tr>',
        '<tr>' + rh("The other two powers", "另外兩項權力")
        + d("Publicly reprimand; and order remedial action by a specified date.", "公開譴責；並命令在指明日期或之前採取糾正行動。", "s.21(2)(a)–(b)")
        + d("The same two: public reprimand and a remedial order.", "同樣兩項：公開譴責及命令採取糾正行動。", "s.43(2)(a)–(b)")
        + d("—", "—") + '</tr>',
        '<tr>' + rh("Ignoring the remedial order", "不遵從糾正命令")
        + d("The authority <b>may further order</b> a daily penalty of up to <b>$100,000</b> for each day the failure continues after the date set.", "有關當局<b>可進一步命令</b>繳付按日罰款，就限期後持續不遵從的每一日，最高<b>$100,000</b>。", "s.21(4)", 'pen')
        + d("The Commissioner <b>may further order</b> a daily penalty of up to <b>$10,000</b> a day.", "關長<b>可進一步命令</b>繳付按日罰款，每日最高<b>$10,000</b>。", "s.43(4)", 'pen')
        + d("—", "—") + '</tr>',
        '<tr>' + rh("Paying", "繳付")
        + d("Within <b>30 days</b> after the order takes effect as a specified decision under s.75, or any longer period the notice specifies.", "在命令根據第75條作為指明決定而生效後<b>30日</b>內繳付，或通知指明的較長期間。", "s.21(3)")
        + d("The same 30 days, with the longer period set by a notice under s.44(2).", "同樣是30日，較長期間由第44(2)條的通知指明。", "s.43(3)")
        + d("A fine on conviction.", "定罪後繳付罰款。", "s.5(5)–(6)") + '</tr>',
        '<tr>' + rh("Before acting", "行使權力之前")
        + d("A <b>reasonable opportunity to be heard</b> is mandatory.", "必須先給予<b>合理的陳詞機會</b>。", "s.22(1)")
        + d("The same requirement.", "規定相同。", "s.44(1)")
        + d("The ordinary criminal process.", "按一般刑事程序處理。", "—") + '</tr>',
        '<tr>' + rh("Enforcing the penalty", "強制執行罰款")
        + d("On the authority's application, the <b>Court of First Instance may register</b> the order. The application is made by producing to the Registrar of the High Court a written notice plus the original order and a copy. Once registered, the order counts as a Court of First Instance order for the payment of money, made in its civil jurisdiction.", "<b>原訟法庭可</b>應有關當局的申請登記該命令；申請方式是向高等法院司法常務官交出書面通知，以及命令正本及一份複本。一經登記，即視為原訟法庭在其民事司法管轄權範圍內就繳付款項而作出的命令。", "s.21(5)–(6)")
        + d("Identical machinery.", "機制完全相同。", "s.43(5)–(6)")
        + d("—", "—") + '</tr>',
        '<tr>' + rh("Publicity", "公開")
        + d("The authority <b>may</b> disclose the decision, its reasons and any material facts.", "有關當局<b>可</b>披露決定、理由及任何重要事實。", "s.21(8)")
        + d("The same discretion.", "酌情權相同。", "s.43(7)")
        + d("— (s.5 has no publicity provision)", "—（第5條沒有公開披露的條文）", "s.5") + '</tr>',
        '<tr>' + rh("Two points only in Part 4", "只見於第4部的兩點")
        + d("Penalties received are paid into <b>general revenue</b>; and the penalty powers cannot be used against the <b>Government</b>.", "所收罰款須撥入<b>政府一般收入</b>；罰款權力不可針對<b>政府</b>行使。", "s.21(7), (9)")
        + d("Neither provision appears in s.43.", "第43條沒有這兩項條文。", "—")
        + d("—", "—") + '</tr>',
    ]))

A = sec('doors', [("Part 4", "第4部"), "s.20A–s.23", ("with s.5, s.43", "另及第5、43條")],
        ("One breach, three doors", "一次違規，三道門"),
    P("Start at the top of the diagram and follow what you actually broke; the words beside each arrow say when that door opens. Breaking a <b>Schedule 2 duty</b> always opens the Part 4 door. It also opens the criminal door if the breach was <b>knowing</b> or made with <b>intent to defraud</b>; neither s.5 nor s.21 makes one door shut the other. Breaking a <b>licence condition or a Part 5 duty</b> opens the Commissioner's s.43 door instead, with a penalty ceiling at most a tenth as high. Each of the eight Part 5 duties it lists is also an offence in its own section if broken without reasonable excuse (see the Part 5 page: <a href=\"#p5-approvals\">approvals</a> and <a href=\"#p5-duties\">ongoing duties</a>). Picking the wrong door is the easiest mark to lose here.",
      "由圖的頂端開始，順着你實際違反了甚麼往下看；每條箭咀旁的字說明該道門何時開啟。違反<b>附表2的責任</b>，必定開啟第4部的門；如屬<b>明知而違反</b>，或<b>出於詐騙意圖</b>而違反，亦會開啟刑事的門；第5條及第21條均沒有規定開啟其中一道門便排除另一道。違反<b>牌照條件或第5部的責任</b>，開啟的則是關長第43條的門，罰款上限最多只有十分之一。該條所列的八項第5部責任，如無合理辯解而違反，本身亦各屬所屬條文的罪行（見第5部一頁的<a href=\"#p5-approvals\">批准</a>及<a href=\"#p5-duties\">持續責任</a>）。選錯門，是這裏最容易失的分。")
    + U.fig(fig_doors,
            ("Section 20A takes licensed virtual asset service providers out of Part 4 entirely by excluding them from the meaning of financial institution. Everything else in the Part reads as normal for a money service operator.",
             "第20A條把持牌虛擬資產服務提供者排除於「金融機構」的涵義之外，因此第4部完全不適用於他們。就金錢服務經營者而言，本部其餘條文如常適用。"),
            U.legend([('must', ("Part 4 discipline", "第4部紀律行動")), ('may', ("Part 5 discipline", "第5部紀律行動")),
                      ('stop', ("criminal offence", "刑事罪行")), ('ok', ("your review route", "你的覆核途徑")),
                      ('', ("what you broke, or a step", "違反的規定或程序步驟"))]))
    + CMP)

# ---------------------------------------------------------------- B. procedure
B_ = sec('procedure', ["s.22 · s.23", ("also s.44–45", "另及第44、45條")],
         ("The procedure, and the guidelines that must come first", "程序，以及必須先行的指引"),
    P("Both disciplinary routes, Part 4 and Part 5, follow the same steps. Read the table down, in the order things happen.",
      "第4部及第5部兩條紀律途徑的步驟相同。按事情發生的次序往下閱讀此表。")
    + table(h("Step", "步驟") + h("What the law requires", "法律規定"), ''.join([
        '<tr>' + rh("Before any penalty exists", "在施加任何罰款之前", "s.23 · s.45") + d("The authority must have <b>published guidelines in the Gazette</b>, and in any other manner it thinks fit, on how it will use the penalty power, before it first uses it; and it must have regard to them each time. They are not subsidiary legislation",
                                                                                                    "有關當局須<b>先在憲報</b>及以其認為適當的其他方式公布指引，說明其擬如何行使罰款權力，方可首次行使；其後每次施加罰款都須顧及該等指引。指引並非附屬法例") + '</tr>',
        '<tr>' + rh("Before deciding", "作出決定之前", "s.22(1) · s.44(1)") + d("A <b>reasonable opportunity to be heard</b>", "必須先給予<b>合理的陳詞機會</b>") + '</tr>',
        '<tr>' + rh("The decision notice", "決定通知", "s.22(2)–(3) · s.44(2)–(3)") + d("In writing, with five contents: (1) the <b>reasons</b>; (2) the terms of any <b>reprimand</b>; (3) any <b>action</b> required; (4) any <b>penalty</b>, with the payment period if it is not the standard 30 days; (5) a statement that you may apply to the <b>Review Tribunal</b>",
                                                                                                  "以書面發出，載有五項內容：(1) <b>理由</b>；(2) 任何<b>譴責</b>的內容；(3) 須採取的任何<b>行動</b>；(4) 任何<b>罰款</b>，以及（如非標準的30日）繳付期限；(5) 可向<b>覆核審裁處</b>申請覆核該決定的提示") + '</tr>',
        '<tr>' + rh("Paying", "繳付", "s.21(3) · s.43(3)") + d("Within 30 days after the order takes effect as a specified decision, or any longer period the notice allows", "在命令作為指明決定生效後30日內繳付，或通知容許的較長期間") + '</tr>',
        '<tr>' + rh("If you do not pay", "如你不繳付", "s.21(5)–(6) · s.43(5)–(6)") + d("On the authority's application the Court of First Instance may register the order; once registered it is regarded as a Court of First Instance order, made within its civil jurisdiction, for the payment of money", "原訟法庭可應有關當局的申請登記該命令；一經登記，即視為原訟法庭在其民事司法管轄權範圍內就繳付款項而作出的命令") + '</tr>',
        '<tr>' + rh("Publicity", "公開", "s.21(8) · s.43(7)") + d("The authority may publish the decision, its reasons and any material facts", "有關當局可公布決定、理由及任何重要事實") + '</tr>',
    ]), minw=660)
    + numreq([
        (("$10,000,000 or 3× profit gained / costs avoided", "$10,000,000或獲取的利潤／避免的開支的金額的3倍"),
         ("The ceiling on a single pecuniary penalty, taken as whichever is greater", "單一罰款的上限，以兩者中較大者為準"),
         ("You contravened a Schedule 2 specified provision and the Commissioner acts under Part 4", "你違反附表2的指明的條文，而關長根據第4部採取行動"),
         ("On the authority's application the Court of First Instance may register the order; once registered it is treated as a Court of First Instance order for the payment of money", "原訟法庭可應有關當局的申請登記該命令；一經登記，即視為原訟法庭就繳付款項而作出的命令"),
         "s.21(2)(c), (5)–(6)"),
        (("Up to $100,000 a day", "每日最高$100,000"),
         ("A daily penalty the authority may further order if a remedial order is not complied with", "不遵從糾正命令時，有關當局可進一步命令繳付的按日罰款"),
         ("A Part 4 remedial order was made and you did not act by the date it specified", "第4部下已作出糾正命令，而你未能在命令指明的日期前採取行動"),
         ("Can be ordered for each day the failure continues after that date, whether or not a pecuniary penalty was also imposed", "可就沒有遵從的狀況於該日期後持續的每一日下令繳付，不論是否另有罰款"),
         "s.21(4)"),
        (("$1,000,000", "$1,000,000"),
         ("The whole ceiling when the Commissioner uses his own Part 5 power instead", "關長改為行使第5部自身權力時的整體上限"),
         ("You broke a regulation, a licence condition, or one of the Part 5 duties in sections 35 to 41", "你違反規例、牌照條件，或第35至41條所訂的第5部責任"),
         ("Same enforcement machinery, at most a tenth of the Part 4 ceiling", "強制執行機制相同，上限則最多只有第4部的十分之一"),
         "s.43(2)(c)"),
        (("Up to $10,000 a day", "每日最高$10,000"),
         ("The Part 5 daily penalty the Commissioner may further order for ignoring a remedial order", "不理會糾正命令時，關長可根據第5部進一步命令繳付的按日罰款"),
         ("The same trigger, under the Commissioner's Part 5 power", "觸發條件相同，但屬關長的第5部權力"),
         ("Can be ordered for each day the failure continues after the specified date", "可就沒有遵從的狀況於指明日期後持續的每一日下令繳付"),
         "s.43(4)"),
        (("30 days", "30日"),
         ("Pay a pecuniary penalty once it is due", "罰款到期後的繳付期限"),
         ("Counted from when the order takes effect as a specified decision, unless the notice allows longer", "自命令作為指明決定而生效時起計，除非通知容許較長期間"),
         ("The authority may apply to have the order registered in the Court of First Instance; once registered it is regarded as a Court of First Instance order, made within its civil jurisdiction, for the payment of money", "有關當局可申請在原訟法庭登記該命令；一經登記，即視為原訟法庭在其民事司法管轄權範圍內就繳付款項而作出的命令"),
         "s.21(3) · s.43(3)"),
    ])
    + P("The Part 2 criminal offences, including those that reach your staff and the one defence written for employees, are laid out on the <a href=\"#p2-offences\">Part 2 page</a>.",
        "第2部的刑事罪行，包括涉及你的僱員的罪行，以及專為僱員而設的免責辯護，詳見<a href=\"#p2-offences\">第2部一頁</a>。")
    + U.traps(
        U.trap(("Part 4 or Part 5: a tenfold difference or more", "第4部或第5部：相差至少十倍"), None, "s.21(2)(c), (4) · s.43(2)(c), (4)",
               vs=[(("Part 4, a Schedule 2 breach", "第4部：違反附表2"), ("Up to $10,000,000 or 3 times the profit gained or costs avoided as a result of the contravention, whichever is greater; up to $100,000 a day for ignoring a remedial order.", "最高$10,000,000或因該項違反而令你獲取的利潤或避免的開支的金額的3倍，以金額較大者為準；不遵從糾正命令，每日最高$100,000。")),
                   (("Part 5, a licence breach", "第5部：違反牌照規定"), ("Up to $1,000,000 flat; up to $10,000 a day.", "劃一最高$1,000,000；每日最高$10,000。"))]),
        U.trap(("The Government escapes the money, not the reprimand", "政府可免罰款，但不免譴責"),
               ("Part 4's pecuniary penalty and daily penalty cannot be imposed on the Government, which matters because the Postmaster General is a financial institution. A public reprimand and a remedial order still can be.",
                "第4部的罰款及每日罰款不可向政府施加；由於郵政署署長屬金融機構，這一點有實際意義。公開譴責及糾正命令則仍可施加。"),
               "s.21(9) · Sch. 1 Pt 2"),
        U.trap(("Part 4 stops at licensed virtual asset providers", "第4部不適用於持牌虛擬資產服務提供者"),
               ("Section 20A takes licensed VAS providers out of the meaning of financial institution for Part 4, so none of its powers reach them. Everything in it still reaches you.",
                "第20A條把持牌虛擬資產服務提供者排除於第4部「金融機構」的涵義之外，故第4部的權力完全不適用於他們；但對你全部適用。"),
               "s.20A"),
    ))

# ---------------------------------------------------------------- C. numbers
P4_NAV = [('doors', 'Three doors', '三道門'), ('procedure', 'Procedure', '程序')]
P4_BODY = A + B_
