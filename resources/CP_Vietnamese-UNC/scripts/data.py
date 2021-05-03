from os import listdir
from os.path import join, dirname

ROOT_FOLDER = dirname(dirname(__file__))


class TextCorpus:
    def __init__(self):
        self.files = None

    @staticmethod
    def load(corpus_folder):
        print(corpus_folder)
        files = listdir(corpus_folder)
        files = [join(corpus_folder, _) for _ in files]
        corpus = TextCorpus()
        corpus.files = files
        return corpus

    def save(self, corpus_folder):
        pass
