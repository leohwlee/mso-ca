# AML/CFT Guideline Chapter 1 (Overview): the general-knowledge module. What ML, TF
# and PF are, the three stages of laundering, the FATF, the six ordinances and the
# offences they create, and how to read the Guideline itself. The AMLO definitions of
# ML and TF, and the AMLO's own offences, stay on the Schedule 1 and Part 2 pages.
from ui import *
from g1_fig import (fig_stages, STAGES_KEY, fig_fatf, FATF_KEY, fig_offences, OFF_KEY, fig_status, STATUS_KEY)


def cc(*cs):
    """Join several citations into one."""
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


def vd(ch):
    return f'<td class="verdict">{ch}</td>'


GLOS = ("Glossary", "詞彙")
DTOS25 = ("DTROP, OSCO s.25", "《販毒（追討得益）條例》、《有組織及嚴重罪行條例》第25條")
DISC = ("DTROP, OSCO s.25A · UNATMO s.12, 14", "《販毒（追討得益）條例》、《有組織及嚴重罪行條例》第25A條 · 《聯合國（反恐怖主義措施）條例》第12、14條")
UNTF = ("UNATMO s.6, 7, 8, 8A, 13, 14", "《聯合國（反恐怖主義措施）條例》第6、7、8、8A、13、14條")
WMD4 = ("WMD(CPS)O s.4", "《大規模毀滅武器（提供服務的管制）條例》第4條")
CIRC = ("Circular 3 Jul 2026", "2026年7月3日通函")

