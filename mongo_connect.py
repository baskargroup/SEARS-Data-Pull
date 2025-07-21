"""
Goal : The purpose of the script is to demonstrate to a data scientist a way to pull data directly from the MongoDB database for analysis.
How to Use it : Needless to say that the script will need changes as the underlying schema undergoes changes. For illustration purposes, we have placed our MongoDB schema in the sample_schema folder. We encourage future users to use the code below as an example and use an AI agent to adapt this code to fit their own schemas in MongoDB.
"""


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
    # We ensure that if multiple readings are present for an experiment, we return the latest reading.
    if num_rows > 0:
        CON = conductivity[num_rows-1]['reading']
    return CON


def process_thickness(thickness):
    THK = 0.0
    num_rows = len(thickness)
    # We ensure that if multiple readings are present for an experiment, we return the latest reading.
    if num_rows > 0:
        THK = thickness[num_rows-1]['reading']
    return THK


def connect_to_mongo(db_name, search_criteria, output_file_name):

    os.makedirs('./file_fetch', exist_ok=True)

    # Load .env file
    load_dotenv(find_dotenv())

    # MONGODB
    MONGODB_HOST = os.getenv("CONN_STRING")
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

        '''
        We are interested in the following fields:
        - _id
        - experiment_name
        - solvents (CB, DCB, TOL)
        - annealing_temperature
        - conductivity
        - thickness
        
        Given all the experiments, we are interested in the ones that have the search_criteria in the experiment_name field.
        We first pull all the matched documents and then extract the fields we are interested in.
        While some fields can be pulled directly, others require some processing. E.g., the solvents field is an array of dictionaries.
        Processing logic for these complex fields have been implemented in the process_solvents, process_conductivity, and process_thickness functions.
        
        We need to use the find() method with a query to filter the results. This is more efficient than pulling all the documents and then filtering them.
        Ref: https://docs.mongodb.com/manual/reference/method/db.collection.find/
        
        '''
        for doc in collection.find():  # Note that this is not efficient for large datasets. We should use the find() method with a query to filter the results.
            if search_criteria in doc.get('experiment_name'):
                row = []
                row.append(doc.get('_id'))
                row.append(doc.get('experiment_name'))
                row.extend(process_solvents(doc.get('solvents')))
                row.append(doc.get('annealing_temperature'))
                row.append(process_conductivity(doc.get('conductivity')))
                row.append(process_thickness(doc.get('thickness')))

                # Append to DataFrame
                df.loc[len(df)] = row

        # Create a text file with just the experiment ids. These are then used to download the files from Digital Ocean for each experiment
        with open('./file_fetch/payload.txt', 'w') as file:
            for exp_id in df['exp_id']:
                file.write(str(exp_id) + '\n')

        # Save DataFrame to CSV file for downstream ML. Index is set to False to avoid writing the row numbers to the file.
        df.to_csv(output_file_name, index=False)

    except Exception as e:
        print(e)


if __name__ == '__main__':

    db_name = 'dope'
    search_criteria = "Spring24_SolvTemp_JPM"
    output_file_name = "./file_fetch/spring24_solvtemp_jpm.csv"

    connect_to_mongo(db_name=db_name, search_criteria=search_criteria,
                     output_file_name=output_file_name)
