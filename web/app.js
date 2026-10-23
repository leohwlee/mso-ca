/* MSO Competence Assessment — offline mock exam. Vanilla JS, no dependencies. */
'use strict';

/* BEGIN GENERATED SOURCE INDEX */
const SOURCE_INDEX = {"documents":{"01":{"tc":{"filename":"01_高_能力評核須知（2022年12月）.pdf","path":"TC/01_高_能力評核須知（2022年12月）.pdf","studyTranslation":false},"en":{"filename":"01_High_Guidance Notes on the Competence Assessment (Dec 2022).pdf","path":"EN/01_High_Guidance Notes on the Competence Assessment (Dec 2022).pdf","studyTranslation":false}},"03":{"tc":{"filename":"03_高_打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）（2023年6月）.pdf","path":"TC/03_高_打擊洗錢及恐怖分子資金籌集指引（金錢服務經營者適用）（2023年6月）.pdf","studyTranslation":false},"en":{"filename":"03_High_Guideline on AML-CFT for Money Service Operators (Jun 2023).pdf","path":"EN/03_High_Guideline on AML-CFT for Money Service Operators (Jun 2023).pdf","studyTranslation":false}},"04":{"tc":{"filename":"04_高_打擊洗錢及恐怖分子資金籌集條例（第615章）（2026年9月24日綜合版）.pdf","path":"TC/04_高_打擊洗錢及恐怖分子資金籌集條例（第615章）（2026年9月24日綜合版）.pdf","studyTranslation":false},"en":{"filename":"04_High_AMLO Cap 615 - Consolidated (24 Sep 2026).pdf","path":"EN/04_High_AMLO Cap 615 - Consolidated (24 Sep 2026).pdf","studyTranslation":false}},"05":{"tc":{"filename":"05_高_牌照指引（2026年5月）.pdf","path":"TC/05_高_牌照指引（2026年5月）.pdf","studyTranslation":false},"en":{"filename":"05_High_Licensing Guide (May 2026).pdf","path":"EN/05_High_Licensing Guide (May 2026).pdf","studyTranslation":false}},"06":{"tc":{"filename":"06_高_適用於所有金錢服務經營者的常見問題（海關網站）.md","path":"TC/06_高_適用於所有金錢服務經營者的常見問題（海關網站）.md","studyTranslation":false},"en":{"filename":"06_High_FAQ applicable to all MSOs (C&ED portal).md","path":"EN/06_High_FAQ applicable to all MSOs (C&ED portal).md","studyTranslation":false}},"07":{"tc":{"filename":"07_高_通函_客戶盡職審查相關監管工作中的發現（2023年11月22日）.pdf","path":"TC/07_高_通函_客戶盡職審查相關監管工作中的發現（2023年11月22日）.pdf","studyTranslation":false},"en":{"filename":"07_High_Circular - Supervisory Findings on Customer Due Diligence (22 Nov 2023).pdf","path":"EN/07_High_Circular - Supervisory Findings on Customer Due Diligence (22 Nov 2023).pdf","studyTranslation":false}},"08":{"tc":{"filename":"08_高_通函_第三方支付涉及的洗錢及恐怖分子資金籌集風險（2024年9月17日）.pdf","path":"TC/08_高_通函_第三方支付涉及的洗錢及恐怖分子資金籌集風險（2024年9月17日）.pdf","studyTranslation":false},"en":{"filename":"08_High_Circular - ML-TF Risks of Third Party Payments (17 Sep 2024).pdf","path":"EN/08_High_Circular - ML-TF Risks of Third Party Payments (17 Sep 2024).pdf","studyTranslation":false}},"09":{"tc":{"filename":"09_高_通函_識別和緩解大殺傷力武器擴散融資風險（2021年12月22日）.pdf","path":"TC/09_高_通函_識別和緩解大殺傷力武器擴散融資風險（2021年12月22日）.pdf","studyTranslation":false},"en":{"filename":"09_High_Circular - Identification and Mitigation of Proliferation Financing Risks (22 Dec 2021).pdf","path":"EN/09_High_Circular - Identification and Mitigation of Proliferation Financing Risks (22 Dec 2021).pdf","studyTranslation":false}},"10":{"tc":{"filename":"10_中重點_有關適當人選準則的指引（2018年4月）.pdf","path":"TC/10_中重點_有關適當人選準則的指引（2018年4月）.pdf","studyTranslation":false},"en":{"filename":"10_Medium-Essential_Guideline on Criteria for Determining Fitness and Propriety (Apr 2018).pdf","path":"EN/10_Medium-Essential_Guideline on Criteria for Determining Fitness and Propriety (Apr 2018).pdf","studyTranslation":false}},"11":{"tc":{"filename":"11_中重點_有關適當人選準則的補充指引（2020年1月）.pdf","path":"TC/11_中重點_有關適當人選準則的補充指引（2020年1月）.pdf","studyTranslation":false},"en":{"filename":"11_Medium-Essential_Supplementary Guideline on Fitness and Propriety (Jan 2020).pdf","path":"EN/11_Medium-Essential_Supplementary Guideline on Fitness and Propriety (Jan 2020).pdf","studyTranslation":false}},"12":{"tc":{"filename":"12_中重點_施加罰款紀律行動指引（2018年4月）.pdf","path":"TC/12_中重點_施加罰款紀律行動指引（2018年4月）.pdf","studyTranslation":false},"en":{"filename":"12_Medium-Essential_Disciplinary Action Guideline on Pecuniary Penalty (Apr 2018).pdf","path":"EN/12_Medium-Essential_Disciplinary Action Guideline on Pecuniary Penalty (Apr 2018).pdf","studyTranslation":false}},"13":{"tc":{"filename":"13_中重點_紀律處分罰款指引（2018年5月）.pdf","path":"TC/13_中重點_紀律處分罰款指引（2018年5月）.pdf","studyTranslation":false},"en":{"filename":"13_Medium-Essential_Disciplinary Fining Guideline (May 2018).pdf","path":"EN/13_Medium-Essential_Disciplinary Fining Guideline (May 2018).pdf","studyTranslation":false}},"14":{"tc":{"filename":"14_中重點_通函_與交付渠道有關的洗錢及恐怖分子資金籌集風險（2021年12月13日）.pdf","path":"TC/14_中重點_通函_與交付渠道有關的洗錢及恐怖分子資金籌集風險（2021年12月13日）.pdf","studyTranslation":false},"en":{"filename":"14_Medium-Essential_Circular - ML-TF Risks of Delivery Channels (13 Dec 2021).pdf","path":"EN/14_Medium-Essential_Circular - ML-TF Risks of Delivery Channels (13 Dec 2021).pdf","studyTranslation":false}},"15":{"tc":{"filename":"15_中重點_通函_經金錢服務經營者牌照系統提交電子版交易報告定期申報表（2025年5月30日）.pdf","path":"TC/15_中重點_通函_經金錢服務經營者牌照系統提交電子版交易報告定期申報表（2025年5月30日）.pdf","studyTranslation":false},"en":{"filename":"15_Medium-Essential_Circular - E-submission of the Periodic Return (30 May 2025).pdf","path":"EN/15_Medium-Essential_Circular - E-submission of the Periodic Return (30 May 2025).pdf","studyTranslation":false}},"16":{"tc":{"filename":"16_中重點_通函_貨幣兌換商條例第34章之修訂（2025年11月17日）.pdf","path":"TC/16_中重點_通函_貨幣兌換商條例第34章之修訂（2025年11月17日）.pdf","studyTranslation":false},"en":{"filename":"16_Medium-Essential_Circular - Amendments to the Money Changers Ordinance Cap 34 (17 Nov 2025).pdf","path":"EN/16_Medium-Essential_Circular - Amendments to the Money Changers Ordinance Cap 34 (17 Nov 2025).pdf","studyTranslation":false}},"17":{"tc":{"filename":"17_中重點_貨幣兌換商條例全文（第34章） (2025-08-24, Bilingual).pdf","path":"TC/17_中重點_貨幣兌換商條例全文（第34章） (2025-08-24, Bilingual).pdf","studyTranslation":false},"en":{"filename":"17_Medium-Essential_Full Money Changers Ordinance, Cap. 34 (2025-08-24, Bilingual).pdf","path":"EN/17_Medium-Essential_Full Money Changers Ordinance, Cap. 34 (2025-08-24, Bilingual).pdf","studyTranslation":false}},"18":{"tc":{"filename":"18_中重點_通函_打擊以貿易進行洗錢活動指引（2026年1月20日）.pdf","path":"TC/18_中重點_通函_打擊以貿易進行洗錢活動指引（2026年1月20日）.pdf","studyTranslation":false},"en":{"filename":"18_Medium-Essential_Circular - Trade-based Money Laundering Guidance (20 Jan 2026).pdf","path":"EN/18_Medium-Essential_Circular - Trade-based Money Laundering Guidance (20 Jan 2026).pdf","studyTranslation":false}},"19":{"tc":{"filename":"19_中重點_通函_財務行動特別組織的聲明（2026年7月3日）.pdf","path":"TC/19_中重點_通函_財務行動特別組織的聲明（2026年7月3日）.pdf","studyTranslation":false},"en":{"filename":"19_Medium-Essential_Circular - Statements issued by the FATF (3 Jul 2026).pdf","path":"EN/19_Medium-Essential_Circular - Statements issued by the FATF (3 Jul 2026).pdf","studyTranslation":false}},"20":{"tc":{"filename":"20_中選讀_遞交業務計劃的指引（12-2019版）.pdf","path":"TC/20_中選讀_遞交業務計劃的指引（12-2019版）.pdf","studyTranslation":false},"en":{"filename":"20_Medium-Selected_Guidelines for Submission of Business Plan (Ver 12-2019).pdf","path":"EN/20_Medium-Selected_Guidelines for Submission of Business Plan (Ver 12-2019).pdf","studyTranslation":false}},"21":{"tc":{"filename":"21_中選讀_遞交打擊洗錢及恐怖分子資金籌集政策的指引（12-2019版）.pdf","path":"TC/21_中選讀_遞交打擊洗錢及恐怖分子資金籌集政策的指引（12-2019版）.pdf","studyTranslation":false},"en":{"filename":"21_Medium-Selected_Guidelines for Submission of AML-CFT Policy (Ver 12-2019).pdf","path":"EN/21_Medium-Selected_Guidelines for Submission of AML-CFT Policy (Ver 12-2019).pdf","studyTranslation":false}},"22":{"tc":{"filename":"22_中選讀_通函_實體貨幣及不記名可轉讓票據跨境流動條例（2018年7月31日）.pdf","path":"TC/22_中選讀_通函_實體貨幣及不記名可轉讓票據跨境流動條例（2018年7月31日）.pdf","studyTranslation":false},"en":{"filename":"22_Medium-Selected_Circular - Cross-boundary Movement of Currency Ordinance Cap 629 (31 Jul 2018).pdf","path":"EN/22_Medium-Selected_Circular - Cross-boundary Movement of Currency Ordinance Cap 629 (31 Jul 2018).pdf","studyTranslation":false}},"23":{"tc":{"filename":"23_中選讀_實體貨幣及不記名可轉讓票據跨境流動條例全文（第629章） (2026-07-31, Bilingual).pdf","path":"TC/23_中選讀_實體貨幣及不記名可轉讓票據跨境流動條例全文（第629章） (2026-07-31, Bilingual).pdf","studyTranslation":false},"en":{"filename":"23_Medium-Selected_Full Cross-boundary Movement of Physical Currency and Bearer Negotiable Instruments Ordinance, Cap. 629 (2026-07-31, Bilingual).pdf","path":"EN/23_Medium-Selected_Full Cross-boundary Movement of Physical Currency and Bearer Negotiable Instruments Ordinance, Cap. 629 (2026-07-31, Bilingual).pdf","studyTranslation":false}},"24":{"tc":{"filename":"24_Medium-Selected_Trade-Based Money Laundering Risk Indicators - FATF and Egmont (Mar 2021).pdf","path":"EN/24_Medium-Selected_Trade-Based Money Laundering Risk Indicators - FATF and Egmont (Mar 2021).pdf","studyTranslation":true},"en":{"filename":"24_Medium-Selected_Trade-Based Money Laundering Risk Indicators - FATF and Egmont (Mar 2021).pdf","path":"EN/24_Medium-Selected_Trade-Based Money Laundering Risk Indicators - FATF and Egmont (Mar 2021).pdf","studyTranslation":false}},"25":{"tc":{"filename":"25_中選讀_香港洗錢及恐怖分子資金籌集風險評估報告（2022年）.pdf","path":"TC/25_中選讀_香港洗錢及恐怖分子資金籌集風險評估報告（2022年）.pdf","studyTranslation":false},"en":{"filename":"25_Medium-Selected_Hong Kong Money Laundering and Terrorist Financing Risk Assessment Report (2022).pdf","path":"EN/25_Medium-Selected_Hong Kong Money Laundering and Terrorist Financing Risk Assessment Report (2022).pdf","studyTranslation":false}},"26":{"tc":{"filename":"26_中選讀_通函_聯合國制裁_原則及預警機制（2018年2月7日）.pdf","path":"TC/26_中選讀_通函_聯合國制裁_原則及預警機制（2018年2月7日）.pdf","studyTranslation":false},"en":{"filename":"26_Medium-Selected_Circular - United Nations Sanctions - Principles and Early Alerts (7 Feb 2018).pdf","path":"EN/26_Medium-Selected_Circular - United Nations Sanctions - Principles and Early Alerts (7 Feb 2018).pdf","studyTranslation":false}}},"questions":{"m1-gn71":["03"],"m1-127":["03"],"m1-128":["03"],"m1-129":["03","04"],"m1-130":["03"],"m1-131":["03"],"m1-132":["03"],"m1-133":["03"],"m1-134":["03"],"m1-135":["19"],"m1-136":["18"],"m1-137":["18"],"m1-138":["08"],"m1-139":["22"],"m1-143":["03"],"m1-144":["03"],"m1-145":["03"],"m1-146":["03"],"m1-147":["04"],"m1-148":["03"],"m1-150":["03"],"m1-151":["03","16"],"m1-152":["03"],"m1-160":["03"],"m1-161":["03","06","19"],"m1-178":["03"],"m1-179":["03"],"m1-180":["03"],"m1-189":["08"],"m1-190":["17"],"m1-191":["17"],"m1-192":["17"],"m1-193":["17"],"m1-194":["17"],"m1-195":["17"],"m1-196":["17"],"m1-197":["17"],"m1-198":["23"],"m1-199":["23"],"m1-200":["23"],"m1-201":["23"],"m1-202":["23"],"m1-203":["23"],"m1-204":["23"],"m1-205":["23"],"m1-206":["25"],"m1-207":["25"],"m1-208":["25"],"m1-209":["25"],"m1-210":["25"],"m1-211":["25"],"m1-212":["25"],"m1-213":["25"],"m1-214":["25"],"m1-215":["25"],"m1-216":["25"],"m1-217":["25"],"m1-218":["25"],"m1-219":["25"],"m1-220":["25"],"m2-ca2":["04"],"m2-309":["04"],"m2-310":["04"],"m2-311":["04"],"m2-312":["04"],"m2-313":["04"],"m2-314":["04"],"m2-315":["04"],"m2-316":["04"],"m2-317":["04"],"m2-318":["04"],"m2-321":["04"],"m2-322":["04"],"m2-323":["04"],"m2-324":["04"],"m2-340":["04"],"m2-341":["04"],"m2-342":["04"],"m2-343":["04"],"m2-344":["04"],"m2-345":["04"],"m2-346":["04"],"m2-347":["04"],"m2-348":["04"],"m2-349":["04"],"m2-350":["04"],"m2-351":["04"],"m2-352":["04"],"m2-353":["04"],"m2-325":["04"],"m2-326":["04"],"m2-327":["04"],"m2-328":["04"],"m2-329":["04"],"m2-330":["04"],"m2-331":["04"],"m2-332":["04"],"m2-333":["04"],"m2-334":["04"],"m2-335":["04"],"m2-336":["04"],"m2-337":["04"],"m2-338":["04"],"m2-354":["04"],"m2-355":["04"],"m2-356":["04","06"],"m2-357":["04"],"m2-358":["04"],"m2-359":["04"],"m2-360":["04"],"m2-363":["04"],"m2-364":["04"],"m2-365":["04"],"m2-366":["04"],"m2-367":["04"],"m2-368":["04"],"m2-369":["04"],"m2-370":["04"],"m2-371":["04"],"m2-372":["04"],"m2-373":["04"],"m2-374":["04"],"m2-375":["04"],"m2-376":["04"],"m2-377":["04"],"m2-378":["04"],"m2-379":["04"],"m2-380":["04"],"m2-381":["04"],"m2-382":["04"],"m2-383":["04"],"m2-384":["04"],"m2-385":["04"],"m2-386":["04"],"m2-387":["04"],"m3-ca3":["04"],"m3-262":["03","04"],"m3-263":["04"],"m3-264":["04"],"m3-265":["04"],"m3-266":["04"],"m3-267":["04"],"m3-268":["04"],"m3-269":["04"],"m3-270":["04"],"m3-271":["04"],"m3-272":["04"],"m3-273":["04"],"m3-274":["04"],"m3-275":["04"],"m3-276":["04"],"m3-277":["04"],"m3-278":["04"],"m3-279":["04"],"m3-280":["04"],"m3-281":["04"],"m3-282":["04"],"m3-283":["04"],"m3-284":["04"],"m3-285":["04"],"m3-286":["04"],"m3-292":["04"],"m3-293":["04"],"m3-294":["04"],"m3-295":["04"],"m3-296":["04"],"m3-297":["04"],"m3-298":["04"],"m3-300":["04"],"m3-301":["04"],"m3-302":["04"],"m3-303":["04"],"m3-304":["04"],"m3-305":["04"],"m3-306":["04"],"m3-322":["04"],"m3-323":["04"],"m3-324":["04"],"m3-325":["04"],"m3-326":["04"],"m3-327":["04"],"m3-328":["04"],"m3-329":["04"],"m3-330":["04"],"m3-331":["04"],"m3-332":["04"],"m3-333":["04"],"m3-334":["04"],"m3-335":["04"],"m3-336":["04"],"m3-337":["04"],"m3-338":["04"],"m3-339":["04"],"m3-340":["04"],"m3-341":["04"],"m3-342":["04"],"m3-343":["04"],"m3-344":["04"],"m3-345":["04"],"m3-346":["04"],"m4-ca4":["05"],"m4-311":["05"],"m4-312":["05"],"m4-313":["01"],"m4-314":["01"],"m4-315":["01","05"],"m4-316":["01"],"m4-317":["01"],"m4-318":["05"],"m4-319":["05"],"m4-320":["05"],"m4-321":["05"],"m4-322":["05","15"],"m4-323":["20"],"m4-324":["21"],"m4-325":["11"],"m4-326":["12","13"],"m4-327":["05"],"m4-328":["05"],"m4-330":["05"],"m4-331":["05"],"m4-332":["05"],"m4-333":["05"],"m4-334":["05"],"m4-335":["05"],"m4-336":["05"],"m4-337":["05"],"m4-338":["05"],"m4-339":["05"],"m4-342":["01"],"m4-343":["01"],"m4-344":["01"],"m4-345":["01"],"m4-346":["10","11"],"m4-347":["11"],"m4-348":["11"],"m4-349":["20"],"m4-350":["20"],"m4-351":["21"],"m4-352":["21"],"m4-353":["21"],"m4-354":["12","13"],"m4-355":["12","13"],"m4-356":["12","13"],"m4-357":["05","06","20"],"m4-364":["04"],"m4-365":["04","05"],"m4-373":["05"],"m4-374":["05"],"m4-375":["05"],"m4-376":["05"],"m4-377":["05"],"m4-378":["11"],"m4-379":["20"],"m4-380":["01"],"m4-381":["13"],"m4-382":["05"],"m4-390":["15"],"m4-391":["15"],"m4-392":["09"],"m4-393":["09"],"m4-394":["26"],"m4-395":["26"],"m4-396":["05"],"m4-397":["05"],"m4-398":["05"],"m4-399":["05"],"m4-400":["05"],"m4-401":["05"],"m4-402":["05"],"m4-403":["05"],"m4-404":["05"],"m4-405":["01"],"m4-406":["01"],"m4-407":["01"],"m4-408":["01"],"m4-409":["11"],"m4-410":["12"],"m4-411":["20"],"m4-412":["21"],"m5-07":["03"],"m5-08":["03"],"m5-12":["03"],"m5-16":["03"],"m5-18":["03"],"m5-19":["03"],"m5-21":["03"],"m5-22":["03"],"m5-26":["03"],"m5-29":["03"],"m5-30":["03"],"m5-31":["03","14"],"m5-33":["03"],"m5-34":["03"],"m5-37":["03"],"m5-39":["03"],"m5-44":["03"],"m5-46":["03"],"m5-47":["03"],"m5-53":["03"],"m5-56":["03"],"m5-57":["03"],"m5-58":["03"],"m5-61":["03"],"m5-63":["03","04"],"m5-64":["03"],"m5-65":["03"],"m5-67":["03"],"m5-68":["03"],"m5-69":["03"],"m5-74":["03"],"m5-75":["03"],"m5-77":["03"],"m5-80":["03"],"m5-88":["03"],"m5-89":["03"],"m5-92":["03"],"m5-ca1":["03"],"m5-97":["03"],"m5-98":["03"],"m5-99":["03"],"m5-100":["03"],"m5-101":["03"],"m5-102":["03"],"m5-103":["03"],"m5-104":["03"],"m5-105":["03"],"m5-106":["03"],"m5-107":["03"],"m5-108":["03"],"m5-109":["03"],"m5-110":["03"],"m5-111":["03"],"m5-112":["21"],"m5-113":["03"],"m5-114":["03"],"m5-115":["24"],"m5-116":["24"],"m5-117":["25"],"m5-118":["25"],"m5-119":["25"],"m5-120":["25"],"m5-121":["03"],"m5-122":["03"],"m5-123":["03"],"m5-124":["03"],"m5-125":["03"],"m5-126":["03"],"m5-127":["03"],"m5-128":["03"],"m5-129":["03"],"m5-130":["03"],"m5-131":["03"],"m5-132":["03"],"m5-133":["03"],"m5-134":["03"],"m5-135":["03"],"m5-136":["03"],"m5-138":["03"],"m5-137":["18"],"m6-ca7":["03"],"m6-341":["03"],"m6-342":["03","06"],"m6-343":["03","06","07"],"m6-344":["03"],"m6-345":["03","06"],"m6-346":["03","07"],"m6-347":["03"],"m6-348":["03","06"],"m6-349":["03","06","07"],"m6-350":["03","06"],"m6-351":["03"],"m6-352":["03"],"m6-353":["03"],"m6-354":["03"],"m6-355":["03","06"],"m6-356":["08"],"m6-357":["03"],"m6-358":["03","06"],"m6-359":["03","06"],"m6-360":["03"],"m6-361":["03","06"],"m6-362":["03","06"],"m6-363":["03"],"m6-364":["03"],"m6-365":["03"],"m6-366":["03"],"m6-367":["03","06"],"m6-368":["03"],"m6-369":["07"],"m6-370":["03"],"m6-371":["03"],"m6-372":["03","06"],"m6-373":["03"],"m6-374":["03"],"m6-375":["03"],"m6-376":["03"],"m6-377":["03","06"],"m6-378":["03","06"],"m6-379":["03"],"m6-380":["14"],"m6-381":["08"],"m6-382":["08"],"m6-383":["08"],"m6-384":["08"],"m6-386":["03","04","06"],"m6-388":["06"],"m6-396":["03"],"m6-397":["06"],"m6-398":["04","08"],"m6-399":["06"],"m6-400":["03"],"m6-410":["03"],"m6-412":["06"],"m6-413":["03"],"m6-414":["03"],"m6-415":["03","06"],"m6-416":["03","06"],"m6-417":["06"],"m6-426":["03","04"],"m6-427":["03"],"m6-428":["03"],"m6-429":["03"],"m6-430":["03"],"m6-442":["03"],"m6-443":["03"],"m6-444":["03"],"m6-445":["03"],"m6-446":["03","06"],"m6-447":["03"],"m6-448":["06"],"m6-449":["03","14"],"m6-460":["03","08"],"m6-470":["03","06"],"m6-471":["24"],"m6-472":["24"],"m6-473":["24"],"m6-474":["24"],"m6-475":["24"],"m6-476":["18"],"m6-477":["18"],"m6-478":["03"],"m6-479":["03"],"m6-480":["03"],"m6-481":["03"],"m6-482":["03","06"],"m6-483":["03"],"m6-484":["03"],"m6-485":["03"],"m6-486":["03","06"],"m6-487":["03"],"m6-488":["03"],"m6-489":["03","06"],"m6-490":["03"],"m6-491":["03"],"m6-492":["03"],"m6-493":["03"],"m6-494":["03","06"],"m6-495":["03","08"],"m6-496":["08"],"m7-ca5":["03"],"m7-ca6":["03"],"m7-155":["03"],"m7-156":["03"],"m7-157":["03"],"m7-158":["03"],"m7-159":["03"],"m7-160":["03"],"m7-161":["03"],"m7-162":["03"],"m7-163":["03"],"m7-164":["03"],"m7-165":["03"],"m7-166":["03"],"m7-167":["03"],"m7-168":["03"],"m7-169":["03"],"m7-170":["03"],"m7-171":["03"],"m7-172":["03"],"m7-173":["03"],"m7-174":["03"],"m7-175":["03"],"m7-176":["03"],"m7-177":["03"],"m7-178":["03"],"m7-179":["03"],"m7-180":["03"],"m7-181":["03"],"m7-182":["03"],"m7-183":["03"],"m7-184":["03"],"m7-185":["03"],"m7-186":["03"],"m7-187":["03"],"m7-188":["03"],"m7-189":["03","06"],"m7-190":["03"],"m7-191":["03"],"m7-192":["03"],"m7-193":["24"],"m7-194":["24"],"m7-195":["24"],"m7-196":["25"],"m7-197":["25"],"m7-198":["25"],"m7-199":["03"],"m7-200":["03"],"m7-201":["03"],"m7-202":["03"],"m7-203":["03"],"m7-204":["03"],"m7-205":["03"],"m7-206":["03"],"m7-207":["03"],"m7-208":["03"],"m7-209":["03"],"m7-210":["03"],"m7-211":["03"],"m7-212":["03"],"m7-213":["03"],"m7-214":["03"],"m7-215":["03"],"m7-216":["03"],"m7-217":["03"]}};
/* END GENERATED SOURCE INDEX */

