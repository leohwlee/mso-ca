"""A final concept-gap prompt checked back against the bilingual original glossary."""
from pathlib import Path
exec(compile((Path(__file__).with_name('edit_guideline.py')).read_text(encoding='utf-8').split('\ndef ml(s):')[0],__file__,'exec'))
def glossary(s):
    s['blocks'].append(block('用語邊界：指引中的金融機構','Terminology boundary: financial institutions in the Guideline',[
        ('第03份的用語一般沿用AMLO涵義；詞彙表特別說明，FI（Financial Institution，金融機構）除另有指明外，採FATF建議的定義。寫明「AMLO所界定的金融機構」時，才用該法定範圍。不能把指引所有FI字眼都直接當成同一份香港機構牌照清單；本地電傳、合資格中介人及SDD各有具體定義／條件，見Part 3及Part 6。','Terms in document 03 generally follow AMLO meanings. Its glossary specifically says FI (Financial Institution) follows the FATF Recommendations unless otherwise specified, for example “an FI as defined in the AMLO”. Do not read every FI reference as the same list of Hong Kong licensed institutions. Domestic wires, eligible intermediaries and SDD have their own specified definitions/conditions in Parts 3 and 6.'),
    ],[ref('03','第1.2段及「主要用語及縮寫詞彙」金融機構條目','¶1.2 and Glossary, Financial institution(s)','unless specified otherwise')]))
write_sections(1,{'legal-framework':glossary})
