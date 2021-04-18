from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

import os
import pymongo
import pandas as pd
from queue import Queue


from backend.database import manage_database
# from database import manage_database
from bson import ObjectId
import math
import requests
import gmplot


from opencage.geocoder import OpenCageGeocode
key = "f17e3adbd2fc4d81ac431f466dfcbe87"  
geocoder = OpenCageGeocode(key)

# from assign_orders import *
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
Geolocator = Nominatim(user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")
def distance(cor1, cor2):
        return (geodesic(cor1,cor2).kilometers)

import os
from timeit import default_timer as timer 

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders





myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# df = pd.read_excel('towns.xlsx')

"""Simple travelling salesman problem between cities."""




class route_order:

    def create_data_model(self, arr):
        """Stores the data for the problem."""
        data = {}
        data['distance_matrix'] = arr # yapf: disable
        data['num_vehicles'] = 1
        data['depot'] = 0
        return data


    def print_solution(self, manager, routing, solution):
        """Prints solution on console."""
        print('Objective: {} miles'.format(solution.ObjectiveValue()))
        index = routing.Start(0)
#         plan_output = 'Route for vehicle 0:\n'
        plan_output = ''
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += ' {} ->'.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        plan_output += ' {}\n'.format(manager.IndexToNode(index))
        return plan_output
        plan_output += 'Route distance: {}miles\n'.format(route_distance)


    def start(self,arr):
        """Entry point of the program."""
        # Instantiate the data problem.
        data = self.create_data_model(arr)

        # Create the routing index manager.
        manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                               data['num_vehicles'], data['depot'])

        # Create Routing Model.
        routing = pywrapcp.RoutingModel(manager)


        def distance_callback(from_index, to_index):
            """Returns the distance between the two nodes."""
            # Convert from routing variable Index to distance matrix NodeIndex.
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return data['distance_matrix'][from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        # Define cost of each arc.
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        # Print solution on console.
        if solution:
            h = self.print_solution(manager, routing, solution)
            h = h.strip("\n")
            h = h.replace('->' ,'')
            li = list(h.split(" ")) 
            for i in li:
                if i == '':
                    li.remove(i)
#             li = li.strip('\n')
            return li
            

            

def store_distance(col_name):
    dist = myclient["distance"]
    dis = dist[col_name]
    o_db = myclient["Orders"]
    orders = o_db[col_name]
    o_town = myclient["coordinates"]
    towns = o_town["town"]
    res = requests.get('https://ipinfo.io/')
    data = res.json()

    city = data['city']

    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    cor1 = (latitude, longitude)

    dis.insert_one({"_id":"start"})
    for order in orders.find():
        id2 = order["_id"]
        address2 = order["Town"]
        coord2 = towns.find_one({"town": address2})
        cor2 = (coord2["lat"], coord2["long"])
        displacement = distance(cor1, cor2)
        dis.update_one({"_id": "start"}, {"$set":{str(id2) : displacement}})
    
    print("start done")

    res = requests.get('https://ipinfo.io/')
    data = res.json()

    city = data['city']

    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    cor1 = (latitude, longitude)

    for order in orders.find():
        id = order["_id"]
        address = order["Town"]
        coord = towns.find_one({"town": address})
        cor2 = (coord["lat"], coord["long"])
        dis.insert_one({"_id": order["_id"], "start":distance(cor1, cor2)})


    for order in orders.find():
        id = order["_id"]
        address = order["Town"]
        coord = towns.find_one({"town": address})
        cor1 = (coord["lat"], coord["long"])
        for o_list in orders.find():
            if(o_list["_id"] != id):
                id2 = o_list["_id"]
                address2 = o_list["Town"]
                coord2 = towns.find_one({"town": address2})
                cor2 = (coord2["lat"], coord2["long"])
                displacement = distance(cor1, cor2)
                dis.update_one({"_id": id}, {"$set":{str(id2) : displacement}})




class order_route(manage_database, route_order):
    
    def __init__(self, col_name,userId):
        print("route")
        start = timer() 
        self.userId = userId
        self.col_name  = col_name
        store_distance(self.col_name)
        print("distance storage done")
        self.get_assign(col_name)
        self.get_Orders(col_name)
        self.get_employee(col_name)
        self.create_divisons(col_name)
        self.create_documents()
        self.get_my_location()
        print('got location')
        self.get_cord()
        print('got cord')
        self.get_distance(col_name)
        print('got distance')
        self.userId = userId
        # print(self.userId)
        # print(self.col_name)
        print('got user')
        self.plan()
        print('got plan')
        
        print(" without GPU:", timer()-start)     

    def create_dir(self):
        try:  
            path = "maps\ " + self.userId
            os.mkdir(path)  
        except OSError as error:  
            
            print(error) 


        for doc in self.employee.find():
            try: 
                path = "maps\ " + self.userId +'\ ' + str(doc["_id"])
                os.mkdir(path)
            except OSError as error:
                print(error)

        try:
           for doc in self.employee.find():
                try: 
                    path = "maps\ " + self.userId +'\ ' + str(doc["_id"]) + '\ ' + self.col_name
                    os.mkdir(path)
                except OSError as error:  
                    print(error)

        except OSError as error:
            print(error)

            


    def get_my_location(self):
        res = requests.get('https://ipinfo.io/')
        data = res.json()

        city = data['city']

        location = data['loc'].split(',')
        self.latitude = location[0]
        self.longitude = location[1]

    



    def coordinates(self, address):
        query = str(address)+','+ "Delhi"
        results = geocoder.geocode(query)   
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        cord = (lat, lng)
        return cord
    
    def get_cor_list(self):
        res = requests.get('https://ipinfo.io/')
        data = res.json()

        city = data['city']

        location = data['loc'].split(',')
        latitude = float(location[0])
        longitude = float(location[1])

        cor1 = (latitude, longitude)
        cor_list = [cor1]

        return cor_list


    def plot(self,lat,long, cor_list,final_list,z, empid, email):
        apikey = 'AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8' 
        self.create_dir()
        gmap = gmplot.GoogleMapPlotter(lat, long, 11.7, apikey=apikey)
        attractions = zip(*cor_list)
        final_list.insert(0, "start")
        for x in range(len(final_list)):
            gmap.text(cor_list[x][0], cor_list[x][1], final_list[x], color='yellow')
        gmap.scatter(
            *attractions,
            color=['red']*len(cor_list),
            s=70,
            ew=2,
            marker=[True]*len(cor_list),
            

        )
        
        cor_list.append((lat, long))
        path = zip(*cor_list)
        gmap.plot(*path, edge_width=3, color='pink')  

        file_name = "maps\ " + self.userId + '\ ' + empid + '\ ' + self.col_name + '\ ' + str(z) 
        gmap.draw(file_name + '.html')
        self.send_route_mail(email, file_name)

    

    def send_route_mail(self, email, file_path):
        fromaddr = "nitishkumar12c@gmail.com"
        toaddr = email

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Delivery Route "

        body = "YOUR TODAY'S ROUTE"

        msg.attach(MIMEText(body, 'plain'))

        filename = file_path + '.html'
        attachment = open(filename, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "9711482366")

        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)

        server.quit()

    def plan(self):


        for doc in self.assign.find():
            post_id = str(doc["_id"])
           
            emp_id = doc["_id"]
            email = self.employee.find_one({"_id": ObjectId(post_id)})["EMAIL_ID"]
            o_list = ["start"]
            o_list = o_list + doc["orders"]
            z = math.ceil(len(o_list)/10)
            o_list.pop(0)
            print("1")
            for k in range(z):
                n_list = ['start']
                while(len(n_list)!= 11):
                    if(len(o_list) == 0):
                        break
                    n_list.append(o_list.pop(0))
            
                arr = []
                
                for i in range(len(n_list)):
                    col = []
                    doc = self.db.find_one({"_id": n_list[i]})
                    
                   
                    for j in range(len(n_list)):
                        if(i == j):
                            col.append(0)
                        else:
                           
                            col.append(doc[str(n_list[j])])
                    arr.append(col)

                print(arr)               
                li = self.start(arr)
                final_list = []
                for i in range(len(n_list)):
                    final_list.append(n_list[int(li[i])])
            
                cor_list = self.get_cor_list()
                final_list.pop(0)

                for x in final_list:
                    doc = self.orders.find_one({"_id": x})
                    address = doc["Town"]
                    
                    cord = self.towns.find_one({"town": address})
                    lat = cord["lat"]
                    long = cord["long"]
                    cor_list.append((lat, long))
                
                self.plot(cor_list[0][0], cor_list[0][1],cor_list,final_list,k, post_id,email)
                print("2")
                print(final_list)
                
                

