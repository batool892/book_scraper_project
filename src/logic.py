Python
import pandas as pd
from bs4 import BeautifulSoup
from src.utils import fetch_page

def parse_articles(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return [{'Title': article.find('h2').get_text(strip=True)} 
            for article in soup.find_all('article') if article.find('h2')]

def save_to_csv(records, output_path):
    dataframe = pd.DataFrame(records)
    dataframe.to_csv(output_path, index=False)
    return len(dataframe)

def run_pipeline(url, output_path):
    html_content = fetch_page(url)
    if not html_content:
        return
    records = parse_articles(html_content)
    row_count = save_to_csv(records, output_path)
    print(f"Successfully processed {row_count} rows and saved to {output_path}")