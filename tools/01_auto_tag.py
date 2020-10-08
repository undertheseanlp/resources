from tools.data import Corpus


corpus = Corpus.load_from_folder("data/docs")
corpus.auto_tags()
corpus.save_conllu("todo/vi_corpus_v1_todo.conllu", write_status=True)

tagged_corpus = Corpus.load_from_conllu_file("vi_corpus_v1.conllu")

print(0)
# content = "\n\n".join(tokenizes)
# open("tmp/tokenize_data.txt", "w").write(content)
