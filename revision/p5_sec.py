# AMLO Part 5: regulation of the operation of money service. The MSO's own Part.
from bl_core import *
from bl_core import _runs
from p5_fig import fig_life, fig_gate, LIFE_KEY, GATE_KEY
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


def LG(p):
    return (f"Licensing Guide ¶{p}", f"《牌照指引》第{_runs(p)}段")


def FPG(p):
    return (f"F&P Guideline ¶{p}", f"《適當人選指引》第{_runs(p)}段")


def cc(*cs):
    """Join several citations into one."""
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


# ---------------------------------------------------------------- A. lifecycle
A = sec('life', [("Part 5", "第5部"), "s.24–s.53", ("your own Part", "你自己的一部")],
        ("The life of your licence", "牌照的一生"),
    P("Read the diagram top to bottom once, then follow the loop on the left. After you apply, the hexagon is the test you have to pass; the red box under the grant lists the duties you have to keep; the bottom row is what can happen next. Only <b>renewal</b>, on the left, keeps the licence, and it sends you back through the same test. The other four take it from you: it expires unrenewed, the Commissioner revokes or suspends it, you stop, or it simply ends. A suspension lasts for a period, or until an event, that the Commissioner specifies, so it takes the licence away for a time rather than ending it.",
      "看圖時先由上而下讀一遍，然後跟着左邊的迴路走。申請後，六角形是你必須通過的測試；批給下方的紅色方格是你必須履行的責任；底部一行是其後可能出現的情況。只有左邊的<b>續期</b>會保留牌照，而續期要你再次通過同一測試。其餘四個方格都會令你失去牌照：沒有續期而期滿失效、關長撤銷或暫時吊銷牌照、你自行停業，或牌照自動失效。暫時吊銷只維持關長指明的一段期間，或直至關長指明的事件發生為止，所以是暫時拿走牌照，而非令牌照終結。")
    + U.fig(fig_life, ("Renewal is not a formality. Section 31(4) applies the whole of section 30(3) and (4) again, so every person who had to be fit and proper at the grant has to be fit and proper again, and the Commissioner may amend, remove or add conditions at that moment.",
                       "續期並非例行公事。第31(4)條再次適用第30(3)及(4)條全部內容，故批給時須屬適當人選的每一個人，續期時仍須是適當人選；關長亦可於此時修改、免除或新增條件。"), LIFE_KEY)
    + numreq([
        (("2 years", "2年"),
         ("How long a licence stays valid once granted", "牌照批給後的有效期"),
         ("From the date of grant, unless the Commissioner sets a different period for your case", "自批給當日起計，除非關長就你的個案另訂期間"),
         ("It simply expires. Carrying on after that is unlicensed operation: $1,000,000 and 2 years on indictment, and the court may disqualify you", "牌照直接期滿。其後繼續經營即屬無牌經營：循公訴程序定罪可處罰款$1,000,000及監禁2年，法庭並可取消你的持牌資格"),
         "s.30(10) · s.29"),
        (("45 days", "45日"),
         ("The latest you may lodge a renewal application, in the specified form and manner and with the Schedule 3 fee", "遞交續期申請的最後限期，須以指明的格式及方式提出，並附隨附表3費用"),
         ("Counted backwards from the day the licence is due to expire", "由牌照期滿之日往前推算"),
         ("Apply in time and, if the licence expires before the Commissioner decides, it stays in force until it is renewed or, if renewal is refused, until the refusal takes effect, unless you withdraw the application or the licence is revoked or suspended under s.34. That protection covers an application made under the section, which means not later than 45 days before expiry",
          "按時申請，而牌照在關長作出決定前期滿，牌照仍然有效，直至獲續期；如續期遭拒絕，則直至拒絕續期的決定生效為止；但如申請被撤回，或牌照根據第34條被撤銷或暫時吊銷，則不在此限。此保障適用於按該條提出的申請，即最遲在期滿前45日提出"),
         "s.31(2)(a)–(c), (10)"),
        (("the day after expiry", "期滿翌日"),
         ("When a renewal takes effect", "續期何時生效"),
         ("The day after the licence expires; if the licence was kept in force while the application was pending, the day after the day it would otherwise have expired", "牌照有效期屆滿之日的翌日；如牌照在申請待決期間仍然有效，則為其本應屆滿之日的翌日"),
         ("Nothing to miss: the renewed licence is then valid for 2 years, or any shorter period the Commissioner determines, beginning on the date it is renewed", "此項無須你遵守：續期牌照其後有效2年，或關長決定的較短期間，自續期生效當日起計"),
         "s.31(11)–(12)"),
        (("more than 25%", "25%以上"),
         ("Makes someone an ultimate owner, who must then be a fit and proper person", "使某人成為最終擁有人，該人因而須是適當人選"),
         ("Partnership: more than 25% of the capital or profits, or of the voting rights. Corporation: more than 25% of the issued share capital (including through a trust or bearer shares), or of the voting rights at general meetings. Either may be held directly or indirectly. Separately, anyone who exercises ultimate control over management is an ultimate owner, whatever the percentage",
          "合夥：資本或利潤、或投票權的25%以上。法團：已發行股本（包括透過信託或持票人股份持有）、或成員大會上投票權的25%以上。直接或間接持有均計算。另外，行使對管理最終的控制權的人，不論所佔百分比，亦屬最終擁有人"),
         ("Becoming one without approval is an offence by that person: level 5 and 6 months. The licensee may also face discipline, and an owner who is no longer fit and proper can cost it the licence", "未經批准而成為最終擁有人，該人即屬犯罪：第5級罰款及監禁6個月。持牌人亦可受紀律處分；最終擁有人不再是適當人選，更可令持牌人失去牌照"),
         "s.24 · s.36(7) · s.43(1)(c) · s.34(1)"),
    ]))

