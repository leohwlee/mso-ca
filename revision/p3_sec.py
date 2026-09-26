# AMLO Part 3: supervision and investigations, written for a money service operator.
from bl_core import *
from p3_fig import fig_tracks, fig_clock
import ui as U


def h(en, tc):
    return f'<th>{B(en, tc)}</th>'


def rh(en, tc, cite=None):
    return f'<th class="rowh">{B(en, tc)}{cite_html(cite)}</th>'


def d(en, tc, cite=None, cls='', pre=''):
    k = f' class="{cls}"' if cls else ''
    body = f'<span class="answer" tabindex="0">{B(en, tc)}</span>' if cls == 'pen' else B(en, tc)
    return f'<td{k}>{pre}{body}{cite_html(cite)}</td>'


def table(head, rows, note=None, minw=720):
    t = '<thead><tr>' + head + '</tr></thead>' if head else ''
    n = f'<tr class="note"><td colspan="9">{note}</td></tr>' if note else ''
    return f'<div class="tbl"><table style="min-width:{minw}px">{t}<tbody>{rows}{n}</tbody></table></div>'


KEY = ('<div class="legend"><span><i class="may"></i>' + B("a power someone may exercise over you", "他人可對你行使的權力", True) + '</span>'
       '<span><i class="must"></i>' + B("a duty on you, or a consequence for you", "你的責任，或你要承受的後果", True) + '</span>'
       '<span><i></i>' + B("a neutral fact", "中性事實", True) + '</span></div>')

# ------------------------------------------------------------------ A. two tracks
CMP = table(
    h("", "") + h("Routine inspection", "例行視察") + h("Investigation", "調查"),
    ''.join([
        '<tr>' + rh("Who turns up", "誰會出現")
        + d("An <b>authorized person</b>. The Commissioner authorises them <b>in writing</b>, and they may be any person, or any person of a class he picks.", "<b>獲授權人</b>。由關長<b>藉書面</b>授權，人選可以是任何人，或關長選定的任何某類別人士。", "s.8 · s.9(12)")
        + d("An <b>investigator</b>. The Commissioner <b>directs</b> a public officer employed in the Customs and Excise Department, or with the Financial Secretary's consent <b>appoints</b> someone from outside.", "<b>調查員</b>。由關長<b>指示</b>受僱任職於香港海關的公職人員擔任，或在財政司司長同意下<b>委任</b>外部人士。", "s.8 · s.11(1)–(2)") + '</tr>',
        '<tr>' + rh("Why they came", "為何前來")
        + d("Only to check whether you are complying, have complied, or are likely to be able to comply with the rules. <b>No suspicion of wrongdoing is needed.</b>", "只為確定你是否正遵從、已遵從或相當可能能夠遵從有關規定。<b>毋須懷疑有任何不當行為。</b>", "s.9(1)")
        + d("Because the Commissioner has <b>reasonable cause to believe</b> an offence may have been committed, or has <b>reason to inquire</b> into a contravention while considering disciplinary action.", "因關長<b>有合理因由相信</b>可能已犯罪行，或在考慮紀律處分時<b>有理由查訊</b>是否有違反。", "s.11(1)") + '</tr>',
        '<tr>' + rh("Who it can be aimed at", "對象是誰")
        + d("A <b>prescribed person</b>, called the <b>inspection subject</b>. A licensed money service operator is one of the twelve kinds of <b>non-Part 5B prescribed person</b> listed in the Ordinance, alongside authorized institutions, licensed corporations, authorized insurers, TCSP licensees and others, so the power reaches you.", "<b>訂明人士</b>，即<b>視察對象</b>。條例列出十二類<b>非第5B部訂明人士</b>，持牌金錢服務經營者是其中之一（其他包括認可機構、持牌法團、獲授權保險人、信託或公司服務持牌人等），因此這項權力適用於你。", "s.8 · s.9(1)")
        + d("A <b>covered person</b>: the person the investigation is about, or anyone the investigator reasonably believes holds relevant records or information. The list is not limited to prescribed persons.", "<b>受涵蓋人</b>：被調查的人，或調查員有合理因由相信管有相關紀錄或資料的任何人。此範圍不限於訂明人士。", "s.12(1)") + '</tr>',
        '<tr>' + rh("Where", "在哪裏")
        + d("Your <b>business premises</b>, at any reasonable time. For you those are the premises shown in the <b>register of licensees</b> the Commissioner keeps.", "你的<b>業務處所</b>，可在任何合理時間進入。就你而言，即關長備存的<b>持牌人登記冊</b>所顯示的處所。", "s.9(1A), (15)")
        + d("Nowhere in particular: the investigator has <b>no power of entry</b> (a magistrate's warrant is a separate matter). The main requirements (s.12(2)) are made <b>in writing</b>, and those to produce records or to attend name a time and place.", "並無特定地點：調查員<b>無權進入處所</b>（裁判官手令另作別論）。主要要求（第12(2)條）以<b>書面</b>作出，其中交出紀錄及會晤的要求須指明時間（或限期）及地點。", "s.12(2) · s.17") + '</tr>',
        '<tr>' + rh("What they can make you do", "可要求你做甚麼")
        + d("Give access to and produce a business record at a stated time and place, and answer questions about that record or a transaction. <b>They cannot summon you to an interview.</b>", "在指明時間及地點提供查閱及交出業務紀錄，並回答關乎該紀錄或交易的問題。<b>但不能傳召你會晤。</b>", "s.9(3)–(5)", pre='<span class="answer">').replace('</td>', '</span></td>')
        + d("Four things: <b>produce</b> records, <b>attend and answer</b> questions in person, <b>respond</b> to written questions, and give <b>any other assistance</b> you reasonably can. Then explain anything you produced.", "四項：<b>交出</b>紀錄、親身<b>會晤及回答</b>問題、<b>回應</b>書面問題，以及提供你按理能夠提供的<b>一切其他協助</b>；其後須就已交出的文件作出解釋。", "s.12(2)–(3)", pre='<span class="answer">').replace('</td>', '</span></td>') + '</tr>',
        '<tr>' + rh("Going to someone else instead of you", "改為向他人取證")
        + d("They may make inquiries of an <b>information holder</b> (someone they reasonably believe has information about, or holds, your records), but <b>only as a last resort</b>, after forming reasonable cause to believe they cannot get it from you.", "可向<b>資料持有人</b>（即被合理相信掌握關於你的紀錄的資料或管有你的紀錄的人）作出查訊，但<b>只可作為最後手段</b>，且須先有合理因由相信無法從你處取得。", "s.9(6)–(7), (15)")
        + d("Anyone reasonably believed to hold relevant records or information can be required directly. There is <b>no last-resort condition</b>.", "任何被合理相信持有相關紀錄或資料的人，均可被直接要求。<b>並無最後手段的條件。</b>", "s.12(1)") + '</tr>',
        '<tr>' + rh("Proving they are who they say", "證明身分")
        + d("They must show you a copy of the Commissioner's written authorisation <b>as soon as reasonably practicable</b> once they start using the power.", "開始行使權力後，須在<b>合理地切實可行範圍內盡快</b>向你出示關長書面授權的文本。", "s.9(14)")
        + d("They must show you the direction or appointment <b>before imposing the first requirement</b> on you. Earlier, and stricter.", "須在向你<b>施加第一項要求之前</b>出示指示或委任文本。時間更早，要求更嚴。", "s.11(5)") + '</tr>',
        '<tr>' + rh("Verifying your answers", "核實你的回答")
        + d("They may require you in writing to confirm an answer by <b>statutory declaration</b> within a time they set, and may take the declaration themselves. If you gave no answer because you <b>do not know</b>, they may make you declare <b>that fact and the reason</b> the same way.", "可藉書面要求你在其指定的限期內以<b>法定聲明</b>核實答案，並可親自監理該聲明。如你以<b>不知悉</b>有關資料為理由而沒有回答，亦可要求你以同樣方式核實<b>該事實及理由</b>。", "s.9(9)–(11)")
        + U.td("The same, covering answers, responses, explanations and particulars. The no-answer declaration is wider here: the information is not within your knowledge <b>or not in your possession</b>.", "相同，並涵蓋回答、回應、解釋及詳情。沒有回答時的法定聲明範圍較廣：有關資料是你所不知悉的，<b>或並非由你管有的</b>。", "s.12(4)–(6)", post=U.flag()) + '</tr>',
        '<tr>' + rh("Your customers' affairs", "你客戶的事務")
        + d("If the officer was authorised by a regulatory authority that is <b>not your own</b>, nothing about a customer need be disclosed unless that other regulatory authority <b>certifies in writing</b> that it is necessary.", "如該人員由<b>並非你的</b>監管當局授權，除非該當局<b>藉書面證明</b>屬必要，否則毋須披露任何客戶資料。", "s.9A")
        + d("The same certificate, <b>and</b> the investigator must reasonably believe that customer can give information relevant to the investigation.", "須有同樣的書面證明，<b>並且</b>調查員須有合理因由相信該客戶能提供與調查相關的資料。", "s.12A") + '</tr>',
        '<tr>' + rh("If the answer might incriminate you", "如回答可能令你入罪")
        + d("Part 3 gives you <b>no protection at all</b> for answers given on a routine inspection: its shield covers only an investigator's requirements.", "就例行視察所作的回答，第3部<b>完全沒有保障</b>：其保障只涵蓋調查員施加的要求。", "s.15(2)(a)")
        + U.td("You must still answer. If you claim <b>before</b> answering that it might incriminate you, the requirement, the question and your answer are not admissible against you in criminal proceedings, <b>except</b> where you are charged over that answer itself under s.13 (for example, for a false or misleading answer) or under Part V of the Crimes Ordinance. The investigator must first inform or remind you of this.", "你仍須回答。如在回答<b>之前</b>聲稱該回答可能會導致你入罪，則該要求、有關問題及你的回答，不得在刑事法律程序中接納為針對你的證據；<b>但</b>如你就該回答本身被控犯第13條所訂罪行（例如給予虛假或具誤導性的回答），或《刑事罪行條例》（第200章）第V部所訂罪行，則不在此限。調查員須事先告知或提醒你此限制。", "s.13(11) · s.15(1)–(3)", post=U.flag()) + '</tr>',
        '<tr>' + rh("What they do afterwards", "事後的處理")
        + d("Nothing is prescribed.", "沒有訂明。", "—")
        + d("Interim reports to the Commissioner when he asks, a <b>final report</b> as soon as the investigation is done, and he may <b>publish</b> it with the Secretary for Justice's consent.", "關長要求時須提交中期報告；調查完成後須盡快提交<b>最後報告</b>；關長並可在律政司司長同意下<b>公布</b>該報告。", "s.12(8)–(10)") + '</tr>',
    ]), minw=760)

