from os.path import join, dirname

from data import CONLLFactory

bk_treebank_file = join(dirname(dirname(__file__)), "tmp", "UD_Vietnamese-BKT2", "vi_bkt2-ud-train.conllu")
corpus = CONLLFactory.load_corpus_from_file(bk_treebank_file)