# ---------------------------------------------------------------- C. who needs one
C = sec('scope', ["s.25 · s.29", "s.46–s.48", ("who is in, who is out", "誰適用，誰不適用")],
        ("Who needs a licence, and who is outside Part 5", "誰須領牌，誰不受第5部規管"),
    P("Two tables: what happens to someone who operates without a licence, and who Part 5 leaves out altogether. In the second, read the right-hand column: for most of the list the exemption lasts only while the money service stays ancillary.",
      "兩個表：無牌經營的後果，以及第5部完全不適用的人。第二個表請看右欄：名單上大部分人只有在金錢服務附屬於其主要業務時才獲豁免。")
    + table(h("Operating without a licence", "無牌經營") + h("What follows", "後果"), ''.join([
        '<tr>' + rh("The offence", "罪行", cc("s.29(1)–(2)", LG("2.11"))) + d("On indictment, a fine of <b>$1,000,000 and 2 years</b>; summarily, a fine at <b>level 6 and 6 months</b>. The Licensing Guide states the summary fine as <b>HK$100,000</b>.", "循公訴程序定罪：<b>罰款$1,000,000及監禁2年</b>；簡易程序：<b>第6級罰款及監禁6個月</b>。《牌照指引》把該簡易程序罰款寫作<b>港幣10萬元</b>。") + '</tr>',
        '<tr>' + rh("Disqualification", "取消資格", "s.29(3)") + U.td("The court or magistrate <b>may order</b> that you are disqualified from holding a licence, for a period beginning on the date of the order. It is a separate order, not an automatic result.", "法庭或裁判官<b>可命令</b>取消你持有牌照的資格，期間自命令日期起計。這是獨立命令，並非自動後果。", post=U.flag()) + '</tr>',
        '<tr>' + rh("How it is policed", "如何執法", "s.46–s.48") + d("It is the offence that opens an authorized officer's warrant to enter and search, and the power to arrest without a warrant.", "此罪行可啟動獲授權人員進入搜查的手令，以及無手令拘捕的權力。") + '</tr>',
    ]), minw=640)
    + table(h("Part 5 does not apply to", "第5部不適用於") + h("On what condition", "條件"), ''.join([
        '<tr>' + d("The <b>Government</b>", "<b>政府</b>", "s.25") + d("None: it is outside Part 5 outright", "無條件：全面不適用") + '</tr>',
        '<tr>' + d("An <b>authorized institution</b>, that is, a bank", "<b>認可機構</b>，即銀行", "s.25(a)") + d("None: outright", "無條件：全面不適用") + '</tr>',
        '<tr>' + d("A licensed corporation, an authorized insurer, a licensed insurance broker company, or a licensed individual insurance agent or licensed insurance agency", "持牌法團、獲授權保險人、持牌保險經紀公司，或持牌個人保險代理或持牌保險代理機構", "s.25(b)–(e)") + U.td("Only while the money service is <b>ancillary to its principal business</b>", "只限其金錢服務<b>附屬於其主要業務</b>", post=U.flag()) + '</tr>',
        '<tr>' + d("An SVF licensee", "工具持牌人（即根據《支付系統及儲值支付工具條例》第8F條獲批給牌照的人）", "s.25(f)") + d("The same ancillary test", "同樣須附屬於其主要業務") + '</tr>',
        '<tr>' + d("The system operator or settlement institution of a designated retail payment system", "指定零售支付系統的系統營運者或交收機構", "s.25(g)") + d("Ancillary to its business as system operator or settlement institution", "該服務附屬於其作為系統營運者或交收機構的業務") + '</tr>',
        '<tr>' + d("A stablecoin licensee", "穩定幣持牌人", "s.25(h)") + U.td("Where the money service is a business activity under its stablecoin licence. There is no ancillary test", "其金錢服務屬該持牌人在其穩定幣牌照下的業務活動。此項不設附屬測試", post=U.flag()) + '</tr>',
    ]), minw=640)
    + U.traps(
        U.trap(("A bank is out; a broker may not be", "銀行不適用；經紀則未必"),
               ("The Government and authorized institutions are outside Part 5 whatever they do. Licensed corporations, authorized insurers, licensed insurance broker companies, licensed insurance agents or agencies and SVF licensees are outside only while the money service is ancillary to their principal business. So a company whose principal business is money service needs a licence even if it holds one of those licences. A designated retail payment system operator or settlement institution is outside only while the service is ancillary to that business. A stablecoin licensee is outside where the service is a business activity under its stablecoin licence.",
                "政府及認可機構無論做甚麼都不受第5部規管。持牌法團、獲授權保險人、持牌保險經紀公司、持牌個人保險代理或持牌保險代理機構及工具持牌人，只有在金錢服務附屬於其主要業務時才獲豁免；因此主要業務是金錢服務的公司，即使持有上述牌照，仍須領牌。指定零售支付系統的系統營運者或交收機構，須該服務附屬於其作為系統營運者或交收機構的業務；穩定幣持牌人則須該金錢服務是其在穩定幣牌照下的業務活動。"),
               "s.25(a)–(h)"),
    ))

