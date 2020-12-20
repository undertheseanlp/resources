from os.path import dirname, join
import joblib

CORPUS_FOLDER = dirname(dirname(__file__))
UTS_DICT_DATA = join(CORPUS_FOLDER, "data", "underthesea_dictionary.data")

KNOWN_POS = {
    'V': 'VERB',
    'N': 'NOUN',
    'A': 'ADJ',
    'P': 'PROPN',
    'C': 'CCONJ',
    'I': 'INTJ',
    'E': 'ADP',
    'M': 'NOUN',  # số từ
    'n': 'NOUN',
    'S': 'NOUN'   # khối
}
TEMP_IGNORE_POS = set([
    'R',  # phụ từ tiếng Việt
    'X',   # không phân loại
    'Z',   # yếu tố cấu tạo từ
    'D',    # không có định nghĩa (ví dụ: chút ít)
    'O',     # úi chà
])

pos_count = {}
data = joblib.load(UTS_DICT_DATA)
for key in data:
    for definition in data[key]:
        p = definition['pos']
        if p not in KNOWN_POS and p not in TEMP_IGNORE_POS:
            print(key)
            print(definition)
            exit(0)
        if p not in pos_count:
            pos_count[p] = 0
        pos_count[p] += 1

print(pos_count)
