import os
import shutil
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
DATASETS_FOLDER = "tmp/datasets"
os.makedirs(DATASETS_FOLDER)
shutil.make_archive(join(DATASETS_FOLDER, "SE_Vietnamese-UBS.zip"), "zip", "SE_Vietnamese-UBS/data")

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
