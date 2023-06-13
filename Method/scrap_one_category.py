import requests
from bs4 import BeautifulSoup


def scrap_one_category():
    book_links = []
    while True:
        category_page = requests.get("http://books.toscrape.com/catalogue/category/books/travel_2/index.html")
        soup = BeautifulSoup(category_page.text, 'html.parser')
        books_url = soup.find_all('h3')
        for book_url in books_url:
            book_url = f"http://books.toscrape.com/catalogue/{book_url.find('a')['href'][9:]}"
            book_links.append(book_url)

        return book_links
