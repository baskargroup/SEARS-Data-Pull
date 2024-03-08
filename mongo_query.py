
import pandas as pd

def query_data(db, collection, query = {}, projection={}):
    try:
        print('Querying data from MongoDB...')
        _results = db[collection].find(query, projection)
        print('Data pulled from MongoDB')
        return _results
    except Exception as e:
        print('Error pulling data from MongoDB:', e)

    