# ---------------------------------------------------------------- D. fit and proper
FP = table(
    h("If the applicant is", "如申請人是") + h("Who must be fit and proper", "誰須是適當人選") + h("And the test on them is", "對他們的測試標準"),
    ''.join([
        '<tr>' + rh("An individual", "個人", "s.30(3)(a)(i)")
        + d("The individual, and the <b>ultimate owner</b> if there is one.", "該名個人；如有<b>最終擁有人</b>，該擁有人亦須符合。")
        + d("The individual must be fit and proper <b>to operate a money service</b>; the ultimate owner, fit and proper <b>to be associated with</b> the business.", "該名個人須是<b>經營金錢服務</b>的適當人選；最終擁有人則須是<b>與該業務有聯繫</b>的適當人選。") + '</tr>',
        '<tr>' + rh("A partnership", "合夥", "s.30(3)(a)(ii)")
        + d("<b>Each partner</b>, and the ultimate owner if there is one.", "<b>每名合夥人</b>；如有最終擁有人，該擁有人亦須符合。")
        + d("Each partner must be fit and proper <b>to operate</b>; the ultimate owner, <b>to be associated with</b> the business.", "每名合夥人須是<b>經營</b>的適當人選；最終擁有人則須是<b>與該業務有聯繫</b>的適當人選。") + '</tr>',
        '<tr>' + rh("A corporation", "法團", "s.30(3)(a)(iii)")
        + d("<b>Each director</b>, and the ultimate owner if there is one. Note that the corporation itself is not the one tested.", "<b>每名董事</b>；如有最終擁有人，該擁有人亦須符合。留意受測試的並非法團本身。")
        + d("Both are tested as fit and proper <b>to be associated with</b> the business. The <b>to operate</b> wording never applies to a corporation.", "兩者均按<b>與該業務有聯繫</b>的適當人選標準測試。<b>經營</b>一語從不適用於法團。") + '</tr>',
        '<tr class="note"><td colspan="3">'
        + B("<b>Ultimate owner</b> of a <b>corporation</b>: more than <b>25%</b> of the issued share capital (held directly or indirectly, including through a trust or bearer shares), or of the voting rights at general meetings, or <b>ultimate control over the management</b>. Of a <b>partnership</b>: more than 25% of the capital or profits, or of the voting rights, or ultimate control over the management. These two limbs match limb (i) of the Schedule 2 beneficial owner; Schedule 2 adds a limb (ii), 'the person on whose behalf it acts', which Part 5 gives only for an individual licensee. Of an <b>individual</b> licensee there is no percentage: it means another individual who ultimately owns or controls that individual's money service business, or the person the individual acts for.",
            "<b>法團</b>的<b>最終擁有人</b>：直接或間接地擁有或控制（包括透過信託或持票人股份持有）已發行股本的<b>25%以上</b>，或成員大會上投票權的25%以上，或可行使對管理<b>最終的控制權</b>。<b>合夥</b>的最終擁有人：資本或利潤、或投票權的25%以上，或對管理最終的控制權。這兩部分與附表2實益擁有人的第(i)節相同；附表2另有「代表另一人行事時指該另一人」一節，第5部只就個人持牌人設此一節。<b>個人</b>持牌人的最終擁有人則不設百分比：指最終擁有或控制該名個人的金錢服務業務的另一名個人，或該名個人代其行事的人。")
        + ' ' + cite_html("s.24 · s.1 Sch. 2") + '</td></tr>',
    ]), minw=700)

D = sec('fitproper', ["s.30(3)–(4)", "s.24", ("the gate", "入場關卡")],
        ("Fit and proper: who is tested, and on what", "適當人選：誰受測試，測試甚麼"),
    P("The fit and proper test is the spine of Part 5. It decides whether a licence is granted or renewed, whether a new director, partner or owner may join, and whether a licence is revoked or suspended. The section 30(4) list is written into the grant, the renewal and each of the three people approvals; the revocation section asks only whether a person is <b>no longer</b> fit and proper, without repeating the list.",
      "適當人選測試是第5部的骨幹。批給或續期牌照、新董事、合夥人或擁有人可否加入、牌照是否撤銷或暫時吊銷，全部取決於它。第30(4)條的因素明文適用於批給、續期及三項人事批准；撤銷條文只問某人是否<b>不再</b>是適當人選，沒有重複列出這些因素。")
    + FP
    + U.traps(
        U.trap(("'To operate' or 'to be associated with' depends on who is tested, not on the kind of applicant", "「經營」還是「有聯繫」，取決於受測試的是誰，而非申請人屬哪一類"), None, "s.30(3)(a)",
               vs=[(("Fit and proper to operate a money service", "經營金錢服務的適當人選"), ("The individual, where the applicant is an individual; <b>each partner</b>, where it is a partnership.", "申請人屬個人時，該名個人；申請人屬合夥時，<b>每名合夥人</b>。")),
                   (("Fit and proper to be associated with the business", "與經營金錢服務業務有聯繫的適當人選"), ("<b>Each director</b>, where the applicant is a corporation; and <b>any ultimate owner</b>, whether the applicant is an individual, a partnership or a corporation.", "申請人屬法團時，<b>每名董事</b>；以及<b>任何最終擁有人</b>，不論申請人屬個人、合夥還是法團。"))]),
        U.trap(("A listed conviction or bankruptcy is weighed, not an automatic bar", "指明罪行的定罪或破產須予衡量，並非自動禁制"),
               ("The Commissioner <b>must have regard to</b> the section 30(4) matters, in addition to any other matter he considers relevant. An applicant who falls within section 30(4) is scrutinised, but the Commissioner has regard to the facts and circumstances of each applicant before deciding whether he or she is fit and proper.",
                "關長除須考慮其認為有關的任何其他事宜外，亦<b>須顧及</b>第30(4)條所列事宜。屬第30(4)條所指的申請人須經仔細審查，但關長會考慮個別申請人的事實及情況，才斷定其是否適當人選。"),
               cc("s.30(4)", FPG("3"))),
    )
    + '<h3>' + B("The section 30(4) factors, used at grant, renewal and each approval", "第30(4)條的因素，適用於批給、續期及每項批准") + '</h3>'
    + table(h("The Commissioner must have regard to", "關長必須顧及") + h("What that covers", "涵蓋範圍"), ''.join([
        '<tr>' + rh("Convictions in Hong Kong", "香港的定罪紀錄", "s.30(4)(a)") + d("Offences under this Ordinance: sections 5(5) to (8), 10, 13, 17(9), 20(1), 61(2) and 66(3). Section 14 of the United Nations (Anti-Terrorism Measures) Ordinance. Sections 25(1), 25A(5) and (7) of, and the scheduled offences in, the Drug Trafficking (Recovery of Proceeds) and the Organized and Serious Crimes Ordinances",
                                                                                         "本條例所訂罪行：第5(5)至(8)、10、13、17(9)、20(1)、61(2)及66(3)條。《聯合國（反恐怖主義措施）條例》第14條。《販毒（追討得益）條例》及《有組織及嚴重罪行條例》第25(1)、25A(5)及(7)條，以及其附表所指明的罪行") + '</tr>',
        '<tr>' + rh("Convictions outside Hong Kong", "香港以外的定罪紀錄", "s.30(4)(b)") + d("For conduct that would have been one of those offences had it happened in Hong Kong; for any offence relating to money laundering or terrorist financing; or for any offence that needed a finding of fraud, corruption or dishonesty",
                                                                                              "假使在香港作出即構成上述罪行的行為；任何關乎洗錢或恐怖分子資金籌集的罪行；或任何須裁斷該人曾欺詐、舞弊或不誠實行事的罪行") + '</tr>',
        '<tr>' + rh("Compliance record", "遵從紀錄", "s.30(4)(c)") + d("Whether the person has <b>persistently failed</b> to comply with a requirement under the Ordinance or a Part 5 regulation", "該人是否<b>屢次不遵從</b>本條例的規定或第5部的規例") + '</tr>',
        '<tr>' + rh("Solvency", "償債能力", "s.30(4)(d)–(e)") + d("An individual: an undischarged bankrupt, or subject to bankruptcy proceedings. A corporation: in liquidation, subject to a winding up order, or with a receiver appointed", "個人：未獲解除破產，或正受破產法律程序規限。法團：正在清盤、受清盤令規限，或已委任接管人") + '</tr>',
        '<tr>' + rh("Anything else", "其他任何事項", "s.30(4)") + d("The list comes <b>in addition to</b> any other matter the Commissioner considers relevant: a floor, not a ceiling", "上述因素是在關長認為相關的任何其他事項<b>以外</b>另加的：是下限，不是上限") + '</tr>',
    ]), minw=680)
    + '<h3>' + B("The premises test, and the domestic-premises trap", "處所測試，以及住宅處所的陷阱") + '</h3>'
    + table(h("If you apply to operate at particular premises", "如申請在特定處所經營") + h("The rule", "規則"), ''.join([
        '<tr>' + rh("Any premises", "任何處所", "s.30(3)(b)(i)") + d("The Commissioner must be satisfied they are <b>suitable</b> for operating a money service", "關長須信納該處所<b>適合</b>用作經營金錢服務") + '</tr>',
        '<tr>' + rh("Domestic premises", "住宅處所", "s.30(3)(b)(ii)") + d("You must also have the <b>written consent of every occupant</b> for an authorized person to enter and use the section 9 inspection powers", "你亦須已取得<b>每名佔用人的書面同意</b>，讓獲授權人進入並行使第9條的視察權力") + '</tr>',
        '<tr>' + rh("Later on", "其後", "s.34(1)(b)") + U.td("If an occupant <b>revokes</b> that consent, or a <b>new occupant refuses</b> to give it, the Commissioner may revoke or suspend the licence. A new flatmate can cost you the licence", "如佔用人<b>撤回</b>同意，或<b>新佔用人拒絕</b>給予同意，關長可撤銷或暫時吊銷牌照。一名新室友足以令你失去牌照", post=U.flag()) + '</tr>',
    ]), minw=640))

