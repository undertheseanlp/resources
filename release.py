import os
import sys
import shutil
from os.path import join

print("Release")
version = open("VERSION").read().strip()
from github import Github

token = os.environ['GITHUB_TOKEN']
print("environ", os.environ)
print("token", token)
print(sys.argv)
G = Github(token)

repo = G.get_repo("undertheseanlp/resources")

# Create new release if not exists
try:
    release_message = f"Release {version}"
    repo.create_git_release(version, f"Release {version}", release_message)
except:
    pass

# Build and pack datasets to this release
DATASETS_FOLDER = "tmp/datasets"
shutil.rmtree(DATASETS_FOLDER)
os.makedirs(DATASETS_FOLDER)
shutil.make_archive(join("SE_Vietnamese-UBS.zip"), "zip", "SE_Vietnamese-UBS/data")

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
