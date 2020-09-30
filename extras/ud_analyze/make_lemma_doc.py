import shutil
from os import listdir
from os.path import abspath, join
import click
import os

from jinja2 import Template

cwd = os.path.dirname(__file__)

lemmas = {}


def parse_sentence(sentence):
    rows = sentence.split("\n")
    rows = [row for row in rows if not row.startswith("# ")]
    text = " ".join([row.split("\t")[2] for row in rows])
    for row in rows:
        id, form, lemma, upos, xpos, feats, head, deprel, deps, misc = row.split("\t")
        if lemma not in lemmas:
            lemmas[lemma] = {
                "sent_count": 1,
                "upos": {},
                "deprel": {}
            }
        else:
            lemmas[lemma]["sent_count"] += 1
        if upos not in lemmas[lemma]["upos"]:
            lemmas[lemma]["upos"][upos] = {
                "count": 1,
                "text": [text]
            }
            lemmas[lemma]["upos"][upos]["text"] = [text]
        else:
            lemmas[lemma]["upos"][upos]["count"] += 1
            lemmas[lemma]["upos"][upos]["text"].append(text)
        if deprel not in lemmas[lemma]["deprel"]:
            lemmas[lemma]["deprel"][deprel] = {
                "count": 1,
                "text": [text]
            }
        else:
            lemmas[lemma]["deprel"][deprel]["count"] += 1
            lemmas[lemma]["deprel"][deprel]["text"].append(text)
    return sentence


def parse_treebank(treebank_file):
    sentences = open(treebank_file).read().split("\n\n")[:-1]
    sentences = [parse_sentence(s) for s in sentences]


class Lemma:
    def __init__(self, lemma, data):
        self.lemma = lemma
        self.data = data

    def to_url(self):
        url = self.lemma.replace("/", "_")
        return url

    def to_text(self):
        lemma = self.lemma
        url = self.to_url()
        count = self.data["sent_count"]
        text = f'<a href="./details/{url}.html">{lemma}</a> ({count})'
        return text

    def to_detail_text(self):
        text = self.lemma
        data = {"content": str(self.data), "sent_count": self.data["sent_count"], "text": text, "data": self.data}
        return data


def sort_lemma_f(lemma):
    return lemma.lemma


def make_lemmas_doc(doc_folders):
    if "lemmas" in listdir(doc_folders):
        shutil.rmtree(join(doc_folders, "lemmas"))
    os.makedirs(join(doc_folders, "lemmas"))
    os.makedirs(join(doc_folders, "lemmas", "details"))
    index_file = join(doc_folders, "lemmas", "index.html")
    index_template = Template(open(join(cwd, "lemmas_index.html.template")).read())
    lemmas_data = [Lemma(key, lemmas[key]) for key in lemmas]
    lemmas_data = sorted(lemmas_data, key=sort_lemma_f)
    lemmas_content = ", ".join([item.to_text() for item in lemmas_data])
    content = index_template.render(content=lemmas_content)

    detail_template = Template(open(join(cwd, "lemmas_detail.html.template")).read())
    open(index_file, "w").write(content)
    for item in lemmas_data:
        url = item.to_url()
        word_file = join(doc_folders, "lemmas", "details", f"{url}.html")
        content = detail_template.render(**item.to_detail_text())
        open(word_file, "w").write(content)
    print("make lemmas doc")


@click.command()
@click.option('--treebank', required=True)
@click.option('--docs', required=True)
def main(treebank, docs):
    """Console script for make doc"""
    try:
        treebank_folder = abspath(join(cwd, treebank))
        print(treebank_folder)
        files = os.listdir(treebank_folder)
        files = [file for file in files if file.endswith(".conllu")]
        if len(files) == 0:
            raise Exception(f"Treebank folder `{treebank_folder}` must contains *.conllu files")
    except:
        raise Exception(f"Treebank folder `{treebank_folder}` must contains *.conllu files")
    for file in files:
        treebank_file = join(treebank_folder, file)
        parse_treebank(treebank_file)

    try:
        docs_folder = abspath(join(cwd, docs))
        os.listdir(docs_folder)
    except:
        raise Exception(f"Docs folder `{docs_folder} must be existed.")

    make_lemmas_doc(docs_folder)


if __name__ == '__main__':
    main()
