# Assemble the AMLO revision pack: Parts 1 to 7 and Schedules 1 to 4, one page each,
# with a grouped document switcher at the top and a floating chapter outline.
# Adding a page means writing its content module and adding one DOCS entry.
import importlib
import io
import os
import re
import sys
import bl_core
from bl_core import B, P, esc, cite_html
from s2page import S2_BODY, S2_NAV
from p1 import P1_BODY, P1_NAV
from p2 import P2_BODY, P2_NAV
from p3_sec import P3_BODY, P3_NAV
from p4_sec import P4_BODY, P4_NAV
from p5_sec import P5_BODY, P5_NAV
from p6 import P6_BODY, P6_NAV
from p6a import P6A_BODY, P6A_NAV
from p7 import P7_BODY, P7_NAV
from s1 import S1_BODY, S1_NAV
from s3 import S3_BODY, S3_NAV
from s4 import S4_BODY, S4_NAV
from gl import GL_BODY, GL_NAV
from ci import CI_BODY, CI_NAV, CI_FOOT

SP = os.path.dirname(os.path.abspath(__file__))
# python revision/pack_build.py [output.html]; the default is revision/mso-revision-pack.html, which review/ reads
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(SP, 'mso-revision-pack.html')

CAP = "Anti-Money Laundering and Counter-Terrorist Financing Ordinance, Cap. 615, consolidated version as at 15 May 2026"
CAP_TC = "《打擊洗錢及恐怖分子資金籌集條例》（第615章）2026年5月15日綜合版"

