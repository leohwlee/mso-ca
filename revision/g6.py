# Guideline Chapter 6: terrorist financing, financial sanctions and proliferation
# financing. Who names the targets, what you must not do, the database, screening,
# and handling a possible match.
from ui import *
from bl_core import _runs
from g6_fig import (fig_regimes, REG_KEY, fig_db, DB_KEY, fig_who, WHO_KEY, fig_match, MATCH_KEY)


def resh(en, tc):
    """A row header that recall mode blurs: the resolution numbers are the thing to remember."""
    return f'<th class="rowh"><span class="answer" tabindex="0">{B(en, tc)}</span></th>'


def cc(*cs):
    """Join several citations into one."""
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


def UA(s):
    return (f"UNATMO s.{s}", f"《聯合國（反恐怖主義措施）條例》第{_runs(s)}條")


def vd(ch):
    return f'<td class="verdict">{ch}</td>'


UNSO = ("UNSO", "《聯合國制裁條例》")
WMD4 = ("WMD(CPS)O s.4", "《大規模毀滅武器（提供服務的管制）條例》第4條")
Q24 = ("FAQ Q24", "常見問題第24問")
C2023 = ("Circular 22 Nov 2023", "2023年11月22日通函")


# ---------------------------------------------------------------- 1. the UN resolutions
TF = sec('tf', ["¶6.1–6.3", "¶6.9–6.10", ("UN Security Council resolutions", "聯合國安理會決議")],
         ("The UN resolutions behind Hong Kong's laws", "香港法例背後的安理會決議"),
    P("Terrorist financing turns on where the property is going, not where it came from: that contrast with money laundering is on the <a href=\"#g1-threats\">Guideline Ch. 1 page</a>, and the statutory definitions are on the <a href=\"#s1-mltf\">Schedule 1 page</a>. Read the table below across: each resolution, what it does, and the law that carries it into Hong Kong.",
      "恐怖分子資金籌集看的是財產的終點或用途，而非來源：這個與洗錢的對比見<a href=\"#g1-threats\">指引第1章一頁</a>，法定定義見<a href=\"#s1-mltf\">附表1一頁</a>。下表請橫向閱讀：每項決議、其作用，以及在香港實施該決議的法例。")
    + table([th("The resolution", "決議"), th("What it does", "作用"), th("How it reaches Hong Kong", "如何在香港實施")], [
        tr(resh("UNSCR 1373 (2001)", "安理會第1373 (2001)號決議"),
           td("Calls on all member states to act to prevent and suppress the financing of terrorist acts", "要求全體成員國採取行動，防止和遏制恐怖分子資金籌集行為", "¶6.2"),
           td("UNATMO further implements its decision on measures to prevent terrorist acts", "《聯合國（反恐怖主義措施）條例》進一步實施該決議中關於防止恐怖主義行為的措施的決定", "¶6.3")),
        tr(resh("UNSCRs 1267 (1999), 1988 (2011), 1989 (2011), 2253 (2015), 2368 (2017) and their successors", "安理會第1267 (1999)號、第1988 (2011)號、第1989 (2011)號、第2253 (2015)號、第2368 (2017)號決議及其後續決議"),
           td("The UN publishes the names of individuals and organisations involved with Al-Qa'ida, ISIL (Da'esh) and the Taliban. Every member state must freeze the funds, other financial assets or economic resources of anyone named, and report suspected name matches to the relevant authorities",
              "聯合國公布涉及基地組織、伊黎伊斯蘭國（達伊沙）和塔利班組織的個人及組織名單。所有成員國均須凍結名列名單者的資金、其他財務資產或經濟資源，並就任何與名單吻合的可疑姓名／名稱向有關當局報告", "¶6.2"),
           td("A person or property designated by the UNSC Committee concerned can be specified in Hong Kong by Gazette notice under UNATMO section 4: see the next section",
              "由相關安理會委員會指定的人或財產，可根據《聯合國（反恐怖主義措施）條例》第4條在憲報刊登公告指明：見下一節", "¶6.4")),
        tr(resh("UNSCR 2178 (2014)", "安理會第2178 (2014)號決議"),
           td("Prevention of travel for the purpose of terrorist acts or terrorist training", "防止以恐怖主義行為或恐怖主義培訓為目的的旅程", "¶6.3"),
           td("UNATMO implements it; section 11L prohibits providing or collecting property to finance such travel", "《聯合國（反恐怖主義措施）條例》予以實施；第11L條禁止提供或籌集財產以資助該等旅程", "¶6.3, 6.5(e)")),
        tr(resh("UNSCR 1540 (2004) and its successors", "安理會第1540 (2004)號決議及其後續決議"),
           td("The <b>global</b> tier of the UNSC's two-tiered approach to PF, made under Chapter VII of the UN Charter and mandatory on member states",
              "安理會遏止擴散資金籌集的兩個層面中的<b>全球層面</b>；根據《聯合國憲章》第七章通過，對成員國施加強制責任", "¶6.9", post=flag()),
           td("Hong Kong's counter-PF regime is implemented through legislation that includes the WMD(CPS)O; the Guideline does not pair this resolution with one ordinance",
              "香港透過法例實施打擊擴散資金籌集制度，當中包括《大規模毀滅武器（提供服務的管制）條例》；指引沒有把此決議配對某一條例", "¶6.10")),
        tr(resh("UNSCR 1718 (2006) against the DPRK and UNSCR 2231 (2015) against Iran, and their successors", "針對朝鮮的安理會第1718 (2006)號決議及針對伊朗的第2231 (2015)號決議，及其後續決議"),
           td("The <b>country-specific</b> tier of the same approach", "同一方法中的<b>國家層面</b>", "¶6.9", post=flag()),
           td("Regulations made under the UNSO that are specific to the DPRK and Iran", "根據《聯合國制裁條例》針對朝鮮及伊朗訂立的規例", "¶6.10")),
    ], minw=820)
    + traps(
        trap(("Which resolution does what", "哪項決議做甚麼"), None, "¶6.2",
             vs=[(("UNSCR 1373 (2001)", "安理會第1373號決議"), ("Calls on all member states to prevent and suppress the financing of terrorist acts. The Guideline links the published name lists to other resolutions, such as 1267, 1988, 1989, 2253 and 2368.", "要求全體成員國防止和遏制恐怖分子資金籌集行為。指引把公布的名單連繫到其他決議，例如第1267、1988、1989、2253及2368號決議。")),
                 (("UNSCR 1267 and its family", "安理會第1267號決議及其系列"), ("Publish the names linked to Al-Qa'ida, ISIL (Da'esh) and the Taliban, which states must freeze and report matches against.", "公布涉及基地組織、伊黎伊斯蘭國（達伊沙）和塔利班組織的名單，各國須凍結其資產並報告吻合的姓名。"))]),
        trap(("Two tiers against proliferation financing", "遏止擴散資金籌集的兩個層面"), None, "¶6.9–6.10",
             vs=[(("Global", "全球層面"), ("UNSCR 1540 (2004): no single country named.", "安理會第1540 (2004)號決議：不針對個別國家。")),
                 (("Country-specific", "國家層面"), ("UNSCR 1718 (2006) against the DPRK and UNSCR 2231 (2015) against Iran; in Hong Kong, UNSO regulations specific to those two countries.", "針對朝鮮的第1718 (2006)號決議及針對伊朗的第2231 (2015)號決議；在香港以《聯合國制裁條例》下針對該兩國的規例實施。"))]),
    ))


