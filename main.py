from Method.scrap_one_page import scrap_one
from Method.scrap_one_category import scrap_one_category

book_info = []
books_info = []

booklinks = scrap_one_category()

for booklink in booklinks:
    book_info = scrap_one(booklink)
    books_info.append(book_info)
print(books_info)