# ---------------------------------------------------------------- 1. the three threats
A = sec('threats', ["¶1.9–1.12", GLOS, "¶6.1"],
        ("What you are guarding against: laundering, terrorist financing and proliferation financing",
         "你要防範的三種威脅：洗錢、恐怖分子資金籌集及擴散資金籌集"),
    P("Read the figure left to right: each box is one stage of money laundering in the Guideline's own words, and the red band underneath is what the Guideline asks of you at every stage. The table then sets the three threats side by side.",
      "由左至右閱讀下圖：每個方格是洗錢的一個階段，文字取自指引原文；下方紅色橫框是指引在每個階段對你的要求。其後的表格把三種威脅並列比較。")
    + fig(fig_stages, ("The names and descriptions are the Guideline's. The statutory definition of money laundering, and the three limbs of terrorist financing, are on the <a href=\"#s1-mltf\">Schedule 1 page</a>.",
                        "階段名稱及描述均取自指引。洗錢的法定定義及恐怖分子資金籌集的三個分項，見<a href=\"#s1-mltf\">附表1一頁</a>。"), STAGES_KEY)
    + table([th("", ""), th("Money laundering (ML)", "洗錢"), th("Terrorist financing (TF)", "恐怖分子資金籌集"),
             th("Proliferation financing (PF)", "擴散資金籌集")], [
        tr(rh("What it is", "是甚麼"),
           td("An act intended to make property that is the proceeds of an indictable offence not appear to be, or represent, such proceeds. The full definition is on the <a href=\"#s1-mltf\">Schedule 1 page</a>",
              "意圖使屬干犯可公訴罪行而獲取的收益的財產，看似並非該等收益、或看似不代表該等收益的行為。完整定義見<a href=\"#s1-mltf\">附表1一頁</a>", "¶1.9"),
           td("Providing or collecting property for terrorist acts; making property or financial (or related) services available to terrorists or terrorist associates; or collecting property or soliciting such services for their benefit. The three limbs, with their mental elements, are on the <a href=\"#s1-mltf\">Schedule 1 page</a>",
              "為恐怖主義行為提供或籌集財產；向恐怖分子或與恐怖分子有聯繫者提供財產或金融（或有關的）服務；或為他們的利益籌集財產或尋求該等服務。三個分項及其心態要求見<a href=\"#s1-mltf\">附表1一頁</a>", "¶1.11"),
           td("The financing of proliferation of weapons of mass destruction", "為大規模毀滅武器擴散籌集資金", GLOS)),
        tr(rh("What decides it", "關鍵在於"),
           td("The <b>source</b> of the property: the handling of criminal proceeds", "財產的<b>來源</b>：處理犯罪得益", "¶6.1"),
           td("The <b>destination or use</b> of the property, which may have come from legitimate sources", "財產的<b>終點或用途</b>；財產可以是從合法來源取得的", "¶6.1", post=flag()),
           td("The source-or-destination contrast in ¶6.1 is drawn for ML and TF only. For PF, section 4 of WMD(CPS)O prohibits providing services where you believe or suspect, on reasonable grounds, that they may be connected to PF",
              "第6.1段只就洗錢及恐怖分子資金籌集比較財產的來源與終點。就擴散資金籌集而言，《大規模毀滅武器（提供服務的管制）條例》第4條禁止任何人在基於合理理由相信或懷疑有關服務與擴散資金籌集有關時提供該等服務", cc("¶6.1", "¶1.27"))),
        tr(rh("Is laundering involved?", "是否涉及清洗資金？"),
           td("By definition. Three common stages, frequently involving numerous transactions: the figure above", "按定義即是。有三個常見階段，經常涉及多宗交易：見上圖", "¶1.10"),
           td("Yes. Terrorists often need to hide their links to their funding, so they too must find ways to launder funds, whether the source is legitimate or illegitimate, to use them without attracting the authorities' attention",
              "是。恐怖分子往往需要隱藏他們與資金來源的連繫，因此同樣必須尋找清洗資金的途徑（不論來源是否合法），以便在不被當局發現的情況下使用", "¶1.12", post=flag()),
           td("Chapter 1 does not say", "第1章沒有說明", cls='faint')),
    ], note=B("Which ordinance covers which threat, and the offences each creates, are in the next two sections: <a href=\"#g1-laws\">six ordinances</a> and <a href=\"#g1-offences\">offences</a>.",
              "哪條條例處理哪種威脅，以及各條例訂立的罪行，見其後兩節：<a href=\"#g1-laws\">六條條例</a>及<a href=\"#g1-offences\">罪行</a>。"), minw=820, cls='cmp')
    + traps(
        trap(("Placement puts it in, layering hides it, integration brings it back", "存放是注入，分層交易是隱藏，整合是回流"),
             ("A question may swap the descriptions. Only placement is about cash proceeds going into the financial system. Disguising the source, subverting the audit trail and providing anonymity are layering. Apparent legitimacy, and proceeds returning to the general financial system, are integration.",
              "題目可能把描述互換。只有「存放」是把現金得益注入金融體系。隱藏款項來源、掩飾審計線索和隱藏擁有人的身分，屬「分層交易」。製造表面的合法性、令得益回流到一般金融體系，屬「整合」。"),
             "¶1.10"),
        trap(("Clean money can still finance terrorism", "合法的錢也可以用作資助恐怖分子"), None, cc("¶1.12", "¶6.1"),
             vs=[(("Money laundering", "洗錢"), ("Turns on where the property came from: it must be criminal proceeds.", "取決於財產從何而來：必須是犯罪得益。")),
                 (("Terrorist financing", "恐怖分子資金籌集"), ("Turns on the destination or use of the property. It may come from legitimate sources, and terrorists still launder it to avoid attention.", "取決於財產的終點或用途。財產可以是從合法來源取得的，恐怖分子仍會清洗資金以免引起注意。"))]),
    ))

