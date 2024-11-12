import time
import pandas as pd
from io import StringIO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Path to your WebDriver (customize this path)
driver_path = 'C:\\selenium\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Mapping URLs to their specific table IDs
url_to_table_id = {
    "https://fbref.com/en/comps/676/stats/UEFA-Euro-Stats": "stats_standard",
    "https://fbref.com/en/comps/676/shooting/UEFA-Euro-Stats": "stats_shooting",
    "https://fbref.com/en/comps/676/passing/UEFA-Euro-Stats": "stats_passing",
    "https://fbref.com/en/comps/676/defense/UEFA-Euro-Stats": "stats_defense",
    "https://fbref.com/en/comps/676/possession/UEFA-Euro-Stats": "stats_possession",
    "https://fbref.com/en/comps/676/misc/UEFA-Euro-Stats": "stats_misc"
}

urls = list(url_to_table_id.keys())

# Loop through each URL and save each table to a separate Excel file
for i, url in enumerate(urls):
    print(f"Scraping data from: {url}")
    driver.get(url)

    # Scroll to the bottom to ensure player stats table is loaded
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Wait for the content to load

    try:
        table_id = url_to_table_id.get(url)
        if not table_id:
            print(f"No table ID found for URL: {url}")
            continue
            
        # Wait for the specific player stats table to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, table_id))
        )

        # Parse the page with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find("table", {"id": table_id})

        if table:
            html_str = str(table)
            df = pd.read_html(StringIO(html_str))[0]

            # Flatten MultiIndex columns if present
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = ['_'.join(col).strip() for col in df.columns.values]

            # Generate a unique filename based on the index
            filename = f'fbref_player_stats_{i+1}.xlsx'
            
            # Save the DataFrame to Excel
            df.to_excel(filename, index=False)
            print(f"Data from {url} saved to {filename}")
        else:
            print(f"Player stats table not found on {url}")

    except Exception as e:
        print(f"Failed to scrape data from {url} due to: {e}")

# Close the WebDriver after processing all URLs
driver.quit()