A = sec('tracks', [("Part 3", "第3部"), ("supervision and", "監管與"), ("investigations", "調查")],
        ("Two very different visits", "兩種截然不同的到訪"),
    P("Telling the two visitors apart is most of what this Part tests. Read the top half down the <b>left</b> column for a routine inspection and down the <b>middle</b> column for an investigation; the warrant on the <b>right</b> belongs to neither. The columns meet at one box because all three are after the same records. Both visitors can make you answer questions, but only the investigator can require you to attend before them at a time and place they name and answer there. Below that box the columns no longer mean the tracks: a failure to meet an authorized person's or investigator's requirement can lead to prosecution, or to a court application with two possible results, and the double arrow at the foot joins the two that cannot both be used.",
      "分辨這兩種訪客，正是本部考核的重點。看圖的上半部時，<b>左</b>欄一路是例行視察，<b>中</b>欄一路是調查；<b>右</b>邊的手令則不屬於任何一方。各欄在同一個方框匯合，因為三者針對的是同一批紀錄。兩種訪客都可要求你回答問題，但只有調查員才能要求你在其指明的時間及地點會晤並回答問題。該方框以下，各欄不再代表兩條途徑：不遵從獲授權人或調查員施加的要求，可導致刑事檢控，或導致向法庭提出申請而有兩種可能結果；底部的雙向箭頭連接的，是不可兩者兼用的那兩項。")
    + f'<figure><div class="figwrap">{tri(fig_tracks)}</div>' + KEY
    + '<figcaption>' + B("The colours above are used the same way everywhere on this page. A warrant belongs to neither track: it can be applied for by an investigator, by an authorized person, or by any employee or staff member of the Commissioner, so it runs alongside both as a third way of taking the records. The two red boxes joined at the foot are the pair that cannot both be used for the same conduct. The lower half covers only requirements made on a routine inspection (s.9) or in an investigation (s.12). Under a warrant, failing without reasonable excuse to comply with a requirement or prohibition, or obstructing the officer exercising those powers, is a separate offence under s.17(9); the s.10 and s.13 offences and the s.14 court route do not apply to it.",
                         "上方顏色在本頁各處含義相同。手令不屬於任何一條途徑：調查員、獲授權人，或關長的任何僱員或員工均可申請，因此它與兩條途徑並行，是取得紀錄的第三條途徑。底部以箭頭相連的兩個紅色方框，就同一行為不可兩者兼用。下半部只涵蓋例行視察（第9條）或調查（第12條）中施加的要求。根據手令，無合理辯解而沒有遵從有關要求或禁止，或妨礙行使該等權力的人員，屬第17(9)條所訂的另一項罪行；第10條及第13條的罪行及第14條的法庭途徑均不適用。") + '</figcaption></figure>'
    + CMP)

