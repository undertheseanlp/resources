from os.path import join, dirname

import joblib
import yaml

SCRIPTS_FOLDER = dirname(__file__)
DICT_FOLDER = join(dirname(SCRIPTS_FOLDER), 'corpus')
tmp_in_file = join(DICT_FOLDER, 'tmp_data.bin')
yaml_out_file = join(DICT_FOLDER, 'data_correct.yaml')
bin_out_file = join(DICT_FOLDER, 'tmp_data_correct.bin')

data = joblib.load(tmp_in_file)


def tag_correct(data):
    correct_data = data
    TAG_MAP = {
        'N': 'noun',
        'A': 'adjective',
        'V': 'verb',
        'P': 'pronoun',
        'M': 'numeral'

    }
    for word in data:
        for i, node in enumerate(data[word]):
            tag = node['tag']
            if tag in TAG_MAP:
                correct_data[word][i]['tag'] = TAG_MAP[tag]
    return correct_data


correct_data = tag_correct(data)
with open(yaml_out_file, 'w') as f:
    yaml.dump(correct_data, f, allow_unicode=True)
joblib.dump(correct_data, bin_out_file)
