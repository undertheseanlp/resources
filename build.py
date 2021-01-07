import sys
from os import listdir
from os.path import dirname, join, isdir, realpath, basename
from termcolor import colored
import yaml


def exit(message):
    print(colored(message, 'red'))
    sys.exit(0)


corpora = []


def validate_corpus_folder(f):
    # each resource folder should has metadata file
    files = listdir(f)
    resource_name = basename(f)
    print(f"[ ] Validate resource {resource_name}")
    if "metadata.yaml" not in files:
        exit(f"[ERROR] Resource {resource_name} must has valid metadata.yaml file")
    with open(join(f, "metadata.yaml")) as metadata_file:
        corpus = yaml.safe_load(metadata_file)
        corpus["name"] = basename(f)
        corpora.append(corpus)
    print(f"\t  ✓ Done\n")


PROJECT_FOLDER = dirname(realpath(__file__))
RESOURCES_FOLDER = join(PROJECT_FOLDER, "resources")
corpus_folders = [join(RESOURCES_FOLDER, f) for f in listdir(RESOURCES_FOLDER) if isdir(join(RESOURCES_FOLDER, f))]
for f in corpus_folders:
    validate_corpus_folder(f)

print(f"-> Detect {len(corpora)} resources\n")

print("[ ] Generate README.md file")
content = ""
# generate header
c = open(join(PROJECT_FOLDER, "docs", "templates", "README.md")).read()
dataset_badge_template = "https://img.shields.io/badge/datasets-?-brightgreen"
dataset_badge = dataset_badge_template.replace("?", str(len(corpora)))
c = c.replace(dataset_badge_template, dataset_badge)
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
    c += f"🐟 [{name}](resources/{name})\n\n"
    c += f"{description}\n\n"
    c += f"`task:{task}` `domain:{domain}` `version:{version}` `year:{year}`\n"
    c += "\n"
    content += c

with open(join(PROJECT_FOLDER, 'README.md'), 'w') as f:
    f.write(content)
print(f"\t  ✓ Done\n")