/* ---------------- constants ---------------- */

const MODULES = [
  { n: 1, en: 'General knowledge on AML/CFT and Counter Proliferation Financing',
    tc: '有關打擊洗錢及恐怖分子資金籌集與打擊擴散資金籌集的常識' },
  { n: 2, en: 'Parts 1–7 of the AMLO', tc: '《打擊洗錢條例》第1至7部' },
  { n: 3, en: 'Schedules to the AMLO', tc: '《打擊洗錢條例》的附表' },
  { n: 4, en: 'Guidelines promulgated by the C&ED', tc: '海關頒布的指引' },
  { n: 5, en: "MSO's systems and controls (i): institutional governance and strategy",
    tc: '金錢服務經營者的系統及管控措施(i)：機構層面的管治及策略' },
  { n: 6, en: "MSO's systems and controls (ii): AML/CFT control areas",
    tc: '金錢服務經營者的系統及管控措施(ii)：打擊洗錢及恐怖分子資金籌集的管控範疇' },
  { n: 7, en: "MSO's systems and controls (iii): demonstrating and monitoring compliance",
    tc: '金錢服務經營者的系統及管控措施(iii)：證明符合規定及監察合規水平' },
];

const CFG = {
  perModule: 5,
  total: 35,
  passTotal: 25,
  maxWrongPerModule: 2,
  minutes: 75,
};

