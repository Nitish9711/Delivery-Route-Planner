import pymongo
import pandas as pd
from queue import Queue
from backend import database as dm
from backend import assign_orders as ao


myclient = pymongo.MongoClient("mongodb://localhost:27017/")



class Queue:
    def __init__(self):
        self.queue = list()
    
    def push(self, data):
        self.queue.append(data)

    def pop_q(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            print("queue is already empty")
    
    def peek(self):
        try:
            return self.queue[0]
        except IndexError:
            print("queue is already empty")

    
    def show(self):
        print(self.queue)



q = Queue()

class handle_database(Queue,  ao.assign):

    def __init__(self):
        self.col_name = "collection"
        self.Orders  = myclient.local
        self.db = self.Orders["startup_log"]
        self.cnt = 0
        self.userId = "dummy"
    
    def access_database(self , collection_name, userId):
        self.Orders = myclient.Orders
        self.col_name = collection_name
        self.userId = userId
        self.db  = self.Orders[self.col_name]
        self.cnt = self.db.count()
      
        for doc in self.db.find():
            ObjectId = doc['_id']
            
            q.push(ObjectId)
        
        self.seperate()
    
    def seperate(self):
        central = []
        north = []
        north_west = []
        north_east = []
        south = []
        south_west =[]
        south_east = []
        east = []
        west = []
        new_delhi = []
        print("seperate")
        self.create_divisons(self.userId)
        self.create_documents()
        for i in range(self.cnt):
            ObjectId = q.pop_q()
            # print(ObjectId)
            doc = self.db.find_one({"_id": ObjectId})['District']
            doc = doc.lower()
            if(doc == "central"):
                central.append(ObjectId)
            elif(doc == "north"):
                north.append(ObjectId)
            elif(doc == "north west"):
                north_west.append(ObjectId)
            elif(doc == "north east"):
                north_east.append(ObjectId)
            elif(doc == "south"):
                south.append(ObjectId)
            elif(doc == "south west"):
                south_west.append(ObjectId)
            elif(doc == "south east"):
                south_east.append(ObjectId)
            elif(doc == "west"):
                west.append(ObjectId)
            elif(doc == "east"):
                east.append(ObjectId)
            elif(doc == "new delhi"):
                new_delhi.append(ObjectId)
            

        data = {self.col_name : central}
        myquery = { "_id": self.userId }
        newvalues = { "$set": data}
        self.central_delhi.update_one(myquery, newvalues)
        
        data = {self.col_name : north}
        myquery = { "_id": self.userId }
        newvalues = { "$set": data}
        self.north_delhi.update_one(myquery, newvalues)

        data = {self.col_name : north_west}
        myquery = { "_id": self.userId }
        newvalues = { "$set": data}
        self.north_west_delhi.update_one(myquery, newvalues)
        
        data = {self.col_name : north_east}
        myquery = { "_id": self.userId }
        newvalues = { "$set": data}
        self.north_east_delhi.update_one(myquery, newvalues)

        data = {self.col_name : south}
        myquery = { "_id": self.userId }
        newvalues = { "$set": data}
        self.south_delhi.update_one(myquery, newvalues)

        data = {self.col_name : south_east}
        myquery = { "_id": self.userId }
        newvalues = { "$set": data}
        self.south_east_delhi.update_one(myquery, newvalues)

        data = {self.col_name : south_west}
        myquery = { "_id": self.userId }
        newvalues = { "$set": data}
        self.south_west_delhi.update_one(myquery, newvalues)

        data = {self.col_name : east}
        myquery = { "_id": self.userId }
        newvalues = { "$set": data}
        self.east_delhi.update_one(myquery, newvalues)

        data = {self.col_name : west}
        myquery = { "_id": self.userId }
        newvalues = { "$set": data}
        self.west_delhi.update_one(myquery, newvalues)

        data = {self.col_name : new_delhi}
        myquery = { "_id": self.userId }
        newvalues = { "$set": data}
        self.new_delhi.update_one(myquery, newvalues)
        
        self.start_assigning()

    def start_assigning (self):
        self.assign_orders(self.col_name, self.userId)
        
        
        
        

    
        


        



