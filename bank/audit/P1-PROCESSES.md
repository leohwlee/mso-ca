# P1流程、条件及例外补题

本轮落实剩余16项P1任务，新增18道组合题、79个题句；当时题库由320题增至338题、1,678个题句。后续更新另见[最终完成记录](REMAINING.md)。

任务来自[总体覆盖清单](README.md)。先核对320题的直接题句，沿用已覆盖部分，只对剩余内容补题。原297题及299题审核基线均保留，不能把不同来源的映射行数当成独立考点或考试覆盖率。

[逐句快照、双语盲答与实施证据](p1-implementation.json) · [专项名词及职责审核](TERMS-AND-ROLES.md)

## 逐项落实

| 任务 | 内容 | 状态 |
|---|---|---|
| B02 P1 | 代表客户行事者的最低识别资料 | 已完成 |
| B03 P1 | 实益拥有人：最终控制、代他人行事及代名安排 | 已完成 |
| B04 P1 | 身份延后核实时的付款例外和失败处理 | 已完成 |
| B05 P1 | 政治人物风险变化、前政治人物及批准权限 | 已完成 |
| B06 P1 | 依赖中介人的边界、资格及可靠性 | 已完成 |
| B07 P1 | 简化尽调的停止条件及客户和账户例外 | 已完成 |
| B08 P1 | 加强尽调仍不足时的剩余风险控制 | 已完成 |
| B09 P1 | 身份证明：所在地、未成年人及可用证件 | 已完成 |
| B10 P1 | 客户与第三方界定、大额非授权现金付款人 | 已完成 |
| B12 P1 | 电汇卡交易例外及缺失资料的追讨 | 已完成 |
| B13 P1 | 金钱服务发牌豁免的业务附属条件 | 已完成 |
| B14 P1 | 遗漏申请资料何时构成罪行 | 已完成 |
| B16 P1 | 经营账户允许的户名 | 已完成 |
| B17 P1 | 纪律罚款上限与实际计罚方法 | 已完成 |
| B18 P1 | 自然人改名后核实及开户前改名例外 | 已完成 |
| B19 P1 | 国际经营中的其他适用制裁 | 已完成 |

## B02 · 代表客户行事者的最低识别资料

- C008、G031、L049：法人代表的主要營業地點；與註冊辦事處不同時須收集。新增`m6-412#5`。
- C008、G031、L049：法人代表的全名。新增`m6-412#3`。
- C008、G031、L049：法人代表的獨特識別號碼及文件類別。新增`m6-412#5`。
- C008、G031、L049：法人代表註冊、成立或登記的地點，包含註冊辦事處地址。新增`m6-412#4`。
- C008、G031、L049：法人代表註冊、成立或登記的日期。新增`m6-412#3`。
- C008、G031、L049：自然人代表的全名。新增`m6-412#1`。
- C008、G031、L049：自然人代表的出生日期。新增`m6-412#1`。
- C008、G031、L049：自然人代表的國籍。新增`m6-412#2`。
- C008、G031、L049：自然人代表的獨特識別號碼及文件類別。新增`m6-412#2`。
- G031：按相應自然人或法人客戶的識別及核實規則處理。新增`m6-412#1,3`。
- L049：低風險經確認名單可替代身分核實方式，但仍須收集最低識別資料。新增`m6-412#6`。

## B03 · 实益拥有人：最终控制、代他人行事及代名安排

- G027、S032：其他類別客戶代另一人行事時，另一人屬實益擁有人。沿用现题`m3-306#5`。
- G027、S032：合夥代另一人行事時，另一人屬實益擁有人。沿用现题`m3-306#3`。
- G027、S032：法團代另一人行事時，另一人屬實益擁有人且可為法人。沿用现题`m3-306#2`。
- G027：除法團、合夥及信託外的客戶，最終擁有或控制者須是個人。沿用现题`m3-306#4`。
- G028：有不是代表自己行事的跡象時，應適當查詢。新增`m6-413#2`。
- G028：自然人客戶通常是實益擁有人，沒有相反跡象時不用主動搜尋。新增`m6-413#1`。
- G030：取得代名安排詳情以確定實益擁有人。新增`m6-413#5`。
- G030：取得信納的代名人及其代表人士身分證據。新增`m6-413#4`。
- L047：控制未實際行使亦可推定，使用、享用或受益於法人資產是例子。沿用现题`m6-397#6`。
- L047：未能支付某些款項可構成控制。沿用现题`m6-397#5`。
- L047：歷史或合約關係可構成沒有持股的控制。沿用现题`m6-397#4`。
- L047：融資可構成沒有持股的控制。沿用现题`m6-397#2`。
- L047：親密家族關係可構成控制。沿用现题`m6-397#3`。
- L047：透過與超過25%持股或投票權擁有人的個人關係控制。沿用现题`m6-397#1`。
- S032：合夥管理的最終控制權為獨立判斷，無須超過25%資本或利潤份額。新增`m6-413#3`。
- S032：法團管理的最終控制權不以持股門檻為前提。沿用现题`m6-397#2,4`。