/* ---------------- state ---------------- */

let bank = [];
let byMod = new Map();          // module n -> [questions]
let byId = new Map();           // id -> question
let S = { lang: null, view: 'home', theme: 'auto' };   // lang null = not chosen yet; theme auto|light|dark
let exam = null;                // active exam state
let practice = null;            // active practice state
let reviewAttempt = null;       // attempt shown on results view
let justFinished = false;       // results view: fresh submit vs history review
let timerId = null;
let homeNotice = null;          // one-shot message on home
let pmodSel = new Set([1, 2, 3, 4, 5, 6, 7]); // practice module selection
const inPractice = q => pmodSel.has(q.module);
let reviewFilter = 'all';       // results view: 'all' | 'wrong'
let homeTick = null;            // ticks the "time left" on the home resume card
const BASE_TITLE = document.title;

const qs = new URLSearchParams(location.search);
const customMinutes = qs.has('minutes') ? Math.max(0.05, parseFloat(qs.get('minutes')) || CFG.minutes) : null;

/* ---------------- storage ---------------- */

const store = {
  get(k, fallback) {
    try { const v = localStorage.getItem('msoca:' + k); return v === null ? fallback : JSON.parse(v); }
    catch { return fallback; }
  },
  set(k, v) { try { localStorage.setItem('msoca:' + k, JSON.stringify(v)); } catch {} },
  del(k) { try { localStorage.removeItem('msoca:' + k); } catch {} },
};

const attemptsKey = () => 'attempts';
const examKey = () => 'exam';

/* The wrong-answer book: every question answered wrong, in practice or in a
   mock, stays listed until it is answered right twice in a row. `seen` is every
   question answered at least once, so practice can draw unseen questions first. */
const book = { get: () => store.get('book', {}), set: v => store.set('book', v) };
const seenIds = () => new Set(store.get('seen', []));
function recordAnswer(qid, ok) {
  const seen = seenIds(); seen.add(qid); store.set('seen', [...seen]);
  const b = book.get(), e = b[qid];
  if (!ok) b[qid] = { w: (e ? e.w : 0) + 1, k: 0, t: Date.now() };
  else if (e && ++e.k >= 2) delete b[qid];
  book.set(b);
}
const bookIds = () => Object.keys(book.get()).filter(id => byId.has(id));

/* ---------------- helpers ---------------- */

