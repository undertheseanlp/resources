import sys
from os import listdir
from os.path import dirname, join, isdir, realpath
from termcolor import colored
import yaml


def exit(message):
    print(colored(message, 'red'))
    sys.exit(0)


corpora = []


def validate_corpus_folder(f):
    # each resource folder should has metadata file
    print(f"[ ] Validate resource {f}")
    files = listdir(f)
    if "metadata.yaml" not in files:
        exit("[ERROR] Resource must has valid metadata.yaml file")
    with open(join(f, "metadata.yaml")) as metadata_file:
        corpus = yaml.safe_load(metadata_file)
        corpus["name"] = f
        corpora.append(corpus)
    print(f"[✓] Validate resource {f}: Success\n")


FOLDER = dirname(realpath(__file__))
folders = [f for f in listdir(FOLDER) if isdir(join(FOLDER, f))]
ignore_folders = ["tools", "app", "docs", ".git", "data", "tmp", ".idea", "extras"]
corpus_folders = [f for f in folders if f not in ignore_folders]
for f in corpus_folders:
    validate_corpus_folder(f)

print(f"-> Detect {len(corpora)} resources\n")

print("[ ] Generate README.md file")
content = ""
# generate header
c = open(join(FOLDER, "docs", "templates", "README.md")).read()
dataset_badge_template = "https://img.shields.io/badge/datasets-?-brightgreen"
dataset_badge = dataset_badge_template.replace("?", str(len(corpora)))
c.replace(dataset_badge_template, dataset_badge)
content += c + "\n\n"

# generate list datasets
content += "## List Datasets\n\n"


def get_key(data, key):
    if key in data:
        return data[key]
    else:
        return ""


for corpus in corpora:
    c = ""
    name = get_key(corpus, "name")
    description = get_key(corpus, "description")
    task = get_key(corpus, "task")
    domain = get_key(corpus, "domain")
    year = get_key(corpus, "year")
    version = get_key(corpus, "version")
    c += f"🐟 [{name}]({name}) `v{version}`\n\n"
    c += f"{description}\n\n"
    c += f"`task:{task}` `domain:{domain}` `year:{year}`\n"
    c += "\n"
    content += c

with open(join(FOLDER, 'README.md'), 'w') as f:
    f.write(content)
print("[✓] Generate README.md file: Success")
