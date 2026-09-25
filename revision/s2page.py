# The Schedule 2 page: its sections come from modules (bl_sec1, bl_sec2, s2x, s2appx and
# the figures in bl_figs and bl_figs2); this module puts them in page order.
from bl_sec1 import S1, S2, S3, S4
from bl_sec2 import S5, S6, S7, S8
from s2x import THR, MON, TRN, REC, SYS
from s2appx import APX

S2_NAV = [('map', 'Decision map', '決策圖'), ('thresholds', 'Thresholds', '門檻'), ('measures', 'Four measures', '四項措施'),
          ('bo', 'Beneficial owner', '實益擁有人'), ('docs', 'Identity documents', '身分證明文件'), ('timing', 'Timing', '時間'), ('monitoring', 'Ongoing monitoring', '持續監察'),
          ('sdd-edd', 'SDD vs EDD', '簡化與更嚴格'), ('pep', 'PEPs', '政治人物'), ('nfp', 'Not present', '沒有現身'),
          ('rely', 'Intermediaries', '中介人'), ('transfers', 'Transfers and remittances', '轉帳與匯款'),
          ('records', 'Record keeping', '備存紀錄'), ('systems', 'Procedures and branches', '程序與分行')]
S2_BODY = S1 + THR + S2 + S3 + APX + S4 + MON + S5 + S6 + S7 + S8 + TRN + REC + SYS