# ---------------------------------------------------------------- E. approvals
E = sec('approvals', ["s.35–s.39", ("ask first", "先申請")],
        ("Five changes that need approval first", "五項須先獲批准的改變"),
    P("Sections 35 to 39 share one shape: the licensee applies, the Commissioner decides, and doing the thing before the answer arrives is an offence carrying a fine at <b>level 5 and 6 months</b>. Only the subject changes.",
      "第35至39條結構相同：由持牌人申請、關長決定；未有答覆前先行其事即屬犯罪，可處<b>第5級罰款及監禁6個月</b>。分別只在對象不同。")
    + U.fig(fig_gate, ("The people gates, sections 35 to 37. The premises gates in sections 38 and 39 follow the same shape, but the test is whether the premises are suitable and, for domestic premises, whether every occupant has consented in writing.",
                       "第35至37條的人事關卡。第38及39條的處所關卡結構相同，但測試的是處所是否適合；如屬住宅處所，則須每名佔用人均已書面同意。"), GATE_KEY)
    + table(h("Section", "條文") + h("Not allowed", "不得") + h("Until", "除非") + h("Penalty", "刑罰"),
        ''.join([
            '<tr>' + rh("35", "35", "s.35")
            + d("A person must not <b>become a director</b> of a corporate licensee", "任何人不得<b>成為</b>法團持牌人的<b>董事</b>")
            + d("The Commissioner has given <b>written approval</b> on the licensee's application, satisfied the person is fit and proper to be associated with the business", "關長應持牌人的申請，信納該人是與該業務有聯繫的適當人選，並已給予<b>書面批准</b>")
            + d("Level 5 (HK$50,000) and 6 months, without reasonable excuse", "第5級罰款（港幣5萬元）及監禁6個月（無合理辯解）", None, 'pen') + '</tr>',
            '<tr>' + rh("36", "36", "s.36")
            + d("A person must not <b>become an ultimate owner</b> of the licensee", "任何人不得<b>成為</b>持牌人的<b>最終擁有人</b>")
            + d("The same written approval on the same test", "同樣須按同一測試取得書面批准")
            + d("Level 5 (HK$50,000) and 6 months", "第5級罰款（港幣5萬元）及監禁6個月", None, 'pen') + '</tr>',
            '<tr>' + rh("37", "37", "s.37")
            + d("A person must not <b>become a partner</b> in a partnership licensee", "任何人不得<b>成為</b>合夥持牌人的<b>合夥人</b>")
            + d("The same approval, but the test is fit and proper <b>to operate</b> a money service", "同樣須取得批准，但測試標準是<b>經營</b>金錢服務的適當人選")
            + d("Level 5 (HK$50,000) and 6 months", "第5級罰款（港幣5萬元）及監禁6個月", None, 'pen') + '</tr>',
            '<tr>' + rh("38", "38", "s.38")
            + d("The licensee must not operate at <b>any premises other than</b> those specified in its licence", "持牌人不得在牌照<b>指明處所以外</b>的任何處所經營")
            + d("The Commissioner has <b>added the new premises</b> to the licence, on payment of the Schedule 3 fee, satisfied they are suitable and, if domestic, consented to", "關長在收取附表3費用後，信納處所適合（如屬住宅處所並已取得同意），並已將新處所<b>加入牌照</b>")
            + d("Level 5 (HK$50,000) and 6 months", "第5級罰款（港幣5萬元）及監禁6個月", None, 'pen') + '</tr>',
            '<tr>' + rh("39", "39", "s.39")
            + d("The licensee must not operate at <b>particular premises</b> when its licence does not tie it to any", "持牌人不得在牌照並未指明處所的情況下，於<b>特定處所</b>經營")
            + d("The Commissioner has added those premises to the licence on the same conditions", "關長已按同樣條件將該處所加入牌照")
            + d("Level 5 (HK$50,000) and 6 months", "第5級罰款（港幣5萬元）及監禁6個月", None, 'pen') + '</tr>',
        ]),
        note=B("For sections 35 to 37 the offender is the person who takes office without approval; the licensee may also face discipline under section 43(1)(c). For sections 38 and 39 the offence is the licensee's own. The dollar figures are the Licensing Guide's; the Ordinance states each penalty as level 5. After granting an application under section 38 or 39 the Commissioner must, as soon as reasonably practicable, add or amend the premises particulars in the register. For the inspection power in section 9 (Part 3), an MSO's business premises are the premises shown in that register.",
               "第35至37條的犯罪者是未獲批准而就任的人；持牌人亦可根據第43(1)(c)條受紀律處分。第38及39條的罪行則由持牌人本身觸犯。上列金額取自《牌照指引》；條例把每項刑罰寫作第5級罰款。關長批准第38或39條的申請後，須在合理地切實可行範圍內，盡快在登記冊加入或修訂有關詳情。就第3部第9條的視察權力而言，持牌金錢服務經營者的業務處所，即登記冊所示可經營金錢服務的處所。") + ' ' + cite_html(cc("s.35(7) · s.38(8) · s.43(1)(c)", LG("8.5–8.9"), "s.38(7) · s.39(7) · s.9(15)")), minw=780))