DOCS = [
    dict(key='p1', group='part', tab=("1", "1"), short=("Part 1 · Preliminary", "第1部 · 導言"),
         eyebrow=("AMLO Cap. 615 · Part 1, sections 1 to 4 · Module 2", "《打擊洗錢條例》第615章 · 第1部第1至4條 · 單元二"),
         title=("AMLO Part 1 Preliminary", "《打擊洗錢條例》第1部：導言"),
         lede=("Part 1 is four sections long, but it wires the Ordinance together: it makes Schedule 1 the home of the Ordinance's shared definitions, applies the Ordinance to the Government, and protects anyone who performs its functions in good faith from civil liability. This page opens with a map of the whole Ordinance, so each later Part and Schedule has somewhere to sit.",
               "第1部只有四條，卻把整條條例連繫起來：它以附表1載列整條條例通用的釋義，令條例適用於政府，並使真誠執行職能者免負民事法律責任。本頁以整條條例的結構圖開始，讓其後每一部及每個附表都有所歸屬。"),
         nav=P1_NAV, body=P1_BODY,
         foot=(f"Drawn from Part 1, sections 1 to 4, of the {CAP}, with the amendment and rule-making powers in sections 6, 7, 23, 45, 50, 51, 58, 76 and 77, and the limits on delegation in section 26.",
               f"取材自{CAP_TC}第1部（第1至4條），以及第6、7、23、45、50、51、58、76及77條有關修訂及訂立規則的權力，和第26條有關轉授職能的限制。")),
    dict(key='p2', group='part', tab=("2", "2"), short=("Part 2 · CDD and records", "第2部 · 盡職審查及紀錄"),
         eyebrow=("AMLO Cap. 615 · Part 2, sections 5 to 7 · Module 2", "《打擊洗錢條例》第615章 · 第2部第5至7條 · 單元二"),
         title=("AMLO Part 2 CDD and Records", "《打擊洗錢條例》第2部：盡職審查及備存紀錄"),
         lede=("Part 2 is where Schedule 2 gets its force. Section 5 makes the Schedule binding on every financial institution, you included, and turns a knowing or fraudulent breach of its key duties into a crime for the institution, and for any employee, person employed to work for it or person concerned in its management who causes or permits the breach. Section 7 settles how much the C&amp;ED Guideline counts. The duties themselves are on the Schedule 2 page.",
               "第2部令附表2具有法律效力。第5條令附表對所有金融機構（包括你）具約束力，並把明知或意圖詐騙而違反其主要責任的行為，定為機構的罪行，亦定為致使或准許該違反的僱員、受僱為機構工作的人或關涉機構管理的人的罪行。第7條則釐定海關指引的份量。各項責任本身，見附表2一頁。"),
         nav=P2_NAV, body=P2_BODY,
         foot=(f"Drawn from Part 2, sections 5 to 7, of the {CAP}, with section 21 and Schedule 1 Part 2 for the comparisons, and the C&amp;ED Disciplinary Fining Guideline (May 2018) and Disciplinary Action Guideline on Imposition of Pecuniary Penalty (April 2018) for their legal basis, and paragraph 1.3 of the AML/CFT Guideline for MSOs (June 2023).",
               f"取材自{CAP_TC}第2部（第5至7條）；比較部分取自第21條及附表1第2部；兩份罰款指引的法律依據取自海關《紀律處分罰款指引》（2018年5月）及《施加罰款紀律行動指引》（2018年4月），另參考《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》（2023年6月）第1.3段。")),
    dict(key='p3', group='part', tab=("3", "3"), short=("Part 3 · Supervision", "第3部 · 監管及調查"),
         eyebrow=("AMLO Cap. 615 · Part 3, sections 8 to 20 · Module 2", "《打擊洗錢條例》第615章 · 第3部第8至20條 · 單元二"),
         title=("AMLO Part 3 Powers", "《打擊洗錢條例》第3部的權力"),
         lede=("Part 3 is headed <b>Supervision and Investigations</b>. It is the Part that decides what happens when someone from Customs arrives to look at your records: who may come, what they may demand, how long you have, and what it costs you if they leave empty-handed. Set out here by situation rather than by section number.",
               "第3部的標題是<b>監管及調查</b>。這一部決定了海關人員上門查閱你的紀錄時會發生甚麼事：誰可以來、可以要求甚麼、你有多少時間，以及他們空手而回的代價。本頁按情境而非條文次序編排。"),
         nav=P3_NAV, body=P3_BODY,
         foot=(f"Drawn from Part 3, sections 8 to 20, of the {CAP}, with the definition of relevant authority from Schedule 1 Part 2.",
               f"取材自{CAP_TC}第3部（第8至20條），「有關當局」的定義取自附表1第2部。")),
    dict(key='p4', group='part', tab=("4", "4"), short=("Part 4 · Discipline", "第4部 · 紀律行動"),
         eyebrow=("AMLO Cap. 615 · Part 4, sections 20A to 23 · Module 2", "《打擊洗錢條例》第615章 · 第4部第20A至23條 · 單元二"),
         title=("AMLO Part 4 Discipline", "《打擊洗錢條例》第4部：紀律行動"),
         lede=("Four sections that let a regulator punish a financial institution for breaking the Schedule 2 duties without going to court. A money service operator is a financial institution, so this is the Commissioner's heaviest money power over you: up to $10,000,000 or three times the profit gained or costs avoided, whichever is greater. Learn it beside the criminal offences in Part 2 and the Commissioner's lighter Part 5 power.",
               "全部只有四條，作用是讓監管機構毋須經法院，即可就違反附表2責任懲處金融機構。金錢服務經營者屬金融機構，故這是關長對你最重的金錢制裁權：最高為$10,000,000或所獲取的利潤或所避免的開支的3倍（以較大者為準）。宜與第2部的刑事罪行、關長較輕的第5部權力一併記誦。"),
         nav=P4_NAV, body=P4_BODY,
         foot=(f"Drawn from Part 4, sections 20A to 23, of the {CAP}, with section 5 and section 43 for the comparisons and Schedule 1 Part 2 for the definitions of financial institution and relevant authority.",
               f"取材自{CAP_TC}第4部（第20A至23條）；對照部分取自第5及43條，「金融機構」及「有關當局」的定義取自附表1第2部。")),
    dict(key='p5', group='part', tab=("5", "5"), short=("Part 5 · Your licence", "第5部 · 發牌制度"),
         eyebrow=("AMLO Cap. 615 · Part 5, sections 24 to 53 · Modules 2 and 4", "《打擊洗錢條例》第615章 · 第5部第24至53條 · 單元二及四"),
         title=("AMLO Part 5 Licensing", "《打擊洗錢條例》第5部：發牌制度"),
         lede=("Part 5 is headed <b>Regulation of Operation of Money Service</b>, and it is the Part written about you. It is where your licence comes from, what it obliges you to do while you hold it, and how you can lose it. Most of its powers belong to the Commissioner of Customs and Excise. There are two main exceptions: the authorized officers he appoints hold the entry, search and arrest powers, and the courts hold others, since a court or magistrate may disqualify a convicted person from holding a licence and a magistrate issues entry warrants. It is laid out here as the life of a licence.",
               "第5部的標題是<b>對經營金錢服務的規管</b>，是專為你而寫的一部。你的牌照從這裏來，持牌期間的責任在這裏訂明，失去牌照的途徑也在這裏。當中大部分權力屬於海關關長。主要例外有兩類：進入、搜查及拘捕的權力屬於關長委任的獲授權人員；另有部分權力屬於法院：法庭或裁判官可取消被定罪者持有牌照的資格，而進入處所的手令則由裁判官發出。本頁按牌照的一生鋪陳。"),
         nav=P5_NAV, body=P5_BODY,
         foot=(f"Drawn from Part 5, sections 24 to 53, of the {CAP}.", f"取材自{CAP_TC}第5部（第24至53條）。")),
    dict(key='p6', group='part', tab=("6", "6"), short=("Part 6 · Review Tribunal", "第6部 · 覆核審裁處"),
         eyebrow=("AMLO Cap. 615 · Part 6, sections 54 to 76 · Module 2", "《打擊洗錢條例》第615章 · 第6部第54至76條 · 單元二"),
         title=("AMLO Part 6 Review Tribunal", "《打擊洗錢條例》第6部：覆核審裁處"),
         lede=("Part 6 is your route out of a decision you think is wrong. It sets up the Anti-Money Laundering and Counter-Terrorist Financing Review Tribunal, fixes the 21 days you have to go to it, decides when the Commissioner's decision starts to bite, and allows one further appeal, with leave, to the Court of Appeal. Read here from the licensee's side.",
               "第6部是你不服決定時的出路。它設立打擊洗錢及恐怖分子資金籌集覆核審裁處，訂明你須在21日內提出申請，決定關長的決定何時生效，並容許經許可後再向上訴法庭上訴一次。本頁從持牌人的角度閱讀。"),
         nav=P6_NAV, body=P6_BODY,
         foot=(f"Drawn from Part 6, sections 54 to 76, of the {CAP}, with sections 15, 21, 30 to 34, 43 and 80 where the timing and notices meet Part 6.",
               f"取材自{CAP_TC}第6部（第54至76條）；時限及通知與第6部相關之處，另參考第15、21、30至34、43及80條。")),
    dict(key='p6a', group='part', tab=("6A", "6A"), short=("Part 6A · Confidentiality", "第6A部 · 保密"),
         eyebrow=("AMLO Cap. 615 · Part 6A, sections 76A to 76G · Module 2", "《打擊洗錢條例》第615章 · 第6A部第76A至76G條 · 單元二"),
         title=("AMLO Part 6A Confidentiality", "《打擊洗錢條例》第6A部：保密的規定"),
         lede=("Part 6A was added in 2022. It binds the regulator's people to keep what they learn secret, lets them share it only through listed gateways, and puts a smaller duty on you: once you have been given an inspection or investigation requirement, or a disciplinary notice, you may not spread what you learned from it.",
               "第6A部於2022年增補。它規定監管方人員須對所知悉的資料保密，只可經所列途徑披露；同時對你施加一項較輕的責任：一旦你獲施加視察或調查要求，或獲發紀律通知，便不得散布從中獲得的資料。"),
         nav=P6A_NAV, body=P6A_BODY,
         foot=(f"Drawn from Part 6A, sections 76A to 76G, of the {CAP}, with sections 9, 12, 21(8) and 43(7).",
               f"取材自{CAP_TC}第6A部（第76A至76G條），另參考第9、12、21(8)及43(7)條。")),
    dict(key='p7', group='part', tab=("7", "7"), short=("Part 7 · Miscellaneous", "第7部 · 雜項"),
         eyebrow=("AMLO Cap. 615 · Part 7, sections 77 to 82 · Module 2", "《打擊洗錢條例》第615章 · 第7部第77至82條 · 單元二"),
         title=("AMLO Part 7 Miscellaneous", "《打擊洗錢條例》第7部：雜項條文"),
         lede=("Six short sections that settle practical questions raised elsewhere: how sure the Commissioner must be, what happens when Customs prosecutes in its own name, when a posted notice counts as delivered, what legal privilege still protects, and how the old register of money changers and remittance agents became licences. Part 8, which follows, is spent.",
               "六條簡短的條文，解決條例其他部分引起的實際問題：關長須證明到甚麼程度、海關以本身名義檢控時會怎樣、郵寄的通知何時視為已送達、法律專業保密權仍保障甚麼，以及舊的貨幣兌換商及匯款代理人紀錄冊如何轉為牌照。其後的第8部已失時效。"),
         nav=P7_NAV, body=P7_BODY,
         foot=(f"Drawn from Part 7, sections 77 to 82, of the {CAP}, with sections 5, 9A, 12A, 21, 24, 26, 51, 53, 59, 60, 63 and 64 where Part 7 is applied.",
               f"取材自{CAP_TC}第7部（第77至82條）；第7部適用之處，另參考第5、9A、12A、21、24、26、51、53、59、60、63及64條。")),
    dict(key='s1', group='sched', tab=("1", "1"), short=("Schedule 1 · Interpretation", "附表1 · 釋義"),
         eyebrow=("AMLO Cap. 615 · Schedule 1 · Modules 1 and 3", "《打擊洗錢條例》第615章 · 附表1 · 單元一及三"),
         title=("AMLO Schedule 1 Interpretation", "《打擊洗錢條例》附表1：釋義"),
         lede=("Schedule 1 holds the words the whole Ordinance shares. Part 1 defines what a money service is, and what money laundering and terrorist financing mean; Part 2 lists the financial institutions and names each one's regulator. For you the practical test comes first: is what you do a money service at all?",
               "附表1載有整條條例共用的詞語。第1部界定何謂金錢服務，以及洗錢和恐怖分子資金籌集的涵義；第2部列出金融機構及各自的監管者。對你而言，首先要問的實際問題是：你做的事究竟是否屬金錢服務？"),
         nav=S1_NAV, body=S1_BODY,
         foot=(f"Drawn from Schedule 1, Parts 1 and 2, of the {CAP}, with section 2 and the definition sections of Parts 3, 5, 6 and 6A and of Schedules 2 and 4; and the AML/CFT Guideline for MSOs (June 2023), paragraph 4.4.1.",
               f"取材自{CAP_TC}附表1第1及2部，另參考第2條，以及第3、5、6、6A部和附表2、4的釋義條文；以及《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》（2023年6月）第4.4.1段。")),
    dict(key='s2', group='sched', tab=("2", "2"), short=("Schedule 2 · CDD and records", "附表2 · 盡職審查及紀錄"),
         eyebrow=("AMLO Cap. 615 · Schedule 2 · with the AML/CFT Guideline for MSOs · Modules 3 and 6", "《打擊洗錢條例》第615章 · 附表2 · 配合《打擊洗錢指引》· 單元三及六"),
         title=("AMLO Schedule 2 CDD and Records", "《打擊洗錢條例》附表2：盡職審查及備存紀錄"),
         lede=("Schedule 2 is the rulebook for the counter: when CDD is owed and how deep it goes, how to monitor, what a wire transfer or remittance must carry, and how long records are kept. It is drawn here as the decisions you make, with the Schedule's sections as the rules and the C&amp;ED Guideline's paragraphs as the detail of how to meet them; in the Guideline, 'should' binds as firmly as 'must' (¶1.6).",
               "附表2是櫃位的規則：何時須執行盡職審查、要查到多深、如何監察、電傳轉帳或匯款須附帶甚麼資料，以及紀錄須保存多久。本頁把它畫成你要作的決定，以附表條文為規則，並以海關指引的段落說明如何符合規則；指引中的「應」與「須」同樣屬強制規定（第1.6段）。"),
         nav=S2_NAV, body=S2_BODY,
         foot=("Drawn from Schedule 2 to the " + CAP + ", and from the Customs and Excise Department's Guideline on Anti-Money Laundering and Counter-Financing of Terrorism (For Money Service Operators), June 2023, Chapters 1, 2, 4, 5, 8, 9, 10 and 11 and Appendix A, with the C&amp;ED FAQ applicable to all money service operators and the Licensing Guide for Money Service Operators (May 2026).",
               f"取材自{CAP_TC}附表2，以及香港海關《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》（2023年6月）第1、2、4、5、8、9、10及11章和附錄A，並參考適用於所有金錢服務經營者的常見問題及《金錢服務經營者牌照指引》（2026年5月）。")),
    dict(key='s3', group='sched', tab=("3", "3"), short=("Schedule 3 · Fees", "附表3 · 費用"),
         eyebrow=("AMLO Cap. 615 · Schedule 3, and Schedules 3A to 3K · Module 3", "《打擊洗錢條例》第615章 · 附表3及附表3A至3K · 單元三"),
         title=("AMLO Schedule 3 Fees", "《打擊洗錢條例》附表3：費用"),
         lede=("Schedule 3 prices every application under your licensing regime, and new rates took effect on 15 May 2026. The eleven lettered schedules that follow it belong to other sectors; the last section says what each one is, so that a borrowed number cannot mislead you.",
               "附表3訂明你的發牌制度下每項申請的收費，新收費已於2026年5月15日生效。其後十一個附有字母的附表屬於其他行業；最後一節說明每個附表的內容，免得被借用的數字誤導。"),
         nav=S3_NAV, body=S3_BODY,
         foot=(f"Drawn from Schedule 3, and the headings of Schedules 3A to 3K, of the {CAP}, with sections 26 to 41, 43, 50, 53ZTN, 53ZTZ and 53ZVR, and sections 3(1)(b), 13A and 20(3A) of Schedule 2; the fee schedule of the Licensing Guide for Money Service Operators (May 2026); and the AML/CFT Guideline for MSOs (June 2023), paragraphs 4.2.1 and 8.4.",
               f"取材自{CAP_TC}附表3及附表3A至3K的標題，另參考第26至41條、第43條、第50條、第5B部及第5C部有關寬免費用的條文、第5C部的釋義條文，以及附表2第3(1)(b)、13A及20(3A)條；《金錢服務經營者牌照指引》（2026年5月）的收費表；以及《打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）》（2023年6月）第4.2.1及8.4段。")),
    dict(key='s4', group='sched', tab=("4", "4"), short=("Schedule 4 · The Tribunal", "附表4 · 審裁處"),
         eyebrow=("AMLO Cap. 615 · Schedule 4 · Module 3", "《打擊洗錢條例》第615章 · 附表4 · 單元三"),
         title=("AMLO Schedule 4 The Tribunal", "《打擊洗錢條例》附表4：覆核審裁處"),
         lede=("Schedule 4 is the Review Tribunal's own rulebook: who sits on a review and for how long, how a sitting runs, the shortcuts the parties can agree to, and what happens when members change. Part 6 decides what you can take to the Tribunal; this Schedule decides what you will find when you get there.",
               "附表4是覆核審裁處本身的規則：誰審理覆核及任期多長、聆訊如何進行、各方可同意的簡化程序，以及成員變動時會怎樣。第6部決定你可把甚麼提交審裁處；本附表決定你到達後會遇到甚麼。"),
         nav=S4_NAV, body=S4_BODY,
         foot=(f"Drawn from Schedule 4 to the {CAP}, with sections 55 to 59 and 69.",
               f"取材自{CAP_TC}附表4，另參考第55至59條及第69條。")),
]

