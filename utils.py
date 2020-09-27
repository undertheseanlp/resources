import unicodedata

from data import Corpus

form_set = set()
lemma_set = set()
form_upos_set = set()
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
            form_upos_set.add((form, upos))
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

# print(sorted(deprel_set))


def write_form_upos_set(form_upos_set):
    data = sorted(form_upos_set)
    f = open("tmp/bk_form_upos.csv", "w")
    f.write("form\tupos\n")
    for form, upos in data:
        f.write(f"{form}\t{upos}\n")


def normalize_BKT():
    UD_FOLDER = "UD_Vietnamese-BKT"
    content = open("tmp/BKT/train").read()
    content = unicodedata.normalize("NFC", content)
    open(f"tmp/{UD_FOLDER}/vi_bkt-ud-train.conllu", "w").write(content)

    content = open("tmp/BKT/dev").read()
    content = unicodedata.normalize("NFC", content)
    open(f"tmp/{UD_FOLDER}/vi_bkt-ud-dev.conllu", "w").write(content)

    content = open("tmp/BKT/test").read()
    content = unicodedata.normalize("NFC", content)
    open(f"tmp/{UD_FOLDER}/vi_bkt-ud-test.conllu", "w").write(content)


def convert_bkt_to_ud(content):
    content = unicodedata.normalize("NFC", content)

    # tags
    content = content.replace("\tNN\t", "\tNOUN\t")
    content = content.replace("\tCL\t", "\tNOUN\t")
    content = content.replace("\tRB\t", "\tADV\t")
    content = content.replace("\tVB\t", "\tVERB\t")
    content = content.replace("\tIN\t", "\tADP\t")

    # deps
    content = content.replace("\tcl\t", "\tclf\t")
    content = content.replace("\tROOT\t", "\troot\t")
    content = content.replace("\tdobj\t", "\tobj\t")

    return content


def normalize_BKT_2():
    UD_FOLDER = "UD_Vietnamese-BKT2"
    content = open("tmp/BKT/train").read()
    content = convert_bkt_to_ud(content)
    open(f"tmp/{UD_FOLDER}/vi_bkt2-ud-train.conllu", "w").write(content)

    content = open("tmp/BKT/dev").read()
    content = convert_bkt_to_ud(content)
    open(f"tmp/{UD_FOLDER}/vi_bkt2-ud-dev.conllu", "w").write(content)

    content = open("tmp/BKT/test").read()
    content = convert_bkt_to_ud(content)
    open(f"tmp/{UD_FOLDER}/vi_bkt2-ud-test.conllu", "w").write(content)


# write_form_upos_set(form_upos_set)

# normalize_BKT()
normalize_BKT_2()
