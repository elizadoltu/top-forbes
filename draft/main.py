import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
from bs4 import BeautifulSoup
import os 
from dotenv import load_dotenv, dotenv_values

load_dotenv()

client = MongoClient(os.getenv('DATABASE_CONNECTION'))
db = client.forbes_billionaires
collection = db.billionaires

try:
    collections = db.list_collection_names()
    print("Connected to MongoDB Atlas. Collections available:", collections)
except Exception as e:
    print(f"Error connecting to the database: {e}")
    exit()

def scrape_forbes_list():
    options = Options()
    options.headless = True
    
    driver = webdriver.Chrome(service=Service('C:/Users/ELIZA/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe'), options=options)
    
    url = "https://www.forbes.com/billionaires/"
    driver.get(url)
    
    time.sleep(5)  

    page_source = driver.page_source

    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')

    billionaires_data = []

    for index, item in enumerate(soup.find_all('div', class_='Table_tableRow__lF_cY'), start=1):
        if index > 200:
            break 
        
        rank = item.find('div', class_='Table_rank__X4MKf')
        name = item.find('div', class_='Table_personName__Bus2E')
        net_worth = item.find('div', class_='Table_finalWorth__UZA6k').find('span') if item.find('div', class_='Table_finalWorth__UZA6k') else None
        age = item.find('div', class_='Table_age__o46g3') if item.find('div', class_='Table_age__o46g3') else None
        country = item.find('div', class_='Table_country__h8clA')
        company = item.find('div', class_='Table_company__tHdb7')

        if rank and name and net_worth and country and company:
            print(f"Rank: {rank.text.strip()}, Name: {name.text.strip()}, Net Worth: {net_worth.text.strip() if net_worth else 'N/A'}, Age: {age.text.strip() if age else 'N/A'}, Country: {country.text.strip()}, Company: {company.text.strip()}")

        if rank and name and net_worth and country and company:
            billionaire = {
                'rank': rank.text.strip(),
                'name': name.text.strip(),
                'net_worth': net_worth.text.strip() if net_worth else 'N/A',
                'age': age.text.strip() if age else 'N/A',
                'country': country.text.strip(),
                'company': company.text.strip()
            }
            billionaires_data.append(billionaire)

    if billionaires_data:
        try:
            collection.insert_many(billionaires_data)
            print(f"Inserted {len(billionaires_data)} billionaires into the database.")
        except Exception as e:
            print(f"Error inserting data into MongoDB: {e}")
    else:
        print("No data found to insert.")

if __name__ == "__main__":
    scrape_forbes_list()