# the AML/CFT Guideline's own chapters (4, 10 and 11 live on the Schedule 2 page); each module
# exports <KEY>_BODY, <KEY>_NAV and <KEY>_META with the tab, headings and footer
for _k in ('g1', 'g2', 'g3', 'g5', 'g6', 'g7', 'g8'):
    _m = importlib.import_module(_k)
    _K = _k.upper()
    DOCS.append(dict(key=_k, group='guide', nav=getattr(_m, _K + '_NAV'), body=getattr(_m, _K + '_BODY'),
                     **getattr(_m, _K + '_META')))

DOCS += [
    dict(key='gl', group='cedd', tab=("Guidelines", "指引"), short=("Guidelines", "指引"),
         eyebrow=("C&amp;ED guidelines to MSOs · Module 4", "海關向金錢服務經營者發出的指引 · 單元四"),
         title=("The C&amp;ED Guidelines", "海關發出的指引"),
         lede=("Beside the Ordinance and the AML/CFT Guideline, the C&amp;ED has issued eight documents that decide how you get, keep and lose a licence: the Licensing Guide, the notes on this Assessment, two fit-and-proper guidelines, two templates for your application, and two guidelines on setting a penalty. This page keeps what they add. Where a rule is the Ordinance's own, it points to that page instead.",
               "除條例及《打擊洗錢指引》外，海關另發出八份文件，決定你如何取得、保留及失去牌照：《牌照指引》、本能力評核的須知、兩份適當人選指引、兩份申請文件範本，以及兩份釐定罰款的指引。本頁只保留它們補充的內容；屬條例本身的規則，則指向相關頁面。"),
         nav=GL_NAV, body=GL_BODY,
         foot=("Drawn from the Customs and Excise Department's Licensing Guide for Money Service Operators (May 2026), Guidance Notes on the Competence Assessment for Money Service Operators (December 2022), Guideline on Criteria for Determining Fitness and Propriety (April 2018) and its Supplementary Guideline (January 2020), Guidelines for Submission of Business Plan and of AML/CFT Policy (version 12/2019), Disciplinary Action Guideline on Imposition of Pecuniary Penalty (April 2018) and Disciplinary Fining Guideline (May 2018), with the official sample questions of 12 May 2021.",
               "取材自香港海關《金錢服務經營者牌照指引》（2026年5月）、《金錢服務經營者適用的能力評核須知》（2022年12月）、《有關適當人選準則的指引》（2018年4月）及其《補充指引》（2020年1月）、《遞交業務計劃的指引》及《遞交打擊洗錢及恐怖分子資金籌集政策的指引》（2019年12月版）、《施加罰款紀律行動指引》（2018年4月）及《紀律處分罰款指引》（2018年5月），並參考2021年5月12日的官方參考試題。")),
    dict(key='ci', group='cedd', tab=("Circulars", "通函"), short=("Circulars and FAQ", "通函及常見問題"),
         eyebrow=("C&amp;ED circulars to MSOs, 2018 to 2026, with the FAQ", "海關致金錢服務經營者的通函（2018至2026年）及常見問題"),
         title=("The C&amp;ED Circulars", "海關發出的通函"),
         lede=("Circulars are how the C&amp;ED tells operators what it expects between revisions of the rules: new typologies to watch, new ways of filing, and the dates rules began to bite. The C&amp;ED's FAQ for all money service operators is here too. Only what they add is kept; where a circular repeats the Ordinance or the AML/CFT Guideline, the rule stays on its own page.",
               "通函是海關在規則修訂之間向經營者說明期望的途徑：須留意的新洗錢手法、新的提交方式，以及規則開始生效的日期。海關為所有金錢服務經營者發布的常見問題亦收錄於此。本頁只保留通函補充的內容；通函重複條例或《打擊洗錢指引》之處，規則仍留在其本身的頁面。"),
         nav=CI_NAV, body=CI_BODY,
         foot=CI_FOOT),
]