# ---------------------------------------------------------------- 2. the FATF
B_ = sec('fatf', ["¶1.13", CIRC],
         ("Why Hong Kong's rules follow an international standard", "香港的規則為何依循國際標準"),
    P("Read the top row left to right: who the FATF is, what it sets and how it checks. The lower boxes are what follows, for Hong Kong on the left and for the jurisdictions the FATF names on the right.",
      "由左至右閱讀頂行：特別組織是誰、它訂立甚麼、如何監察。下方方格是隨之而來的結果：左邊關乎香港，右邊關乎特別組織點名的司法管轄區。")
    + fig(fig_fatf, ("The FATF Recommendations are published on the FATF's website. Many major economies are members, and the FATF has become a global network for international co-operation between member jurisdictions.",
                      "特別組織建議可在特別組織的網站查閱。很多大型經濟體系都已加入特別組織，形成國際合作的全球網絡，促進成員司法管轄區之間的交流。"), FATF_KEY)
    + traps(
        trap(("Obliged to implement the Recommendations; important to comply with the standards", "有責任實施建議；必須符合國際標準"), None, "¶1.13",
             vs=[(("Obliged", "有責任"), ("As a member of the FATF, Hong Kong is obliged to implement the latest FATF Recommendations.", "香港作為特別組織的成員，有責任實施最新的特別組織建議。")),
                 (("Important", "必須"), ("It is important that Hong Kong complies with the international AML/CFT standards to maintain its status as an international financial centre.",
                                        "香港必須符合國際打擊洗錢／恐怖分子資金籌集標準，以維持其國際金融中心的地位。"))]),
        trap(("Scrutiny from the FATF, counter-measures from others", "加強審查來自特別組織，針對措施來自其他各方"), None, "¶1.13",
             vs=[(("Enhanced scrutiny", "加強審查"), ("By the FATF itself, of the high-risk and other monitored jurisdictions it identifies.", "由特別組織本身，針對其識別的高度風險及其他受監察的司法管轄區。")),
                 (("Counter-measures", "針對措施"), ("By the FATF's members and the international community at large.", "由特別組織的成員及整個國際社會。"))]),
    ))

# ---------------------------------------------------------------- 3. the six ordinances
LAW_NOTE = B("The Guideline says it is very important that MSOs and their officers and staff fully understand their responsibilities under each of these laws. "
             "Convictions under several of these ordinances also count against fitness and properness: see the <a href=\"#p5-fitproper\">Part 5 page</a>.",
             "指引指出，金錢服務經營者及它們的主管人員和職員均須充分了解他們在這些法例之下的各種責任，這點至為重要。"
             "根據其中數條條例被定罪，亦會影響是否適當人選的判斷：見<a href=\"#p5-fitproper\">第5部一頁</a>。") + ' ' + cite_html(cc("¶1.14", "s.30(4)(a)"))

