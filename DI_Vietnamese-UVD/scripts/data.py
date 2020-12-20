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
        print("hihi")

    def to_dict(self):
        data = {
            'a': [
                {
                    'tag': 'noun',
                    'defs': [
                        {
                            'def': 'aflafjs',
                            'examples': [
                                'abc\n\n',
                                'def',
                                'ghi'
                            ]
                        }
                    ]
                }
            ],
            'b': [
                {'tag': 'noun'}
            ]
        }
        return data

    def save(self, file):
        data = self.to_dict()
        with open(file, 'w') as f:
            yaml.dump(data, f, sort_keys=False)
