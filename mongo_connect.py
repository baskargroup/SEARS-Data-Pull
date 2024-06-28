from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os


def connect_to_mongo(db_name):
    # Load .env file
    load_dotenv(find_dotenv())

    # MONGODB
    CONN_STRING = os.environ.get('MONGO_URI')
    print(CONN_STRING)
    MONGODB_HOST = 'rtali:vqPi8ORyWQJGdJbs@isu.wet0vxf.mongodb.net'
    MONGODB_PORT = 27017
    DB_NAME = 'dope'
    COLLECTION_NAME = 'productData'

    # Connect to MongoDB
    try:

        # client = MongoClient(CONN_STRING)
        # client = MongoClient(MONGODB_HOST,serverSelectionTimeoutMS=10000)

        client = MongoClient(CONN_STRING)
        db = client[db_name]
        print('Connected to MongoDB')
        collection = db[COLLECTION_NAME]
        for doc in collection.find():
            print(doc.get('experiment_name'))
    except Exception as e:
        print('Error connecting to MongoDB:', e)


if __name__ == '__main__':
    db_name = 'dope'
    connect_to_mongo(db_name=db_name)
