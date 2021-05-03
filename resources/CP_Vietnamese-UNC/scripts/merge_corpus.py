from os.path import join, dirname

from data import TextCorpus, ROOT_FOLDER

corpus_folder = join(ROOT_FOLDER, "corpus", "CP_Vietnamese-UNC")
tc1 = TextCorpus.load(corpus_folder)
