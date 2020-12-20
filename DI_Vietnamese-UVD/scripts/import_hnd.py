from os.path import dirname, join
import json
from data import Dictionary

CORPUS_FOLDER = dirname(dirname(__file__))
HND_FOLDER = join(CORPUS_FOLDER, "data", "dictionaries", "hongocduc")
with open(join(HND_FOLDER, "words.txt")) as f:
    lines = f.read().splitlines()
for line in lines:
    open(line)
Dictionary.hi()
