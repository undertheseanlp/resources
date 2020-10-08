import os
from os.path import dirname, join
import re

folder = dirname(dirname(__file__))
doc_folder = join(folder, "docs")
readme = join(folder, "README.md")
command = f"cp {doc_folder}/README.md {readme}"
os.system(command)


def copy_sub_folder(name):
    content = open(join(doc_folder, name, "README.md")).read()
    content = re.sub("\[(.*)\]\((.*)\)", r"[\1](docs/" + name + "/" + r"\2)", content)
    with open(readme, "a") as f:
        f.write(content)


copy_sub_folder("linguistics")
copy_sub_folder("vietnamese")