C_ = sec('laws', ["¶1.14–1.21", "¶1.26–1.27"],
         ("Six ordinances, and which one a question is about", "六條條例：題目問的是哪一條"),
    P("Each row is one of the six ordinances the Guideline names as Hong Kong's main laws on ML, TF, PF and financial sanctions. Start from the subject in the first column, then read across for the ordinance, its chapter number and what the Guideline says it does. The offences they create are in the next section.",
      "每一行是指引列為香港在洗錢、恐怖分子資金籌集、擴散資金籌集及金融制裁方面的六條主要法例之一。先看第一欄的主題，再橫向閱讀條例名稱、章號及指引所述的作用。這些條例訂立的罪行，見下一節。")
    + table([th("If the question is about", "如題目關於"), th("The ordinance", "條例"), th("Cap.", "章號"), th("What the Guideline says it does", "指引所述的作用")], [
        tr(rh("Your CDD and records, and the CCE supervising you", "你的盡職審查及紀錄，以及關長對你的監管"),
           td("Anti-Money Laundering and Counter-Terrorist Financing Ordinance (AMLO)", "《打擊洗錢及恐怖分子資金籌集條例》（打擊洗錢條例）"),
           td("615", "第615章", cls='pen'),
           td("Imposes CDD and record-keeping requirements on MSOs and gives the Commissioner powers to supervise compliance with them and with its other requirements. Section 23 of Schedule 2 adds all reasonable measures to ensure proper safeguards against contravening Parts 2 and 3 of the Schedule, and to mitigate ML/TF risks. Its offences and disciplinary penalties are on the <a href=\"#p2-chain\">Part 2 page</a>",
              "對金錢服務經營者施加客戶盡職審查及備存紀錄的規定，並賦予關長權力監督該等規定及條例其他規定的合規情況。附表2第23條另規定須採取所有合理措施，確保有適當的預防措施防止違反附表2第2及3部，並減低洗錢／恐怖分子資金籌集的風險。條例的罪行及紀律處分見<a href=\"#p2-chain\">第2部一頁</a>",
              "¶1.15–1.18")),
        tr(rh("Drug money", "販毒得益"),
           td("Drug Trafficking (Recovery of Proceeds) Ordinance (DTROP)", "《販毒（追討得益）條例》"),
           td("405", "第405章", cls='pen'),
           td("Investigating assets suspected to derive from drug trafficking; freezing assets on arrest; confiscating the proceeds of drug trafficking on conviction",
              "對涉嫌從販毒活動所得的資產進行調查；在逮捕涉嫌罪犯時將資產凍結；在定罪後沒收販毒得益", "¶1.19")),
        tr(rh("Proceeds of organised and serious crime", "有組織及嚴重罪行的得益"),
           td("Organized and Serious Crimes Ordinance (OSCO)", "《有組織及嚴重罪行條例》"),
           td("455", "第455章", cls='pen'),
           td("Among other things: (a) gives officers of the Hong Kong Police and the Customs and Excise Department powers to investigate organised crime and triad activities; (b) gives the courts jurisdiction to confiscate the proceeds of organised and serious crimes, and to issue restraint orders and charging orders over the property of a defendant of an offence specified in the OSCO; (c) creates an offence of money laundering in relation to the proceeds of indictable offences; (d) lets the courts, under appropriate circumstances, receive information about an offender and an offence, to decide whether a greater sentence is appropriate for an organised crime, triad-related or other serious offence",
              "除其他事項外：(a) 賦予香港警方及香港海關人員調查有組織罪行及三合會活動的權力；(b) 賦予法院司法管轄權，沒收來自有組織及嚴重罪行的得益，以及就被控觸犯該條例所指罪行的被告人的財產發出限制令及押記令；(c) 增訂一項有關來自可公訴罪行得益的洗錢罪行；(d) 容許法院在適當的情況下收取有關違法者及罪行的資料，以決定當罪行構成有組織／與三合會有關的罪行或其他嚴重罪行時，是否適宜作出更重的判刑",
              "¶1.20", post=flag())),
        tr(rh("Financing terrorism", "資助恐怖主義"),
           td("United Nations (Anti-Terrorism Measures) Ordinance (UNATMO)", "《聯合國（反恐怖主義措施）條例》"),
           td("575", "第575章", cls='pen'),
           td("Principally implements decisions in relevant United Nations Security Council Resolutions (UNSCRs) aimed at preventing the financing of terrorist acts and combating the threats posed by foreign terrorist fighters. Beyond the resolutions' mandatory elements, it also implements the more pressing elements of the FATF Recommendations specifically on TF. It permits terrorist property to be frozen and then forfeited",
              "旨在實施聯合國安全理事會（安理會）相關決議中關於防止向恐怖主義行為提供資金和減低外國恐怖主義戰鬥人員威脅的決定。除安理會決議中強制執行的措施外，亦實施特別組織建議中明確與恐怖分子資金籌集有關較具逼切性的部分。該條例容許將恐怖分子財產凍結，然後充公",
              "¶1.21, 1.23")),
        tr(rh("United Nations sanctions", "聯合國制裁"),
           td("United Nations Sanctions Ordinance (UNSO)", "《聯合國制裁條例》"),
           td("537", "第537章", cls='pen'),
           td("Provides for sanctions against persons and against places outside the People's Republic of China, arising from Chapter 7 of the Charter of the United Nations. Most UNSCRs are implemented in Hong Kong under it",
              "就《聯合國憲章》第七章所引起而對中華人民共和國以外地方施加制裁而訂定條文。在香港，大部分聯合國安理會決議均根據該條例實施",
              "¶1.26", post=flag())),
        tr(rh("Weapons of mass destruction", "大規模毀滅武器"),
           td("Weapons of Mass Destruction (Control of Provision of Services) Ordinance (WMD(CPS)O)", "《大規模毀滅武器（提供服務的管制）條例》"),
           td("526", "第526章", cls='pen'),
           td("Controls the provision of services that will or may assist the development, production, acquisition or stockpiling of weapons capable of causing mass destruction, or the means of delivering them. Section 4 is the prohibition, in the next section",
              "管制提供將會或可能協助發展、生產、取得或貯存可造成大規模毀滅的武器，或該等武器投射工具的服務。第4條的禁止規定見下一節", "¶1.27")),
    ], note=LAW_NOTE, minw=880)
    + traps(
        trap(("DTROP is drugs; OSCO is any indictable offence", "《販毒（追討得益）條例》針對販毒；《有組織及嚴重罪行條例》針對任何可公訴罪行"), None, cc("¶1.19–1.20", "¶1.22"),
             vs=[(("DTROP, Cap. 405", "《販毒（追討得益）條例》，第405章"), ("Proceeds of drug trafficking: investigation, freezing on arrest, confiscation on conviction.", "販毒得益：調查、逮捕時凍結、定罪後沒收。")),
                 (("OSCO, Cap. 455", "《有組織及嚴重罪行條例》，第455章"), ("Proceeds of indictable offences generally, plus investigation powers, restraint and charging orders, and heavier sentences for organised and serious crime.", "一般可公訴罪行的得益，另有調查權力、限制令及押記令，以及對有組織及嚴重罪行判處更重刑罰。"))]),
        trap(("UNATMO is about terrorism; UNSO carries most UN sanctions", "《聯合國（反恐怖主義措施）條例》關乎恐怖主義；大部分聯合國制裁經《聯合國制裁條例》實施"), None, cc("¶1.21", "¶1.26"),
             vs=[(("UNATMO, Cap. 575", "《聯合國（反恐怖主義措施）條例》，第575章"), ("Security Council decisions against financing terrorist acts and foreign terrorist fighters, and the pressing FATF TF Recommendations.", "安理會有關防止向恐怖主義行為提供資金及外國恐怖主義戰鬥人員的決定，以及特別組織較具逼切性的相關建議。")),
                 (("UNSO, Cap. 537", "《聯合國制裁條例》，第537章"), ("Sanctions arising from Chapter 7 of the UN Charter. Most Security Council resolutions are implemented under this one.", "因《聯合國憲章》第七章而施加的制裁。大部分安理會決議均根據此條例實施。"))]),
        trap(("526, 537, 575: three chapter numbers in a row", "526、537、575：三個相近的章號"),
             ("Weapons of mass destruction is Cap. 526, UN sanctions Cap. 537, anti-terrorism Cap. 575. The two crime-proceeds ordinances are DTROP Cap. 405 and OSCO Cap. 455, and the AMLO is Cap. 615.",
              "大規模毀滅武器為第526章，聯合國制裁為第537章，反恐怖主義措施為第575章。兩條關於犯罪得益的條例是《販毒（追討得益）條例》第405章及《有組織及嚴重罪行條例》第455章；打擊洗錢條例是第615章。"),
             "¶1.14"),
    ))

