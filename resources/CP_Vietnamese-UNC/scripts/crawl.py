from os.path import dirname, join

import requests
from bs4 import BeautifulSoup

CORPUS_LOCATION = join(dirname(dirname(__file__)), "corpus", "crawl")


def get_urls():
    for page in range(1, 11):
        yield f"https://dantri.com.vn/kinh-doanh/trang-{page}.htm"
        yield f"https://dantri.com.vn/giao-duc-huong-nghiep/trang-{page}.htm"
        yield f"https://dantri.com.vn/giai-tri/trang-{page}.htm"
        yield f"https://dantri.com.vn/suc-khoe/trang-{page}.htm"
        yield f"https://dantri.com.vn/khoa-hoc-cong-nghe/trang-{page}.htm"
        yield f"https://dantri.com.vn/khoa-hoc-cong-nghe/trang-{page}.htm"
        yield f"https://dantri.com.vn/xa-hoi/trang-{page}.htm"
        yield f"https://dantri.com.vn/the-thao/trang-{page}.htm"
        yield f"https://dantri.com.vn/suc-manh-so/trang-{page}.htm"
        yield f"https://dantri.com.vn/du-lich/trang-{page}.htm"
        yield f"https://dantri.com.vn/the-gioi/trang-{page}.htm"


def get_page_content(article_url):
    def clean_page_content(content):
        content = content.replace("\xa0", "")
        return content

    print(f"Crawl article {article_url}")
    html = requests.get(article_url).text
    article_id = article_url.split("/")[-1]
    date = article_id.split("-")[-1].split(".")[0][:8]
    soup = BeautifulSoup(html, "html.parser")
    paragraphs = soup.find("div", {"class": "dt-news__body"}).find_all("p")
    texts = [p.text for p in paragraphs]
    content = "\n".join(texts)
    content = clean_page_content(content)
    metadata = "# url = " + article_url + "\n" + \
        "# date = " + date + "\n"
    content = metadata + content
    with open(join(CORPUS_LOCATION, article_id), "w") as f:
        f.write(content)


def get_page(page_url):
    html = requests.get(page_url).text
    soup = BeautifulSoup(html, "html.parser")
    titles = soup.find_all("h3", {"class": "news-item__title"})
    urls = [title.find("a").get("href") for title in titles]
    urls = ["https://dantri.com.vn" + url for url in urls]
    for url in urls:
        get_page_content(url)


urls = get_urls()
for url in urls:
    get_page(url)
