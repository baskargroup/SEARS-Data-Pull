#Write a MongoDB query as a nested dictionary

from datetime import datetime

def my_query():
    
    #Define timestamp range
    start_timestamp = datetime(2024, 1, 1)  # Replace with your start timestamp
    end_timestamp = datetime(2024, 1, 31)   # Replace with your end timestamp
    
    query = {
        
        #Search Criteria - 1
        'experiment_dt' :{
            '$lt': end_timestamp,  #You can also use just dates by using the start_timestamp declared above
            #'$lte': '2020-12-31T23:59:59.000Z'
        },
        #Search Criteria - 2
        'user': 'rtali@iastate.edu'
    }
    
    return query