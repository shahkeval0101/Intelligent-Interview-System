import tkinter as tk
from tkinter import ttk

LARGEFONT =("Verdana", 35)


# use this to check indivisual pages
# add this code at the end of your page

# import helper.checker as chk
# app =chk.Checker(MODULE CLASS TO BE CHECKED)
# app.mainloop()

class Checker(tk.Tk):
    
    # __init__ function for class tkinterApp
    def __init__(self,Page, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        width= self.winfo_screenwidth() //2
        height= self.winfo_screenheight()//2
        self.geometry("%dx%d" % (width, height))

        container = tk.Frame(self)
        container.pack(side = "right", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        
        # for F in (startPage.StartPage,login.Login, greeting.Greeting):

        #     frame = F(container, self)

        #     # initializing frame of that object from
        #     # startpage, page1, page2 respectively with
        #     # for loop
        #     self.frames[F] = frame

        #     frame.grid(row = 0, column = 0, sticky ="nsew")

        # self.show_frame(startPage.StartPage)

        # MY CODE
        frame = Page(container, self)
        self.frames[Page] = frame
        frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(Page)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame startpage

        
# # Driver Code
# app = Checker()
# app.mainloop()
