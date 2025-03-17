from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os
import json
import glob


def upload_experiment(json_file_directory):

    # Load .env file
    load_dotenv(find_dotenv())

    # MONGODB
    MONGODB_HOST = os.getenv("CONN_STRING")
    COLLECTION_NAME = 'productData'

    # Connect to MongoDB
    try:
        client = MongoClient(MONGODB_HOST)
        db = client['productData']
        print('Connected to SEARS backend')
        collection = db[COLLECTION_NAME]

        files = glob.glob(json_file_directory + '/*.json')
        num_files = len(files)

        if num_files == 0:
            print('No files to upload')

        else:
            print(f'Uploading {num_files} experiments to SEARS...')

            for json_file_path in files:
                try:
                    # Read the JSON file
                    with open(json_file_path, 'r') as file:
                        data = json.load(file)

                    # Insert the data into MongoDB
                    collection.insert_one(data)
                    print('Data inserted successfully')

                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)

    finally:
        client.close()

    print('All data inserted successfully')


if __name__ == '__main__':

    try:
        # Upload the experiment data
        upload_experiment('./uploads')

        # Delete the files after uploading
        files = glob.glob('./uploads/*.json')
        for f in files:
            os.remove(f)

    except Exception as e:
        print(e)
