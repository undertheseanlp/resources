import requests
from bs4 import BeautifulSoup
url = "https://baomoi.com/"

r = requests.get(url)
print(0)

html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')
links = [tag.find("a") for tag in soup.find_all("h4")]
print(links)