DISCLAIM = ("A revision aid, not legal advice: the source document prevails, so check the cited paragraph or section before relying on any line here.",
            "本頁屬溫習輔助，並非法律意見：一切以原文為準，引用前請查核所引段落或條文。")


def prefix_ids(html, ids, pre):
    for i in sorted(ids, key=len, reverse=True):
        html = html.replace(f'id="{i}"', f'id="{pre}-{i}"').replace(f'href="#{i}"', f'href="#{pre}-{i}"')
    return html


CARD_KEYS = [
    ('must', ("a duty on you, or a consequence for you", "你的責任，或你要承受的後果")),
    ('may', ("a power or a discretion held by someone else", "他人持有的權力或酌情權")),
    ('ok', ("a protection or a safe outcome for you", "你可依靠的保障或安全結果")),
]


def _close_div(html, start):
    i, depth = start, 0
    while i < len(html):
        if html.startswith('<div', i):
            depth += 1
            i += 4
        elif html.startswith('</div>', i):
            depth -= 1
            i += 6
            if depth == 0:
                return i
        else:
            i += 1
    raise ValueError('unbalanced div')


def add_card_legends(html):
    """Put a key beside every group of cards that uses colour."""
    out, pos = [], 0
    for m in re.finditer(r'<div class="(?:cards[^"]*|pick)">', html):
        if m.start() < pos:
            continue
        end = _close_div(html, m.start())
        block = html[m.start():end]
        kinds = set(re.findall(r'<div class="card ([a-z]*)"', block))
        entries = [f'<span><i class="{k}"></i>{B(en, tc, True)}</span>'
                   for k, (en, tc) in CARD_KEYS if k in kinds]
        if entries and (kinds & {'', 'line'}):
            entries.append('<span><i></i>' + B("no colour: a neutral fact", "無色：中性事實", True) + '</span>')
        legend = f'<div class="legend cardkey">{"".join(entries)}</div>' if entries else ''
        out.append(html[pos:m.start()])
        out.append(legend + block)
        pos = end
    out.append(html[pos:])
    return ''.join(out)


