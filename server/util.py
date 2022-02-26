import pickle
import json
from statistics import mode
import numpy as np
import sklearn

locations = None
data_columns = None
model = None

def get_estimated_price(sqft,bath,bhk,avail,furnish,trans,location):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1
    avail_index  = data_columns.index(avail)
    
    
    furnish_index  = data_columns.index(furnish)


    trans_index  = data_columns.index(trans)

    x = np.zeros(len(data_columns))
    x[0]= sqft
    x[1]= bath
    x[2]= bhk
    if loc_index >= 0:
        x[loc_index]=1
    if avail_index>=0:
        x[avail_index]=1
    if furnish_index>=0:
        x[furnish_index]=1
    if trans_index>=0:
        x[trans_index]=1
    return round(model.predict([x])[0],2)

def load_saved_arfifacts():
    print("LOADING saved artifacts.........>>>>>")
    global data_columns
    global locations

    with open("server/artifacts/bhopal_colums.json","r") as f:
        data_columns = json.load(f)["data_columns"]
        locations = data_columns[11:]

    global model
    with open("server/artifacts/fixedbpl.pickle","rb") as f:
        model = pickle.load(f)
    print("Loading Artifacts Donee....>>>")

def get_location_names():
    return locations

def get_data_columns():
    return data_columns
if __name__ == '__main__':
    load_saved_arfifacts()
    # print(get_location_names())
    print(data_columns.index('resale'))
    print(get_estimated_price(1000,2,2,'ready to move','furnished','resale','kolar road'))
# "availability",
#  "furnishing_details",
#   "transaction_details", 
#   "bathroom", 
#   "balcony", 
#   "bhk",
#    "total_sqft",