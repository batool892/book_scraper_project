# Book_Scraper_Project (Capstone Project)

This is a Python project that scrapes book data from the web, processes the information,
 and saves it into a CSV file using a functional programming approach

## Installation and Usage

1. Install required packages:
   ```bash
   pip install -r requirements.txt

2. Run the application:
    ```bash
    python src/main.py


## Libraries Used
BeautifulSoup4: Used to read the HTML and get the information I need from the webpage.
Requests: Used to send HTTP requests and get the webpage data.

## Project Structure
src/main.py: The main file. It runs the scraping and saving process and gets the URL from the user.
src/logic.py: Contains the main functions for extracting data from the webpage.
src/utils.py: Contains helper functions for validation and working with CSV files.