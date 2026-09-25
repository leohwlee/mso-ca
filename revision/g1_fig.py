# Figures for the Guideline Chapter 1 page: the three stages of laundering, the
# FATF's standard-setting cycle, the offences a suspicion can lead to, and what
# follows when a requirement of the Guideline is not met.
from ui import *


def dash(pts):
    d = ' '.join(f'{x:.0f},{y:.0f}' for x, y in pts)
    return f'<polyline class="e e-dash" points="{d}"/>'


def mlab(x, y, en, tc, anchor='middle'):
    """Edge label like ui.mlabel, but with 16 units between the stacked English and
    Chinese lines of the combined view, so the two do not touch."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        n = len(ls)
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (n - 1 - i) * 16:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def even(*ns):
    h = max(n.h for n in ns)
    for n in ns:
        n.h = h


# ---------------------------------------------------------------- 1. the three stages
def fig_stages():
    W = 1000
    P1 = Card(30, 230, ("1 · Placement", "1 · 存放"),
              ("Disposing of cash proceeds derived from illegal activities into the financial system",
               "處置來自非法活動的現金得益，並注入金融體系"), 'plain', "¶1.10(a)", answer=True)
    P2 = Card(295, 310, ("2 · Layering", "2 · 分層交易"),
              ("Separating illicit proceeds from their source through complex layers of financial transactions, designed to disguise the source, subvert the audit trail and provide anonymity",
               "透過複雜多層的金融交易，將非法得益及其來源分開，從而隱藏款項的來源、掩飾審計線索和隱藏擁有人的身分"), 'plain', "¶1.10(b)", answer=True)
    P3 = Card(640, 330, ("3 · Integration", "3 · 整合"),
              ("Creating the impression of apparent legitimacy for criminally derived wealth. Where layering succeeds, the proceeds return to the general financial system and appear to come from, or be connected to, legitimate business",
               "為犯罪得來的財富製造表面的合法性。當分層交易成功，經清洗的得益便回流到一般金融體系，令人以為來自或涉及合法的商業活動"), 'plain', "¶1.10(c)", answer=True)
    even(P1, P2, P3)
    for n in (P1, P2, P3):
        n.h += 10
    D = Card(30, 940, ("Your duty: be alert to any sign of any stage", "你的責任：留意任何一個階段的徵兆"),
             ("The stages frequently involve numerous transactions. The Guideline says an MSO should be alert to any such sign of potential criminal activity, and in this Guideline 'should' means a mandatory requirement",
              "這些階段經常涉及多宗交易。指引訂明金錢服務經營者應留意可能涉及犯罪活動的徵兆；在本指引中，「應」即屬強制規定"),
             'must', "¶1.10 · ¶1.6")
    H = place([([P1, P2, P3], 40), ([D], 0)], y0=14)
    m = 'g1s'
    b = [n.render() for n in (P1, P2, P3, D)]
    b.append(edge([P1.right, P2.left], mid=m))
    b.append(edge([P2.right, P3.left], mid=m))
    aria = ("The three common stages of money laundering, left to right. Placement disposes of cash proceeds of illegal activities into the financial system. Layering separates the proceeds from their source through complex layers of transactions that disguise the source, subvert the audit trail and provide anonymity. Integration gives criminally derived wealth apparent legitimacy, returning it to the general financial system looking like legitimate business. Below, the MSO's duty: the stages often involve numerous transactions, and the MSO should be alert to any sign of them.",
            "洗錢的三個常見階段，由左至右。存放：處置來自非法活動的現金得益並注入金融體系。分層交易：透過複雜多層的金融交易將得益與來源分開，隱藏來源、掩飾審計線索和隱藏擁有人的身分。整合：為犯罪得來的財富製造表面的合法性，令其回流到一般金融體系，看似來自合法商業活動。下方是金錢服務經營者的責任：這些階段經常涉及多宗交易，經營者應留意任何徵兆。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


STAGES_KEY = legend([('', ("a stage of laundering", "洗錢的一個階段")), ('must', ("your duty", "你的責任"))])


# ---------------------------------------------------------------- 2. the FATF
def fig_fatf():
    W = 1000
    A = Card(30, 300, ("The FATF", "財務行動特別組織"),
             ("An inter-governmental body formed in 1989, to set standards and promote effective implementation of legal, regulatory and operational measures against ML, TF, PF and related threats",
              "於1989年成立的跨政府組織，宗旨是制訂標準，並推動有效執行法律、監管及作業措施，以打擊洗錢、恐怖分子資金籌集、擴散資金籌集及相關威脅"),
             'plain', "¶1.13")
    B_ = Card(350, 330, ("It sets the standard", "制訂標準"),
              ("The FATF Recommendations, recognised as the international standard for combating ML, TF and PF, and the basis for a co-ordinated response and a level playing field",
               "特別組織建議獲承認為打擊洗錢、恐怖分子資金籌集及擴散資金籌集的國際標準，為協調應對威脅提供基礎，並有助營造公平競爭的環境"),
              'plain', "¶1.13")
    C = Card(700, 270, ("It checks jurisdictions", "監察各司法管轄區"),
             ("Evaluations of each jurisdiction's compliance, then stringent follow-up",
              "透過評核監察各司法管轄區的合規情況並在評核後進行嚴格的跟進程序"),
             'plain', "¶1.13")
    even(A, B_, C)
    HK = Card(30, 480, ("Hong Kong, as a member, is obliged to implement the latest Recommendations", "香港作為成員，有責任實施最新的特別組織建議"),
              ("It is important that Hong Kong complies with the international standards to maintain its status as an international financial centre. Its main laws on ML, TF, PF and financial sanctions follow in the next section",
               "香港必須符合國際標準，以維持其國際金融中心的地位。香港在這方面的主要法例見下一節"),
              'plain', "¶1.13–1.14")
    D = Card(540, 430, ("It names high-risk and other monitored jurisdictions", "識別高度風險及其他受監察的司法管轄區"),
             ("These may face enhanced scrutiny by the FATF, or counter-measures by FATF members and the international community",
              "特別組織可能加強對這些地區的審查，而特別組織成員及國際社會也可能對其採取針對措施"),
             'may', "¶1.13")
    even(HK, D)
    E = Card(30, 940, ("What the FATF's two lists call for", "特別組織兩份名單的要求"),
             ("High-risk jurisdictions: the FATF calls for enhanced due diligence and, in the most serious cases, countermeasures. Jurisdictions under increased monitoring: the FATF encourages its members to take the statement into account in their risk analysis. The circular of 3 July 2026 relays the June 2026 statements; the FAQ on both lists is on the Circulars page",
              "高風險司法管轄區：特別組織要求採取更嚴格的盡職審查，在最嚴重的情況下採取針對措施。被加強監察的司法管轄區：特別組織鼓勵其成員在進行風險分析時參考有關聲明。2026年7月3日的通函轉達2026年6月的聲明；有關兩份名單的常見問題見通函一頁"),
             'faint', ("Circular 3 Jul 2026", "2026年7月3日通函"), href="#ci-edd")
    H = place([([A, B_, C], 56), ([HK, D], 40), ([E], 0)], y0=14)
    m = 'g1f'
    b = [n.render() for n in (A, B_, C, HK, D, E)]
    b.append(edge([A.right, B_.left], mid=m))
    b.append(edge([B_.right, C.left], mid=m))
    # standard -> Hong Kong: down from the Recommendations, into Hong Kong's box from above
    b.append(edge([(440, B_.bottom[1]), (440, HK.y)], mid=m))
    b.append(mlab(430, B_.bottom[1] + 34, "members implement", "成員實施", anchor='end'))
    b.append(edge([(C.cx, C.bottom[1]), (C.cx, D.y)], mid=m))
    b.append(mlab(C.cx - 10, C.bottom[1] + 34, "in its follow-up", "跟進程序中", anchor='end'))
    b.append(dash([D.bottom, (D.cx, E.y)]))
    aria = ("The FATF's standard-setting cycle. The FATF, an inter-governmental body formed in 1989, sets the FATF Recommendations, recognised as the international standard for combating ML, TF and PF. It evaluates jurisdictions' compliance and follows up, identifying high-risk and other monitored jurisdictions, which may face enhanced scrutiny or counter-measures. Hong Kong, as a member, is obliged to implement the latest Recommendations, and it is important that it complies with the international standards to keep its status as an international financial centre. For high-risk jurisdictions the FATF calls for enhanced due diligence and, in the most serious cases, countermeasures; the C&ED relayed the June 2026 statements by circular on 3 July 2026.",
            "特別組織制訂及監察標準的過程。特別組織是1989年成立的跨政府組織，訂立特別組織建議，獲承認為打擊洗錢、恐怖分子資金籌集及擴散資金籌集的國際標準。它評核各司法管轄區的合規情況並作跟進，識別高度風險及其他受監察的司法管轄區；特別組織可能加強對這些地區的審查，而特別組織成員及國際社會也可能對其採取針對措施。香港作為成員，有責任實施最新的建議，並必須符合國際標準，以維持其國際金融中心的地位。就高風險司法管轄區，特別組織要求採取更嚴格的盡職審查，在最嚴重的情況下採取針對措施；海關於2026年7月3日以通函轉達2026年6月的聲明。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


FATF_KEY = legend([('', ("the FATF, and what follows for Hong Kong", "特別組織及其對香港的影響")),
                   ('may', ("action others may take", "其他各方可採取的行動")),
                   ('faint', ("the latest circular, and where to read on", "最新通函及延伸閱讀"))])


# ---------------------------------------------------------------- 3. the offences
def fig_offences():
    W = 1000
    S = Card(230, 540, ("Property at your counter may be the proceeds of crime, or terrorist property", "你櫃枱前的財產可能是犯罪得益或恐怖分子財產"),
             None, 'plain', "¶1.22–1.25")
    A = Card(44, 290, ("You deal with it anyway", "你仍然處理該財產"), None, 'plain')
    Bq = Card(356, 290, ("You keep quiet about what you know or suspect", "你對所知悉或懷疑的事保持沉默"), None, 'plain')
    C = Card(668, 300, ("You disclose it as soon as it is reasonable", "你在合理範圍內盡快作出披露"),
             ("That meets the disclosure duty", "這樣便履行了披露責任"), 'ok', "¶1.24", answer=True)
    even(A, Bq, C)
    A2 = Card(44, 290, ("Offence: dealing with proceeds", "罪行：處理得益"),
              ("If you knew, or had reasonable grounds to believe, it represents proceeds of drug trafficking or of an indictable offence. Up to 14\u00a0years and $5\u00a0million",
               "如你知道或有合理理由相信該財產代表販毒或可公訴罪行的得益。最高監禁14年及罰款五百萬元"),
              'stop', "¶1.22", answer=True)
    B2 = Card(356, 290, ("Offence: failure to disclose", "罪行：未有披露"),
              ("You knew or suspected, and did not disclose as soon as it was reasonable. Up to 3\u00a0months and $50,000",
               "你知悉或懷疑，卻未能在合理範圍內盡快作出披露。最高可判監禁3個月及罰款50,000元"),
              'stop', "¶1.24", answer=True)
    C2 = Card(668, 300, ("Then say nothing that could prejudice an investigation", "其後不可洩露任何可能損害調查的事宜"),
              ("Knowing or suspecting that a disclosure has been made, whoever made it, disclose to no one anything likely to prejudice an investigation that might follow",
               "知道或懷疑已曾作出披露，不論披露由誰作出，都不可向任何人披露相當可能損害其後調查的事宜"),
              'must', "¶1.25")
    even(A2, B2, C2)
    A3 = Card(44, 290, ("Offence: if it is for terrorists", "罪行：如財產是為恐怖分子提供"),
              ("Providing or collecting property for, or making property or financial (or related) services available to, terrorists or terrorist associates. Up to 14\u00a0years and a fine",
               "向恐怖分子或與恐怖分子有聯繫者提供或籌集財產，或向他們提供財產或金融（或有關的）服務。最高監禁14年及罰款"),
              'stop', "¶1.23", answer=True)
    N = Card(44, 924, ("Disclosing can also give you a defence to the ML/TF offence", "作出披露亦可為你提供洗錢／恐怖分子資金籌集罪行的免責辯護"),
             ("An STR to the JFIU gives a statutory defence to the ML/TF offence for the acts it discloses: made before them, with the JFIU's consent to the acts; or after them, on your own initiative and as soon as reasonable. Chapter 7",
              "向財富情報組提交可疑交易報告，可就報告所披露的作為提供洗錢／恐怖分子資金籌集罪行的法定免責辯護：在作出該作為之前提交，而該作為得到財富情報組同意；或在其後主動及在合理範圍內盡快提交。見第7章"),
             'faint', "¶7.25", href="#g7-after")
    C3 = Card(668, 300, ("Offence: tipping off", "罪行：通風報訊"),
              ("Up to 3\u00a0years and a fine", "最高監禁3年及罰款"), 'stop', "¶1.25", answer=True)
    H = place([([S], 58), ([A, Bq, C], 40), ([A2, B2, C2], 44), ([A3, C3], 40), ([N], 0)], y0=14)
    m = 'g1o'
    b = [n.render() for n in (S, A, Bq, C, A2, B2, C2, A3, N, C3)]
    jy = S.bottom[1] + 26
    b.append(edge([S.bottom, (S.cx, jy), (A.cx, jy), A.top], mid=m))
    b.append(edge([(S.cx, jy), (C.cx, jy), C.top], mid=m))
    b.append(edge([(Bq.cx, jy), Bq.top], mid=m))
    for a, c in ((A, A2), (Bq, B2), (C, C2)):
        b.append(edge([a.bottom, c.top], mid=m))
    # dealing with it, where it is for terrorists: down the left margin, past the dealing box
    gx = 22
    b.append(edge([A.left, (gx, A.cy), (gx, A3.cy), A3.left], mid=m))
    b.append(edge([C2.bottom, C3.top], mid=m))
    b.append(mlab(C2.cx + 10, (C2.bottom[1] + C3.y) / 2 + 5, "if you tip anyone off", "如仍洩露", anchor='start'))
    # the defence comes from disclosing: down the right margin, past the tipping-off boxes
    rx = W - 18
    b.append(dash([C.right, (rx, C.cy), (rx, N.cy), N.right]))
    aria = ("Three things you might do when property at your counter may be the proceeds of crime or terrorist property. Deal with it anyway: an offence if you knew or had reasonable grounds to believe it represents proceeds of drug trafficking or an indictable offence, up to 14 years and $5 million; and, where property or services go to terrorists or terrorist associates, a UNATMO offence, up to 14 years and a fine. Keep quiet: failing to disclose knowledge or suspicion as soon as reasonable is an offence, up to 3 months and $50,000. Disclose as soon as reasonable: that meets the duty, but anyone who knows or suspects a disclosure has been made must then say nothing likely to prejudice an investigation; tipping off carries up to 3 years and a fine. Disclosing can also give a statutory defence to the ML/TF offence for the acts disclosed, set out in Guideline Chapter 7.",
            "當櫃枱前的財產可能是犯罪得益或恐怖分子財產時，你可能採取的三種做法。仍然處理：如你知道或有合理理由相信該財產代表販毒或可公訴罪行的得益，即屬犯罪，最高監禁14年及罰款五百萬元；如向恐怖分子或與恐怖分子有聯繫者提供財產或服務，即屬《聯合國（反恐怖主義措施）條例》下的罪行，最高監禁14年及罰款。保持沉默：未能在合理範圍內盡快披露所知悉或懷疑的事，即屬犯罪，最高監禁3個月及罰款50,000元。在合理範圍內盡快披露：這樣便履行了責任，但任何人知道或懷疑已曾作出披露，就不可洩露任何相當可能損害調查的事宜；通風報訊最高可判監禁3年及罰款。作出披露亦可就所披露的作為提供洗錢／恐怖分子資金籌集罪行的法定免責辯護，見指引第7章。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


OFF_KEY = legend([('', ("the situation, and what you might do", "情況及你可能採取的做法")), ('ok', ("meets the duty", "履行責任")),
                  ('must', ("a duty that follows", "隨之而來的責任")), ('stop', ("a criminal offence", "刑事罪行")),
                  ('faint', ("where to read on", "延伸閱讀"))])


# ---------------------------------------------------------------- 4. when a requirement is not met
def fig_status():
    W = 1000
    T = Card(200, 600, ("A requirement the Guideline states with 'must' or 'should' is not met", "未有遵守指引以「須」或「應」表述的一項規定"),
             ("The Guideline is published by the CCE under section 7 of the AMLO, and compliance with it is enforced through the AMLO",
              "指引由海關關長根據打擊洗錢條例第7條公布，其遵行情況按照打擊洗錢條例強制執行"),
             'plain', "¶1.1 · ¶1.3 · ¶1.6")
    M = Card(30, 270, ("The MSO", "金錢服務經營者"),
             ("May face disciplinary and other actions under the AMLO for not complying with the relevant requirements",
              "或會因沒有遵守相關規定而面對根據打擊洗錢條例採取的紀律行動及其他行動"),
             'must', "¶1.3")
    F = Card(315, 270, ("Its sole proprietor, partner, director and ultimate owner, where applicable", "其獨資經營者、合夥人、董事和最終擁有人（如適用）"),
             ("Non-compliance may also reflect adversely on their fitness and properness",
              "不遵從指引，將對他們作為適當人選帶有負面影響"),
             'must', "¶1.3")
    L = Card(600, 380, ("In AMLO court proceedings, and when the Commissioner weighs a Schedule 2 breach", "在根據打擊洗錢條例進行的法院程序中，以及關長判斷有否違反附表2時"),
             ("Failing to comply does not by itself make anyone liable to proceedings. In AMLO court proceedings the Guideline is admissible in evidence, and the court must take any provision that appears relevant into account; the Commissioner must have regard to it in judging a Schedule 2 breach. See the Part 2 page",
              "沒有遵守指引本身不會令人被起訴；但在根據打擊洗錢條例於法院進行的法律程序中，指引可獲接納為證據，法院須考慮攸關的條文；關長判斷有否違反附表2時亦須顧及。見第2部一頁"),
             'faint', "¶1.8", href="#p2-guidelines")
    even(M, F, L)
    H = place([([T], 56), ([M, F, L], 0)], y0=14)
    m = 'g1r'
    b = [n.render() for n in (T, M, F, L)]
    jy = T.bottom[1] + 26
    b.append(edge([T.bottom, (T.cx, jy), (M.cx, jy), M.top], mid=m))
    b.append(edge([(T.cx, jy), (L.cx, jy), L.top], mid=m))
    b.append(edge([(F.cx, jy), F.top], mid=m))
    aria = ("What follows when a requirement the Guideline states with must or should is not met. The Guideline is published by the CCE under section 7 of the AMLO and enforced through the AMLO. The MSO may face disciplinary and other actions under the AMLO. Non-compliance may also reflect adversely on the fitness and properness of its sole proprietor, partner, director and ultimate owner, where applicable. Failing to comply does not by itself make anyone liable to proceedings, but in AMLO court proceedings the Guideline is admissible in evidence and the court must take any relevant provision into account, and the Commissioner must have regard to it when considering a Schedule 2 contravention, as the Part 2 page explains.",
            "未有遵守指引以「須」或「應」表述的規定時的後果。指引由海關關長根據打擊洗錢條例第7條公布，並按照該條例強制執行。金錢服務經營者或會面對根據條例採取的紀律行動及其他行動。金錢服務經營者不遵從指引，將對其獨資經營者、合夥人、董事和最終擁有人（如適用）作為適當人選帶有負面影響。沒有遵守指引本身不會令人被起訴，但在根據打擊洗錢條例於法院進行的法律程序中，指引可獲接納為證據，法院須考慮攸關的指引條文，關長在考慮有否違反附表2時亦須顧及指引，詳見第2部一頁。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


STATUS_KEY = legend([('', ("the starting point", "起點")), ('must', ("a consequence for you", "你要承受的後果")),
                     ('faint', ("where to read on", "延伸閱讀"))])
