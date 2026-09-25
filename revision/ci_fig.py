# Figures for the Circulars page: the third-party payment decision, the
# trade-based laundering chain, and the half-yearly periodic return calendar.
from ui import *
from bl_core import _runs
from bl_figs import lines_down
from gl_fig import tick_text, dash  # noqa: F401 (kept for importers)

# Only the circulars that are still current sources. Circulars whose content a later official
# document now covers (the Guideline of June 2023, the CA Guidance Notes, the Licensing Guide of
# May 2026, the consolidated AMLO) are no longer sources and are not listed here.
DATES = {"31 Jul 2018": "2018年7月31日", "13 Dec 2021": "2021年12月13日",
         "22 Nov 2023": "2023年11月22日", "17 Sep 2024": "2024年9月17日", "30 May 2025": "2025年5月30日",
         "17 Nov 2025": "2025年11月17日", "20 Jan 2026": "2026年1月20日",
         "24 Apr 2025": "2025年4月24日", "23 Jun 2025": "2025年6月23日",
         "3 Jul 2026": "2026年7月3日", "16 Jul 2026": "2026年7月16日"}


def CI(d, extra=None):
    en, tc = f"Circular {d}", f"{DATES[d]}通函"
    if extra:
        en, tc = en + ", " + extra[0], tc + "，" + extra[1]
    return (en, tc)


def TP(i):
    return CI("17 Sep 2024", (f"standard {i}", f"標準第{_runs(i)}項"))


def TPF(n):
    return CI("17 Sep 2024", (f"note {n}", f"註{n}"))


def TB(i):
    return CI("20 Jan 2026", (f"area {i}", f"範疇{_runs(i)}"))


