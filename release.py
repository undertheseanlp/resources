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
repo.create_git_release(version, f"Release {version}")




