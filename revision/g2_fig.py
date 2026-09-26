# Figures for the Guideline Chapter 2 page: the institutional risk assessment cycle,
# the three look-alike lists of areas and factors, and the life of a customer rating.
from ui import *
from bl_core import _runs
from bl_figs import lines_down
from gl_fig import dash


# ---------------------------------------------------------------- 1. institutional assessment cycle
def dashkey(items, en, tc):
    """A legend with a dashed-line swatch appended (legend() has no kind for a line)."""
    sw = ('<span><i style="height:0;border:0;border-top:2px dashed var(--text);border-radius:0"></i>'
          f'{B(en, tc, True)}</span>')
    return legend(items)[:-len('</div>')] + sw + '</div>'


def fig_ira():
    W = 1000
    L, LW = 50, 510          # left column: the steps
    R_, RW = 610, 360        # right column: the factors, and what sits beside the steps
    IN = Card(L, LW, ("What you draw on", "資料來源"),
              ("Quantitative and qualitative information from relevant internal and external sources, which may include risk assessments and guidance by the FATF, inter-governmental organisations, governments and authorities, Hong Kong's jurisdiction-wide risk assessment and any higher risks the CCE notifies",
               "從相關內部與外部來源取得的數量及質量分析資料，可包括特別組織、跨政府組織、各地政府及主管當局發出的相關風險評估及導引，包括香港在司法管轄區層面的風險評估，以及關長通報的任何較高風險"),
              'plain', "¶2.6")
    FACT = Card(R_, RW, ("What you weigh", "須考慮的因素"),
                ("Customer, country, product, service or transaction, delivery channel and other risk factors, across four areas. The next section lists every one",
                 "客戶、國家、產品、服務或交易、交付渠道及其他風險因素，涵蓋四個範疇。下一節逐項列出"),
                'plain', "¶2.2 · ¶2.4", href="#factors")
    A = Card(L, LW, ("Document the risk assessment process", "記錄風險評估程序"),
             ("Identify and assess the relevant risks, supported by qualitative and quantitative analysis and information from relevant internal and external sources",
              "識別和評估有關風險，並輔以從相關內部與外部來源取得的定質與定量分析及資料"), 'must', "¶2.3(a)")
    Bq = Card(L, LW, ("Weigh every relevant factor, then decide", "考慮所有相關風險因素，然後決定"),
              ("The level of overall risk, and the appropriate level and type of mitigation to apply",
               "整體風險水平，以及擬採用何種程度和類別合適的減低風險措施"), 'must', "¶2.3(b)")
    C = Card(L, LW, ("Senior management approves the results", "由高級管理層審批風險評估結果"), None, 'must', "¶2.3(c)")
    R = Card(L, LW, ("Keep the records", "備存紀錄"),
             ("The risk factors identified and assessed; the information sources taken into account; your evaluation of whether your AML/CFT Systems are adequate and appropriate",
              "所識別及評估的風險因素；所考慮的資料來源；就你的打擊洗錢／恐怖分子資金籌集制度是否充分和適當而作出的評估"), 'must', "¶2.10")
    E = Card(R_, RW, ("Provide it to the CCE when required", "應關長要求提供"),
             ("Have appropriate mechanisms to do so", "設有適當機制"), 'must', "¶2.3(e)")
    T2 = Card(L, 180, ("Every two years", "每兩年一次"), ("The regular cycle", "定期進行"), 'plain', "¶2.9")
    TE = Card(L + 200, LW - 200, ("A trigger event", "觸發事件"),
              ("One material to your business and risk exposure. The Guideline's examples are under Keeping it current",
               "顯著影響你的業務及所面對風險的事件。指引所舉的例子見「保持評估反映現況」"),
              'plain', "¶2.9", href="#review")
    NEW = Card(R_, RW, ("Something new? Assess it before launch", "推出新事物？先行評估"),
               ("New products, business practices and technologies: assess the risks, then manage and mitigate them. A launch of new products is also a trigger event",
                "新產品、新經營方法及嶄新科技：先評估風險，再管理和減低風險。推出新產品亦屬觸發事件"),
               'must', "¶2.9 · ¶2.11–2.12", href="#review")
    V = Card(L, LW, ("Review and update the assessment", "覆核及更新評估"),
             ("Document the results, and have senior management approve them. The cycle then starts again from the top",
              "覆核結果須記錄在案，並由高級管理層審批。其後由頂部再次開始"), 'must', "¶2.3(d) · ¶2.9")
    H = place([([IN, FACT], 34), ([A], 34), ([Bq], 34), ([C], 34), ([R, E], 44), ([T2, TE, NEW], 40), ([V], 0)], y0=14)
    b = [n.render() for n in (IN, FACT, A, Bq, C, R, E, T2, TE, NEW, V)]
    m = 'g2i'
    for a, c in ((IN, A), (A, Bq), (Bq, C), (C, R)):
        b.append(edge([a.bottom, c.top], mid=m))
    # the factors feed the weighing step from the right
    fx = FACT.cx
    b.append(edge([FACT.bottom, (fx, Bq.cy), Bq.right], mid=m))
    # records sit beside the duty to hand the assessment over
    b.append(dash([R.right, E.left]))
    # the two routes into a review
    jy = R.bottom[1] + 20
    b.append(edge([R.bottom, (R.cx, jy)], marker=False))
    b.append(edge([(T2.cx, jy), (TE.cx, jy)], marker=False))
    b.append(edge([(T2.cx, jy), T2.top], mid=m))
    b.append(edge([(TE.cx, jy), TE.top], mid=m))
    b.append(edge([T2.bottom, (T2.cx, V.y)], mid=m))
    b.append(edge([TE.bottom, (TE.cx, V.y)], mid=m))
    b.append(edge([NEW.left, TE.right], mid=m))
    # the loop back to the top
    rx = 24
    b.append(edge([V.left, (rx, V.cy), (rx, A.cy), A.left], mid=m))
    aria = ("The institutional ML/TF risk assessment as a cycle. It draws on quantitative and qualitative information from relevant internal and external sources, which may include risk assessments and guidance by the FATF, inter-governmental organisations, governments and authorities, Hong Kong's jurisdiction-wide risk assessment and higher risks the CCE notifies. Document the risk assessment process of identifying and assessing the risks. Weigh every relevant factor, then decide the overall risk level and the level and type of mitigation. Senior management approves the results. Keep records of the factors, the sources and the evaluation of your AML/CFT Systems; alongside, have mechanisms to provide the assessment to the CCE when required. Every two years, and on trigger events material to your business and risk exposure, review and update the assessment, document the results and have senior management approve them; then the cycle starts again. New products, business practices and technologies are assessed before launch, and a launch of new products is also a trigger event.",
            "機構層面的洗錢／恐怖分子資金籌集風險評估是一個循環。評估參考相關內部與外部來源的數量及質量分析資料，可包括特別組織、跨政府組織、各地政府及主管當局的風險評估及導引、香港在司法管轄區層面的風險評估，以及關長通報的較高風險。記錄識別和評估風險的程序。考慮所有相關風險因素，然後決定整體風險水平及減低風險措施的程度和類別。由高級管理層審批結果。備存風險因素、資料來源及對制度評估的紀錄；同時設有機制應關長要求提供評估結果。每兩年一次，以及遇有顯著影響業務及所面對風險的觸發事件時，覆核及更新評估，記錄結果並由高級管理層審批，然後再次開始。新產品、新經營方法及嶄新科技須在推出前評估，推出新產品亦屬觸發事件。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


IRA_KEY = dashkey([('must', ("what the Guideline requires of you", "指引對你的要求")),
                   ('', ("context: what you draw on, the factors you weigh, and what sets off a review", "背景：資料來源、須考慮的因素，以及引致覆核的事件"))],
                  "applies alongside, not a next step", "並行適用，並非下一步")


# ---------------------------------------------------------------- 2. the three look-alike lists
def fig_lists():
    W = 1000
    X = (10, 340, 640)
    CWS = (310, 280, 350)   # the third column is widest so its long title fits on two lines
    heads = [
        (["Institutional assessment:", "the 4 areas it covers"], ["機構層面的評估：", "涵蓋的4個範疇"], "¶2.2"),
        (["Institutional assessment:", "the 5 groups of factors"], ["機構層面的評估：", "考慮的5組因素"], "¶2.4"),
        (["Customer risk framework:", "the 3 groups of factors"], ["客戶風險評估框架：", "包含的3組因素"], "¶2.15"),
    ]
    v = lay()
    nl = max(len(en) if v == 'en' else len(tc) if v == 'tc' else len(en) + len(tc) for en, tc, _ in heads)
    b = []
    hsz = 12.5
    for x, CW, (en, tc, c) in zip(X, CWS, heads):
        b.append(lines_down(x + CW / 2, 6, en, tc, 't t-b', hsz))
        cy_ = 6 + nl * hsz * FS * 1.3 + 2 + 10.5 * FS
        for vv, t in (('en', c), ('tc', cite_txt(c, 'tc')), ('both', c)):
            b.append(f'<text class="c s-{vv}" font-size="{10.5 * FS}" text-anchor="middle"><tspan x="{x + CW / 2:.1f}" y="{cy_:.1f}">{esc(t)}</tspan></text>')
    y0 = 6 + nl * hsz * FS * 1.3 + 10.5 * FS * 1.3 + 18
    a = [Card(X[0], CWS[0], ("Your customers", "你的客戶"), None, 'plain', "¶2.2(a)"),
         Card(X[0], CWS[0], ("The countries or jurisdictions your customers are from or in", "客戶所屬或所在的國家或司法管轄區"), None, 'plain', "¶2.2(b)"),
         Card(X[0], CWS[0], ("The countries or jurisdictions where you have operations", "你業務所在的國家或司法管轄區"), None, 'plain', "¶2.2(c)"),
         Card(X[0], CWS[0], ("Your products, services, transactions and delivery channels", "你的產品、服務、交易及交付渠道"), None, 'plain', "¶2.2(d)")]
    f = [Card(X[1], CWS[1], ("Customer risk factors", "客戶風險因素"), None, 'plain', "¶2.4(a)"),
         Card(X[1], CWS[1], ("Country risk factors", "國家風險因素"), None, 'plain', "¶2.4(b)"),
         Card(X[1], CWS[1], ("Product, service or transaction risk factors", "產品、服務或交易風險因素"), None, 'plain', "¶2.4(c)"),
         Card(X[1], CWS[1], ("Delivery or distribution channel risk factors", "交付或分銷渠道風險因素"), None, 'plain', "¶2.4(d)"),
         Card(X[1], CWS[1], ("Other risk factors", "其他風險因素"),
              ("Risk-management resources and staff, compliance and regulatory findings, audit results", "風險管理資源及員工、合規及監管的發現、審計結果"), 'plain', "¶2.4(e)")]
    c3 = [Card(X[2], CWS[2], ("Customer risk factors", "客戶風險因素"), None, 'plain', "¶2.15"),
          Card(X[2], CWS[2], ("Country risk factors", "國家風險因素"), None, 'plain', "¶2.15"),
          Card(X[2], CWS[2], ("Product, service, transaction or delivery channel risk factors", "產品、服務、交易或交付渠道的風險因素"), None, 'plain', "¶2.15"),
          Card(X[2], CWS[2], ("No counterpart", "沒有對應組別"), ("The framework's list stops at three groups", "框架只列出三組"), 'faint')]
    hh = max(n.h for n in a + f[:4] + c3[:3])
    for n in a + f[:4] + c3[:3]:
        n.h = hh
    st = hh + 16
    for i, n in enumerate(a):
        n.y = y0 + i * st
    for n, k in zip(f, (0, 1.5, 3, 4, 5)):
        n.y = y0 + k * st
    for n, k in zip(c3, (0, 1.5, 3.5, 5)):
        n.y = y0 + k * st
    c3[3].y = f[4].cy - c3[3].h / 2
    b += [n.render() for n in a + f + c3]
    pairs = [(a[0], f[0]), (a[1], f[1]), (a[2], f[1]), (a[3], f[2]), (a[3], f[3]),
             (f[0], c3[0]), (f[1], c3[1]), (f[2], c3[2]), (f[3], c3[2])]
    for p, q in pairs:
        b.append(f'<line class="e" x1="{p.x + p.w}" y1="{p.cy:.1f}" x2="{q.x}" y2="{q.cy:.1f}"/>')
    H = max(n.y + n.h for n in f + c3) + 14
    aria = ("Three lists from Chapter 2 side by side. The institutional assessment covers four areas: your customers; the countries your customers are from or in; the countries where you operate; and your products, services, transactions and delivery channels. It weighs five groups of factors: customer, country, product service or transaction, delivery or distribution channel, and other. The customer risk assessment framework generally has three groups: customer, country, and product, service, transaction or delivery channel. Lines pair the items that deal with the same thing; the other risk factors have no counterpart in the customer framework.",
            "第2章三份清單並列。機構層面的洗錢／恐怖分子資金籌集風險評估涵蓋四個範疇：你的客戶；客戶所屬或所在的國家；你業務所在的國家；以及你的產品、服務、交易及交付渠道。它考慮五組因素：客戶、國家、產品服務或交易、交付或分銷渠道，以及其他。客戶風險評估框架一般包含三組：客戶、國家，以及產品、服務、交易或交付渠道。連線把處理同一事項的項目配對；其他風險因素在客戶框架中沒有對應組別。")
    return svg(W, H, ''.join(b), aria, 'g2l', 860)


LISTS_KEY = legend([('', ("an item on the Guideline's list", "指引清單上的項目")), ('faint', ("no counterpart on that list", "該清單上沒有對應項目"))])


# ---------------------------------------------------------------- 3. the life of a customer rating
def mlabel16(x, y, en, tc, anchor='middle'):
    """ui.mlabel with a 16-unit line pitch, so the stacked English descenders clear the Chinese line."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        n = len(ls)
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (n - 1 - i) * 16:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def fig_cra():
    W = 1000
    L, LW = 50, 510
    R_, RW = 630, 340
    S = Card(270, 460, ("A customer, or a proposed business relationship", "客戶或擬開展的業務關係"), None, 'plain')
    P1 = Card(245, 510, ("Assess the risk at the initial stage of CDD", "在盡職審查程序初期評估風險"),
              ("Against your framework: customer, country, and product, service, transaction or delivery channel risk factors",
               "按你的框架：客戶、國家，以及產品、服務、交易或交付渠道的風險因素"), 'must', "¶2.13 · ¶2.15")
    Q = Node(340, 320, ("Is the risk higher or lower?", "風險較高還是較低？"), "¶2.13", shape='hex')
    HI = Card(L, 280, ("Do more", "加強"), ("More information, of more types, verified more thoroughly", "索取數量及類別更多的資料，並以更嚴謹方式核實"),
              'must', "¶2.13", answer=True)
    MID = Card(360, 280, ("All the CDD measures, and ongoing monitoring", "執行所有盡職審查措施並持續監察"),
               ("The measures in ¶4.1.3 always apply, except in situations Chapter 4 specifies",
                "除第4章指明的若干情況外，第4.1.3段所列的盡職審查措施一律適用"), 'must', "fn 5", href="#s2-map", answer=True)
    LO = Card(670, 300, ("CDD may be simplified", "可簡化審查程序"),
              ("Outside the situations Chapter 4 specifies, all the CDD measures still apply. See the Schedule 2 page",
               "除第4章指明的情況外，仍須執行所有盡職審查措施。詳見附表2一頁"),
              'ok', "¶2.13 · fn 5", href="#s2-sdd-edd", answer=True)
    F = Card(L, LW, ("Finalise the customer risk assessment", "敲定客戶風險評估"),
             ("From a holistic view of the information obtained in CDD", "綜合審視執行盡職審查措施期間所索取的資料"), 'must', "¶2.14")
    REC = Card(R_, RW, ("Keep records of the assessment", "就客戶風險評估備存紀錄"),
               ("So that you can show the CCE how you assess the customer's risk, and that the extent of CDD and ongoing monitoring is appropriate to it",
                "以便向關長證明你如何評估客戶的風險，以及基於該風險，所執行的盡職審查措施及持續監察程度是合適的"), 'must', "¶2.16", href="#s2-records")
    MON = Card(L, 420, ("It sets the level and type of ongoing monitoring", "決定持續監察的程度和類別"),
               ("Ongoing CDD and transaction monitoring", "持續的盡職審查及交易監察"), 'must', "¶2.14", href="#s2-monitoring", answer=True)
    DEC = Card(L + 450, 400, ("It supports your decision to enter into, continue or terminate the relationship", "支持你建立、繼續或終止業務關係的決定"),
               None, 'plain', "¶2.14", answer=True)
    RV = Card(L, 420, ("Review and update it from time to time", "不時覆核和更新"),
              ("Particularly during ongoing monitoring, because the customer's risk profile changes over time",
               "尤以持續監察時為然，因為客戶風險狀況會隨時間轉變"), 'must', "¶2.14")
    H = place([([S], 34), ([P1], 34), ([Q], 70), ([HI, MID, LO], 70), ([F, REC], 50), ([MON, DEC], 34), ([RV], 0)], y0=14)
    b = [n.render() for n in (S, P1, Q, HI, MID, LO, F, REC, MON, DEC, RV)]
    m = 'g2c'
    b.append(edge([S.bottom, P1.top], mid=m))
    b.append(edge([P1.bottom, Q.top], mid=m))
    # three answers; each label sits beside its own drop, clear of the bus line
    jy = Q.bottom[1] + 18
    b.append(edge([Q.bottom, (Q.cx, jy)], marker=False))
    b.append(edge([(HI.cx, jy), (LO.cx, jy)], marker=False))
    for n in (HI, MID, LO):
        b.append(edge([(n.cx, jy), n.top], mid=m))
    b.append(mlabel16(HI.cx - 8, jy + 34, "higher", "較高", 'end'))
    b.append(mlabel16(MID.cx + 8, jy + 34, "neither", "兩者皆非", 'start'))
    b.append(mlabel16(LO.cx + 8, jy + 34, "lower", "較低", 'start'))
    # all three lead on to the finalised assessment
    ky = max(n.y + n.h for n in (HI, MID, LO)) + 20
    for n in (HI, MID, LO):
        b.append(edge([n.bottom, (n.cx, ky)], marker=False))
    b.append(edge([(HI.cx, ky), (LO.cx, ky)], marker=False))
    b.append(edge([(F.cx, ky), F.top], mid=m))
    b.append(dash([F.right, REC.left]))
    ly = max(F.bottom[1], REC.bottom[1]) + 22
    b.append(edge([F.bottom, (F.cx, ly)], marker=False))
    b.append(edge([(MON.cx, ly), (DEC.cx, ly)], marker=False))
    b.append(edge([(MON.cx, ly), MON.top], mid=m))
    b.append(edge([(DEC.cx, ly), DEC.top], mid=m))
    b.append(edge([MON.bottom, RV.top], mid=m))
    rx = 24
    b.append(edge([RV.left, (rx, RV.cy), (rx, F.cy), F.left], mid=m))
    aria = ("The life of one customer risk rating. For a customer or proposed business relationship, assess the risk at the initial stage of CDD against the framework's customer, country and product, service, transaction or delivery channel factors. If the risk is higher, obtain more information of more types and verify it more thoroughly. If it is neither higher nor lower, apply all the CDD measures in paragraph 4.1.3 and conduct ongoing monitoring, which always apply except in situations Chapter 4 specifies. If it is lower, CDD may be simplified, but outside the situations Chapter 4 specifies all the CDD measures still apply. Then finalise the customer risk assessment from a holistic view of the CDD information; alongside, keep records that show the CCE how you assessed the risk and that CDD and monitoring fit it. The finalised assessment sets the level and type of ongoing monitoring and supports the decision to enter into, continue or terminate the relationship. Review and update it from time to time, particularly during ongoing monitoring, which loops back to the finalised assessment.",
            "一項客戶風險評估的生命周期。對客戶或擬開展的業務關係，在盡職審查程序初期按框架的客戶、國家，以及產品、服務、交易或交付渠道因素評估風險。風險較高，便索取數量及類別更多的資料並以更嚴謹方式核實。風險既非較高亦非較低，便執行第4.1.3段所列的所有盡職審查措施並持續監察；除第4章指明的若干情況外，這些措施一律適用。風險較低，可簡化審查程序，但除第4章指明的情況外，仍須執行所有盡職審查措施。其後綜合審視盡職審查資料，敲定客戶風險評估；同時備存紀錄，以便向關長證明如何評估風險，以及基於該風險，所執行的盡職審查措施及持續監察程度是合適的。敲定的評估決定持續監察的程度和類別，並支持建立、繼續或終止業務關係的決定。其後不時覆核和更新，尤以持續監察時為然，並回到敲定評估的步驟。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


CRA_KEY = dashkey([('must', ("what the Guideline requires of you", "指引對你的要求")), ('ok', ("you may simplify", "可以簡化")),
                   ('', ("where it starts, and a decision it supports", "起點，以及評估所支持的決定")),
                   ('hex', ("the question", "問題"))],
                  "applies alongside, not a next step", "並行適用，並非下一步")
