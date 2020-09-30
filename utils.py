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


def convert_bkt_to_ud_extract_lemma(row):
    row[2] = row[1]
    return row


def convert_bkt_to_ud_sentence_converter(sentence, i, corpus_name):
    if sentence == "":
        return sentence
    result = ""
    result += f"# sent_id = {corpus_name}-s{i + 1}\n"
    rows = [s.split("\t") for s in sentence.split("\n")]
    rows = [convert_bkt_to_ud_extract_lemma(row) for row in rows]
    forms = [row[1] for row in rows]
    text = " ".join(forms)
    result += f"# text = {text}\n"
    sentence = "\n".join(["\t".join(row) for row in rows])
    result += sentence
    return result


def convert_bkt_to_ud2(content, corpus_name):
    # tags
    content = content.replace("\tNN\t", "\tNOUN\t")
    content = content.replace("\tNNP\t", "\tPROPN\t")
    content = content.replace("\tCL\t", "\tNOUN\t")

    content = content.replace("\tPRP\t", "\tPRON\t")

    content = content.replace("\tCD\t", "\tNUM\t")

    content = content.replace("\tVB\t", "\tVERB\t")
    content = content.replace("\tAV\t", "\tVERB\t")

    content = content.replace("\tJJ\t", "\tADJ\t")
    content = content.replace("\tVA\t", "\tADJ\t")

    content = content.replace("\tRB\t", "\tADV\t")
    content = content.replace("\tTO\t", "\tADV\t")

    content = content.replace("\tDT\t", "\tDET\t")
    content = content.replace("\tIN\t", "\tADP\t")
    content = content.replace("\tMD\t", "\tAUX\t")

    content = content.replace("\tCC\t", "\tCCONJ\t")

    content = content.replace("\tRBKT\t", "\tPUNCT\t")
    content = content.replace("\tLBKT\t", "\tPUNCT\t")

    # deps
    content = content.replace("\tcl\t", "\tclf\t")
    content = content.replace("\tROOT\t", "\troot\t")
    content = content.replace("\tdobj\t", "\tobj\t")
    return content


def convert_bkt_to_ud2(content, corpus_name):
    # tags
    content = content.replace("\tNN\t", "\tNOUN\t")
    content = content.replace("\tNNP\t", "\tPROPN\t")
    content = content.replace("\tCL\t", "\tNOUN\t")

    content = content.replace("\tPRP\t", "\tPRON\t")

    content = content.replace("\tCD\t", "\tNUM\t")

    content = content.replace("\tVB\t", "\tVERB\t")
    content = content.replace("\tAV\t", "\tVERB\t")

    content = content.replace("\tJJ\t", "\tADJ\t")
    content = content.replace("\tVA\t", "\tADJ\t")

    content = content.replace("\tRB\t", "\tADV\t")
    content = content.replace("\tTO\t", "\tADV\t")

    content = content.replace("\tDT\t", "\tDET\t")
    content = content.replace("\tIN\t", "\tADP\t")
    content = content.replace("\tMD\t", "\tAUX\t")

    content = content.replace("\tCC\t", "\tCCONJ\t")

    content = content.replace("\tRBKT\t", "\tPUNCT\t")
    content = content.replace("\tLBKT\t", "\tPUNCT\t")

    # deps
    content = content.replace("\tcl\t", "\tclf\t")
    content = content.replace("\tROOT\t", "\troot\t")
    content = content.replace("\tdobj\t", "\tobj\t")
    return content


def normalize_bkt_2():
    SOURCE_TREEBANK = "UD_Vietnamese-BKT1"
    DEST_TREEBANK = "UD_Vietnamese-BKT2"

    content = open(f"tmp/{SOURCE_TREEBANK}/train").read()
    content = convert_bkt_to_ud2(content, "train")
    open(f"tmp/{DEST_TREEBANK}/vi_bkt2-ud-train.conllu", "w").write(content)

    content = open(f"tmp/{SOURCE_TREEBANK}/dev").read()
    content = convert_bkt_to_ud2(content, "dev")
    open(f"tmp/{DEST_TREEBANK}/vi_bkt2-ud-dev.conllu", "w").write(content)

    content = open(f"tmp/{SOURCE_TREEBANK}/test").read()
    content = convert_bkt_to_ud2(content, "test")
    open(f"tmp/{DEST_TREEBANK}/vi_bkt2-ud-test.conllu", "w").write(content)


