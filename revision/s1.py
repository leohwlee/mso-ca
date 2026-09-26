# AMLO Schedule 1: interpretation. What counts as a money service, ML and TF,
# institutions and their regulators, and where the other definitions live.
from ui import *

PT1 = ("Sch. 1 Pt 1", "附表1第1部")
PT2 = ("Sch. 1 Pt 2", "附表1第2部")


def top_align(*rows):
    """place() centres nodes in a row; top-align them so sibling arrows are the same length."""
    for row in rows:
        t = min(n.y for n in row)
        for n in row:
            n.y = t


def set_tc_lines(n, lines):
    """Break a Chinese text at phrase boundaries instead of mid-word (Node or Card body)."""
    if isinstance(n, Card):
        n.seg['tc'] = [x for x in n.seg['tc'] if 't-b' in x[1]] + [(l, 't', n.size) for l in lines]
        n.seg['both'] = n.seg['en'] + n.seg['tc']
        n.h = sum(sz * LH for _, _, sz in n.seg[lay()]) + 16 + (CS * LH if n.cite else 0)
    else:
        n.v['tc'] = list(lines)
        n.v['both'] = n.v['en'] + n.v['tc']
        n.h = need_h(n.v, n.size, n.cite) + (6 if n.shape == 'hex' else 0)


