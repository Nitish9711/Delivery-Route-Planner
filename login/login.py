from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
from tkinter import messagebox,ttk
import pymysql
import os #new
class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg = "#856ff8")

        #----------Background Colours----------
        left_lbl = Label(self.root,bg = "#856ff8")
        left_lbl.place(x = 0,y = 0,relheight = 1,width = 675)

        right_lbl = Label(self.root,bg = "violet")
        right_lbl.place(x = 675,y = 0,relheight = 1,relwidth = 1)
        
        #----------Frames----------
        login_frame = Frame(self.root,bg = "white")
        login_frame.place(x = 250,y = 100,width = 800,height = 500)

        title = Label(login_frame,text = "LOGIN HERE",font = ("times new roman",30,"bold"),bg = "white",fg = "#08A3D2").place(x = 250,y = 50)

        email = Label(login_frame,text = "EMAIL ADDRESS",font = ("times new roman",18,"bold"),bg = "white",fg = "Grey").place(x = 250,y = 150)
        self.txt_email = Entry(login_frame,font = ("times new roman",15),bg = "light grey")
        self.txt_email.place(x = 250,y = 180,width = 350,height = 35)

        password = Label(login_frame,text = "PASSWORD",font = ("times new roman",18,"bold"),bg = "white",fg = "Grey").place(x = 250,y = 250)
        self.txt_password = Entry(login_frame,font = ("times new roman",15),bg = "light grey")
        self.txt_password.place(x = 250,y = 280,width = 350,height = 35)

        reg_btn = Button(login_frame,text = "Register New Account?",command = self.register_window,font = ("times new roman",14),bg = "white",bd = 0,fg = "#B00857",cursor = "hand2").place(x = 243,y = 330)
        btn_forget = Button(login_frame,text = "Forgot Password?",command = self.forget_password_window,font = ("times new roman",14),bg = "white",bd = 0,fg = "red",cursor = "hand2").place(x = 450,y = 330)

        reg_login = Button(login_frame,text = "Login",command = self.login,font = ("times new roman",20,"bold"),fg = "white",bg = "#B00857",cursor = "hand2").place(x = 250,y = 380,width = 180,height = 40)

        #----------Clock----------
        self.lbl = Label(self.root,text = "\nTime",font = ("book antiqua",25,"bold"),fg = "white",compound = BOTTOM,bg = "black",bd = 20,relief = RAISED)
        self.lbl.place(x = 90,y = 120,height = 450,width = 350)
        #self.clock_image()
        self.working()

    def reset(self):
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.cmb_question.current(0)
        self.txt_answer.delete(0,END)
        self.txt_new_password.delete(0,END)

    def forget_password(self):
        if self.cmb_question.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_password.get() == "":
            messagebox.showerror("Error","All Fields Are Required!",parent = self.root2)
        else:
            try:
                con = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "12345678",
                    database = "route_planner"
                )
                cur = con.cursor()
                cur.execute("select * from employee where email = %s and question = %s and answer = %s",(self.txt_email.get(),self.cmb_question.get(),self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please Enter Valid Credentials",parent = self.root2)
                else:
                    cur.execute("update employee set password = %s where email = %s",(self.txt_new_password.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password Successfully Updated!",parent = self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent = self.root)

    def forget_password_window(self):
        if self.txt_email.get() == "":
            messagebox.showerror("Error","Please Enter an email address to reset your Password",parent = self.root)
        else:
            try:
                con = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "Nkumar12c@",
                    database = "route_planner"
                )
                cur = con.cursor()
                cur.execute("select * from employee where email = %s",self.txt_email.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please Enter A valid email address to reset your Password",parent = self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("360x400+490+150")
                    self.root2.config(bg = "white")
                    self.root.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2,text = "Forget Password",font = ("times new roman",20,"bold"),bg = "white",fg = "red").place(x = 0,y = 10,relwidth = 1)

                    #---------------------------Forget Password
                    question = Label(self.root2,text = "Security Question",font = ("times new roman",15,"bold"),bg = "white",fg = "grey").place(x = 50,y = 100)
                    self.cmb_question = ttk.Combobox(self.root2,font = ("times new roman",13),state = "readonly",justify = CENTER)
                    self.cmb_question['value'] = ("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_question.place(x = 50,y = 130,width = 250)
                    self.cmb_question.current(0)

                    answer = Label(self.root2,text = "Answer",font = ("times new roman",15,"bold"),bg = "white",fg = "grey").place(x = 50,y = 180)
                    self.txt_answer = Entry(self.root2,font = ("times new roman",15),bg = "light grey")
                    self.txt_answer.place(x = 50,y = 210,width = 250)

                    new_password = Label(self.root2,text = "New Password",font = ("times new roman",15,"bold"),bg = "white",fg = "grey").place(x = 50,y = 260)
                    self.txt_new_password = Entry(self.root2,font = ("times new roman",15),bg = "light grey")
                    self.txt_new_password.place(x = 50,y = 290,width = 250)

                    btn_change_pass = Button(self.root2,text = "Reset Password",command = self.forget_password,font = ("times new roman",15,"bold"),bg = "green",fg = "white").place(x = 100,y = 340)

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent = self.root)
                print(es)
            
    def register_window(self):
        self.root.destroy()
        #Linking the Registration Page To Login Page
        import register
    
    def login(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error","All Fields Are Required",parent = self.root)
        else:
            try:
                con = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "Nkumar12c@",
                    database = "route_planner"
                )
                cur = con.cursor()
                cur.execute("select * from employee where email = %s and password = %s ",(self.txt_email.get(),self.txt_password.get()))
                row = cur.fetchone()
                print(row)
                if row == None:
                    messagebox.showerror("Error","Invalid Username or Password",parent = self.root)
                else:
                    messagebox.showinfo("Success","Welcome You will be directed to upload_details window in a moment",parent = self.root)
                    path_parent = os.path.dirname(os.getcwd())
                    os.chdir(path_parent)
                    # user = self.txt_email.get()
                    cmd = "python upload_employee.py "+ str(row[2])
                    # python argparser1.py Admin
                    root.destroy()
                    os.system(cmd)
                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent = self.root)
    
    def clock_image(self,hr,min_,sec):
        clock = Image.new("RGB",(400,400),(8,25,35))
        draw = ImageDraw.Draw(clock)
        
        #Formation of Clock Image.
        bg = Image.open("images/new.jpg")
        bg = bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        
        #Formula to rotate the clock in AntiClockwise Direction
        #angle_in_radians = angle_in_degrees * math.pi/180
        #line_length = 100
        #center_x = 250
        #center_y = 250
        #end_x = center_x - line_length * math.cos(angle_in_radians)
        #end_y = center_y + line_length * math.sin(angle_in_radians)

        #Formation of Hour Line Image.
        origin = 200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill = "#DF005E",width = 3)
        #Formation of Minute Line Image.
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill = "white",width = 3)
        #Formation of Second Line Image.
        draw.line((origin,200+100*sin(radians(sec)),200-100*cos(radians(sec))),fill = "yellow",width = 2)
        #Forming Center of The Clock
        draw.ellipse((195,195,210,210),fill = "#1AD5D5")
        clock.save("images/clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second
        hr = (h/12)*360
        min_ = (m/60)*360
        sec = (s/60)*360
        self.clock_image(hr,min_,sec)
        self.img = ImageTk.PhotoImage(file = "images/clock_new.png")
        self.lbl.config(image = self.img)
        self.lbl.after(200,self.working)

root = Tk()
obj = Login_Window(root)
root.mainloop()