# ---------------------------------------------------------------- F. duties
F = sec('duties', ["s.39A–s.41", "s.27–s.28 · s.33 · s.52", ("while you hold it", "持牌期間")],
        ("What you owe while you hold the licence", "持牌期間你的責任"),
    P("The first table is every running duty with its clock and its penalty. The second is what the licence itself must show, and the public register, which the Commissioner keeps but which decides what others can prove about you.",
      "第一個表列出每項持續責任及其時限和罰則。第二個表是牌照本身須載明的內容，以及公開登記冊：登記冊由關長備存，但它決定了別人可以證明你甚麼。")
    + numreq([
        (("at all times", "任何時候"),
         ("Display the <b>original</b> of the licence in a conspicuous place, not a copy", "在顯眼地方展示牌照<b>正本</b>，而非複本"),
         ("Whenever you are licensed to operate at premises specified in the licence", "凡你獲准在牌照指明的處所經營期間"),
         ("An offence without reasonable excuse: a fine at level 5, with no imprisonment", "如無合理辯解即屬犯罪：第5級罰款，不設監禁"),
         "s.39A"),
        (("1 month", "1個月"),
         ("Notify the Commissioner in writing of any change in the particulars you gave with your application, or notified since", "以書面向關長具報申請時所提供或其後具報的詳情的任何改變"),
         ("From the date the change takes place, not from when you notice it", "自改變發生之日起計，而非自你察覺時起計"),
         ("An offence without reasonable excuse: a fine at level 5, which the Licensing Guide states as HK$50,000", "如無合理辯解即屬犯罪：第5級罰款，《牌照指引》寫作港幣5萬元"),
         cc("s.40(1)–(2), (4)", LG("9.3"))),
        (("before the date", "停業日期之前"),
         ("Notify in writing your intention to cease, and the date", "以書面具報停業意向及日期"),
         ("Before you stop operating, entirely or at some of your premises", "在你全面停業或停止在部分處所經營之前"),
         ("An offence without reasonable excuse: a fine at level 5 (HK$50,000 in the Licensing Guide)", "如無合理辯解即屬犯罪：第5級罰款（《牌照指引》寫作港幣5萬元）"),
         cc("s.41(1)(a), (4)", LG("10.4"))),
        (("7 days", "7日"),
         ("Return the licence for cancellation or amendment", "交回牌照以作取消或修訂"),
         ("Within 7 days beginning on the date of cessation itself", "在自停業日期起計的7日內"),
         ("An offence without reasonable excuse: a fine at level 5. If the licence is returned for cancellation, no licence fee paid for its grant or renewal is refunded", "如無合理辯解即屬犯罪：第5級罰款。如牌照交回以作取消，已就該牌照的批給或續期繳付的牌照費不予退回"),
         "s.41(1)(b), (3)–(4)"),
        (("no number", "不涉數字"),
         ("Do not make a statement that is false or misleading in a material particular, or omit a material particular from a statement so that it becomes false or misleading, in connection with a grant or renewal application", "在與批給或續期申請有關連的情況下，不得作出在要項上屬虛假或具誤導性的陳述，亦不得在陳述中遺漏任何要項，以致該陳述成為虛假或具誤導性"),
         ("When you knew, or were reckless as to whether, it was false or left out", "你明知或罔顧其是否虛假或遺漏"),
         ("An offence: a fine at level 5 and 6 months. The Licensing Guide, on an omitted premises (s.52(2)), states the fine as up to HK$50,000", "即屬犯罪：第5級罰款及監禁6個月。《牌照指引》就漏填處所（第52(2)條）把罰款寫作最高港幣5萬元"),
         cc("s.52", LG("4.9"))),
    ], heading=False)
    + table(h("The licence and the register", "牌照及登記冊") + h("The rule", "規則"), ''.join([
        '<tr>' + rh("What the licence shows", "牌照須載明甚麼", "s.33") + d("It is in a form the Commissioner specifies, and must give the address of every premises where you may operate (or, if you are not tied to premises, your correspondence address), be endorsed with the conditions imposed or amended under sections 30, 31 or 32, and state the period for which it is valid", "牌照須採用關長指明的格式，並須指明你可經營金錢服務所在的每一個處所的地址（如屬任何其他情況，則為你的通訊地址）、批註根據第30、31或32條施加或修改的條件，並指明牌照的有效期") + '</tr>',
        '<tr>' + rh("What the register holds", "登記冊載有甚麼", "s.27(1)–(2)") + d("Every licensee's name, and either every premises address or, for a licensee not tied to premises, a correspondence address. Kept at the Commissioner's office, in any form he thinks fit", "每名持牌人的姓名或名稱，以及其可經營金錢服務的每一個處所的地址；如屬任何其他情況，則為該持牌人的通訊地址。由關長以其認為合適的形式在其辦事處備存") + '</tr>',
        '<tr>' + rh("Who may look", "誰可查閱", "s.27(3)–(4)") + d("The public, <b>free of charge</b> during normal office hours, so anyone can check they are dealing with a licensee", "公眾可在正常辦公時間內<b>免費</b>查閱，以核實對方是否持牌人") + '</tr>',
        '<tr>' + rh("A certified copy", "核證複本", "s.28(2)–(3)") + d("Admissible without further proof and <b>evidence</b> of what it states; a name missing from it is evidence the person was not licensed on the date the copy was certified", "毋須進一步證明即獲接納，並屬所述事實的<b>證據</b>；複本上沒有某人的姓名或名稱，即可作為證據，證明該人在該複本經核證當日並沒有獲批給牌照") + '</tr>',
        '<tr>' + rh("The Commissioner's certificate", "關長的證明書", "s.28(4)") + U.td("That a name was entered, removed or never entered: <b>conclusive evidence</b>", "述明姓名或名稱曾記入、已刪除或從未記入：屬<b>確證</b>", post=U.flag()) + '</tr>',
    ]), minw=640))

