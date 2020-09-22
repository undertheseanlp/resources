from os import listdir
from underthesea import word_tokenize

class Corpus:
    def __init__(self, docs=None):
        self.docs = docs

    @staticmethod
    def load_from_folder(folder):
        docs = {}
        doc_files = listdir(folder)
        for doc_file in doc_files:
            doc_id = doc_file[:-4]
            file = f"data/docs/{doc_file}"
            doc = Doc.load_from_file(doc_id, file)
            docs[doc_id] = doc
        corpus = Corpus(docs)
        return corpus

    @staticmethod
    def load_from_conllu_file(conllu_file):
        corpus = Corpus()
        return corpus

    def auto_tags(self):
        for doc_id in self.docs:
            self.docs[doc_id].auto_tags()


class Doc:
    def __init__(self, id=None, sentences=None):
        self.id = id
        self.sentences = sentences

    @staticmethod
    def load_from_file(doc_id=None, doc_file=None):
        lines = open(doc_file).read().splitlines()
        texts = [line for line in lines if not line.startswith("#")]
        ids = [f"{doc_id}-{str(i+1)}" for i in range(len(texts))]
        sentences = {}
        for id, text in zip(ids, texts):
            sentences[id] = Sentence(id=id, text=text)
        doc = Doc(id=doc_id, sentences=sentences)
        return doc

    def auto_tags(self):
        for sent_id in self.sentences:
            self.sentences[sent_id].auto_tags()


class Sentence:
    def __init__(self, id=None, text=None):
        self.id = id
        self.text = text
        self.tokens = None

    def auto_tags(self):
        self.tokens = word_tokenize(self.text)