const $ = sel => document.querySelector(sel);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => (
  { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

/* inline SVG icons (render identically on Windows and Mac, unlike emoji) */
const ICONS = {
  clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  flag: '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
  check: '<path d="M5 13l4 4L19 7"/>',
  x: '<path d="M6 6l12 12M18 6L6 18"/>',
};
const icon = n => `<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">${ICONS[n]}</svg>`;

/* theme: explicit light/dark, or auto = follow the operating system */
const darkQuery = window.matchMedia('(prefers-color-scheme: dark)');
function applyTheme() {
  const dark = S.theme === 'dark' || (S.theme === 'auto' && darkQuery.matches);
  document.documentElement.dataset.theme = dark ? 'dark' : 'light';
}
darkQuery.addEventListener('change', () => { if (S.theme === 'auto') applyTheme(); });

function toast(msg) {
  let el = document.querySelector('.toast');
  if (!el) { el = document.createElement('div'); el.className = 'toast'; document.body.appendChild(el); }
  el.textContent = msg;
  clearTimeout(toast.t);
  requestAnimationFrame(() => el.classList.add('show'));
  toast.t = setTimeout(() => el.classList.remove('show'), 3500);
}

/* Every question has the shape of the real paper: a stem, four to six numbered
   statements, and five options a)–e) naming which statements are correct. An
   item stores its statements, which of them are true, and its options as sets of
   statement numbers; the labels ("1, 2 and 4", 「1、2 及 4」) are written here.

   The statements are reordered every time a question is drawn, and the options
   renumbered to match, so that the letter of an answer cannot be memorised. Each
   item's notes follow its statements. Options are shown as C&ED prints them: its own block in its own
   order, otherwise smaller sets first and then by number, with "All of the
   above" or "None of the above" always last. */
const LETTERS = 'ABCDE';
const OFFICIAL4 = [[1, 2, 3], [1, 2, 4], [2, 3, 4], [1, 3, 4]];        // MSSB/CA_01/2021, then e) All of the above
const GN71 = [[1, 2, 3], [2, 3, 4], [1, 3, 4], [1, 2, 5], [3, 4, 5]];  // Guidance Notes ¶7.1
const isToken = o => o === 'all' || o === 'none';
const identityPerm = q => q.truth.map((_, i) => i);
const drawPerm = q => shuffle(identityPerm(q));
/* A stored order is used only while it still fits the item: the same number of
   statements, each once. History outlives the file it was made in, and an item
   may since have gained a statement. */
function permFor(q, stored) {
  if (Array.isArray(stored) && stored.length === q.truth.length &&
      [...stored].sort((a, b) => a - b).every((v, i) => v === i)) return stored;
  return identityPerm(q);
}

/* The question as drawn: perm[d] is the statement shown at position d; `shown`
   holds each stored option renumbered accordingly, and `order` the stored option
   indices in the order they are displayed. Answers are kept as stored indices, so
   grading never depends on the draw. */
function arrange(q, perm) {
  const at = [];
  perm.forEach((orig, d) => { at[orig] = d + 1; });
  const shown = q.options.map(o => isToken(o) ? o : o.map(x => at[x - 1]).sort((a, b) => a - b));
  return { perm, shown, order: displayOrder(shown, q.truth.length) };
}

function displayOrder(shown, n) {
  const idx = shown.map((_, i) => i);
  const body = idx.filter(i => !isToken(shown[i])), tail = idx.filter(i => isToken(shown[i]));
  const key = s => s.join(',');
  const find = block => block.map(b => body.find(i => key(shown[i]) === key(b)));
  const is = block => body.length === block.length && find(block).every(i => i !== undefined);
  let ordered;
  if (n === 4 && tail.length === 1 && is(OFFICIAL4)) ordered = find(OFFICIAL4);
  else if (n === 5 && tail.length === 0 && is(GN71)) ordered = find(GN71);
  else ordered = body.slice().sort((a, b) => cmpSets(shown[a], shown[b]));
  return ordered.concat(tail);
}

function cmpSets(a, b) {
  if (a.length !== b.length) return a.length - b.length;
  for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return a[i] - b[i];
  return 0;
}

function optLabel(o, lang) {
  if (o === 'all') return lang === 'en' ? 'All of the above' : '以上皆是';
  if (o === 'none') return lang === 'en' ? 'None of the above' : '以上皆非';
  if (lang === 'en') return o.length === 1 ? `${o[0]} only` : o.slice(0, -1).join(', ') + ' and ' + o[o.length - 1];
  return o.length === 1 ? `只有 ${o[0]}` : o.slice(0, -1).join('、') + ' 及 ' + o[o.length - 1];
}

/* the kinds of defect a false statement carries (bank/FORMAT.md) */
const TRAPS = {
  offlist: ['Not on the list', '清單以外'],
  added: ['A word added', '多了字眼'],
  scope: ['Scope changed', '範圍改了'],
  reversed: ['Rule reversed', '原則顛倒'],
  qualifier: ['Qualifier dropped', '漏了限定語'],
  number: ['Wrong number', '數字有誤'],
  period: ['Wrong time limit', '期限有誤'],
  actor: ['Wrong person or body', '主體有誤'],
  modal: ['Strength changed', '語氣強弱改了'],
  name: ['Wrong name', '名稱有誤'],
  condition: ['Wrong case', '情況錯配'],
};

function shuffle(a) {
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/* ui(en, tc): chrome text in the current language mode */
function ui(en, tc) {
  if (S.lang === 'en') return en;
  if (S.lang === 'tc') return tc;
  return en + ' · ' + tc;
}

/* bilingual content block (stem / explanation / note) */
function contentPair(en, tc) {
  en = esc(en); tc = esc(tc);
  if (S.lang === 'en') return en ? `<div>${en}</div>` : '';
  if (S.lang === 'tc') return tc ? `<div>${tc}</div>` : '';
  return en || tc ? `<div>${en}</div><div class="tcline">${tc}</div>` : '';
}
const contentHTML = (obj, field) => contentPair(obj.en[field], obj.tc[field]);

/* an option as shown: a set of statement numbers, or All / None of the above */
function optionHTML(o) {
  const en = esc(optLabel(o, 'en')), tc = esc(optLabel(o, 'tc'));
  if (S.lang === 'en') return en;
  if (S.lang === 'tc') return tc;
  return `${en}<span class="tcline">${tc}</span>`;
}

/* The numbered statements, in the order drawn. Once a question is answered
   (`reveal`) each is marked correct or not, with the kind of trap a false one
   sets and the note saying why, in the source's words. */
function statementsHTML(q, perm, reveal = false) {
  const rows = perm.map(i => {
    const e = esc(q.en.statements[i]), t = esc(q.tc.statements[i]);
    const body = S.lang === 'en' ? e : S.lang === 'tc' ? t : `${e}<span class="tcline">${t}</span>`;
    if (!reveal) return `<li>${body}</li>`;
    const ok = q.truth[i];
    const trap = !ok && q.traps && TRAPS[q.traps[i]];
    const note = q.en.notes ? contentPair(q.en.notes[i], q.tc.notes[i]) : '';
    return `<li class="${ok ? 'st-true' : 'st-false'}">${body}
      <div class="st-verdict">${ok ? icon('check') + ' ' + ui('Correct', '正確') : icon('x') + ' ' + ui('Incorrect', '不正確')}${
        trap ? `<span class="trap">· ${ui('Trap', '陷阱')}: ${ui(trap[0], trap[1])}</span>` : ''}</div>
      ${note ? `<div class="st-note">${note}</div>` : ''}</li>`;
  }).join('');
  return `<ol class="stmts">${rows}</ol>`;
}

function stemHTML(q, perm, reveal = false) {
  return `<div class="stem">${contentHTML(q, 'q')}</div>${statementsHTML(q, perm, reveal)}`;
}

/* the five options of a drawn question; `cls(orig)` styles each one */
function optsHTML(arr, cls = () => '', disabled = false) {
  return arr.order.map((orig, di) => `
    <button class="opt ${cls(orig)}" data-orig="${orig}" ${disabled ? 'disabled' : ''}>
      <span class="letter">${LETTERS[di]}</span>
      <span class="otext">${optionHTML(arr.shown[orig])}</span>
    </button>`).join('');
}

function sourceHTML(q) {
  const src = S.lang === 'en' ? q.source.en : S.lang === 'tc' ? q.source.tc : q.source.en + ' · ' + q.source.tc;
  const langs = S.lang === 'both' ? ['tc','en'] : [S.lang];
  const files = (SOURCE_INDEX.questions[q.id] || []).map(doc => langs.map(lang => {
    const file = SOURCE_INDEX.documents[doc][lang];
    const translation = file.studyTranslation ? ' · 學習譯文，英文原件' : '';
    return `<div class="source-file" lang="${lang === 'tc' ? 'zh-Hant' : 'en'}"><a href="../docs/${encodeURI(file.path)}" target="_blank" rel="noopener">${esc(file.filename)}</a>${translation}</div>`;
  }).join('')).join('');
  return `<div class="cite"><b>${ui('Source', '出處')}:</b> ${esc(src)}<div class="source-files">${files}</div></div>`;
}

function modName(n) {
  const m = MODULES[n - 1];
  return ui(m.en, m.tc);
}

function fmtTime(ms) {
  const t = Math.max(0, Math.ceil(ms / 1000));
  const h = Math.floor(t / 3600), m = Math.floor((t % 3600) / 60), s = t % 60;
  const mm = String(m).padStart(2, '0'), ss = String(s).padStart(2, '0');
  return h > 0 ? `${h}:${mm}:${ss}` : `${m}:${ss}`;
}

function fmtDate(ts) {
  const d = new Date(ts);
  return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }) + ' ' +
         d.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' });
}

/* ---------------- scoring ---------------- */

function grade(qids, answers) {
  const moduleWrong = [0, 0, 0, 0, 0, 0, 0];
  const moduleTotal = [0, 0, 0, 0, 0, 0, 0];
  let score = 0;
  for (const qid of qids) {
    const q = byId.get(qid);
    if (!q) continue;
    moduleTotal[q.module - 1]++;
    if (answers[qid] === q.answer) score++;
    else moduleWrong[q.module - 1]++;
  }
  const floorsOK = moduleWrong.every(w => w <= CFG.maxWrongPerModule);
  const totalOK = score >= CFG.passTotal;
  return { score, moduleWrong, moduleTotal, floorsOK, totalOK, pass: floorsOK && totalOK };
}

// A saved attempt keeps the result it was given when submitted. Questions can later be removed from
// the bank or re-keyed, so grading the answers again would change a recorded pass or fail; show the
// recorded result instead, and count each module's questions from the ids (m6-12 is module 6).
function recordedResult(a) {
  if (typeof a.score !== 'number' || !Array.isArray(a.moduleWrong)) return grade(a.qids, a.answers);
  const moduleTotal = [0, 0, 0, 0, 0, 0, 0];
  for (const qid of a.qids) {
    const q = byId.get(qid);
    const m = q ? q.module : Number((/^m(\d)-/.exec(qid) || [])[1]);
    if (m >= 1 && m <= 7) moduleTotal[m - 1]++;
  }
  const floorsOK = a.moduleWrong.every(w => w <= CFG.maxWrongPerModule);
  const totalOK = a.score >= CFG.passTotal;
  return { score: a.score, moduleWrong: a.moduleWrong, moduleTotal, floorsOK, totalOK, pass: !!a.pass };
}

/* ---------------- render root ---------------- */

function render() {
  stopTimer();
  clearInterval(homeTick);
  if (S.view !== 'exam') document.title = BASE_TITLE;
  const app = $('#app');
  if (S.view === 'exam') app.innerHTML = examView();
  else if (S.view === 'results') app.innerHTML = resultsView();
  else if (S.view === 'practice') app.innerHTML = practiceView();
  else app.innerHTML = homeView();
  bindCommon();
  if (S.view === 'exam') { bindExam(); startTimer(); }
  else if (S.view === 'practice') bindPractice();
  else if (S.view === 'results') bindResults();
  else bindHome();
}

/* ---------------- top bar ---------------- */

function topbarHTML() {
  const activePart = S.view === 'practice' && practice ? byId.get(practice.pool[practice.idx]).module : S.view === 'exam' && exam ? byId.get(exam.qids[exam.cur]).module : 1;
  return `
  <div class="topbar"><div class="wrap">
    <div class="brand">
      <div class="t1">${ui('MSO Competence Assessment', '金錢服務經營者能力評核')}</div>
      <div class="t2">${ui('C&ED · 35 questions · 7 modules · 75 minutes', '香港海關 · 35題 · 7個單元 · 75分鐘')}</div>
    </div>
    <div class="topctl">
      <a class="study-entry" href="../revision/study-notes/part-${activePart}.html?lang=${S.lang || 'tc'}" target="_blank" rel="noopener">${ui('Study notes', '溫習資料')}</a>
      ${S.lang ? `<div class="seg" id="langseg">
        <button data-lang="en" class="${S.lang === 'en' ? 'on' : ''}">EN</button>
        <button data-lang="tc" class="${S.lang === 'tc' ? 'on' : ''}">中文</button>
        <button data-lang="both" class="${S.lang === 'both' ? 'on' : ''}">EN+中</button>
      </div>` : ''}
      <div class="seg" id="themeseg">
        <button data-theme="auto" class="${S.theme === 'auto' ? 'on' : ''}">${ui('Auto', '自動')}</button>
        <button data-theme="light" class="${S.theme === 'light' ? 'on' : ''}">${ui('Light', '淺色')}</button>
        <button data-theme="dark" class="${S.theme === 'dark' ? 'on' : ''}">${ui('Dark', '深色')}</button>
      </div>
    </div>
  </div></div>`;
}

function bindCommon() {
  document.querySelectorAll('#langseg button').forEach(b => {
    b.onclick = () => {
      S.lang = b.dataset.lang;
      store.set('lang', S.lang);
      render();
    };
  });
  document.querySelectorAll('#themeseg button').forEach(b => {
    b.onclick = () => {
      S.theme = b.dataset.theme;
      store.set('theme', S.theme);
      applyTheme();
      render();
    };
  });
}

/* ---------------- home ---------------- */

function homeView() {
  if (!S.lang) return langView();
  const attempts = store.get(attemptsKey(), []);
  const saved = store.get(examKey(), null);
  const minutes = customMinutes || CFG.minutes;

  const examCard = saved ? `
    <div class="card">
      <h2>${ui('Mock exam in progress', '模擬試進行中')}</h2>
      <div class="sub">${ui('The clock keeps running while you are away.', '離開期間計時不會暫停。')}
        ${ui('Time left', '剩餘時間')}: <b id="resume-left">${fmtTime(saved.endsAt - Date.now())}</b></div>
      <div class="actions">
        <button class="btn" id="btn-resume">${ui('Resume exam', '繼續作答')}</button>
        <button class="btn secondary" id="btn-discard">${ui('Discard attempt', '放棄此卷')}</button>
      </div>
    </div>` : `
    <div class="card">
      <h2>${ui('Mock exam', '模擬試')}</h2>
      <div class="sub">${ui(
        `35 questions (7 modules × 5), ${minutes === CFG.minutes ? '75 minutes' : minutes + ' minutes (custom)'}, drawn at random from a bank of ${bank.length}. Every question has the real paper's shape: numbered statements, and five options naming which of them are correct. The statements are reordered each time a question is drawn.`,
        `35題（7個單元 × 每單元5題），限時${minutes === CFG.minutes ? '75' : minutes}分鐘，從${bank.length}題題庫隨機抽出。全部採用真實試卷的格式：題目列出編號陳述，五個選項列出哪幾項正確。每次抽題，陳述的次序都會重新排列。`)}</div>
      <div class="rulebox">${ui(
        '<b>Pass rules (both required):</b> at most 2 wrong in <b>each</b> module, and a total of <b>25/35</b> or above. 32/35 still fails if one module has 3 mistakes.',
        '<b>及格準則（兩項須同時符合）：</b>每個單元錯題不多於2題，及全卷總分達<b>25/35</b>。即使總分32/35，只要任何一個單元錯3題即全卷不及格。')}</div>
      <div class="actions">
        <button class="btn" id="btn-start" ${bank.length ? '' : 'disabled'}>${ui('Start mock exam', '開始模擬試')}</button>
      </div>
    </div>`;

  const chips = MODULES.map(m =>
    `<button class="chip ${pmodSel.has(m.n) ? 'on' : ''}" data-pm="${m.n}" aria-pressed="${pmodSel.has(m.n)}">${ui(`Part ${m.n}`, `第${m.n}部分`)} ${esc(shortMod(m))}</button>`).join('');
  const seen = seenIds();
  const selected = bank.filter(inPractice), unseen = selected.filter(q => !seen.has(q.id)).length;
  const wrong = bookIds().length;

  return topbarHTML() + `
  <div class="wrap">
    ${homeNotice ? `<div class="card"><div class="sub" style="margin:0">${homeNotice}</div></div>` : ''}
    <p class="scope-note">${ui('Question sources: documents 01–26 in your reading library.', '出題範圍：閱讀文檔庫第01–26份文件。')}</p>
    ${examCard}
    <div class="card">
      <h2>${ui('Custom practice', '自選練習')}</h2>
      <div class="sub">${ui('Choose one or more parts. Untimed, with an explanation and source for every statement after each answer.',
        '可選擇一個或多個部分，不設時限。每題作答後，逐句顯示正確與否、陷阱解釋及原文出處。')}</div>
      <div class="chips" id="pmods">${chips}
        <button class="chip" id="pm-all">${ui('All', '全選')}</button>
      </div>
      <div class="actions">
        <button class="btn secondary" id="btn-practice" ${bank.length ? '' : 'disabled'}>${ui('Start practice', '開始練習')}</button>
        <span class="note">${ui(`${unseen} of ${selected.length} selected questions not yet answered; those come first.`,
          `所選${selected.length}題中有${unseen}題未做過，會先抽未做過的。`)}</span>
      </div>
    </div>
    <div class="card">
      <h2>${ui('Wrong-answer book', '錯題本')} · ${wrong}</h2>
      <div class="sub">${ui('Every question answered wrong in practice or in a mock exam is kept here until you answer it right twice in a row.',
        '練習或模擬試答錯的題目會記在這裏，連續答對兩次才移除。')}</div>
      <div class="actions">
        <button class="btn" id="btn-book" ${wrong ? '' : 'disabled'}>${ui('Practise the book', '練錯題')}</button>
        ${wrong ? `<button class="btn secondary small" id="btn-book-clear">${ui('Clear the book', '清空錯題本')}</button>` : ''}
      </div>
    </div>
    <details class="exam-history">
      <summary>${ui('Mock exam results and history', '模擬試成績及紀錄')} · ${attempts.length}</summary>
      ${attempts.length ? progressCardHTML(attempts) : ''}
    <div class="card">
      <h2>${ui('History', '過往紀錄')}</h2>
      ${attempts.length ? historyHTML(attempts) : `<div class="sub" style="margin:0">${ui('No attempts yet.', '未有應考紀錄。')}</div>`}
      <div class="actions">
        ${attempts.length ? `<button class="btn secondary small" id="btn-save">${ui('Save history to file (.md)', '儲存紀錄至檔案 (.md)')}</button>` : ''}
        <button class="btn secondary small" id="btn-load">${ui('Load history from file', '從檔案載入紀錄')}</button>
        ${attempts.length ? `<button class="btn secondary small" id="btn-clear">${ui('Clear history', '清除紀錄')}</button>` : ''}
        <input type="file" id="file-load" accept=".md,.json,.txt,text/markdown,application/json" hidden>
        <span class="note">${ui('History lives in this browser; the file is a readable backup you can load on any computer.',
          '紀錄儲存於此瀏覽器；檔案是可閱讀的備份，可在任何電腦載入。')}</span>
      </div>
    </div>
    </details>
    <div class="footer">${ui(
      'Practice questions are reconstructions from official C&ED / e-Legislation materials, not real exam questions. ' +
      'C&ED publishes no answers beyond a few sample questions, and where the sources conflict or are unclear, ' +
      'the answer follows the most defensible reading. Not an official C&ED product, and not legal advice.',
      '練習題按官方材料重構而成，並非真題。除少量參考試題外，香港海關沒有公布答案；如原始文件互相矛盾或意思不清晰，' +
      '答案採用最有根據的解讀。本程式並非香港海關的官方產品，亦不構成法律意見。')}</div>
  </div>`;
}

function shortMod(m) {
  /* compact module label for chips */
  const shortEn = ['General AML/CFT', 'AMLO Parts 1–7', 'AMLO Schedules', 'C&ED guidelines',
    'Governance', 'Control areas', 'Compliance'][m.n - 1];
  const shortTc = ['常識', '條例1–7部', '條例附表', '海關指引', '管治', '管控範疇', '證明合規'][m.n - 1];
  return ui(shortEn, shortTc);
}

function historyHTML(attempts) {
  const rows = [...attempts].reverse().map((a, ri) => {
    const idx = attempts.length - 1 - ri;
    const cells = a.moduleWrong.map((w, i) =>
      `<i class="${w <= CFG.maxWrongPerModule ? 'ok' : 'bad'}" title="M${i + 1}: ${w} wrong">${w}</i>`).join('');
    return `<tr>
      <td>${fmtDate(a.ts)}</td>
      <td class="num">${a.score}/${a.qids.length}</td>
      <td><span class="modcells">${cells}</span></td>
      <td><span class="tag ${a.pass ? 'pass' : 'fail'}">${a.pass ? ui('PASS', '合格') : ui('FAIL', '不合格')}</span></td>
      <td><button class="btn secondary small" data-review="${idx}">${ui('Review', '重溫')}</button></td>
    </tr>`;
  }).join('');
  return `<div class="tablewrap"><table class="hist">
    <tr><th>${ui('Date', '日期')}</th><th>${ui('Score', '分數')}</th>
    <th>${ui('Wrong per module (M1–M7)', '各單元錯題數（M1–M7）')}</th><th></th><th></th></tr>
    ${rows}</table></div>`;
}

function bindHome() {
  homeNotice = null;
  const start = $('#btn-start');
  if (start) start.onclick = () => startExam();
  const resume = $('#btn-resume');
  if (resume) resume.onclick = () => resumeExam();
  const left = $('#resume-left');
  if (left) homeTick = setInterval(() => {
    const s = store.get(examKey(), null);
    if (!s) return;
    if (Date.now() >= s.endsAt) { exam = s; finishExam(true); return; }
    left.textContent = fmtTime(s.endsAt - Date.now());
  }, 1000);
  const discard = $('#btn-discard');
  if (discard) discard.onclick = () => {
    confirmModal(
      ui('Discard this attempt?', '確定放棄此卷？'),
      ui('The exam in progress will be deleted. It will not appear in your history.', '進行中的模擬試將被刪除，且不會計入紀錄。'),
      ui('Discard', '放棄'), () => { store.del(examKey()); render(); }, true);
  };
  const prac = $('#btn-practice');
  if (prac) prac.onclick = () => startPractice();
  const bookBtn = $('#btn-book');
  if (bookBtn) bookBtn.onclick = () => startPractice(shuffle(bookIds()));
  const bookClear = $('#btn-book-clear');
  if (bookClear) bookClear.onclick = () => confirmModal(
    ui('Clear the wrong-answer book?', '清空錯題本？'),
    ui('Every question listed in the book will be removed. Your history is kept.', '錯題本內的題目會全部移除，過往紀錄不受影響。'),
    ui('Clear', '清空'), () => { book.set({}); render(); }, true);
  document.querySelectorAll('#pmods .chip[data-pm]').forEach(c => {
    c.onclick = () => {
      const n = +c.dataset.pm;
      if (pmodSel.has(n) && pmodSel.size === 1) return; // keep at least one
      pmodSel.has(n) ? pmodSel.delete(n) : pmodSel.add(n);
      store.set('pmods', [...pmodSel]);
      render();
    };
  });
  const all = $('#pm-all');
  if (all) all.onclick = () => { pmodSel = new Set([1, 2, 3, 4, 5, 6, 7]); store.set('pmods', [...pmodSel]); render(); };
  document.querySelectorAll('[data-review]').forEach(b => {
    b.onclick = () => {
      const attempts = store.get(attemptsKey(), []);
      reviewAttempt = attempts[+b.dataset.review];
      justFinished = false;
      reviewFilter = 'all';
      S.view = 'results'; render();
      window.scrollTo(0, 0);
    };
  });
  const save = $('#btn-save');
  if (save) save.onclick = saveHistoryFile;
  const load = $('#btn-load'), fileIn = $('#file-load');
  if (load && fileIn) {
    load.onclick = () => fileIn.click();
    fileIn.onchange = async () => {
      const f = fileIn.files[0];
      if (!f) return;
      try {
        const r = importHistoryText(await f.text());
        homeNotice = ui(`Loaded ${esc(f.name)}: ${r.found} attempt${r.found === 1 ? '' : 's'} found, ${r.added} new added.`,
          `已載入 ${esc(f.name)}：找到${r.found}次應考紀錄，新增${r.added}次。`);
      } catch (e) {
        homeNotice = ui(`Could not read ${esc(f.name)} — it is not a history file saved by this app.`,
          `無法讀取 ${esc(f.name)}——這不是本程式儲存的紀錄檔案。`);
      }
      render();
    };
  }
  const clear = $('#btn-clear');
  if (clear) clear.onclick = () => {
    const n = store.get(attemptsKey(), []).length;
    confirmModal(
      ui('Clear all history?', '清除所有紀錄？'),
      ui(`All ${n} attempt${n === 1 ? '' : 's'} and the Progress card will be removed from this browser. This cannot be undone — save history to a file first if you may want it later.`,
         `此瀏覽器內的${n}次應考紀錄及進度卡將被刪除，且無法復原。如日後可能需要，請先將紀錄儲存至檔案。`),
      ui('Clear history', '清除紀錄'),
      () => {
        store.del(attemptsKey());
        homeNotice = ui('History cleared.', '紀錄已清除。');
        render();
      }, true);
  };
  document.querySelectorAll('.missed-head').forEach(b => {
    b.onclick = () => { const body = $('#mq-' + b.dataset.mq); if (body) body.hidden = !body.hidden; };
  });
  const weak = $('#btn-practice-weak');
  if (weak) weak.onclick = () => startPractice(stats(store.get(attemptsKey(), [])).mostMissed.map(x => x.qid));
}

/* ---------------- first-run language chooser ---------------- */

function langView() {
  return topbarHTML() + `
  <div class="wrap">
    <div class="card welcome">
      <div class="eyebrow">Customs and Excise Department · Money Service Operators</div>
      <h2>Choose your paper language<br>請選擇試卷語言</h2>
      <div class="profiles">
        <div class="profile-card" data-pick-lang="en">
          <div class="avatar">EN</div>
          <div class="name">English paper</div>
          <div class="paper">Questions, answers and explanations in English</div>
        </div>
        <div class="profile-card" data-pick-lang="tc">
          <div class="avatar">中</div>
          <div class="name">中文卷</div>
          <div class="paper">以繁體中文顯示題目、答案及解釋</div>
        </div>
      </div>
      <div class="note" style="margin-top:20px">You can switch languages, or show both (EN+中), at any time from the top bar.<br>可隨時於頂欄切換語言或同時顯示雙語（EN+中）。</div>
    </div>
  </div>`;
}

/* ---------------- exam ---------------- */

function startExam() {
  const minutes = customMinutes || CFG.minutes;
  const qids = [], perm = {};
  for (const m of MODULES) {
    const pool = shuffle([...(byMod.get(m.n) || [])]);
    for (const q of pool.slice(0, CFG.perModule)) {
      qids.push(q.id);
      perm[q.id] = drawPerm(q);
    }
  }
  exam = {
    qids, perm, answers: {}, flags: [],
    cur: 0, minutes,
    startedAt: Date.now(), endsAt: Date.now() + minutes * 60000,
  };
  warned = new Set();
  saveExam();
  S.view = 'exam'; render();
  window.scrollTo(0, 0);
}

function resumeExam() {
  const saved = loadExam();
  if (!saved) { render(); return; }
  if (Date.now() >= saved.endsAt) { exam = saved; finishExam(true); return; }
  exam = saved;
  warned = new Set();
  S.view = 'exam'; render();
  window.scrollTo(0, 0);
}

function saveExam() { if (exam) store.set(examKey(), exam); }

/* A source-scope update may retire questions. Completed results keep their
   original scores; an incomplete paper must be restarted with 35 valid items. */
function loadExam() {
  const e = store.get(examKey(), null);
  if (!e || !Array.isArray(e.qids)) return null;
  const valid = e.qids.length === CFG.total && new Set(e.qids).size === CFG.total &&
    e.qids.every(id => byId.has(id)) && MODULES.every(m =>
      e.qids.filter(id => byId.get(id).module === m.n).length === CFG.perModule);
  if (valid) return e;
  store.del(examKey());
  homeNotice = ui('The question bank has changed. Please start a new mock exam; completed results are kept.',
    '題庫已更新，請重新開始模擬試；已完成的考試成績仍會保留。');
  return null;
}

/* the drawn arrangement of an exam question (a paper saved before arrangements
   were stored has none, and is shown in the stored order) */
const examArr = qid => arrange(byId.get(qid), permFor(byId.get(qid), exam.perm && exam.perm[qid]));

function examView() {
  const q = byId.get(exam.qids[exam.cur]);
  const answered = Object.keys(exam.answers).length;
  const flagged = exam.flags.includes(q.id);
  const arr = examArr(q.id);
  const chosen = exam.answers[q.id];
  const opts = optsHTML(arr, orig => chosen === orig ? 'sel' : '');

  const n = exam.qids.length;
  const buttons = `
    <button class="btn small btn-submit">${ui('Submit paper', '交卷')}</button>
    <button class="btn small secondary btn-exit">${ui('Exit', '離開')}</button>`;

  return `
  <div class="examtop"><div class="wrap">
    <div class="timer">${icon('clock')}<span class="tval">--:--</span></div>
    <div class="grow"></div>
    <div class="prog">${ui('Answered', '已作答')} <b>${answered}</b>/${n}</div>
    ${buttons}
  </div></div>
  <div class="wrap">
    <div class="examgrid">
      <div>
        <div class="qcard">
          <div class="qmeta">
            <span class="qnum">${ui('Question', '第')} ${exam.cur + 1} / ${n}${S.lang === 'tc' ? ' 題' : ''}</span>
            <span class="qmod">M${q.module} · ${esc(modName(q.module))}</span>
            <button class="qflag ${flagged ? 'on' : ''}" id="btn-flag">${icon('flag')} ${flagged ? ui('Flagged', '已標記') : ui('Flag', '標記')}</button>
          </div>
          ${stemHTML(q, arr.perm)}
          <div class="opts" id="opts">${opts}</div>
          <div class="qnav-row">
            <button class="btn secondary" id="btn-prev" ${exam.cur === 0 ? 'disabled' : ''}>${ui('Previous', '上一題')}</button>
            <div class="grow"></div>
            ${exam.cur === n - 1
              ? `<button class="btn" id="btn-next-submit">${ui('Submit paper', '交卷')}</button>`
              : `<button class="btn" id="btn-next">${ui('Next', '下一題')}</button>`}
          </div>
        </div>
        <div class="footer kbd">${ui('Keyboard: A–E or 1–5 to answer (press again to erase) · Enter next · ←/→ move · or mark the sheet directly',
          '鍵盤：A–E 或 1–5 作答（再按一次可清除）· Enter 下一題 · ←/→ 切換 · 亦可直接在答題紙上作答')}</div>
      </div>
      <aside class="rail">
        <div class="card">
          <div class="tlabel">${ui('Time remaining', '剩餘時間')}${exam.minutes !== CFG.minutes ? ` · ${exam.minutes} min` : ''}</div>
          <div class="timer">${icon('clock')}<span class="tval">--:--</span></div>
          <div class="tprog"><i></i></div>
          <div class="meta">
            <span>${ui('Answered', '已作答')} <b>${answered}</b>/${n}</span>
            <span>${ui('Flagged', '已標記')} <b>${exam.flags.length}</b></span>
          </div>
        </div>
        <div class="railbtns">${buttons}</div>
        <div class="card">
          <div class="tlabel">${ui('Answer sheet', '答題紙')}</div>
          ${omrSheetHTML()}
          <div class="omr-legend">${ui('Mark a bubble to answer; click a number to jump.', '點選圓圈作答；點擊題號跳至該題。')}</div>
        </div>
      </aside>
    </div>
  </div>`;
}

/* the answer sheet in the rail, drawn like the machine-read sheet: one row per question, bubbles A–E */
function omrSheetHTML() {
  const groups = MODULES.map(m => {
    const rows = exam.qids.map((qid, i) => ({ qid, i, q: byId.get(qid) }))
      .filter(x => x.q.module === m.n)
      .map(x => {
        const chosen = exam.answers[x.qid];
        const bubbles = examArr(x.qid).order.map((orig, di) =>
          `<button class="bub ${chosen === orig ? 'on' : ''}" data-mark="${x.i}:${di}" title="Q${x.i + 1} ${LETTERS[di]}">${LETTERS[di]}</button>`).join('');
        const fl = `<span class="fl">${exam.flags.includes(x.qid) ? icon('flag') : ''}</span>`;   // slot always present
        return `<div class="omr-row ${x.i === exam.cur ? 'current' : ''}">
          <button class="omr-num" data-goto="${x.i}">${x.i + 1}</button>${bubbles}${fl}</div>`;
      }).join('');
    return `<div class="omr-group"><div class="omr-mod">M${m.n}</div>${rows}</div>`;
  }).join('');
  return `<div class="omr">${groups}</div>`;
}

function bindExam() {
  document.querySelectorAll('#opts .opt').forEach(b => {
    b.onclick = () => {
      const q = byId.get(exam.qids[exam.cur]);
      const orig = +b.dataset.orig;
      if (exam.answers[q.id] === orig) delete exam.answers[q.id];  // click again to erase
      else exam.answers[q.id] = orig;
      saveExam();
      rerenderExamKeepScroll();
    };
  });
  const flag = $('#btn-flag');
  if (flag) flag.onclick = () => {
    const qid = exam.qids[exam.cur];
    const i = exam.flags.indexOf(qid);
    i >= 0 ? exam.flags.splice(i, 1) : exam.flags.push(qid);
    saveExam();
    rerenderExamKeepScroll();
  };
  const prev = $('#btn-prev'); if (prev) prev.onclick = () => gotoQ(exam.cur - 1);
  const next = $('#btn-next'); if (next) next.onclick = () => gotoQ(exam.cur + 1);
  const nsub = $('#btn-next-submit'); if (nsub) nsub.onclick = () => confirmSubmit();
  document.querySelectorAll('.btn-submit').forEach(b => { b.onclick = () => confirmSubmit(); });
  document.querySelectorAll('.btn-exit').forEach(b => {
    b.onclick = () => confirmModal(
      ui('Leave the exam?', '離開模擬試？'),
      ui('Your answers are saved and you can resume from the home screen — but the clock keeps running.',
         '你的答案已儲存，可隨時從主頁繼續 — 但計時不會暫停。'),
      ui('Leave', '離開'), () => { S.view = 'home'; render(); });
  });
  document.querySelectorAll('[data-goto]').forEach(b => { b.onclick = () => gotoQ(+b.dataset.goto); });
  document.querySelectorAll('[data-mark]').forEach(b => {
    b.onclick = () => {                       // mark the sheet directly
      const [i, di] = b.dataset.mark.split(':').map(Number);
      const qid = exam.qids[i];
      // the bubbles were drawn through the question's arrangement, so read the
      // answer back the same way
      const orig = examArr(qid).order[di];
      if (exam.answers[qid] === orig) delete exam.answers[qid];
      else exam.answers[qid] = orig;
      saveExam();
      rerenderExamKeepScroll();
    };
  });
  // keep the current row visible inside the sticky rail (wide layout only)
  const cur = document.querySelector('.omr-row.current');
  if (cur && window.matchMedia('(min-width: 960px)').matches) cur.scrollIntoView({ block: 'nearest' });
  document.onkeydown = examKeys;
}

function rerenderExamKeepScroll() {
  const y = window.scrollY; render(); window.scrollTo(0, y);
}

function gotoQ(i) {
  if (i < 0 || i >= exam.qids.length) return;
  exam.cur = i; saveExam();
  render();
  window.scrollTo(0, 0);
}

function examKeys(e) {
  if (S.view !== 'exam' || $('.modal-back') || e.ctrlKey || e.metaKey || e.altKey) return;
  const k = e.key.toLowerCase();
  if (k === 'arrowleft') gotoQ(exam.cur - 1);
  else if (k === 'arrowright') gotoQ(exam.cur + 1);
  else if (k === 'enter') {
    if (e.target && e.target.tagName === 'BUTTON') return;   // a focused button already handles Enter
    if (exam.cur === exam.qids.length - 1) confirmSubmit(); else gotoQ(exam.cur + 1);
  }
  else if (k.length === 1 && ('abcde'.includes(k) || '12345'.includes(k))) {
    const di = 'abcde'.includes(k) ? 'abcde'.indexOf(k) : '12345'.indexOf(k);
    const q = byId.get(exam.qids[exam.cur]);
    const orig = examArr(q.id).order[di];
    if (exam.answers[q.id] === orig) delete exam.answers[q.id];
    else exam.answers[q.id] = orig;
    saveExam();
    rerenderExamKeepScroll();
  }
}

function confirmSubmit() {
  const un = exam.qids.map((qid, i) => exam.answers[qid] === undefined ? i + 1 : null).filter(x => x);
  const flaggedN = exam.flags.length;
  let body = ui(`All ${exam.qids.length} questions answered.`, `${exam.qids.length}題已全部作答。`);
  if (un.length) body = `<span class="warn">${ui(
    `${un.length} unanswered question${un.length > 1 ? 's' : ''}: `, `尚有${un.length}題未作答：`)}#${un.join(', #')}</span><br>` +
    ui('Unanswered questions count as wrong.', '未作答的題目作錯題計算。');
  if (flaggedN) body += `<br>${ui(`${flaggedN} flagged for review.`, `${flaggedN}題已標記待覆核。`)}`;
  const extra = un.length
    ? { label: ui('Go to first unanswered', '跳至首題未作答'), onClick: () => gotoQ(un[0] - 1) }
    : flaggedN ? { label: ui('Go to first flagged', '跳至首題已標記'), onClick: () => gotoQ(exam.qids.indexOf(exam.flags[0])) } : null;
  confirmModal(ui('Submit the paper?', '確定交卷？'), body, ui('Submit', '交卷'), () => finishExam(false), false, extra);
}

