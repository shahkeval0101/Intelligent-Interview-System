import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
import os
# import gui.startPage
# import gui.greeting
from gui import startPage
from gui import greeting

LARGEFONT = ("Comic Sans MS", 25, 'bold')
# login details 'boss','1234'
# second window frame page1


class Login(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.configure(bg = '#bdbf41')
        label = ttk.Label(self, text="Login", font=LARGEFONT, background = '#bdbf41', foreground = "#ad2d2d")
        label.grid(row=0, column=4, padx=10, pady=10)

        # this wil create a label widget
        l1 = ttk.Label(self, text="Name:",background = '#bdbf41', foreground = '#e30909',font = ('Verdana', 15, 'bold'))
        l2 = ttk.Label(self, text="Email Id:",background = '#bdbf41', foreground = '#e30909',font = ('Verdana', 15, 'bold'))
        l3 = ttk.Label(self, text="Password:", background = '#bdbf41',foreground = '#e30909', font = ('Verdana',15,'bold'))

        # grid method to arrange labels in respective
        # rows and columns as specified
        l1.place(x = 500, y = 250, height = 30, width = 120)
        l2.place(x = 500, y = 300, height = 30, width = 120)
        # l1.grid(row=1, column=0, sticky="W", pady=2)
        l3.place(x=500, y=350, height = 30, width = 120)

        name_val = tk.StringVar()
        email_val = tk.StringVar()
        password_val = tk.StringVar()

        # entry widgets, used to take entry from user
        name = ttk.Entry(self, textvariable=name_val)
        self.email = ttk.Entry(self, textvariable=email_val)
        password = ttk.Entry(self, textvariable=password_val,show = "*")

        # this will arrange entry widgets
        name.place(x= 650, y=250,height = 30, width = 250)
        self.email.place(x= 650, y=300,height = 30, width = 250)
        password.place(x= 650, y = 350, height = 30, width = 250)

        # button to show frame 2 with text
        # layout2

        """
         button1 = tk.Button(self, text="Login", fg = '#ebe8e9', bg ='#0a0002', font = ('Verdana', 15, 'bold'),
                             command=lambda: controller.show_frame(login.Login))
        
        # putting the button in its place by
        # # using grid
        button1.place(x=675, y=530, height = 50, width = 150)
        """       
        button1 = tk.Button(self, text="StartPage", fg = '#ebe8e9', bg ='#0a0002', font = ('Verdana', 15, 'bold'),
                             command=lambda: controller.show_frame(startPage.StartPage))

        # putting the button in its place
        # by using grid
        button1.place(x=525, y=450,  height = 50, width = 150)

        def checkcred():
            username = email_val.get()
            password1 = password_val.get()
            local_path = os.path.realpath(__file__)
            parent_path = os.path.dirname(os.path.realpath(__file__))
            # print(local_path)
            print(parent_path)
            filename = os.path.join(str(parent_path), "data.db")
            print(filename)

            con = sql.connect(filename)
            print(con)
            cur = con.cursor()
            # statement = "SELECT username from users WHERE username=" + \
            str(username)+" AND Password = "+str(password1)+";"
            statement = "SELECT username from users WHERE username='{}' AND Password = '{}';".format(
                username, password1)
            cur.execute(statement)
            #email.delete(0)
            #password.delete(0)

            if not cur.fetchone():  # An empty result evaluates to False.
                print("Login failed")
                failed = ttk.Label(self, text="Try again details incorrect", foreground = "red",background = '#bdbf41', font = ('Verdana',8) )
                failed.place(x=550, y=410,height = 18, width = 220)
                self.email.delete(0,'end')
                password.delete(0,'end')
                name.delete(0,'end')
                return
            else:
                print("Login Passed")
                self.email.delete(0,'end')
                password.delete(0,'end')
                name.delete(0,'end')
                controller.show_frame(greeting.Greeting)

        # button to show frame 3 with text
        # layout3
        button2 = tk.Button(self, text="Login", fg = '#ebe8e9', bg ='#0a0002', font = ('Verdana', 15, 'bold'),
                             command=checkcred)
        # putting the button in its place by
        # using grid
        button2.place(x=700, y = 450, height = 50, width = 150 )

    def getter(self):
        return self.email.get()

# import helper.checker as chk
# app =chk.Checker(Login)
# app.mainloop()
