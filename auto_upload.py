from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os
import json
import glob
import sys
import time
from time import sleep
from logging_helper import setup_logger


def upload_experiment(json_file_directory):

    # Load .env file
    load_dotenv(find_dotenv())

    # MONGODB SETTINGS OF SEARS
    MONGODB_HOST = os.getenv("CONN_STRING")
    COLLECTION_NAME = 'productData'

    # Connect to MongoDB
    try:
        client = MongoClient(MONGODB_HOST)
        db = client['dope']
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

                    # Insert the data into MongoDB - Key Step
                    collection.insert_one(data)
                    print(f'Experiment {json_file_path} inserted successfully')

                except Exception as e:
                    print(e)

            print('\nAll experiments inserted to SEARS successfully')
            return num_files

    except Exception as e:
        print(e)
        return 0

    finally:
        client.close()


if __name__ == '__main__':

    os.makedirs('./uploads', exist_ok=True)
    os.makedirs('./logs', exist_ok=True)

    if len(sys.argv) < 2:
        print('\n You have decided to run the uploader in auto mode. The program will look for new experiment files every five minutes \n')

        ctrl = True

        while ctrl:

            curr_time = time.ctime()

            # Extract Month and Year from the current time
            curr_month = curr_time.split(' ')[1]
            curr_year = curr_time.split(' ')[-1]

            # Create a logger for every month
            logger = setup_logger(
                f'./logs/auto_upload_{curr_month}_{curr_year}.log')

            logger.info(f'Auto uploader resumed at {curr_time}')

            try:
                # Upload the experiment data
                n_exp = upload_experiment('./uploads')
                logger.info(
                    f' {n_exp} experiments uploaded successfully at {curr_time}')

                # Delete the files after uploading
                files = glob.glob('./uploads/*.json')
                for f in files:
                    os.remove(f)

                logger.info('Experiments deleted successfully from ./uploads')

                # Sleep for 5 minutes
                sleep(300)

            except Exception as e:
                print(e)
                ctrl = False
                logger.error(f'Error: {e}')
                print(
                    f'\nAuto uploader stopped due to an error. Please check the latest log {logger.name} for more information\n')
                logger.info(
                    'Auto uploader stopped due to an error. Please check the latest log for more information\n')

    else:
        if sys.argv[1] == 'cron':
            print('\n You have decided to run the uploader in cron mode. \n')

            curr_time = time.ctime()

            # Extract Month and Year from the current time
            curr_month = curr_time.split(' ')[1]
            curr_year = curr_time.split(' ')[-1]

            # Create a logger for every month
            logger = setup_logger(
                f'./logs/auto_upload_{curr_month}_{curr_year}.log')

            try:
                # Upload the experiment data
                n_exp = upload_experiment('./uploads')
                logger.info(
                    f' {n_exp} experiments uploaded successfully at {curr_time}')

                # Delete the files after uploading
                files = glob.glob('./uploads/*.json')
                for f in files:
                    os.remove(f)

                logger.info('Experiments deleted successfully from ./uploads')

            except Exception as e:
                print(e)
                logger.error(f'Error: {e}')
                print(
                    f'\nAuto uploader encountered an error. Please check the latest log {logger.name} for more information\n')
                logger.info(
                    'Auto uploader encountered an error. Please check the latest log for more information\n')
        else:
            print('\n Invalid argument(s). Please use either cron or dont pass anything. E.g. python3 auto_upload.py or python3 auto_upload.py cron \n')
