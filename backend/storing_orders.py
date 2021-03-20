import pymongo
import pandas as pd
import datetime
# from backend import distribute_data as dd
import backend.distribute_data as dd


# creating a client
myclient = pymongo.MongoClient("mongodb://localhost:27017/")



class store_orders(dd.handle_database):

    def __init__(self):
        print("store_orders")
        self.collection_name = "empty"
        self.cur_time = "d"
        self.userId = "dummy"
        self.date = "00"
        self.hour = "00"
        self.minute = "00"
        

    def create_collection(self):
        self.cur_time = datetime.datetime.now()
        self.date = str(self.cur_time.date())
        self.hour = str(self.cur_time.hour)
        self.minute = str(self.cur_time.minute)
        self.collection_name = self.userId +" "+ self.date +" "+ self.hour + " " + self.minute
        return self.collection_name
      
        
    def create_database(self):
        database = myclient["Orders"]
        return database

    
    def get_file(self, filename, userId):
        self.userId = userId
        self.collection_name = self.create_collection()
        df_orders = pd.read_excel(filename)

        # df_orders = df_orders.to_csv(index = False)
        database = self.create_database()
        db = database[self.collection_name]
        # print(col_name)
        
        
        for i in range(len(df_orders)):
            data = df_orders.iloc[i]
            # print(name.NAME)
            order_data = {  "Name": str(data.NAME),
                            "Item":  str(data.ITEM),
                            "Price": int(data.PRICE),
                            "House_no": str(data.HOUSE_NO),
                            "Locality": str(data.LOCALITY),
                            "District": str(data.DISTRICT),
                            "Town": str(data.TOWN),
                            "Email_id": str(data.EMAIL_ID),
                            "Phone_no": str(data.PHONE_NO),
                            "userId": str(self.userId)
                        }
            x = db.insert_one(order_data)
        
        self.access_database(self.collection_name, self.userId)
    
        
    



