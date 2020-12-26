import os
print("Release")

print("Get Release")

from github import Github
token = os.getenv('GITHUB_TOKEN', '...')
print(token)
G = Github(token)

repo = G.get_repo("undertheseanlp/resources")
releases = repo.get_releases()
for release in releases:
    print(release)