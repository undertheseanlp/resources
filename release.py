import os
import sys
print("Release")

from github import Github
token = os.getenv('GITHUB_TOKEN', '...')
print("environ", os.environ)
print("token", token)
print(sys.argv)
G = Github(token)

repo = G.get_repo("undertheseanlp/resources")
releases = repo.get_releases()
for release in releases:
    print(release)

print(G.get_user())
print(G.get_user())
# for repo in G.get_user().get_repos():
#     print(repo.name)




