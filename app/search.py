from os.path import dirname, join

from data import CONLLFactory

search_value = "DET-ADJ"

bk_treebank_file = join(dirname(dirname(__file__)), "tmp", "UD_Vietnamese-BKT2", "vi_bkt2-ud-train.conllu")
corpus = CONLLFactory.load_corpus_from_file(bk_treebank_file)
sent = corpus.search()
print(0)
