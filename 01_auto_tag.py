from underthesea import word_tokenize


def load_dictionary():
    words = open("data/dictionary.txt")
    return words


dictionary = load_dictionary()


def load_raw_sentences():
    sentences = open("data/sentences.txt").read().splitlines()
    return sentences


def convert_to_tokenize(tokens):
    return "\n".join(tokens)


sentences = load_raw_sentences()


def generate_tokenize(sentence):
    tokens = word_tokenize(sentence)
    return convert_to_tokenize(tokens)


tokenizes = [generate_tokenize(sentence) for sentence in sentences]

content = "\n\n".join(tokenizes)
open("tmp/tokenize_data.txt", "w").write(content)
