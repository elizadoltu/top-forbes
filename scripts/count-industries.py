from pymongo import MongoClient
from dotenv import load_dotenv
import os 

load_dotenv()

client = MongoClient(os.getenv('DATABASE_CONNECTION'))
db = client.forbes_billionaires
collection = db.billionaires

def count_industries(filename="industry_counts.txt"):
    try:
        if not os.path.exists('auto'):
            os.makedirs('auto')

        file_path = os.path.join('auto', filename)

        pipeline = [
            {
                "$unwind": "$Industry", 
            },
            {
                "$group": { "_id": "$Industry", "count": { "$sum": 1 } }  
            },
            {
                "$sort": {"count": -1}  
            }
        ]
        
        result = collection.aggregate(pipeline)
        
        with open(file_path, 'w') as file:
            for industry in result:
                file.write(f"Industry: {industry['_id']}, Count: {industry['count']}\n")
        
        print(f"Industry counts saved to {file_path}")
    
    except Exception as e:
        print(f"Error saving industry counts: {e}")
        
if __name__ == "__main__":
    count_industries()
