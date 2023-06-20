from Method.scrap_one_page import scrap_one
from Method.scrap_one_category import scrap_one_category
from Method.scrap_all_category import scrap_all_category
import csv
import os
import requests
import unicodedata
import re


categorylinks = scrap_all_category()
book_info = []
books_info = []
new_folder = None

os.makedirs('Data\\Image', exist_ok=True)
os.makedirs('Data\\Category', exist_ok=True)

for categorylink in categorylinks:
    booklinks = scrap_one_category(categorylink)

    for booklink in booklinks:
        book_info = scrap_one(booklink)
        books_info.append(book_info)
        csv_category = book_info["category"]
        filename = f".\Data\Category\{csv_category}.csv"
        keys = books_info[0].keys()
        with open(filename, "w", encoding="utf8", newline="") as csvfile:
            dict_writer = csv.DictWriter(csvfile, keys, delimiter=";")
            dict_writer.writeheader()
            dict_writer.writerows(books_info)

    for booklink in booklinks:
        book_info = scrap_one(booklink)
        books_info.append(book_info)
        csv_category = book_info["category"]
        image_name = book_info["title"]
        image_name = unicodedata.normalize('NFKD', image_name).encode('ascii', 'ignore')
        image_name = image_name.decode("ascii")
        image_name = re.sub('[:/"*?]', ' ', image_name)
        url_image = book_info["image_url"]
        download_image = requests.get(url_image).content
        new_folder = f"Data\\Image\{csv_category}"
        if not os.path.exists(new_folder) :
            os.mkdir(new_folder)
        with open(new_folder+'\\'+str(image_name)+".jpg", "wb+") as handler:
            handler.write(download_image)

    books_info.clear()
