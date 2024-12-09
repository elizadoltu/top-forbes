import json 
import os 
from pymongo import MongoClient
from dotenv import load_dotenv, dotenv_values

load_dotenv()

client = MongoClient(os.getenv('DATABASE_CONNECTION'))
db = client.forbes_billionaires
collection = db.billionaires

def load_billionaires_data(filename="billionaires_data.json"):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "billionaires_data.json".
    """
    
    try: 
        with open(filename, 'r') as f: 
            data = json.load(f)
            print(f"Data loaded from {filename}")
            return data 
    
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None 
    
    except json.JSONDecodeError:
        print(f"Error: {filename} is not a valid JSON file.")
        return None
    
def extract_billionaire_details(billionaire_data):
    """_summary_

    Args:
        billionaire_data (_type_): _description_
    """
    exctracted_data = []
    
    for billionaire in billionaire_data: 
        extracted_billionaire = {
            'Rank': billionaire.get('rank'),
            'First Name': billionaire.get('firstName'),
            'Last Name': billionaire.get('lastName'),
            'Age': billionaire.get('age'),
            'Net Worth': billionaire.get('finalWorth'),
            'Source of Wealth': billionaire.get('source'),
            'City': billionaire.get('city'),
            'Country of Citizenship': billionaire.get('countryOfCitizenship'),
            'Status': billionaire.get('status'),   
            'Title': billionaire.get('title'),
            'Industry': billionaire.get('industries'),
        }
        exctracted_data.append(extracted_billionaire)
    
    return exctracted_data

def save_to_database(data):
    """_summary_

    Args:
        data (_type_): _description_
    """
    try:
        result = collection.insert_many(data)
        print(f"Data saved to database. Inserted IDs: {result.inserted_ids}")
    except Exception as e:
        print(f"Error saving data to database: {e}")
        
if __name__ == "__main__":
    billionaires_data = load_billionaires_data()
    
    if billionaires_data:
        extracted_data = extract_billionaire_details(billionaires_data)
        save_to_database(extracted_data)