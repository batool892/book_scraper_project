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
Pandas: Used to organize the data and save it in a CSV file.

## Project Structure
src/main.py: The main file that runs the scraping and saving process.
src/logic.py: Contains the main functions for processing and extracting the data.
src/utils.py: Contains helper functions for requests and handling errors.
data/: Stores the output files, such as the CSV file