def convert_bkt_to_ud_replace_tags(sentence):
    tokens = sentence.split("\n")
    results = tokens[:2]
    map_pos_tags = {
        "NN": "NOUN",
        "CL": "NOUN",
        "NNP": "PROPN",
        "PRP": "PRON",
        "CD": "NUM",
        "VB": "VERB",
        "AV": "VERB",
        "MD": "VERB",
        "JJ": "ADJ",
        "VA": "ADJ",
        "RB": "ADV",
        "TO": "ADV",
        "DT": "DET",
        "IN": "ADP",
        "CC": "CCONJ",
        "RBKT": "PUNCT",
        "LBKT": "PUNCT"
    }

    map_dep_tags = {
        "ROOT": "root",
        "cl": "clf",
        "dobj": "obj"
    }
    for row in tokens[2:]:
        items = row.split("\t")
        pos_tag = items[3]
        dep_tag = items[7]
        if pos_tag in map_pos_tags:
            items[3] = map_pos_tags[pos_tag]
        if dep_tag in map_dep_tags:
            items[7] = map_dep_tags[dep_tag]
        results.append("\t".join(items))
    result = "\n".join(results)
    return result


def convert_bkt_to_ud21(content):
    sentences = content.split("\n\n")
    sentences = sentences[:-1]
    sentences = [convert_bkt_to_ud_replace_tags(sentence) for sentence in sentences]
    content = "\n\n".join(sentences)
    content += "\n\n"
    return content


def normalize_bkt_21():
    SOURCE_TREEBANK = "UD_Vietnamese-BKT1"
    DEST_TREEBANK = "UD_Vietnamese-BKT2"

    content = open(f"tmp/{SOURCE_TREEBANK}/train").read()
    content = convert_bkt_to_ud21(content)
    open(f"tmp/{DEST_TREEBANK}/vi_bkt2-ud-train.conllu", "w").write(content)

    content = open(f"tmp/{SOURCE_TREEBANK}/dev").read()
    content = convert_bkt_to_ud21(content)
    open(f"tmp/{DEST_TREEBANK}/vi_bkt2-ud-dev.conllu", "w").write(content)

    content = open(f"tmp/{SOURCE_TREEBANK}/test").read()
    content = convert_bkt_to_ud21(content)
    open(f"tmp/{DEST_TREEBANK}/vi_bkt2-ud-test.conllu", "w").write(content)


def convert_bkt_to_ud_generate_sent_id(content, corpus_name):
    sentences = content.split("\n\n")
    sentences = sentences[:-1]
    sentences = [convert_bkt_to_ud_sentence_converter(sentence, i, corpus_name) for (i, sentence) in
                 enumerate(sentences)]
    content = "\n\n".join(sentences)
    return content


def convert_bkt_to_ud1(content, corpus_name):
    content = unicodedata.normalize("NFC", content)
    content = convert_bkt_to_ud_generate_sent_id(content, corpus_name)
    content += "\n\n"
    return content


def normalize_bkt_1():
    SOURCE_FOLDER = "tmp/BKT"
    UD_FOLDER = "UD_Vietnamese-BKT1"
    content = open(f"{SOURCE_FOLDER}/train").read()
    content = convert_bkt_to_ud1(content, "train")
    open(f"tmp/{UD_FOLDER}/train", "w").write(content)

    # content = open(f"{SOURCE_FOLDER}/dev").read()
    # content = convert_bkt_to_ud1(content, "dev")
    # open(f"tmp/{UD_FOLDER}/dev", "w").write(content)
    #
    # content = open(f"{SOURCE_FOLDER}/test").read()
    # content = convert_bkt_to_ud1(content, "test")
    # open(f"tmp/{UD_FOLDER}/test", "w").write(content)


# write_form_upos_set(form_upos_set)

# normalize_BKT()
# normalize_bkt_1()
# normalize_bkt_2()
normalize_bkt_21()
