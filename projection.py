#Write a MongoDB projection as a dictionary
#Specify the fields you want to include in the result

def my_projection():
    
    projection = {
        '_id': 1,
        'timestamp': 1,
        'sol_CB': 1,
        'sol_oDCB': 1
    }
    
    return projection
    