from utils import save_to_csv, scrape_books, get_book_count, get_first_books


def main():
  print("=== Starting Book Scraper Tool ===")

  target_url = "http://books.toscrape.com/"
  print(f"Fetching data from: {target_url}")

  # Fetch the data
  scraped_data = scrape_books(target_url)

  if scraped_data:
    print(f"Successfully scraped {len(scraped_data)} books.")

    # Save the data to a CSV file
    save_to_csv(scraped_data)

    print("\n--- Summary Insights ---")
    total_books = get_book_count(scraped_data)
    print(f"Total number of books scraped: {total_books}")
    first_books = get_first_books(scraped_data, n=3)
    for i, book in enumerate(first_books, 1):
      print(f"{i}. {book['Title']} - {book['Price']}")
  else:
    print("No data was collected due to an error.")

  print("=== Process Finished ===")


if __name__ == "__main__":
  main()