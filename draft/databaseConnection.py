import pymongo
from pymongo import MongoClient

def connection():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.forbes_billionaires 
    collection = db.billionaires