## B04 · 身份延后核实时的付款例外和失败处理

- G033：付款例外須沒有洗錢／恐怖分子資金籌集懷疑。新增`m6-414#1`。
- G033：付款例外須經高級管理層批准。沿用现题`m6-363#4`。
- G033：付款例外須評定風險屬低度。沿用现题`m6-363#4`。
- G033：批准前考慮客戶業務性質，而非以獲利能力取代。新增`m6-414#2`。
- G033：收款人姓名／名稱不得與恐怖嫌疑人物及政治人物等監察名單吻合。新增`m6-414#3`。
- G033：未完成核實時原則不得向第三者付款，付款須屬符合條件的例外。新增`m6-414#1,2,3`；沿用现题`m6-363#4`。
- G033：核實未能按合理時限完成而終止關係時，避免進一步交易；可行情況下原狀退回資金或其他資產除外。新增`m6-414#4`。

## B05 · 政治人物风险变化、前政治人物及批准权限

- G040：繼續已有香港／國際組織政治人物關係，其後變高風險時適用全部三項措施。新增`m6-415#1`。
- G040：繼續已有高風險關係，其後才知悉客戶或實益擁有人屬香港／國際組織政治人物時適用全部三項措施。新增`m6-415#2`。
- G041、L057：三類前政治人物停止措施均須高級管理層批准。新增`m6-415#3`；沿用现题`m6-388#1`。
- G041、L057：三類前政治人物均須適當評估與政治人物地位相關的風險。新增`m6-415#3`。
- G041：仍能運用的非正式影響力。新增`m6-416#1`。
- G041：保留前政治人物相關風險評估紀錄作合規證明。新增`m6-415#4`。
- G041、L057：停止措施時前政治人物須不再高風險。新增`m6-415#3`；沿用现题`m6-388#2`。
- G041：前後職能聯繫；委任繼任人及繼續處理相同事務例子。新增`m6-416#3`。
- G041：本人任政治人物時的職位等級，不是繼任者的等級。新增`m6-416#2`。
- L058：批准人選數目及職銜依經營者規模、類型、機構層面風險評估而異。新增`m6-416#4`。
- L058：批准人選須有足夠資歷。沿用现题`m6-388#4`。
- L058：由經營者自行決定，明文清晰政策列明批准建立及維持關係的人選。沿用现题`m6-388#3`。

## B06 · 依赖中介人的边界、资格及可靠性

- G043：An intention to terminate reliance triggers immediate retrieval of all CDD information, rather than waiting for a customer review.。新增`m6-426#2`。
- G043：Doubts about intermediary reliability require reasonable steps to review its CDD ability.。新增`m6-426#1`。
- G043：Reliance on an intermediary does not extend to ongoing CDD and transaction monitoring.。沿用现题`m6-386#1`。
- G044：Group policy should adequately mitigate higher country risk of the related foreign FI's jurisdiction; elimination is not the rule.。新增`m6-426#4`。
- G044：The MSO must be satisfied about regular independent group review of ongoing policy compliance.。沿用现题`m6-386#4`。
- G044：The domestic professional intermediary must itself be subject to Schedule 2 for the customer; adequate procedures alone do not state the whole Guideline condition.。新增`m6-426#3`。
- L059：Ongoing CDD and transaction monitoring cannot be delegated by intermediary reliance, despite assistance collecting updates.。沿用现题`m6-386#1`。
- S049：A qualifying branch of that non-redomiciled MSO's head office also qualifies.。沿用现题`m6-386#3`。
- S049：A re-domiciled MSO uses the own-branch route, with the required outside-Hong-Kong similar business.。新增`m6-426#5`。
- S049：An MSO incorporated outside Hong Kong and not re-domiciled may have a qualifying head office.。沿用现题`m6-386#2`。

## B07 · 简化尽调的停止条件及客户和账户例外

