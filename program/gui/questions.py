import gui.helper.checker as chk
import tkinter as tk
from tkinter import ttk
import json
import os
import time
import threading
# import mcq_main
from gui.helper.time_manager import run, create_directory, this_student_directory_create
from gui import mcq_main
from gui import login

"""
#a7c957
#3399FF
#8FAADC
"""


"""
todo:
----add gif of recording when recording in progress
----get student directory name from login .py 
video preview window is shown only for the first question, why so?
--FIXED-- question frames are getting overlap because of different size -- one solutions is fix the width and height of all question frame
make button of end test RED in color
--FIXED--show stopwatch timer in screen if possible 
disable button when recording in progress
--FIXED--replace the while loop in time manager with sleep
add database to resources
"""
"""
frame size fix -  disable propogation 
"""
LARGEFONT = ("Comic Sans MS", 25, 'bold')
FRAME_BG_COLOR = "#4ed10d"
FRAME_BORDER_SIZE = 5




class Questions(tk.Frame):


    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.configure(bg = '#bdbf41')
        self.controller = controller
        # self.create_student_folder()

        label_heading = ttk.Label(self, text="Questions", font=LARGEFONT,background = '#bdbf41', foreground = "#ad2d2d")
        label_heading.grid(row=0, column=0, padx=10, pady=10)

        
        label_instruction = tk.Label(
            self, text="You  Will Be Proctored For Reading and Answering-  Don'T Perform Any Suspicious Activity", font=LARGEFONT,background = '#bdbf41')
        label_instruction.grid(row=1, column=0, padx=10, pady=10)

        # get questions from json file
        questions = open(self.get_file_path(), 'r')
        self.question_dict = json.load(questions)
        print("\nquestion dict ---", self.question_dict)

        sorted_questions_keys = sorted(self.question_dict.keys())
        print("\nsorted question keys ---", sorted_questions_keys)

        self.question_read_time = 5

        # storing each frame on a list
        self.question_list = []

        for q_id in sorted_questions_keys:
            # creating frame
            question_frame = tk.LabelFrame(
                self,text = "Question No"+str( q_id),  bg=FRAME_BG_COLOR, border=FRAME_BORDER_SIZE, highlightcolor="blue")
            question_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            # add questiorn lable
            label_question = tk.Label(
                question_frame, text=self.question_dict[q_id]["text"], font=LARGEFONT,background = FRAME_BG_COLOR)
            label_question.grid(row=0, column=0, padx=10, pady=10)

            # add time label
            label_timer = tk.Label(question_frame, text="Time allocated for answering this question is: \t " +
                                   str(self.question_dict[q_id]["time"])+" secs", font=LARGEFONT, background = FRAME_BG_COLOR)
            label_timer.grid(row=1, column=0, padx=10, pady=10)

### a label at row 2 is dyanmically generated in next_question() so do not add anything coz it  will be hidden by that label


            question_frame.grid_columnconfigure( index = 0, weight=1)
            question_frame.grid_columnconfigure(index = 1, weight=1)
            # add this frame to parent frame
            self.question_list.append(question_frame)

        print("question list is", self.question_list)
        self.current_question_number = 0

        # first frame
        self.first_question_frame = tk.Frame(
            self, bg=FRAME_BG_COLOR, border=FRAME_BORDER_SIZE, highlightcolor="blue")
        self.first_question_frame.grid(row=2, column=0, sticky="nsew")
        
        first_label_question = tk.Label(
            self.first_question_frame, text="Click on the next button when you are ready. Reading time for each questions is " + str(self.question_read_time) + " secs", font=LARGEFONT, background = FRAME_BG_COLOR)
        first_label_question.grid(row=0, column=0, padx=10, pady=10,sticky="nsew")
        
        self.first_question_frame.grid_columnconfigure( index = 0, weight=1)
        self.first_question_frame.grid_columnconfigure(index = 1, weight=1)
            
        # last frame
        self.last_question_frame = tk.Frame(
            self, bg=FRAME_BG_COLOR, border=FRAME_BORDER_SIZE, highlightcolor="blue")
        self.last_question_frame.grid(row=2, column=0, sticky="nsew")

        last_label_question = tk.Label(
            self.last_question_frame, text="All questions done", font=LARGEFONT, background = FRAME_BG_COLOR)
        last_label_question.grid(row=0, column=0, padx=10, pady=10)

        self.last_question_frame.grid_columnconfigure( index = 0, weight=1)
        self.last_question_frame.grid_columnconfigure(index = 1, weight=1)
        
