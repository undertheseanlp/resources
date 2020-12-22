import sys
from os import listdir
from os.path import dirname, join, isdir, realpath

from termcolor import colored


def exit(message):
    print(colored(message, 'red'))
    sys.exit(0)


def validate_corpus_folder(f):
    # each corpus folder should has VERSION file
    print(f"[ ] Validate resource {f}")
    files = listdir(f)
    if "VERSION" not in files:
        exit("[ERROR] Resource must has VERSION file")
    print(f"[✓] Validate resource {f}: Success\n")


FOLDER = dirname(realpath(__file__))
folders = [f for f in listdir(FOLDER) if isdir(join(FOLDER, f))]
ignore_folders = ["tools", "app", "docs", ".git", "data", "tmp", ".idea", "extras"]
corpus_folders = [f for f in folders if f not in ignore_folders]
for f in corpus_folders:
    validate_corpus_folder(f)