- G034：Identification-information veracity or adequacy doubts prevent starting SDD despite a low risk rating.。新增`m6-429#1`。
- G034：The same doubts prevent continuing SDD despite a low risk rating.。新增`m6-429#1`。
- G035：A separate employee relationship requires its own CDD despite the scheme's qualifying treatment.。新增`m6-427#2`。
- G035：Before the listed-customer BO concession, assess whether disclosure requirements ensure adequate BO transparency.。新增`m6-427#1`。
- G035：The life-policy product route also includes a single premium no greater than HK$20,000 or equivalent.。新增`m6-427#3`。
- G036：A qualifying responsible institution does not replace the MSO's satisfaction with reliable systems and controls for CDD on all underlying investors.。新增`m6-428#1`。
- G036：Both account routes require customer FI authority to operate, evidenced by contract or agreement.。新增`m6-427#6`。
- G036：Investment-vehicle service-provider account: customer FI has conducted AMLO CDD on the vehicle, not its manager as substitute.。新增`m6-427#5`。
- G036：Nominee-company account: customer FI has conducted CDD on its underlying customers.。新增`m6-427#4`。
- G037：Clients' money or securities must be mingled.。新增`m6-428#2`。
- G037：Separate client sub-accounts without co-mingling require the underlying clients' identities as well as the solicitor's.。新增`m6-428#4`。
- G037：The solicitor or firm manages as the clients' agent.。新增`m6-428#3`。
- S039：Clients' money or securities must be mingled; account name alone is insufficient.。新增`m6-428#2`。
- S039：The solicitor customer manages as the clients' agent, not the MSO.。新增`m6-428#3`。

## B08 · 加强尽调仍不足时的剩余风险控制

- G038：Account-function restrictions are another possible example, not a requirement to apply both examples together.。新增`m6-429#4`。
- G038：EDD that cannot fully mitigate identified risk requires other measures for the residual risk.。新增`m6-429#2`。
- G038：Transaction limits are an example of a possible additional residual-risk measure, not a universally compulsory component.。新增`m6-429#3`。

## B09 · 身份证明：所在地、未成年人及可用证件

- G072：A Hong Kong-born minor without a valid travel document or HKID uses the Hong Kong birth-certificate route.。新增`m6-430#3`。
- G072：A non-resident physically present in Hong Kong is verified by a valid travel document under Appendix A.。新增`m6-430#1`。
- G072：For a non-resident not in Hong Kong, a current photographic national identity card is a listed choice.。新增`m6-430#2`。
- G072：For a non-resident not in Hong Kong, a valid photographic national driving licence from a competent national/state authority is a listed choice.。新增`m6-430#2`。
- G072：The Macau Permanent Resident Identity Card is a listed travel document, distinct from the already tested Macau resident permit.。新增`m6-430#4`。

## B10 · 客户与第三方界定、大额非授权现金付款人

- G019：汇出电汇收款人与汇款MSO无其他关系时，不是其客户；上轮 RC008 已补。。沿用现题`m6-396#4`。
- G021：存档副本是为了持续监察。。新增`m6-442#4`。
- G021：现金交易、姓名不在账户委托书、相等于或超过120,000的合并触发条件。。新增`m6-442#1`。
- G021：要求进行现金交易的人本人的身份证明文件，不能以账户客户文件代替。。新增`m6-442#2`。
- G021：须存档证件副本，记录证件号码不足。。新增`m6-442#3`。

## B12 · 电汇卡交易例外及缺失资料的追讨

- G067：卡不得用作执行人与人之间转账的支付系统；附随卡号不能替代该条件。。新增`m6-443#4`。
- G067：卡号或等同独特标识附随信息／付款表格的条件原已测试，不作为新增缺口。。沿用现题`m3-292#5`。
- G067：同一例外范围中未直接测试的原文例子：扣账卡ATM提款、信用卡现金垫支、预付卡支付货品服务；题干保留卡号条件，前三种所述用途本身属原文例子；第4句独立检验人对人条件。。新增`m6-443#1,2,3`。
- G070：原有条例题分别测试本地收款机构的号码范围、非本地中介／收款机构所有所需资料、尽快向发出指示机构取得及无法取得后的措施。依 B20 保留不同来源范围，不复制。。沿用现题`m3-294#2,4,5`。
- G070：指引涵盖本地电汇缺失的所需收款人资料，不能只追补账户号码；上轮 RG035 已补。。沿用现题`m6-400#2`。

