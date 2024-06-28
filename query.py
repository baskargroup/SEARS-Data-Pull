# Write a MongoDB query as a nested dictionary

from datetime import datetime


def my_query():

    # Define timestamp range
    start_timestamp = datetime(2024, 1, 1)  # Replace with your start timestamp
    end_timestamp = datetime(2024, 3, 31)   # Replace with your end timestamp

    query = {

        # Search Criteria - 1
        'experiment_dt': {
            # You can also use just dates by using the start_timestamp declared above
            '$lt': end_timestamp,
            # '$lte': '2020-12-31T23:59:59.000Z'
        },
        # Search Criteria - 2
        'experiment_name': {
            '$regex': '.*Spring24_SolvTemp_JPM.*',  # Replace with your search string
            '$options': 'i'  # Case-insensitive search
        },
    }

    return query