function finishExam(auto) {
  stopTimer();
  const g = grade(exam.qids, exam.answers);
  for (const qid of exam.qids) recordAnswer(qid, exam.answers[qid] === byId.get(qid).answer);
  const attempt = {
    ts: Date.now(),
    minutes: exam.minutes,
    usedMs: Math.min(Date.now() - exam.startedAt, exam.minutes * 60000),
    qids: exam.qids, perm: exam.perm, answers: exam.answers,
    score: g.score, moduleWrong: g.moduleWrong, pass: g.pass, auto: !!auto,
  };
  const attempts = store.get(attemptsKey(), []);
  attempts.push(attempt);
  store.set(attemptsKey(), attempts);
  store.del(examKey());
  exam = null;
  reviewAttempt = attempt;
  justFinished = true;
  reviewFilter = 'all';
  S.view = 'results'; render();
  window.scrollTo(0, 0);
}

/* ---------------- timer ---------------- */

let warned = new Set();   // minute marks already announced in this sitting

function startTimer() {
  if (!exam) return;
  const els = document.querySelectorAll('.timer');
  const bar = document.querySelector('.tprog i');
  if (!els.length) return;
  const tick = () => {
    if (!exam) return;
    const left = exam.endsAt - Date.now();
    if (left <= 0) { finishExam(true); return; }
    const txt = fmtTime(left);
    document.title = txt + ' · ' + BASE_TITLE;    // visible on the tab even when it is not in front
    els.forEach(el => {
      el.querySelector('.tval').textContent = txt;
      el.classList.toggle('warn', left <= 10 * 60000 && left > 5 * 60000);
      el.classList.toggle('crit', left <= 5 * 60000);
    });
    if (bar) bar.style.width = Math.min(100, 100 * (1 - left / (exam.minutes * 60000))) + '%';
    for (const m of [10, 5]) {
      if (left <= m * 60000 && !warned.has(m)) { warned.add(m); toast(ui(`${m} minutes left`, `尚餘 ${m} 分鐘`)); }
    }
  };
  tick();
  timerId = setInterval(tick, 500);
}

