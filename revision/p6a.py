# AMLO Part 6A: confidentiality requirements, ss.76A-76G.
import re
from ui import *


def _toks(text):
    """Like bl_core.tokens, but a run wrapped in {braces} is kept on one line (Chinese words, 監禁2年)."""
    out = []
    for seg in re.split(r'(\{[^}]*\})', text):
        if seg.startswith('{') and seg.endswith('}'):
            out.append(seg[1:-1])
        elif seg:
            out.extend(tokens(seg))
    return out


def _wrap(text, width_px, size):
    lines, cur, cw = [], '', 0.0
    for tok in _toks(text):
        w = tw(tok, size)
        if tok == ' ':
            if cur:
                cur += ' '; cw += w
            continue
        if cw + w <= width_px or not cur or (tok in NOSTART):
            cur += tok; cw += w
        else:
            lines.append(cur.rstrip()); cur, cw = tok, w
    if cur.strip():
        lines.append(cur.rstrip())
    return lines


def _plain(pair):
    return None if pair is None else tuple(re.sub(r'[{}]', '', t) for t in pair)


class NCard(Card):
    """A Card whose Chinese never breaks inside a {braced} word."""

    def __init__(self, x, w, title, body=None, kind='plain', cite=None, href=None,
                 size=11.5, tsize=12.5, minh=0, answer=False):
        super().__init__(x, w, _plain(title), _plain(body), kind, cite, href, size, tsize, minh, answer)
        size, tsize, inner = size * FS, tsize * FS, w - 24
        tcls = 't-inv t-b' if kind == 'stop' else 't t-b'
        bcls = 't-inv' if kind == 'stop' else 't'
        for i, v in enumerate(('en', 'tc')):
            tl = _wrap(title[i], inner, tsize) if title and title[i] else []
            bl = _wrap(body[i], inner, size) if body and body[i] else []
            self.seg[v] = [(l, tcls, tsize) for l in tl] + [(l, bcls, size) for l in bl]
        self.seg['both'] = self.seg['en'] + self.seg['tc']
        self.h = max(minh, sum(s * LH for _, _, s in self.seg[lay()]) + 16 + (CS * LH if cite else 0))


def _same_h(*cards):
    """Give the cards of one row one height, so their tops and bottoms line up."""
    h = max(c.h for c in cards)
    for c in cards:
        c.h = h


