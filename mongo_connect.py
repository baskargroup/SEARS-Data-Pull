from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os
import pandas as pd


def process_solvents(solvents):
    CB = 0.0
    DCB = 0.0
    TOL = 0.0
    for solvent in solvents:
        if solvent['name'] == 'CB':
            CB = solvent['value']
        elif solvent['name'] == 'DCB':
            DCB = solvent['value']
        elif solvent['name'] == 'Tol':
            TOL = solvent['value']

    return [CB, DCB, TOL]


def process_conductivity(conductivity):
    CON = 0.0
    num_rows = len(conductivity)
    if num_rows > 0:
        CON = conductivity[num_rows-1]['reading']
    return CON


def process_thickness(thickness):
    THK = 0.0
    num_rows = len(thickness)
    if num_rows > 0:
        THK = thickness[num_rows-1]['reading']
    return THK


def connect_to_mongo(db_name, search_criteria, output_file_name):
    # Load .env file
    load_dotenv(find_dotenv())

    # MONGODB
    CONN_STRING = os.environ.get('MONGO_URI')
    # print(CONN_STRING)
    MONGODB_HOST = 'mongodb+srv://rtali:vqPi8ORyWQJGdJbs@isu.wet0vxf.mongodb.net/?appName=ISU'
    MONGODB_PORT = 27017
    DB_NAME = 'dope'
    COLLECTION_NAME = 'productData'

    # Create a DataFrame
    df = pd.DataFrame(columns=['exp_id', 'experiment_name', 'CB', 'DCB',
                      'TOL', 'annealing_temperature', 'conductivity', 'thickness'])

    # Connect to MongoDB
    try:
        client = MongoClient(MONGODB_HOST)
        db = client[db_name]
        print('Connected to MongoDB')
        collection = db[COLLECTION_NAME]

        for doc in collection.find():
            if search_criteria in doc.get('experiment_name'):
                row = []
                row.append(doc.get('_id'))
                row.append(doc.get('experiment_name'))
                row.extend(process_solvents(doc.get('solvents')))
                row.append(doc.get('annealing_temperature'))
                row.append(process_conductivity(doc.get('conductivity')))
                row.append(process_thickness(doc.get('thickness')))

                # Append to DataFrame and index is false
                df.loc[len(df)] = row

        # Create a text file with just the experiment ids. These are then used to download the files from Digital Ocean for each experiment
        with open('./file_fetch/payload.txt', 'w') as file:
            for exp_id in df['exp_id']:
                file.write(str(exp_id) + '\n')

        # Save DataFrame to CSV
        df.to_csv(output_file_name, index=False)

    except Exception as e:
        print(e)


if __name__ == '__main__':

    db_name = 'dope'
    search_criteria = "Spring24_SolvTemp_JPM"
    output_file_name = "./file_fetch/spring24_solvtemp_jpm.csv"

    connect_to_mongo(db_name=db_name, search_criteria=search_criteria,
                     output_file_name=output_file_name)
