import json
# import startPage
# import greeting
import tkinter as tk
from tkinter import ttk
import os

from gui import startPage
from gui import greeting

# and import messagebox as mb from tkinter
from tkinter import IntVar
from tkinter import messagebox as mb
# import json to use json file for data
import json

LARGEFONT = ("Comic Sans MS", 25, 'bold')


class Quiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg = '#bdbf41')
        local_path = os.path.realpath(__file__)
        parent_path = os.path.dirname(local_path)
        # print(local_path)
        print(parent_path)
        filename = os.path.join(str(parent_path),"resources", "MCQ_Questions.json")
        print(filename)
        f = open(filename, "r")
        data = json.load(f)

        question = (data['question'])
        options = (data['options'])
        answer = (data['answer'])
        # label of frame Layout 2
        #label = tk.Label(self, text ="Quiz", font = LARGEFONT)

        # putting the grid in its place by using
        # grid
        #label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button1 = tk.Button(self, text ="Page 1",
        # #command = lambda : controller.show_frame(Page1)
        # )
        # putting the button in its place by
        # using grid
        # button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # ## button to show frame 2 with text layout2
        # button2 = tk.Button(self, text ="Page 2",
        # #command = lambda : controller.show_frame(Page2)
        # )

        # putting the button in its place by
        # using grid
        # button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.q_no = 0
        self.correct = 0

        # This method is used to Display Title
        def display_title():

            # The title to be shown
            title = tk.Label(self, text="Technical MCQ Test",
                             background = '#bdbf41', foreground = '#e30909',font = ('Verdana', 35, 'bold'))

            # place of the title
            title.place(x=0, y=2)

        def display_question():

            # setting the Quetion properties
            q_no = tk.Label(self, text=question[self.q_no], font = ('Verdana', 25, 'bold'),background = '#bdbf41',anchor='w')

            # placing the option on the screen
            q_no.place(x=70, y=100, height = 50, width = 1500)

        def radio_buttons():

            # initialize the list with an empty list of options
            q_list = []

            # position of the first option
            y_pos = 150

            # adding the options to the list
            while len(q_list) < 4:

                # setting the radio button properties
                radio_btn = tk.Radiobutton(self, text=" ", variable=opt_selected,
                                           value=len(q_list)+1, font=("Verdana", 14), background = '#bdbf41')

                # adding the button to the list
                q_list.append(radio_btn)

                # placing the button
                radio_btn.place(x=100, y=y_pos)

                # incrementing the y-axis position by 40
                y_pos += 40

            # return the radio buttons
            return q_list

        def display_options():
            val = 0

            # deselecting the options
            opt_selected.set(0)

            # looping over the options to be displayed for the
            # text of the radio buttons.
            for option in options[self.q_no]:
                opts[val]['text'] = option
                val += 1

        def buttons():

            # The first button is the Next button to move to the
            # next Question
            next_button = tk.Button(self, text="Next", 
                                    fg = '#ebe8e9', bg ='#0a0002', font = ('Verdana', 15, 'bold'),command=next_btn)

            # palcing the button on the screen
            next_button.place(x=200, y=380,height = 50, width = 150)

            # This is the second button which is used to Quit the GUI
            quit_button = tk.Button(self, text="End",
                                   fg = '#ebe8e9', bg ='#0a0002', font = ('Verdana', 15, 'bold'), command=self.quit)

            # placing the Quit button on the screen
            quit_button.place(x=1100, y=20, height = 50, width = 150,)

        def next_btn():
            print(self.correct)
            # Check if the answer is correct
            if check_ans():

                # if the answer is correct it increments the correct by 1
                self.correct += 1

            # Moves to next Question by incrementing the q_no counter
            self.q_no += 1

            # checks if the q_no size is equal to the data size
            if self.q_no == data_size:

                # if it is correct then it displays the score
                display_result()

                # destroys the GUI
                # self.controller.destroy()
            else:
                # shows the next question
                display_question()
                display_options()

        def display_result():

            # calculates the wrong count'
            print("result", data_size, self.correct, self.correct/data_size)
            score = self.correct / data_size * 100
            wrong_count = data_size - self.correct
            #self.correct = f"Correct: {self.correct}"
            #wrong = f"Wrong: {wrong_count}"

            # calcultaes the percentage of correct answers
            #result = f"Score: {score}%"

            # Shows a message box to display the result
            mb.showinfo("Result", "\nPercentage score :{}\nCorrect{}\nWrong{}".format(
                score, self.correct, wrong_count))

        # This method checks the Answer after we click on Next.

        def check_ans():

            # checks for if the selected option is correct
            if opt_selected.get() == answer[self.q_no]:
                # if the option is correct it return true
                return True

        print("function")
        display_title()
        display_question()

        # opt_selected holds an integer value which is used for
        # selected option in a question.
        opt_selected = IntVar()

        # displaying radio button for the current question and used to
        # display options for the current question
        opts = radio_buttons()

        # display options for the current question
        display_options()

        # displays the button for next and exit.
        buttons()

        # no of questions
        data_size = len(question)

        # keep a counter of correct answers
        self.correct = 0
    def quit(self):
        self.controller.destroy()
