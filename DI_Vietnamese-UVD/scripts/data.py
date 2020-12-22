import yaml


class Word:
    def __init__(self, text, data=None):
        self.text = text
        self.data = data

    def to_dict(self):
        return {
            "text": self.text
        }


class Dictionary:
    def __init__(self):
        self.words = {}

    def add(self, word):
        self.words[word.text] = word

    @staticmethod
    def load(file):
        with open(file) as f:
            data = yaml.safe_load(f)
            new_dict = Dictionary()
            return new_dict

    def to_dict(self):
        data = {}
        words = sorted(self.words)
        for text in words:
            word = self.words[text]
            if word.data is None:
                content = ''
            elif len(word.data) == 0:
                content = ''
            else:
                content = word.data
            data[text] = content
        return data

    def save(self, file):
        data = self.to_dict()
        with open(file, 'w') as f:
            yaml.dump(data, f, sort_keys=False, allow_unicode=True)