# initially show the first question
        self.first_question_frame.tkraise()


        self.label_clock_timer = ttk.Label(self, text="Time remaining will be displaced here", font=LARGEFONT,background = '#bdbf41')
        self.label_clock_timer.grid(row=3, column=0, padx=10, pady=10)

        self.buttonNext = tk.Button(self, text="Next", fg = '#ebe8e9', bg ='#0a0002', font = ('Verdana', 15, 'bold'),
                                     command=self.next_question)
        # putting the button in its place
        # by using grid
        self.buttonNext.place(x=700, y=500, height = 50, width = 200)




    def next_question(self):

        print("self.buttonNext[state]", self.buttonNext["state"])
        if self.current_question_number == 0:
            # self.current_question_number
            self.create_student_folder()
        print("current question number is", self.current_question_number)
        # all questions done, show the end screen
        if self.current_question_number == len(self.question_dict):
            # self.buttonNext["state"] = "DISABLED"
            self.show_last_frame()
            return

        def update_question_on_screen():
            self.question_list[self.current_question_number].tkraise()
        # daemon - true : if main program exits thread will not block and will exit too
        question_thread = threading.Thread(
            target=update_question_on_screen, daemon=True)
        question_thread.start()

        self.current_question_number += 1

        def start_recording():

            # only for testing . remove if condition in production
            # if True :
            #     return
            current_frame = self.question_list[self.current_question_number - 1]
            
            label_question = tk.Label(current_frame, text="Question Reading recording starts", font=LARGEFONT, background = FRAME_BG_COLOR)
            label_question.grid(row=2, column=0, padx=10, pady=10)


            t = self.question_read_time
            update_timer_thread = threading.Thread(target = self.update_timer_function, daemon=True, args=(t+1,) )
            update_timer_thread.start()

            run(str(self.current_question_number) + "_reading",
                self.this_student_folder_directory_path, self.question_read_time)
            # print("inside start recording")

            ans_time = self.question_dict[str(
                self.current_question_number)]["time"]

            label_question.configure(text="Answering recording starts", background = FRAME_BG_COLOR)

            ### start clock timer
            update_timer_thread = threading.Thread(target = self.update_timer_function, daemon=True, args=(ans_time
            +1,) )
            update_timer_thread.start()
            run(str(self.current_question_number) + "_answering",
                self.this_student_folder_directory_path, ans_time)

        recording_thread = threading.Thread(
            target=start_recording, daemon=True)
        recording_thread.start()

        # Makes sure the threads have finished
        print("active threads in question.py", threading.active_count())
        print("all thread completed")

        print('self.buttonNext["state"]',self.buttonNext["state"])





    def show_last_frame(self):
        self.last_question_frame.tkraise()
        self.buttonNext.configure(
            text="Mcq section", command=lambda: self.controller.show_frame(mcq_main.Quiz),height = 50, width = 200)
        # 
        # self.buttonNext.configure(
        #     text="End test", command=self.quit())

    def update_timer_function(self,t):
        def update(t):
            t -= 1
            self.label_clock_timer.configure(text = t)
            if t > 0:
                self.label_clock_timer.after(1000, lambda : update(t))
            else:
                self.label_clock_timer.configure(text = "Time Up!")
                # self.buttonNext["state"] = "NORMAL"

        update(t)



    def create_student_folder(self):
        # this part should be in login file after login is successful
        self.student_folder_directory_path = create_directory(self.controller.frames[login.Login].getter().split("@")[0])
        self.this_student_folder_directory_path = this_student_directory_create(
            self.student_folder_directory_path)
        print("this stud folder directory path",
              self.this_student_folder_directory_path)



    def get_file_path(self):
        # os.getcwd()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        file_dir = os.path.join(dir_path, 'resources')
        file_path = os.path.join(file_dir, "questions.json")
        return (file_path)

    def show_timer(self):
        pass

    def quit(self):
        self.controller.destroy()

    # def __del__(self):
    #     if self.video.isOpened():
    #         self.video.release()
    #         self.out.release()


# app = chk.Checker(Questions)
# app.mainloop()
