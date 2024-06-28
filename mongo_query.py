
import pandas as pd
import json
from bson.json_util import dumps

def query_data(db, collection, query={}, projection={}):
    try:
        print('Querying data from MongoDB...')
        _results = db[collection].find(query, projection)  # This is a cursor
        with open('collection.json', 'w') as file:
            json.dump(json.loads(dumps(_results)), file)
    except Exception as e:
        print('Error pulling data from MongoDB:', e)