## B13 · 金钱服务发牌豁免的业务附属条件

- S060：工具持牌人金钱服务附属其主要业务的条件已由上轮 RO016 补。。沿用现题`m4-365#6`。
- S060：持牌个人保险代理须附属于代理本身主要业务，不能替换为保险人主要业务。。新增`m2-357#2`。
- S060：持牌保险代理机构的附属业务条件。。新增`m2-357#3`。
- S060：持牌保险经纪公司的金钱服务须附属其本身主要业务。。新增`m2-357#1`。
- S060：指定零售支付系统交收机构的服务须附属于其作为交收机构的业务。。新增`m2-357#4`。
- S060：指定零售支付系统营运者的对应条件已有，未复制。。沿用现题`m2-340#3`。
- S060：稳定币持牌人的金钱服务须为其稳定币牌照下的业务活动。。新增`m2-357#5`。

## B14 · 遗漏申请资料何时构成罪行

- S061：主观状态的对象是要项被遗漏，不另要求知道虚假／误导结果。。新增`m2-358#4`。
- S061：对要项是否遗漏的罔顾可满足主观要件，并非必须实际知道。。新增`m2-358#2`。
- S061：结果虚假本身不足；须另有明知或罔顾遗漏的主观状态。。新增`m2-358#3`。
- S061：遗漏要项必须导致陈述虚假或误导；知道遗漏不能取代结果要件。。新增`m2-358#1`。

## B16 · 经营账户允许的户名

- L018：Permitted names: company, sole proprietor, partner, director and ultimate owner。新增`m4-373#1,2,3,4`。

边界：Question expressly tests the Licensing Guide 11.1(j) account-name list. Business Plan guideline item 8 does not define third party; this question does not purport to resolve that cross-document term or broaden the list.

## B17 · 纪律罚款上限与实际计罚方法

- L036：三倍利润／避免开支是其中一个法定最高额，实际罚款不自动与所得或节省挂钩。。新增`m4-366#1`。
- L036：同一计罚主题的未测试因素：尝试隐瞒、发现后补救及涉事人员／防止再犯措施、其他主管当局相当可能采取的行动。没有复用 m4-326 已测的财务困难、疏忽及轻微事项合计。。新增`m4-366#2,3,4`。

## B18 · 自然人改名后核实及开户前改名例外

- L041：以可靠及獨立來源核實新姓名。新增`m6-417#1`。
- L041：以現有紀錄核對新證件的出生日期、證號等，減低假冒風險。新增`m6-417#2`。
- L041：如有疑問可索取改名證明文件複本，例如結婚證書、改名契。新增`m6-417#3`。
- L041：開戶前已改名只須識別及核實現時姓名。新增`m6-417#4`。

## B19 · 国际经营中的其他适用制裁

- G051：可能影响业务即应考虑影响并采取适当措施，不等待实际影响发生。。新增`m1-178#2`。
- G051：同一金融制裁范围的相邻未测子项：由被指认者控制的实体，以及代表被指认者行事的人所拥有的实体。区别于 m1-130#3处理被指认者资金及#4向代表其行事者提供资金。。新增`m1-178#3,4`。
- G051：国际经营者须注意相关司法管辖区制裁制度的范围和重点。。新增`m1-178#1`。
- G051：香港法一般不强制关注境外单方面制裁已有；未复制。。沿用现题`m1-130#6`。

## 审核与限制

- 新题先由另一审核者遮住答案及解释，分别按英文及繁体原文判定；所有最终题句与审核快照一致，歧义及差异均已处理。
- 将新题与全库及同批题做语义去重，并与温习资料逐项对照；引文命中只是来源核验，不能代替条件、主体和例外的实质判断。
- 检查组合选项、逐句引文、双语术语和整库质量规则；原有320题内容及答案保持不变，旧作答记录无需迁移。
- 审核者使用同一会话模型；没有把未做的异模型对抗或跨语言嵌入检查写成已完成。未对全部旧题重做盲答。
- 本轮仍按归档23份官方资料及已定来源关系出题。沿用上一轮来源核验日期及条例官网访问限制，没有声称全部资料已重新确认最新版本。
- 本报告保留P1轮次的审核结论；其后P2／P3及部分扩写替换另见最终完成记录。本报告的“完成”针对列明的任务，不保证覆盖真实考试的全部内容。

维护：运行 `python -X utf8 bank/audit/p1_report.py --check`；题句、来源或覆盖判断改变时需重新审核，不能只更新摘要值。