# ---------------------------------------------------------------- 2. three laws
REG = sec('regimes', ["¶6.4–6.10", ("UNATMO s.4–6", "《聯合國（反恐怖主義措施）條例》第4至6條"), ("UNSO", "《聯合國制裁條例》"),
                      ("WMD(CPS)O s.4", "《大規模毀滅武器（提供服務的管制）條例》第4條")],
          ("Three laws: who names the target, and who can let a payment through", "三條法例：誰指明對象，誰可准許付款"),
    P("Read each column from top to bottom: the UN decision behind the law, who names the target and where the name is published, what you must not do, and the only way round the prohibition. Then compare across a row to see where the three laws part company.",
      "每欄由上而下閱讀：法例背後的聯合國決定、誰指明對象及在哪裏公布、你不可做的事，以及繞過禁令的唯一途徑。然後橫向比較每一行，看三條法例的分別。")
    + fig(fig_regimes, ("The WMD(CPS)O column ends without a licence because the Guideline describes none for it. Its prohibition turns on your belief or suspicion, not on a list.",
                         "《大規模毀滅武器（提供服務的管制）條例》一欄沒有特許，因為指引沒有就該條例描述任何特許。該條例的禁令取決於你的相信或懷疑，而非名單。"), REG_KEY)
    + traps(
        trap(("Who specifies, who freezes, who licenses", "誰指明，誰凍結，誰批予特許"), None, "¶6.4–6.8",
             vs=[(("Terrorism: UNATMO", "恐怖主義：《聯合國（反恐怖主義措施）條例》"), ("The Chief Executive specifies by Gazette notice, or applies for a court order that does so. The Secretary for Security freezes suspected terrorist property and grants the licences: you write to the Security Bureau.", "由行政長官在憲報刊登公告指明，或申請法庭命令指明。保安局局長凍結懷疑是恐怖分子的財產並批予特許：你向保安局提出書面申請。")),
                 (("UN sanctions: UNSO", "聯合國制裁：《聯合國制裁條例》"), ("The Chief Executive makes the regulations and grants the licences: you write to the Commerce and Economic Development Bureau.", "由行政長官訂立規例並批予特許：你向商務及經濟發展局提出書面申請。"))]),
        trap(("Two ways to specify under UNATMO", "《聯合國（反恐怖主義措施）條例》下的兩種指明途徑"), None, cc("¶6.4", UA("4–5")),
             vs=[(("After a UNSC Committee designation", "安理會委員會作出指定後"), ("Where a UNSC Committee has designated a person or property, the Chief Executive <b>may</b> specify it by notice in the Gazette (s.4).", "如某人或財產已被安理會委員會指定，行政長官<b>可</b>在憲報刊登公告指明（第4條）。")),
                 (("By court order", "經法庭命令"), ("Separately, the Chief Executive may apply to the Court of First Instance for an order specifying a person or property; if the order is made, it is also published in the Gazette (s.5).", "此外，行政長官可向原訟法庭申請命令，指明某人或財產；法庭作出的命令亦會在憲報刊登（第5條）。"))]),
    ))


