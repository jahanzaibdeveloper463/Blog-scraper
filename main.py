"""
Project: Automated Blog / Content Harvester
Author: Jahanzaib
Description: Production-ready web scraper designed to crawl blog catalogs, 
             extract article titles, publication metadata, and target URIs, 
             and export them into structured spreadsheet formats.
"""

import sys
import logging
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Configure execution pipeline logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Target: Quotes ToScrape (Structured blog/article style markup for stable parsing)
BASE_URL = "https://quotes.toscrape.com/page/{}/"
OUTPUT_FILENAME = "blog_articles_export.xlsx"
MAX_PAGES = 2

def harvest_blog_articles():
    """Crawls multi-page blog archives, parses DOM article nodes, 
    and returns a normalized list of content records."""
    article_records = []
    
    logging.info("Initializing Blog Content Harvesting Pipeline...")

    for page_idx in range(1, MAX_PAGES + 1):
        target_url = BASE_URL.format(page_idx)
        logging.info(f"Ingesting markup payload from: {target_url}")

        try:
            response = requests.get(target_url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"Network transport fault on page {page_idx}: {err}")
            continue

        # Parse raw HTML into navigable tree structure
        soup = BeautifulSoup(response.text, "html.parser")
        quote_containers = soup.find_all("div", class_="quote")

        if not quote_containers:
            logging.warning(f"No article nodes resolved on page {page_idx}. Halting crawl.")
            break

        for idx, container in enumerate(quote_containers, start=1):
            # Extract main article title / quote text
            article_title = container.find("span", class_="text").text.strip()
            
            # Extract author / content contributor metadata
            contributor = container.find("small", class_="author").text.strip()
            
            # Extract category taxonomy tags
            tag_elements = container.find_all("a", class_="tag")
            tags_list = [tag.text for tag in tag_elements]
            tags_formatted = ", ".join(tags_list) if tags_list else "Uncategorized"

            # Construct unique resource identifier
            article_id = f"ART-2026-{page_idx}0{idx}"

            # Append normalized record dictionary
            article_records.append({
                "Article ID": article_id,
                "Headline / Content": article_title,
                "Author / Contributor": contributor,
                "Taxonomy Tags": tags_formatted,
                "Source Engine": "ToScrape Archive"
            })

    logging.info(f"Harvesting complete. Total articles processed: {len(article_records)}")
    return article_records

def export_articles_to_spreadsheet(records):
    """Serializes harvested article records into an organized Excel workbook."""
    if not records:
        logging.warning("Dataset buffer is empty. Skipping spreadsheet generation.")
        return

    logging.info("Compiling records into pandas DataFrame...")
    dataframe = pd.DataFrame(records)

    # Export buffer directly to disk without internal pandas index numbering
    dataframe.to_excel(OUTPUT_FILENAME, index=False)
    logging.info(f"Pipeline successfully finalized. File saved as: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    harvested_dataset = harvest_blog_articles()
    export_articles_to_spreadsheet(harvested_dataset)