# ------------------------------------------------------------------ B. what applies when
WHEN = table(
    h("If this happens to you", "如發生以下情況") + h("What it is, and what applies", "那是甚麼，以及適用甚麼規定"),
    ''.join([
        '<tr>' + rh("An officer walks in during opening hours and asks to see your files", "有人員在營業時間內進入，要求查閱你的檔案")
        + d("A <b>routine inspection</b>. They need no suspicion, but they may only enter at a <b>reasonable time</b>, only your business premises as shown in the register of licensees, and they must show you a copy of the Commissioner's written authorisation as soon as reasonably practicable.", "屬<b>例行視察</b>。毋須任何懷疑，但只可在<b>合理時間</b>進入，且只限持牌人登記冊所顯示的業務處所；並須在合理地切實可行範圍內盡快出示關長書面授權的文本。", "s.9(1A) · s.9(14) · s.9(15)") + '</tr>',
        '<tr>' + rh("A written notice tells you to attend at a named place and time", "你收到書面通知，要求你在指定地點及時間出席")
        + d("This is an <b>investigation</b>, not an inspection, because only an investigator can compel attendance. Check that they showed you their direction or appointment <b>before</b> this first requirement was imposed.", "這是<b>調查</b>而非視察，因為只有調查員能強制你出席。請核實他們是否在施加這第一項要求<b>之前</b>已出示指示或委任文本。", "s.12(2)(b) · s.11(5)") + '</tr>',
        '<tr>' + rh("They ask your bank, or one of your customers, rather than you", "他們向你的銀行或其中一名客戶索取，而非向你")
        + d("On a routine inspection that person is an <b>information holder</b>, and they can be asked <b>only</b> where the officer has reasonable cause to believe the material cannot be obtained from you. In an investigation they are a <b>covered person</b>, and there is no such condition.", "在例行視察中，該人屬<b>資料持有人</b>，<b>只有</b>當人員有合理因由相信無法從你處取得有關資料時方可向其索取；在調查中，該人屬<b>受涵蓋人</b>，並無此條件。", "s.9(6)–(7) · s.12(1)") + '</tr>',
        '<tr>' + rh("The officer was authorised by a regulatory authority other than the Commissioner and asks about a customer", "該人員由關長以外的監管當局派出，並查詢客戶資料")
        + d("You need not disclose anything about a customer's affairs <b>unless that other regulatory authority certifies in writing</b> that the disclosure is necessary. In an investigation they must also reasonably believe that customer has relevant information.", "除非<b>該其他監管當局藉書面證明</b>披露屬必要，否則你毋須披露任何客戶事務資料。在調查中，他們另須有合理因由相信該客戶掌握相關資料。", "s.9A · s.12A") + '</tr>',
        '<tr>' + rh("You are asked something whose honest answer would incriminate you", "你被問及一條如實回答會令你入罪的問題")
        + d("If an investigator is asking, refusing is not an option. <b>Say so before you answer</b>, and the requirement, the question and your answer are not admissible against you in criminal proceedings. The shield does not help if you are charged over that answer itself under s.13 (for example, for a false answer) or under Part V of the Crimes Ordinance, and it does not exist at all on a routine inspection.", "如提問的是調查員，拒絕並非選項。<b>在回答前先行聲稱</b>，則該要求、有關問題及你的回答，不得在刑事法律程序中接納為針對你的證據。但如你就該回答本身被控犯第13條所訂罪行（例如給予虛假回答），或《刑事罪行條例》（第200章）第V部所訂罪行，該保障即不適用；而在例行視察中，該保障根本不存在。", "s.13(11) · s.15") + '</tr>',
        '<tr>' + rh("You hold the documents but someone owes you money for them", "文件在你手上，但有人欠你有關費用")
        + d("A <b>lien</b> changes nothing about producing them. You must still produce, <b>no fee is payable</b> to you for doing so, and producing them <b>does not destroy your lien</b>.", "<b>留置權</b>不影響交出文件。你仍須交出，交出<b>毋須向你支付費用</b>，而交出<b>亦不影響你的留置權</b>。", "s.16") + '</tr>',
        '<tr>' + rh("The records are held in an information system, or are not recorded in a legible form", "紀錄記錄於資訊系統內，或並非以可閱讀形式記錄")
        + d("Whoever can require the record can also require a <b>reproduction in legible form</b>, or for an information system, one in a form that can be reproduced legibly. Keeping it on a server is not an answer.", "任何有權要求交出該紀錄的人，亦可要求交出<b>以可閱讀形式重現而製成的版本</b>；如屬資訊系統，則可要求交出能以可閱讀形式重現的版本。存放於伺服器並非理由。", "s.18") + '</tr>',
        '<tr>' + rh("You cannot produce what they asked for in the time given", "你無法在指定時間內交出所要求的文件")
        + U.td("Without a <b>reasonable excuse</b> this is an offence. Separately, the <b>authorized person or investigator who imposed the requirement</b> may apply to the Court of First Instance for an inquiry; the Court may order you to comply and may punish you as if for contempt. A prosecution and contempt-style punishment <b>cannot both</b> be pursued for the same conduct.", "如無<b>合理辯解</b>，即屬犯罪。施加該要求的<b>獲授權人或調查員</b>亦可藉原訴傳票向原訟法庭申請進行查訊；原訟法庭可命令你遵從，並可猶如你犯藐視法庭罪般懲罰你。就同一行為，刑事檢控與猶如藐視法庭罪的懲罰<b>不可兩者兼用</b>。", "s.10(1) · s.13(1) · s.14", post=U.flag()) + '</tr>',
        '<tr>' + rh("Officers arrive with a warrant signed by a magistrate", "人員持裁判官簽發的手令到場")
        + d("They may enter at any time within <b>7 days</b> beginning on the warrant's date, <b>by force if necessary</b>, and search for, seize and remove records. Any of your staff found there can be required to produce records. Ask to see the warrant: they must produce it if required.", "他們可在自手令日期起計的<b>7日</b>內隨時進入（<b>如有必要，可強行進入</b>），並搜尋、檢取和移走紀錄。在場的任何員工均可被要求交出紀錄。你可要求查閱手令：如被要求，他們須出示。", "s.17(1)–(3), (7)") + '</tr>',
        '<tr>' + rh("Your files have been taken away", "你的檔案已被取走")
        + U.td("If they were removed under a magistrate's warrant, ask for the <b>receipt</b>, which must be given as soon as reasonably practicable. Those records may be kept for up to 6 months, or longer if they are or may be required for criminal proceedings or proceedings under the Ordinance, for as long as those proceedings need them. Records you produced on a routine inspection or in an investigation (s.9 or s.12) carry <b>no such receipt or time rule</b>. Two rules cover inspecting and copying them: the officer who removed them under the warrant <b>may</b> permit it, while an investigator, or an authorized person holding the Commissioner's written authorisation, who has taken possession of records under Part 3 (by warrant or otherwise) <b>must</b> permit it, and may impose reasonable conditions.","如檔案是根據裁判官手令被移走，應索取<b>收據</b>；收據須在合理地切實可行範圍內盡快發出。該等檔案可保留不超過6個月；如屬或可能屬刑事法律程序或根據本條例進行的法律程序所需要，可在該等程序所需的較長期間內保留。如檔案是在例行視察或調查中（第9條或第12條）應要求交出的，則<b>無上述收據或保留期限的規定</b>。有兩條規則涉及<b>查閱及複製</b>：根據手令移走檔案的人<b>可</b>准許；而調查員或持關長書面授權的獲授權人，如已根據本部（不論是否藉手令）管有紀錄，則<b>須</b>准許，並可施加合理條件。", "s.17(4)–(6) · s.19", post=U.flag()) + '</tr>',
        '<tr>' + rh("You are tempted to tidy the file before handing it over", "你想在交出前先「整理」一下檔案")
        + d("Destroying, falsifying, concealing or disposing of a required record <b>with intent to conceal</b> is its own offence, carrying a million dollars and two years. Causing or permitting someone else to do it counts too.", "出於<b>隱瞞意圖</b>而銷毀、揑改、隱藏或處置被要求交出的紀錄，本身即屬罪行，可處罰款一百萬元及監禁2年。致使或准許他人作出該等行為同樣入罪。", "s.20") + '</tr>',
    ]), minw=740)