# ---------------------------------------------------------------- 3. what is prohibited
PRO = sec('prohibited', ["¶6.5", "¶6.7", "¶6.10", "fn 56", "fn 57"],
          ("What you must not do with a listed party's money", "對名單上人士的資金，你不可做甚麼"),
    P("Each row of the first table is one kind of conduct the Guideline singles out under UNATMO as of particular relevance to MSOs, with the mental element or condition it turns on. The wording is the Guideline's summary of each provision.",
      "第一個表每一行是指引在《聯合國（反恐怖主義措施）條例》下指出與金錢服務經營者尤其相關的一種行為，以及其所依據的犯罪意圖或條件。用語均為指引對各條文的撮要。")
    + h3("UNATMO: the conduct that matters to you", "《聯合國（反恐怖主義措施）條例》：與你相關的行為")
    + table([th("The conduct", "行為"), th("What the provision does", "條文的作用"), th("What it turns on", "關鍵條件")], [
        tr(rh("Freezing suspected terrorist property", "凍結懷疑是恐怖分子的財產", cc("¶6.5(a)", UA("6"))),
           td("Empowers the Secretary for Security to freeze it", "授權保安局局長凍結該財產"),
           td("A power the Government holds, not a prohibition on you. The Guideline's own text gives section 6 to the Secretary for Security; its margin also cites section 6 beside restraint orders served during an investigation, which are on the <a href=\"#g7-lea\">Guideline Ch. 7 page</a>",
              "屬政府持有的權力，並非對你的禁令。指引正文把第6條的權力歸於保安局局長；指引在調查期間送達的限制令一段旁註亦引用第6條，限制令見<a href=\"#g7-lea\">指引第7章一頁</a>", cc("¶6.5(a)", "¶7.33"), post=flag())),
        tr(rh("Funding terrorist acts", "資助恐怖主義行為", cc("¶6.5(b)", UA("7"))),
           td("Prohibits providing or collecting property for use to commit terrorist acts", "禁止提供或籌集財產以作出恐怖主義行為"),
           td("The property is for use to commit terrorist acts", "財產用於作出恐怖主義行為")),
        tr(rh("Serving terrorists or their associates", "為恐怖分子或與恐怖分子有聯繫者提供財產或服務", cc("¶6.5(c)", UA("8"))),
           td("Prohibits anyone making available, or collecting or soliciting, property or financial (or related) services for terrorists and terrorist associates",
              "禁止任何人向恐怖分子及與恐怖分子有聯繫者提供財產或金融（或有關的）服務，或為其籌集財產或尋求金融（或有關的）服務"),
           td("Who it is for: terrorists and terrorist associates", "對象：恐怖分子及與恐怖分子有聯繫者")),
        tr(rh("Dealing with specified terrorist property", "處理指明的恐怖分子財產", cc("¶6.5(d)", UA("8A"))),
           td("Prohibits anyone dealing with property that is specified terrorist property, or property of a specified terrorist or terrorist associate", "禁止任何人處理指明的恐怖分子財產，或指明的恐怖分子或與恐怖分子有聯繫者的財產"),
           td("<b>Knowing</b> that it is, or <b>being reckless</b> as to whether it is", "<b>知道</b>屬實，或<b>罔顧</b>是否屬實", post=flag())),
        tr(rh("Funding travel for terrorism", "資助為恐怖主義而進行的旅程", cc("¶6.5(e)", UA("11L"))),
           td("Prohibits providing or collecting property to finance a person's travel between states for a specified purpose: perpetrating, planning, preparing or taking part in terrorist acts, or giving or receiving training connected with them",
              "禁止提供或籌集財產，以資助某人為指明目的進行往來國家之間的旅程，即作出、籌劃、籌備或參與恐怖主義行為，或提供或接受與此有關連的培訓"),
           td("With the intention, <b>or</b> knowing, that the travel is for that purpose: either state of mind is enough; and <b>even if no terrorist act occurs</b>",
              "在<b>懷有意圖及知悉</b>的情況下；<b>即使實際上沒有恐怖主義行為發生</b>", post=flag())),
    ], minw=820)
    + h3("UNSO: whom the offence reaches", "《聯合國制裁條例》：罪行涵蓋的對象")
    + P("Except under the authority of a licence granted by the Chief Executive, each of the following is an offence. In the table, 'funds' stands for funds, other financial assets or economic resources, and making them available covers doing so directly or indirectly, to the person or for their benefit.",
        "除獲行政長官批予的特許授權外，以下每一種情況均屬犯罪。下表的「資金」指資金、其他財務資產或經濟資源；「提供」包括直接或間接向對方提供，或為其利益而提供。")
    + table([th("The situation", "情況"), th("Offence without a licence?", "未獲特許是否犯罪？")], [
        tr(rh("You make funds available to a designated person or entity", "你向被指認的個人或實體提供資金", "¶6.7(a)(i)"), vd(YES)),
        tr(rh("You make funds available to a person or entity acting on behalf of, or at the direction of, a designated person or entity", "你向代表被指認的個人或實體或按其指示行事的個人或實體提供資金", "¶6.7(a)(ii)"),
           f'<td class="verdict">{YES}{flag()}</td>'),
        tr(rh("You make funds available to a person or entity owned or controlled by a designated person or entity", "你向由被指認的個人或實體擁有或控制的個人或實體提供資金", "¶6.7(a)(ii)"),
           f'<td class="verdict">{YES}{flag()}</td>'),
        tr(rh("You make funds available to an entity owned by any of those above", "你向上文所述者擁有的實體提供資金", "¶6.7(a)(iii)"),
           f'<td class="verdict">{YES}{flag()}</td>'),
        tr(rh("You deal, directly or indirectly, with funds belonging to, or owned or controlled by, any of them", "你直接或間接處理屬於上述個人或實體或由其擁有或控制的資金", "¶6.7(b)"), vd(YES)),
    ], minw=720)
    + table([th("The term", "詞語"), th("What it means", "涵義")], [
        tr(rh("Terrorist property", "恐怖分子財產", ("fn 56 · UNATMO s.2", "註56 · 《聯合國（反恐怖主義措施）條例》第2條")),
           td("The property of a terrorist or terrorist associate, or any other property intended to be used, or used, to finance or assist the commission of terrorist acts",
              "恐怖分子或與恐怖分子有聯繫者的財產；或任何擬用於或曾用於資助或協助作出恐怖主義行為的財產")),
        tr(rh("Targeted financial sanctions", "針對性金融制裁", "fn 57"),
           td("<b>Both</b> asset freezing <b>and</b> prohibitions preventing funds or other assets being made available, directly or indirectly, for the benefit of designated persons and entities",
              "<b>一併</b>指凍結資產<b>及</b>禁止為被指認的個人及實體的利益而直接或間接提供資金或其他資產", post=flag())),
        tr(rh("Provision of services, under the WMD(CPS)O", "《大規模毀滅武器（提供服務的管制）條例》下的提供服務", "¶6.10"),
           td("Widely defined, and includes lending money or any other provision of financial assistance", "定義廣泛，包括借出款項或以其他方式提供金融資助")),
    ], minw=720)
    + P("The maximum penalty for the UNATMO financing offences (14 years and a fine) is on the <a href=\"#g1-offences\">Guideline Ch. 1 page</a>, beside the other penalties it is easily confused with. The Guideline states none for the UNSO or WMD(CPS)O offences.",
        "《聯合國（反恐怖主義措施）條例》資金籌集罪行的最高刑罰（監禁14年及罰款）見<a href=\"#g1-offences\">指引第1章一頁</a>，並與容易混淆的其他刑罰並列。指引沒有列出《聯合國制裁條例》或《大規模毀滅武器（提供服務的管制）條例》罪行的刑罰。")
    + traps(
        trap(("Recklessness is enough to deal unlawfully", "罔顧已足以構成非法處理"),
             ("Dealing with property is caught when you know it is specified terrorist property, or property of a specified terrorist or terrorist associate. You do not have to know: being reckless as to whether it is such property is enough.",
              "如你知道財產屬指明的恐怖分子財產，或屬指明的恐怖分子或與恐怖分子有聯繫者的財產，處理該財產即受禁制。毋須確實知道：罔顧其是否屬該等財產已足夠。"),
             cc("¶6.5(d)", UA("8A"))),
        trap(("Two routes against proliferation financing", "打擊擴散資金籌集的兩條途徑"), None, "¶6.10",
             vs=[(("UNSO regulations for the DPRK and Iran", "《聯合國制裁條例》下針對朝鮮及伊朗的規例"), ("List-based: the question is whether the person is designated.", "以名單為本：問題在於對方是否被指認。")),
                 (("WMD(CPS)O section 4", "《大規模毀滅武器（提供服務的管制）條例》第4條"), ("Belief-based: any service you believe or suspect, on reasonable grounds, may be connected to PF. Lending money counts.", "以判斷為本：凡你基於合理理由相信或懷疑可能與擴散資金籌集有關的服務，均受禁制。借出款項亦包括在內。"))]),
    ))