def slabel(x, y, en, tc, anchor='middle'):
    """Edge label; the combined view stacks English over Chinese 16.5 apart (the .lbl font is 13.5),
    keeping the lower line at y so it stays clear of the connector."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        n = len(ls)
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (n - 1 - i) * 16.5:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


# ---------------------------------------------------------------- third-party payments
def fig_tpp():
    W = 1000
    A = Card(40, 520, ("A payment arrives from someone other than your customer", "有款項來自客戶以外的人"),
             ("For the circular, a third party means anyone other than the customer", "就該通函而言，「第三方」指客戶以外的任何人"), cite=TPF("3"))
    Q1 = Node(40, 520, ("Can your controls handle this inherently high risk and meet the requirements?", "你的管控措施能否應付這類本身屬高風險的付款，並符合規定？"), TP("3"), shape='hex')
    X1 = Card(630, 340, ("Accept no third-party payment at all", "完全不接受第三方支付"), None, 'stop', TP("3"), answer=True)
    Q2 = Node(40, 520, ("Exceptional and legitimate, and reasonably in line with the customer's profile and normal commercial practice?",
                        "屬特殊及合法情況，並合理地符合客戶狀況及一般商業作業手法？"), TP("4"), shape='hex')
    X2 = Card(630, 340, ("Do not accept it", "不予接納"), ("Where the circumstances give grounds for suspicion, report to the JFIU", "如情況引起懷疑，向財富情報組報告"), 'stop', TP("4, 9"), answer=True)
    DD = Card(40, 520, ("Due diligence before you accept", "接納前的盡職審查"),
              ("Evaluate why the payment is needed; on a risk-sensitive basis, verify the third party's identity and its relationship with the customer; get approval from senior management with an AML/CFT role; record the enquiries, evidence and approval",
               "嚴格評估使用第三方支付的原因及需要；因應風險核實第三方的身分及其與客戶的關係；取得擔任打擊洗錢相關職位的高級管理層批准；記錄查詢結果、核對證據及批准"), 'must', TP("6"))
    Q3 = Node(40, 520, ("Is this third party higher risk? (Immediate family, the customer's beneficial owners or affiliated companies, and regulated financial institutions are generally lower risk)",
                        "該第三方是否屬較高風險？（直系親屬、客戶的實益擁有人或聯繫公司，以及受規管金融機構一般屬較低風險）"),
              CI("17 Sep 2024", ("standard 7, note 6", "標準第7項、註6")), shape='hex')
    E = Card(630, 340, ("Enhanced scrutiny", "更嚴格審查"),
             ("Establish the source of funds of the customer or beneficial owner. Take extra care if the relationship is hard to verify, the payer cannot be identified before payment, or one payer serves several unrelated customers",
              "確立相關客戶或實益擁有人的資金來源。如雙方關係難以核實、付款前未能提供付款人身分資料，或同一付款人為多名看似無關連的客戶付款或收款，須格外留神"), 'must', TP("7–8"))
    OK = Card(40, 520, ("Accept it, then watch more closely", "接納，然後加強監察"),
              ("Enhanced ongoing monitoring, with third-party red flags defined in your monitoring system; stay alert to the payer being the true beneficial owner; report to the JFIU on grounds for suspicion",
               "加強持續監察，並在交易監察系統中為第三方支付設定可疑交易訊號；留意付款人可能才是真正的實益擁有人；如有懷疑理由，向財富情報組報告"), 'ok', TP("9"), answer=True)
    H = place([([A], 32), ([Q1, X1], 40), ([Q2, X2], 40), ([DD], 32), ([Q3, E], 40), ([OK], 0)], y0=14)
    b = [n.render() for n in (A, Q1, X1, Q2, X2, DD, Q3, E, OK)]
    m = 'cit'
    b.append(edge([A.bottom, Q1.top], mid=m))
    for q, x in ((Q1, X1), (Q2, X2)):
        b.append(edge([q.right, x.left], mid=m))
        b.append(slabel((q.x + q.w + x.x) / 2, q.cy - 8, "no", "否"))
    b.append(edge([Q1.bottom, Q2.top], ("yes", "是"), Q1.cx + 10, (Q1.bottom[1] + Q2.top[1]) / 2 + 4, 'start', mid=m))
    b.append(edge([Q2.bottom, DD.top], ("yes", "是"), Q2.cx + 10, (Q2.bottom[1] + DD.top[1]) / 2 + 4, 'start', mid=m))
    b.append(edge([DD.bottom, Q3.top], mid=m))
    b.append(edge([Q3.right, E.left], mid=m))
    b.append(slabel((Q3.x + Q3.w + E.x) / 2, Q3.cy - 8, "yes", "是"))
    b.append(edge([Q3.bottom, OK.top], ("no", "否"), Q3.cx + 10, (Q3.bottom[1] + OK.top[1]) / 2 + 4, 'start', mid=m))
    b.append(edge([E.bottom, (E.cx, OK.cy), OK.right], mid=m))
    aria = ("Deciding on a third-party payment. A payment comes from someone other than the customer. If your controls cannot handle the risk, accept no third-party payment at all. If they can, accept it only in exceptional and legitimate circumstances in line with the customer's profile; otherwise refuse, and report if suspicious. Before accepting, evaluate the need, verify the payer and the relationship on a risk-sensitive basis, get senior management approval and record it all. A higher-risk payer gets enhanced scrutiny, including the source of funds; immediate family, the customer's beneficial owners or affiliated companies, and regulated financial institutions are generally lower risk. Accepted payments get enhanced ongoing monitoring and a report to the JFIU if suspicion arises.",
            "處理第三方支付。有款項來自客戶以外的人。如你的管控措施無法應付風險，則完全不接受第三方支付。如能應付，只在符合客戶狀況的特殊及合法情況下接納；否則不予接納，如有懷疑須舉報。接納前須評估需要、因應風險核實付款人身分及雙方關係、取得高級管理層批准並妥為記錄。較高風險的付款人須接受更嚴格審查，包括確立資金來源；直系親屬、客戶的實益擁有人或聯繫公司，以及受規管金融機構一般屬較低風險。接納的付款須加強持續監察，如有懷疑須向財富情報組報告。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


def cc_(*cs):
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


TPP_KEY = legend([('hex', ("a question you answer", "你須回答的問題")), ('', ("where it starts", "起點")),
                  ('must', ("a step expected of you", "你應採取的步驟")), ('ok', ("accepted", "接納")), ('stop', ("not accepted", "不予接納"))])


# ---------------------------------------------------------------- trade-based laundering
def fig_tbml():
    W = 1000
    xs, cw = [10, 261, 512, 763], 226
    top = [
        Card(xs[0], cw, ("A fake contract or invoice", "偽造的合同或發票"), ("Falsified trade documents", "偽造的貿易文件")),
        Card(xs[1], cw, ("A bogus trade record", "虛假的交易紀錄"), ("Illicit money dressed up as legitimate trade income", "把非法資金偽裝成合法貿易收入")),
        Card(xs[2], cw, ("A shell company", "空殼公司"), ("May be used with the fabricated documents to hide the beneficial owner or the source of illicit funds", "可能會與偽造文件一併使用，掩飾實益擁有人身份或非法資金來源")),
        Card(xs[3], cw, ("Your cross-boundary remittance", "你的跨境匯款"), ("Could be exploited as one of the conduits for moving the proceeds", "可能被利用作為轉移貿易犯罪得益的一種渠道")),
    ]
    th_ = max(n.h for n in top)
    for n in top:
        n.h, n.y = th_, 14
    by = 14 + th_ + 20                      # the brace under the whole chain
    hd = Card(10, 979, ("Your controls: the four areas the circular asks you to enhance", "你的管控措施：通函要求你優化的四個範疇"),
              None, 'must', TB("1–4"))
    hd.y = by + (70 if lay() == 'both' else 58)   # two label lines in the combined view need the room
    g1 = hd.y + hd.h + 12
    ctl = [
        Card(10, 485, ("1 · Understanding ML/TF risks", "1 · 了解洗錢及恐怖分子資金籌集的風險"),
             ("A customer risk assessment framework that picks out higher-risk customers and weighs material changes in their profile; flag and escalate to senior management when several risk indicators appear; training and guidance so both the first and second lines of defence are risk-aware",
              "客戶風險評估框架能識別較高風險的客戶，並評估客戶狀況重大轉變的合理性；客戶出現多項風險指標時，作出標記並上報高級管理層；輔以員工培訓及指導，使第一及第二道防線均具備風險意識"), 'must', TB("1")),
        Card(504, 485, ("2 · Customer due diligence", "2 · 客戶盡職審查"),
             ("EDD for high-risk customers; consider asking for source of funds and wealth; much higher risk from a new entity without significant assets, staff or operations; proactively consider anti-fraud checks on information customers provide, to verify the transaction is genuine and assess how likely the originator or recipient is a shell company; review documents periodically",
              "對高風險客戶施加更嚴格的盡職審查要求，並考慮索取資金及財富來源資料；新成立而缺乏顯著資產、員工或活躍業務的法律實體風險較高；主動考慮以反欺詐程序審查客戶提供的資料，以核實交易真實性及評估匯款人或收款人為空殼公司的可能性；定期審查文件"), 'must', TB("2")),
        Card(10, 485, ("3 · Transaction monitoring", "3 · 監察交易"),
             ("Alerts for unusual or suspicious transactions; examine background and purpose, ask the customer or get more CDD information; never close an alert without sufficient justification and analysis; weigh the risk profile, source of funds or wealth, and past transactions",
              "系統能就不尋常或可疑交易發出警報；審查交易背景及目的，向客戶查詢或索取額外盡職審查資料；不可在沒有充分理由及分析下消除警報；考慮風險狀況、資金或財富來源及交易歷史"), 'must', TB("3")),
        Card(504, 485, ("4 · Filing STRs", "4 · 提交可疑交易報告"),
             ("Report when you suspect proceeds of crime or terrorist property, with what the suspicion rests on; weigh everything you hold on both the originator and the recipient; whatever the amount, and attempted transactions too",
              "懷疑交易與犯罪得益或恐怖分子財產有關，便須提交報告，連同懷疑所根據的事宜；考慮所掌握的匯款人及收款人的所有資料；不論所涉金額，亦涵蓋試圖進行的交易"), 'must', TB("4")),
    ]
    r1 = max(ctl[0].h, ctl[1].h)
    r2 = max(ctl[2].h, ctl[3].h)
    for n in ctl[:2]:
        n.h, n.y = r1, g1
    for n in ctl[2:]:
        n.h, n.y = r2, g1 + r1 + 12
    b = [n.render() for n in top + [hd] + ctl]
    m = 'cib'
    # the shell company is used together with the fake documents, not after them: a '+' joins the two
    b.append(edge([top[0].right, top[1].left], mid=m))
    b.append(text_variants((top[1].x + top[1].w + top[2].x) / 2, top[1].cy, {'en': ['+'], 'tc': ['+'], 'both': ['+']}, 22 * FS, 't t-b'))
    b.append(edge([top[2].right, top[3].left], mid=m))
    b.append(f'<polyline class="e" points="{xs[0]},{by - 10} {xs[0]},{by} {xs[3] + cw},{by} {xs[3] + cw},{by - 10}"/>')
    b.append(edge([hd.top, (hd.cx, by + 2)], mid=m))
    b.append(slabel(hd.cx + 12, (by + hd.y) / 2 + (14 if lay() == 'both' else 5), "aimed at the whole chain", "針對整條鏈條", 'start'))
    aria = ("How trade-based laundering uses a remittance counter, and the controls the circular asks for. A fake contract or invoice creates a bogus trade record that dresses illicit money as legitimate trade income; a shell company may be used together with the fabricated documents to obscure the beneficial owner or the source of funds; your cross-boundary remittance could be exploited as one of the conduits for moving the proceeds. Beneath the chain are the circular's four areas for enhancement: understanding ML/TF risks, with escalation to senior management; customer due diligence, with EDD, source of funds and wealth, and anti-fraud checks to consider; transaction monitoring that never closes an alert without analysis; and filing STRs whatever the amount, attempted transactions included.",
            "貿易洗錢如何利用匯款櫃位，以及通函要求的管控措施。偽造的合同或發票製造虛假交易紀錄，把非法資金偽裝成合法貿易收入；空殼公司可能會與偽造文件一併使用，以掩飾實益擁有人的身份或資金來源；你的跨境匯款可能被利用作為轉移得益的其中一種渠道。鏈條下方是通函的四個優化範疇：了解洗錢及恐怖分子資金籌集的風險並上報高級管理層；客戶盡職審查，包括更嚴格的盡職審查、資金及財富來源，以及考慮採取反欺詐程序；不會在沒有分析下消除警報的交易監察；以及不論金額、涵蓋試圖進行的交易的可疑交易報告。")
    return svg(W, g1 + r1 + 12 + r2 + 14, ''.join(b), aria, m, 860)


TBML_KEY = legend([('', ("part of the scheme; + means used together", "洗錢手法的一環；「+」表示一併使用")), ('must', ("an area you are expected to enhance", "你須優化的範疇"))])


# ---------------------------------------------------------------- periodic returns
def vtext(x, y, en, tc, size, cls='t', anchor='middle'):
    """Text lines per view, top line's baseline at y; 'both' stacks English over Chinese."""
    size = size * FS
    out = []
    for v, ls in (('en', en), ('tc', tc), ('both', en + tc)):
        g = [f'<text class="{cls} s-{v}" font-size="{size}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x:.1f}" y="{y + i * size * 1.25:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def nl(en, tc):
    return {'en': len(en), 'tc': len(tc), 'both': len(en) + len(tc)}[lay()]


MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb"]


def fig_pr():
    W = 1000
    X0, MW = 160, 58
    xm = [X0 + i * MW for i in range(15)]
    two = lay() == 'both'
    ms = 11 * FS
    b = []
    # months, labelled in the middle of each month; the last two belong to the next year
    ay = 14 + (2 if two else 1) * ms * 1.25 + 4
    b.append(f'<line class="e" x1="{X0}" y1="{ay}" x2="{xm[14]}" y2="{ay}"/>')
    for i in range(15):
        b.append(f'<line class="e" x1="{xm[i]}" y1="{ay - 5}" x2="{xm[i]}" y2="{ay + 5}"/>')
    for i, en in enumerate(MON):
        tc = f"{(i % 12) + 1}月"
        b.append(vtext(xm[i] + MW / 2, ay - 8 - (ms * 1.25 if two else 0), [en], [tc], 11))
    if two:
        b.append(vtext((xm[12] + xm[14]) / 2, ay + 19, ["next year / 翌年"], [], 10.5))
    else:
        b.append(vtext((xm[12] + xm[14]) / 2, ay + 19, ["next year"], ["翌年"], 10.5))
    # since 30 June 2025: two returns, by the calendar
    y1 = ay + 30
    BH = 66 if two else 46
    for x0, x1_, en, tc in ((xm[0], xm[6], "Return 1: 1 January to 30 June", "第一份申報表：1月1日至6月30日"),
                            (xm[6], xm[12], "Return 2: 1 July to 31 December", "第二份申報表：7月1日至12月31日")):
        b.append(f'<rect class="bar-soft" x="{x0}" y="{y1}" width="{x1_ - x0}" height="{BH}" rx="3" style="stroke:var(--faint)"/>')
        b.append(text_variants((x0 + x1_) / 2, y1 + BH / 2, {'en': [en], 'tc': [tc], 'both': [en, tc]}, 12 * FS, 't t-b'))
    hen, htc = ["From", "30 Jun 2025"], ["2025年6月30日起"]
    b.append(vtext(10, y1 + BH / 2 - nl(hen, htc) * 11.5 * FS * 1.25 / 2 + 11.5 * FS * 0.85, hen, htc, 11.5, 't t-b', 'start'))
    # lodging windows: two weeks from the start of the next half
    yl = y1 + BH + 34
    wk = MW * 14 / 31
    labs = ((xm[3], xm[6], ["Return 1 lodged within", "2 weeks from 1 July"], ["第一份於7月1日起", "兩星期內遞交"]),
            (xm[9], xm[12], ["Return 2 lodged within", "2 weeks from 1 January"], ["第二份於翌年1月1日起", "兩星期內遞交"]))
    for xc, x0, en, tc in labs:
        b.append(f'<rect class="bar" x="{x0:.1f}" y="{yl}" width="{wk:.1f}" height="22" rx="3"/>')
        b.append(edge([(xc, y1 + BH), (xc, yl + 11), (x0, yl + 11)], mid='cip'))
        b.append(vtext(x0 + wk / 2, yl + 22 + ms + 2, en, tc, 11))
    lab_h = nl(labs[0][2], labs[0][3]) * ms * 1.25
    # until 30 June 2025: quarters from the licence date (example: a licence that began on 1 March)
    yo = yl + 22 + lab_h + 30
    QH = 48 if two else 28
    quarters = [(xm[0], xm[2], "… quarter 4", "…第4季"), (xm[2], xm[5], "quarter 1", "第1季"), (xm[5], xm[8], "quarter 2", "第2季"),
                (xm[8], xm[11], "quarter 3", "第3季"), (xm[11], xm[14], "quarter 4", "第4季")]
    for x0, x1_, en, tc in quarters:
        b.append(f'<rect class="n n-faint" x="{x0 + 2}" y="{yo}" width="{x1_ - x0 - 4}" height="{QH}" rx="3" style="stroke:var(--faint)"/>')
        b.append(vtext((x0 + x1_) / 2, yo + (QH - (2 if two else 1) * ms * 1.25) / 2 + ms * 0.85, [en], [tc], 11, 't t-faint'))
    hen, htc = ["Until", "30 Jun 2025"], ["2025年6月30日前"]
    b.append(vtext(10, yo + QH / 2 - nl(hen, htc) * 11.5 * FS * 1.25 / 2 + 11.5 * FS * 0.85, hen, htc, 11.5, 't t-b', 'start'))
    nen = ["Four returns a year, each quarter counted from the licence's start date",
           "(here, a licence that began on 1 March; its quarter 4 runs from December to February)"]
    ntc = ["每年四份，每季由牌照生效日期起計", "（此例牌照於3月1日生效，其第4季由12月至翌年2月）"]
    b.append(vtext((xm[0] + xm[14]) / 2, yo + QH + 8 + ms, nen, ntc, 11, 't t-faint'))
    H = yo + QH + 8 + nl(nen, ntc) * ms * 1.25 + 14
    aria = ("The periodic return calendar since 30 June 2025. Return 1 covers 1 January to 30 June and is lodged within two weeks from 1 July; return 2 covers 1 July to 31 December and is lodged within two weeks from 1 January of the next year. Until 30 June 2025, returns were quarterly, four a year, each quarter counted from the licence's own start date: for a licence that began on 1 March, the quarters ran March to May, June to August, September to November and December to February.",
            "2025年6月30日起的定期申報表時間表。第一份涵蓋1月1日至6月30日，於7月1日起兩星期內遞交；第二份涵蓋7月1日至12月31日，於翌年1月1日起兩星期內遞交。2025年6月30日前，申報表每季遞交，每年四份，每季由牌照本身的生效日期起計：如牌照於3月1日生效，四季分別為3月至5月、6月至8月、9月至11月，以及12月至翌年2月。")
    return svg(W, H, ''.join(b), aria, 'cip', 860)


PR_KEY = legend([('', ("the period a return covers", "申報表涵蓋的期間")), ('must', ("the two weeks to lodge it", "遞交的兩星期")),
                 ('faint', ("the old quarterly cycle", "舊有每季周期"))])