function stopTimer() { if (timerId) { clearInterval(timerId); timerId = null; } }

/* ---------------- results / review ---------------- */

function resultsView() {
  const a = reviewAttempt;
  const g = recordedResult(a);
  const removed = a.qids.filter(qid => !byId.has(qid)).length;
  // one row of dots per module: correct first, then wrong; the mark is the floor (at least 3 correct)
  const perMod = MODULES.map(m => {
    const total = g.moduleTotal[m.n - 1], wrong = g.moduleWrong[m.n - 1], right = total - wrong;
    const breach = wrong > CFG.maxWrongPerModule;
    const need = total - CFG.maxWrongPerModule;
    let dots = '';
    for (let i = 0; i < total; i++) {
      if (i === need) dots += '<i class="floor"></i>';
      dots += `<i class="dot ${i < right ? 'ok' : 'bad'}"></i>`;
    }
    return `<div class="dotrow ${breach ? 'breach' : ''}">
      <div class="dlabel">M${m.n} · ${esc(modName(m.n))}</div>
      <div class="dots">${dots}</div>
      <div class="dnum">${right}/${total} · ${breach
        ? `<span class="bad">${ui(`${wrong} wrong, over the limit`, `錯${wrong}題，超出上限`)}</span>`
        : `<span class="ok">${ui(`${wrong} wrong`, `錯${wrong}題`)}</span>`}</div>
    </div>`;
  }).join('');

  const whyIn = lang => {
    if (g.pass) return lang === 'en'
      ? 'Total ≥ 25/35 and every module within the 2-wrong limit.'
      : '總分達25/35，且每個單元錯題不多於2題。';
    const reasons = [];
    if (!g.totalOK) reasons.push(lang === 'en'
      ? `total ${g.score}/${a.qids.length} is below ${CFG.passTotal}`
      : `總分${g.score}/${a.qids.length}未達${CFG.passTotal}`);
    if (!g.floorsOK) {
      const bad = g.moduleWrong.map((w, i) => w > CFG.maxWrongPerModule ? `M${i + 1} (${w})` : null).filter(x => x);
      reasons.push(lang === 'en'
        ? `more than 2 wrong in ${bad.join(', ')}`
        : `${bad.join('、')}錯題多於2題`);
    }
    return (lang === 'en' ? 'Failed: ' : '不合格原因：') + reasons.join(lang === 'en' ? ' and ' : '；');
  };
  const why = S.lang === 'en' ? whyIn('en') : S.lang === 'tc' ? whyIn('tc')
    : whyIn('en') + '<br>' + whyIn('tc');

  const wrongIdx = a.qids.map((qid, i) => byId.has(qid) && a.answers[qid] !== byId.get(qid).answer ? i : -1).filter(i => i >= 0);
  const shown = i => reviewFilter === 'all' || wrongIdx.includes(i);
  const items = a.qids.map((qid, i) => byId.has(qid) ? (shown(i) ? reviewItemHTML(byId.get(qid), i, a) : '')
    : reviewFilter === 'all' ? removedItemHTML(qid, i) : '').join('');
  const nextSteps = `
    <button class="btn secondary btn-home">${ui('Back to home', '返回主頁')}</button>
    ${wrongIdx.length ? `<button class="btn btn-practice-wrong">${ui(`Practice my ${wrongIdx.length} wrong answer${wrongIdx.length === 1 ? '' : 's'}`, `練習答錯的${wrongIdx.length}題`)}</button>` : ''}`;

  return topbarHTML() + `
  <div class="wrap">
    <div class="banner ${g.pass ? 'pass' : 'fail'}">
      <div>
        <div class="verdict">${g.pass ? ui('PASS', '合格') : ui('FAIL', '不合格')}</div>
        <div class="note">${fmtDate(a.ts)}${a.auto ? ' · ' + ui('auto-submitted when time ran out', '時間屆滿自動交卷') : ''}
          · ${ui('time used', '用時')} ${fmtTime(a.usedMs)}</div>
      </div>
      <div class="score">${g.score}<small>/${a.qids.length}</small></div>
      <div class="why">${why}${removed ? '<br>' + ui(
        `${removed} question${removed === 1 ? ' in this attempt has' : 's in this attempt have'} since been removed from the question bank. The result is the one recorded when you submitted.`,
        `此次應考有${removed}題其後已從題庫刪除；以上成績為交卷時記錄的成績。`) : ''}</div>
    </div>
    <div class="actions" style="margin-top:12px">
      ${nextSteps}
      <button class="btn secondary" id="btn-save-r">${ui('Save history to file (.md)', '儲存紀錄至檔案 (.md)')}</button>
    </div>
    <div class="card">
      <h2>${ui('By module', '各單元成績')}</h2>
      <div class="sub">${ui('Correct answers first, then wrong. The mark is the floor: at least 3 correct in every module.',
        '先列答對、後列答錯。豎線代表底線：每個單元最少須答對3題。')}</div>
      <div class="dotrows">${perMod}</div>
    </div>
    <div class="card" id="review-top">
      <h2>${ui('Full review', '全卷重溫')}</h2>
      <div class="sub">${ui('Your answer is marked; the correct answer is highlighted in green. Click a number to jump.',
        '你的作答已標示；正確答案以綠色顯示。點擊題號可跳至該題。')}</div>
      <div class="chips" style="margin-bottom:12px">
        <button class="chip ${reviewFilter === 'all' ? 'on' : ''}" data-rf="all">${ui('All', '全部')} · ${a.qids.length}</button>
        <button class="chip ${reviewFilter === 'wrong' ? 'on' : ''}" data-rf="wrong">${ui('Wrong only', '只看錯題')} · ${wrongIdx.length}</button>
      </div>
      <div class="chips" id="jumpgrid">${a.qids.map((qid, i) => {
        if (!byId.has(qid) || !shown(i)) return '';
        const ok = a.answers[qid] === byId.get(qid).answer;
        return `<button class="ncell ${ok ? 'rok' : 'rbad'}" data-jump="${i}">${i + 1}</button>`;
      }).join('')}</div>
    </div>
    ${items || `<div class="card"><div class="sub" style="margin:0">${ui('No wrong answers in this attempt.', '此次應考沒有錯題。')}</div></div>`}
    <div class="actions" style="margin-top:22px">${nextSteps}</div>
  </div>`;
}

