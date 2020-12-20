from data import Dictionary, Word

dict = Dictionary()
word = Word('a', [])
dict.add(word)
dict.save('test_dict.yaml')
