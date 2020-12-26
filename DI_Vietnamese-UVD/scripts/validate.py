import yaml
from os.path import join, basename, dirname

from termcolor import colored

total_errors = 0
SCRIPTS_FOLDER = dirname(__file__)
DICT_FOLDER = join(dirname(SCRIPTS_FOLDER), 'dictionary')


def warn(file, line_number, message, type=None):
    global total_errors
    text = ""
    if type:
        text = f"[{type}] "
    text += basename(file) + ":" + str(line_number)
    print(colored(text, 'red'), colored(message, 'red'))

    total_errors += 1


MIN_WORDS_IN_DICT = 3000

# dictionary_file = join(DATA_FOLDER, "underthesea_dictionary.yaml")
dictionary_file = join(DICT_FOLDER, "data.yaml")
# validate
with open(dictionary_file) as f:
    data = yaml.safe_load(f)
    num_words = len(data)
    if num_words < MIN_WORDS_IN_DICT:
        warn('DICT', '', f'Dictionary must has at least {MIN_WORDS_IN_DICT} words (found {num_words})')

if total_errors > 0:
    print(colored(f"\n[x] BUILD ERRORS: {total_errors} errors", 'red'))
else:
    print(f"\n[+] BUILD SUCCESS")


def stats():
    print("\n# DICTIONARY STATISTICS")
    global num_words
    print("Number words:", num_words)


stats()
