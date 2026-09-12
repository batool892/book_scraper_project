from utils import validate_url
from bs4 import BeautifulSoup
import requests


def scrape_books(url="http://books.toscrape.com/"):
    """Scrapes book titles and prices from books.toscrape.com safely."""
    books_list = []

    if not validate_url(url):
        print("Error: Invalid URL provided.")
        return books_list

    try:
        response = requests.get(url, timeout=10)
        response.encoding = response.apparent_encoding  # It solves the encoding problem

        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return books_list

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            books_list.append({"Title": title, "Price": price})

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return books_list


def get_book_count(data):
    """Returns the total number of books scraped."""
    return len(data)


def get_first_books(data, n=3):
    """Returns the first n books from the scraped data."""
    return data[:n]