BSEC = sec('when', [("look it up", "按情況查閱"), ("by situation", "對號入座")],
           ("What applies when", "甚麼情況適用甚麼規定"),
    P("The same eleven situations come up again and again, in the exam and at the counter. This is the lookup: find your situation on the left, and the rule is on the right.",
      "以下十一種情況，無論在試場或櫃位都會反覆出現。這是一張對照表：左邊找出你的處境，右邊就是適用的規則。")
    + WHEN)

# ------------------------------------------------------------------ C. timing
STD = table(
    h("The wording", "用語") + h("Where it is used", "用於何處"),
    ''.join([
        '<tr>' + rh("at any reasonable time", "於任何合理時間")
        + d("When an authorized person may enter your business premises to inspect. It is the <b>only</b> limit on the timing of a routine visit.", "獲授權人可於何時進入你的業務處所作視察。這是例行到訪在時間上的<b>唯一</b>限制。", "s.9(1A), (1B)") + '</tr>',
        '<tr>' + rh("at all reasonable times", "在任何合理時間")
        + d("When <b>you</b> may inspect and copy records that have been taken from you: an investigator or authorized person holding them must permit it, and an officer who removed them under a warrant may. Almost the same phrase, working in your favour.", "指<b>你</b>可於何時查閱及複製被取走的紀錄：管有紀錄的調查員或獲授權人須准許；根據手令移走紀錄的人則可准許。用語與上一行幾乎相同（只差「於」與「在」一字），但此處對你有利。", "s.17(6) · s.19(1)") + '</tr>',
        '<tr>' + rh("as soon as reasonably practicable", "在合理地切實可行範圍內盡快")
        + d("Showing you the authorisation on an inspection; giving you a <b>receipt</b> after taking records away; making an interim report when the Commissioner asks for one; and making the <b>final report</b> once an investigation is finished.", "視察時向你出示授權書；取走紀錄後向你發出<b>收據</b>；關長要求時提交中期報告；以及調查完成後提交<b>最後報告</b>。", "s.9(14) · s.17(5) · s.12(8)(b), (9)") + '</tr>',
        '<tr>' + rh("before first imposing any requirement", "在首次施加任何要求之前")
        + d("An investigator showing you the direction or appointment. Note how much earlier this is than the authorized person's duty above.", "調查員須於此時向你出示指示或委任文本。留意這比上述獲授權人的責任要早得多。", "s.11(5)") + '</tr>',
        '<tr>' + rh("first, before you answer", "事先，在你回答之前")
        + d("The investigator must ensure that you have first been informed or reminded of the limits on using the requirement, the question and your answer as evidence. Your answer is protected only if you claim, before answering, that it might incriminate you.", "調查員須確保你已事先獲告知或提醒，該要求、有關問題及你的回答作為證據的可接納性所受的限制；你須在回答之前聲稱該回答可能會導致你入罪，該回答才受保障。", "s.15(1), (2)(b)") + '</tr>',
        '<tr>' + rh("within the time specified in the requirement", "在該要求所指明的限期內")
        + d("Producing records, and verifying an answer by statutory declaration. The officer writes the deadline, so read it and diarise it.", "交出紀錄，以及以法定聲明核實回答。期限由人員自行訂明，故須細閱並記下。", "s.9(9)–(10) · s.12(2)(a), (4)–(5)") + '</tr>',
        '<tr>' + rh("at the time and place specified", "在指明的時間及地點")
        + d("Attending before an investigator to answer questions in person.", "親身會晤調查員並回答問題。", "s.12(2)(b)") + '</tr>',
        '<tr>' + rh("within the time specified by the Court", "在原訟法庭指明的時間內")
        + d("Complying after the Court of First Instance has ordered you to. Here the Court sets the clock, not the Commissioner.", "原訟法庭命令你遵從後的遵從期限。此處由法庭而非關長訂定時限。", "s.14(2)(a)") + '</tr>',
    ]), minw=640)