# ---------------------------------------------------------------- G. losing it
G = sec('losing', ["s.30–s.34", "s.41 · s.42", ("how it ends", "如何終結")],
        ("Changing the terms, and the ways it ends", "條件的更改，以及牌照終結的方式"),
    P("Each row is one way a licence changes or ends. Compare the columns: what triggers it, when it takes effect, and whether the Review Tribunal is open to you.",
      "每一行是牌照改變或終結的一種方式。比較各欄：觸發條件、生效時間，以及可否向覆核審裁處申請覆核。")
    + table(h("What happens", "發生甚麼") + h("Trigger", "觸發條件") + h("Takes effect", "生效時間") + h("Fee refunded?", "費用退還？") + h("Review?", "可否覆核？"), ''.join([
        '<tr>' + rh("Conditions changed mid-term", "有效期內更改條件", "s.32")
        + d("The Commissioner is satisfied it is <b>reasonable in the circumstances</b>; written notice with reasons", "關長信納在有關情況下屬<b>合理</b>；以書面通知並載明理由")
        + d("On receipt of the notice, or the time it specifies, whichever is later", "收到通知時或通知指明的時間，以較遲者為準")
        + d("—", "—") + d("Yes", "可以", "s.54") + '</tr>',
        '<tr>' + rh("Revoked or suspended", "撤銷或暫時吊銷", "s.34")
        + d("Someone who had to be fit and proper <b>no longer is</b>, or consent to enter <b>domestic premises</b> is revoked or refused. A reasonable opportunity to be heard comes first. The Licensing Guide gives a longer, non-exhaustive list of examples, such as a periodic return not submitted on time: see the <a href=\"#gl-endings\">Guidelines page</a>", "本須屬適當人選的人<b>不再</b>是適當人選，或<b>住宅處所</b>的進入同意被撤回或拒絕給予。須先給予合理的陳詞機會。《牌照指引》另列出並非詳盡無遺的例子，例如未能按時遞交定期申報表：見<a href=\"#gl-endings\">指引頁</a>", cc("s.34(1), (3)", LG("7.1–7.2")))
        + U.td("At the time the notice specifies; the notice also sets a suspension's terms, or the time to surrender a revoked licence", "在通知指明的時間；通知亦須載明吊銷的條款，或撤銷後交回牌照的期限", post=U.flag())
        + d("No; and failing to surrender a revoked licence is an offence at level 5", "不退還；沒有交回已撤銷的牌照即屬犯罪，可處第5級罰款")
        + d("Yes", "可以", "s.54") + '</tr>',
        '<tr>' + rh("Not renewed", "不獲續期", "s.31")
        + d("The renewal application fails the same fit and proper and premises tests as a new application", "續期申請未能通過與新申請相同的適當人選及處所測試")
        + U.td("If you applied in time, the licence stays in force past its expiry until the refusal takes effect, unless you withdraw the application or the licence is revoked or suspended", "如你按時申請，牌照在期滿後仍然有效，直至拒絕續期的決定生效為止；但如申請被撤回，或牌照被撤銷或暫時吊銷，則不在此限", post=U.flag())
        + d("—", "—") + d("Yes", "可以", "s.54") + '</tr>',
        '<tr>' + rh("It expires", "期滿失效", "s.30(10) · s.31(12)")
        + d("No renewal application made under section 31. One lodged later than 45 days before expiry does not count, and the Licensing Guide treats it as invalid. It also treats a renewal as invalid if requested documents are not produced within the specified period, or no eligible person is nominated for the Assessment within 7 days of receiving the invitation letter, which comes with the renewal reminder sent 90 days before expiry", "沒有根據第31條提出續期申請。遲於期滿前45日才遞交的申請不算在內，《牌照指引》視之為無效申請。如未有在指明期限內遞交所需文件，或未有在接獲邀請信當日起計7日內提名合資格人士應考能力評核，《牌照指引》亦視該續期申請為無效；邀請信夾附於期滿前90日發出的續期提示通知", LG("6.2–6.4"))
        + d("When its validity period runs out; trading on is unlicensed operation. The Licensing Guide treats expiry as a cessation: notify before it and return the expired licence within 7 days (see the <a href=\"#gl-renewal\">Guidelines page</a>)", "有效期屆滿時即失效；其後繼續經營即屬無牌經營。《牌照指引》把期滿視作停業：須在期滿前具報，並在7日內交回已屆滿的牌照（見<a href=\"#gl-renewal\">指引頁</a>）", cc("s.31(2)(a)", LG("10.2")))
        + d("—", "—") + d("No: it is not a decision", "不可以：這不是決定") + '</tr>',
        '<tr>' + rh("You stop", "你停業", "s.41")
        + d("Your own decision, notified in writing before the date of cessation", "你自己的決定，須在停業日期前書面具報")
        + d("From the date of cessation; return the licence within 7 days beginning on that date", "自停業日期起；須在自停業日期起計的7日內交回牌照")
        + d("No, if it is returned for cancellation", "如交回以作取消，則不退還", "s.41(3)") + d("Nothing to review", "無可覆核") + '</tr>',
        '<tr>' + rh("It simply ends", "自動失效", "s.42")
        + d("An individual dies; a partnership dissolves; a corporation's winding up commences", "個人去世；合夥解散；法團開始清盤")
        + d("At that moment, with no decision, notice or hearing", "即時失效，毋須任何決定、通知或聆訊")
        + d("—", "—") + d("No: it is not a decision", "不可以：這不是決定") + '</tr>',
    ]), minw=860))

