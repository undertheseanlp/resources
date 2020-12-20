from os.path import dirname, join
import joblib

from data import Dictionary, Word

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
    'S': 'NOUN'  # khối
}
TEMP_IGNORE_POS = set([
    'R',  # phụ từ tiếng Việt
    'X',  # không phân loại
    'Z',  # yếu tố cấu tạo từ
    'D',  # không có định nghĩa (ví dụ: chút ít)
    'O',  # úi chà
])

dict = Dictionary()
pos_count = {}
data = joblib.load(UTS_DICT_DATA)
count = 0
for key in data:
    defs = []
    pos_tags = {}
    text = key
    for definition in data[key]:
        pos_tag = definition['pos']
        if pos_tag not in pos_tags:
            i = len(pos_tags)
            pos_tags[pos_tag] = i
            tag_data = {'tag': pos_tag, 'defs': []}
            defs.append(tag_data)
        index = pos_tags[pos_tag]
        defs[index]["defs"].append({
            "def": definition['definition'],
            'examples': [
                definition['example']
            ]
        })
    word = Word(text, defs)
    dict.add(word)

dict.save('underthesea_dictionary.yaml')
print('[+] Done')
