"""Study tier for every manuscript block, in block order (depth-review-2026-10-20 tiers).

M = remember, U = understand, R = recognise, F = reference. A block title that already
starts with a tier word must agree with its letter; build.py checks both.
"""

TIERS = {
    1: {'money-laundering': 'MUU', 'terrorist-financing': 'MU', 'legal-framework': 'MMFU', 'international': 'MU',
        'risk-assessment': 'UFUUURRRF', 'sanctions': 'MUUMUF', 'cross-boundary-cash': 'MMRMRUF'},
    2: {'statutory-map': 'UMR', 'criminal-liability': 'MMF', 'inspection-investigation': 'MURF', 'licence-scope': 'MM',
        'grant-renewal': 'MMRU', 'changes': 'M', 'discipline': 'MR', 'enforcement': 'U', 'review': 'MM',
        'statutory-administration': 'UFF', 'other-sector-regimes': 'FFFFFFF'},
    3: {'definitions': 'MMMUU', 'core-duties': 'RM', 'simplification': 'M', 'special-cases': 'MR', 'sector-specific': 'FFF',
        'ongoing-and-records': 'M', 'fees': 'MU', 'tribunal-schedule': 'RF'},
    4: {'premises': 'MU', 'application': 'URUM', 'fitness': 'MMR', 'assessment': 'MRUMUF', 'licensing-actions': 'MUMMM',
        'penalty-factors': 'MR', 'exchange-note': 'MR', 'exchange-display': 'MU'},
    5: {'risk-based': 'MU', 'institutional-assessment': 'MM', 'customer-assessment': 'MU', 'new-business': 'M',
        'control-framework': 'M', 'roles': 'MMMU', 'group-controls': 'MUU', 'business-plan': 'R', 'policy': 'U'},
    6: {'cdd': 'MU', 'triggers': 'MM', 'identity': 'MMUUM', 'identity-evidence': 'MMU', 'beneficial-owners': 'MUUURU',
        'representatives': 'MUM', 'timing': 'MMU', 'simplified': 'MMMURM', 'enhanced': 'MMUURUU', 'peps': 'MMU',
        'remote': 'MU', 'intermediaries': 'MMRRM', 'monitoring': 'MMMR', 'screening': 'MMU', 'third-party-payments': 'MRM',
        'delivery': 'U', 'wire-transfers': 'MMUU', 'wire-receiving': 'MM', 'remittances': 'MMU',
        'trade-based-laundering': 'MRRURRRR', 'suspicion-indicators': 'URRRRRR'},
    7: {'reporting-duty': 'MU', 'internal-report': 'MUUM', 'tipping-off': 'M', 'after-report': 'M', 'evidence-records': 'M',
        'retention': 'MM', 'independent-audit': 'MU', 'training': 'MMU', 'law-enforcement': 'UF', 'periodic-return': 'MM',
        'safe': 'M'},
}

LABELS = {
    'M': {'tc': '必記', 'en': 'Remember'},
    'U': {'tc': '理解', 'en': 'Understand'},
    'R': {'tc': '認識', 'en': 'Recognise'},
    'F': {'tc': '參考', 'en': 'Reference'},
}

# Title prefixes that already state a tier; the chip replaces them on the page.
PREFIXES = {
    'M': {'tc': ('須記住：', '記憶：'), 'en': ('Remember: ',)},
    'U': {'tc': ('理解：',), 'en': ('Understand: ',)},
    'R': {'tc': ('須認識：', '認識：'), 'en': ('Recognise: ',)},
    'F': {'tc': ('參考：',), 'en': ('Reference: ',)},
}