# ---------------------------------------------------------------- H. enforcement
H_ = sec('enforce', ["s.43–s.48", "s.26 · s.50–s.53", ("the sharp end", "執法一端")],
         ("Discipline for licensees; warrants and arrest for the unlicensed", "持牌人受紀律處分；無牌者面對手令及拘捕"),
    P("Read the second column first. Section 43 is aimed at licensees that breach a regulation, a licence condition or a Part 5 duty; sections 47 and 48 at people operating without a licence.",
      "先看第二欄。第43條針對違反規例、牌照條件或第5部責任的持牌人；第47及48條則針對在沒有牌照的情況下經營金錢服務的人。")
    + table(h("Power", "權力") + h("Aimed at", "針對") + h("What it allows", "可以做甚麼") + h("The limits", "限制"), ''.join([
        '<tr>' + rh("Discipline", "紀律行動", "s.43–s.45")
        + d("A <b>licensee</b> that breaches a Part 5 regulation, a licence condition, or sections 35(1) to 41(1)", "違反第5部規例、牌照條件或第35(1)至41(1)條的<b>持牌人</b>")
        + d("Public reprimand, a remedial order, a penalty of up to <b>$1,000,000</b>, and up to <b>$10,000 a day</b> while a remedial order is ignored", "公開譴責、糾正命令、最高<b>$1,000,000</b>的罰款；不遵從糾正命令期間，另可命令繳付每日最高<b>$10,000</b>的罰款")
        + d("A reasonable opportunity to be heard first; a written notice with reasons and the Tribunal statement; penalty guidelines published before first use", "須先給予合理的陳詞機會；書面通知須載明理由及覆核審裁處的提示；首次施加罰款前須公布指引") + '</tr>',
        '<tr>' + rh("Authorized officers", "獲授權人員", "s.46")
        + d("Staffing the two powers below", "執行下列兩項權力的人員")
        + d("The Commissioner appoints them in writing from public officers employed in the Customs and Excise Department", "由關長從受僱於香港海關的公職人員中以書面委任")
        + U.td("Not the same as Part 3's <b>authorized person</b>, who is authorised under section 9(12) and may come from outside Customs", "與第3部的<b>獲授權人</b>不同：後者根據第9(12)條獲授權，可以是海關以外的人", post=U.flag()) + '</tr>',
        '<tr>' + rh("Warrant", "手令", "s.47")
        + d("Suspected <b>unlicensed operation</b> on the premises", "懷疑該處所有<b>無牌經營</b>")
        + d("A magistrate, on information on oath, authorises entry and search, by force if needed; seizure of records, documents, <b>cash</b> and other evidence; and detaining anyone on the premises who may have relevant information until the search is done", "裁判官根據經宣誓而作的告發，授權進入及搜查（如有需要可強行進入）；檢取紀錄、文件、<b>現金</b>及其他證據；並可扣留在場可能掌握相關資料的人，直至搜查完畢")
        + d("Obstructing the officer is an offence: level 6 and 6 months", "妨礙該人員即屬犯罪：第6級罰款及監禁6個月") + '</tr>',
        '<tr>' + rh("Arrest", "拘捕", "s.48")
        + d("Reasonable grounds to suspect <b>unlicensed operation</b>", "有合理理由懷疑<b>無牌經營</b>")
        + d("Arrest without a warrant, or detain for further enquiries; reasonable force against forcible resistance", "可無手令拘捕或扣留以作進一步查訊；如遭強行反抗，可使用合理武力")
        + d("Show evidence of appointment if asked; a search of the person only by an officer of the same sex; no one held more than <b>48 hours</b> without being charged and brought before a magistrate", "如被要求須出示委任證明；搜身只可由同性人員進行；任何人不得被扣留超過<b>48小時</b>而不予落案起訴及帶到裁判法院") + '</tr>',
        '<tr>' + rh("Regulations and fees", "規例及費用", "s.50–s.51 · s.26(2)")
        + d("The rules and prices of the Part 5 regime", "第5部制度的規則及收費")
        + d("The Commissioner of Customs and Excise may make Part 5 regulations, and the Commissioner may amend the Schedule 3 fees by notice in the Gazette", "海關關長可訂立第5部規例；關長可藉憲報公告修訂附表3的費用")
        + U.td("Making regulations is one of only two functions that can <b>never</b> be delegated; amending the fees can be delegated", "訂立規例是<b>絕不可</b>轉授的兩項職能之一；修訂費用則可以轉授", post=U.flag()) + '</tr>',
    ]), minw=900)
    + numreq([
        (("$1,000,000", "$1,000,000"),
         ("The ceiling on a Part 5 disciplinary penalty", "第5部紀律處分罰款的上限"),
         ("You broke a regulation, a licence condition, or one of the duties in sections 35 to 41", "你違反規例、牌照條件，或第35至41條所訂的責任"),
         ("Payable within 30 days (or any longer period the Commissioner specifies) after it takes effect; on the Commissioner's application the Court of First Instance may register it, and it then counts as a civil order of that Court for payment of money", "須在生效後30日（或關長指明的較長期間）內繳付；原訟法庭可應關長申請登記該命令，登記後視為原訟法庭在民事司法管轄權範圍內作出的繳付款項命令"),
         "s.43(2)(c), (3), (5)"),
        (("up to $10,000 a day", "每日最高$10,000"),
         ("A further daily penalty the Commissioner may order if a remedial order is not complied with", "糾正命令未獲遵從時，關長可進一步命令繳付的按日罰款"),
         ("For each day the failure continues after the date by which the remedial action was due", "命令指明的採取糾正行動期限後，未遵從狀況持續的每一日"),
         ("If ordered, payable for each day of continued non-compliance, separate from any penalty under s.43(2)(c)", "如關長作出命令，須就持續未遵從的每一日繳付不超逾$10,000的按日罰款，與根據第43(2)(c)條判處的罰款分開計算"),
         "s.43(4)"),
        (("48 hours", "48小時"),
         ("The longest anyone arrested or detained under s.48 may be held without being charged", "根據第48條被拘捕或扣留的人，在未被落案起訴前可被扣留的上限"),
         ("After an authorized officer arrests or detains you on suspicion of unlicensed operation", "獲授權人員因懷疑你無牌經營而將你拘捕或扣留之後"),
         ("You may not be held beyond it unless charged and brought before a magistrate", "除非已被落案起訴及帶到裁判法院應訊，否則不得被扣留超過此時限"),
         "s.48(4)"),
        (("12 months", "12個月"),
         ("The window for prosecuting a Part 5 offence that is not indictable", "檢控第5部非可公訴罪行的期限"),
         ("From when the Commissioner discovers the offence or it comes to his notice, not from when you committed it", "自關長發現或知悉該罪行時起計，而非自你作出該行為時起計"),
         ("Once it passes, proceedings for that offence can no longer be instituted", "期限屆滿後，即不能再就該罪行提起法律程序"),
         "s.53"),
    ]))

