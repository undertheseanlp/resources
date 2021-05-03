import os
from os.path import join, basename, dirname

DATA_FOLDER = join(dirname(dirname(__file__)), "corpus", "CP_Vietnamese-UNC")


def warn(file, line_number, message, type=None):
    global total_erros
    text = ""
    if type:
        text = f"[{type}] "
    text += basename(file) + ":" + str(line_number)
    print(text, message)
    total_erros += 1


total_documents = 0
total_sentences = 0
MIN_SENTENCES_PER_TOPICS = 300
MIN_SENTENCES_PER_FILE = 3
MIN_SENTENCES_IN_CORPUS = 3000
topics = ["society", "world", "business", "tech", "entertainment", "sport", "health", "science", "education", "travel"]
topics_sentences = {}
for topic in topics:
    topics_sentences[topic] = 0
total_erros = 0


def validate():
    global topics
    global MIN_SENTENCES_PER_TOPICS

    def validate_file(file):
        global topics_sentences
        global total_sentences
        global total_documents
        total_documents += 1
        try:
            # file should has doc_id, url and date
            lines = open(file).read().splitlines()
            lines = [(i + 1, line) for i, line in enumerate(lines)]
            if not lines[0][1].startswith("# doc_id = "):
                warn(file, 1, "File should has valid doc_id", "E101")
            doc_id = lines[0][1][11:]
            if doc_id != basename(file)[:-4]:
                warn(file, 1, "doc_id must be same with file name", "E101")
            file_topic = None
            for topic in topics:
                if topic in lines[0][1]:
                    file_topic = topic
            if file_topic is None:
                warn(file, 0, "File should has valid topic", "E104")
            if not lines[1][1].startswith("# url = "):
                warn(file, 1, "File should has valid url", "E102")
            if not lines[2][1].startswith("# date = "):
                warn(file, 2, "File should has valid date", "E103")
            # file shouldn't contains space
            sentences = lines[4:]
            if len(sentences) < MIN_SENTENCES_PER_FILE:
                warn(file, 4, f"File should has more than {MIN_SENTENCES_PER_FILE} sentences", "E105")
                return
            for line_number, sentence in sentences:
                if sentence == "":
                    warn(file, line_number, "Sentence should not be blank", "E301")
                    continue
                if sentence.strip() != sentence:
                    warn(file, line_number, "Sentence should be striped", "E302")
                    continue
            topics_sentences[file_topic] += len(sentences)
            total_sentences += len(sentences)
        except Exception as e:
            warn(file, 0, e)

    files = os.listdir(DATA_FOLDER)
    files = sorted([join(DATA_FOLDER, file) for file in files])
    for file in files:
        validate_file(file)

    for topic in topics:
        n_sentences = topics_sentences[topic]
        if n_sentences < MIN_SENTENCES_PER_TOPICS:
            message = f'Topic "{topic}" should has at least {MIN_SENTENCES_PER_TOPICS} sentences (found {n_sentences})'
            warn('CORPUS', '', message, 'E201')

    if total_sentences < MIN_SENTENCES_IN_CORPUS:
        message = f'Corpus should has at least {MIN_SENTENCES_IN_CORPUS} sentences (found {total_sentences})'
        warn('CORPUS', '', message, 'E202')


def stats():
    print("\n# CORPUS STATISTICS")
    global topics
    global total_sentences
    global total_documents
    print("Number of topics    :", len(topics))
    print("Number of documents :", total_documents)
    print("Number of sentences :", total_sentences)


def build():
    global total_erros
    validate()
    if total_erros > 0:
        print(f"\n[x] BUILD ERRORS: {total_erros} errors")
    else:
        print(f"\n[+] BUILD SUCCESS")
    stats()


build()