def render_doc(doc):
    pre = doc['key']
    ids = [i for i, _, _ in doc['nav']]
    body = add_card_legends(prefix_ids(doc['body'], ids, pre))
    return (f'<section class="doc" id="doc-{pre}">'
            '<header class="top"><div class="wrap">'
            f'<p class="eyebrow">{B(*doc["eyebrow"], True)}</p>'
            f'<h1>{B(*doc["title"])}</h1>'
            f'<p class="lede">{B(*doc["lede"])}</p>'
            '</div></header>'
            f'<main class="wrap">{body}</main>'
            f'<footer><div class="wrap">{P(doc["foot"][0] + " " + DISCLAIM[0], doc["foot"][1] + DISCLAIM[1])}</div></footer>'
            '</section>')


def docbtn(d):
    en, tc = d['short']
    # numbered tabs show the number; the guidance tabs are words, so they switch language
    lab = B(*d['tab'], True) if d['group'] == 'cedd' else esc(d['tab'][0])
    return (f'<button data-doc="doc-{d["key"]}" aria-pressed="false" title="{esc(en)} / {esc(tc)}">'
            f'{lab}</button>')


GROUPS = [('part', ("Parts", "條例各部")), ('sched', ("Schedules", "附表")),
          ('guide', ("Guideline chapters", "指引各章")), ('cedd', None)]
