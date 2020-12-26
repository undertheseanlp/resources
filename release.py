import os
import sys

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
assets = ["README.md"]
release = repo.get_release(id=version)
current_assets = [asset.name for asset in release.get_assets()]
print(current_assets)
for asset in assets:
    try:
        release.upload_asset(asset)
        print(f"Upload asset {asset} successfully")
    except:
        pass
