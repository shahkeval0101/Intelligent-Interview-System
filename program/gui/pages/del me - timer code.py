# source
# https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter#:~:text=Tkinter%20root%20windows%20have%20a,up%20an%20automatically%20recurring%20event.&text=Bear%20in%20mind%20that%20after,will%20run%20exactly%20on%20time.

import tkinter as tk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()