# ---------------------------------------------------------------- 4. the database
DB = sec('database', ["¶6.11–6.15", "¶6.19"],
         ("Keeping the list you screen against", "備存用作篩查的名單"),
    P("Read the figure from left to right: what should go into the database, the database itself, and the ways you may hold it. Below it, screening draws on the same database.",
      "由左至右閱讀下圖：數據庫應收錄的名單、數據庫本身，以及你可選用的備存方式。下方是使用同一數據庫進行的篩查。")
    + fig(fig_db, ("The Commissioner draws UNSC updates on terrorism, TF and PF to your attention from time to time. The dashed lines are the alternatives open to you.",
                   "每當聯合國安理會就恐怖主義、恐怖分子資金籌集及擴散資金籌集頒布更新資料，關長會不時通知金錢服務經營者。虛線表示你可選用的方式。"), DB_KEY)
    + table([th("The situation", "情況"), th("What the Guideline expects", "指引的要求")], [
        tr(td("The lists change", "名單有變", "¶6.15"),
           td("Update the database in a timely way, and keep it easy for relevant staff to reach", "及時更新數據庫，並讓相關職員易於查閱")),
        tr(td("You operate internationally, and another jurisdiction imposes its own unilateral sanctions", "你經營國際業務，而另一司法管轄區實施單方面制裁", "¶6.11"),
           td("Hong Kong law does not normally oblige you to have regard to them. You still need to be aware of the scope and focus of the relevant regimes, and where they may affect your operations, consider the implications and take appropriate measures",
              "根據香港法律，你一般並無責任關注該等制裁。但你仍須注意相關制裁制度的範疇及重點；如可能對你的業務構成影響，應考慮會引致甚麼影響，並採取適當措施", post=flag())),
        tr(td("Setting up, and training staff", "建立制度及培訓職員", "¶6.12"),
           td("Establish and maintain effective policies, procedures and controls to comply with the TF, financial sanctions and PF laws. You and your staff should understand your legal and regulatory obligations well, and staff should get adequate guidance and training",
              "設立及維持有效的政策、程序及管控措施，確保恐怖分子資金籌集、金融制裁及擴散資金籌集的相關法規獲遵守。你及職員應充分了解本身的法律及監管責任，職員應獲提供充足導引及培訓")),
    ], minw=780)
    + numreq([
        (("As soon as practicable", "在切實可行範圍內盡快"),
         ("Include in the database the countries, individuals and entities the UNSC has put in its resolutions and sanctions lists", "把安理會決議及制裁名單所列的國家、個人及實體收錄於數據庫"),
         ("After the UNSC promulgates them, whether or not the sanctions are implemented by Hong Kong legislation", "在安理會頒布之後，不論有關制裁是否已透過香港法例實施"),
         ("Screening would miss the name, while the listing itself may already give grounds for knowledge or suspicion under the ML, TF and PF laws, triggering statutory (including reporting) obligations and offence provisions", "篩查會漏掉該名字，而被列入名單本身，為施行打擊洗錢、恐怖分子資金籌集及擴散資金籌集的相關法例，可能已構成知悉或懷疑的理由，法定（包括舉報）責任及罪行條文亦因而適用"),
         "¶6.14"),
        (("Timely", "及時"),
         ("Update the database", "更新數據庫"),
         ("Whenever there are changes to the lists", "每當名單資料有變化"),
         ("Screening runs against an out-of-date database", "篩查所用的數據庫已經過時"),
         "¶6.15"),
    ])
    + traps(
        trap(("Do not wait for Hong Kong to legislate", "毋須等待香港立法"), None, "¶6.14",
             vs=[(("A tempting wrong answer", "似是而非的答案"), ("Only sanctions Hong Kong has made law need to be in the database.", "只有已在香港立法的制裁才須收錄於數據庫。")),
                 (("What the Guideline says", "指引的說法"), ("UNSC listings go in as soon as practicable after promulgation, regardless of whether Hong Kong has implemented them.", "安理會名單在頒布後應在切實可行範圍內盡快收錄，不論香港是否已實施。"))]),
        trap(("Outsourcing the work is not outsourcing the responsibility", "工作可以外判，責任不能外判"), None, "¶6.13, 6.19",
             vs=[(("A third-party database", "第三者數據庫"), ("Allowed, but take appropriate measures, such as periodic sample testing, to make sure it is complete and accurate.", "可以，但應採取適當措施（例如定期抽樣測試），確保數據庫完整而準確。")),
                 (("Your overseas office", "在外地的辦事處"), ("It may keep the database or screen for you; the ultimate responsibility for complying with the TF, financial sanctions and PF laws remains yours.", "可為你備存數據庫或執行篩查；確保恐怖分子資金籌集、金融制裁及擴散資金籌集相關法規獲遵守的最終責任，仍由你承擔。"))]),
    ))