DOCNAV = ''.join(
    '<span class="dgroup">' + (f'<span class="dlabel">{B(*lab, True)}</span>' if lab else '')
    + ''.join(docbtn(d) for d in DOCS if d['group'] == g) + '</span>'
    for g, lab in GROUPS)

# one chapter list per document; CSS shows only the active one
CHAPNAV = ''.join(
    f'<nav class="chapnav" data-for="doc-{d["key"]}" aria-label="Chapters 章節">'
    f'<p class="chaphead">{B(*d["short"])}</p>'
    + ''.join(f'<a href="#{d["key"]}-{i}">{B(en, tc)}</a>' for i, en, tc in d['nav'])
    + '</nav>' for d in DOCS)

OUTLINE_ICON = ('<svg viewBox="0 0 16 16" width="15" height="15" fill="currentColor" aria-hidden="true">'
                '<circle cx="3" cy="4" r="1.1"/><rect x="6" y="3.35" width="8" height="1.3" rx=".65"/>'
                '<circle cx="3" cy="8" r="1.1"/><rect x="6" y="7.35" width="8" height="1.3" rx=".65"/>'
                '<circle cx="3" cy="12" r="1.1"/><rect x="6" y="11.35" width="5.5" height="1.3" rx=".65"/></svg>')
CHAPCSS = ''.join(
    f'html[data-doc="doc-{d["key"]}"] .chapnav[data-for="doc-{d["key"]}"]{{display:flex;}}' for d in DOCS)

