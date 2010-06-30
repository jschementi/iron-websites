# Copyright (c) 2006 by Seo Sanghyeon

# 2006-07-13 sanxiyn Created
# 2006-07-19 sanxiyn Added unidata_version, normalize

unidata_version = '3.2.0'

# --------------------------------------------------------------------
# Normalization

from System import String
from System.Text import NormalizationForm

def normalize(form, string):
    return String.Normalize(string, _form_mapping[form])

_form_mapping = {
    'NFC': NormalizationForm.FormC,
    'NFKC': NormalizationForm.FormKC,
    'NFD': NormalizationForm.FormD,
    'NFKD': NormalizationForm.FormKD,
}

# --------------------------------------------------------------------
# Character properties

from System.Globalization import CharUnicodeInfo

def _handle_default(function):
    def wrapper(unichr, default=None):
        result = function(unichr)
        if result != -1:
            return result
        if default is None:
            raise ValueError()
        return default
    return wrapper

decimal = _handle_default(CharUnicodeInfo.GetDecimalDigitValue)
digit = _handle_default(CharUnicodeInfo.GetDigitValue)
numeric = _handle_default(CharUnicodeInfo.GetNumericValue)

def category(unichr):
    uc = CharUnicodeInfo.GetUnicodeCategory(unichr)
    return _category_mapping[int(uc)]

_category_mapping = {
    0: 'Lu',
    1: 'Ll',
    2: 'Lt',
    3: 'Lm',
    4: 'Lo',
    5: 'Mn',
    6: 'Mc',
    7: 'Me',
    8: 'Nd',
    9: 'Nl',
    10: 'No',
    11: 'Zs',
    12: 'Zl',
    13: 'Zp',
    14: 'Cc',
    15: 'Cf',
    16: 'Cs',
    17: 'Co',
    18: 'Pc',
    19: 'Pd',
    20: 'Ps',
    21: 'Pe',
    22: 'Pi',
    23: 'Pf',
    24: 'Po',
    25: 'Sm',
    26: 'Sc',
    27: 'Sk',
    28: 'So',
    29: 'Cn',
}
