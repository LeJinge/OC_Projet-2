from Method.scrap_one_page import scrap_one
from Method.scrap_one_category import scrap_one_category
from Method.scrap_all_category import scrap_all_category
import csv

categorylinks = scrap_all_category()
book_info = []
books_info = []

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
    books_info.clear()


