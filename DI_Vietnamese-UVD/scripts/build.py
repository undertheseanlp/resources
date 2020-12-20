import yaml
import os
from os.path import join, basename

from termcolor import colored

total_erros = 0
SCRIPTS_FOLDER = os.path.dirname(__file__)
DATA_FOLDER = join(os.path.dirname(SCRIPTS_FOLDER), "data")


def warn(file, line_number, message, type=None):
    global total_erros
    text = ""
    if type:
        text = f"[{type}] "
    text += basename(file) + ":" + str(line_number)
    print(colored(text, 'red'), colored(message, 'red'))

    total_erros += 1


MIN_WORDS_IN_DICT = 3000

dictionary_file = join(DATA_FOLDER, "underthesea_dictionary.yaml")
# dictionary_file = join(DATA_FOLDER, "data.yaml")
# validate
with open(dictionary_file) as f:
    data = yaml.safe_load(f)
    num_words = len(data)
    if num_words < MIN_WORDS_IN_DICT:
        warn('DICT', '', f'Dictionary must has at least {MIN_WORDS_IN_DICT} words (found {num_words})')

if total_erros > 0:
    print(colored(f"\n[x] BUILD ERRORS: {total_erros} errors", 'red'))
else:
    print(f"\n[+] BUILD SUCCESS")


def stats():
    print("\n# DICTIONARY STATISTICS")
    global num_words
    print("Number words:", num_words)


stats()
