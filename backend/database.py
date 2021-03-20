import pymongo



myclient = pymongo.MongoClient("mongodb://localhost:27017/")


class manage_database:

    def __init__(self):
        self.userId = "dummy"
    
   
    def create_divisons(self, userId):
        self.userId = userId
        self.divide = myclient["divisions"]
        self.central_delhi = self.divide["central_delhi"]
        self.new_delhi = self.divide["new_delhi"]
        self.east_delhi = self.divide["east_delhi"]
        self.west_delhi = self.divide["west_delhi"]
        self.south_delhi = self.divide["south_delhi"]
        self.south_east_delhi = self.divide["south_east_delhi"]
        self.south_west_delhi = self.divide["south_west_delhi"]
        self.north_delhi = self.divide["north_delhi"]
        self.north_west_delhi = self.divide["north_west_delhi"]
        self.north_east_delhi = self.divide["north_east_delhi"]


    def create_documents(self):
        x = self.central_delhi.find_one({"_id" : self.userId})
        if(x == None):
            data =  { "_id": self.userId}
            self.central_delhi.insert(data)
            self.new_delhi.insert(data)
            self.east_delhi.insert(data)
            self.west_delhi.insert(data)
            self.south_delhi.insert(data)
            self.south_east_delhi.insert(data)
            self.south_west_delhi.insert(data)
            self.north_delhi.insert(data)
            self.north_east_delhi.insert(data)
            self.north_west_delhi.insert(data)

    def get_Orders(self, col_name):
        self.o_db = myclient["Orders"]
        self.orders = self.o_db[col_name]
    
    def get_employee(self, col_name):
        self.e_db = myclient["employee"]
        self.employee = self.e_db[self.userId]
 
    def get_assign(self, col_name):
        self.a_db = myclient["assign"]
        self.assign = self.a_db[col_name]
       
    def get_cord(self):
        coordinates = myclient["coordinates"]
        self.towns = coordinates["town"]

    def get_distance(self,col_name):
        self.dist = myclient["distance"]
        self.db = self.dist[col_name]
    
    
    
    
    
    

            
    
        

   

    
