import pandas as pd
from mongo_connect import connect_to_mongo
from mongo_query import query_data
from query import my_query
from projection import my_projection

if __name__ == '__main__':
    
    # Connect to MongoDB
    db = connect_to_mongo('dope')
   
    #Pull Query and Projection
    _query = my_query()
    _projection = my_projection()
    
    #Get result and convert to DataFrame
    _result = query_data(db, 'productData', _query, _projection)
    df = pd.DataFrame(list(_result))
    print(df.head())