# ---------------------------------------------------------------- 5. screening
SCR = sec('screening', ["¶6.16–6.17", "fn 58", "¶4.4.1", Q24, C2023],
          ("When to screen, and whom", "何時篩查，篩查誰"),
    P("The top band is your customer; the bottom band is a single cross-border wire transfer. Red boxes are screened every time, whatever risk rating the customer carries; the grey box is screened on a risk-based approach.",
      "上半部是你的客戶；下半部是一宗跨境電傳轉帳。紅色方格不論客戶的風險評級為何，每次都要篩查；灰色方格按風險為本的方法篩查。")
    + fig(fig_who, ("The payment-chain list is the C&amp;ED FAQ's minimum for 'all relevant parties'; it is also summarised on the <a href=\"#ci-edd\">Circulars page</a>. Screening for politically exposed persons is a separate duty: see the <a href=\"#s2-pep\">PEP section</a>.",
                    "付款鏈名單是海關常見問題對「相關各方」的最低要求，亦撮錄於<a href=\"#ci-edd\">通函一頁</a>。政治人物篩查屬另一責任，見<a href=\"#s2-pep\">政治人物</a>一節。"), WHO_KEY)
    + table([th("The situation", "情況"), th("Whom you screen", "篩查誰")], [
        tr(rh("A new customer, individual or not", "新客戶，不論是否個人"),
           td("The customer and any beneficial owner. An individual customer can have one too: a natural person on whose behalf the customer is conducting a transaction or activity, for example. On a risk-based approach, also anyone purporting to act on the customer's behalf and, for a customer that is not an individual, its connected parties",
              "該客戶及其任何實益擁有人。個人客戶亦可有實益擁有人，例如由客戶代其進行交易或活動的自然人。按風險為本的方法，亦擴大至看似代表客戶行事的人；如客戶並非個人，亦擴大至其有關連者",
              cc("¶6.16(a)", "¶6.17", "¶4.4.1", "¶4.3.19"), post=flag())),
        tr(rh("A customer you have rated low risk", "你評為低風險的客戶"),
           td("Exactly the same people: screening is carried out irrespective of the risk profile attributed to the customer", "完全相同：不論客戶的風險狀況為何均應篩查", "fn 58", post=flag())),
        tr(rh("A new or updated designation is added to your database", "數據庫加入新增或更新的指認"),
           td("Your customers and their beneficial owners; connected parties and persons purporting to act on the customer's behalf (PPTAs) on a risk-based approach", "你的客戶及其實益擁有人；有關連者及看似代表客戶行事的人按風險為本的方法處理", "¶6.16(b), 6.17")),
        tr(rh("A customer asks you to carry out a cross-border or cross-boundary wire transfer or remittance transaction", "客戶要求你執行一宗跨境電傳轉帳或匯款交易"),
           td("All relevant parties in the transfer: the FAQ's minimum list is in the figure above", "轉帳的相關各方：常見問題列出的最低要求見上圖", cc("¶6.16(c)", Q24), post=flag())),
    ], minw=760)
    + numreq([
        (("At onboarding", "建立關係時"),
         ("Screen the customer and any beneficial owners against the current database", "根據當時的數據庫篩查客戶及其任何實益擁有人"),
         ("Every new business relationship, whatever the customer's risk profile", "每段新的業務關係，不論客戶的風險狀況為何"),
         ("You risk establishing a relationship with a terrorist suspect or possible sanctioned party, which is what screening exists to prevent", "你可能與嫌疑恐怖分子或可能受制裁的一方建立業務關係，而篩查正是為了防止這種情況"),
         "¶6.16(a) · fn 58"),
        (("As soon as practicable", "在切實可行範圍內盡快"),
         ("Screen customers and any beneficial owners against every new and updated designation", "根據所有新增及任何更新的指認篩查客戶及其任何實益擁有人"),
         ("Each time designations are added to or changed in the database", "每次數據庫加入或更改指認"),
         ("A customer designated after onboarding would go undetected", "在開戶後才被指認的客戶會被遺漏"),
         "¶6.16(b)"),
        (("Before the transfer", "執行轉帳前"),
         ("Screen all relevant parties against the current database", "根據當時的數據庫篩查相關各方"),
         ("Every cross-border or cross-boundary wire transfer, remittance transactions included", "每宗跨境電傳轉帳，包括匯款交易"),
         ("A check made after the money has gone does not meet the rule", "在款項匯出後才篩查，並不符合規定"),
         "¶6.16(c)"),
    ])
    + traps(
        trap(("No risk-based opt-out, but a risk-based extension", "不可按風險豁免，但可按風險擴展"), None, "fn 58 · ¶6.17",
             vs=[(("Customers, beneficial owners, relevant parties to a transfer", "客戶、實益擁有人、轉帳的相關各方"), ("Screened irrespective of the customer's risk profile.", "不論客戶的風險狀況為何均應篩查。")),
                 (("Connected parties and PPTAs", "有關連者及看似代表客戶行事的人"), ("Screening is extended to them using a risk-based approach.", "以風險為本的方法把篩查擴大至他們。"))]),
        trap(("The connected-party extension covers onboarding and re-screening only", "有關連者的擴展只涵蓋建立關係時及重新篩查"),
             ("The extension to connected parties and PPTAs attaches to the screening when the relationship is established and against new or updated designations. Transfer screening already reaches all relevant parties in the payment.",
              "擴大至有關連者及看似代表客戶行事的人的規定，適用於建立關係時的篩查及根據新增或更新指認進行的篩查。轉帳篩查本已涵蓋付款的相關各方。"),
             "¶6.17"),
        trap(("Beneficial owners were the gap the C&amp;ED found", "海關發現的漏洞在於實益擁有人"),
             ("In its 2023 supervisory findings the C&amp;ED found MSOs screening customers against a commercial database for PEPs and targeted financial sanctions without extending it to beneficial owners. It restated that customers, their beneficial owners and all relevant parties in remittances are to be screened against sanctions and designated-persons lists, irrespective of risk profile. The circular words this as a requirement; the Guideline paragraph it cites says 'should'.",
              "海關在2023年的巡查結果中發現，有經營者以商業數據庫篩查客戶是否屬政治人物或受針對性金融制裁，但沒有擴大至實益擁有人。海關重申，不論客戶的風險狀況為何，均須與制裁名單及被指認的個人名單比對，篩查客戶、其實益擁有人及匯款交易的所有相關各方。通函用「須」，而所引用的指引第6.16段用「應」。"),
             cc(C2023, "¶6.16")),
    ))


