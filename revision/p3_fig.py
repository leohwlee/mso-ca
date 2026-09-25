# Figures for AMLO Part 3: the two tracks, and the warrant clock.
from bl_core import *


def txt(x, y_top, en, tc, cls='lbl', size=11, anchor='middle'):
    """Free text lines, one group per view, laid downward from y_top. Size is scaled by FS."""
    size = size * FS
    lh = max(size, 13.5) * 1.3
    out = []
    for v, ls in (('en', en), ('tc', tc), ('both', en + tc)):
        g = [f'<text class="{cls} s-{v}" font-size="{size}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y_top + size + i * lh:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def above(x, line_y, en, tc, anchor='middle'):
    """A label whose last line sits just above a horizontal line at line_y, in every view."""
    size = 11 * FS
    lh = max(size, 13.5) * 1.3
    n = nlines(en, tc)
    return txt(x, line_y - 11 - size - (n - 1) * lh, en, tc, anchor=anchor)


def nlines(en, tc):
    """How many lines a txt() block takes in the view being drawn."""
    return {'en': len(en), 'tc': len(tc), 'both': len(en) + len(tc)}[lay()]


def fig_tracks():
    W = 1000
    L, M, R = 20, 350, 680          # three columns, each 300 wide
    CW = 300
    COMM = Node(145, 380, ("The Commissioner of Customs and Excise", "海關關長"),
                ("your relevant authority · Sch. 1 Pt 2", "你的有關當局 · 附表1第2部"))
    AP = Node(L, CW, ("Authorized person", "獲授權人"), "s.9(12)")
    INV = Node(M, CW, ("Investigator", "調查員"), "s.11(1)")
    S9 = Node(L, CW, ("May enter your registered premises at any reasonable time, inspect and copy your business records, and make inquiries. No suspicion of anything is required.",
                      "可在任何合理時間進入你已登記的處所，查閱和複製你的業務紀錄，並作出查訊。毋須有任何懷疑。"), "s.9(1A)", 'may', answer=True)
    S12 = Node(M, CW, ("May require you in writing to produce records, to attend and answer questions, and to give any other assistance. Needs a reason to investigate.",
                       "可藉書面要求你交出紀錄、會晤並回答問題，以及提供其他協助。須有調查理由。"), "s.11(1) · s.12(2)", 'may', answer=True)
    WAR = Node(R, CW, ("A magistrate may issue a warrant to enter (by force if necessary), search, seize and remove",
                       "裁判官可發出手令，以進入（如有必要可強行進入）、搜尋、檢取和移走"), "s.17(1)", 'may', answer=True)
    REC = Node(L, 630, ("The records and documents you are required to produce",
                        "你被要求交出的紀錄及文件"))
    FAIL = Node(165, 340, ("You do not comply with an inspector's or investigator's requirement", "你沒有遵從視察人員或調查員施加的要求"), "s.9 · s.12")
    CFI = Node(M, 630, ("The authorized person or investigator who imposed the requirement may apply to the Court of First Instance, by originating summons, for an inquiry into the failure",
                        "施加要求的獲授權人或調查員，可藉原訴傳票向原訟法庭申請，要求對該項不遵從進行查訊"), "s.14(1)", 'may', answer=True)
    CRIM = Node(L, CW, ("Prosecution. Three tiers of offence, from no reasonable excuse up to intent to defraud.",
                        "刑事檢控。三級罪行，由無合理辯解至出於詐騙意圖。"), "s.10 · s.13", 'must', answer=True)
    PUN = Node(M, CW, ("Failure without reasonable excuse: you, and anyone knowingly involved, can be punished as if for contempt of court",
                       "無合理辯解而沒有遵從：你及明知而牽涉入的人可被懲罰，猶如犯藐視法庭罪"), "s.14(2)(b)", 'must', answer=True)
    ORD = Node(R, CW, ("No reasonable excuse: you can be ordered to comply within a time the Court specifies",
                       "無合理辯解：你可被命令在法庭指明的時間內遵從"), "s.14(2)(a)", 'must', answer=True)
    # room under REC for the warrant label, which hangs below the warrant's horizontal arrow
    wl_en, wl_tc = ["the same records,", "taken under the warrant"], ["同一批紀錄，", "憑手令取得"]
    rec_gap = max(40, 22 + nlines(wl_en, wl_tc) * 17.6 - REC.h / 2 + 8)
    il_en, il_tc = ["directs, or appoints with the", "Financial Secretary's consent"], ["指示，或經財政司司長", "同意後委任"]
    top_gap = 20 + nlines(il_en, il_tc) * 17.9 + 12
    H = place([([COMM], top_gap), ([AP, INV], 34), ([S9, S12, WAR], 44), ([REC], rec_gap), ([FAIL], 46),
               ([CFI], 40), ([CRIM, PUN, ORD], 0)])
    b = [n.render() for n in (COMM, AP, INV, S9, S12, WAR, REC, FAIL, CFI, CRIM, PUN, ORD)]
    m = 'p3'

    # Commissioner to the two officers; labels sit beside the vertical drops
    jy = COMM.bottom[1] + 14
    b.append(edge([COMM.bottom, (COMM.cx, jy), (AP.cx, jy), AP.top], mid=m))
    b.append(edge([COMM.bottom, (COMM.cx, jy), (INV.cx, jy), INV.top], mid=m))
    ly = jy + 6
    b.append(txt(AP.cx + 10, ly, ["authorises in writing"], ["藉書面授權"], anchor='start'))
    b.append(txt(INV.cx + 10, ly, il_en, il_tc, anchor='start'))
    b.append(edge([AP.bottom, S9.top], mid=m))
    b.append(edge([INV.bottom, S12.top], mid=m))

    # both tracks are after the same records; the warrant is a third way to take them
    ky = max(S9.bottom[1], S12.bottom[1]) + 18
    b.append(edge([S9.bottom, (S9.cx, ky), (REC.cx, ky), REC.top], mid=m))
    b.append(edge([S12.bottom, (S12.cx, ky), (REC.cx, ky), REC.top], mid=m))
    b.append(edge([WAR.bottom, (WAR.cx, REC.cy), (REC.x + REC.w, REC.cy)], mid=m))
    b.append(txt((REC.x + REC.w + WAR.cx) / 2 - 4, REC.cy + 4, wl_en, wl_tc))

    # failing to comply opens two routes
    b.append(edge([REC.bottom, (REC.bottom[0], FAIL.top[1])], mid=m))
    fy = FAIL.bottom[1] + 20
    b.append(edge([FAIL.bottom, (FAIL.cx, fy), (CRIM.cx, fy), CRIM.top], mid=m))
    b.append(edge([FAIL.bottom, (FAIL.cx, fy), (CFI.cx, fy), CFI.top], mid=m))
    gy = CFI.bottom[1] + 18
    b.append(edge([CFI.bottom, (CFI.cx, gy), (PUN.cx, gy), PUN.top], mid=m))
    b.append(edge([CFI.bottom, (CFI.cx, gy), (ORD.cx, gy), ORD.top], mid=m))

    # the bar between prosecution and contempt-style punishment only
    ty = max(CRIM.bottom[1], PUN.bottom[1]) + 22
    b.append(edge([CRIM.bottom, (CRIM.cx, ty), (PUN.cx, ty), PUN.bottom], mid=m, mstart=True))
    bl_en = ["for the same conduct, while one of these two is pending", "(or cannot be brought again), the other is barred;", "an order to comply is not"]
    bl_tc = ["就同一行為，其中一項仍待決或不得再次提起時，", "另一項即不得提起；命令遵從則不受此限"]
    b.append(txt((CRIM.cx + PUN.cx) / 2, ty + 4, bl_en, bl_tc))
    Ht = ty + 10 + nlines(bl_en, bl_tc) * 17.6 + 8
    aria = ("The Commissioner authorises an authorized person in writing for routine inspection, and directs or appoints an investigator. The inspector may enter your registered premises without suspicion; the investigator may compel you to attend and answer. Both are after the same records, and a magistrate's warrant is a third way to take them. If you do not comply with an inspector's or investigator's requirement, you may be prosecuted (non-compliance under a warrant is the separate s.17(9) offence); separately, the authorized person or investigator may apply to the Court of First Instance, which may order you to comply and may punish you as if for contempt. For the same conduct, while prosecution or contempt-style proceedings are pending or cannot be brought again, the other is barred; an order to comply is not barred.",
            "關長藉書面授權獲授權人作例行視察，並指示或委任調查員。視察者毋須任何懷疑即可進入你已登記的處所；調查員則可強制你會晤及回答。兩者針對同一批紀錄，而裁判官手令是取得同一批紀錄的第三條途徑。你若不遵從視察人員或調查員施加的要求，可被刑事檢控（不遵從手令下的要求屬第17(9)條所訂的另一項罪行）；另外，獲授權人或調查員亦可向原訟法庭申請，法庭可命令你遵從，並可猶如藐視法庭罪般懲罰你。就同一行為，刑事檢控或猶如藐視法庭罪的懲罰程序其中一項仍待決或不得再次提起時，另一項即不得提起；命令遵從則不受此限。")
    return svg(W, Ht, ''.join(b), aria, m, 860)


def fig_clock():
    W = 900
    WIN = Node(40, 356, ("Entry window: 7 days beginning on the date of the warrant. Entry at any time in those days, by force if necessary.",
                         "進入期限：手令日期起計7日。期內可隨時進入，如有必要可強行進入。"), "s.17(1)(a)", 'may')
    KEEP = Node(460, 420, ("Retention: up to 6 months beginning on the day of removal, or longer if the records are or may be required for criminal proceedings or proceedings under the Ordinance.",
                           "保留期：自移走當日起計不超過6個月；如屬或可能屬刑事法律程序或根據本條例進行的法律程序所需要，可保留較長期間。"), "s.17(4)", 'may')
    hh = max(WIN.h, KEEP.h)
    WIN.h = KEEP.h = hh
    H = place([([WIN, KEEP], 0)], y0=14)
    T0, T1, T7, BRK, T6, END = 100, 250, 360, 540, 740, 880
    lab_h = nlines(["x"], ["x"]) * 17.9
    y1 = H + 18 + lab_h  # lane 1: the 7-day window
    ext_en, ext_tc = ["longer if", "proceedings", "need them"], ["法律程序", "需要時可更長"]
    # lane 2: the retention period; leave room above it for the two-line extension label
    y2 = max(y1 + 30, H + 20 + 11 + 11 * FS + (nlines(ext_en, ext_tc) - 1) * max(11 * FS, 13.5) * 1.3)
    ay = y2 + 30         # the time axis
    m = 'p3c'
    b = [WIN.render(), KEEP.render()]

    def bracket(x1, x2, y, dashed_to=None):
        s = [f'<line class="e" x1="{x1}" y1="{y}" x2="{x2}" y2="{y}"/>',
             f'<line class="e" x1="{x1}" y1="{y-7}" x2="{x1}" y2="{y+7}"/>',
             f'<line class="e" x1="{x2}" y1="{y-7}" x2="{x2}" y2="{y+7}"/>']
        return ''.join(s)

    # lane 1: 7 days from the warrant date
    b.append(bracket(T0, T7, y1))
    b.append(above((T0 + T7) / 2, y1, ["7 days"], ["7日"]))
    # lane 2: up to 6 months from the day of removal, then a dashed extension
    b.append(bracket(T1, T6, y2))
    b.append(f'<line class="e" x1="{T6}" y1="{y2}" x2="{END}" y2="{y2}" stroke-dasharray="5 4" marker-end="url(#{mref(m)})"/>')
    b.append(above((T7 + BRK) / 2 + 20, y2, ["up to 6 months"], ["不超過6個月"]))
    b.append(above((T6 + END) / 2 + 6, y2, ext_en, ext_tc))
    # the axis, broken to show it is not to scale
    b.append(f'<line class="e" x1="60" y1="{ay}" x2="{BRK-6}" y2="{ay}"/>')
    b.append(f'<line class="e" x1="{BRK+6}" y1="{ay}" x2="{END}" y2="{ay}" marker-end="url(#{mref(m)})"/>')
    for yy in (y2, ay):
        b.append(f'<rect x="{BRK-6}" y="{yy-9}" width="12" height="18" fill="var(--bg)" stroke="none"/>')
        for dx in (-6, 2):
            b.append(f'<line class="e" x1="{BRK+dx}" y1="{yy+8}" x2="{BRK+dx+4}" y2="{yy-8}"/>')
    for x in (T0, T1, T6):
        b.append(f'<line class="e" x1="{x}" y1="{ay-8}" x2="{x}" y2="{ay+8}"/>')
        b.append(f'<line class="e" x1="{x}" y1="{y1 if x == T0 else y2}" x2="{x}" y2="{ay}" stroke-dasharray="2 3"/>')
    le0, lt0 = ["date of the warrant"], ["手令日期"]
    le1, lt1 = ["an entry within the 7 days:", "records removed, and a", "receipt given as soon as", "reasonably practicable"], \
               ["在7日內進入：", "移走紀錄，並須在合理地", "切實可行範圍內盡快", "發出收據"]
    le6, lt6 = ["6 months after removal"], ["移走後6個月"]
    b.append(txt(T0, ay + 12, le0, lt0, 'c-sans'))
    b.append(txt(T1 + 12, ay + 12, le1, lt1, 'c-sans', anchor='start'))
    b.append(txt(T6, ay + 12, le6, lt6, 'c-sans'))
    b.append(txt(END, ay + 12 + max(nlines(le6, lt6), 1) * 17.9 + 4, ["not to scale"], ["非按比例"], 'c-sans', size=10.5, anchor='end'))
    Ht = ay + 12 + nlines(le1, lt1) * 17.9 + 12
    aria = ("The only two fixed periods in Part 3, both attached to a magistrate's warrant. Entry must happen within seven days beginning on the date of the warrant. Records removed on such an entry may be retained for up to six months beginning on the day of removal, or longer, for as long as needed, if they are or may be required for criminal proceedings or proceedings under the Ordinance, and a receipt must be given as soon as reasonably practicable after removal.",
            "第3部僅有的兩個固定期間，均與裁判官手令有關。進入處所須在自手令日期起計的7日內進行。在進入時移走的紀錄，可自移走當日起保留不超過6個月；如屬或可能屬刑事法律程序或根據本條例進行的法律程序所需要，則可在該等程序所需的較長期間內保留；移走後亦須在合理地切實可行範圍內盡快發出收據。")
    return svg(W, Ht, ''.join(b), aria, m, 720)
