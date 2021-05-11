import tkinter as tk 
from tkinter import ttk
# tkinter.ttk/

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

surprise = tk.StringVar()
label_heading = ttk.Label(frame, textvariable = surprise )
label_heading.pack()

def put_text():
    surprise.set("Surprise")

label_heading.after(2000, put_text)

root.mainloop()