DARK = """
  --bg:#0f0f0f; --panel:#191919; --ink:#f2f2f2; --text:#dcdcdc; --muted:#9a9a9a; --faint:#6b6b6b;
  --line:#262626; --line-strong:#3a3a3a;
  --green:#6fbf8f; --green-bg:#16241c; --amber:#d9a43b; --amber-bg:#2a2314; --red:#e07068; --red-bg:#2b1a18;
  --accent:#a99af6; --trap-bg:#1b1729; --trap-line:#3a3160;
"""
CSS = io.open(os.path.join(SP, 'pack_css.css'), encoding='utf-8').read().replace('%DARK%', DARK) + CHAPCSS
JS = io.open(os.path.join(SP, 'pack_js.js'), encoding='utf-8').read()

BOOT = ('<script>(function(){var d=document.documentElement,l="both",c="";'
        'try{l=localStorage.getItem("pack-lang")||"both";c=localStorage.getItem("pack-doc")||"";}catch(e){}'
        'if(["en","tc","both"].indexOf(l)<0)l="both";if(c==="doc-cdd")c="doc-s2";d.setAttribute("data-lang",l);'
        'if(c)d.setAttribute("data-doc",c);})();</script>')

PAGE = (
    '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>MSO Revision Pack</title>\n'
    '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:opsz,wght@9..40,400..700&display=swap" rel="stylesheet">\n'
    f'<style>{CSS}</style>\n{BOOT}\n'
    '<div class="bar"><div class="wrap barin">'
    f'<span class="brand">{B("MSO Competence Assessment", "金錢服務經營者能力評核", True)}</span>'
    f'<nav class="docnav" aria-label="Documents 文件">{DOCNAV}</nav>'
    '<div class="ctls"><div class="seg" role="group" aria-label="Language 語言">'
    '<button data-lang="en" aria-pressed="false">EN</button>'
    '<button data-lang="tc" aria-pressed="false">中文</button>'
    '<button data-lang="both" aria-pressed="false">EN + 中文</button></div>'
    '<button id="recall" aria-pressed="false">Recall mode</button></div>'
    '</div></div>\n'
    '<div class="outline">'
    f'<button class="outline-toggle" id="outline-toggle" aria-expanded="true" aria-controls="outline-panel" title="Chapters 章節">{OUTLINE_ICON}</button>'
    f'<div class="outline-panel" id="outline-panel">{CHAPNAV}</div>'
    '</div>\n'
    '<div class="wrap"><p class="recallnote">'
    + B("Recall mode blurs the outcomes in the diagrams and the key numbers in the tables. Click a blurred block, or focus it and press Enter, to check yourself.",
        "自測模式會模糊圖中的結論及表內的關鍵數字。點擊模糊的方塊，或以鍵盤選取後確認，即可核對。")
    + '</p></div>\n'
    + ''.join(render_doc(d) for d in DOCS) + '\n'
    f'<script>{JS}</script>\n'
)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
io.open(OUT, 'w', encoding='utf-8', newline='\n').write(PAGE)  # same bytes on every platform
print('wrote', OUT, len(PAGE.encode('utf-8')), 'bytes')
for w in bl_core.warnings:
    print('WARN', w)

# ---- audits -------------------------------------------------------------
ids = re.findall(r'id="([^"]+)"', PAGE)
dupes = sorted({i for i in ids if ids.count(i) > 1})
print('duplicate ids:', dupes or 'none')
print('docs:', re.findall(r'class="doc" id="([^"]+)"', PAGE))
print('sections:', len(re.findall(r'<section class="sec"', PAGE)))
dead = [h for h in set(re.findall(r'href="#([^"]+)"', PAGE)) if h not in ids]
print('dead anchors:', dead or 'none')
bad = [t for t in re.findall(r'<span class="c-tc"[^>]*>([^<]*)</span>', PAGE) if re.search(r'[A-Za-z]{3,}', t)]
print('cites with English left in the Chinese view:', bad or 'none')
tcbad = [t for t in re.findall(r'<span class="l-tc[^"]*" lang="zh-Hant">(.*?)</span>', PAGE) if re.search(r'[A-Za-z]{3,}', re.sub(r'<[^>]+>', '', t))]
print('Chinese text with English words:', len(tcbad))
for t in tcbad[:12]:
    print('   ', re.sub(r'<[^>]+>', '', t)[:120])
