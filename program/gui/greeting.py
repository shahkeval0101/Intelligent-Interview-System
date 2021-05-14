import tkinter as tk
from tkinter import ttk

# import gui.startPage
# import gui.questions

from gui import startPage
from gui import questions
LARGEFONT =  ("Comic Sans MS", 18, 'bold')

# second window frame page1


class Greeting(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Important Instruction and Guidelines", font=LARGEFONT, background = '#bdbf41', foreground = "#ad2d2d")
        label.grid(row=0, column=1, padx=10, pady=10)
        self.configure(bg = '#bdbf41')
        welcome_speech = """
        •	This is robotic intelligent interviewer 
        •	The assessment has two section. Please attempt both the sections before submitting.
        •	The assessment has total 3 Questions followed by MCQ test for which the total time allowed is specified on the screen(15 sec to read questions and specified duration to answer on the question.
        •	For the entire duration of the assessment. Please remain seated in front of your webcam.
        •	IF you get caught practicing any means of malpractice, you would be disqualified  by the evaluator.
        •	Ensure proper lightning in the room – Source of light must not be behind you.
        •	Please sit in a quite with no background noise or people behind you.
        •	Please ensure the wall behind you has a plain background.
        •	You will be judged on the basis of soft skills and hard skills.
        •	A report will be send to you on your mail.
        •   All these steps are automated with no human interference.
        •   By continuing you agree to our terms and conditions.

        BEST OF LUCK

        """
        label = ttk.Label(self, text=welcome_speech, font=LARGEFONT, background = '#bdbf41', foreground = "#ad2d2d",)
        label.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = tk.Button(self, text="StartPage",fg = '#ebe8e9', bg ='#0a0002', font = ('Verdana', 15, 'bold'),
                             command=lambda: controller.show_frame(startPage.StartPage))

        # putting the button in its place
        # by using grid
        button1.place(x=200, y=600, height = 50, width = 150)

        button2 = tk.Button(self, text="Questions",fg = '#ebe8e9', bg ='#0a0002', font = ('Verdana', 15, 'bold'),
                             command=lambda: controller.show_frame(questions.Questions))

        # putting the button in its place
        # by using grid
        button2.place(x=400, y=600, height = 50, width = 150)

# import helper.checker as chk
# app =chk.Checker(Greeting)
# app.mainloop()
