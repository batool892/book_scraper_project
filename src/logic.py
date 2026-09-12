import requests  # third-party HTTP library
from bs4 import BeautifulSoup  # third-party library for parsing HTML


def scrape_books(url="http://books.toscrape.com/"):
    """Scrape book titles and prices from a books.toscrape.com style page."""
    books_list = []  # will hold one dict per book we find on the page

    try:
        response = requests.get(url, timeout=10)  # ask the server for the page, wait max 10 seconds
        response.encoding = "utf-8"  # make sure special characters like £ show up correctly

        if response.status_code != 200:  # 200 means "OK"; anything else means something went wrong
            print(f"Error: server returned status code {response.status_code}")
            return books_list

        soup = BeautifulSoup(response.text, "html.parser")  # parse the HTML so we can search through it
        books = soup.find_all("article", class_="product_pod")  # each book on the page lives in one of these

        for book in books:  # loop over every book found on the page
            title = book.h3.a["title"]  # the title is stored in the "title" attribute of the <a> tag
            price = book.find("p", class_="price_color").text  # the price is the text inside this <p> tag
            books_list.append({"Title": title, "Price": price})  # save this book's data to our list

    except Exception as e:  # covers network errors, missing page elements, etc.
        print(f"An error occurred while scraping: {e}")

    return books_list


def get_book_count(data):
    """Return how many books are in the scraped data."""
    return len(data)


def get_first_books(data, n=3):
    """Return the first n books from the scraped data (default: 3)."""
    return data[:n]