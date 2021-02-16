import yaml
from os.path import join, basename, dirname
import joblib
from termcolor import colored

total_errors = 0
SCRIPTS_FOLDER = dirname(__file__)
DICT_FOLDER = join(dirname(SCRIPTS_FOLDER), 'corpus')
MAX_SHOW_ERRORS = 100

def warn(file, line_number, message, type=None):
    global total_errors
    text = ""
    if type:
        text = f"[{type}] "
    text += basename(file) + ":" + str(line_number)
    if total_errors < MAX_SHOW_ERRORS:
        print(colored(text, 'red'), colored(message, 'red'))

    total_errors += 1


MIN_WORDS_IN_DICT = 3000

# load file
dictionary_file = join(DICT_FOLDER, "data.yaml")
tmp_file = join(DICT_FOLDER, 'tmp.bin')
RELOAD = False
if RELOAD:
    with open(dictionary_file) as f:
        data = yaml.safe_load(f)
    joblib.dump(data, tmp_file)
else:
    data = joblib.load(tmp_file)

# validate
NUM_WORDS = 0
VALID_TAGS = {'noun'}


def validate_num_words(data):
    global NUM_WORDS
    NUM_WORDS = len(data)
    if NUM_WORDS < MIN_WORDS_IN_DICT:
        warn('DICT', '', f'Dictionary must has at least {MIN_WORDS_IN_DICT} words (found {NUM_WORDS})')


def validate_tags(data):
    for word in data:
        nodes = data[word]
        for node in nodes:
            tag = node['tag']
            if tag not in VALID_TAGS:
                warn('DICT', word, f'Tag {tag} is not valid')


validate_num_words(data)
validate_tags(data)

if total_errors > 0:
    print(colored(f"\n[x] BUILD ERRORS: {total_errors} errors", 'red'))
else:
    print(f"\n[+] BUILD SUCCESS")


def stats():
    print("\n# DICTIONARY STATISTICS")
    global NUM_WORDS
    print("Number words:", NUM_WORDS)


stats()
