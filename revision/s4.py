# AMLO Schedule 4: provisions relating to the Review Tribunal.
from ui import *


def mlabel18(x, y, en, tc, anchor='middle'):
    """ui.mlabel with an 18-unit line pitch, so stacked EN descenders clear the TC line."""
    out = []
    for v, ls in (('en', [en]), ('tc', [tc]), ('both', [en, tc])):
        n = len(ls)
        g = [f'<text class="lbl s-{v}" text-anchor="{anchor}">']
        for i, l in enumerate(ls):
            g.append(f'<tspan x="{x}" y="{y - (n - 1 - i) * 18:.1f}">{esc(l)}</tspan>')
        g.append('</text>')
        out.append(''.join(g))
    return ''.join(out)


def tc_lines(card, lines):
    """Replace a Card's Chinese body with hand-broken lines, and re-size the card to match."""
    body_cls = next(c for _, c, s in card.seg['tc'] if s == card.size)
    card.seg['tc'] = [e for e in card.seg['tc'] if e[2] != card.size] + [(l, body_cls, card.size) for l in lines]
    card.seg['both'] = card.seg['en'] + card.seg['tc']
    card.h = sum(s * LH for _, _, s in card.seg[lay()]) + 16 + (CS * LH if card.cite else 0)


def fig_bench():
    W = 900
    NB = ' '
    SEC = Card(200, 500, ("The Secretary for Financial Services and the Treasury", "財經事務及庫務局局長"),
               ("Appoints the chairperson, the panel, and two ordinary members for each review",
                "委任主席、委員團，以及每項覆核的兩名普通成員"), cite="s.56(1) · s.2(1), 4(1) Sch. 4")
    CH = Card(14, 416, ("The chairperson", "主席"),
              (f"Eligible for appointment as a High Court judge, and not a public officer except as chair of a statutory board or tribunal. Term: up to 3{NB}years, renewable",
               "具資格獲委任為高等法院法官；不屬公職人員（僅憑藉擔任根據條例設立的委員會或審裁處主席而屬公職人員者除外）。任期不超過3年，可再度委任"),
              cite="s.56(2) · s.3 Sch. 4")
    # the automatic wrap splits compounds (根|據, 任|期); break this body between phrases instead
    tc_lines(CH, ["具資格獲委任為高等法院法官；不屬公職人員",
                  "（僅憑藉擔任根據條例設立的委員會或審裁處主席",
                  "而屬公職人員者除外）。任期不超過3年，可再度委任"])
    PAN = Card(470, 416, ("The panel", "委員團"),
               ("People the Secretary considers suitable as ordinary members, none of them public officers, each for whatever term he sets",
                "局長認為適合擔任普通成員的人，全部不得為公職人員，任期由局長訂定"), cite="s.2 Sch. 4")
    # three lines like the chair's body, so the two titles sit level and 任期 stays with 由局長訂定
    tc_lines(PAN, ["局長認為適合擔任普通成員的人，",
                   "全部不得為公職人員，",
                   "任期由局長訂定"])
    ORD = Card(470, 416, ("Two ordinary members, for this review", "兩名普通成員（就本項覆核）"),
               ("Picked from the panel by the Secretary, on the chairperson's recommendation, to act in one specified review",
                "由局長按主席的建議，從委員團中委任，就指明的覆核行事"), cite="s.4 Sch. 4")
    SIT = Card(130, 640, ("Every sitting", "每次聆訊"),
               ("The chairperson and both ordinary members must be present; the chairperson presides; questions are decided by majority, but a question of law by the chairperson alone",
                "主席及兩名普通成員均須出席；由主席主持；問題以過半數票裁定，但法律問題由主席單獨裁定"), 'must', "s.6(3)–(5) Sch. 4", answer=True)
    hrow = max(CH.h, PAN.h)
    CH.h = PAN.h = hrow          # same height, so both arrowheads land level
    two = lay() == 'both'        # the bilingual view stacks each edge label on two lines
    H = place([([SEC], 46), ([CH, PAN], 58 if two else 46), ([ORD], 50), ([SIT], 0)])
    b = [n.render() for n in (SEC, CH, PAN, ORD, SIT)]
    m = 's4b'
    jy = SEC.bottom[1] + 22
    b.append(edge([SEC.bottom, (SEC.cx, jy), (CH.cx, jy), CH.top], mid=m))
    b.append(edge([SEC.bottom, (SEC.cx, jy), (PAN.cx, jy), PAN.top], mid=m))
    b.append(edge([PAN.bottom, ORD.top], mid=m))
    ly = (PAN.bottom[1] + ORD.top[1]) / 2 + (11 if two else 5)
    b.append(mlabel18(PAN.cx - 12, ly, "two are picked for each review", "每項覆核選出兩名", 'end'))
    # the chairperson's recommendation: its own dashed arrow from the chair box to the two members
    dx = CH.x + CH.w - 56
    b.append(f'<polyline class="e e-dash" points="{dx:.0f},{CH.bottom[1]:.0f} {dx:.0f},{ORD.cy:.0f} {ORD.x:.0f},{ORD.cy:.0f}" marker-end="url(#{mref(m)})"/>')
    b.append(mlabel18(dx - 10, (CH.bottom[1] + ORD.cy) / 2 + (12 if two else 5), "recommends", "作出建議", 'end'))
    # both drop straight down: the chair and member columns sit over the sitting box
    b.append(edge([CH.bottom, (CH.cx, SIT.top[1])], mid=m))
    b.append(edge([ORD.bottom, (ORD.cx, SIT.top[1])], mid=m))
    aria = ("How a review bench is formed. The Secretary for Financial Services and the Treasury appoints the chairperson, who must be eligible to be a High Court judge and not a public officer except as chair of a statutory board or tribunal, for renewable terms of up to three years; and appoints a panel of non-public officers. For each review the Secretary, on the chairperson's recommendation, appoints two panel members as ordinary members. At every sitting the chairperson and both ordinary members must be present; the chairperson presides, questions are decided by majority, and questions of law by the chairperson alone.",
            "覆核審裁處的組成。財經事務及庫務局局長委任主席（須具資格獲委任為高等法院法官，並非公職人員（僅因擔任法定委員會或審裁處主席而屬公職人員者除外），每一任期最長三年，可再度委任），並委出由非公職人員組成的委員團。就每項覆核，局長按主席的建議，從委員團委任兩名普通成員。每次聆訊主席及兩名普通成員均須出席；由主席主持，問題以過半數票裁定，法律問題則由主席單獨裁定。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


# The key needs a dashed-line swatch, which legend() has no kind for.
BENCH_KEY = ('<div class="legend">'
             f'<span><i></i>{B("who appoints, and who is appointed", "委任者及獲委任者", True)}</span>'
             f'<span><i class="must"></i>{B("the rule for every sitting", "每次聆訊的規則", True)}</span>'
             '<span><i style="height:0;border:0;border-top:2px dashed var(--text);border-radius:0"></i>'
             f'{B("the chairperson recommends", "主席作出建議", True)}</span></div>')


A = sec('bench', [("Schedule 4", "附表4"), ("with s.55–s.58", "另及第55至58條")],
        ("Who sits on a review", "誰審理覆核"),
    P("Read from the top: one appointing authority, two pools of people, and the three who sit. The dashed arrow is the chairperson's only part in choosing the other two.",
      "由上而下閱讀：一個委任當局、兩批人選，以及三名出席聆訊的人。虛線箭頭是主席在選擇另外兩人時唯一的角色。")
    + fig(fig_bench, ("Schedule 4 has effect because section 58 says so, and the Secretary may amend it by notice in the Gazette. The Secretary may also set up additional tribunals, each run on the same rules.",
                        "附表4因第58條的規定而具有效力，局長可藉憲報公告修訂。局長亦可增設審裁處，每個均按相同規則運作。"),
          BENCH_KEY)
    + table([th("", ""), th("The chairperson", "主席"), th("A panel member", "委員"), th("An ordinary member (sits on one review)", "普通成員（就一項覆核行事）")], [
        tr(rh("Qualification", "資格"), td("Eligible for appointment as a High Court judge", "具資格根據《高等法院條例》獲委任為法官", "s.56(2)"),
           td("Whoever the Secretary considers suitable for appointment as an ordinary member", "局長認為適合獲委任為審裁處普通成員的人", "s.2(1) Sch. 4"),
           td("Must be a panel member: the Secretary appoints 2 for each review, on the chairperson's recommendation", "須為委員：局長按主席的建議，就每項覆核委任2名", "s.4(1) Sch. 4")),
        tr(rh("Public officers?", "可否是公職人員？"), td("Not a public officer, unless only by being chair of a board or tribunal set up under an Ordinance", "不屬公職人員；僅憑藉擔任根據條例設立的委員會或審裁處主席而屬公職人員者除外", "s.56(2)(b)"),
           td("Never", "一律不可", "s.2(1) Sch. 4", post=flag()),
           td("Never, since every ordinary member comes from the panel", "一律不可，因為普通成員均從委員團中委任", "s.2(1), 4(1) Sch. 4")),
        tr(rh("Term", "任期"), td("No more than 3 years, and may be reappointed", "不超過3年，可再度委任", "s.3(1)–(2) Sch. 4"),
           td("Any term the Secretary considers appropriate, and may be reappointed", "局長認為適當的任何期間，可再度委任", "s.2(2)–(3) Sch. 4"),
           td("Appointed to act in a specified review; may be reappointed after that appointment expires", "獲委任就指明的覆核行事；任期屆滿後可獲再度委任", "s.4(2) Sch. 4", post=flag())),
        tr(rh("Resigning", "辭職"), td("Written notice to the Secretary, effective on receipt or on a later date it names", "向局長發出書面通知，於局長接獲之日或通知指明的較後日期生效", "s.3(3)–(4) Sch. 4"),
           td("Written notice to the Secretary", "向局長發出書面通知", "s.2(4) Sch. 4"),
           td("Written notice to the Secretary, effective on receipt or on a later date it names", "向局長發出書面通知，於局長接獲之日或通知指明的較後日期生效", "s.4(3)–(4) Sch. 4")),
        tr(rh("Leaving office", "離任"), td("The Secretary may remove him by written notice if he is no longer qualified, or for incapacity, bankruptcy, neglect of duty, conflict of interest or misconduct", "局長可藉書面通知將主席免任：不再具有資格；或喪失履行職務能力、破產、疏於職守、有利益衝突或行為失當", "s.3(5) Sch. 4"),
           td("The Secretary may remove him by written notice for incapacity, bankruptcy, neglect of duty, conflict of interest or misconduct", "局長可藉書面通知，基於喪失履行職務能力、破產、疏於職守、有利益衝突或行為失當而將委員免任", "s.2(5) Sch. 4"),
           td("Stops being an ordinary member as soon as he stops being a panel member", "停任委員時，即停任普通成員", "s.4(5) Sch. 4")),
        tr(rh("Paid?", "有否酬金？"), td("May be paid a fee the Secretary considers appropriate, charged on general revenue", "可獲付局長認為適當的酬金，由政府一般收入支付", "s.57"),
           td("Not provided for: section 57 covers the chairperson and the other members of the Tribunal, and a panel member becomes one only when appointed as an ordinary member", "未有訂明：第57條只涵蓋審裁處的主席及其他成員，委員須獲委任為普通成員才屬審裁處成員", "s.57 · s.1 Sch. 4"),
           td("May be paid in the same way, as one of the other members of the Tribunal", "作為審裁處的其他成員，同樣可獲付酬金", "s.57")),
    ], minw=860, cls='cmp')
    + numreq([
        (("3 years", "3年"),
         ("The longest single term for a chairperson", "主席每一任期的上限"),
         ("Each appointment or reappointment", "每次委任或再度委任"),
         ("A term cannot exceed it, but the chairperson may be reappointed, and may finish a review already under way when the term ends", "任期不得超過此限，但主席可再度委任；任期屆滿時，亦可繼續完成已展開的覆核"),
         "s.3(1)–(2), 5(1) Sch. 4"),
        (("2 ordinary members", "2名普通成員"),
         ("With the chairperson, the members who must be present at every sitting", "連同主席，每次聆訊必須出席的成員"),
         ("Every sitting, unless the review is being decided by the chairperson alone", "每次聆訊，除非覆核由主席單獨裁定"),
         ("Without them the Tribunal is not properly constituted, except where the chairperson may sit alone", "如他們缺席，審裁處即未妥為組成，但主席可單獨審理的情況除外"),
         "s.56(1) · s.6(3), 9 Sch. 4"),
    ])
    + traps(
        trap(("The Secretary appoints the Tribunal; the Chief Justice appoints only a stand-in for a stay", "審裁處由局長委任；終審法院首席法官只委任處理暫緩執行申請的代任法官"), None, "s.56(1) · s.4(1), 9(5) Sch. 4",
             vs=[(("The Secretary for Financial Services and the Treasury", "財經事務及庫務局局長"),
                  ("Appoints the chairperson, the panel, and the 2 ordinary members for each review (on the chairperson's recommendation).", "委任主席、委員團，以及（按主席的建議）每項覆核的2名普通成員。")),
                 (("The Chief Justice", "終審法院首席法官"),
                  ("Appoints a judge or deputy judge of the Court of First Instance to decide a stay application when the chairperson cannot act, or considers it improper or undesirable to act.", "當主席不能處理暫緩執行申請，或認為由自己處理是不恰當或不可取時，委任原訟法庭法官或暫委法官裁定該申請。"))]),
    ))

# ---------------------------------------------------------------- B. how a sitting runs
B_ = sec('sitting', ["s.6 Sch. 4", "s.10 Sch. 4"],
         ("How a sitting runs", "聆訊如何進行"),
    P("Rules for the room itself. The two that are easiest to reverse carry the marker.",
      "關於聆訊本身的規則。最容易被顛倒的兩項已加上標記。")
    + table([th("Topic", "事項"), th("The rule", "規則")], [
        tr(rh("Convening and directions", "召開聆訊及指示", "s.6(1)–(2) Sch. 4"), td("The chairperson convenes sittings as often as needed, and may at any time after an application arrives give the parties directions on procedure and on time limits for complying", "主席按需要召開聆訊，並可在接獲申請後隨時就程序事宜及遵從時限向各方作出指示")),
        tr(rh("Who must be present", "誰須出席", "s.6(3)–(4) Sch. 4"), td("The chairperson and 2 ordinary members; the chairperson presides", "主席及2名普通成員；由主席主持")),
        tr(rh("How questions are decided", "問題如何裁定", "s.6(5) Sch. 4"), td("By majority of the votes cast by the chairperson and the ordinary members, except that a <b>question of law is decided by the chairperson alone</b>", "由主席及普通成員所投的過半數票裁定，但<b>法律問題由主席單獨裁定</b>", post=flag())),
        tr(rh("In public or in private", "公開或閉門", "s.6(6)–(8) Sch. 4"), td("<b>In public</b> unless the Tribunal decides, on its own initiative or on a party's application, that the interests of justice require a private sitting. An application for a private sitting is itself heard in private", "<b>公開進行</b>，除非審裁處主動或應任何一方的申請，裁定為達致公正須閉門進行。閉門聆訊的申請本身須閉門聆訊", post=flag())),
        tr(rh("Who may speak for a party", "誰可代表一方陳詞", "s.6(9), (11) Sch. 4"), td("The party in person, a corporation through an officer or employee, a partnership through a partner, and the Commissioner through a public officer employed in Customs; or a solicitor or counsel; or anyone else with the Tribunal's leave", "當事人親自陳詞；法團透過高級人員或僱員；合夥透過合夥人；關長透過受僱於香港海關的公職人員；或透過律師或大律師；或在審裁處許可下透過任何其他人")),
        tr(rh("The record", "紀錄", "s.6(10) Sch. 4"), td("The chairperson prepares a record of the proceedings of every sitting", "主席須為每次聆訊擬備程序紀錄")),
        tr(rh("Privileges and immunities", "特權和豁免權", "s.10 Sch. 4"), td("The Tribunal, its members, the parties, witnesses and lawyers have those they would have in civil proceedings in the Court of First Instance", "審裁處、其成員、各方、證人及律師享有的特權和豁免權，與在原訟法庭進行的民事法律程序相同")),
    ], minw=720))

# ---------------------------------------------------------------- C. shortcuts
C_ = sec('shortcuts', ["s.7–s.9 Sch. 4"],
         ("Shortcuts, and what each needs", "簡化程序，以及各自的條件"),
    P("Read the middle column first: it is what unlocks each shortcut. Agreement between the parties is the usual key, and the two applications a chairperson can decide alone are the exception.",
      "先看中間一欄：這是啟動每項簡化程序的條件。雙方同意通常是關鍵；主席可單獨裁定的兩類申請則屬例外。")
    + table([th("The shortcut", "簡化程序"), th("What it needs", "條件"), th("What follows", "結果")], [
        tr(rh("A preliminary conference", "初步會議", "s.7 Sch. 4"),
           td("A direction by the chairperson, on his own initiative or a party's application, <b>but only if the parties agree</b>", "主席主動或應任何一方申請作出指示，<b>但須各方同意</b>"),
           td("The chairperson presides, may give directions and try to get the parties to agree what they reasonably should, then reports to the Tribunal", "由主席主持，可作出指示並設法促使各方達成合理協議，其後向審裁處報告")),
        tr(rh("A consent order", "同意令", "s.8 Sch. 4"),
           td("The parties request and agree to the order, and consent to all of its terms", "各方要求並同意作出該命令，並同意其全部條款"),
           td("The Tribunal or chairperson may make any order it could make, even if other requirements have not been met, and it counts as properly made", "審裁處或主席可作出其有權作出的任何命令，即使其他規定未獲符合，亦視為妥為作出")),
        tr(rh("The chairperson alone decides the whole review", "主席單獨裁定整項覆核", "s.9(1), (3) Sch. 4"),
           td("The parties tell the Tribunal in writing, <b>before any sitting</b>, that they agree to it", "各方<b>在任何聆訊舉行前</b>以書面通知審裁處，表示同意"),
           td("The chairperson sitting alone counts for all purposes as the full Tribunal", "由主席作為審裁處唯一成員構成的審裁處，就所有目的而言，須視為連同2名普通成員構成的審裁處")),
        tr(rh("The chairperson alone decides an application to extend time, or for a stay", "主席單獨裁定延展限期或暫緩執行的申請", "s.9(2), (4) Sch. 4"),
           td("<b>Nothing further</b>: no agreement is needed for these two", "<b>毋須其他條件</b>：這兩類申請毋須各方同意", post=flag()),
           td("After deciding a stay, the chairperson reports the decision and reasons to the Tribunal", "裁定暫緩執行後，主席須向審裁處報告裁定及理由")),
        tr(rh("The chairperson cannot, or considers he should not, hear a stay application", "主席不能或認為不宜處理暫緩執行申請", "s.9(5) Sch. 4"),
           td("Illness, absence from Hong Kong or another cause, or he considers it improper or undesirable to act", "因傷病、不在香港或其他因由而不能執行職能，或主席認為由自己處理是不恰當或不可取的"),
           td("A judge or deputy judge of the Court of First Instance, appointed by the Chief Justice, decides it as if chairperson", "由終審法院首席法官委任的原訟法庭法官或暫委法官，猶如主席般裁定")),
    ], minw=760)
    + traps(
        trap(("Sitting alone: agreement for a review, none for two applications", "單獨審理：覆核須同意，兩類申請則毋須"), None, "s.9(1)–(2) Sch. 4",
             vs=[(("The whole review", "整項覆核"), ("Only if the parties agree in writing before any sitting.", "須各方在任何聆訊前以書面同意。")),
                 (("An extension of time, or a stay", "延展限期或暫緩執行"), ("The chairperson may decide these alone, with no agreement needed.", "主席可單獨裁定，毋須各方同意。"))]),
    ))

# ---------------------------------------------------------------- D. changes mid-review
D_ = sec('changes', ["s.5 Sch. 4", "s.4(5) Sch. 4"],
         ("When people change during a review", "覆核期間的人事變動"),
    P("Two rules decide whether a review survives a change of people.", "兩條規則決定覆核在人事變動後能否繼續。")
    + table([th("What changes", "發生甚麼變動"), th("What happens to the review", "覆核會怎樣")], [
        tr(rh("The chairperson's term ends before the review is decided", "主席任期在覆核裁定前屆滿", "s.5(1) Sch. 4"), td("He may carry on as chairperson for that review until it is decided", "他可繼續擔任該項覆核的主席，直至覆核獲裁定為止")),
        tr(rh("The membership changes during the proceedings", "在程序進行期間成員有變", "s.5(2)–(3) Sch. 4"), td("The proceedings continue <b>only if the parties consent</b>. Otherwise they are discontinued, and may begin anew", "<b>須各方同意</b>，程序方可繼續；否則程序即告終止，但可重新開始", post=flag())),
        tr(rh("An ordinary member stops being a panel member", "普通成員不再是委員", "s.4(5) Sch. 4"), td("He stops being an ordinary member at the same time", "他同時不再是普通成員")),
    ], minw=680))

S4_NAV = [('bench', 'Who sits', '誰審理'), ('sitting', 'How a sitting runs', '聆訊如何進行'),
          ('shortcuts', 'Shortcuts', '簡化程序'), ('changes', 'Changes mid-review', '覆核期間的變動')]
S4_BODY = A + B_ + C_ + D_