function removedItemHTML(qid, i) {
  const m = Number((/^m(\d)-/.exec(qid) || [])[1]);
  return `
  <div class="qcard review-item" id="rev-${i}">
    <div class="qmeta">
      <span class="qnum">${i + 1}.</span>
      ${m ? `<span class="qmod">M${m} · ${esc(modName(m))}</span>` : ''}
    </div>
    <div class="sub" style="margin:0">${ui('This question has since been removed from the question bank, so it can’t be shown.',
      '此題其後已從題庫刪除，因此無法顯示。')}</div>
  </div>`;
}

/* the class that marks an answered option: the key green, a wrong pick red */
const markCls = (q, chosen) => orig => orig === q.answer ? 'correct' : orig === chosen ? 'wrong' : 'dim';

function reviewItemHTML(q, i, a) {
  const chosen = a.answers[q.id];
  const arr = arrange(q, permFor(q, a.perm && a.perm[q.id]));
  const opts = optsHTML(arr, markCls(q, chosen), true);
  const state = chosen === undefined
    ? `<span class="verdict bad">${icon('x')} ${ui('Not answered', '未作答')}</span>`
    : chosen === q.answer
      ? `<span class="verdict good">${icon('check')} ${ui('Correct', '答對')}</span>`
      : `<span class="verdict bad">${icon('x')} ${ui('Incorrect', '答錯')}</span>`;
  return `
  <div class="qcard review-item" id="rev-${i}">
    <div class="qmeta">
      <span class="qnum">${i + 1}.</span>
      <span class="qmod">M${q.module} · ${esc(modName(q.module))}</span>
    </div>
    ${stemHTML(q, arr.perm, true)}
    <div class="opts">${opts}</div>
    <div class="explain">
      <div class="verdict">${state}</div>
      ${contentHTML(q, 'explain')}
      ${sourceHTML(q)}
    </div>
  </div>`;
}

function bindResults() {
  document.querySelectorAll('.btn-home').forEach(b => {
    b.onclick = () => { S.view = 'home'; reviewAttempt = null; render(); window.scrollTo(0, 0); };
  });
  document.querySelectorAll('.btn-practice-wrong').forEach(b => {
    b.onclick = () => {
      const a = reviewAttempt;
      startPractice(a.qids.filter(qid => byId.has(qid) && a.answers[qid] !== byId.get(qid).answer));
    };
  });
  document.querySelectorAll('[data-rf]').forEach(b => {
    b.onclick = () => {
      reviewFilter = b.dataset.rf;
      render();
      const top = $('#review-top');
      if (top) top.scrollIntoView({ block: 'start' });
    };
  });
  const save = $('#btn-save-r');
  if (save) save.onclick = saveHistoryFile;
  document.querySelectorAll('[data-jump]').forEach(b => {
    b.onclick = () => {
      const el = $('#rev-' + b.dataset.jump);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    };
  });
}

/* ---------------- history file & progress ---------------- */

const pad2 = n => String(n).padStart(2, '0');
function fmtDateFull(ts) {
  const d = new Date(ts);
  return `${d.getFullYear()}-${pad2(d.getMonth() + 1)}-${pad2(d.getDate())} ${pad2(d.getHours())}:${pad2(d.getMinutes())}`;
}

/* plain-text (no HTML) question text in the current language mode, for the file;
   the statements in their stored order, which is how the options are numbered */
function qStem(q) {
  const stem = S.lang === 'en' ? q.en.q : S.lang === 'tc' ? q.tc.q : q.en.q + ' ｜ ' + q.tc.q;
  const list = q.en.statements.map((en, i) => {
    const t = q.tc.statements[i];
    return `(${i + 1}) ` + (S.lang === 'en' ? en : S.lang === 'tc' ? t : en + ' ｜ ' + t);
  }).join('  ');
  return stem + '  ' + list;
}
function optText(q, i) {
  const o = q.options[i];
  return S.lang === 'en' ? optLabel(o, 'en') : S.lang === 'tc' ? optLabel(o, 'tc') : optLabel(o, 'en') + ' ｜ ' + optLabel(o, 'tc');
}

/* aggregate all attempts: accuracy per module, and questions most often missed */
function stats(attempts) {
  const perModule = MODULES.map(() => ({ correct: 0, total: 0 }));
  const seen = new Map();   // qid -> { wrong, seen }
  for (const a of attempts) {
    for (const qid of a.qids) {
      const q = byId.get(qid);
      if (!q) continue;
      const ok = a.answers[qid] === q.answer;   // unanswered counts as wrong
      const pm = perModule[q.module - 1];
      pm.total++; if (ok) pm.correct++;
      const m = seen.get(qid) || { wrong: 0, seen: 0 };
      m.seen++; if (!ok) m.wrong++;
      seen.set(qid, m);
    }
  }
  const mostMissed = [...seen.entries()].filter(([, m]) => m.wrong > 0)
    .sort((x, y) => y[1].wrong - x[1].wrong || (y[1].wrong / y[1].seen) - (x[1].wrong / x[1].seen))
    .map(([qid, m]) => ({ qid, ...m }));
  return { perModule, mostMissed };
}

/* the saved file: readable Markdown + a JSON data block the app reads back */
function historyMarkdown(attempts) {
  const L = (en, tc) => S.lang === 'en' ? en : S.lang === 'tc' ? tc : en + ' / ' + tc;
  const st = stats(attempts);
  const out = [];
  out.push(`# ${L('MSO Competence Assessment — mock exam history', '金錢服務經營者能力評核 — 模擬試紀錄')}`, '');
  out.push(`${L('Saved', '儲存時間')}: ${fmtDateFull(Date.now())} · ${L('Attempts', '應考次數')}: ${attempts.length}`, '');
  out.push(`## ${L('Performance by module (all attempts)', '各單元表現（累計）')}`, '');
  out.push(`| ${L('Module', '單元')} | ${L('Correct', '答對')} | % |`, '|---|---|---|');
  MODULES.forEach(m => {
    const s = st.perModule[m.n - 1];
    const pct = s.total ? Math.round(100 * s.correct / s.total) : 0;
    out.push(`| M${m.n} ${L(m.en, m.tc)} | ${s.correct}/${s.total} | ${pct}% |`);
  });
  if (st.mostMissed.length) {
    out.push('', `## ${L('Most-missed questions', '最常答錯的題目')}`, '');
    st.mostMissed.slice(0, 15).forEach(x => {
      const q = byId.get(x.qid);
      out.push(`- **${q.id}** (M${q.module}) — ${L('wrong', '答錯')} ${x.wrong}/${x.seen}: ${qStem(q)}`);
      out.push(`  - ${L('Correct answer', '正確答案')}: ${optText(q, q.answer)}`);
    });
  }
  [...attempts].reverse().forEach(a => {
    out.push('', `## ${fmtDateFull(a.ts)} — ${a.score}/${a.qids.length} — ${a.pass ? L('PASS', '合格') : L('FAIL', '不合格')}`, '');
    out.push(`${L('Wrong per module', '各單元錯題')}: ${a.moduleWrong.map((w, i) => `M${i + 1}: ${w}`).join(' · ')}` +
      (a.auto ? ' · ' + L('auto-submitted when time ran out', '時間屆滿自動交卷') : ''), '');
    a.qids.forEach((qid, n) => {
      const q = byId.get(qid);
      if (!q || a.answers[qid] === q.answer) return;
      const chosen = a.answers[qid];
      out.push(`- Q${n + 1} (M${q.module}, ${q.id}) ${qStem(q)}`);
      out.push(`  - ${L('Your answer', '你的答案')}: ${chosen === undefined ? L('(not answered)', '（未作答）') : optText(q, chosen)}`);
      out.push(`  - ${L('Correct answer', '正確答案')}: ${optText(q, q.answer)}`);
    });
  });
  out.push('', '---', '', `<!-- ${L('Data block: the app reads this when you load the file. Do not edit.', '資料區塊：程式載入檔案時讀取，請勿修改。')} -->`);
  out.push('```json', JSON.stringify({ app: 'mso-ca', version: 1, attempts }, null, 1), '```', '');
  return out.join('\n');
}

function downloadText(text, filename, type) {
  const link = document.createElement('a');
  link.href = URL.createObjectURL(new Blob([text], { type }));
  link.download = filename;
  document.body.appendChild(link); link.click(); link.remove();
  setTimeout(() => URL.revokeObjectURL(link.href), 5000);
}

function saveHistoryFile() {
  downloadText(historyMarkdown(store.get(attemptsKey(), [])),
    'mso-ca-history-' + new Date().toISOString().slice(0, 10) + '.md', 'text/markdown');
}

