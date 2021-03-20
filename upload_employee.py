from tkinter import *
from tkinter.ttk import *
from tkinter import ttk,messagebox
import os
from backend import employee_data as e_data
import backend.storing_orders as sd
from tkinter.filedialog import askopenfile
import threading
import argparse


# parser=argparse.ArgumentParser(description="sample argument parser")
# parser.add_argument("user")
# args = parser.parse_args()

# userId = args.user
userId = "nitish"

employee_file = "employee"
order_file = "order"


# employee_file = "employee"
# order_file = "order"

root = Tk()


root.title("Delivery route Planner")
root.geometry('397x200')
# root['background']='#856ff8'





f1 = Frame(root,width=200,height=200 )
# f1['background'] = "light grey"
f2 = Frame(root,width=200,height=200)
# f2['background'] = "light grey"
f3 = Frame(root)

def raise_frame(frame):
    frame.tkraise()



for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky='news')
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

def open_employee():
    print("da")
    root.filename = askopenfile(title ="select employee file", filetypes = [("xlsx files","*.xlsx")])
    my_label = Label(root, text = root.filename.name)
    global employee_file
    employee_file = str(root.filename.name)
    
        

def open_orders():
    root.filename = askopenfile(title ="select orders file", filetypes = [("xlsx files","*.xlsx")])
    my_label = Label(root, text = root.filename)
    
    global order_file
    order_file = str(root.filename.name)

def thanks():
    lines = ["Thank You for visiting Efficient Delivery System Softwares!!", "The route map will be sent to employees 'e-mail Id as well will be saved on your computer."]
    messagebox.showinfo("Success","\n".join(lines),parent = f2)

style = ttk.Style() 

style.configure('TButton', font =('georgia', 7, 'italic', 'underline'), foreground = 'red',bg = 'blue',borderwidth = '4') 
    
btn = ttk.Button(f1, text ='Upload Employee File', command = lambda: open_employee(),cursor = "hand2",style = 'TButton')
btn.pack(side='top', ipadx=80,ipady = 15, pady=10)

btn2 = ttk.Button(f1, text ='Upload Order File', command = lambda:open_orders(),cursor = "hand2")
btn2.pack(side='top', ipadx=80,ipady = 15, padx=80)


btn3 = ttk.Button(f1, text= "Next", command = lambda: raise_frame(f2),cursor = "hand2")
btn3.pack(side='top', padx=80, ipady = 15,pady=10)


btn2 = ttk.Button(f2, text= "EXIT", command = lambda: [thanks(),root.destroy()],cursor = "hand2") 
btn2.pack(side='top', padx=80, ipady = 20,pady=50)



raise_frame(f1)
try:
	root.mainloop()
except AssertionError as error:
	print(error)
    
print(employee_file)
print(order_file)


e = e_data.Employee_database(employee_file, userId)
e.store_details()
ob1 = sd.store_orders()
ob1.get_file(order_file, userId)