# ---------------------------------------------------------------- I. traps
I_ = sec('traps', [("contrasts", "對照"), ("worth marking", "值得標記")],
         ("Where Part 5 catches people out", "第5部容易失分之處"),
    U.traps(
        U.trap(("Two years on grant; two years or less on renewal", "批給兩年；續期兩年或更短"), None, "s.30(10) · s.31(12)",
               vs=[(("A new licence", "新牌照"), ("Valid for 2 years, or any <b>other</b> period the Commissioner considers appropriate, longer or shorter.", "有效期2年，或關長認為適當的任何<b>其他</b>期間，可長可短。")),
                   (("A renewed licence", "續期牌照"), ("Valid for 2 years, or any <b>shorter</b> period the Commissioner determines. Never longer.", "有效期2年，或關長決定的任何<b>較短</b>期間。絕不會較長。"))]),
        U.trap(("45 days before, and the licence survives the wait", "期滿前45日，牌照在等待期間仍然有效"),
               ("Apply not later than 45 days before expiry. If the licence expires while the Commissioner is still deciding, it stays in force until the renewal is granted or, if refused, until the refusal takes effect, unless the application is withdrawn or the licence is revoked or suspended under s.34.",
                "須於期滿前45日或之前申請。如牌照在關長作出決定前期滿，除非續期申請被撤回，或牌照根據第34條被撤銷或暫時吊銷，否則它會持續有效，直至續期獲批給；如被拒絕，則直至拒絕續期的決定生效為止。"),
               "s.31(2)(a), (10)"),
        U.trap(("One month for changes, seven days for the licence", "改變一個月，交回牌照七日"), None, "s.40 · s.41",
               vs=[(("A change of particulars", "詳情改變"), ("Notify in writing within one month beginning on the date the change takes place.", "在自改變發生之日起計的一個月內，藉書面具報。")),
                   (("Ceasing business", "停業"), ("Notify the Commissioner in writing before the date of cessation, then return the licence within 7 days beginning on the date of cessation.", "在停業日期前藉書面向關長具報，並在自停業日期起計的7日內將牌照交回關長。"))]),
        U.trap(("Levels in the Ordinance, dollars in the Licensing Guide", "條例寫級別，《牌照指引》寫金額"),
               ("The Ordinance states the Part 5 fines (other than the $1,000,000 on indictment) as levels; the Licensing Guide states the same offences in dollars. Level 5 appears there as <b>HK$50,000</b>: unapproved directors, owners, partners and premises, a late change notice, a missed cessation duty, and an omitted particular. Level 6 appears as <b>HK$100,000</b>: operating without a licence, tried summarily.",
                "條例把第5部的罰款（循公訴程序定罪的$1,000,000除外）寫作級別；《牌照指引》則把同一罪行寫作金額。第5級在指引中寫作<b>港幣5萬元</b>：未經批准的董事、擁有人、合夥人及處所、逾期具報詳情改變、違反停業責任，以及遺漏要項。第6級寫作<b>港幣10萬元</b>：循簡易程序定罪的無牌經營。"),
               cc(LG("2.11"), LG("4.9"), LG("8.5–8.9"), LG("9.3"), LG("10.4"))),
        U.trap(("A corporation is never the one tested", "法團本身從不受測試"),
               ("Where the applicant is a corporation, what is tested is each director and any ultimate owner, both as fit to be associated with the business. The words fit and proper to operate a money service apply only to an individual applicant and to partners.",
                "如申請人是法團，受測試的是每名董事及任何最終擁有人，標準都是是否適合與該業務有聯繫。「經營金錢服務的適當人選」這個標準只適用於屬個人的申請人及合夥人。"),
               "s.30(3)(a)"),
        U.trap(("Evidence, or conclusive evidence", "證據，還是確證"), None, "s.28(2), (4)",
               vs=[(("A certified copy of the register", "登記冊的核證複本"), ("Evidence of what it states.", "屬所述事實的證據。")),
                   (("The Commissioner's signed certificate", "關長簽署的證明書"), ("Conclusive evidence.", "屬確證。"))]),
        U.trap(("Conditions and revocation do not wait for the 21 days", "條件及撤銷不等待21日"),
               ("A condition takes effect when you receive the notice, or later if the notice says so, and a revocation or suspension at the time the notice specifies. Applying to the Review Tribunal does not by itself pause them.",
                "條件在你收到通知時生效（如通知另定較後時間則按該時間），撤銷或暫時吊銷則在通知指明的時間生效。向覆核審裁處申請本身並不會令它們暫停。"),
               "s.30(7) · s.32(4) · s.34(6) · s.69(1)"),
    ))

P5_NAV = [('life', 'Lifecycle', '生命周期'), ('scope', 'Who needs one', '誰須領牌'),
          ('fitproper', 'Fit and proper', '適當人選'), ('approvals', 'Approvals', '批准'), ('duties', 'Your duties', '你的責任'),
          ('losing', 'Changes and endings', '更改與終結'), ('enforce', 'Enforcement', '執法'), ('traps', 'Traps', '陷阱')]
P5_BODY = A + C + D + E + F + G + H_ + I_
