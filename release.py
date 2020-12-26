import os
import sys
print("Release")

from github import Github
token = os.environ['GITHUB_TOKEN']
print("environ", os.environ)
print("token", token)
print(sys.argv)
G = Github(token)

repo = G.get_repo("undertheseanlp/resources")
repo.create_git_release('ghi', 'ghi', 'ghi')