/* merge attempts from a saved file (.md with data block, or plain .json); returns counts */
function importHistoryText(text) {
  let raw = text.trim();
  const fence = raw.match(/```json\s*([\s\S]*?)```/);
  if (fence) raw = fence[1];
  const data = JSON.parse(raw);
  const list = Array.isArray(data) ? data : data && data.attempts;
  if (!Array.isArray(list)) throw new Error('no attempts');
  // an attempt may name questions this edition no longer has; the views skip those, so keep it
  const valid = list.filter(a => a && typeof a.ts === 'number' && Array.isArray(a.qids) && a.answers
    && typeof a.score === 'number' && Array.isArray(a.moduleWrong));
  const existing = store.get(attemptsKey(), []);
  const have = new Set(existing.map(a => a.ts));
  const added = valid.filter(a => !have.has(a.ts));
  store.set(attemptsKey(), existing.concat(added).sort((x, y) => x.ts - y.ts));
  return { found: valid.length, added: added.length };
}

/* a question with its correct answer and explanation (no attempt context) */
function explainCardHTML(q) {
  const arr = arrange(q, identityPerm(q));
  return `${stemHTML(q, arr.perm, true)}
    <div class="opts">${optsHTML(arr, orig => orig === q.answer ? 'correct' : 'dim', true)}</div>
    <div class="explain">${contentHTML(q, 'explain')}${sourceHTML(q)}</div>`;
}

/* score per attempt, with the pass mark as a dashed line; inline SVG, no library */
function sparklineSVG(attempts) {
  if (attempts.length < 2) return '';
  const W = 1000, H = 72, px = 12, py = 10, T = CFG.total;
  const xs = i => (px + i * (W - 2 * px) / (attempts.length - 1)).toFixed(1);
  const ys = s => (H - py - (s / T) * (H - 2 * py)).toFixed(1);
  const pts = attempts.map((a, i) => `${xs(i)},${ys(a.score)}`).join(' ');
  const dots = attempts.map((a, i) =>
    `<circle class="pt ${a.pass ? 'pass' : 'fail'}" cx="${xs(i)}" cy="${ys(a.score)}" r="5"><title>${fmtDate(a.ts)} · ${a.score}/${a.qids.length}</title></circle>`).join('');
  const passY = ys(CFG.passTotal);
  return `<svg class="spark" viewBox="0 0 ${W} ${H}" preserveAspectRatio="xMinYMid meet">
    <line class="pass-line" x1="${px}" x2="${W - px}" y1="${passY}" y2="${passY}"/>
    <text x="${W - px}" y="${passY - 4}" text-anchor="end">${CFG.passTotal}/${T}</text>
    <polyline class="line" points="${pts}"/>${dots}</svg>`;
}

function progressCardHTML(attempts) {
  const st = stats(attempts);
  const rows = MODULES.map(m => {
    const s = st.perModule[m.n - 1];
    const pct = s.total ? Math.round(100 * s.correct / s.total) : 0;
    const cls = pct < 60 ? 'bad' : pct < 80 ? 'mid' : 'good';
    return `<div class="prow">
      <div class="plabel">M${m.n} · ${esc(modName(m.n))}</div>
      <div class="pbar"><i class="${cls}" style="width:${pct}%"></i></div>
      <div class="pnum">${s.correct}/${s.total} · <b>${pct}%</b></div>
    </div>`;
  }).join('');
  const missed = st.mostMissed.slice(0, 10).map(x => {
    const q = byId.get(x.qid);
    return `<div class="missed">
      <button class="missed-head" data-mq="${q.id}">
        <span class="qmod">M${q.module}</span>
        <span class="mstem">${contentHTML(q, 'q')}</span>
        <span class="tag fail">${ui('wrong', '答錯')} ${x.wrong}/${x.seen}</span>
      </button>
      <div class="missed-body" id="mq-${q.id}" hidden>${explainCardHTML(q)}</div>
    </div>`;
  }).join('');
  const n = attempts.length, k = st.mostMissed.length;
  return `<div class="card">
    <h2>${ui('Progress', '進度')}</h2>
    <div class="sub">${ui(`Across ${n} attempt${n === 1 ? '' : 's'}. A module under 60% is on course to breach the 2-wrong floor.`,
      `累計${n}次應考。單元答對率低於60%，即有機會超出每單元錯2題的上限。`)}</div>
    ${sparklineSVG(attempts)}
    ${n >= 2 ? `<div class="note">${ui('Score per attempt, oldest to newest; the dashed line is the pass mark.', '每次應考的分數（由舊至新）；虛線為及格分數。')}</div>` : ''}
    <h3 class="subhead">${ui('Accuracy by module', '各單元答對率')}</h3>
    <div class="pgrid">${rows}</div>
    ${k ? `<h3 class="subhead">${ui('Most-missed questions', '最常答錯的題目')} · ${ui('click to see the answer', '點擊查看答案')}</h3>
    <div class="missed-list">${missed}</div>
    <div class="actions">
      <button class="btn" id="btn-practice-weak">${ui('Practice these questions', '練習這些題目')}</button>
      <span class="note">${ui(`${k} question${k === 1 ? '' : 's'} missed at least once`, `共${k}題曾答錯`)}</span>
    </div>` : `<div class="note" style="margin-top:12px">${ui('No mistakes so far.', '暫未有錯題。')}</div>`}
  </div>`;
}

/* ---------------- practice ---------------- */

function startPractice(customPool = null) {
  const seen = seenIds(), ids = bank.filter(inPractice).map(q => q.id);
  // unseen questions first, then the rest; each group shuffled
  const pool = customPool ? customPool.slice()
    : shuffle(ids.filter(id => !seen.has(id))).concat(shuffle(ids.filter(id => seen.has(id))));
  if (!pool.length) { toast(ui('No questions in the chosen modules', '所選單元沒有題目')); return; }
  practice = {
    pool, idx: 0,
    perm: null, chosen: null,
    tally: { seen: 0, right: 0 },
  };
  nextPracticeQ(false);
  S.view = 'practice'; render();
  window.scrollTo(0, 0);
}

function nextPracticeQ(advance = true) {
  if (advance) practice.idx++;
  if (practice.idx >= practice.pool.length) {   // recycle, reshuffled
    shuffle(practice.pool);
    practice.idx = 0;
    toast(ui(`All ${practice.pool.length} questions seen once — starting another round`,
      `已完成全部 ${practice.pool.length} 題，重新開始一輪`));
  }
  practice.perm = drawPerm(byId.get(practice.pool[practice.idx]));
  practice.chosen = null;
}

function answerPractice(orig) {
  if (practice.chosen !== null) return;
  const q = byId.get(practice.pool[practice.idx]);
  practice.chosen = orig;
  practice.tally.seen++;
  const ok = orig === q.answer;
  if (ok) practice.tally.right++;
  recordAnswer(q.id, ok);
}

function practiceView() {
  const q = byId.get(practice.pool[practice.idx]);
  const done = practice.chosen !== null;
  const arr = arrange(q, practice.perm);
  const opts = optsHTML(arr, done ? markCls(q, practice.chosen) : () => '', done);

  const t = practice.tally;
  return topbarHTML() + `
  <div class="wrap">
    <div class="qcard">
      <div class="qmeta">
        <span class="qnum">${ui('Practice', '練習')}</span>
        <span class="qmod">M${q.module} · ${esc(modName(q.module))}${q.id in book.get() ? ' · ' + ui('in the book', '錯題本') : ''}</span>
        <span class="tally" style="margin-left:auto">${ui('This session', '本節')}: <b>${t.right}</b>/${t.seen}</span>
      </div>
      ${stemHTML(q, arr.perm, done)}
      <div class="opts" id="opts">${opts}</div>
      ${done ? `
      <div class="explain">
        <div class="verdict ${practice.chosen === q.answer ? 'good' : 'bad'}">
          ${practice.chosen === q.answer ? icon('check') + ' ' + ui('Correct', '答對') : icon('x') + ' ' + ui('Incorrect', '答錯')}</div>
        ${contentHTML(q, 'explain')}
        ${sourceHTML(q)}
      </div>
      <div class="qnav-row">
        <div class="grow"></div>
        <button class="btn" id="btn-pnext">${ui('Next question', '下一題')}</button>
      </div>` : ''}
    </div>
    <div class="actions">
      <button class="btn secondary" id="btn-pend">${ui('End practice', '結束練習')}</button>
    </div>
  </div>`;
}

function bindPractice() {
  document.querySelectorAll('#opts .opt:not([disabled])').forEach(b => {
    b.onclick = () => { answerPractice(+b.dataset.orig); render(); };
  });
  const nx = $('#btn-pnext');
  if (nx) nx.onclick = () => { nextPracticeQ(); render(); window.scrollTo(0, 0); };
  $('#btn-pend').onclick = () => { practice = null; S.view = 'home'; render(); };
  document.onkeydown = e => {
    if (S.view !== 'practice' || $('.modal-back') || e.ctrlKey || e.metaKey || e.altKey) return;
    const k = e.key.toLowerCase();
    if (practice.chosen === null && k.length === 1 && ('abcde'.includes(k) || '12345'.includes(k))) {
      const di = 'abcde'.includes(k) ? 'abcde'.indexOf(k) : '12345'.indexOf(k);
      const el = document.querySelectorAll('#opts .opt')[di];
      if (el) el.click();
    } else if (practice.chosen !== null && (k === 'arrowright' || (k === 'enter' && e.target.tagName !== 'BUTTON'))) {
      nextPracticeQ(); render(); window.scrollTo(0, 0);
    }
  };
}

/* ---------------- modal ---------------- */

function confirmModal(title, bodyHTML, okLabel, onOK, danger = false, extra = null) {
  const back = document.createElement('div');
  back.className = 'modal-back';
  back.innerHTML = `<div class="modal">
    <h3>${title}</h3>
    <p>${bodyHTML}</p>
    <div class="actions">
      ${extra ? `<button class="btn secondary" id="m-extra">${extra.label}</button>` : ''}
      <button class="btn secondary" id="m-cancel">${ui('Cancel', '取消')}</button>
      <button class="btn ${danger ? 'danger' : ''}" id="m-ok">${okLabel}</button>
    </div>
  </div>`;
  document.body.appendChild(back);
  back.querySelector('#m-cancel').onclick = () => back.remove();
  back.onclick = e => { if (e.target === back) back.remove(); };
  back.querySelector('#m-ok').onclick = () => { back.remove(); onOK(); };
  if (extra) back.querySelector('#m-extra').onclick = () => { back.remove(); extra.onClick(); };
  back.querySelector('#m-ok').focus();
}

/* ---------------- boot ---------------- */

async function boot() {
  try {
    if (Array.isArray(window.BANK)) {
      bank = window.BANK;                       // single-file build: bank embedded in the page
    } else {
      const res = await fetch('questions.json');
      bank = await res.json();
    }
  } catch (e) {
    $('#app').innerHTML = `<div class="loading">Failed to load questions.json 題庫載入失敗</div>`;
    return;
  }
  for (const q of bank) {
    byId.set(q.id, q);
    if (!byMod.has(q.module)) byMod.set(q.module, []);
    byMod.get(q.module).push(q);
  }

  S.lang = store.get('lang', null);
  S.theme = ['auto', 'light', 'dark'].includes(store.get('theme', 'auto')) ? store.get('theme', 'auto') : 'auto';
  applyTheme();
  store.del('examcombo');   // the exam-realistic switch is gone: every paper is in the real format
  store.del('newonly');     // every item now has per-statement notes
  const savedSel = store.get('pmods', null);
  const validSel = Array.isArray(savedSel) ? savedSel.filter(n => Number.isInteger(n) && n >= 1 && n <= 7) : [];
  if (validSel.length) pmodSel = new Set(validSel);
  const linkedPart = Number(qs.get('part'));
  if (Number.isInteger(linkedPart) && linkedPart >= 1 && linkedPart <= 7) pmodSel = new Set([linkedPart]);
  if (['tc','en','both'].includes(qs.get('lang'))) S.lang = qs.get('lang');

  // an exam that expired while the app was closed → submit it now
  const saved = loadExam();
  if (saved && Date.now() >= saved.endsAt) {
    exam = saved;
    finishExam(true);
    return;
  }
  render();
}

/* first-run language choice (delegated) */
document.addEventListener('click', e => {
  const card = e.target.closest('[data-pick-lang]');
  if (!card) return;
  S.lang = card.dataset.pickLang;
  store.set('lang', S.lang);
  render();
});

boot();
