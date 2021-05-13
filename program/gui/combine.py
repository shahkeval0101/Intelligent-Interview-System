import tkinter as tk
from tkinter import ttk

from gui import login
from gui import startPage
from gui import greeting
from gui import mcq_main
from gui import questions
# import gui.login
# import gui.startPage
# import gui.greeting
# import gui.mcq_main
# import gui.questions


LARGEFONT = ("Comic Sans MS", 25)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Intelligent Interviewer')

        # self is like window - dont ask how

        # getting screen width and height of display
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        # setting tkinter window size to full screen
        self.geometry("%dx%d" % (width, height))
        # self.geometry
        # self.configure(bg = "red")
        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (startPage.StartPage, login.Login, greeting.Greeting, questions.Questions, mcq_main.Quiz):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(startPage.StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def getCandidateEmail(self):
        return self.frame[login.Login].getter()


# first window frame startpage


# Driver Code
app = tkinterApp()
app.mainloop()