# ---------------------------------------------------------------- 4. the offences
D_ = sec('offences', ["¶1.22–1.25", "¶1.27", "¶1.16–1.17", "¶7.6", "¶7.25"],
         ("Crimes you or any of your staff can commit", "你或你任何一名職員都可能觸犯的罪行"),
    P("Start from the top box and follow each of the three things you might do. The black boxes are offences under DTROP, OSCO and UNATMO; each is committed by \"a person\", so they reach you and every member of your staff, not only the licensee. The dashed box at the foot, reached from the disclosure path, links to Chapter 7. The table after the figure has every penalty the Guideline gives for these crimes and for terrorist financing.",
      "由頂部方格開始，沿你可能採取的三種做法往下看。黑色方格是《販毒（追討得益）條例》、《有組織及嚴重罪行條例》及《聯合國（反恐怖主義措施）條例》下的罪行；條文針對的是「任何人」，因此適用於你及你的每一名職員，而不限於持牌人。底部的虛線方格由披露一路引出，連結至第7章。圖後的表格列出指引就這些罪行及恐怖分子資金籌集所載的每項刑罰。")
    + fig(fig_offences, ("The failure-to-disclose offence covers property that represents proceeds of, was used in connection with, or is intended to be used in connection with, drug trafficking or an indictable offence, and terrorist property. The dealing offence covers proceeds only.",
                          "未有披露的罪行涵蓋代表販毒或可公訴罪行的得益、曾在與其有關的情況下使用或擬如此使用的財產，以及恐怖分子財產。處理得益的罪行則只涵蓋得益。"), OFF_KEY)
    + numreq([
        (("14 years and $5,000,000", "監禁14年及罰款五百萬元"),
         ("Do not deal with property that represents anyone's proceeds of drug trafficking (DTROP) or of an indictable offence (OSCO)",
          "不可處理代表任何人的販毒得益（《販毒（追討得益）條例》）或可公訴罪行的得益（《有組織及嚴重罪行條例》）的財產"),
         ("You know, or have reasonable grounds to believe, that the property represents such proceeds", "你知道或有合理理由相信該財產代表該等得益"),
         ("The dealing offence: the highest penalty on conviction", "處理得益的罪行：定罪後的最高刑罰"),
         cc("¶1.22", DTOS25)),
        (("14 years and a fine", "監禁14年及罰款"),
         ("Do not provide or collect property for, or make any property or financial (or related) services available to, terrorists or terrorist associates",
          "不可向恐怖分子或與恐怖分子有聯繫者提供或籌集財產，或向他們提供任何財產或金融（或有關的）服務"),
         ("The property or services are for terrorists or terrorist associates. Chapter 1 states no mental element here; those in the definition of TF are on the <a href=\"#s1-mltf\">Schedule 1 page</a>",
          "有關財產或服務是為恐怖分子或與恐怖分子有聯繫者而提供或籌集。第1章在此沒有列明心態要求；恐怖分子資金籌集定義中的心態要求見<a href=\"#s1-mltf\">附表1一頁</a>"),
         ("The UNATMO offence: the highest penalty on conviction; the Guideline gives no fine amount", "《聯合國（反恐怖主義措施）條例》的罪行：定罪後的最高刑罰；指引沒有列明罰款金額"),
         cc("¶1.23", UNTF)),
        (("3 months and $50,000", "監禁3個月及罰款50,000元"),
         ("Disclose, as soon as it is reasonable, your knowledge or suspicion that property directly or indirectly represents anyone's proceeds of, was used in connection with, or is intended to be used in connection with, drug trafficking or an indictable offence, or is terrorist property",
          "如知悉或懷疑任何財產直接或間接代表任何人的販毒或可公訴罪行的得益、曾在與其有關的情況下使用、擬如此使用，或為恐怖分子財產，須在合理範圍內盡快作出披露"),
         ("You know or suspect", "你知悉或懷疑"),
         ("Failure to disclose: the maximum on conviction", "未有披露：定罪後的最高刑罰"),
         cc("¶1.24", DISC)),
        (("3 years and a fine", "監禁3年及罰款"),
         ("Do not disclose to any other person anything likely to prejudice an investigation that might follow the disclosure",
          "不可向其他人披露任何相當可能損害為跟進該披露而進行的調查的事宜"),
         ("You know or suspect that a disclosure has been made; the Guideline does not limit it to your own. Chapter 7 adds that it also covers a suspicion raised inside your business but not yet reported to the JFIU: see the <a href=\"#g7-duty\">Guideline Ch. 7 page</a>",
          "你知道或懷疑已曾作出披露；指引沒有限定須是你本人作出的披露。第7章另指出，已於你業務內部提出但尚未向財富情報組報告的懷疑亦包括在內，見<a href=\"#g7-duty\">指引第7章一頁</a>"),
         ("Tipping off: the maximum on conviction; the Guideline gives no fine amount", "通風報訊：定罪後的最高刑罰；指引沒有列明罰款金額"),
         cc("¶1.25", "¶7.6", DISC)),
    ], minw=860)
    + traps(
        trap(("Four offences, four different states of mind", "四項罪行，四種不同的心態要求"), None, cc("¶1.22", "¶1.24–1.25", "¶1.27", WMD4),
             vs=[(("Dealing", "處理得益"), ("Knowing, or having reasonable grounds to believe, that the property is proceeds.", "知道或有合理理由相信該財產是得益。")),
                 (("Failure to disclose", "未有披露"), ("Knowledge or suspicion that the property is proceeds or terrorist property.", "知悉或懷疑該財產是得益或恐怖分子財產。")),
                 (("Tipping off", "通風報訊"), ("Knowing or suspecting that a disclosure has been made.", "知道或懷疑已曾作出披露。")),
                 (("Providing services (PF)", "提供服務（擴散資金籌集）"), ("Believing or suspecting, on reasonable grounds, that the services may be connected to PF. Services are widely defined and include lending money or other financial assistance. Chapter 1 gives no penalty.",
                                                                      "基於合理理由相信或懷疑該等服務與擴散資金籌集有關。提供服務的定義廣泛，包括借出款項或以其他方式提供財政資助。指引第1章沒有列明刑罰。"))]),
        trap(("3 months or 3 years; a sum or just 'a fine'", "3個月還是3年；列明金額還是只寫「罰款」"), None, cc("¶1.22–1.25"),
             vs=[(("Stated in full", "列明金額"), ("Dealing: 14 years and $5 million. Failure to disclose: 3 months and $50,000.", "處理得益：監禁14年及罰款五百萬元。未有披露：監禁3個月及罰款50,000元。")),
                 (("Prison term and 'a fine'", "監禁及「罰款」"), ("The UNATMO terrorist financing offences: 14 years and a fine. Tipping off: 3 years and a fine.", "《聯合國（反恐怖主義措施）條例》的恐怖分子資金籌集罪行：監禁14年及罰款。通風報訊：監禁3年及罰款。"))]),
        trap(("These are not the AMLO's offences", "這些並非打擊洗錢條例的罪行"), None, cc("¶1.16–1.17", "¶1.22–1.25"),
             vs=[(("AMLO section 5", "打擊洗錢條例第5條"), ("The MSO contravening a specified provision, or an employee, a person employed to work for it or a person concerned in its management causing or permitting it to, knowingly or with intent to defraud (for the MSO, the CCE; for those people, the MSO or the CCE): up to 2 years (knowingly) or 7 years (intent to defraud), and $1 million. Details on the <a href=\"#p2-offences\">Part 2 page</a>.",
                                                       "金錢服務經營者違反指明的條文，或其僱員、受僱為其工作或關涉其管理的人致使或准許其違反，而屬明知或意圖詐騙（經營者：詐騙關長；上述人士：詐騙該經營者或關長）：最高監禁2年（明知）或7年（意圖詐騙），及罰款一百萬元。詳情見<a href=\"#p2-offences\">第2部一頁</a>。")),
                 (("DTROP, OSCO, UNATMO", "《販毒（追討得益）條例》、《有組織及嚴重罪行條例》、《聯合國（反恐怖主義措施）條例》"), ("Any person who deals with proceeds, fails to disclose, tips off, or finances terrorists, whether or not they work for an MSO.", "任何處理得益、未有披露、通風報訊或資助恐怖分子的人，不論是否受僱於金錢服務經營者。"))]),
    ))