def fig_service():
    W = 1000
    HK = "Hong Kong"
    START = Card(290, 420, (f"A service operated in {HK} as a business", "在香港作為業務經營的服務"),
                 ("Both definitions require this before anything else", "兩項定義都先要求符合這一點"), cite=PT1)
    Q1 = Node(330, 340, ("What does the service do?", "該服務做甚麼？"), None, shape='hex')
    MCD = Card(10, 400, ("Exchanging currencies", "兌換貨幣"),
               ("Currency includes a cheque and a traveller's cheque", "貨幣包括支票及旅行支票"), cite=PT1)
    NOT = Card(425, 150, ("Neither", "兩者皆不是"), ("not a money service", "不屬金錢服務"), 'ok', answer=True)
    RSD = Card(590, 400, ("Moving money across the border", "跨境轉移金錢"),
               (f"Sending money out of {HK}, or receiving it from outside, or arranging either; or arranging for money to be received outside {HK}",
                "把金錢送往香港以外地方或從香港以外地方收取，或作出上述安排；或安排在香港以外地方收取金錢"), cite=PT1)
    Q2 = Node(10, 400, ("The hotel exception? Run by the person managing a hotel, on its premises, mainly for guests, and only buying non-Hong Kong currencies for Hong Kong currency",
                        "酒店例外？由管理酒店的人在酒店處所內經營、主要為方便住客，且只以港元購入非港元貨幣"), PT1, shape='hex')
    Q4 = Node(590, 400, ("Do you only provide financial institutions with a message system or other support system for transmitting funds?",
                         "你是否只為金融機構提供資金傳送的信息系統或其他支援系統？"), ("s.3 Sch. 1 Pt 1", "附表1第1部第3條"), shape='hex')
    set_tc_lines(RSD, ["把金錢送往香港以外地方或從香港以外地方收取，", "或作出上述安排；或安排在香港以外地方收取金錢"])
    set_tc_lines(Q2, ["酒店例外？由管理酒店的人在酒店處所內經營、", "主要為方便住客，且只以港元購入非港元貨幣"])
    set_tc_lines(Q4, ["你是否只為金融機構提供資金傳送的信息系統", "或其他支援系統？"])
    LIC = ("Licence needed unless Part 5 does not apply to you", "須領牌，除非第5部不適用於你")
    HOK = Card(10, 190, ("Not a money changing service", "不屬貨幣兌換服務"), None, 'ok', answer=True)
    MC = Card(215, 250, ("A money changing service", "屬貨幣兌換服務"), LIC, 'must', "s.29 · s.25", answer=True)
    ROK = Card(535, 190, ("Not operating a remittance service", "不被視為經營匯款服務"), None, 'ok', answer=True)
    RS = Card(740, 250, ("A remittance service", "屬匯款服務"), LIC, 'must', "s.29 · s.25", answer=True)
    rows = [([START], 30), ([Q1], 56), ([MCD, NOT, RSD], 32), ([Q2, Q4], 56), ([HOK, MC, ROK, RS], 0)]
    H = place(rows)
    top_align([MCD, NOT, RSD], [Q2, Q4], [HOK, MC, ROK, RS])
    b = [n.render() for n in (START, Q1, MCD, NOT, RSD, Q2, Q4, HOK, MC, ROK, RS)]
    m = 's1s'
    b.append(edge([START.bottom, Q1.top], mid=m))
    jy = Q1.bottom[1] + 26
    # a shared stem is drawn once, then each branch starts at the junction
    b.append(edge([Q1.bottom, (Q1.cx, jy)], marker=False, mid=m))
    b.append(edge([(Q1.cx, jy), (MCD.cx, jy), MCD.top], mid=m))
    b.append(edge([(Q1.cx, jy), (RSD.cx, jy), RSD.top], mid=m))
    b.append(edge([(Q1.cx, jy), NOT.top], mid=m))
    b.append(edge([MCD.bottom, Q2.top], mid=m))
    b.append(edge([RSD.bottom, Q4.top], mid=m))
    fy2 = Q2.bottom[1] + 24
    fy4 = Q4.bottom[1] + 24
    b.append(edge([Q2.bottom, (Q2.cx, fy2)], marker=False, mid=m))
    b.append(edge([Q4.bottom, (Q4.cx, fy4)], marker=False, mid=m))
    b.append(edge([(Q2.cx, fy2), (HOK.cx, fy2), HOK.top], ("yes", "是"), HOK.cx + 8, HOK.y - 8, 'start', mid=m))
    b.append(edge([(Q2.cx, fy2), (MC.cx, fy2), MC.top], ("no", "否"), MC.cx + 8, MC.y - 8, 'start', mid=m))
    b.append(edge([(Q4.cx, fy4), (ROK.cx, fy4), ROK.top], ("yes", "是"), ROK.cx + 8, ROK.y - 8, 'start', mid=m))
    b.append(edge([(Q4.cx, fy4), (RS.cx, fy4), RS.top], ("no", "否"), RS.cx + 8, RS.y - 8, 'start', mid=m))
    aria = ("Is it a money service? A service operated in Hong Kong as a business that exchanges currencies, cheques and traveller's cheques included, is a money changing service unless the hotel exception applies. One that sends money out of Hong Kong, receives it from outside, arranges either, or arranges for money to be received outside Hong Kong is a remittance service, unless the person only provides financial institutions with a message or support system for transmitting funds. Anything else is not a money service. A money service needs a licence unless Part 5 does not apply.",
            "是否屬金錢服務？在香港作為業務經營、兌換貨幣（包括支票及旅行支票）的服務屬貨幣兌換服務，除非符合酒店例外。把金錢送往香港以外地方、從香港以外地方收取、作出上述安排，或安排在香港以外地方收取金錢的服務屬匯款服務，除非該人只為金融機構提供資金傳送的信息或支援系統。其他服務不屬金錢服務。金錢服務須領牌，除非第5部不適用。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


SKEY = legend([('hex', ("a question you answer", "你須回答的問題")), ('', ("what the definition covers", "定義涵蓋的範圍")),
               ('ok', ("outside the definition", "不在定義之內")), ('must', ("a money service: needs a licence", "屬金錢服務：須領牌"))])

A = sec('service', [("Schedule 1", "附表1"), ("Part 1", "第1部"), ("money service", "金錢服務")],
        ("Is it a money service?", "是否屬金錢服務？"),
    P("Start at the top and answer the questions in the hexagons. The two red boxes at the bottom are the only two kinds of money service there are; everything else is outside the money service licensing regime in Part 5.",
      "由頂部開始，回答六邊形內的問題。底部兩個紅色方格是僅有的兩種金錢服務；其他一切都在第5部的金錢服務發牌制度之外。")
    + fig(fig_service, ("A money service is a money changing service or a remittance service, nothing more. Whether a particular operator then needs a licence is Part 5's question: banks never do, and some other licensed firms do not when the money service is only ancillary to their main business.",
                          "金錢服務只有貨幣兌換服務及匯款服務兩種。個別經營者是否須領牌，則屬第5部的問題：銀行一律毋須領牌；其他某些持牌機構的金錢服務如只屬其主要業務的附帶部分，亦毋須領牌。"), SKEY)
    + traps(
        trap(("Receiving money from abroad is remittance too", "從外地收款同樣屬匯款"),
             ("The definition runs both ways. Paying out in Hong Kong money that was sent from overseas is receiving money from a place outside Hong Kong, and arranging for someone overseas to be paid is also caught.",
              "定義是雙向的。在香港支付從外地匯來的款項，屬從香港以外地方收取金錢；安排在外地向某人付款，亦在涵蓋之列。"),
             PT1),
        trap(("The hotel exception is one-directional", "酒店例外只限單一方向"),
             ("It covers only transactions in which the hotel buys non-Hong Kong currencies in exchange for Hong Kong currency, in a service run on the hotel premises mainly for guests. A hotel desk that also sells non-Hong Kong currencies is outside the exception and is operating a money changing service.",
              "例外只涵蓋酒店以港元購入非港元貨幣的交易，而該服務須在酒店處所內經營、主要為方便入住該酒店的顧客。若酒店櫃位同時出售非港元貨幣，即不在例外之內，屬經營貨幣兌換服務。"),
             PT1),
        trap(("A traveller's cheque is currency", "旅行支票屬貨幣"),
             ("Because currency includes a cheque and a traveller's cheque, exchanging them is money changing, and money means money in whatever form or currency.",
              "由於貨幣包括支票及旅行支票，兌換這些票據即屬貨幣兌換；而金錢指屬任何形式或貨幣的金錢。"),
             PT1),
    ))

# ---------------------------------------------------------------- B. ML and TF
B_ = sec('mltf', [("Part 1", "第1部"), ("ML and TF", "洗錢及恐怖分子資金籌集")],
         ("Money laundering and terrorist financing, as defined", "條例對洗錢及恐怖分子資金籌集的定義"),
    P("Read each row across. The two definitions differ most on the mental element and on whether anything must actually happen to the money.",
      "逐行橫向閱讀。兩項定義最大的分別，在於犯罪意圖，以及款項是否須實際被使用。")
    + table([th("", ""), th("Money laundering", "洗錢"), th("Terrorist financing", "恐怖分子資金籌集")], [
        tr(rh("What is done", "作出的行為"),
           td("An act", "行為"),
           td("Providing or collecting property; making property or financial services available to or for a person; collecting property or soliciting financial services for a person's benefit", "提供或籌集財產；向某人或為某人的利益提供財產或金融服務；為某人的利益籌集財產或尋求金融服務")),
        tr(rh("The mental element", "犯罪意圖"),
           td("<b>Intended</b> to make the property not appear to be, or represent, the proceeds", "<b>意圖</b>使財產看似並非該等收益或看似不代表該等收益"),
           td("For the first limb, <b>intending or knowing</b> the property will be used for terrorist acts. For the other two, <b>knowing or being reckless</b> as to whether the person is a terrorist or terrorist associate", "第一項：<b>懷有意圖或知道</b>財產將用於恐怖主義行為。其餘兩項：<b>知道或罔顧</b>某人是否恐怖分子或與恐怖分子有聯繫者", post=flag())),
        tr(rh("Whose property", "涉及甚麼財產"),
           td("Proceeds of an indictable offence in Hong Kong, or of conduct elsewhere that would be one here; or property representing them, directly or indirectly, in whole or in part", "干犯香港可公訴罪行，或在其他地方作出假使在香港發生即屬可公訴罪行的作為所得的收益；或全部或部分、直接或間接代表該等收益的財產"),
           td("Any property, by any means, directly or indirectly", "任何財產，以任何方法，直接或間接")),
        tr(rh("Must it be used?", "財產是否須被實際使用？"),
           td("—", "—"),
           td("<b>No.</b> The first limb applies whether or not the property is actually used", "<b>否。</b>不論財產實際上有否被如此使用，第一項均適用", post=flag())),
        tr(rh("Borrowed words", "借用的詞語"),
           td("Property is defined in Schedule 1 itself, and covers money, goods, choses in action and land anywhere", "財產在附表1界定，涵蓋位於任何地方的金錢、貨品、據法權產及土地"),
           td("Terrorist, terrorist act and terrorist associate take their meaning from the United Nations (Anti-Terrorism Measures) Ordinance", "恐怖分子、恐怖主義行為及與恐怖分子有聯繫者的涵義，取自《聯合國（反恐怖主義措施）條例》")),
    ], minw=760, cls='cmp')
    + traps(
        trap(("Foreign crime counts", "外地罪行同樣計算"),
             ("The laundered proceeds need not come from a Hong Kong offence. Conduct abroad that would be an indictable offence had it occurred in Hong Kong is enough.",
              "被清洗的收益不一定來自香港罪行。在外地作出、假使在香港發生即屬可公訴罪行的作為，已經足夠。"),
             PT1),
    ))

# ---------------------------------------------------------------- C. institutions and regulators
FI = ("Financial institution", "金融機構")
DN = ("DNFBP", "指定非金融業人士")
C_ = sec('bodies', [("Part 2", "第2部"), ("who regulates whom", "誰監管誰")],
         ("Financial institutions, DNFBPs, and who supervises each", "金融機構、指定非金融業人士，以及各自的監管者"),
    P("Schedule 2 duties land on financial institutions (s.5) and, under s.5A, on DNFBPs too. Each is policed by its relevant authority or, for accountants, estate agents and lawyers, by its regulatory body. Find the person on the left; the middle column says which list the Ordinance puts it on. The shaded row is you.",
      "附表2的責任落在金融機構身上（第5條），亦按第5A條適用於指定非金融業人士；各自由其有關當局（或就會計專業人士、地產代理及法律專業人士而言，由其監管機構）監督。在左邊找出有關人士；中間一欄說明條例把它列入哪一類。有底色的一行就是你。")
    + table([th("The person", "有關人士"), th("Which list", "屬哪一類"), th("Who supervises it", "由誰監管")], [
        tr(td("Authorized institution (a bank), SVF licensee, stablecoin licensee", "認可機構（銀行）、工具持牌人、穩定幣持牌人"), td(*FI), td("The Monetary Authority", "金融管理專員")),
        tr(td("Licensed corporation; licensed virtual asset service provider", "持牌法團；持牌虛擬資產服務提供者"),
           td("Financial institution (for the VAS provider, subject to s.20A)", "金融機構（持牌虛擬資產服務提供者除第20A條另有規定外屬金融機構）", "s.20A"), td("The Securities and Futures Commission", "證監會")),
        tr(td("An associated entity of a licensed virtual asset service provider", "持牌虛擬資產服務提供者的有聯繫實體"),
           td("Neither: not on the financial institution list", "兩者皆不是：不在金融機構名單之內", post=flag()), td("The Securities and Futures Commission", "證監會")),
        tr(td("Authorized insurer, licensed individual insurance agent, licensed insurance agency, licensed insurance broker company", "獲授權保險人、持牌個人保險代理、持牌保險代理機構、持牌保險經紀公司"), td(*FI), td("The Insurance Authority", "保監局")),
        tr(td("<b>Licensed money service operator</b>", "<b>持牌金錢服務經營者</b>"), td(*FI), td("<b>The Commissioner</b>", "<b>關長</b>"), cls='you'),
        tr(td("The <b>Postmaster General</b>", "<b>郵政署署長</b>"), td(*FI), td("The <b>Commissioner</b>", "<b>關長</b>", post=flag())),
        tr(td("TCSP licensee", "信託或公司服務持牌人"), td(*DN), td("The Registrar of Companies", "公司註冊處處長")),
        tr(td("Category B PMS registrant (precious metals and stones)", "貴金屬及寶石B類註冊人"), td(*DN), td("The Commissioner", "關長")),
        tr(td("Category A registrant under Part 5C (precious metals and stones)", "第5C部所指的A類註冊人（貴金屬及寶石）"),
           td("Neither: not a financial institution and not a DNFBP", "兩者皆不是：既非金融機構，亦非指定非金融業人士", post=flag()), td("The Commissioner", "關長")),
        tr(td("Accounting professional, estate agent, legal professional", "會計專業人士、地產代理、法律專業人士"), td(*DN),
           td("Not a relevant authority but a regulatory body: the AFRC (or the HKICPA for some purposes), the Estate Agents Authority, the Law Society", "不是有關當局，而是監管機構：會財局（在某些情況下為香港會計師公會）、地產代理監管局、律師會")),
    ], note=B("<b>The Commissioner</b> in the Ordinance is not one person: it means the Commissioner of Customs and Excise, any Deputy or Assistant Commissioner, or anyone he has delegated a function to under section 26. <b>DNFBP</b> stands for the designated non-financial businesses and professions described in the Financial Action Task Force's Recommendations, and the Ordinance's list of DNFBPs has exactly five entries, all shown above.",
             "條例中的<b>關長</b>並非只指一人：它指海關關長、任何海關副關長或助理關長，或獲海關關長根據第26條轉授職能的人。<b>指定非金融業人士</b>指財務行動特別組織的建議中所述的指定非金融企業及行業人士，條例的指定非金融業人士名單只有五類，均列於上表。") + ' ' + cite_html(PT2), minw=820)
    + traps(
        trap(("Customs has three constituencies, not one", "海關監管三類對象，而非一類"),
             ("The Commissioner is relevant authority for licensed money service operators, for the Postmaster General, and for precious metals and stones registrants. A question that pairs the Postmaster General with the Monetary Authority is wrong.",
              "關長是持牌金錢服務經營者、郵政署署長，以及貴金屬及寶石註冊人的有關當局。把郵政署署長配對金融管理專員的選項是錯的。"),
             PT2),
        trap(("Financial institution or DNFBP", "金融機構還是指定非金融業人士"), None, PT2,
             vs=[(("Financial institution", "金融機構"), ("Banks, SVF and stablecoin licensees, licensed corporations, licensed VAS providers, authorized insurers and the licensed insurance agents, agencies and brokers, <b>licensed money service operators</b> and the <b>Postmaster General</b>.", "認可機構、工具持牌人及穩定幣持牌人、持牌法團、持牌虛擬資產服務提供者、獲授權保險人及持牌保險代理、代理機構及經紀公司、<b>持牌金錢服務經營者</b>及<b>郵政署署長</b>。")),
                 (("DNFBP: a closed list of five", "指定非金融業人士：只有五類"), ("Accounting professional, estate agent, legal professional, TCSP licensee, <b>Category B</b> PMS registrant. A Category A registrant is on neither list.", "會計專業人士、地產代理、法律專業人士、信託或公司服務持牌人、貴金屬及寶石<b>B類</b>註冊人。A類註冊人不在任何一份名單之內。"))]),
        trap(("Part 2 of Schedule 1 moves; Part 1 does not", "附表1第2部可變；第1部不可變"),
             ("The list of financial institutions and relevant authorities sits in Part 2, which the Secretary can amend by notice in the Gazette. The core definitions in Part 1, money service among them, can only be changed by an amending Ordinance.",
              "金融機構及有關當局的名單載於第2部，局長可藉憲報公告修訂。第1部的核心定義（包括金錢服務）只可由修訂條例修改。"),
             "s.2(2)"),
    ))

# ---------------------------------------------------------------- D. words that decide a case
D_ = sec('words', [("Parts 1 and 2", "第1及2部"), ("key words", "關鍵詞語")],
         ("Small words that decide a question", "決定答案的細小詞語"),
    P("Each of these is a short definition with a consequence somewhere else in the Ordinance. The right-hand column tells you where it bites.",
      "以下每項都是簡短的定義，卻在條例其他地方產生影響。右欄說明影響在哪裏。")
    + table([th("Word", "詞語"), th("What it means", "涵義"), th("Where it bites", "在哪裏產生影響")], [
        tr(rh("Commissioner", "關長", PT2), td("The Commissioner of Customs and Excise, a Deputy or Assistant Commissioner, or a delegate under section 26", "海關關長、海關副關長或助理關長，或根據第26條獲轉授職能的人"),
           td("Any power given to the Commissioner can be used by any of them, except where a section names the Commissioner of Customs and Excise himself, as the power to make Part 5 regulations does", "賦予關長的任何權力均可由上述任何一人行使；除非條文指明由海關關長本人行使，例如訂立第5部規例的權力", "s.51 · s.26(2)", post=flag())),
        tr(rh("Customer", "客戶", PT2), td("Includes a client", "包括當事人"), td("Every CDD duty in Schedule 2 that speaks of a customer", "附表2中每項提及客戶的盡職審查責任")),
        tr(rh("Business day", "營業日", PT2), td("Any day except a public holiday, a gale warning day or a black rainstorm warning day", "公眾假日、烈風警告日或黑色暴雨警告日以外的任何日子"),
           td("The 3 business days within which full originator information for a domestic wire transfer must be supplied on request", "應要求提供本地電傳轉帳完整匯款人資料的3個營業日限期", "s.12(6) Sch. 2", post=flag())),
        tr(rh("Money, currency", "金錢、貨幣", PT1), td("Money in whatever form or currency; currency includes a cheque and a traveller's cheque", "屬任何形式或貨幣的金錢；貨幣包括支票及旅行支票"), td("What counts as a money service", "何謂金錢服務")),
        tr(rh("Property", "財產", PT1), td("Money, goods, choses in action and land, anywhere, and every interest arising out of them", "位於任何地方的金錢、貨品、據法權產及土地，以及由此產生的各類權益"), td("The money laundering and terrorist financing definitions", "洗錢及恐怖分子資金籌集的定義")),
        tr(rh("Corporation", "法團", PT2), td("A company under the Companies Ordinance, or any other body corporate incorporated in Hong Kong or elsewhere", "《公司條例》所界定的公司，或在香港或其他地方成立為法團的其他法人團體"),
           td("For a corporate applicant, each director and any ultimate owner must be fit and proper to be associated with the business of operating a money service. Where a person being assessed is itself a corporation, the Commissioner <b>must</b> have regard to whether it is in liquidation, is the subject of a winding up order, or has a receiver appointed. The F&amp;P Guideline also covers the applicant itself, and asks whether a corporate applicant is being wound up or has a receiver appointed",
              "法團申請人的每名董事均須是與經營金錢服務有聯繫的適當人選；任何最終擁有人則須是與經營金錢服務業務有聯繫的適當人選。如接受評估的人本身屬法團，關長<b>須</b>顧及該人是否正在清盤當中，或是否任何清盤令的標的，或是否有接管人已就該人而獲委任。《有關適當人選準則的指引》亦同時適用於申請人本身，並考慮屬法團的申請人是否在清盤中，或是否有接管人已獲委任",
              ("s.30(3)(a)(iii) · s.30(4)(e) · F&P Guideline ¶4, ¶5(c)", "第30(3)(a)(iii)條 · 第30(4)(e)條 · 《適當人選指引》第4段、第5(c)段"), post=flag())),
        tr(rh("Director", "董事", ("s.24", "第24條")), td("For Part 5, director <i>includes</i> any person occupying the position of director, by whatever name called. Schedule 1 Part 2 has the general definition; section 24 adds this inclusive wording for Part 5 rather than giving a closed definition", "就第5部而言，董事包括任何擔任董事職位的人，不論職稱為何。附表1第2部載有一般定義；第24條為第5部加上這項「包括」式的定義，而非一個封閉的定義", post=flag()),
           td("Who must be fit and proper, and who needs the Commissioner's written approval before becoming a director of a corporate licensee", "誰須是適當人選，以及誰須先獲關長書面批准，方可成為屬法團的持牌人的董事", "s.30 · s.35")),
        tr(rh("Record, document", "紀錄、文件", PT1), td("As defined in the Securities and Futures Ordinance", "具有《證券及期貨條例》給予的涵義"), td("What an authorized person or investigator can require you to produce", "獲授權人或調查員可要求你交出甚麼")),
        tr(rh("Re-domiciled entity", "經遷冊實體", PT2), td("A company re-domiciled into Hong Kong and deregistered in its old home, added in 2025", "已遷冊至香港並在原註冊地撤銷註冊的公司，於2025年增補"), td("It is treated like a Hong Kong company for the overseas branch duty and for relying on related foreign institutions", "就海外分行的責任及依賴相關外地機構而言，它被視為香港公司", "s.18(7), 22(1) Sch. 2")),
    ], minw=820))

# ---------------------------------------------------------------- E. defined elsewhere
E_ = sec('elsewhere', [("look it up", "對照"), ("defined elsewhere", "在別處界定")],
         ("Defined somewhere other than Schedule 1", "不在附表1界定的詞語"),
    P("Not every defined term is in Schedule 1. Terms that only one Part or Schedule uses are defined where they are used. Find the term on the left.",
      "並非所有經界定的詞語都在附表1。只由某一部或某一附表使用的詞語，就在使用之處界定。在左邊找出詞語。")
    + table([th("The term", "詞語"), th("Defined in", "界定於")], [
        tr(td("Beneficial owner, business relationship, occasional transaction, politically exposed person, former politically exposed person, equivalent jurisdiction, identification document, pre-existing customer, public body, recognized digital identification system",
              "實益擁有人、業務關係、非經常交易、政治人物、前政治人物、對等司法管轄區、識別文件、先前客戶、公共機構、認可數碼識別系統"),
           td("Schedule 2, section 1: the CDD definitions", "附表2第1條：盡職審查的定義", "s.1 Sch. 2")),
        tr(td("Wire transfer; its originator and a domestic wire transfer; remittance transaction; virtual asset transfer", "電傳轉帳；其匯款人及本地電傳轉帳；匯款交易；虛擬資產轉帳"),
           td("Schedule 2, where each special requirement is set out", "附表2各項特別規定所在之處", "s.1(4), 12(11), 13(3), 13A(1) Sch. 2")),
        tr(td("Specified provision", "指明的條文"), td("Part 2, section 5", "第2部第5條", "s.5(11)")),
        tr(td("Authorized person, investigator, prescribed requirement", "獲授權人、調查員、訂明規定"), td("Part 3, section 8", "第3部第8條", "s.8")),
        tr(td("Licence, register, ultimate owner, authorized officer, and director as Part 5 uses it", "牌照、登記冊、最終擁有人、獲授權人員，以及第5部所用的董事"), td("Part 5, section 24", "第5部第24條", "s.24", post=flag())),
        tr(td("Specified decision, specified authority, parties, review", "指明決定、指明當局、各方、覆核"), td("Part 6, section 54", "第6部第54條", "s.54")),
        tr(td("Specified person", "指明人士"), td("Part 6A, section 76A", "第6A部第76A條", "s.76A")),
        tr(td("Chairperson, ordinary member, panel member", "主席、普通成員、委員"), td("Schedule 4, section 1", "附表4第1條", "s.1 Sch. 4")),
    ], minw=700)
    + traps(
        trap(("Ultimate owner is not beneficial owner", "最終擁有人不等於實益擁有人"), None, "s.24 · s.30(3) · s.36 · s.1 Sch. 2 · ¶4.4.1",
             vs=[(("Ultimate owner, Part 5", "最終擁有人（第5部）"), ("Whose ownership of <b>your business</b> makes them subject to the fit and proper test and to approval before they come in. For a corporation or partnership: an individual with more than 25% (of the share capital, the capital or profits, or the voting rights) or ultimate control over its management. For an individual: another individual who ultimately owns or controls the individual's money service business, or, if the individual is acting on behalf of another person, the other person.",
                                                                "因擁有<b>你的業務</b>而須接受適當人選測試，並須先獲批准方可加入的人。就法團或合夥而言：持有25%以上（已發行股本、資本或利潤，或投票權）或對其管理行使最終控制權的個人。就個人而言：最終擁有或控制該名個人的金錢服務業務的另一名個人；或（如首述個人是代表另一人行事）該另一人。")),
                 (("Beneficial owner, Schedule 2", "實益擁有人（附表2）"), ("The <b>natural person(s)</b> behind <b>your customer</b>, whom you must identify during CDD. The same 25% and control tests, plus a limb Part 5 lacks for corporations and partnerships: if the customer acts on behalf of another person, that person. For a trust: the settlor, the trustee, a protector or enforcer, beneficiaries, or a class of beneficiaries, entitled to a vested interest, and any individual with ultimate control over the trust.",
                                                                   "在盡職審查中須識別的、<b>你客戶</b>背後的<b>自然人</b>。採用相同的25%及控制權準則，另加第5部就法團及合夥所沒有的一項：如客戶是代表另一人行事，指該另一人。就信託而言：財產授予人、受託人、保護人或執行人、有權享有信託財產既得權益的受益人或某類別受益人，以及對該信託擁有最終控制權的個人。"))]),
    ))

S1_NAV = [('service', 'Is it a money service?', '是否屬金錢服務'), ('mltf', 'ML and TF', '洗錢與恐怖分子資金籌集'),
          ('bodies', 'Institutions and regulators', '機構與監管者'), ('words', 'Small words', '細小詞語'),
          ('elsewhere', 'Defined elsewhere', '在別處界定')]
S1_BODY = A + B_ + C_ + D_ + E_
