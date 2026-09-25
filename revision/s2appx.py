# Guideline Appendix A on the Schedule 2 page: the documents and sources that verify identity,
# and who may certify a copy (section id 'docs').
from bl_core import *
import ui as U


def cc(*cs):
    """Join several citations into one (en, tc) pair."""
    pairs = [cite_pair(c) for c in cs]
    return (' · '.join(p[0] for p in pairs), ' · '.join(p[1] for p in pairs))


def AX(p):
    """A paragraph of Guideline Appendix A."""
    return (f"App. A ¶{p}", f"附錄A第{p.replace('–', '至').replace(', ', '、')}段")


def AF(n):
    """A footnote in Guideline Appendix A."""
    return (f"App. A fn {n}", f"附錄A註{n}")


def FAQ(q):
    return (f"FAQ Q{q}", f"常見問題第{q}問")


def LG(p):
    return (f"Licensing Guide ¶{p}", f"《牌照指引》第{p}段")


def vd(ch):
    return f'<td class="verdict">{ch}</td>'


# ---------------------------------------------------------------- Figure: which document for an individual
def fig_person():
    W = 1000
    m = 's2dA'
    YES, NO = ("yes", "是"), ("no", "否")
    q1 = Node(300, 400, ("Is the individual a Hong Kong resident?", "該個人是否香港居民？"), AX("1"), shape='hex')
    hk = U.Card(30, 330, ("Hong Kong identity card or document of identity", "香港身份證或簽證身分書"),
                ("Should always be used for a Hong Kong resident", "香港居民應經常以此識別及／或核實"), 'ok', AX("1"), answer=True)
    q2 = Node(520, 470, ("Is the non-resident physically present in Hong Kong?", "該非居民是否實際身在香港？"), AX("1–2"), shape='hex')
    tv = U.Card(300, 250, ("A valid travel document", "有效旅遊證件"), None, 'ok', AX("1"), answer=True)
    three = U.Card(570, 370, ("Any one of these three", "以下三者之一"),
                   ("(a) valid international passport or other travel document; (b) current national identity card with the person's photograph; (c) current valid national driving licence with photograph, issued by a competent national or state authority",
                    "(a) 有效的國際護照或其他旅遊證件；(b) 附有個人照片的有效國民身分證；(c) 由主管的國家或政府機構簽發、附照片的有效國家駕駛執照"),
                   'ok', AX("2"), answer=True)
    idp = U.Card(595, 320, ("An international driving permit or licence", "國際駕駛許可證及執照"),
                 ("Not acceptable for this purpose", "不能用於此目的"), 'stop', AF("72"), answer=True)
    H = place([([q1], 56), ([hk, q2], 60), ([tv, three], 50), ([idp], 0)], y0=14)
    # the travel-document box sits level with the top of the taller three-document box
    tv.y = three.y
    b = [n.render() for n in (q1, hk, q2, tv, three, idp)]
    b.append(edge([q1.left, (hk.cx, q1.cy), hk.top], YES, hk.cx + 10, q1.cy - 8, 'start', mid=m))
    b.append(edge([q1.right, (q2.cx, q1.cy), q2.top], NO, q2.cx - 10, q1.cy - 8, 'end', mid=m))
    b.append(edge([q2.left, (tv.cx, q2.cy), tv.top], YES, tv.cx - 10, (q2.bottom[1] + tv.top[1]) / 2 + 4, 'end', mid=m))
    b.append(edge([q2.bottom, three.top], NO, three.cx + 10, (q2.bottom[1] + three.top[1]) / 2 + 4, 'start', mid=m))
    # an exclusion note on item (c), not a next step: dashed, no arrowhead
    b.append(edge([three.bottom, idp.top], ("(c) does not include", "(c)項不包括"), three.cx + 10, (three.bottom[1] + idp.top[1]) / 2 + 5, 'start',
                  marker=False, mid=m).replace('class="e"', 'class="e e-dash"'))
    aria = ("Decision tree for an individual customer: a Hong Kong resident is always identified and verified by Hong Kong identity card or document of identity; a non-resident who is physically present by a valid travel document; a non-resident who is not present by a travel document, a national identity card with photograph or a national driving licence with photograph, but never an international driving permit.",
            "個人客戶的決策樹：香港居民一律以香港身份證或簽證身分書識別及核實；實際身在香港的非居民以有效旅遊證件核實；沒有現身香港的非居民以旅遊證件、附照片的國民身分證或附照片的國家駕駛執照核實，但國際駕駛許可證不能使用。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


PERSON_KEY = U.legend([('hex', ("a question you answer", "你須回答的問題")),
                       ('ok', ("a document that verifies identity", "可核實身分的文件")),
                       ('stop', ("not acceptable", "不能接納"))])


# ---------------------------------------------------------------- Figure: a certified copy
def fig_cert():
    W = 1000
    m = 's2dB'
    YES, NO = ("yes", "是"), ("no", "否")
    c1 = U.Card(20, 290, ("The certifier sees the original", "證明人查閱正本"),
                ("Without this the certification is not effective", "否則認證並不有效"), 'plain', AX("7"))
    c2 = U.Card(340, 295, ("The certifier marks the copy", "證明人在複本上註明"),
                ("Signs and dates it, prints his or her name in capitals underneath, states his or her position or capacity, and states it is a true copy of the original",
                 "簽署並寫上日期，在下方以大楷列示姓名，註明職位或身分，並說明該複本為正本的真確複本"), 'plain', AX("9"))
    c3 = U.Card(670, 300, ("You decide whether to accept it", "由你決定是否接納"),
                ("You stay liable for the CDD. Be cautious, especially with copies from a country perceived as high risk or from an unregulated entity",
                 "你仍須為盡職審查負責。須審慎行事，特別是來自被視為涉及高風險的國家或不受監管實體的複本"), 'must', AX("10"))
    q = Node(645, 350, ("Unsure it is authentic, or that it relates to the customer?", "未能確定文件真確，或懷疑文件與客戶無關？"), AX("10"), shape='hex')
    extra = U.Card(60, 380, ("Take additional measures", "採取額外措施"),
                   ("to mitigate the ML/TF risk", "以減低洗錢／恐怖分子資金籌集的風險"), 'must', AX("10"), answer=True)
    ok = U.Card(660, 320, ("You may accept the certified copy", "可接納經認證的複本"), None, 'ok', AX("10"), answer=True)
    H = place([([c1, c2, c3], 56), ([extra, q], 50), ([ok], 0)], y0=14)
    b = [n.render() for n in (c1, c2, c3, q, extra, ok)]
    b.append(edge([c1.right, (c2.x, c1.right[1])], mid=m))
    b.append(edge([c2.right, (c3.x, c2.right[1])], mid=m))
    b.append(edge([c3.bottom, q.top], mid=m))
    b.append(edge([q.left, extra.right], YES, (q.x + extra.x + extra.w) / 2, q.cy - 8, mid=m))
    b.append(edge([q.bottom, ok.top], NO, q.cx + 10, (q.bottom[1] + ok.top[1]) / 2 + 5, 'start', mid=m))
    aria = ("Certification flow: the certifier sees the original, then signs, dates, names and states capacity on the copy and states it is a true copy; the MSO stays liable and decides whether to accept it; if unsure of authenticity or of the link to the customer, it takes additional measures, otherwise it may accept the copy.",
            "認證流程：證明人查閱正本，然後在複本上簽署、寫上日期、列示姓名及註明職位或身分，並說明為真確複本；金錢服務經營者仍須負責並決定是否接納；如未能確定文件真確或與客戶有關，須採取額外措施，否則可接納複本。")
    return svg(W, H + 14, ''.join(b), aria, m, 860)


CERT_KEY = U.legend([('', ("a step", "步驟")), ('hex', ("a question you answer", "你須回答的問題")),
                     ('must', ("a duty on you", "你的責任")), ('ok', ("safe to proceed", "可以進行"))])


# ---------------------------------------------------------------- the section
T = U.table
tr, rh, td, th = U.tr, U.rh, U.td, U.th

PERSON_TABLE = T([th("The individual", "個人客戶的情況"), th("Verify identity against", "核實身分的依據")], [
    tr(rh("A Hong Kong resident", "香港居民", AX("1")),
       td("You should always identify and verify by the Hong Kong identity card or document of identity. Every resident aged 11 or above must register for an identity card; a permanent resident's card has a capital letter A under the date of birth on the front",
          "應經常以香港身份證或簽證身分書識別及／或核實。所有年滿11歲的香港居民均須登記領取身分證；永久性居民身份證正面的出生日期下方註有大寫英文字母「A」",
          cc(AX("1"), AF("73")))),
    tr(rh("A non-resident who is physically present in Hong Kong", "實際身在香港的非居民", AX("1")),
       td("A valid travel document: a non-resident's identity should be verified by reference to it. Appendix A lists the national identity card and driving licence only for non-residents who are not physically present (next row; see also the easy-to-confuse box below)",
          "有效旅遊證件：非居民的身分應根據其有效旅遊證件核實。附錄A只就沒有現身香港的非居民列出國民身分證及駕駛執照（見下一行，另見下文「易混淆」方塊）", AX("1–2"), post=U.flag())),
    tr(rh("A non-resident who is not physically present in Hong Kong", "沒有現身香港的非居民", AX("2")),
       td("You may use any one of: a valid international passport or other travel document; a current national (Government- or State-issued) identity card bearing the person's photograph; or a current valid national driving licence with photographic evidence of identity, issued by a competent national or state authority. An international driving permit or licence is not acceptable",
          "應根據以下任何一項：有效的國際護照或其他旅遊證件；附有個人照片的有效國民（即由政府或國家簽發）身分證；或由主管的國家或政府機構簽發、有照片證明身分的有效國家駕駛執照。國際駕駛許可證及執照不能用於此目的",
          cc(AX("2"), AF("72")), post=U.flag())),
    tr(rh("A minor born in Hong Kong with neither a valid travel document nor a Hong Kong identity card", "在香港出生而沒有有效旅遊證件或香港身份證的未成年人", AX("4")),
       td("The minor's Hong Kong birth certificate. With <b>any</b> minor, you should also record and verify the identity of the parent or guardian who represents or accompanies the minor, by the rules above",
          "該未成年人的香港出生證明書。與<b>任何</b>未成年人建立關係時，亦應按以上規定，記錄及核實該未成年人的父母或代表或陪同該未成年人的監護人的身分",
          AX("4"))),
    tr(rh("From a jurisdiction with no national identity cards, and holding no travel document or driving licence with a photograph", "來自沒有國民身分證的司法管轄區，亦沒有附相片的旅遊證件或駕駛執照", AX("6")),
       td("Exceptionally, and on a risk-based approach, you may accept other documents as evidence of identity. They should carry the person's photograph wherever possible",
          "你可採取以風險為本的方法，破例接受其他文件作為身分識別證據。該等文件應盡可能附有該個人的照片",
          AX("6"))),
    tr(rh("No identification document with a photograph can be obtained", "未能取得載有照片的身分證明文件", "¶4.3.4"),
       td("The document should carry the customer's photograph. In exceptional circumstances you may accept one without, but only after the associated risks have been properly assessed and mitigated",
          "身分證明文件應載有客戶的照片。如情況特殊，你可以接納沒有照片的文件，但須先妥善評估並減低所涉及的風險",
          "¶4.3.4")),
], note=B("The general rule behind every row: verify name, date of birth, identification number and document type against a reliable and independent source, such as a Hong Kong identity card or other national identity card, a valid travel document (for example an unexpired passport), or another document from a reliable and independent source, such as one issued by a government body. Appendix A lists the documents the CCE recognises for this. ",
          "每一行背後的一般規定：根據可靠及獨立來源核實姓名、出生日期、識別號碼及文件類別，例如香港身份證或其他國家的身份證、有效的旅遊證件（例如未過期的護照），或其他可靠及獨立來源的文件（例如政府機構發出的文件）。附錄A載有關長認可屬此用途的文件。")
         + cite_html(cc("¶4.3.3 fn 16", AX("1–6"))), minw=720)

TRAVEL_TABLE = T([th("", ""), th("Guideline Appendix A ¶3 (June 2023)", "《指引》附錄A第3段（2023年6月）"), th("C&amp;ED FAQ answer 2", "海關常見問題答.2")], [
    tr(rh("(a)", "(a)"), td("Permanent Resident Identity Card of the Macau SAR", "澳門特別行政區永久居民身分證", AX("3(a)")),
       td("Passport", "護照", FAQ("2"), post=U.flag())),
    tr(rh("(b)", "(b)"), td("Mainland Travel Permit for Taiwan Residents", "台灣居民往來內地通行證", AX("3(b)")), td("The same", "相同", FAQ("2"))),
    tr(rh("(c)", "(c)"), td("Seaman's Identity Document, issued under the International Labour Organisation Convention / Seafarers Identity Document Convention 1958",
                          "海員身分證明文件（根據《國際勞工組織公約》╱《1958年海員身分證件公約》簽發）", AX("3(c)")), td("The same", "相同", FAQ("2"))),
    tr(rh("(d)", "(d)"), td("Taiwan Travel Permit for Mainland Residents", "內地居民的台灣旅遊許可證", AX("3(d)")), td("The same", "相同", FAQ("2"))),
    tr(rh("(e)", "(e)"), td("Permit for residents of Macau issued by the Director of Immigration", "由入境事務處處長簽發的澳門居民旅遊證", AX("3(e)")), td("The same", "相同", FAQ("2"))),
    tr(rh("(f)", "(f)"), td("Exit-entry Permit for Travelling to and from Hong Kong and Macau for Official Purposes", "因公往來香港澳門特別行政區通行證", AX("3(f)")), td("The same", "相同", FAQ("2"))),
    tr(rh("(g)", "(g)"), td("Exit-entry Permit for Travelling to and from Hong Kong and Macau", "往來港澳通行證", AX("3(g)")), td("The same", "相同", FAQ("2"))),
], note=B("Appendix A ¶3 defines a travel document as a passport or some other document with the holder's photograph that establishes the holder's identity and nationality, domicile or place of permanent residence. The FAQ gives its list for the purpose of ¶4.3.3 and cites Appendix A ¶3 as its reference. The Guideline's list names the Macau permanent resident card and not the passport; the FAQ's list names the passport and not the Macau card. Neither source says the other is wrong. ",
          "附錄A第3段把旅遊證件界定為附有持有人照片，能確定持有人的身分及國籍、原居地或永久居留地的護照或其他證件。常見問題的清單是就第4.3.3段而列出，並以附錄A第3段為參考資料。《指引》的清單列出澳門永久居民身分證而沒有列出護照；常見問題的清單列出護照而沒有列出澳門永久居民身分證。兩者均沒有指對方有誤。")
         + cite_html(cc(AX("3"), FAQ("2"))), minw=760, cls='cmp')

ID_DOC_TABLE = T([th("For", "就以下而言"), th("“Identification document” means", "「識別文件」指")], [
    tr(rh("An individual", "個人", "s.1 Sch. 2"), td("His or her identity card, certificate of identity, document of identity or travel document, as defined in the Immigration Ordinance (Cap. 115)",
                                                       "該人的身分證、身分證明書、簽證身分書或旅行證件（該等文件為《入境條例》（第115章）所界定者）")),
    tr(rh("A company under the Companies Ordinance", "《公司條例》所界定的公司", "s.1 Sch. 2"), td("Its certificate of incorporation, or its certificate of re-domiciliation",
                                                                                      "其公司註冊證明書，或其遷冊證明書")),
    tr(rh("A registered non-Hong Kong company", "註冊非香港公司", "s.1 Sch. 2"), td("Its certificate of registration", "其註冊證明書")),
    tr(rh("Any other corporation incorporated outside Hong Kong", "其他在香港以外地方成立的法團", "s.1 Sch. 2"),
       td("Its certificate of incorporation or registration, or any other document evidencing its incorporation, issued by the authority there that does what the Registrar of Companies does",
          "由當地執行與公司註冊處處長職能類同的主管當局發出的公司註冊證書或註冊證明書，或任何其他證明其成立為法團的文件")),
    tr(rh("A partnership carrying on business in Hong Kong", "在香港經營業務的合夥", "s.1 Sch. 2"), td("Its business registration certificate", "其商業登記證"), cls=''),
    tr(rh("A partnership not carrying on business in Hong Kong", "並無在香港經營業務的合夥", "s.1 Sch. 2"),
       td("Its partnership agreement, or any document evidencing its formation or registration issued by a governmental body", "其合夥協議，或由政府機構發出的任何證明其成立或註冊的文件")),
], minw=680)

ENTITY_TABLE = T([th("If the customer is", "如客戶是"), th("Examples of reliable and independent sources", "可靠及獨立來源的例子")], [
    tr(rh("Any legal person", "任何法人", "¶4.3.7"),
       td("Certificate of incorporation; record in an independent company registry; certificate of incumbency; certificate of good standing; record of registration; partnership agreement or deed; constitutional document; or another document from a reliable and independent source, such as one issued by a government body. One document may not be enough: a certificate of incorporation usually verifies the name and legal form but cannot prove current existence",
          "公司註冊證明書；獨立公司註冊登記冊的記錄；職權證明書；良好聲譽證明書；註冊記錄；合夥協議或契約；章程文件；或其他可靠及獨立來源的文件（例如政府機構發出的文件）。一份文件未必足夠：公司註冊證明書在大部分情況下僅能核實名稱及法定形式，不能證明該法人現時仍然存在",
          "¶4.3.7 fn 20", post=U.flag())),
    tr(rh("A corporation", "公司客戶", AX("5")),
       td("You may run a company registry search in the place of incorporation and obtain a full company search report (or the overseas equivalent)",
          "你可於該公司註冊地的公司註冊處查冊，取得一份完整的公司查冊報告（或外地對等資料）", AX("5"))),
    tr(rh("A partnership or unincorporated body that is well known and reputable", "眾所周知、有信譽的合夥或非法團團體", "¶4.3.8"),
       td("Confirming its membership of a relevant professional or trade association is likely to be enough, but only if all three hold: it is well known and reputable; it has a long history in its industry; and there is substantial public information about it, its partners and controllers",
          "確認其具有相關專業或行業協會會員身分，可能已足夠，但須三項條件全部符合：該客戶眾所周知、有信譽；在業內歷史悠久；以及有大量有關該客戶、其合夥人及控制人的公開資料",
          "¶4.3.8")),
    tr(rh("An association, club, society, charity, religious body, institute, mutual or friendly society, co-operative or provident society", "協會、會所、社團、慈善組織、宗教組織、院校、友好互助社團、合作社或公積金社團", "¶4.3.9"),
       td("You should satisfy yourself that its purpose is legitimate, for example by asking to see its constitution", "應令自己信納其合法目的，例如要求閱覽其組織章程", "¶4.3.9")),
    tr(rh("A trust or other similar legal arrangement", "信託或其他類似法律安排", "¶4.3.12"),
       td("Trust deed or similar instrument (exceptionally, you may keep a redacted copy); record of an appropriate register in the country of establishment; written confirmation from a trustee acting in a professional capacity; written confirmation from a lawyer who has reviewed the instrument; or written confirmation from a trust company in your own financial group, if it manages the trust",
          "信託契據或類似文書（在特殊情況下可保存刪節本）；成立信託的相關國家的合適登記冊記錄；由以專業身分行事的受託人簽發的書面確認書；由已覆核相關文書的律師簽發的書面確認書；或由與你同屬一個金融集團的信託公司簽發的書面確認書（如有關信託由該信託公司管理）",
          "¶4.3.12 fn 23")),
], minw=720)

CERTIFIER_TABLE = T([th("Who certified the copy", "由誰認證複本"), th("Acceptable?", "可否接納"), th("What to note", "須注意")], [
    tr(rh("An intermediary specified in s.18(3) of Schedule 2", "附表2第18(3)條指明的中介人", AX("8(a)")), vd(U.YES),
       td("The same list of intermediaries you may rely on for CDD: see <a href=\"#s2-rely\">Intermediaries</a>", "即可依賴其執行盡職審查的中介人名單，見<a href=\"#s2-rely\">中介人一節</a>", "s.18(3) Sch. 2")),
    tr(rh("A member of the judiciary in an equivalent jurisdiction", "在對等司法管轄區的司法人員", AX("8(b)")), vd(U.YES), td("—", "—")),
    tr(rh("An officer of an embassy, consulate or high commission", "大使館、領事館或高級專員公署的人員", AX("8(c)")), vd(U.YES),
       td("Of the country that issued the identity document", "須屬發出該身分核實文件的國家", AX("8(c)"))),
    tr(rh("A Justice of the Peace", "太平紳士", AX("8(d)")), vd(U.YES), td("—", "—")),
    tr(rh("A professional person, such as a certified public accountant, lawyer, notary public or chartered secretary", "專業人士，例如會計師、律師、公證人及特許秘書", AX("8(e)")), vd(U.YES),
       td("Other appropriate professionals may also be accepted, with the same caution as for any certifier. A chartered secretary is a current full member of the Institute of Chartered Secretaries and Administrators or one of its designated divisions",
          "亦可接納其他合適的專業人士，但須與其他證明人一樣審慎考慮。特許秘書指屬英國特許秘書及行政人員公會或其指定分部現任正式會員的人",
          cc(AF("75"), AF("76")))),
    tr(rh("The customer itself", "客戶本人", AF("74")), vd(U.NO),
       td("In general, self-certified copies are not sufficient", "一般來說，由客戶自行認證文件複本並不足夠", AF("74"), post=U.flag())),
    tr(rh("A professional person inside a legal-person customer", "法人客戶內的專業人士", AF("74")), vd(U.YES),
       td("Only if that person is subject to the professional conduct requirements of a relevant professional body and certified the copies in his or her professional capacity",
          "該專業人士須遵守相關專業團體的專業操守規定，並已經以其專業身分認證該等文件複本", AF("74"))),
], note=B("The five are examples, not a closed list. ", "以上五類只是例子，並非詳盡無遺。") + cite_html(AX("8")), minw=760)

APX = sec('docs', [("App. A", "附錄A"), "¶4.3.3–4.3.4", "¶4.3.7–4.3.12", "s.1 Sch. 2"],
          ("Which documents prove identity, and who may certify a copy", "哪些文件可核實身分，以及誰可認證複本"),
    P("Start at the top and answer two questions: is the person a Hong Kong resident, and if not, are they in Hong Kong? The green box you land on is the document Appendix A expects. Appendix A is headed \"illustrative examples\", and the Guideline describes it as the documents the CCE recognises as reliable and independent sources.",
      "由頂部開始回答兩條問題：該人是否香港居民？如不是，他是否身在香港？你到達的綠色方格，就是附錄A預期的文件。附錄A的標題為「示例」，《指引》形容其載有關長認可屬可靠及獨立來源的文件。")
    + U.fig(fig_person, ("For a Hong Kong resident, Appendix A says to use the Hong Kong identity card or document of identity always. It lists the national identity card and national driving licence only for non-residents who are not physically present in Hong Kong.",
                         "就香港居民而言，附錄A指應經常以香港身份證或簽證身分書識別及／或核實。附錄A只就沒有現身香港的非居民列出國民身分證及國家駕駛執照。"), PERSON_KEY)
    + U.h3("Individuals: the situation decides the document", "個人：按情況決定用哪份文件")
    + PERSON_TABLE
    + U.h3("What counts as a travel document", "甚麼屬旅遊證件")
    + P("A travel document is a passport or some other document with the holder's photograph that establishes the holder's identity and nationality, domicile or place of permanent residence. Appendix A then names seven documents that count as travel documents for identity verification; the C&ED's FAQ gives a list of seven that differs in its first item.",
        "旅遊證件是指附有持有人照片，能確定持有人的身分及國籍、原居地或永久居留地的護照或其他證件。附錄A其後列出七種可作身分核實用途的旅遊證件；海關常見問題亦列出七種，但第一項不同。")
    + TRAVEL_TABLE
    + U.h3("The Ordinance's \"identification document\", used for remittances", "條例中的「識別文件」：用於匯款")
    + P("The Ordinance defines \"identification document\" for individuals, companies and partnerships. Schedule 2 uses it for remittances: before a remittance transaction to which s.13 applies, you verify the originator's identity by reference to it and record its number, and the place of issue if it is a travel document (s.13(2) of Schedule 2; see <a href=\"#s2-transfers\">Transfers and remittances</a>).",
        "條例就個人、公司及合夥界定「識別文件」。附表2在匯款上使用這個詞：進行第13條適用的匯款交易前，須藉參考匯款人的識別文件核實其身分，並記錄文件號碼；如屬旅行證件，亦須記錄發出旅行證件的地方（附表2第13(2)條；見<a href=\"#s2-transfers\">轉帳與匯款一節</a>）。")
    + ID_DOC_TABLE
    + U.h3("Companies, partnerships and trusts", "公司、合夥及信託")
    + '<p>' + B("For a legal person or a trust, the Guideline says you should normally verify its name, legal form, current existence (at the time of verification) and the powers that regulate and bind it, and its examples of sources go wider than the statutory document.",
                "就法人或信託而言，《指引》指一般應核實其名稱、法定形式、現時（核實時）仍然存在及規管和約束它的權力；所舉的來源例子比法定識別文件更廣。")
    + ' ' + cite_html(cc("¶4.3.7", "¶4.3.12")) + '</p>'
    + ENTITY_TABLE
    + U.h3("A certified copy: who may certify it, and how", "經認證的複本：誰可認證，如何認證")
    + P("An independent, appropriate certifier guards against the risk that the documents do not belong to the customer being verified. Follow the top row from left to right, then answer the question below it. What to certify when the customer is not present is answered on the <a href=\"#ci-cdd\">Circulars page</a>.",
        "委聘獨立的合適人選認證文件，可防範所提供的文件與正接受身分核實的客戶不相符的風險。先由左至右閱讀上排方格，再回答下方的問題。客戶沒有現身時須認證哪些文件，答案見<a href=\"#ci-cdd\">通函一頁</a>。")
    + U.fig(fig_cert, ("Certification never shifts responsibility: the MSO remains liable for any failure to carry out the prescribed CDD.",
                       "認證從不轉移責任：金錢服務經營者仍須就未有執行訂明的盡職審查負上法律責任。"), CERT_KEY)
    + CERTIFIER_TABLE
    + U.traps(
        U.trap(("A non-resident at your counter: a valid travel document", "身在櫃位的非居民：有效旅遊證件"),
               ("Watch whether the question says the person is, or is not, physically present in Hong Kong: Appendix A lists the national identity card and national driving licence only for a non-resident who is not. The Guideline's main text also gives \"Hong Kong identity card or other national identity card\" as an example for verifying any individual customer.",
                "留意題目是否指明該人實際身在香港或沒有現身香港：附錄A只就沒有現身香港的非居民列出國民身分證及國家駕駛執照。指引正文亦把「香港身份證或其他國家的身份證」列為核實任何屬自然人的客戶身分的例子。"),
               cc(AX("1–2"), "¶4.3.3(a)"),
               vs=[(("Physically present in Hong Kong", "實際身在香港"),
                    ("A non-resident's identity should be verified by reference to a valid travel document.",
                     "非居民的身分應根據其有效旅遊證件核實。")),
                   (("Not physically present in Hong Kong", "沒有現身香港"),
                    ("You may use any one of three: a valid travel document, a national identity card with the person's photograph, or a national driving licence with a photograph.",
                     "應根據以下三者之一：有效旅遊證件、附有個人照片的國民身分證，或附照片的國家駕駛執照。"))]),
        U.trap(("A national driving licence, not an international driving permit", "國家駕駛執照，不是國際駕駛許可證"),
               ("The licence must be a current national one, issued by a competent national or state authority and carrying a photograph. International driving permits and licences are expressly not acceptable.",
                "執照須是由主管的國家或政府機構簽發、附照片的有效國家駕駛執照。國際駕駛許可證及執照明文不能使用。"),
               cc(AX("2(c)"), AF("72"))),
        U.trap(("Certifying a copy is not witnessing the licence form", "認證身分文件複本，不同於見證牌照表格"),
               None, cc(AX("8"), LG("5.8")),
               vs=[(("Certifier of a customer's ID copy (Appendix A)", "客戶身分文件複本的證明人（附錄A）"),
                    ("Examples: a s.18(3) intermediary, a member of the judiciary in an equivalent jurisdiction, an officer of the issuing country's embassy, consulate or high commission, a Justice of the Peace, or a professional such as an accountant, lawyer, notary public or chartered secretary.",
                     "例子：附表2第18(3)條的中介人、對等司法管轄區的司法人員、發證國家的大使館、領事館或高級專員公署人員、太平紳士，或會計師、律師、公證人、特許秘書等專業人士。")),
                   (("Witness to Appendix I of Form 3A (Licensing Guide)", "表格3A附錄I的見證人（《牌照指引》）"),
                    ("An authorised C&ED officer, a practising professional such as a solicitor, accountant or auditor, a notary public or a Justice of the Peace. This is for the fit-and-proper declaration in a licence application, not for customers (see <a href=\"#gl-route\">Getting licensed</a>).",
                     "海關的獲授權人員、執業專業人士（例如事務律師、會計師或核數師）、公證人或太平紳士。這是牌照申請中的適當人選聲明所用，與客戶無關（見<a href=\"#gl-route\">申領牌照一節</a>）。"))]),
    ))
