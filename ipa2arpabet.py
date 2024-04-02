import sys

ipa_arpabet_pairs = {
    'ə': 'AX',
    'ɚ': 'AXR',
    'ɑ': 'AA',
    'æ': 'AE',
    'ʌ': 'AH',
    'ɔ': 'AO',
    'aʊ': 'AW',
    'aɪ': 'AY',
    'ɛ': 'EH',
    'ɝ': 'ER',
    'eɪ': 'EY',
    'ɪ': 'IH',
    'i': 'IY',
    'oʊ': 'OW',
    'ɔɪ': 'OY',
    'ʊ': 'UH',
    'u': 'UW',
    'b': 'B',
    'tʃ': 'CH',
    'd': 'D',
    'ð': 'DH',
    'f': 'F',
    'g': 'G',
    'h': 'HH',
    'dʒ': 'JH',
    'k': 'K',
    'l': 'L',
    'm': 'M',
    'm̩': 'EM',
    'n': 'N',
    'n̩': 'EN',
    'ŋ': 'NG',
    'p': 'P',
    'ɹ': 'R',
    'ɾ': 'DX',
    's': 'S',
    'ʃ': 'SH',
    't': 'T',
    'θ': 'TH',
    'v': 'V',
    'w': 'W',
    'j': 'Y',
    'z': 'Z',
    'ʒ': 'ZH'
}
#total number of entries
n = len(sys.argv)

arpabet_spellings = []

def convert_to_arpabet(ipa):
    arpabet = ""
    i = 0
    while i < len(ipa):
        if ipa[i:i+2] in ['aʊ', 'oʊ', 'aɪ', 'eɪ', 'ɔɪ', 'tʃ', 'dʒ']:
            arpabet += ipa_arpabet_pairs[ipa[i:i+2]]
            i += 2
        elif ipa[i] in list(ipa_arpabet_pairs.keys()):
            arpabet += ipa_arpabet_pairs[ipa[i]]
            i += 1
        else:
            i += 1

    return arpabet

for i in range(1, n):
    arpabet_spellings.append(convert_to_arpabet(sys.argv[i]))

for spelling in arpabet_spellings:
    print(spelling)