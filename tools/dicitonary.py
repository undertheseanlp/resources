from os.path import dirname, join
import yaml

root = dirname(dirname(__file__))
dictionary_file = join(root, "data", "dictionary", "data.yaml")
with open(dictionary_file) as f:
    data = yaml.safe_load(open(dictionary_file))
print(0)