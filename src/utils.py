import csv
import os


def validate_url(url):
    """Check that url is a text string starting with http:// or https://."""
    return isinstance(url, str) and url.startswith(("http://", "https://"))


def save_to_csv(data, file_path="data/books_data.csv"):
    """Write the scraped data (a list of dicts) to a CSV file."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # make sure the data/ folder exists
        with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:  # open/create the file for writing
            fieldnames = ["Title", "Price"]  # the column headers
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)  # writer that understands dicts
            writer.writeheader()  # write the header row first
            for row in data:  # write one row per book
                writer.writerow(row)
        print(f"Successfully saved data to {file_path}")
    except IOError as e:  # covers permission errors, disk full, etc.
        print(f"File writing error: {e}")


def read_from_csv(file_path="data/books_data.csv"):
    """Read book data back from a CSV file and return it as a list of dicts."""
    data = []
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as csv_file:  # open the file for reading
            reader = csv.DictReader(csv_file)  # reader that turns each row into a dict
            for row in reader:  # loop over every row in the file
                data.append(row)
    except FileNotFoundError:
        print(f"Error: file not found at {file_path}")
    except IOError as e:
        print(f"File reading error: {e}")
    return data