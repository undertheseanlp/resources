import os
print("Release")

print("Get Release")

from github import Github
token = os.getenv('GITHUB_TOKEN', '...')
print(token)