def _route_label(x, y_bottom, text):
    """Edge label; in the combined view English sits above Chinese, 17 units apart."""
    en, tc = text
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        g = [f'<text class="lbl s-{v}" text-anchor="middle">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y_bottom - (len(ls) - 1 - i) * 17:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def fig_secret():
    W = 1000
    LX, RX, CW = 34, 526, 440          # left column x, right column x, column width
    REG = NCard(LX, CW, ("The regulator's side: specified persons", "監管方：{指明人士}"),
               ("The Commissioner; anyone who is or was his member, employee, consultant, agent or adviser; and anyone appointed under, performing a function under, or assisting in a function under the Ordinance",
                "{關長}；屬或曾屬其{成員}、{僱員}、{顧問}或{代理人}的人；以及{根據本條例}{獲委任}、{執行職能}，或協助{執行職能}的人"), cite="s.76A")
    YOU = NCard(RX, CW, ("You, the licensee", "你（持牌人）"),
               ("Once a section 9 or 12 requirement has been imposed on you, or you have been given a section 22 or 44 disciplinary notice",
                "一旦有{第9或12條}的要求{施加於你}，或你獲發{第22或44條}的{紀律通知}"), 'must', "s.76E(1)")
    REGR = NCard(LX, CW, ("Must not pass on what it learns, or let anyone see the records", "{不得}傳達所{獲悉的事宜}，亦{不得}讓他人取覽{紀錄}"),
                ("Anything learned, and any record obtained, through an appointment or a function under the Ordinance. Permitted disclosures include those in performing a function, for criminal proceedings or an investigation in Hong Kong, and under a court order. The Commissioner has more, including to other regulators",
                 "凡憑藉{根據本條例}{獲委任}，或在執行或協助{執行職能}的{過程中}{獲悉}的事宜及{取得}的{紀錄}，均{受約束}。{獲准許的披露}{包括}{執行職能}、在香港進行的{刑事法律程序}或{調查}，以及{法院命令}。{關長}另可作{其他}{獲准許的披露}，{包括}向{其他}{監管機構}{披露}"),
                cite="s.76B · s.76C · s.76D")
    YOUR = NCard(RX, CW, ("Must not disclose what you learn from it", "{不得}{披露}從中獲得的{資料}"),
                ("Unless the Commissioner consents, or it is already lawfully public, or it is for professional advice, for proceedings you are a party to, or a court order or the law requires it",
                 "除非獲{關長}{同意}，或{資料}已{合法公開}，{或是}為徵詢{專業意見}，{或是}在你{身為一方}的{法律程序}中{披露}，{或是}按照{法院命令}或{法律規定}{披露}"), 'must', "s.76E(2)–(4)")
    REGP = NCard(LX, CW, ("Offence: $1,000,000 and 2 years on indictment", "罪行：循{公訴程序}{定罪}，{罰款$1,000,000及監禁2年}"), None, 'stop', "s.76B(3)", answer=True)
    YOUP = NCard(RX, CW, ("Offence: a fine at level 4, and no imprisonment", "罪行：第4級{罰款}，{不設監禁}"), None, 'stop', "s.76E(6)", answer=True)
    ON = NCard(150, 700, ("Specified recipients: whoever receives it through most permitted disclosures, and anyone who gets it from them", "{指明收取人}：經大部分{獲准許的披露}{接獲}{資料}的人，以及從其處{取得}{資料}的人"),
              ("Must not pass it on either, unless the relevant authority consents, it is already public, or it is for professional advice, for proceedings they are a party to, or a court order or the law requires it. Those not bound include whoever receives an anonymised summary, a disclosure to an overseas regulator, or one made with the consent of the person it came from and of anyone it is about, and anyone you tell only information that is already lawfully public",
               "同樣{不得}再向他人{披露}，除非獲{有關當局}{同意}、{資料}是{公眾已可得到的}，{或是}為徵詢{專業意見}，{或是}在其{身為一方}的{法律程序}中{披露}，{或是}按照{法院命令}或{法律規定}{披露}。{不受約束}的人包括：經{撮要形式}、向{香港以外}{監管機構}{披露}，或經{提供資料的人}及{資料}{所關乎}的人{同意}而獲{披露}{資料}的人，以及你只向其{披露}{已合法公開}{資料}的人"),
              cite="s.76F(1), (4)")
    ONP = NCard(ON.x + 130, 440, ("Offence: $1,000,000 and 2 years on indictment", "罪行：循{公訴程序}{定罪}，{罰款$1,000,000及監禁2年}"), None, 'stop', "s.76F(3), (7)", answer=True)
    for row in ((REG, YOU), (REGR, YOUR), (REGP, YOUP)):
        _same_h(*row)
    both = lay() == 'both'
    H = place([([REG, YOU], 34), ([REGR, YOUR], 36), ([REGP, YOUP], 70 if both else 56), ([ON], 36), ([ONP], 0)])
    b = [n.render() for n in (REG, YOU, REGR, YOUR, REGP, YOUP, ON, ONP)]
    m = 'p6aa'
    b.append(edge([REG.bottom, REGR.top], mid=m))
    b.append(edge([YOU.bottom, YOUR.top], mid=m))
    b.append(edge([REGR.bottom, REGP.top], ("if broken", "如違反"), REGR.cx + 10, (REGR.bottom[1] + REGP.top[1]) / 2 + 5, 'start', mid=m))
    b.append(edge([YOUR.bottom, YOUP.top], ("if broken", "如違反"), YOUR.cx + 10, (YOUR.bottom[1] + YOUP.top[1]) / 2 + 5, 'start', mid=m))
    b.append(edge([ON.bottom, ONP.top], ("if broken", "如違反"), ON.cx + 10, (ON.bottom[1] + ONP.top[1]) / 2 + 5, 'start', mid=m))
    ky = REGP.bottom[1] + (50 if both else 36)
    lx, rx = 14, W - 14
    la, ra = ON.x + 70, ON.x + ON.w - 70
    b.append(edge([REGR.left, (lx, REGR.cy), (lx, ky), (la, ky), (la, ON.top[1])], mid=m))
    b.append(edge([YOUR.right, (rx, YOUR.cy), (rx, ky), (ra, ky), (ra, ON.top[1])], mid=m))
    b.append(_route_label((lx + la) / 2, ky - 7, ("by most permitted disclosures", "經大部分獲准許的披露")))
    b.append(_route_label((rx + ra) / 2 - 22, ky - 7, ("with consent or most conditions", "經同意或符合大部分條件")))
    aria = ("Who must keep information secret. Specified persons on the regulator's side must not pass on anything they learn, or any record they obtain, through an appointment or a function under the Ordinance, unless it is a permitted disclosure, on pain of $1,000,000 and two years. The licensee, once a section 9 or 12 requirement is imposed or a section 22 or 44 notice is given, must not disclose what it learns from it unless the Commissioner consents or one of four conditions applies, on pain of a level 4 fine. Whoever receives the information through most permitted disclosures, and anyone who gets it from them, must not pass it on either, on pain of $1,000,000 and two years; someone the licensee tells only information that is already lawfully public is not bound.",
            "誰須保密。監管方的指明人士，對憑藉根據本條例獲委任、或在執行或協助執行職能的過程中獲悉的事宜及取得的紀錄，除非屬獲准許的披露，否則不得傳達，違者可處罰款$1,000,000及監禁2年。持牌人一旦被施加第9或12條的要求或獲發第22或44條的通知，除非獲關長同意或符合四項條件之一，否則不得披露從中獲得的資料，違者可處第4級罰款。經大部分獲准許的披露接獲資料的人，以及從其處取得資料的人，同樣不得再向他人披露，違者可處罰款$1,000,000及監禁2年；持牌人只向其披露已合法公開資料的人，則不受此約束。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


A = sec('who', [("Part 6A", "第6A部"), "s.76A–s.76G", ("added 2022", "2022年增補")],
        ("The regulator and you each owe a duty of secrecy", "監管方與你各有保密責任"),
    P("Read the two columns separately: the left one is the regulator's duty, the right one is yours. They differ in what they cover and in the penalty. The wide box below both columns catches most people the information is lawfully passed on to, whichever side passed it.",
      "兩欄分開閱讀：左欄是監管方的責任，右欄是你的責任。兩者涵蓋的範圍和罰則都不同。兩欄下方的闊方格涵蓋大部分經獲准許的披露而取得資料的人，不論資料由哪一方披露。")
    + fig(fig_secret, ("The gap between the two penalties is the point to remember: breaching the regulator's confidence risks prison, while a licensee who talks about its own inspection faces only a level 4 fine.",
                         "要記住的是兩者罰則的差距：監管方洩密可被判監禁，而持牌人談論自己所受的視察，只會被處第4級罰款。"),
          legend([('', ("someone else, and their duty", "他人及其責任")), ('must', ("you, and your duty", "你及你的責任")), ('stop', ("the offence", "罪行"))]))
    + traps(
        trap(("The regulator must keep more secret than you do", "監管方須保密的範圍比你廣"), None, "s.76B(1) · s.76E(2)–(3)",
             vs=[(("The regulator's side", "監管方"), ("Anything learned, and any record obtained, through an appointment or a function under the Ordinance. It is not limited to inspections, investigations and disciplinary action.", "憑藉根據本條例獲委任，或在執行或協助執行本條例職能的過程中獲悉的任何事宜及取得的紀錄。範圍不限於視察、調查及紀律處分。")),
                 (("You", "你"), ("Only what you learn from a section 9 or 12 requirement, or from a section 22 or 44 notice and your communications with the Commissioner about its subject matter.", "只限於你從第9或12條的要求，或從第22或44條的通知及就該通知的標的事宜與關長的通訊中獲得的資料。"))]),
        trap(("Level 4 for you, prison for them", "你是第4級罰款，他們是監禁"), None, "s.76B(3) · s.76E(6) · s.76F(7)",
             vs=[(("You, disclosing without a condition", "你在不符合條件下披露"), ("A fine at level 4 on conviction. There is no indictment tier and no imprisonment.", "一經定罪，可處第4級罰款。不設公訴程序，亦不設監禁。")),
                 (("A specified person, or an onward recipient", "指明人士或其後的收取人"), ("$1,000,000 and 2 years on indictment; level 6 and 6 months summarily.", "公訴程序：罰款$1,000,000及監禁2年；簡易程序：第6級罰款及監禁6個月。"))]),
        trap(("It is not only the licensee who is bound", "受約束的不只是持牌人"),
             ("Section 76E catches any person on whom a section 9 or 12 requirement has been imposed. A bank or any other person required to produce your records is bound in the same way as you are.",
              "第76E條涵蓋任何被施加第9或12條要求的人。被要求交出你紀錄的銀行或任何其他人，與你一樣受到約束。"),
             "s.76E(1)(a) · s.9(6) · s.12(1)"),
    ))

# ---------------------------------------------------------------- B. your own duty
B_ = sec('you', ["s.76E", ("your duty", "你的責任")],
         ("Who you may tell", "你可以告訴誰"),
    P("Once the duty has started, every disclosure needs either the Commissioner's consent or one of four conditions. Find the person you want to tell.",
      "責任一旦開始，每次披露都需要關長同意，或符合四項條件之一。先找出你想告訴的人。")
    + table([th("You want to tell", "你想告訴"), th("Allowed?", "可否？"), th("Why", "理由")], [
        tr(td("Your solicitor, counsel or another professional adviser, acting in a matter arising under the Ordinance", "就本條例所引起的事宜行事的律師、大律師或其他專業顧問"),
           f'<td class="verdict">{YES}</td>', td("Seeking or receiving professional advice is one of the four conditions", "徵詢或獲得專業意見屬四項條件之一", "s.76E(4)(b)")),
        tr(td("A court or tribunal hearing proceedings you are a party to, such as your own review", "審理你身為一方的法律程序的法院或審裁處，例如你自己的覆核"),
           f'<td class="verdict">{YES}</td>', td("Disclosure in connection with proceedings you are a party to", "在你身為一方的法律程序中披露", "s.76E(4)(c)")),
        tr(td("Anyone, because a court has ordered it or a Hong Kong law requires it", "任何人，因法院已作出命令或香港法律有此規定"),
           f'<td class="verdict">{YES}</td>', td("Disclosure in accordance with an order or a law of Hong Kong", "按照命令或香港法律作出的披露", "s.76E(4)(d)")),
        tr(td("Anyone, but only information that has already been lawfully made public, for example the details, reasons and material facts the Commissioner publishes with a disciplinary decision", "任何人，但只限於已合法公開的資料（例如關長公布紀律決定時披露的細節、理由及重要事實）"),
           f'<td class="verdict">{YES}</td>', td("The information has already become public through a disclosure section 76B does not forbid. Everything else you learned from the notice or the requirement stays confidential", "資料已因第76B條沒有禁止的披露而可供公眾取得。你從通知或要求中獲得的其他資料，仍須保密", "s.76E(4)(a) · s.21(8) · s.43(7)", post=flag())),
        tr(td("Your business partner, your landlord, a customer, or the press, while the matter is not public", "在事件尚未公開時，告訴你的業務夥伴、業主、客戶或傳媒"),
           f'<td class="verdict">{NO}</td>', td("None of the four conditions fits, so you need the Commissioner's consent, which he may give on conditions", "不符合四項條件中任何一項，故須取得關長同意；關長給予同意時可附加條件", "s.76E(2)–(3), (5)", post=flag())),
    ], minw=720)
    + numreq([
        (("level 4", "第4級"),
         ("Keep information obtained through a requirement or a disciplinary notice to yourself", "對經由要求或紀律通知獲得的資料保密"),
         ("From the moment a section 9 or 12 requirement is imposed on you, or a section 22 or 44 notice is given", "自第9或12條的要求施加於你，或第22或44條的通知發出之時起"),
         ("A fine at level 4 on conviction", "一經定罪，可處第4級罰款"),
         "s.76E(6)"),
        (("$1,000,000 + 2 years", "罰款$1,000,000及監禁2年"),
         ("Anyone you lawfully pass it to, with the Commissioner's consent or for professional advice, proceedings you are a party to, or a court order or Hong Kong law (a specified recipient), must not pass it on unless the Commissioner consents, the information is already public, it is to seek professional advice, it is in connection with proceedings they are a party to, or a court order or Hong Kong law requires it. Someone you tell only information that is already lawfully public is not bound", "你經關長同意，或為徵詢專業意見、在你身為一方的法律程序中，或按照法院命令或香港法律而向其披露資料的人（指明收取人），不得向另一人披露該資料，除非關長同意，或該資料是公眾已可得到的資料，或為徵詢專業意見，或在與其身為一方的法律程序相關的情況下披露，或按照法院命令或香港法律披露。如你披露的只是已因第76B條沒有禁止的披露而可供公眾取得的資料，收取人不受此約束"),
         ("Including your own professional adviser, and anyone who gets it from them", "包括你的專業顧問，以及從其處取得資料的任何人"),
         ("$1,000,000 and 2 years on indictment; level 6 and 6 months summarily", "公訴程序：罰款$1,000,000及監禁2年；簡易程序：第6級罰款及監禁6個月"),
         "s.76F(1), (3)–(4), (7)–(8)"),
    ])
    + traps(
        trap(("Public, but lawfully public", "公開，但須是合法公開"),
             ("The condition is not simply that the information is out there. It must have become public through a disclosure section 76B does not forbid. A leak in breach of section 76B, for example by a public officer employed in the Customs and Excise Department or another specified person, does not release you.",
              "條件並非只要資料已流出即可，而是必須經由第76B條沒有禁止的披露而公開。違反第76B條的洩露（例如由受僱於香港海關的公職人員或其他指明人士洩露）並不能解除你的責任。"),
             "s.76E(4)(a)"),
    ))

# ---------------------------------------------------------------- C. the gateways
OK = '<td class="verdict ctr">✓</td>'
NA = '<td class="verdict ctr faint">—</td>'


def grow(en, tc, cols, cite, post=''):
    return '<tr>' + td(en, tc, cite, post=post) + ''.join(OK if c else NA for c in cols) + '</tr>'


C_ = sec('gateways', ["s.76C", "s.76D", "s.76E(4)", "s.76G"],
         ("When disclosure is allowed, side by side", "准許披露的情況一併比較"),
    P("A tick means that permitted disclosure is open to that holder of the information. The Commissioner is also a specified person, so every tick in the first column is open to him as well.",
      "剔號表示該項獲准許的披露對該資料持有人開放。關長本身亦屬指明人士，故第一欄的每個剔號對他同樣適用。")
    + table([th("Permitted disclosure", "獲准許的披露"), th("Any specified person", "任何指明人士"), th("The Commissioner, as relevant authority", "關長（以有關當局身分）"), th("You, the licensee", "你（持牌人）")], [
        grow("In performing a function, or carrying the Ordinance into effect", "在執行職能或施行本條例的過程中", (1, 1, 0), "s.76C(1)(a)"),
        grow("Information already public (for you, only if it became public through a disclosure section 76B does not forbid)", "公眾已可得到的資料（就你而言，須是因第76B條沒有禁止的披露而可供公眾取得）", (1, 1, 1), "s.76C(1)(b) · s.76E(4)(a)", post=flag()),
        grow("For criminal proceedings, or an investigation, in Hong Kong", "為在香港進行的刑事法律程序或調查", (1, 1, 0), "s.76C(1)(c)–(d)"),
        grow("For professional advice", "為徵詢專業意見", (1, 1, 1), "s.76C(1)(e) · s.76E(4)(b)"),
        grow("In proceedings the holder is a party to", "在持有人身為一方的法律程序中", (1, 1, 1), "s.76C(1)(f) · s.76E(4)(c)"),
        grow("By court order, or as Hong Kong law requires", "按法院命令或香港法律規定", (1, 1, 1), "s.76C(1)(g) · s.76E(4)(d)"),
        grow("With the Commissioner's consent, on any conditions he sets", "經關長同意，並遵守其所訂條件", (0, 0, 1), "s.76E(2)(a), (3)(a), (5)"),
        grow("In a summary that identifies no one", "以無法識別任何人的撮要形式", (0, 1, 0), "s.76D(1)(a)"),
        grow("With the consent of the person it came from, and of anyone it is about", "經提供資料的人及資料所關乎的人同意", (0, 1, 0), "s.76D(1)(f)"),
        grow("To a liquidator, the Review Tribunal, or the Securities and Futures Appeals Tribunal", "向清盤人、覆核審裁處或證券及期貨事務上訴審裁處", (0, 1, 0), "s.76D(1)(b)–(d)"),
        grow("To eighteen listed officials and bodies, among them the Chief Executive, the Financial Secretary, the other financial regulators and the Commissioner of the Independent Commission Against Corruption, if desirable in the public interest and the recipient needs it", "向十八個指明的人員及機構（包括行政長官、財政司司長、其他金融監管機構及廉政專員），但須顧及公眾利益並屬可取，而接收者亦有需要", (0, 1, 0), "s.76D(1)(g), (2)"),
        grow("Inspection or investigation material, to the Secretary for Justice, the Commissioner of Police, the Commissioner of the Independent Commission Against Corruption or the Review Tribunal", "視察或調查所得資料，向律政司司長、警務處處長、廉政專員或覆核審裁處", (0, 1, 0), "s.76D(1)(h)"),
        grow("To an overseas regulator bound by adequate secrecy provisions, on the same public-interest test", "向受充分保密條文規限的香港以外監管機構，並須符合同樣的公眾利益準則", (0, 1, 0), "s.76D(1)(i), (2)"),
    ], note=B("Part 6A does not override the disclosure rules in the Banking, Insurance, Payment Systems and Stored Value Facilities, and Securities and Futures Ordinances, or in any other Ordinance governing a financial regulator.",
             "第6A部並不損害《銀行業條例》、《保險業條例》、《支付系統及儲值支付工具條例》、《證券及期貨條例》，或管限金融監管者的任何其他條例中關於披露資料的條文。") + ' ' + cite_html("s.76G"), minw=760, cls='gw')
    + traps(
        trap(("Two permitted disclosures carry a public-interest test", "兩類獲准許的披露須符合公眾利益準則"),
             ("Passing information to the listed officials and bodies, or to an overseas regulator, is allowed only if the Commissioner is satisfied it is desirable or expedient, having regard to the public interest and the recipient's need for it. The other permitted disclosures have no such test.",
              "向指明人員及機構或香港以外監管機構披露資料，只有在關長經顧及公眾利益及接收者的需要，信納披露屬可取或合宜時，方可進行。其他獲准許的披露並無此準則。"),
             "s.76D(2)"),
    ))

P6A_NAV = [('who', 'Two duties of secrecy', '兩項保密責任'), ('you', 'Who you may tell', '你可以告訴誰'),
           ('gateways', 'Permitted disclosures', '獲准許的披露')]
P6A_BODY = A + B_ + C_
