import os
import shutil
from os import listdir
from os.path import join
from github import Github

G = Github(os.environ['GITHUB_TOKEN'])
repo = G.get_repo("undertheseanlp/resources")
version = open("VERSION").read().strip()

# Create new release if not exists
try:
    release_message = f"Release {version}"
    repo.create_git_release(version, f"Release {version}", release_message)
except:
    pass


# Build and pack datasets to this release
def scan_datasets():
    resources = os.listdir("resources")
    datasets = {}
    for resource in resources:
        if "datasets" not in listdir(join("resources", resource)):
            print(f"[warning] {resource} has not datasets")
            continue
        items = listdir(join("resources", resource, "datasets"))
        for item in items:
            datasets[item] = join("resources", resource, "datasets", item)
    return datasets


datasets = scan_datasets()
DATASETS_FOLDER = "tmp/datasets"
os.makedirs(DATASETS_FOLDER)
for dataset in datasets:
    shutil.make_archive(join(DATASETS_FOLDER, dataset), "zip", datasets[dataset])

# Upload assets

assets = os.listdir(DATASETS_FOLDER)
release = repo.get_release(id=version)
current_assets = set([asset.name for asset in release.get_assets()])
print(current_assets)
for asset in assets:
    if asset in current_assets:
        continue
    try:
        release.upload_asset(join(DATASETS_FOLDER, asset))
        print(f"Upload asset {asset} successfully")
    except:
        pass
