import os
from pymongo import MongoClient

def get_top_10_youngest_billionaires():
    """Returns the top 10 youngest billionaires from the database"""
    
    client = MongoClient(os.getenv('DATABASE_CONNECTION'))
    db = client.forbes_billionaires
    collection = db.billionaires
    
    try:
        youngest_billionaires = collection.find({}).sort("Age", 1).limit(10)
        
        result = []
        
        for billionaire in youngest_billionaires:
            line = (f"Rank: {billionaire.get('Rank')}, "
                    f"First Name: {billionaire.get('First Name')}, "
                    f"Last Name: {billionaire.get('Last Name')}, "
                    f"Age: {billionaire.get('Age')}, "
                    f"Source Of Wealth: {billionaire.get('Source of Wealth')}, "
                    f"Net Worth: {billionaire.get('Net Worth')}, "
                    f"Residence: {billionaire.get('Residence')}, "
                    f"Citizenship: {billionaire.get('Citizenship')}, "
                    f"Marital Status: {billionaire.get('Marital Status')}, "
                    f"Children: {billionaire.get('Children')}, "
                    f"Education: {billionaire.get('Education')}"
                )
            result.append(line)

        folder = "auto"
        os.makedirs(folder, exist_ok=True) 
        
        file = os.path.join(folder, "top_10_youngest_billionaires.txt")
        
        with open(file, 'w') as f:
            f.write("\n".join(result))
            
        print(f"Data saved to {file}")
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    get_top_10_youngest_billionaires()