# ---------------------------------------------------------------- 5. status of the Guideline
E_ = sec('status', ["¶1.1–1.8"],
         ("Reading the Guideline: 'should' binds you as much as 'must'", "閱讀指引：「應」與「須」同樣具約束力"),
    P("Start from the top box, a requirement you have not met, and read the three boxes below it left to right. The two red boxes are what can follow for the MSO and for the people behind it; the dashed box links to the Part 2 page.",
      "由頂部方格開始，即你未有遵守的一項規定，然後由左至右閱讀下方三個方格。兩個紅色方格分別是金錢服務經營者本身及其背後人士所面對的後果；虛線方格連結至第2部一頁。")
    + fig(fig_status, ("Both red boxes say 'may': the MSO may face disciplinary and other action, and non-compliance may also reflect adversely on the fitness and properness of the people behind it (¶1.3).",
                        "留意兩個紅色方格的用詞：經營者「或會」面對紀律行動及其他行動；經營者不遵從指引，「將」對其背後人士作為適當人選帶有負面影響（第1.3段）。"), STATUS_KEY)
    + traps(
        trap(("'Should' is not a softer 'must'", "「應」不是較寬鬆的「須」"), None, "¶1.6",
             vs=[(("Must", "須／必須"), ("A mandatory requirement.", "強制規定。")),
                 (("Should", "應／應該"), ("Also a mandatory requirement. The Guideline gives the two words the same force, so an answer that treats a 'should' as best practice you may skip is wrong.", "同樣是強制規定。指引賦予兩者相同效力；把「應」當作可以略過的良好做法，是錯誤答案。"))]),
        trap(("Mandatory, but not exhaustive", "屬強制，但並非無遺"), None, "¶1.6",
             vs=[(("Mandatory", "強制"), ("Every requirement the Guideline states with must or should.", "指引以「須」或「應」表述的每一項規定。")),
                 (("Not exhaustive", "並非無遺"), ("The means of meeting those requirements. MSOs differ too much for one set of measures to fit all, so use the Guideline as a basis to build measures for your own structure and business.", "履行規定的途徑。不同經營者差異重大，並無單一普遍適用的措施；你應以指引為基礎，按本身結構及業務制訂適當措施。"))]),
    ))