CSEC = sec('timing', [("two numbers", "兩個數字"), ("eight standards", "八項標準")],
           ("The clock, and how Part 3 tells the time", "時限，以及第3部如何計算時間"),
    P("Part 3 hardly ever gives you a number. In twenty sections there are exactly <b>two fixed periods</b>, and both are attached to a magistrate's warrant. Everything else is a <b>standard</b>, and the standard is almost always some version of what is reasonable. Learn the two numbers, then learn which standard attaches to which duty, because that is the distinction the paper can test.",
      "第3部極少給出具體數字。二十條之中，只有<b>兩個固定期間</b>，而且都與裁判官手令有關。其餘全部都是<b>標準</b>，而該標準幾乎都是「合理」的某種說法。先記住兩個數字，再記清哪項責任配哪種標準，因為那正是試卷可以考的分別。")
    + f'<figure><div class="figwrap">{tri(fig_clock)}</div>' + U.legend([('may', ("a power someone may exercise over you", "他人可對你行使的權力"))]) + '<figcaption>' + B("Read the two brackets against the axis. The seven days run from the <b>date of the warrant</b>; the records are removed on an entry within those days, and the six months run from the <b>day of removal</b>, not from the end of the seven days. The six months can be exceeded only where the records are or may be required for criminal proceedings or proceedings under the Ordinance, and only for as long as those proceedings need them.",
                                                                          "請對照時間軸閱讀兩個括號。7日自<b>手令日期</b>起計；紀錄在這7日內的一次進入中被移走，而6個月自<b>移走當日</b>起計，並非由7日屆滿時起計。只有在紀錄屬或可能屬刑事法律程序或根據本條例進行的法律程序所需要時，才可超越6個月，並以該等程序所需的期間為限。") + '</figcaption></figure>'
    + '<h3>' + B("The eight time standards, and what each one governs", "八項時間標準，以及各自規管甚麼") + '</h3>'
    + STD
    + numreq([
        (("7 days", "7日"),
         ("The window in which a warrant authorises entry, at any time of day and by force if necessary", "手令授權進入處所的期限，期內可隨時進入，如有必要可強行進入"),
         ("Counted from the date of the warrant, not from when you are told about it", "自手令日期起計，而非自你獲告知時起計"),
         ("Entry after the seventh day is not authorised by that warrant, so ask to see the date on it", "第七日之後進入不獲該手令授權，故應要求查看手令上的日期"),
         "s.17(1)(a)"),
        (("6 months", "6個月"),
         ("The limit on keeping records that have been removed from you", "被移走的紀錄可被保管的上限"),
         ("Counted from the day of removal", "自移走當日起計"),
         ("Beyond six months, records may be kept only if they are or may be required for criminal proceedings or proceedings under the Ordinance, and only for as long as those proceedings need them", "超過6個月後，只有在該紀錄屬或可能屬刑事法律程序或根據本條例進行的法律程序所需要時，方可在該等程序所需的較長期間內予以保留"),
         "s.17(4)"),
        (("the time in the requirement", "要求所指明的限期"),
         ("Produce the records, attend the interview, or verify your answer by statutory declaration", "交出紀錄、出席會晤，或以法定聲明核實你的回答"),
         ("Set by the officer in each written requirement, so it differs every time", "由人員在每份書面要求中訂明，故每次不同"),
         ("Without a reasonable excuse this is an offence: $200,000 and 1 year on indictment. The Court of First Instance route is also available, but contempt-style punishment and prosecution cannot both be used", "如無合理辯解即屬犯罪：循公訴程序定罪可處罰款$200,000及監禁1年。亦可循原訟法庭途徑處理，但猶如藐視法庭罪的懲罰與刑事檢控不可兩者兼用"),
         "s.9(9)–(10) · s.12(2), (4)–(5) · s.10(1) · s.13(1)"),
        (("the time set by the Court", "原訟法庭指明的時間"),
         ("Comply with an order of the Court of First Instance to meet the original requirement", "遵從原訟法庭的命令，履行原來的要求"),
         ("After the authorized person or investigator applies by originating summons and the Court is satisfied there is no reasonable excuse", "獲授權人或調查員藉原訴傳票向原訟法庭提出申請，而法庭信納無合理辯解之後"),
         ("Part 3 says nothing more about this deadline. Separately, on the same application the Court may punish a failure without reasonable excuse as if it were contempt, reaching you and anyone knowingly involved", "第3部對此時限沒有進一步訂明。另外，原訟法庭可在同一申請中，就無合理辯解而沒有遵從的情況，猶如犯藐視法庭罪般懲罰你及明知而牽涉入的任何其他人"),
         "s.14(2)"),
    ]))

