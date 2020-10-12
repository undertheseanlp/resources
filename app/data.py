from os import listdir
from underthesea import word_tokenize


class Corpus:
    def __init__(self, docs=None):
        self.docs = docs
        self.sentences = None
        if self.docs is not None:
            self.sentences = {}
            for doc_id, doc in self.docs.items():
                self.sentences.update(doc.sentences)

    def is_exist(self, sent_id=None, doc_id=None):
        if sent_id is None and doc_id is None:
            raise Exception("sent_id or doc_id must be not None")

        if self.docs is None:
            return False

        if doc_id is not None:
            return doc_id in self.docs.keys()

        return sent_id in self.sentences.keys()

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
    def load_from_conllu_file(conll_file):
        return CONLLCorpus.load_from_file(conll_file)

    def auto_tags(self):
        for doc_id in self.docs:
            self.docs[doc_id].auto_tags()

    def save_conllu(self, file, **kwargs):
        content = "".join([doc.to_conllu(**kwargs) for id, doc in self.docs.items()])
        with open(file, "w") as f:
            f.write(content)
        print(f"Corpus is saved in file {file}")


class CONLLFactory:
    @staticmethod
    def load_corpus_from_file(conll_file):
        with open(conll_file, "r") as f:
            content = f.read()
        sents = content.split("\n\n")[:-1]
        corpus = CONLLCorpus(sents=sents)
        return corpus

    @staticmethod
    def load_sent(content):
        return CONLLSentence(content)


class CONLLSentenceFormatException(Exception):
    pass


class CONLLSentence:
    def __init__(self, content):
        lines = content.split("\n")
        self.id = 1

        if not lines[0].startswith("# sent_id ="):
            message = "sent_id must be in first row\n"
            message += content
            raise CONLLSentenceFormatException(message)
        if not lines[1].startswith("# text ="):
            message = "sent_id must be in second row\n"
            message += content
            raise CONLLSentenceFormatException(message)
        self.id = lines[0][12:]
        self.text = lines[1][9:]
        self.content = content


class CONLLCorpus:
    def __init__(self, sents):
        self.sents = {}
        for sent in sents:
            conll_sent = CONLLFactory.load_sent(sent)
            self.index(conll_sent)

    def index(self, sent: CONLLSentence):
        self.sents[sent.id] = sent

    def search(self, value=None):
        return list(self.sents.values())[:30]


class Doc:
    def __init__(self, id=None, sentences=None):
        self.id = id
        self.sentences = sentences

    @staticmethod
    def load_from_file(doc_id=None, doc_file=None):
        with open(doc_file, "r") as f:
            content = f.read()
        lines = content.splitlines()
        texts = [line for line in lines if not line.startswith("#")]
        ids = [f"{doc_id}-{str(i + 1)}" for i in range(len(texts))]
        sentences = {}
        for id, text in zip(ids, texts):
            sentences[id] = Sentence(id=id, text=text)
        doc = Doc(id=doc_id, sentences=sentences)
        return doc

    def auto_tags(self):
        for sent_id in self.sentences:
            self.sentences[sent_id].auto_tags()

    def to_conllu(self, **kwargs):
        content = f"# doc_id = {self.id}\n"
        content += "\n".join(sentence.to_conllu(**kwargs) for id, sentence in self.sentences.items())
        content += "\n"
        return content


class Sentence:
    def __init__(self, id=None, text=None):
        self.id = id
        self.text = text
        self.tokens = None

    def auto_tags(self):
        self.tokens = word_tokenize(self.text)

    def to_conllu(self, write_status=False, status=False):
        content = f"# sent_id = {self.id}\n"
        content += f"# text = {self.text}\n"
        if write_status:
            content += f"# status = \n"
        orders = [str(i + 1) for i in range(len(self.tokens))]
        rows = zip(orders, self.tokens)
        rows = ["\t".join(row) for row in rows]
        content += "\n".join(rows)
        content += "\n"
        return content
