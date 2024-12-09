import os 
from pymongo import MongoClient

def how_many_us_citizenship():
    """Returns the number of billionaires with US citizenship"""
    
    client = MongoClient(os.getenv('DATABASE_CONNECTION'))
    db = client.forbes_billionaires
    collection = db.billionaires
    
    american_citizens = 0 
    non_american_citizens = 0
    
    billionaires = collection.find({})
    
    for billionaire in billionaires: 
        citizenship = billionaire.get('Country of Citizenship')
        if 'United States' in citizenship:
            american_citizens += 1
        else:
            non_american_citizens += 1
            
    if not os.path.exists('auto'):
        os.makedirs('auto')
        
    result = f"American Citizens: {american_citizens}\nNon-American Citizens: {non_american_citizens}"
    
    with open('auto/us_citizenship.txt', 'w') as f:
        f.write(result)
        
    print(f"Data saved to auto/us_citizenship.txt")
    
if __name__ == "__main__":
    how_many_us_citizenship()