import pymongo
import pandas as pd

from backend.route import *

from backend.database import *
import math
import os





myclient = pymongo.MongoClient("mongodb://localhost:27017/")


class assign(manage_database):
    def get_collections(self):
            print("assign")
            self.create_divisons(self.userId)
            self.get_Orders(self.col_name)
            self.get_employee(self.col_name)
            self.get_assign(self.col_name)
       

    def assign_orders(self, col_name, userId):
        
        self.col_name = col_name
        self.userId = userId
        self.get_collections()
        print(self.col_name)
        self.free = []
        for doc in self.employee.find():
            self.free.append(doc['_id'])
        # print(self.free)
        districts = self.divide.collection_names()
        total_orders = self.orders.count()
        # print(total_orders)

        # central
        s_d_orders = self.central_delhi.find_one({'_id': self.userId})[self.col_name]
        self.assign.insert({"_id":self.free[0] , "orders":s_d_orders})

        # new
        s_d_orders = self.new_delhi.find_one({'_id': self.userId})[self.col_name]
        self.assign.insert({"_id":self.free[1] , "orders":s_d_orders})

        # east
        s_d_orders = self.east_delhi.find_one({'_id': self.userId})[self.col_name]
        self.assign.insert({"_id":self.free[2] , "orders":s_d_orders})


        # west
        s_d_orders = self.west_delhi.find_one({'_id': self.userId})[self.col_name]
        self.assign.insert({"_id":self.free[3] , "orders":s_d_orders})

        # south
        s_d_orders = self.south_delhi.find_one({'_id': self.userId})[self.col_name]
        self.assign.insert({"_id":self.free[4] , "orders":s_d_orders})

        # south_east
        s_d_orders = self.south_east_delhi.find_one({'_id': self.userId})[self.col_name]
        self.assign.insert({"_id":self.free[5] , "orders":s_d_orders})

        # south_west
        s_d_orders = self.south_west_delhi.find_one({'_id': self.userId})[self.col_name]
        self.assign.insert({"_id":self.free[6] , "orders":s_d_orders})

        # north
        s_d_orders = self.north_delhi.find_one({'_id': self.userId})[self.col_name]
        self.assign.insert({"_id":self.free[7] , "orders":s_d_orders})

        # north_west
        s_d_orders = self.north_west_delhi.find_one({'_id': self.userId})[self.col_name]
        self.assign.insert({"_id":self.free[8] , "orders":s_d_orders})

        
        # north_east
        s_d_orders = self.north_west_delhi.find_one({'_id': self.userId})[self.col_name]
        self.assign.insert({"_id":self.free[9] , "orders":s_d_orders})

        ob = order_route(self.col_name, self.userId)
        
        






        
        

    
        




