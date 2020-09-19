class Dictionary:
    words = []

    @staticmethod
    def load():
        words = open("data/dictionary.txt")
        Dictionary.words = words

    @staticmethod
    def is_exist(word):
        return False

Dictionary.load()

def load_words():
    words = open("data/tokenized_data.txt").read().splitlines()
    words = [word for word in words if not "#####" in word]
    return words

words = load_words()
words = sorted(set(words))
new_words = [word for word in words if not Dictionary.is_exist(word)]

def create_new_word_form(word):
    content = "#" * 60 + "\n"
    content += "WORD: " + word + "\n"
    content += "POSTAG: " + "\n"
    content += "ENTITY_TYPE: " + "\n"
    content += "WIKIDATA_ID: " + "\n"
    return content

forms = [create_new_word_form(word) for word in new_words]
content = "\n\n".join(forms)
open("tmp/new_words_form.txt", "w").write(content)