# ---------------------------------------------------------------- 6. a possible match
MAT = sec('match', ["¶6.18", "¶6.14", "¶7.1", "¶4.9.1"],
          ("A possible match: check it, report any suspicion, record everything", "可能吻合：查核、舉報懷疑、全部記錄"),
    P("Start at the top. The left-hand branch is a genuine hit; the right-hand exit from the second question is a report to the JFIU. A genuine hit also goes on to the second question, because the listing itself may give grounds for suspicion. Every path ends at the record.",
      "由頂部開始。左邊分支是真正吻合；第二個問題右邊的出口是向聯合財富情報組（財富情報組）報告。真正吻合亦要接着考慮第二個問題，因為被列入名單本身可能已構成懷疑的理由。所有路徑都以記錄作結。")
    + fig(fig_match, ("Whether it is a genuine hit and whether to report are separate questions: the report is triggered by suspicion of TF, PF or a sanctions violation. What the report must say, and when, is on the <a href=\"#g7-jfiu\">Guideline Ch. 7 page</a>.",
                      "是否真正吻合與是否舉報是兩個不同問題：觸發舉報的是懷疑涉及恐怖分子資金籌集、擴散資金籌集或違反制裁。報告須說明甚麼、何時提交，見<a href=\"#g7-jfiu\">指引第7章一頁</a>。"), MATCH_KEY)
    + P("For terrorist property, reporting is also a statutory duty under UNATMO section 12(1): the deadline and the penalty for missing it are on the <a href=\"#g7-duty\">Guideline Ch. 7 page</a>. Records of the enhanced-check results, together with all screening records, should be documented or recorded electronically.",
        "如屬恐怖分子財產，舉報亦是《聯合國（反恐怖主義措施）條例》第12(1)條下的法定責任：期限及未有舉報的刑罰見<a href=\"#g7-duty\">指引第7章一頁</a>。更嚴格查核的結果（連同篩查紀錄）應記錄在案或以電子方式記錄。")
    + traps(
        trap(("A possible match is not yet a hit", "可能吻合不等於真正吻合"), None, "¶6.18 · ¶6.6–6.8",
             vs=[(("Possible match", "可能吻合"), ("Carry out enhanced checks to decide whether it is genuine.", "執行更嚴格的查核，以斷定是否真正吻合。")),
                 (("Genuine hit", "真正吻合"), ("The prohibitions apply: any payment to or for the party needs a licence.", "禁令適用：向該方或為其利益付款均須取得特許。"))]),
        trap(("Report to the JFIU; ask the bureau for a licence", "向財富情報組舉報；向保安局或商務及經濟發展局申請特許"), None, "¶6.6, 6.8, 6.18",
             vs=[(("Suspicion of TF, PF or a sanctions violation", "懷疑涉及恐怖分子資金籌集、擴散資金籌集或違反制裁"), ("Report to the JFIU.", "向財富情報組報告。")),
                 (("Permission to pay a designated party", "准許向指定一方或被指認人士付款"), ("Write to the bureau for the law concerned: see <a href=\"#g6-regimes\">Three laws</a>.", "按所涉法例，向保安局（《聯合國（反恐怖主義措施）條例》）或商務及經濟發展局（《聯合國制裁條例》）提出書面申請：見<a href=\"#g6-regimes\">三條法例</a>。"))]),
        trap(("Enhanced checks are not enhanced due diligence", "更嚴格的查核不等於更嚴格的盡職審查"), None, cc("¶6.18", "¶4.9.1"),
             vs=[(("Enhanced checks", "更嚴格的查核"), ("Done when screening throws up a possible name match, to decide whether it is a genuine hit.", "在篩查期間識別出可能吻合的姓名／名稱時執行，以斷定是否真正吻合。")),
                 (("Enhanced due diligence (EDD)", "更嚴格的盡職審查"), ("Measures you must apply to a business relationship or transaction to mitigate and manage high ML/TF risks: see the <a href=\"#s2-sdd-edd\">Schedule 2 page</a>.", "為減低及管理高度洗錢／恐怖分子資金籌集風險，必須對業務關係或交易執行的措施：見<a href=\"#s2-sdd-edd\">附表2一頁</a>。"))]),
    ))


