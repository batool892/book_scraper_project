import csv
import os
from bs4 import BeautifulSoup
import requests


def scrape_books(url="http://books.toscrape.com/"):
  """Scrapes book titles and prices from books.toscrape.com safely."""
  books_list = []

  try:
    response = requests.get(url, timeout=10)
    # Check that the page responded successfully (200 OK)
    if response.status_code != 200:
      print(f"Error: Received status code {response.status_code}")
      return books_list

    # Convert the text into BeautifulSoup for parsing
    soup = BeautifulSoup(response.text, "html.parser")
    # Search for book elements on the page
    books = soup.find_all("article", class_="product_pod")

    for book in books:
      #  Extract the book title
      title = book.h3.a["title"]
      # Extract the price
      price = book.find("p", class_="price_color").text

      books_list.append({"Title": title, "Price": price})

  except requests.exceptions.RequestException as e:
    print(f"Network error occurred: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

  return books_list


def save_to_csv(data, file_path="data/books_data.csv"):
  """Saves the scraped data into a CSV file (Data Persistence)."""
  try:
    # Make sure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(
        file_path, mode="w", newline="", encoding="utf-8"
    ) as csv_file:
      fieldnames = ["Title", "Price"]
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

      writer.writeheader()
      for row in data:
        writer.writerow(row)
    print(f"Successfully saved data to {file_path}")

  except IOError as e:
    print(f"File writing error: {e}")

def get_book_count(data):
  """Returns the total number of books scraped."""
  return len(data)

def get_first_books(data, n=3):
  """Returns the first n books from the scraped data."""
  return data[:n]