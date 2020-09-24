from data import Corpus

form_set = set()
lemma_set = set()
upos_set = set()
xpos_set = set()
feats_set = set()
head_set = set()
deprel_set = set()
deps_set = set()
misc_set = set()


def load_bk_treebank():
    global word_tag_set
    global pos_tag_set
    global lemma_tag_set

    f = open("tmp/BKT/train")
    content = f.read()
    sentences = content.split("\n\n")
    sentences = [s.split("\n") for s in sentences]
    for s in sentences:
        if s == [""]:
            continue
        for token_text in s:
            tokens = token_text.split("\t")
            id, form, lemma, upos, xpos, feats, head, deprel, deps, misc = tokens
            form_set.add(form)
            lemma_set.add(lemma)
            upos_set.add(upos)
            xpos_set.add(xpos)
            feats_set.add(feats)
            head_set.add(head)
            deprel_set.add(deprel)
            deps_set.add(deps)
            misc_set.add(misc)
    return sentences


sentences = load_bk_treebank()
# print("== FORM == ")
# print(form_set)
print(sorted(deprel_set))
