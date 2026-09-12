import csv
import os


def validate_url(url):
  """Checks that the URL is a non-empty string starting with http."""
  return isinstance(url, str) and url.startswith(("http://", "https://"))


def save_to_csv(data, file_path="data/books_data.csv"):
  """Saves the scraped data into a CSV file (Data Persistence)."""
  try:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
      fieldnames = ["Title", "Price"]
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      writer.writeheader()
      for row in data:
        writer.writerow(row)
    print(f"Successfully saved data to {file_path}")
  except IOError as e:
    print(f"File writing error: {e}")


def read_from_csv(file_path="data/books_data.csv"):
  """Reads previously saved book data back from a CSV file."""
  data = []
  try:
    with open(file_path, mode="r", newline="", encoding="utf-8") as csv_file:
      reader = csv.DictReader(csv_file)
      for row in reader:
        data.append(row)
  except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
  except IOError as e:
    print(f"File reading error: {e}")
  return data