import os
import shutil
from os import listdir
from os.path import join
from github import Github
import yaml


def get_version(resource):
    metadata = yaml.safe_load(open(join("resources", resource, "metadata.yaml")))
    return str(metadata['version'])


datasets = {}
versions = {}


# Build and pack datasets to this release
def scan_datasets():
    global datasets
    global versions
    resources = os.listdir("resources")
    for resource in resources:
        if "datasets" not in listdir(join("resources", resource)):
            print(f"[warning] {resource} has not datasets")
            continue
        version = get_version(resource)
        items = listdir(join("resources", resource, "datasets"))
        for item in items:
            datasets[item] = join("resources", resource, "datasets", item)
            versions[item] = version


DATASETS_FOLDER = "tmp/datasets"
shutil.rmtree(DATASETS_FOLDER, ignore_errors=True)
os.makedirs(DATASETS_FOLDER)
scan_datasets()
for dataset in datasets:
    shutil.make_archive(join(DATASETS_FOLDER, dataset) + "-" + versions[dataset], "zip", datasets[dataset])

G = Github(os.environ['GITHUB_TOKEN'])
repo = G.get_repo("undertheseanlp/resources")
version = open("VERSION").read().strip()

# Create new release if not exists
try:
    release_message = f"Release {version}"
    repo.create_git_release(version, f"Release {version}", release_message)
except:
    pass

# Upload assets
assets = os.listdir(DATASETS_FOLDER)
release = repo.get_release(id=version)
current_assets = set([asset.name for asset in release.get_assets()])
print(f"Current datasets: {len(current_assets)}")
for asset in current_assets:
    print(f"- {asset}")

for asset in assets:
    if asset in current_assets:
        continue
    try:
        release.upload_asset(join(DATASETS_FOLDER, asset))
        print(f"Upload asset {asset} successfully")
    except Exception as e:
        print(e)
