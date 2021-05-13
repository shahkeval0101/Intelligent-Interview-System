import tkinter as tk
from tkinter import ttk

# import greeting
# import login

from gui import login
from gui import greeting

import os

from PIL import ImageTk,Image


LARGEFONT = ("Comic Sans MS", 25, 'bold')


# todo
# its like the banner page of our app
# add images

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = '#bdbf41')

        # label of frame Layout 2
        local_path = os.path.realpath(__file__)
        parent_path = os.path.dirname(local_path)
        # print(local_path)
        print(parent_path)
        filename = os.path.join(str(parent_path), "resources","logo_main.pgm")
        print(filename)
        image = Image.open(filename)
        image = image.resize((400, 250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        label = ttk.Label(self, image = photo)
        label.image = photo
        label.place(x = 500, y = 200)

        #heading
        label = ttk.Label(
            self, text="Intelligent Interviewer System", font=LARGEFONT, background = '#bdbf41', foreground = "#ad2d2d" )

        # # putting the grid in its place by using
        # # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = tk.Button(self, text="Login", fg = '#ebe8e9', bg ='#0a0002', font = ('Verdana', 15, 'bold'),
                             command=lambda: controller.show_frame(login.Login))
        
        # putting the button in its place by
        # # using grid
        button1.place(x=625, y=480, height = 50, width = 150)