# ------------------------------------------------------------------ D. penalties
PEN = table(
    h("What you did", "你做了甚麼") + h("On indictment", "循公訴程序定罪") + h("Summarily", "循簡易程序定罪") + h("Where", "條文"),
    ''.join([
        '<tr>' + d("Failed to comply with a requirement, <b>without reasonable excuse</b>", "<b>無合理辯解</b>而沒有遵從要求")
        + '<td class=\"pen\"><span class=\"answer\" tabindex=\"0\">' + B("$200,000 + 1 year", "罰款$200,000及監禁1年") + '</span></td><td class="pen">' + B("level 5 + 6 months", "第5級罰款及監禁6個月") + '</td>' + d("", "", "s.10(1)–(2) · s.13(1)–(2)") + '</tr>',
        '<tr>' + d("Produced a record or gave an answer that was <b>false or misleading in a material particular</b>, knowing that it was or being reckless as to whether it was", "交出的紀錄或給予的回答<b>在要項上屬虛假或具誤導性</b>，且明知或罔顧實情")
        + '<td class=\"pen\"><span class=\"answer\" tabindex=\"0\">' + B("$1,000,000 + 2 years", "罰款$1,000,000及監禁2年") + '</span></td><td class="pen">' + B("level 6 + 6 months", "第6級罰款及監禁6個月") + '</td>' + d("", "", "s.10(3)–(4) · s.13(3)–(4)") + '</tr>',
        '<tr class="peak">' + d("Did either of the above <b>with intent to defraud</b>, or as an employee or manager caused or allowed someone else to", "<b>出於詐騙意圖</b>作出上述任何一項；或身為僱員或管理層，致使或容許他人作出")
        + '<td class=\"pen\"><span class=\"answer\" tabindex=\"0\">' + B("$1,000,000 + 7 years", "罰款$1,000,000及監禁7年") + '</span></td><td class="pen">' + B("level 6 + 6 months", "第6級罰款及監禁6個月") + '</td>' + d("", "", "s.10(5)–(9) · s.13(5)–(9)") + '</tr>',
        '<tr>' + d("<b>Obstructed</b> an officer exercising powers under a magistrate's warrant to require records, prohibit interference or take steps to preserve them, or <b>without reasonable excuse</b> failed to comply with such a requirement or prohibition", "<b>妨礙</b>根據裁判官手令要求交出紀錄、禁止干擾紀錄或採取步驟保存紀錄的人員，或<b>無合理辯解</b>而沒有遵從該等要求或禁止")
        + '<td class=\"pen\"><span class=\"answer\" tabindex=\"0\">' + B("$1,000,000 + 2 years", "罰款$1,000,000及監禁2年") + '</span></td><td class="pen">' + B("level 6 + 6 months", "第6級罰款及監禁6個月") + '</td>' + d("", "", "s.17(9)–(10)") + '</tr>',
        '<tr>' + d("<b>Destroyed, falsified, concealed or disposed of</b> a record you had been required to produce, meaning to hide what it would show", "<b>銷毀、揑改、隱藏或處置</b>你被要求交出的紀錄，意圖隱瞞其可披露的內容")
        + '<td class=\"pen\"><span class=\"answer\" tabindex=\"0\">' + B("$1,000,000 + 2 years", "罰款$1,000,000及監禁2年") + '</span></td><td class="pen">' + B("level 6 + 6 months", "第6級罰款及監禁6個月") + '</td>' + d("", "", "s.20") + '</tr>',
    ]),
    note=B("The third row reaches your people as well as your company. It catches your <b>related persons</b>: an <b>employee</b>, anyone employed to work for you, and anyone <b>concerned in your management</b> who, with intent to defraud, causes or allows the obligated person to fail, or to produce a false record or give a false answer. Note also that Part 3 sets a <b>cash amount</b> for conviction on indictment but only a <b>fine level</b> for summary conviction, so learn these summary penalties as levels. Contrast the Part 2 fraud offences, where the summary fine is $500,000 (see the <a href=\"#p2-offences\">Part 2 page</a>).",
             "第三行不只涵蓋公司，也涵蓋你的<b>相關人士</b>：包括<b>僱員</b>、受僱為你工作的人，以及任何<b>關涉你的管理</b>的人，如出於詐騙意圖致使或容許義務人不遵從，或交出虛假紀錄或給予虛假回答。另須留意：第3部就公訴程序定罪訂明<b>款額</b>，但就簡易程序定罪只訂明<b>罰款級別</b>，故本部的簡易程序刑罰應按級別記誦；第2部的詐騙罪行則不同，簡易程序罰款為$500,000（見<a href=\"#p2-offences\">第2部一頁</a>）。") + cite_html("s.10(7)–(8), (11) · s.5(6), (8)"),
    minw=740)

DSEC = sec('penalties', [("three tiers", "三級"), ("plus two", "另加兩項")],
           ("What it costs to get this wrong", "違規的代價"),
    P("There are two offence sections, one for each set of powers: s.10 for routine inspections under s.9, and s.13 for investigators under s.12. Their penalty ladders are identical, so learn one ladder and you have both. The jump that matters is the third rung: <b>intent to defraud takes the maximum from two years to seven</b>, while the fine stays where it is.",
      "兩條罪行條文分別對應兩類權力：第10條對應第9條的例行視察，第13條對應第12條的調查員權力。兩者的罰則階梯完全相同，記熟其中一條階梯，兩條皆通。關鍵的跳升在第三級：<b>出於詐騙意圖者，最高刑期由2年升至7年</b>，罰款則維持不變。")
    + PEN
    + U.traps(
        U.trap(("A conviction after an investigation can also carry its costs", "調查後被定罪，可能還要承擔調查費用"),
               ("If an <b>investigation</b> leads to a prosecution and you are convicted, the court may order you to pay the relevant authority all or part of the <b>costs and expenses of the investigation</b>, which it can recover from you as a civil debt. The rule is written into the investigation offence section only; the routine inspection offence section has no such rule.",
                "如<b>調查</b>所得導致你遭檢控並被定罪，法院可命令你向有關當局繳付該項<b>調查的全部或部分費用及開支</b>，而該當局可將之作為拖欠它的民事債項向你追討。此規則只寫在調查的罪行條文中，例行視察的罪行條文並無此規則。"),
               "s.13(12) · s.10")))

