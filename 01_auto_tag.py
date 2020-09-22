from data import Corpus


# corpus = Corpus.load_from_folder("data/docs")
# corpus.auto_tags()

tagged_corpus = Corpus.load_from_conllu_file("vi_corpus_v1.conllu")

# content = "\n\n".join(tokenizes)
# open("tmp/tokenize_data.txt", "w").write(content)
