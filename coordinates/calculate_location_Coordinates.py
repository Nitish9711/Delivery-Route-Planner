import pandas as pd
# pandas.__version__

import pymongo



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
coordinates = myclient["coordinates"]
town = coordinates["town"]
df_towns = pd.read_excel('towns.xlsx',index_col = 0)

from opencage.geocoder import OpenCageGeocode
key = "f17e3adbd2fc4d81ac431f466dfcbe87"  
geocoder = OpenCageGeocode(key)

list_lat = []   # create empty lists
list_long = []

for index, row in df_towns.iterrows(): # iterate over rows in dataframe
    
    Town = row['Name']
    query = str(Town)+','+ "Delhi"

    results = geocoder.geocode(query)   
    lat = results[0]['geometry']['lat']
    long = results[0]['geometry']['lng']
    cor = {"coordinate": (lat, long)}
    town.insert_one(cor)
    list_lat.append(lat)
    list_long.append(long)

	
# create new columns from lists    

df_towns['latitude'] = list_lat   

df_towns['longitude'] = list_long

df_towns.to_excel("towns.xlsx")