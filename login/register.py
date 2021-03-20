from tkinter import*
from tkinter import ttk,messagebox
from PIL import ImageTk, Image #pip install pillow
import pymysql #pip install pymysql
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg = "white")# Setting the background colour
        # Background Image
        self.bg = ImageTk.PhotoImage(file = "images/2.jpg")#object of class
        bg = Label(self.root,image = self.bg).place(x = 80,y = 0,relwidth = 1,relheight = 1)#object of root window

        # Left Image
        self.left = ImageTk.PhotoImage(file = "images/1.jpg")#object of class
        left = Label(self.root,image = self.left).place(x = 80,y = 100,width = 400,height = 500)#object of root window

        #Forming the Registration Frame
        frame1 = Frame(self.root,bg = "white")
        frame1.place(x = 480,y = 100,width = 700,height = 500)
        title = Label(frame1,text = "REGISTER HERE",font = ("times new roman",20,"bold"),bg = "white",fg = "green").place(x = 50,y = 30)

        #---------------------------Row 1
        f_name = Label(frame1,text = "First Name",font = ("times new roman",15,"bold"),bg = "white",fg = "grey").place(x = 50,y = 100)
        #Making an entry field
        self.txt_fname = Entry(frame1,font = ("times new roman",15),bg = "light grey")
        self.txt_fname.place(x = 50,y = 130,width = 250)

        l_name = Label(frame1,text = "Last Name",font = ("times new roman",15,"bold"),bg = "white",fg = "grey").place(x = 370,y = 100)
        self.txt_lname = Entry(frame1,font = ("times new roman",15),bg = "light grey")
        self.txt_lname.place(x = 370,y = 130,width = 250)

        #---------------------------Row 2
        contact = Label(frame1,text = "Contact Number",font = ("times new roman",15,"bold"),bg = "white",fg = "grey").place(x = 50,y = 170)
        self.txt_contact = Entry(frame1,font = ("times new roman",15),bg = "light grey")
        self.txt_contact.place(x = 50,y = 200,width = 250)

        email = Label(frame1,text = "Email Id",font = ("times new roman",15,"bold"),bg = "white",fg = "grey").place(x = 370,y = 170)
        self.txt_email = Entry(frame1,font = ("times new roman",15),bg = "light grey")
        self.txt_email.place(x = 370,y = 200,width = 250)

        #---------------------------Row 3
        question = Label(frame1,text = "Security Question",font = ("times new roman",15,"bold"),bg = "white",fg = "grey").place(x = 50,y = 240)
        self.cmb_question = ttk.Combobox(frame1,font = ("times new roman",13),state = "readonly",justify = CENTER)
        self.cmb_question['value'] = ("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_question.place(x = 50,y = 270,width = 250)
        self.cmb_question.current(0)

        answer = Label(frame1,text = "Answer",font = ("times new roman",15,"bold"),bg = "white",fg = "grey").place(x = 370,y = 240)
        self.txt_answer = Entry(frame1,font = ("times new roman",15),bg = "light grey")
        self.txt_answer.place(x = 370,y = 270,width = 250)

        #---------------------------Row 4
        password = Label(frame1,text = "Password",font = ("times new roman",15,"bold"),bg = "white",fg = "grey").place(x = 50,y = 310)
        self.txt_password = Entry(frame1,font = ("times new roman",15),bg = "light grey")
        self.txt_password.place(x = 50,y = 340,width = 250)

        cpassword = Label(frame1,text = "Confirm Password",font = ("times new roman",15,"bold"),bg = "white",fg = "grey").place(x = 370,y = 310)
        self.txt_cpassword = Entry(frame1,font = ("times new roman",15),bg = "light grey")
        self.txt_cpassword.place(x = 370,y = 340,width = 250)

        #---------------------------Terms And Conditions
        self.var_chk = IntVar()
        check = Checkbutton(frame1,text = "I Agree With Terms And Conditions",variable = self.var_chk,onvalue = 1,offvalue = 0,bg = "white",font = ("times new roman",12)).place(x = 50,y = 380)
        
        self.btn_img = ImageTk.PhotoImage(file = "images/3.jpg")
        btn_register = Button(frame1,image = self.btn_img,bd = 0,cursor = "hand2",command = self.register_data).place(x = 50,y = 420)

        btn_login = Button(self.root,text = "Sign In",command = self.login_window,font = ("times new roman",20),bd = 0,cursor = "hand2").place(x = 350,y = 500,width = 120)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_question.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)

    def login_window(self):
        self.root.destroy()
        #Linking the Login Page To Registration Page
        import login

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmb_question.get() == "Select" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error","All Fields Are Required!",parent = self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error","Password And Confirm Password Should Be Same",parent = self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error","Please Agree To Our Terms And Conditions",parent = self.root)
            
        else:
            try:
                con = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "Nkumar12c@",
                    database = "route_planner"
                )

                cur = con.cursor()
                sql = """CREATE TABLE IF NOT EXISTS employee(
                    f_name VARCHAR(20),
                    l_name VARCHAR(20),
                    contact VARCHAR(10),
                    email VARCHAR(30),
                    question VARCHAR(50),
                    answer VARCHAR(20),
                    password VARCHAR(20)
                )"""
                cur.execute(sql)
                cur.execute("select * from employee where email = %s",self.txt_email.get())
                row = cur.fetchone()
                #print(row)

                if row != None:
                    messagebox.showerror("Error","User Already Exist,try with other Email!",parent = self.root)
                else:
                    cur.execute("INSERT INTO employee(f_name,l_name,contact,email,question,answer,password) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                                            (
                                                self.txt_fname.get(),
                                                self.txt_lname.get(),
                                                self.txt_contact.get(),
                                                self.txt_email.get(),
                                                self.cmb_question.get(),
                                                self.txt_answer.get(),
                                                self.txt_password.get()
                                            ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registered Successfully",parent = self.root)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due To:{str(es)}",parent = self.root)
            
            #self.txt_fname.get()
            #self.txt_lname.get()
            #self.txt_contact.get()
            #self.txt_email.get()
            #self.cmb_question.get()
            #self.txt_answer.get()
            #self.txt_password.get()
            #self.txt_cpassword.get()

root = Tk()
obj = Register(root)
root.mainloop()