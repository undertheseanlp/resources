import os
from os.path import join, basename

SCRIPTS_FOLDER = os.path.dirname(__file__)
DATA_FOLDER = join(os.path.dirname(SCRIPTS_FOLDER), "data")


def warn(file, line_number, message, type=None):
    text = ""
    if type:
        text = f"[{type}] "
    text += basename(file) + ":" + str(line_number)
    print(text, message)


total_sentences = 0
MIN_SENTENCES_PER_TOPICS = 300
MIN_SENTENCES_PER_FILE = 3
topics = ["society", "sport", "health", "economy", "tech", "education", "laws"]
topics_sentences = {}
for topic in topics:
    topics_sentences[topic] = 0


def validate():
    global topics
    global MIN_SENTENCES_PER_TOPICS

    def validate_file(file):
        global topics_sentences
        global total_sentences
        try:
            # file should has doc_id, url and date
            lines = open(file).read().splitlines()
            lines = [(i + 1, line) for i, line in enumerate(lines)]
            if not lines[0][1].startswith("# doc_id = "):
                warn(file, 1, "File should has valid doc_id")
            file_topic = None
            for topic in topics:
                if topic in lines[0][1]:
                    file_topic = topic
            if file_topic is None:
                warn(file, 0, "File should has valid topic")
            if not lines[1][1].startswith("# url = "):
                warn(file, 1, "File should has valid url")
            if not lines[2][1].startswith("# date = "):
                warn(file, 2, "File should has valid date")
            # file shouldn't contains space
            sentences = lines[4:]
            if len(sentences) < MIN_SENTENCES_PER_FILE:
                warn(file, 4, f"File should has more than {MIN_SENTENCES_PER_FILE}", "FILE_ERROR")
                return
            for line_number, sentence in sentences:
                if sentence == "":
                    warn(file, line_number, "Sentence should not be blank")
                    return
            topics_sentences[file_topic] += len(sentences)
            total_sentences += len(sentences)
        except Exception as e:
            warn(file, 0, e)

    files = os.listdir(DATA_FOLDER)
    files = [join(DATA_FOLDER, file) for file in files]
    for file in files:
        validate_file(file)

    for topic in topics:

        n_sentences = topics_sentences[topic]
        if n_sentences < MIN_SENTENCES_PER_TOPICS:
            message = f'[CORPUS_INCOMPLETE] Topic "{topic}" should has at least {MIN_SENTENCES_PER_TOPICS} sentences (found {n_sentences})'
            print(message)


def build():
    validate()


build()
print("[+] Build: DONE")
