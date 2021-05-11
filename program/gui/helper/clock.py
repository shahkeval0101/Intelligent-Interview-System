import tkinter as tk
from tkinter import ttk
import time


class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Digital Clock')
        self.resizable(0, 0)
        self.geometry('250x80')
        self['bg'] = 'black'

        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='black',
            foreground='red')

        # label
        start_time = 10
        self.label = ttk.Label(
            self,
            text=start_time,
            font=('Digital-7', 40))

        self.label.pack(expand=True)

        # schedule an update every 1 second
        self.label.after(1000, lambda : self.update(start_time))

    # def time_string(self,t):
    #     return t-1
        # return time.strftime('%H:%M:%S')

    def update(self,t):
        """ update the label every 1 second """
        # t = self.time_string()
        t-=1
        self.label.configure(text=t)

        # schedule another timer
        if t > 0:
            self.label.after(1000, lambda : self.update(t))


if __name__ == "__main__":
    clock = DigitalClock()
    clock.mainloop()