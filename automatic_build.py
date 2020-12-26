import os
from github import Github

G = Github(os.environ['GITHUB_TOKEN'])
repo = G.get_repo("undertheseanlp/resources")

try:
    repo.create_file("new_file.txt", "automatic build", "file_content 313213 ------ ")
except:
    pass

print('hihi')

