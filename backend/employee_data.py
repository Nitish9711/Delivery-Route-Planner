import pymongo
import pandas as pd



myclient = pymongo.MongoClient("mongodb://localhost:27017/")

class Employee_database:
    
    def __init__(self, file_name, userId):
        self.file_name = file_name
        self.userId = userId


    def create_employee_database(self):
        self.employee = myclient["employee"]

        self.ed_name = str(self.userId)
        self.ec = self.employee[self.ed_name]
    
    
    def store_details(self):
        self.create_employee_database()
        df_emp = pd.read_excel(self.file_name)
 
        for i in range(len(df_emp)):
            data = df_emp.iloc[i]
            employee_data ={
                            "NAME": str(data.NAME),
                            "PHONE_NO": str(data.PHONE_NO),
                            "ADDRESS" : str(data.ADDRESS),
                            "EMAIL_ID": str(data.EMAIL_ID)
                            }
            if self.ec.find_one(employee_data) == None:
                self.ec.insert_one(employee_data)