# ------------------------------------------------------------------ E. warrants
ESEC = sec('warrants', [("warrants", "手令"), ("seizure", "檢取"), ("and court", "與法庭")],
           ("When they come with a warrant", "當他們持手令到來"),
    P("The first table follows a warrant from the magistrate to the day your files come back. The second holds two rules that apply to any production of records under Part 3, warrant or not, and one that does not reach a warrant at all: the court route, which covers only requirements made on a routine inspection or in an investigation.",
      "第一個表跟隨一張手令，由裁判官簽發直到你的檔案歸還。第二個表載有兩條適用於根據本部交出任何紀錄的規則（不論有沒有手令），以及一條完全不涉及手令的規則：法庭途徑，只涵蓋例行視察或調查中施加的要求。")
    + table(h("Stage", "階段") + h("The rule", "規則"), ''.join([
        '<tr>' + rh("Getting the warrant", "取得手令", "s.17(1)") + d("A <b>magistrate</b>, on information given <b>on oath</b>, must be satisfied there are reasonable grounds to suspect that records which could be demanded under Part 3 are, or are likely to be, on the premises. The oath can come from an investigator, an authorized person, or <b>any employee or staff member</b> of the Commissioner, which is why a warrant belongs to neither track",
                                                                               "<b>裁判官</b>須根據<b>經宣誓</b>作出的告發，信納有合理理由懷疑該處所有或相當可能有本部下可被要求交出的紀錄。作出宣誓者可以是調查員、獲授權人，或關長的<b>任何僱員或員工</b>；因此手令不屬於任何一條途徑") + '</tr>',
        '<tr>' + rh("Getting in", "進入", "s.17(1)") + d("Within <b>7 days</b> of the warrant's date, at any time, <b>by force if necessary</b>, with a police officer and any helpers needed", "自手令日期起計<b>7日內</b>隨時進入，<b>如有必要可強行進入</b>，並可有警務人員及所需協助者同行") + '</tr>',
        '<tr>' + rh("Inside", "處所內", "s.17(1)–(3)") + d("Search for, seize and remove records they reasonably believe could be demanded; require <b>anyone on the premises who works in the business</b>, your counter staff included, to produce records; and <b>prohibit</b> anyone present from removing, erasing, altering or interfering with a record, or take any other step that appears necessary to preserve it or prevent interference with it",
                                                                        "搜尋、檢取及移走他們有合理因由相信本部下可被要求交出的紀錄；要求<b>在場並受僱於該業務的任何人</b>（包括你的櫃位員工）交出紀錄；並<b>禁止</b>在場任何人移走、刪除、更改或干擾紀錄，或採取其覺得屬必需的任何其他步驟，以保存紀錄或防止紀錄受干擾") + '</tr>',
        '<tr>' + rh("Seeing the warrant", "查閱手令", "s.17(7)") + d("They must produce it if you require them to", "如你要求，他們須出示手令") + '</tr>',
        '<tr>' + rh("After removal", "移走之後", "s.17(4)–(5)") + d("A <b>receipt</b> as soon as reasonably practicable; the records kept for up to <b>6 months</b>, or longer if they are or may be required for criminal proceedings or proceedings under the Ordinance, for as long as those proceedings need them", "須在合理地切實可行範圍內盡快發出<b>收據</b>；紀錄可保留不超過<b>6個月</b>；如屬或可能屬刑事法律程序或根據本條例進行的法律程序所需要，可在該等程序所需的較長期間內保留") + '</tr>',
        '<tr>' + rh("Your access", "你的查閱", "s.17(6) · s.19") + U.td("The officer who removed them under the warrant <b>may permit</b> you to inspect and copy them at all reasonable times: s.17(6) itself gives only a discretion. Separately, an investigator or an authorized person holding the Commissioner's written authorisation who has taken possession of records under Part 3 <b>must permit</b> it, subject to any reasonable condition as to security or otherwise", "根據手令移走紀錄的人<b>可准許</b>你在任何合理時間查閱及複製該等紀錄：第17(6)條本身只賦予酌情權。另外，調查員或持關長書面授權的獲授權人如已根據本部管有紀錄，則<b>須准許</b>查閱，但可就保安或其他方面施加合理條件", post=U.flag()) + '</tr>',
        '<tr>' + rh("Getting in their way", "妨礙執行", "s.17(9)–(10)") + d("Obstructing an officer who, under the warrant, is requiring your staff to produce records, prohibiting interference with them or taking steps to preserve them, or failing <b>without reasonable excuse</b> to comply with such a requirement or prohibition, is an offence: $1,000,000 and 2 years on indictment, level 6 and 6 months summarily. The court route is not available here", "妨礙根據手令要求你的員工交出紀錄、禁止干擾紀錄或採取步驟保存紀錄的人員（即手令所授權的人），或<b>無合理辯解</b>而沒有遵從該等要求或禁止，即屬犯罪：循公訴程序定罪，可處罰款$1,000,000及監禁2年；循簡易程序定罪，可處第6級罰款及監禁6個月。此處不適用法庭途徑") + '</tr>',
    ]), minw=680)
    + table(h("Producing records: the wider rules", "交出紀錄：其他規則") + h("The rule", "規則"), ''.join([
        '<tr>' + rh("A lien", "留置權", "s.16") + d("Claiming a lien over a document does not excuse producing it; no fee is payable to you for producing it; and producing it does not destroy the lien", "就文件聲稱有留置權，不能免除你交出文件的責任；交出毋須向你支付費用；而交出亦不會令該留置權失效") + '</tr>',
        '<tr>' + rh("Unreadable records", "無法閱讀的紀錄", "s.18") + d("Whoever can require a record can also require a <b>reproduction in legible form</b> of information that is not recorded in legible form but can be reproduced in it, or, for information held in an information system, a reproduction in a form that can be reproduced legibly", "有權要求交出紀錄的人，如有關資料並非以可閱讀形式記錄但能夠以該形式重現，亦可要求交出<b>以可閱讀形式重現而製成的版本</b>；如資料記錄於資訊系統內，則可要求交出能以可閱讀形式重現的版本") + '</tr>',
        '<tr>' + rh("The court route", "法庭途徑", "s.14") + d("The <b>authorized person or investigator who imposed the requirement</b> may apply to the <b>Court of First Instance</b> by originating summons for an inquiry into the failure. This covers requirements made on a routine inspection or in an investigation, not those made under a warrant. Satisfied there was no reasonable excuse, the Court may order you to comply within a time it sets, and may punish you, and anyone knowingly involved, as if for contempt. For the same conduct, a prosecution and contempt-style punishment exclude each other; an order to comply is not barred",
                                                                        "施加要求的<b>獲授權人或調查員</b>可藉原訴傳票向<b>原訟法庭</b>提出申請，要求對該項不遵從進行查訊。這只涵蓋例行視察或調查中施加的要求，不涵蓋根據手令施加的要求。原訟法庭如信納無合理辯解，可命令你在其指明的時間內遵從，並可懲罰你及明知而牽涉入的任何其他人，猶如犯藐視法庭罪一樣。就同一行為，刑事檢控與猶如藐視法庭罪的懲罰互相排斥；命令遵從則不受此限") + '</tr>',
    ]), minw=680))

