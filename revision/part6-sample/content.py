"""Authored bilingual Part 6 study content; source IDs follow docs/catalog.json."""

def P(tc, en):
    return {"tc": tc, "en": en}


def R(doc, loc):
    return {"doc": doc, "loc": loc}


def row(tc, en, *refs):
    assert len(tc) == len(en)
    return {"cells": [P(a, b) for a, b in zip(tc, en)], "refs": list(refs)}


def table(tc, en, rows):
    return {"kind": "table", "head": [P(a, b) for a, b in zip(tc, en)], "rows": rows}


def flow(tc, en, steps, *refs):
    return {"kind": "flow", "title": P(tc, en), "steps": [P(a, b) for a, b in steps], "refs": list(refs)}


def note(tc, en, *refs):
    return {"kind": "note", "text": P(tc, en), "refs": list(refs)}


def example(tc, en, *refs):
    return {"kind": "example", "text": P(tc, en), "refs": list(refs)}


def section(key, tc, en, intro_tc, intro_en, questions, *blocks):
    return {"id": key, "title": P(tc, en), "intro": P(intro_tc, intro_en),
            "questions": questions.split(), "blocks": list(blocks)}


SECTIONS = [
section("start", "先判斷何時須做客戶盡職審查", "Decide when customer due diligence is required",
        "先分清業務關係和非經常交易，再檢查門檻、關連交易及懷疑。金額低於門檻，不等於可以忽略風險。",
        "Distinguish a business relationship from an occasional transaction, then check thresholds, linked transactions and suspicion. Below-threshold activity does not remove risk obligations.",
        "m6-346 m6-357 m6-442 m6-470 m6-478",
 flow("開始交易前的判斷順序", "A decision path before acting", [
     ("有洗錢／恐怖分子資金籌集懷疑，或舊身分資料有疑點？ → 須執行盡職審查；有相關知悉或懷疑時，按規定舉報。", "ML/TF suspicion, or doubt about previous identification data? → Apply CDD; report relevant knowledge or suspicion as required."),
     ("沒有上述情況，而將建立業務關係？ → 須在建立前執行盡職審查；延後核實僅屬有條件的例外。", "Otherwise, establishing a business relationship? → Apply CDD before establishment; delayed verification is only a conditional exception."),
     ("只是非經常交易？ → 判斷交易種類，並合併看似有關連的操作；達適用門檻須先完成盡職審查。", "Only an occasional transaction? → Identify the transaction type and aggregate apparently linked operations; complete CDD first when the applicable threshold is met.")],
     R("03", "¶4.2.1–4.2.5; ¶4.7.1; ¶4.13.1"), R("04", "Sch.2 s.3(1)–(4)")),
 table(["情況／數字", "如何處理", "容易混淆"], ["Situation / number", "What follows", "Easy to confuse"], [
     row(["業務關係", "延續一段時間是關係的元素，或首次接觸時經營者有此預期。了解關係目的及擬具有的性質；非自然人亦須了解業務性質。", "不是達到某個金額後才做盡職審查。"],
         ["Business relationship", "Duration is an element, or is expected at first contact. Understand its purpose and intended nature, and the nature of a non-individual customer's business.", "CDD does not wait for a monetary threshold."], R("03", "¶4.2.1(a); ¶4.2.2; ¶4.6.1")),
     row(["120,000港元或以上", "一般非經常交易須在交易前執行盡職審查；包括其他貨幣同等款額及有關連的操作。", "等於門檻已包括在內；不能只看單筆。"],
         ["HK$120,000 or more", "Apply CDD before a general occasional transaction, including the equivalent in other currencies and linked operations.", "Equality counts; do not assess each payment in isolation."], R("03", "¶4.2.1(b)(i); ¶4.2.4–4.2.5")),
     row(["8,000港元或以上", "非經常電傳轉帳及指引所述虛擬資產轉帳適用此盡職審查門檻。", "不能將所有非經常交易一律套用120,000元。虛擬資產轉帳另須留意附表2第13A條；本章重點為金錢服務。"],
         ["HK$8,000 or more", "This CDD threshold applies to occasional wire transfers and the virtual-asset transfers described in the Guideline.", "The HK$120,000 threshold is not universal. Virtual-asset transfers also engage Schedule 2 s.13A; this chapter focuses on money services."], R("03", "¶4.2.1(b)(ii)–(iii), fn14")),
     row(["第三方現金交易達120,000元", "如進行交易者的姓名不在帳戶委託書上，應要求身分證明文件，並存檔複本供持續監察。", "這項特定規定，與第三方支付通函的一般風險管控須分開理解。"],
         ["Third-party cash transaction of HK$120,000 or more", "If the transactor is not on the account mandate, request identification documents and retain copies for ongoing monitoring.", "Distinguish this specific requirement from the wider third-party payment controls."], R("03", "¶4.2.6")),
     row(["先前客戶", "特指2012年4月1日前建立關係的客戶。異常或可疑交易、帳戶運作大變、懷疑或舊資料疑點均可觸發盡職審查；持續監察仍適用。", "不是一般口語的『以前來過的客戶』；也不是永久豁免。"],
         ["Pre-existing customer", "Specifically, a relationship established before 1 April 2012. Unusual or suspicious activity, material operating changes, suspicion or data doubts trigger CDD; ongoing monitoring still applies.", "Not simply a returning customer, and not a permanent exemption."], R("03", "¶4.12.1–4.12.3"))]),
 example("說明例：街客在一小時內向同一收款人作三筆每筆3,000元的有關連電傳轉帳。總額9,000元；不能因每筆低於8,000元而避開盡職審查。『有關連』仍須按交易特徵及時間判斷。",
         "Illustration: a walk-in makes three linked HK$3,000 wire transfers to the same recipient in an hour. The total is HK$9,000; the individual amounts do not avoid CDD. Linkage still depends on the characteristics and timing.", R("03", "¶4.2.1–4.2.5"))),

section("identity", "分清客戶、代表及有關連者", "Separate the customer, representative and connected parties",
        "公司派人開戶，客戶仍然是公司。身分識別資料、身分核實及代表授權是三件相關但不同的事。",
        "A company remains the customer when it sends a representative. Identification data, identity verification and authority are related but separate tasks.",
        "m6-ca7 m6-341 m6-343 m6-345 m6-354 m6-358 m6-359 m6-362 m6-369 m6-396 m6-410 m6-412 m6-417 m6-430 m6-444 m6-446 m6-479 m6-482",
 table(["對象", "要掌握的規則", "容易混淆"], ["Subject", "Rule to learn", "Easy to confuse"], [
     row(["自然人", "最低識別資料：全名、出生日期、國籍、獨特識別號碼及文件類別。核實姓名、出生日期、識別號碼及文件類別；並索取住址資料。", "收集資料不等於每一項均須核實；性別不在這份最低識別資料清單。一般並非一律要求住址證明。"],
         ["Individual", "Minimum identification data: full name, date of birth, nationality, unique identification number and document type. Verify name, date of birth, number and document type; obtain residential address information.", "Collection does not mean verifying every data item. Sex is not on this minimum list. Address proof is not universally required."], R("03", "¶4.3.2–4.3.5, fn18; ¶4.3.13")),
     row(["法人", "最低識別資料：全名；註冊／成立／登記日期及地點（含註冊辦事處地址）；識別號碼及文件類別；主要營業地點（如不同）。核實名稱、法定形式、現時仍然存在及規管和約束的權力。", "公司註冊證明書通常不能單獨證明公司目前仍然存在。公司秘書不在這份最低識別資料清單。"],
         ["Legal person", "Collect full name; incorporation/establishment/registration date and place (including registered office); number and document type; principal business place if different. Verify name, legal form, current existence and powers that regulate and bind it.", "An incorporation certificate alone usually does not establish current existence. Company secretary is not on this minimum identification list."], R("03", "¶4.3.6–4.3.7, fn19–20")),
     row(["合夥、非法團團體及其他組織", "可參考登記紀錄、合夥協議或契約；有時仍需其他文件了解權力。眾所周知、有信譽、歷史悠久且公開資料充足的合夥或非法團團體，確認專業／行業會員身分可能足夠。其他組織應確認其合法目的。", "不能把有條件的會員身分做法套用所有合夥。"],
         ["Partnership, unincorporated body and other organisations", "Use registration records, partnership agreements or deeds; additional evidence of powers may be needed. Professional/trade membership may suffice for a well-known, reputable, long-established partnership or unincorporated body with ample public information. Be satisfied about other organisations' legitimate purposes.", "The conditional membership route is not available to every partnership."], R("03", "¶4.3.8–4.3.9"), R("06", "AML/CFT Q7")),
     row(["看似代表客戶行事的人", "按角色、活動及風險判斷；識別並採取合理措施核實身分，亦須用適當文件核實授權，例如董事會決議或類似書面授權。", "已知其身分不等於已核實授權；代表毋須必然是董事或實益擁有人。低風險關係可按常見問題第12題，參考客戶獨立部門確認的代表名單核實。"],
         ["Person purporting to act for the customer", "Assess role, activities and risk. Identify and take reasonable measures to verify identity, and verify authority with suitable documentary evidence, such as a board resolution or similar written authority.", "Knowing identity does not verify authority. The representative need not be a director or BO. In a low-risk relationship, FAQ12 allows verification against a list confirmed by the customer's independent department."], R("03", "¶4.5.1–4.5.4"), R("06", "AML/CFT Q9, Q12"), R("07", "Appendix (3)")),
     row(["有關連者", "法人、信託等的有關連者須收集姓名：法團董事、合夥人、信託受託人；其他情況為高級管理或掌握執行權力的自然人。", "若同一人亦屬客戶、實益擁有人或代表，須履行該身分的識別及核實要求，不能停留於收集姓名。"],
         ["Connected parties", "Obtain names: directors for a corporation, partners for a partnership, trustees for a trust; otherwise natural persons in senior management or with executive authority.", "A party who is also a customer, beneficial owner or representative attracts the requirements of that role; obtaining a name is not enough."], R("03", "¶4.3.18–4.3.19, fn26")),
     row(["公司地址與客戶更名", "主要營業地點是主要營運／活動地點，可與註冊地址不同。可靠獨立文件已載註冊地址，可接納，除非知悉並非現況。客戶更名後須核實新姓名，並以現有紀錄核對其他資料。", "建立關係前已更名，僅須識別及核實現名。地址與已知業務不符時應跟進原因。"],
         ["Business address and name changes", "Principal business place is the main operating/activity location and may differ from registered office. An address in reliable independent evidence may be accepted unless known to be out of date. Verify a changed name and cross-check other data against existing records.", "A name changed before onboarding requires identification and verification of the current name only. Follow up addresses inconsistent with the known business."], R("06", "AML/CFT Q4–Q6"))]),
 note("可用可靠獨立來源包括政府、有關主管當局、相類似的海外主管當局、關長認可的數碼識別系統及其他認可來源。文件應反映提交／取得時的現況；外語文件亦須有合理理由信納其身分證據效力。",
      "Reliable independent sources include government, relevant authorities, equivalent overseas authorities, recognised digital identification systems and other recognised sources. Evidence should be current when supplied or obtained; take appropriate steps to be reasonably satisfied about foreign-language evidence.", R("03", "¶4.3.1; ¶4.3.14–4.3.17"))),

section("ownership", "沿擁有權追查實益擁有人", "Trace ownership and control to beneficial owners",
        "不要只找大股東。最終管理控制權、代他人行事、信託角色及代名人安排都可能改變判斷。",
        "Do not stop at large shareholders. Ultimate management control, acting for another person, trust roles and nominee arrangements can change the result.",
        "m6-342 m6-344 m6-360 m6-361 m6-397 m6-413 m6-445 m6-480 m6-481 m6-493 m6-495",
 flow("追查的三層問題", "Three questions when tracing ownership", [
     ("客戶是誰、屬甚麼法律形式？ → 識別所有中介層，了解擁有權及控制權結構。", "Who is the customer and what is its legal form? → Identify intermediate layers and understand ownership and control."),
     ("誰最終擁有或控制？有否代他人行事？ → 按法團、合夥、信託等相應定義逐一判斷。", "Who ultimately owns or controls it? Is it acting for another? → Apply the relevant corporation, partnership, trust or other definition."),
     ("法人沒有符合定義的自然人？ → 識別相關高級管理自然人，並採取合理措施核實；不能直接略過。", "No natural person meets the definition for a legal person? → Identify the relevant senior managing natural person and take reasonable verification measures; do not skip the step.")], R("03", "¶4.4.4–4.4.13")),
 table(["情況", "判斷及措施", "容易混淆"], ["Situation", "Decision and measures", "Easy to confuse"], [
     row(["法團／合夥", "法團：股本或投票權25%以上，或最終管理控制權；合夥：資本／利潤或投票權25%以上，或最終管理控制權。亦包括客戶代其行事的另一人。", "門檻是超過25%，不是25%或以上；沒有股份亦可能因管理控制權而符合。"],
         ["Corporation / partnership", "Corporation: more than 25% of share capital or voting rights, or ultimate management control. Partnership: more than 25% of capital/profits or voting rights, or ultimate management control. Also includes another person on whose behalf the customer acts.", "More than 25%, not 25% or more. Control may qualify without shares."], R("03", "¶4.4.6–4.4.9")),
     row(["自然人客戶", "一般視客戶本人為實益擁有人；如有跡象顯示並非為自己行事，須適當查詢。", "不能把一般做法變成『永遠不用查其他人』。"],
         ["Individual customer", "Normally treat the individual as the beneficial owner, but make appropriate enquiries if indications suggest otherwise.", "The normal approach is not a rule that other persons can always be ignored."], R("03", "¶4.4.5")),
     row(["信託", "識別財產授予人、受託人、保護人及執行人（如有）、受益人或類別，以及最終控制的自然人；採取合理措施核實。按類別指定的受益人，須有足夠資料在付款或行使權益時確立其身分。", "實益擁有人的法定定義不能一概縮成『只限自然人』；例如財產授予人或受託人可屬法人。"],
         ["Trust", "Identify settlor, trustee, protector/enforcer if any, beneficiaries or class, and natural persons with ultimate control; take reasonable verification measures. Obtain enough class-beneficiary information to establish identity on payout or exercise of rights.", "Do not narrow the statutory definition to natural persons only: for example, a settlor or trustee may be a legal person."], R("03", "¶4.4.10–4.4.12"), R("04", "Sch.2 s.1(1), beneficial owner")),
     row(["信託客戶與受託人", "信託本身須識別及核實；受託人代不具獨立法人身分的信託建立關係時，視受託人為客戶。信託資料包括名稱、成立／結算日期、管治司法管轄區、官方識別號碼（如有）及文件類別、註冊地址（如適用）。", "信託契據並非唯一證據：亦可參考合適登記冊、專業受託人或已閱文書律師的確認等。受託人兼具角色時用較嚴格相關要求。"],
         ["Trust customer and trustee", "Identify and verify the trust; treat a trustee as customer when acting for a trust without separate legal personality. Collect name, establishment/settlement date, governing jurisdiction, official number if any and document type, and registered office if applicable.", "A deed is not the only evidence: suitable registers and confirmations from professional trustees or lawyers who reviewed instruments are examples. Apply the stricter relevant requirements where roles overlap."], R("03", "¶4.3.10–4.3.12, fn22–25")),
     row(["複雜架構／代名人", "了解中介層及複雜架構的合法理由；對代名人及其代表的人取得足夠身分證據和安排詳情。", "理解架構是責任；索取架構圖及例行核實每一中介公司，並非一律強制。"],
         ["Complex structure / nominee", "Understand intermediate layers and the legitimate reason for complexity. Obtain satisfactory evidence of a nominee and the person represented, plus arrangement details.", "Understanding is required; an ownership chart and routine verification of every intermediate company are not universally mandatory."], R("03", "¶4.4.13–4.4.14; ¶4.4.18"), R("06", "AML/CFT Q8")),
     row(["持票人股份", "已交認可／註冊保管人：尋求獨立證據並在定期覆核時確認。未交保管人：開戶前及其後每年向每名實益擁有人索取聲明，並要求即時通知擁有權變更。", "保管人證據與每年聲明是兩種情況，不能互換。相同措施適用指引所述不記名認股權證。"],
         ["Bearer shares", "With an authorised/registered custodian: seek independent evidence and confirm in periodic reviews. Without one: obtain each beneficial owner's declaration before opening and annually thereafter; require immediate ownership-change notification.", "Custodian evidence and annual declarations address different cases. The same measures apply to the bearer warrants described in the Guideline."], R("03", "¶4.4.15–4.4.17, fn30"))]),
 note("實益擁有人是『識別＋合理措施核實』，不能把客戶本人的核實規定原樣套用，也不能只接受聲明而不考慮風險。合理措施應足以令經營者信納知道對方是誰。",
      "For beneficial owners, identify and take reasonable verification measures. Do not mechanically apply the customer's verification standard or accept declarations without considering risk. Measures must satisfy the MSO that it knows who the owner is.", R("03", "¶4.4.1–4.4.4"))),

section("documents", "選對身分證據及認證方法", "Choose the right identity evidence and certification",
        "證件是否適用，取決於人在哪裏、證件是否有效，以及個別例外；有認證也不會免除經營者責任。",
        "Suitable documents depend on location, validity and specific exceptions. Certification does not remove the MSO's responsibility.",
        "m6-353 m6-447",
 table(["情況", "可用方法／條件", "容易混淆"], ["Situation", "Method / conditions", "Easy to confuse"], [
     row(["身在香港", "香港居民通常用香港身份證或簽證身分書；非居民用有效旅遊證件。", "不能把不在香港的非居民可用文件清單，直接套用櫃枱情況。"],
         ["Physically in Hong Kong", "Normally use a Hong Kong resident's identity card or Document of Identity for Visa Purposes; use a non-resident's valid travel document.", "Do not import the overseas non-resident document list into an in-person Hong Kong case."], R("03", "Appendix A ¶1–2")),
     row(["不在香港的非居民", "有效國際護照／其他旅遊證件，或附照片的有效國民身分證，或合適國家機構發出的有效國家駕駛執照。", "國際駕駛許可證及執照不適用這條途徑；澳門永久居民身分證則在指引列作旅遊證件。"],
         ["Non-resident outside Hong Kong", "Valid international passport/other travel document, valid national identity card with photograph, or valid national driving licence issued by a competent national/government authority.", "International driving permits/licences do not qualify under this route. The Guideline lists Macau's permanent resident identity card as a travel document."], R("03", "Appendix A ¶2–3, fn72")),
     row(["未成年人及特殊證件情況", "香港出生且沒有有效旅遊證件或香港身份證的未成年人可用香港出生證明書；同時記錄並核實陪同／代表的父母或監護人身分。特殊情況無照片文件，經妥善評估及減低風險後可接納。", "未成年人身分核實不取代父母／監護人識別；無照片也不是一概接受。"],
         ["Minors and exceptional documents", "A Hong Kong-born minor without a valid travel document or identity card may use a Hong Kong birth certificate; record and verify the accompanying/representing parent or guardian too. Exceptionally, non-photographic evidence may be accepted after proper risk assessment and mitigation.", "The minor's verification does not replace the parent/guardian step. Missing photographs are not generally acceptable without assessment."], R("03", "¶4.3.4; Appendix A ¶4, ¶6")),
     row(["認證複本", "證明人須查閱正本，在複本簽署及註明日期，以大楷清楚列明姓名及職位／身分，並確認為真確複本或同等字句。例子包括指明中介人、對等司法管轄區司法人員、證件發出國的大使館／領事館／高級專員公署人員、太平紳士及合適專業人士。", "名單非詳盡；一般客戶自行認證不足。法人內受專業操守規管並以專業身分認證的人士，可屬註74的例外。認證不能確定真確性或與客戶的關係有疑時，仍應採額外措施減低風險。"],
         ["Certified copies", "The certifier must see the original, sign/date the copy, clearly print their name in capitals and state position/capacity, and certify a true copy or equivalent. Examples include specified intermediaries, a judicial officer in an equivalent jurisdiction, an issuing-country embassy/consulate/high-commission officer, a JP and suitable professionals.", "The list is non-exhaustive. Self-certification is generally insufficient; footnote 74 allows a qualifying professional within a legal-person customer. Uncertain authenticity or a suspected mismatch with the customer still requires extra mitigation."], R("03", "Appendix A ¶7–10, fn74–76"))])),

section("timing", "處理延後核實及非面對面業務", "Handle delayed verification and non-face-to-face business",
        "把『何時核實』和『用甚麼渠道核實』分開。延後核實並非方便客戶就可使用；非面對面亦不代表不能建立關係。",
        "Separate when verification occurs from the channel used. Convenience alone does not justify delay, and remote onboarding is not prohibited.",
        "m6-352 m6-363 m6-414 m6-483 m6-485",
 table(["情況", "條件及行動", "容易混淆"], ["Situation", "Conditions and action", "Easy to confuse"], [
     row(["例外延後核實", "只適用建立業務關係：有效管理延誤帶來的風險；為不干擾正常業務而有必要；合理地切實可行範圍內盡快完成。另須定完成時限、交易限制、異常監察及向高級管理層報告未完成個案。", "達門檻非經常交易須先完成盡職審查，不能借用這項例外。"],
         ["Exceptional delayed verification", "For a business relationship only: effectively manage delay risks; delay must be essential not to interrupt normal business; complete as soon as reasonably practicable. Set deadlines, transaction limits, unusual-activity monitoring and reporting of outstanding cases to senior management.", "A threshold-triggered occasional transaction needs CDD first; this exception does not transfer to it."], R("03", "¶4.7.1–4.7.3"), R("04", "Sch.2 s.3(1)–(3)")),
     row(["延後期間向第三者付款", "原則上確保不支付。例外須同時：無懷疑、風險低、高級管理層先考慮業務性質後批准，及收款人姓名與監察名單不吻合。", "管理層批准只是其中一項，不能取代其他條件。"],
         ["Third-party payout while verification is pending", "Normally ensure no payout. Exception requires all: no ML/TF suspicion, low assessed risk, senior approval after considering business nature, and no recipient-name match on watch lists.", "Approval is one condition, not a substitute for the others."], R("03", "¶4.7.3(e)")),
     row(["未能按時完成", "合理地切實可行範圍內盡快終止關係，避免進一步交易；可行時以原狀退回資金／資產除外。評估未能核實有否引起知悉或懷疑，並考慮可疑交易報告。", "不能照客戶要求任意轉給陌生人或把現金轉成另一資產。"],
         ["Verification not completed in time", "Terminate as soon as reasonably practicable and avoid further transactions, except returning funds/assets in their original form where possible. Assess knowledge/suspicion and consider an STR.", "Do not freely redirect funds to strangers or convert cash to another asset at the customer's request."], R("03", "¶4.7.4; ¶4.13.1")),
     row(["客戶未現身", "除認可數碼識別例外外，須至少一項：用未曾使用的可靠獨立證據進一步核實；增補措施核實已取得資料；或經符合條件的客戶本人銀行戶口作出首次付款。", "不是三項全部必做；首次付款銀行仍須符合附表2第9(1)(c)條的機構、監管等條件。"],
         ["Customer not physically present", "Unless the recognised digital-ID exception applies, use at least one: further verification using unused reliable independent evidence; supplementary checks on existing information; or first payment from the customer's own bank account meeting every condition in ¶4.10.1(c).",
          "Not all three are mandatory. The first-payment institution must meet the paragraph's institutional and supervisory conditions."], R("03", "¶4.10.1–4.10.4"), R("04", "Sch.2 s.9(1)(c)")),
     row(["認可數碼識別／法人遙距開戶", "以關長認可為可靠及獨立來源的數碼識別系統核實身分，無須執行第4.10.1段額外措施。法人透過非面對面渠道開戶，或只提供文件複本，仍應減低增加的風險。", "一般視像通話或掃描證件，不會自動成為認可數碼識別系統。代表是員工而非董事，並非本身禁止開戶。"],
         ["Recognised digital ID / remote corporate onboarding", "Verification using a digital ID system recognised by the Commissioner as reliable and independent removes the ¶4.10.1 additional measures. A legal person onboarded remotely or using only document copies still needs mitigation of increased risks.", "An ordinary video call or scanned document does not automatically become a recognised digital-ID system. An authorised employee need not be a director."], R("03", "¶4.10.2; ¶4.10.5"), R("06", "AML/CFT Q9"))])),

section("risk", "分清簡化、一般及更嚴格審查", "Distinguish simplified, normal and enhanced due diligence",
        "低風險可以調整程度，但不是不做審查。高風險措施應針對風險，並繼續處理採取措施後的剩餘風險。",
        "Lower risk can change intensity, not remove due diligence. Enhanced measures should address the risk and any risk remaining afterwards.",
        "m6-351 m6-364 m6-365 m6-366 m6-371 m6-427 m6-428 m6-429",
 table(["情況", "可行做法及限制", "容易混淆"], ["Situation", "Approach and limits", "Easy to confuse"], [
     row(["低風險", "須有適當分析支持。可降低資料更新頻率、監察程度，或按交易／關係推斷目的，但仍須持續監察。", "風險不再低、產生懷疑或舊身分資料有疑點時，不應執行或繼續簡化措施。"],
         ["Low risk", "Support the assessment with appropriate analysis. Examples include less frequent updates, lower monitoring intensity or inferring purpose from the transaction/relationship; ongoing monitoring remains required.", "Do not apply or continue SDD if risk is no longer low, suspicion arises or identity data is doubtful."], R("03", "¶4.8.2–4.8.8")),
     row(["特定客戶的實益擁有人簡化安排", "第4.8.10段列出金融機構、符合全部條件的對等地機構、上市法團、合資格投資公司及政府／公共機構等類別。上市客戶另應評估披露規定是否確保實益擁有權透明。", "只是有關實益擁有人識別及核實的安排；不是整套客戶盡職審查豁免。上層合資格實體以外的無關連實益擁有人仍須處理。"],
         ["BO simplification for specified customers", "¶4.8.10 lists financial institutions, equivalent-jurisdiction institutions meeting all conditions, listed corporations, qualifying investment companies and government/public bodies. For a listed customer, assess whether disclosure requirements ensure ownership transparency.", "This concerns BO identification/verification, not exemption from all CDD. Unrelated beneficial owners outside a qualifying entity's chain still need attention."], R("03", "¶4.8.9–4.8.12")),
     row(["代名人／投資公司帳戶", "第4.8.13段安排須有金融機構對相關客戶／投資公司完成適用盡職審查，並獲合約授權操作帳戶。投資公司或獲委任機構須符合第4.8.14–4.8.15段類別及制度條件。", "沒有合資格機構時，仍須識別超過25%權益投資者並採取合理措施核實；書面陳述是否適當取決於風險，接納情況須記錄並定期覆核。"],
         ["Nominee / investment company accounts", "¶4.8.13 requires the financial institution to have completed applicable CDD on underlying customers/investment company and contractual account authority. Investment companies/appointed institutions must satisfy ¶4.8.14–4.8.15 institutional and system conditions.", "Without a qualifying institution, identify investors with more than 25% and take reasonable verification measures. Reliance on representations is risk-dependent and must be documented and periodically reviewed."], R("03", "¶4.8.13–4.8.16")),
     row(["退休及低額人壽產品", "須符合第4.8.17段產品條件。退休供款由受僱收入扣減且利益不可轉讓；相關保單須不可退回及不可抵押；人壽保單每年保費不多於8,000元，或整付保費不多於20,000元。", "這裏的8,000元是保費條件，並非電傳轉帳門檻。與僱員另建業務關係仍須盡職審查。"],
         ["Retirement and low-value life products", "Meet ¶4.8.17 product conditions: employment-income contributions and non-assignable benefits; relevant policies without surrender clauses or collateral use; life premiums no more than HK$8,000 annually or HK$20,000 single premium.", "This HK$8,000 is a premium condition, not the wire-transfer threshold. A separate employee relationship still requires CDD."], R("03", "¶4.8.17–4.8.18")),
     row(["律師當事人戶口", "簡化安排須戶口以律師／律師行名義開設，當事人金錢或證券混合，並由其以代理人身分管理。", "單一客戶，或每名客戶有附屬戶口且資金未在經營者內匯集時，除核實律師外亦應識別相關當事人。"],
         ["Lawyer's client account", "The simplification requires an account in the lawyer/firm's name, pooled clients' money/securities and management as agent.", "For a single client or individual subaccounts without pooling at the MSO, identify underlying clients in addition to verifying the lawyer."], R("03", "¶4.8.19–4.8.20")),
     row(["高風險", "建立／維持高風險業務關係應取得高級管理層批准並加強持續監察。按具體風險採取額外資料、財富／資金來源、交易原因等措施；不要求每宗個案一律採用全部例子。剩餘風險可另設交易限額或帳戶限制。", "政治人物有指定整套措施，須另看下一節；不能用一般高風險措施的選擇性取代。"],
         ["High risk", "Obtain senior approval to establish/continue a high-risk business relationship and intensify its monitoring. Tailor additional information, wealth/funds enquiries and transaction-reason checks to risk; not every example is expected in every case. Address residual risk with measures such as limits or account restrictions.", "PEPs have a specified package in the next section; general flexibility does not replace it."], R("03", "¶4.9.1–4.9.6, fn36"), R("04", "Sch.2 s.15")),
     row(["司法管轄區與匿名戶口", "對特別組織呼籲的司法管轄區，按風險比例更嚴格審查並遵守關長書面通知。對等司法管轄區包括香港以外特別組織成員或有類似規定者；後者評估須記錄並定期／觸發覆核。不得開立匿名或虛構姓名戶口。", "保密號碼戶口仍須知道真實身分、同樣盡職審查及監察；轉帳及匯款用真名，並向獲授權人士提供紀錄。"],
         ["Jurisdictions and anonymous accounts", "Apply proportionate EDD for FATF-call jurisdictions and comply with written Commissioner notices. Equivalence includes FATF members other than Hong Kong or jurisdictions with similar requirements; document the latter assessment and review periodically/on triggers. No anonymous or fictitious-name accounts.", "Numbered accounts still require true identity, full CDD and monitoring; transfers/remittances use real names, and records remain available to authorised persons."], R("03", "¶4.14.1, fn49–50; ¶4.15.1–4.16.3"))])),

section("pep", "政治人物：先分類，再決定措施", "PEPs: classify first, then select measures",
        "政治人物並非只限公職人員本人；指定家人及關係密切的人亦在範圍內。卸任本身不會自動終止更嚴格審查。",
        "PEPs include specified family members and close associates, not only office-holders. Leaving office does not automatically end enhanced measures.",
        "m6-349 m6-350 m6-367 m6-368 m6-388 m6-415 m6-416 m6-448 m6-494",
 table(["類別／問題", "應掌握的判斷", "容易混淆"], ["Category / issue", "Decision to learn", "Easy to confuse"], [
     row(["非香港政治人物", "設有效程序斷定客戶或實益擁有人是否符合。建立關係前，或其後發現而維持關係前，執行全部三項：高級管理層批准、合理措施確立財富及資金來源、更嚴格持續監察。", "不能因自評低風險便略去整套措施；前政治人物的風險為本例外另有條件。"],
         ["Non-Hong Kong PEP", "Maintain effective identification procedures for customers and BOs. Before establishment, or continuation after later discovery, apply all three: senior approval, reasonable measures to establish wealth and funds sources, and enhanced ongoing monitoring.", "A low self-assessed risk does not by itself remove the package; the former-PEP exception has separate conditions."], R("03", "¶4.9.7–4.9.12")),
     row(["香港／國際組織政治人物", "採取合理措施識別；與其建立高風險關係前、現有關係轉為高風險時，或既有高風險關係後來發現其身分時，執行同一整套更嚴格措施。", "不能說所有類別均不問風險一律觸發同一規定；國際組織是指引界定的政府間組織，不是任何跨國公司。"],
         ["Hong Kong / international organisation PEP", "Take reasonable identification measures. Apply the same package before high-risk establishment, when a relationship becomes high risk, or when a high-risk customer's PEP status is later discovered.", "The trigger is not identical for every category. An international organisation means the Guideline's intergovernmental entities, not any multinational company."], R("03", "¶4.9.13–4.9.17")),
     row(["家人與關係密切的人", "範圍包括配偶、伴侶、子女、父母、子女配偶／伴侶；關係密切的人按共同實益擁有權、密切業務關係或為其利益設立實體等定義判斷。中級及更低級官員不在重要公職例子內。", "『認識某官員』不是自動符合定義；兄弟姊妹亦不在這份指定家人清單。"],
         ["Family and close associates", "Includes spouse, partner, child, parent and child's spouse/partner. Assess associates through the defined joint ownership, close business relationship or entity established for the PEP's benefit. Middle-ranking and junior officials are excluded from the prominent-office examples.", "Knowing an official is not automatically enough; siblings are not on this specified family list."], R("03", "¶4.9.7–4.9.8; ¶4.9.13–4.9.14; ¶4.9.22")),
     row(["前政治人物", "須適當風險評估、判斷不再構成高風險並獲高級管理層批准，才可不採取／停止指定更嚴格措施。考慮剩餘影響力、原職位等級、以往與現有職能連繫，保存評估。", "不能僅訂退休後若干月／年便自動解除。批准人須有一定資歷，並有明文政策；如反映組織及風險管理方法，可包括其他司法管轄區人員。"],
         ["Former PEP", "Only cease/omit specified enhanced measures after appropriate assessment establishes no continuing high risk and senior management approves. Consider influence, former seniority and links between former/current functions; retain the assessment.", "No automatic retirement time limit. Approvers need sufficient seniority and documented policy; overseas personnel may qualify if consistent with the organisation and risk-management approach."], R("03", "¶4.9.12, fn37–38; ¶4.9.18, fn41–42"), R("06", "AML/CFT Q20–Q21")),
     row(["財富來源／資金來源", "財富來源是全部財富如何累積；資金來源是特定資金／資產由甚麼活動產生。按風險索取及核對有實質內容的資料。", "只知道從哪家銀行匯出，不能取代了解產生資金的活動；商業政治人物數據庫只屬支援，不能取代傳統盡職審查。"],
         ["Source of wealth / source of funds", "Wealth: how total assets were accumulated. Funds: the activity generating the specific money/assets. Obtain and corroborate substantive information on a risk basis.", "Knowing the sending bank does not establish the generating activity. Commercial PEP databases support, rather than replace, traditional CDD."], R("03", "¶4.9.21; ¶4.9.23–4.9.26"), R("06", "AML/CFT Q16"))])),

section("intermediary", "依賴中介人：工作可借助，責任仍在", "Relying on intermediaries: keep control and responsibility",
        "先確認中介人資格，再確認資料何時取得、如何取回文件及合作終止時的安排。外判與法定的依賴中介人不是同一概念。",
        "Check eligibility, immediate information access, document retrieval and exit arrangements. Outsourcing differs from statutory reliance on an intermediary.",
        "m6-370 m6-386 m6-426 m6-484",
 table(["關鍵問題", "規則", "容易混淆"], ["Key question", "Rule", "Easy to confuse"], [
     row(["依賴還是外判？", "依賴通常由已有客戶關係的第三方按其本身程序執行；外判／代理則按經營者程序代為執行並受其管控。經營者仍負最終責任；不能藉依賴中介人履行自己的持續監察責任。", "用第三方不代表轉移法律責任。"],
         ["Reliance or outsourcing?", "Reliance usually uses a third party's own procedures and existing customer relationship; an outsourced agent uses the MSO's procedures under its control. Ultimate responsibility remains with the MSO; its own ongoing monitoring cannot be satisfied by intermediary reliance.", "Using a third party does not transfer legal responsibility."], R("03", "¶4.11.1–4.11.2, fn44")),
     row(["何時拿資料？", "取得書面同意擔任中介人及列明工作範圍。中介人完成措施後須立刻取得相關數據／資料；文件複本及紀錄可按規定應要求提供。", "不是所有文件複本也必須同時立刻取得，但須確保能沒有延誤地取回。"],
         ["When is information obtained?", "Obtain written agreement and the CDD scope. Obtain relevant data/information immediately after the measures; copies and records may be retrieved on request under the requirements.", "Immediate data access is distinct from simultaneous receipt of every document copy, but prompt retrieval must be assured."], R("03", "¶4.11.3–4.11.4")),
     row(["如何監察及退出？", "取得保留資料承諾：關係期間及終止後至少5年或關長指定時間；即將結業／停止擔任中介人時提供全部相關資料。定期抽樣測試；可靠性有疑立即合理覆核，終止合作立即取回全部資料。", "如對過往措施存疑，仍須在合理地切實可行範圍內盡快補做所需盡職審查。"],
         ["Monitoring and exit", "Obtain retention undertakings for the relationship and at least five years after termination or the Commissioner's specified time, plus full data on closure/cessation. Sample-test retrieval; immediately review reliability doubts and obtain all CDD information on termination.", "Doubts about earlier work require necessary CDD as soon as reasonably practicable."], R("03", "¶4.11.5–4.11.7")),
     row(["本地／海外／相關外地機構", "本地中介人須屬列明類別，專業人士等另須有足夠程序及就該客戶受附表2相關規定約束。海外中介人須符合對等地、業務／專業、註冊／領牌／規管、相類似措施及監管條件。相關外地金融機構另須符合關係、集團政策及集團監管等條件。", "同一集團或有專業牌照，本身都不足以自動合資格；外地成立／經遷冊等情況應按現行法定定義逐項判斷。"],
         ["Local / overseas / related foreign institution", "Local intermediaries must be listed types; professionals also need adequate procedures and relevant Schedule 2 duties for that customer. Overseas eligibility includes equivalence, business/profession, registration/licensing/regulation, similar measures and supervision. Related foreign institutions have separate relationship, group-policy and group-supervision tests.", "Group membership or a professional licence alone is insufficient. Apply the current statutory definition to foreign-incorporation/redomiciliation cases."], R("03", "¶4.11.8–4.11.14"), R("04", "Sch.2 s.18(3)–(7)"))])),

section("monitoring", "持續監察：先查原因，再作決定", "Ongoing monitoring: investigate before deciding",
        "持續監察包括更新盡職審查資料及審查交易。看整段關係和相關帳戶，不能只看每筆付款是否低於門檻。",
        "Ongoing monitoring covers CDD updates and transaction scrutiny. Assess the relationship and linked accounts, rather than only individual payment thresholds.",
        "m6-347 m6-348 m6-372 m6-373 m6-486 m6-487",
 flow("發現不尋常交易後", "After detecting unusual activity", [
     ("審查背景及目的 → 適當詢問客戶／取得額外資料；如合理相信繼續查詢會通風報訊，可停止該程序並記錄及舉報。", "Examine background and purpose → Make appropriate enquiries/obtain more information. If continuing is reasonably believed to tip off, discontinue that process, document the basis and report."),
     ("取得可信納解釋 → 可判斷沒有懷疑理由；仍考慮更新客戶風險狀況。", "Satisfactory explanation → May conclude no grounds for suspicion; still consider updating the risk profile."),
     ("未取得可信納解釋 → 可判斷有懷疑理由；識別懷疑便應提交可疑交易報告。", "No satisfactory explanation → May conclude grounds for suspicion; identified suspicion calls for an STR."),
     ("兩條路均須留痕 → 記錄發現、結果及決定理由，供關長、主管當局及核數師查閱。", "Document either route → Record findings, outcome and reasons for the Commissioner, authorities and auditors.")], R("03", "¶5.10–5.14")),
 table(["監察項目", "要求／數字", "容易混淆"], ["Monitoring item", "Requirement / number", "Easy to confuse"], [
     row(["資料覆核", "按政策定期及／或觸發覆核；高風險客戶最低每年一次，有需要更頻密。不動關係重新活躍時應覆核。", "更新資料不是每次重新核實已核實身分，除非原資料真實性／充分性有疑。"],
         ["CDD review", "Review periodically and/or on triggers under policy. Review high-risk customers at least annually and more often if needed; review dormant relationships on reactivation.", "Updating data does not mean reverifying an already verified identity unless its authenticity/adequacy is doubtful."], R("03", "¶5.1–5.3, fn52–53")),
     row(["何種交易須審查背景及目的？", "交易不符合對客戶、其業務、風險狀況或資金來源的認知時，應查詢是否有懷疑理由。另須識別同時符合兩組條件的交易：（一）複雜、款額大得異乎尋常或模式異常；及（二）沒有明顯經濟或合法目的，並書面列明審查所得。", "第二項的兩組條件須同時具備；不能把法定清單拆成兩個互不相關的類別。但其他情況引起的懷疑仍須處理。"],
         ["Which transactions require background/purpose examination?", "Investigate grounds for suspicion where activity conflicts with knowledge of the customer, business, risk profile or funds source. Also identify transactions that meet both groups: (i) complex, unusually large or unusually patterned; and (ii) without apparent economic/lawful purpose, and document the findings.", "The second rule requires both groups together, not two unrelated categories. Suspicion arising elsewhere still requires action."], R("03", "¶5.1(b)(ii); ¶5.10; ¶5.14"), R("04", "Sch.2 s.5(1)(b)–(c)")),
     row(["監察範圍", "盡可能以關係為本，涵蓋同一或跨業務的多個及相關戶口。所有業務關係均按風險監察；低風險只可下調程度。", "逐個帳戶看似正常，合併後仍可能異常。"],
         ["Monitoring scope", "Use a relationship-based approach as far as possible, across multiple/related accounts and business lines. Monitor every business relationship on a risk basis; low risk permits reduced intensity.", "Individually normal accounts may reveal unusual aggregate activity."], R("03", "¶5.6; ¶5.9")),
     row(["系統設計與參數", "考慮規模複雜程度、業務風險、管控、既有程序及產品／渠道。參數須顧及交易性質、連串交易、對手、付款／收款地點、正常活動／營業額；定期覆核、記錄及獨立驗證。", "固定金額警報不是全部要求；職員亦須適時取得充分資料。"],
         ["System design and parameters", "Consider scale/complexity, business risk, controls, existing procedures and products/channels. Parameters address transaction type, series, counterparties, payment/receipt location and normal activity/turnover; review, document and independently validate them.", "Fixed amount alerts are not the entire requirement; staff also need timely, sufficient information."], R("03", "¶5.4–5.8"))]),
 example("說明例：客戶解釋某筆異常付款，經營者認為解釋可信納，但得知其業務已持續擴大。這次可以沒有懷疑理由，仍應考慮更新風險狀況，並記錄判斷理由。",
         "Illustration: an unusual payment receives a satisfactory explanation, but enquiries reveal lasting business expansion. There may be no grounds for suspicion in that case; still consider a risk-profile update and document the decision.", R("03", "¶5.11; ¶5.14"))),

section("screening", "制裁篩查：何時篩、篩誰、如何處理吻合", "Sanctions screening: when, whom and how to resolve matches",
        "制裁篩查不因客戶低風險而省略。名單更新、已有客戶及轉帳相關各方，都要放進程序。",
        "Low customer risk does not remove sanctions screening. The process must address list updates, existing customers and transfer parties.",
        "m6-355 m6-374 m6-375 m6-399 m6-488",
 table(["情況", "行動", "容易混淆"], ["Situation", "Action", "Easy to confuse"], [
     row(["備存及更新數據庫", "綜合已知名單，收錄憲報／商務及經濟發展局網站及關長通知的名單，及時更新並方便職員查閱。用第三方數據庫亦應抽樣測試完整及準確程度。", "聯合國新名單尚未經香港立法實施，仍應在切實可行範圍內盡快收錄；也可能構成相關法律的知悉或懷疑理由。"],
         ["Database maintenance", "Consolidate known lists, including Gazette/CEDB and Commissioner-notified lists; update promptly and make accessible. Test completeness and accuracy of third-party databases.", "Add new UN designations as soon as practicable even before local implementation; they can also give grounds for relevant knowledge/suspicion."], R("03", "¶6.12–6.15")),
     row(["建立關係／名單有變", "建立時對客戶及任何實益擁有人篩查；新增／更新指認後盡快重新篩查。以風險為本擴及有關連者及代表。", "低風險不豁免；政治人物的風險分類不是制裁篩查豁免。"],
         ["Onboarding / list change", "Screen customers and all BOs at establishment, then as soon as practicable against new/updated designations. Extend to connected parties and representatives on a risk basis.", "No low-risk exemption. PEP classification does not create a sanctions-screening exemption."], R("03", "¶6.16–6.17, fn58")),
     row(["跨境電傳轉帳及匯款前", "根據當時名單篩查相關各方。常見問題列明最低包括：匯款人、收款人、匯款機構、中介機構、收款機構及撥付訊息中被具名的人士。", "不限於經營者自己的客戶；亦不限於8,000元以上。"],
         ["Before cross-border wire transfers / remittances", "Screen relevant parties against the current database. FAQ24 specifies at least: originator, recipient, ordering institution, intermediary institution, beneficiary institution and parties named in cover-payment messages.", "Not limited to the MSO's own customers, nor only amounts above HK$8,000."], R("03", "¶6.16(c)"), R("06", "AML/CFT Q24")),
     row(["姓名可能吻合", "作更嚴格查核以確定是否真吻合；記錄查核結果及篩查紀錄。如懷疑有恐怖分子／擴散資金籌集或制裁違規，向財富情報組報告。", "可能吻合不等於已確認；但也不能未查核便消除警報。用外地辦事處篩查，最終責任仍在經營者。"],
         ["Potential name match", "Conduct enhanced checks to determine a true match, document results and screening records, and report suspected TF/PF/sanctions breaches to the JFIU.", "A potential match is not confirmation, but do not dismiss it without checking. Overseas-office screening leaves ultimate responsibility with the MSO."], R("03", "¶6.18–6.19"))]),
 flow("可能吻合的處理", "Resolving a potential match", [
     ("可能吻合 → 作更嚴格查核，確定是否真正吻合。", "Potential match → Enhanced checks to determine whether it is a true match."),
     ("如懷疑違規 → 向財富情報組報告；查核及篩查紀錄均保存。", "Suspected breach → Report to the JFIU; retain screening and checking records.")], R("03", "¶6.18"))),

section("third-party", "第三方支付：接納前逐項過關", "Third-party payments: work through acceptance conditions",
        "這份通函的第三方是客戶以外的任何人。較低風險第三方不等於自動接納，也不會取消必要的核查及批准。",
        "For this circular, a third party is anyone other than the customer. Lower-risk status is not automatic acceptance and does not remove checks and approval.",
        "m6-356 m6-381 m6-382 m6-383 m6-384 m6-398 m6-460 m6-496",
 flow("第三方付款的接納路線", "Third-party payment acceptance route", [
     ("管控不足以應付本身高風險？ → 不應接受任何第三方支付。", "Controls cannot manage the inherent high risk? → Do not accept any third-party payments."),
     ("管控足夠？ → 仍只在特殊、合法且合理符合客戶狀況及一般商業作業的情況接納。", "Adequate controls? → Acceptance remains limited to exceptional, legitimate circumstances reasonably consistent with the customer profile and normal commercial practice."),
     ("接納前 → 評估原因及需要；按風險合理核實第三方身分及關係；取得擔任相關職位的高級管理層批准，記錄證據和批准。", "Before acceptance → Evaluate reasons/need; reasonably verify identity and relationship on a risk basis; obtain approval from senior management with an AML/CFT role; document evidence and approval."),
     ("接納後 → 加強監察，及時查詢可疑訊號；有懷疑理由向財富情報組提交報告。", "After acceptance → Intensify monitoring and promptly investigate red flags; report grounds for suspicion to the JFIU.")], R("08", "Key control standards 3–4, 6, 9, 11; fn3")),
 table(["情況", "措施／分別", "容易混淆"], ["Situation", "Measures / distinction", "Easy to confuse"], [
     row(["較低／較高風險第三方", "一般較低風險例子：直系親屬、客戶實益擁有人或聯繫公司、受規管金融機構。其他第三方較高風險，應更嚴格審查並確立客戶／實益擁有人資金來源。", "較低風險不是沒有風險，也不是免批准。"],
         ["Lower / higher-risk third party", "Generally lower-risk examples: immediate family, the customer's BO or affiliate, regulated financial institution. Other third parties carry higher risk; enhance scrutiny and establish the customer/BO's source of funds.", "Lower risk is not no risk or exemption from approval."], R("08", "Key control standard 7, fn6–7")),
     row(["須格外留神的三種情況", "關係難核實；付款前不能提供第三方身分詳情供核實；或同一第三方向多名看似無關客戶付款／收款。可用未使用的額外身分證據進一步核實。", "不能只因第三方稱是親屬，便忽略出現的具體警號。"],
         ["Three extra-caution cases", "Hard-to-verify relationship; no identity details available for verification before payment; one third party paying/receiving for several apparently unrelated customers. Further verify with additional unused evidence, for example.", "A claimed family relationship does not neutralise actual warning signs."], R("08", "Key control standard 8, fn8")),
     row(["可疑交易訊號", "例如：無商業理由的頻繁／大額第三方資助、無關客戶同樣交易模式、多人授權同一不受規管第三方、拆單、大額跨境現金，或不能即時提供額外證件。", "訊號是進一步查詢及判斷的依據，不能直接當作已證明犯罪；亦留意付款人才是真正實益擁有人。"],
         ["Red flags", "Examples: frequent/large third-party-funded transfers without business reasons, identical patterns among unrelated customers, one unregulated representative, structuring, large cross-border cash or inability to promptly supply additional identification.", "Indicators support enquiries and assessment, not automatic proof of crime. Consider whether the payer is the true BO."], R("08", "Red flags, pp.2–3; key control standard 9")),
     row(["制度、培訓及客戶溝通", "政策詳細並經高級管理層批准及有效傳達，配合嚴格合規監察、專責人員、清晰職員指引、完整評估紀錄，並告知客戶政策及所需文件。通函強烈鼓勵指定客戶本人銀行帳戶付款。", "『強烈鼓勵』不能寫成一律法定必須；被拒絕付款也不會自動免去有懷疑時的舉報。"],
         ["Systems, training and communication", "Detailed senior-approved policies communicated effectively, strict compliance monitoring, assigned personnel, clear staff guidance, full assessment records and customer communication of policy/document requirements. The circular strongly encourages payments through designated own-name bank accounts.", "Strong encouragement is not a universal statutory must. Refusal does not remove reporting where suspicion exists."], R("08", "Key control standards 1–5, 10–12; standard 9"))])),

section("transfers", "電傳轉帳與匯款：按角色及金額判斷", "Wire transfers and remittances: assess role and amount",
        "先分清交易是否電傳轉帳，再看你是匯款、中介還是收款機構；核實身分、附隨資料和備存紀錄各有規定。",
        "First determine whether the transaction is a wire transfer, then your ordering, intermediary or beneficiary role. Verification, accompanying information and retention are separate requirements.",
        "m6-376 m6-377 m6-378 m6-379 m6-400 m6-443 m6-489 m6-490 m6-491 m6-492",
 flow("交易與機構角色", "Transaction and institutional roles", [
     ("以電子方式由匯款機構，經中介機構（如有），向收款機構提供款項 → 檢查第10章電傳轉帳規定。", "Electronic transfer from ordering institution through intermediaries, if any, to beneficiary institution → Check Chapter 10 wire-transfer rules."),
     ("送往／安排送往香港以外的非電傳匯款 → 檢查第11章特別規定。", "Non-wire remittance sending/arranging funds outside Hong Kong → Check the special Chapter 11 rules."),
     ("同一交易仍須按適用情況檢查盡職審查、制裁篩查、監察及舉報。", "For either route also check applicable CDD, screening, monitoring and reporting.")], R("03", "¶10.1–10.4; ¶11.1–11.6; ¶4.2.1; ¶6.16; ¶7.5")),
 table(["情況／數字", "資料及核實", "容易混淆"], ["Situation / number", "Information and verification", "Easy to confuse"], [
     row(["電傳轉帳達8,000元", "附匯款人姓名、戶口／獨特參考編號，及地址／客戶識別號碼／識別文件號碼／出生日期和地點其中一類；另附收款人姓名及戶口／獨特參考編號。所需匯款人資料須準確，非經常交易須核實匯款人。", "客戶識別號碼與交易參考編號不同；沒有帳戶須用可追蹤的獨特參考編號，不能留空。"],
         ["Wire transfer of HK$8,000 or more", "Include originator name, account/unique reference, and one of address/customer ID/document number/date and place of birth; plus recipient name and account/unique reference. Required originator data must be accurate; verify the originator for an occasional transfer.", "Customer ID and transaction reference differ. No account means a traceable unique reference, not a blank field."], R("03", "¶10.5; ¶10.7–10.9, fn70")),
     row(["電傳轉帳低於8,000元", "仍附雙方姓名及戶口／獨特參考編號。非經常交易一般無須核實匯款人，但有關連轉帳合計達門檻或懷疑洗錢／恐怖分子資金籌集則例外。", "『一般不核實』不是『毋須任何資料』。制裁篩查另行適用。"],
         ["Wire transfer below HK$8,000", "Still include both names and accounts/unique references. For an occasional transfer, originator verification is normally unnecessary unless linked transfers reach the threshold or ML/TF is suspected.", "Normally no verification does not mean no information. Screening is a separate obligation."], R("03", "¶10.6–10.9; ¶6.16(c)")),
     row(["本地轉帳／批量轉帳", "本地可按第10.11段僅附匯款人戶口／可追蹤參考編號；應指示接收機構或關長要求，3個營業日內提供完整匯款人資料，執法機構要求則立即提供。同一匯款人海外批量轉帳，群組檔案仍須有完整所需資料。", "3個營業日不是所有索取資料的統一期限；本地精簡亦不是全面資料豁免。"],
         ["Domestic / batch transfer", "Domestic transfers may use the ¶10.11 originator-account/traceable-reference route. Supply full originator data within three business days of the receiving institution's or Commissioner's request, and immediately to law enforcement. Overseas batches from one originator still need required complete data in the batch file.", "Three business days is not universal for all requests; domestic simplification is not a blanket data waiver."], R("03", "¶10.10–10.12, fn71")),
     row(["中介機構", "保留並向下游傳遞所有附隨資料。技術限制使跨境／本地相關轉帳不能保留時，將接收的所有資料至少存檔5年。識別及風險處理欠資料轉帳；缺資料盡快索取，不完整／無意義資料則盡快減低風險。", "不是因技術限制便可以刪除；執行、拒絕或暫停須按風險政策判斷。"],
         ["Intermediary institution", "Retain and pass all accompanying data. Where technical limits prevent retention in a linked domestic/cross-border transfer, keep all received data for at least five years. Detect and risk-manage missing data; seek missing data promptly and mitigate incomplete/meaningless data.", "Technical limits do not permit deletion. Execute/reject/suspend decisions follow risk policies."], R("03", "¶10.14–10.18")),
     row(["收款機構", "識別及處理欠資料的本地／跨境轉帳，風險決定執行、拒絕、暫停及跟進。依指引盡快索取缺資料；無法取得時考慮限制／終止機構關係或減低風險。達8,000元且未曾核實收款人時應核實。", "已核實收款人，不等於可忽略無意義匯款人資料。法例對本地欠資料與指引的較廣要求應分清。"],
         ["Beneficiary institution", "Detect/handle missing-data domestic/cross-border transfers; use risk policies for execution, rejection, suspension and follow-up. Under the Guideline, seek missing data promptly; consider restricting/ending institutional ties or mitigation if unavailable. Verify an unverified recipient for HK$8,000 or more.", "Prior recipient verification does not excuse meaningless originator data. Distinguish the statutory domestic missing-data rule from the wider Guideline requirement."], R("03", "¶10.19–10.22"), R("04", "Sch.2 s.12(9)–(10)")),
     row(["不是電傳轉帳的匯款達8,000元", "交易前識別並按識別文件核實匯款人；記錄姓名、證件號碼及旅遊證件發出地、地址、貨幣款額、指示日期時間、收款人姓名地址、送遞方式。匯款人是付款來源戶口持有人；無戶口則為發出指示者。", "匯款與電傳轉帳不可混為一談；實際付款第三方亦可能觸發另一套風險查詢。"],
         ["Non-wire remittance of HK$8,000 or more", "Before acting, identify/verify the originator against ID and record name, ID number and travel-document issue place, address, currency/amount, instruction date/time, recipient name/address and delivery method. Originator is the source-account holder, or instructing person without an account.", "Remittance and wire transfer are distinct; a third-party payer may also trigger separate risk enquiries."], R("03", "¶11.2–11.6")),
     row(["咭交易及其他不適用情況", "第10.4段包括經營者與指明金融／外地機構各自為自身行事的轉帳，以及符合條件的咭交易。咭交易例子有提款、信用咭現金透支及購貨／服務；咭不得用作人對人支付系統，且咭號／獨特標識須附隨。", "不是只限購貨；附有咭號也只是其中一項條件。咭用作人對人轉帳不屬該例外。"],
         ["Card transactions and exclusions", "¶10.4 covers transfers between an MSO and specified financial/foreign institutions where each acts on its own behalf, and qualifying card transactions, such as ATM withdrawals, credit-card cash advances and purchases. The card must not be used as a person-to-person payment system and its number/unique identifier must accompany the transfer.", "Not limited to purchases. A card number is only one condition; person-to-person card transfers are outside the exception."], R("03", "¶10.4"))])),

section("trade", "交付渠道及貿易洗錢風險", "Delivery channels and trade-based laundering risks",
        "評估的不只是客戶，也包括合作方、境外渠道及交易是否符合真實業務。貿易風險指標提示查核，並非單憑一項即證明犯罪。",
        "Assess counterparties, overseas channels and the commercial reality as well as customers. A trade-risk indicator prompts examination; one indicator alone is not proof of crime.",
        "m6-380 m6-449 m6-471 m6-472 m6-473 m6-474 m6-475 m6-476 m6-477",
 table(["情況", "應掌握的措施／訊號", "容易混淆"], ["Situation", "Measures / indicators", "Easy to confuse"], [
     row(["境外交付渠道", "合作前先做全面風險評估，建立或維持與客戶、夥伴／交易對手的關係時審慎評估，定期覆核渠道以符合相關司法管轄區最新規定。高風險採更嚴格審查，知悉或懷疑時舉報。", "不能只在開業時評估一次；凍結資金或境外違法風險亦須按香港適用法律及具體事實處理。"],
         ["Overseas delivery channel", "Perform comprehensive risk assessment before collaboration; carefully assess customer/partner/counterparty ties on establishment/continuation. Periodically review channels against the jurisdiction's latest requirements; enhance high-risk CDD and report knowledge/suspicion.", "Not a one-time start-up check. Frozen funds and overseas conduct require assessment under applicable Hong Kong law and the facts."], R("14", "¶1–6, note4")),
     row(["新成立／空殼風險", "通函提示留意缺乏資產、職員或活躍業務的法律實體；主動考慮反欺詐程序核查資料及交易真實性，並評估匯款人／收款人是否空殼公司。", "新成立本身不是自動禁止交易；也不代表文件可以免查。"],
         ["New entity / shell risk", "The circular highlights legal entities lacking assets, staff or active business. Proactively consider anti-fraud checks on information and transaction authenticity, and assess whether originator/recipient is a shell.", "New incorporation alone is not automatic prohibition, or an excuse to omit checks."], R("18", "Area 2")),
     row(["多個風險指標／警報", "出現多項指標應標記及上報高級管理層。警報須查背景、目的、客戶狀況、資金／財富來源及歷史，不得沒有充分理由和分析便消除。", "高級管理層處理風險，不取代洗錢報告主任及法定舉報程序。"],
         ["Multiple indicators / alerts", "Flag multiple indicators and escalate to senior management. Examine background, purpose, profile, sources of funds/wealth and history; do not dismiss alerts without adequate reasons and analysis.", "Senior risk escalation does not replace the MLRO or statutory reporting process."], R("18", "Areas 1, 3–4")),
     row(["結構、地址及網上資料（學習譯文）", "英文來源列出不合理複雜架構、可能大量註冊地址且缺單位、業務與地址不符而無合理解釋、欠網上資料或網站與聲稱業務不符、代名人管理層、職員少而貿易量大、無法解釋不動期等訊號。", "這是非詳盡訊號清單，不是每項必然違法。中文為學習譯文；決定性原文是英文。"],
         ["Structure, address and online presence", "The English source lists illogical complexity, possible mass-registration addresses lacking units, unexplained address/business mismatch, missing or inconsistent online presence, nominee management, few staff versus trade volume and unexplained dormancy, among other indicators.", "The list is non-exhaustive and each indicator is not necessarily unlawful. The Chinese text is a study translation; the deciding source is English."], R("24", "printed pp.2–3")),
     row(["貿易活動（學習譯文）", "留意貿易與業務不符、無關行業多重中介、異常路線、無理由長期／多次延長信用證、不合理低毛利、購貨超出經濟能力、新／重啟公司突然大額高量業務。", "應整體考慮客戶及背景；部分訊號需額外外部資料。中文為學習譯文。"],
         ["Trade activity", "Consider business-inconsistent trade, incongruent third-party intermediaries, unusual routes, unjustifiably long/extended letters of credit, unreasonably low margins, purchases beyond economic capacity and sudden high-volume/value activity by new/reactivated entities.", "Consider the full customer context; some indicators require external data. The Chinese text is a study translation."], R("24", "printed pp.2, 4"))])),

section("reporting", "有懷疑後：內部報告、舉報及避免通風報訊", "After suspicion: internal reports, disclosure and tipping-off",
        "本節補足管控流程的最後一環；管治職責及制度效能在全套資料的其他 Part 再作主題整理。這裏先掌握遇到懷疑時怎樣處理。",
        "This completes the control process. The full pack will address governance roles and system effectiveness in their main Parts; here, focus on responding to suspicion.",
        "",
 flow("由職員發現至洗錢報告主任決定", "From staff detection to the MLRO's decision", [
     ("職員發現懷疑 → 按程序報告洗錢報告主任，無故延誤不可接受；非洗錢報告／合規職能主管不可過濾。", "Staff identify suspicion → Report to the MLRO under procedures without unwarranted delay; managers outside reporting/compliance functions must not filter reports."),
     ("洗錢報告主任 → 確認收悉、提醒不可通風報訊，考慮所有相關資料，記錄覆核及結論。", "MLRO → Acknowledge, remind staff about tipping-off, consider all relevant information and record review/conclusions."),
     ("有知悉或懷疑理由 → 評估後在合理範圍內盡快向財富情報組披露及提供依據；不舉報亦須妥善記錄慎重考慮及行動。", "Grounds for knowledge/suspicion → Disclose to the JFIU as soon as reasonably practicable after assessment with the basis; a no-report decision also needs a proper record of deliberations/actions.")], R("03", "¶7.12–7.20")),
 table(["情況", "判斷", "容易混淆"], ["Situation", "Decision", "Easy to confuse"], [
     row(["未完成／未進行交易", "知悉或懷疑確立後，試圖進行或未成事交易亦可有舉報責任；不論金額，毋須先掌握確鑿犯罪證據。", "『沒有成交』或『金額很小』都不是自動不舉報理由。"],
         ["Attempted / uncompleted transaction", "Knowledge/suspicion can trigger reporting for attempted or uncompleted transactions, regardless of amount; conclusive proof of crime is not required.", "No completed transaction or a small amount is not an automatic reason not to report."], R("03", "¶7.1–7.5, fn60"), R("18", "Area 4")),
     row(["查詢與通風報訊", "真誠適當查詢本身不構成通風報訊。合理相信繼續盡職審查會通風報訊，可停止該程序，記錄評估基礎並舉報。通風報訊也涵蓋已內部提出懷疑而未對外舉報的情況。", "『尚未向財富情報組報告』不是安全透露內部懷疑的理由。"],
         ["Enquiry versus tipping-off", "Good-faith appropriate enquiry is not itself tipping-off. If further CDD is reasonably believed to tip off, discontinue that process, document the basis and report. Tipping-off also covers suspicion raised internally before external reporting.", "Not yet reported to the JFIU is not a safe basis for revealing internal suspicion."], R("03", "¶5.13; ¶7.6")),
     row(["其他轉帳情況", "控制匯款與收款雙方時，應在受可疑轉帳影響的司法管轄區提交可疑交易報告，並向財富情報組提供交易資料。急需移動資金、結戶等緊急情況，於報告列明，特殊緊急情況考慮先電話通知。", "查關連資料與及時舉報須平衡；不能為等待所有資料而無限延後。"],
         ["Other transfer situations", "When controlling both sides, file STRs in jurisdictions affected by a suspicious wire and provide transaction information to the JFIU. Mark urgency such as imminent fund movement/closure; exceptionally consider initial telephone contact.", "Balance linked-account enquiries against timely reporting; do not postpone indefinitely to collect everything."], R("03", "¶7.18–7.21"))]),
 note("已按經營者政策及程序向洗錢報告主任報告懷疑的職員，已履行相關法定報告要求。是否對外報告的覆核仍須按上述程序處理。",
      "Staff who report suspicion to the MLRO under the MSO's policies and procedures have discharged the relevant statutory reporting obligation; external-report assessment still follows the process above.", R("03", "¶7.14")))
]
