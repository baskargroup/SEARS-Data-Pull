# Write a MongoDB projection as a dictionary
# Specify the fields you want to include in the result

def my_projection():

    projection = {
        '_id': 1,
        # 'timestamp': 1,
        # 'solvents': 1,
        # 'annealing_temperature': 1,
        # 'conductivity': 1,
        # 'thickness': 1
    }

    return projection