# ------------------------------------------------------------------ F. traps
FSEC = sec('traps', [("easy marks", "易失分處"), ("if you read", "只要細讀"), ("carefully", "措辭")],
           ("Nine places the wording turns", "九處措辭的轉折"),
    U.traps(
        U.trap(("A routine visit needs no suspicion at all", "例行到訪毋須任何懷疑"),
               ("An inspection happens simply to check compliance. If an answer says an inspection requires suspicion that an offence has been committed, it is describing an <b>investigation</b>, which is the other track entirely.", "視察只為查核是否遵從規定。若某答案稱視察須先懷疑有罪行，那描述的其實是<b>調查</b>，屬另一條途徑。"), "s.9(1)"),
        U.trap(("Only an investigator can make you sit down", "只有調查員能要求你坐下"),
               ("On a routine inspection, the authorized person can require you to hand over a record at a stated time and place, and to answer questions about it. The power to require a person to <b>attend</b> before the officer exists only in the investigation section.", "在例行視察中，獲授權人可要求你在指明時間及地點交出紀錄，並回答有關問題。要求某人<b>會晤</b>該人員的權力，只見於調查條文。"), "s.12(2)(b)"),
        U.trap(("The last-resort rule applies to one track only", "最後手段規則只適用於一條途徑"),
               ("Making inquiries of an information holder is a <b>last resort during an inspection</b>: the officer must first have reasonable cause to believe you cannot supply it. During an investigation, a person reasonably believed to hold relevant records or information can be required directly.", "在<b>視察</b>中向資料持有人作出查訊屬<b>最後手段</b>：人員須先有合理因由相信你無法提供。在調查中，被合理相信持有相關紀錄或資料的人可被直接要求。"), "s.9(6)–(7) · s.12(1)"),
        U.trap(("Two different moments for showing authority", "出示授權的兩個不同時點"), None, "s.9(14) · s.11(5)",
               vs=[(("An authorized person", "獲授權人"), ("Shows the written authorisation as soon as reasonably practicable while using the power.", "在行使權力期間盡快出示書面授權。")),
                   (("An investigator", "調查員"), ("Shows the direction or appointment before imposing the first requirement: earlier.", "須在施加第一項要求之前出示指示或委任文本：時點較早。"))]),
        U.trap(("You must answer, but the answer can be sealed off", "你必須回答，但回答可獲封存"),
               ("That an answer might incriminate you is <b>no excuse</b> for refusing to comply with an investigator's requirement. The protection is narrower than people expect: only if you claim it <b>before answering</b> do the requirement, the question and the answer become inadmissible against you in criminal proceedings, and even then not if you are charged over that answer itself under s.13 or Part V of the Crimes Ordinance.", "可能導致入罪<b>不能作為</b>拒絕遵從調查員要求的理由。該保障比一般人以為的窄：只有在<b>回答之前</b>作出聲稱，該要求、有關問題及回答才不得在刑事法律程序中接納為針對你的證據；即使如此，若你就該回答本身被控犯第13條或《刑事罪行條例》（第200章）第V部所訂罪行，該保障亦不適用。"), "s.13(11) · s.15"),
        U.trap(("That protection does not cover a routine visit", "該保障不涵蓋例行到訪"),
               ("The protection is written around requirements imposed <b>by an investigator</b>. Nothing you say to an authorized person on a routine inspection is protected by it, and it also falls away if you are charged over the answer itself under s.13 (for example, for a false answer) or under Part V of the Crimes Ordinance.", "該保障是圍繞<b>調查員</b>施加的要求而訂。你在例行視察中向獲授權人所說的話，一律不受保障；若你就該回答本身被控犯第13條所訂罪行（例如給予虛假回答），或《刑事罪行條例》（第200章）第V部所訂罪行，該保障亦不適用。"), "s.15(2)–(3)"),
        U.trap(("Prosecution or contempt-style punishment, not both", "刑事檢控或猶如藐視法庭罪的懲罰，不可兩者兼用"),
               ("For the same conduct, a prosecution and Court of First Instance proceedings to punish you <b>as if for contempt</b> are <b>alternatives</b>, not a sequence. Once one has been started, the other is barred while the first is pending or cannot lawfully be brought again. The bar is written into both the criminal sections and the court section, so it works in either direction. It does <b>not</b> stop the Court from ordering you to comply.", "就同一行為而言，檢控與在原訟法庭以<b>猶如犯藐視法庭罪</b>的方式懲罰你，是<b>二擇其一</b>，並非先後次序：一旦提起其中一項，而該法律程序仍待決或不得再次合法提起，另一項即不得提起。該限制同時寫在刑事條文及法庭條文之中，故雙向適用。但它<b>不</b>妨礙原訟法庭命令你遵從。"), "s.10(10) · s.13(10) · s.14(2), (4)"),
        U.trap(("Breaking a licence condition is breaking the rules", "違反牌照條件即屬違規"),
               ("The standard an authorized person checks you against on a routine inspection is not only the Ordinance. It also covers any notice or requirement given under it, <b>the conditions on your licence</b>, any conditions on a registration, and any other condition imposed under the Ordinance.", "獲授權人在例行視察中用以衡量你的標準，不限於本條例本身，還包括據此給予的任何通知或要求、<b>你牌照上的條件</b>、任何註冊的條件，以及據本條例施加的任何其他條件。"), "s.8"),
        U.trap(("The power to walk in stops at the business premises shown in the register", "進入權力只及於登記冊所顯示的業務處所"),
               ("For a money service operator, business premises means the premises at which you may operate a money service <b>as shown in the register of licensees</b>. The routine inspection power to <b>enter</b> reaches only those premises. It does not shield records kept elsewhere: they can still be inspected, or you can be required to produce them at a place the officer names, and Part 3's other way into premises is a magistrate's warrant.", "就金錢服務經營者而言，業務處所指<b>持牌人登記冊所顯示</b>你可經營金錢服務的處所。例行視察的<b>進入</b>權力只及於該等處所。但這並不保護存放於其他地方的紀錄：該等紀錄仍可被查閱，或你可被要求在人員指明的地點交出；而第3部進入處所的另一途徑是裁判官手令。"), "s.9(1A), (3)–(5), (15) · s.17(1)"),
    ))

P3_NAV = [('tracks', 'Two visits', '兩種到訪'), ('when', 'What applies when', '按情況查閱'), ('timing', 'Timing', '時限'),
          ('penalties', 'Penalties', '刑罰'), ('warrants', 'Warrants', '手令'), ('traps', 'Traps', '陷阱')]
P3_BODY = A + BSEC + CSEC + DSEC + ESEC + FSEC
