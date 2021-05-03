from os import listdir
from os.path import join, dirname

ROOT_FOLDER = dirname(dirname(__file__))

CRAWL_FOLDER = join(ROOT_FOLDER, 'tmp', 'crawl')
DATASETS_FOLDER = join(ROOT_FOLDER, 'datasets', 'CP_Vietnamese-UNC')

CATEGORIES = {}
CATEGORIES_MAP = {
    'kinh-doanh': 'business',
    'suc-manh-so': 'tech',
    'suc-khoe': 'health',
    'giao-duc-huong-nghiep': 'education',
    'xa-hoi': 'society',
    'giai-tri': 'entertainment',
    'khoa-hoc-cong-nghe': 'science',
    'the-gioi': 'world',
    'du-lich': 'travel',
    'the-thao': 'sport'
}
DOC_URLS = set()


def fetch_current_dataset():
    global CATEGORIES
    global DOC_URLS
    filenames = sorted(listdir(DATASETS_FOLDER))
    for file in filenames:
        with open(join(DATASETS_FOLDER, file)) as f:
            lines = f.read().splitlines()
            doc_id = lines[0][11:]
            url = lines[1][8:]
            DOC_URLS.add(url)
            genre, category, doc_id_number = doc_id.split("_")
            if category not in CATEGORIES:
                CATEGORIES[category] = 0
            category_doc_number = int(doc_id_number)
            CATEGORIES[category] = max(CATEGORIES[category], category_doc_number)


def update_dataset(crawl_folder):
    global CATEGORIES
    global DOC_URLS
    files = sorted(listdir(crawl_folder))
    for file in files:
        with open(join(crawl_folder, file)) as f:
            content = f.read()
            lines = content.splitlines()
            url = lines[0][8:]
            if url in DOC_URLS:
                print(f"URL is existed. ({url})")
                continue
            DOC_URLS.add(url)
            genre = "news"
            category_text_id = url.split("/")[3]
            if category_text_id not in CATEGORIES_MAP:
                # print(f"Category '{category_text_id}' is not exist")
                continue
            category = CATEGORIES_MAP[category_text_id]
            CATEGORIES[category] += 1
            doc_id_number = CATEGORIES[category]
            doc_id_number_text = f"{doc_id_number:03d}"
            doc_id = "_".join([genre, category, doc_id_number_text])
            doc_id_line = f"# doc_id = {doc_id}\n"
            doc_filename = f"{doc_id}.txt"
            doc_filepath = join(DATASETS_FOLDER, doc_filename)
            with open(doc_filepath, "w") as outfile:
                output = doc_id_line + content
                outfile.write(output)


# MERGE CRAWL_FOLDER with CURRENT DATASET
fetch_current_dataset()
update_dataset(CRAWL_FOLDER)
print(CATEGORIES)