G1_NAV = [('threats', 'Three threats', '三種威脅'), ('fatf', 'The FATF standard', '特別組織標準'),
          ('laws', 'Six ordinances', '六條條例'), ('offences', 'Offences and penalties', '罪行與罰則'),
          ('status', 'Reading the Guideline', '閱讀指引')]
G1_BODY = A + B_ + C_ + D_ + E_

G1_META = dict(
    tab=("1", "1"),
    short=("Guideline Ch. 1 · Overview", "指引第1章 · 概覽"),
    eyebrow=("AML/CFT Guideline · Chapter 1 · Module 1", "《打擊洗錢指引》第1章 · 單元一"),
    title=("Threats, Laws and Offences", "威脅、法例與罪行"),
    lede=("Chapter 1 is the general knowledge the first module tests: what laundering, terrorist financing and proliferation financing are, the international standard behind Hong Kong's rules, the six ordinances that carry them, and the crimes you or any of your staff can commit under them. It also settles how to read the rest of the Guideline: a 'should' binds you as firmly as a 'must'.",
          "第1章是第一個單元考核的常識：洗錢、恐怖分子資金籌集及擴散資金籌集是甚麼，香港規則背後的國際標準，實施這些標準的六條條例，以及你或你任何一名職員都可能因而觸犯的罪行。本章亦確立閱讀指引其餘部分的方法：「應」與「須」同樣具約束力。"),
    foot=("Drawn from Chapter 1 (paragraphs 1.1 to 1.27) and the Glossary of the C&amp;ED Guideline on Anti-Money Laundering and Counter-Financing of Terrorism (For Money Service Operators), June 2023, with paragraph 6.1 for the contrast between ML and TF, paragraph 7.25 for the statutory defence, section 30(4)(a) of the AMLO, and the C&amp;ED circular MSSB/FATF_02/2026 of 3 July 2026 on the FATF's statements.",
          "取材自海關《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》（2023年6月）第1章（第1.1至1.27段）及詞彙部分；洗錢與恐怖分子資金籌集的分別取自第6.1段，法定免責辯護取自第7.25段，另參考打擊洗錢條例第30(4)(a)條，以及海關2026年7月3日有關特別組織聲明的通函。"),
)