G6_NAV = [('tf', 'UN resolutions', '安理會決議'), ('regimes', 'Three laws', '三條法例'),
          ('prohibited', 'What is prohibited', '禁止的行為'), ('database', 'The database', '數據庫'),
          ('screening', 'When and whom', '何時篩查誰'), ('match', 'A possible match', '可能吻合')]
G6_BODY = TF + REG + PRO + DB + SCR + MAT

G6_META = dict(
    tab=("6", "6"),
    short=("Guideline Ch. 6 · Sanctions", "指引第6章 · 制裁"),
    eyebrow=("AML/CFT Guideline · Chapter 6 · Modules 1 and 6", "《打擊洗錢指引》第6章 · 單元一及單元六"),
    title=("Terrorist financing, sanctions and proliferation financing", "恐怖分子資金籌集、金融制裁及擴散資金籌集"),
    lede=("Chapter 6 decides whom you must not pay without a licence, and how you find out in time. Three laws name the targets and set the prohibitions. The Guideline then has you keep a database of every list made known to you, screen customers, beneficial owners and all relevant parties to a transfer against it whatever their risk, check possible matches, report suspicion to the JFIU and keep the records.",
          "第6章決定哪些人你未獲特許便不可付款，以及如何及時發現他們。三條法例負責指明對象及訂立禁令。指引則要求你備存數據庫，綜合你所知的每份名單；不論風險高低，以數據庫篩查客戶、實益擁有人及轉帳的相關各方；查核可能吻合的名字；向財富情報組舉報懷疑；並備存紀錄。"),
    foot=("Sources: Guideline on Anti-Money Laundering and Counter-Financing of Terrorism (For Money Service Operators), June 2023, Chapter 6 with ¶4.3.19, ¶4.4.1, ¶4.9.1 and ¶7.1; C&amp;ED FAQ applicable to all MSOs, Q24; C&amp;ED circular of 22 November 2023 (supervisory findings on CDD).",
          "資料來源：《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》（2023年6月）第6章，以及第4.3.19、4.4.1、4.9.1及7.1段；海關適用於所有金錢服務經營者的常見問題第24問；海關2023年11月22日（盡職審查巡查結果）通函。"),
)
