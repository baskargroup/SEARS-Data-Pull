from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os

def connect_to_mongo(db_name):
    # Load .env file
    load_dotenv(find_dotenv())

    #Connection String
    CONN_STRING = os.environ.get('MONGO_URI')

    # Connect to MongoDB
    try:
        print('Connecting to MongoDB...')
        client = MongoClient(CONN_STRING)
        db = client[db_name]
        print('Connected to MongoDB')
        return db
    except Exception as e:
        print('Error connecting to MongoDB:', e)