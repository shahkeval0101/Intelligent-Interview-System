import tkinter as tk
from tkinter import ttk
import json
import os
import time
from helper.time_manager import run, create_directory, this_student_directory_create
import cv2
import PIL.Image, PIL.ImageTk
import pyaudio, wave


student_folder_directory_path = create_directory("keval909") # this part should be in login file after login is successful
this_student_folder_directory_path = this_student_directory_create(student_folder_directory_path)
print("this stud folder directory path", this_student_folder_directory_path)
LARGEFONT =("Verdana", 15)


class Questions(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        label_heading = ttk.Label(self, text ="Questions", font = LARGEFONT)
        label_heading.grid(row = 0, column = 4, padx = 10, pady = 10)

        label_instruction = tk.Label(self, text ="You  Will Be Proctored For Reading- Don'T Perform Any Suspicious Activity", font = LARGEFONT)
        label_instruction.grid(row = 1, column = 4, padx = 10, pady = 10)

        

        # get questions from json file
        # run loop for each question
        # save_and_show timer for each question

        self.question_frame = tk.Frame(self, bg="blue",border=10, highlightcolor="blue")
        self.question_frame.grid(row = 3, column = 4)
        
        variable_question_text  = tk.StringVar()
        variable_time_allocated  = tk.IntVar()

        label_question = tk.Label(self.question_frame, textvariable = variable_question_text, font = LARGEFONT)
        label_question.grid(row = 4, column = 4)
        # txt.set("initial")

        label_timer = tk.Label(self, textvariable= variable_time_allocated, font = LARGEFONT)
        label_timer.grid(row = 5, column = 5, padx = 10, pady = 10)

        # loading question json file to python dictionary
        questions = open(self.get_file_path(), 'r')
        question_dict = json.load(questions)
        
        question_read_time = 5
        buffer_time = 3 # extra time for which the frame will be shown even after the question recording is complete

        print(question_dict)
        self.q_id = "1"
        # MAKE SURE ALL ENTRIES IN QUESTION.TXT ARE ORDER WISE STARTING FROM 1
        # # print(q,type(q))

        # def update_question():
        #     # global q_id
        #     print(self.q_id,self.q_id in question_dict)
        #     if self.q_id in question_dict: # checking presence in txt file

        #         question_text = question_dict[self.q_id]["text"]
        #         time_allocated = question_dict[self.q_id]["time"]
        #         print( "print save_and_show question", question_text, time_allocated )

        #         variable_question_text.set( question_text )
        #         variable_time_allocated.set( time_allocated )

        #         # run(self.q_id +"_reading",this_student_folder_directory_path, question_read_time )
        #         file_path = self.q_id +"_reading.avi"
        #         self.record_video(file_path)


        #         time.sleep(2) # check is this time is counted by .after method

        #         print("answersing starts")

        #         run(self.q_id+ "_answering", this_student_folder_directory_path, question_dict[self.q_id]['time'])
        #         time.sleep(2)


        #         self.q_id = int(self.q_id) + 1
        #         self.q_id = str(self.q_id)
        #         self.question_frame.after( (question_read_time+ time_allocated)*1000, update_question)

        #     else:
        #         variable_question_text.set( "Congratulations, all questions done!" )
        #         variable_time_allocated.set( 0 )

        
        # self.question_frame.after(5000,save_and_show_question)
        self.show_questions()

    


        # iterate each ques
        # print ques in label
        # start its timer
        # record
        # move to next question after its time




        # self.question_frame.after(1000, save_and_show_question)

    def get_file_path(self):
        os.getcwd()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        file_dir = os.path.join(dir_path,'resources')
        file_path = os.path.join(file_dir,"questions_testing.json")
        return (file_path)

  

    def show_questions(self):
        # print(file_path)

        self.camera_frame = tk.Frame(self.question_frame, bg="blue",border=10, highlightcolor="blue")
        self.camera_frame.grid(row = 6, column = 4)

        self.video = cv2.VideoCapture(0)
        
        self.width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.video.release()

        self.canvas = tk.Canvas(self.camera_frame, width=self.width, height=self.height)
        self.canvas.grid(row =7 , column = 5, padx = 10, pady = 10)


        self.opencamera = tk.Button(self.camera_frame, text="open camera", command=self.open_camera)
        self.opencamera.grid(row = 9, column = 5, padx = 10, pady = 10)

        self.closecamera = tk.Button(self.camera_frame, text="close camera", command=self.close_camera)
        self.closecamera.grid(row = 10, column = 5, padx = 10, pady = 10)

        self.delay = 10

        # self.set_camera(file_path) #this needs to be set every time you open the camera
        self.video_recorder(10)



    def video_recorder(self, duration):
        print("video recorder on")

        self.video_file_path = os.path.join(this_student_folder_directory_path, "ved101.avi")
        self.audio_file_path = os.path.join(this_student_folder_directory_path, "aud101.wav")

        self.set_camera(self.video_file_path)
        self.set_mic(self.audio_file_path) #mic close requires file location

        self.start_time = time.time()
        self.duration = duration
        self.save_and_show()



    def set_mic(self, file_path):
        self.open = True
        self.rate = 44100
        self.frames_per_buffer = 1024
        self.channels = 2
        self.format = pyaudio.paInt16
        self.audio_filename = file_path
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer = self.frames_per_buffer)
        self.audio_frames = []
        self.stream.start_stream()

   

    def open_camera(self, file_path):
        # self.ok = True
        # self.set_camera(file_path)
        print("camera opened")
        print(self.ok)


    def set_camera(self, file_path):
        print("setting camera")
        # self.ok = True
        self.video = cv2.VideoCapture(0)
        #create videowriter
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # self.out = cv2.VideoWriter('output.avi',self.fourcc,10,(640,480))
        print("file is saved at", file_path)
        self.out = cv2.VideoWriter(file_path,self.fourcc,10,(640,480))
        # self.save_and_show()


    def save_and_show(self):
        ret, frame = self.video.read()
        # print("in save_and_show")
        if ret:
            # save
            self.out.write(frame)
            # show 
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

            # while(self.open == True):
            data = self.stream.read(self.frames_per_buffer) 
            self.audio_frames.append(data)

        if time.time() - self.start_time > self.duration: # time out case
            print("time out")
            self.close_camera()
            self.close_mic()
        else: 
            self.camera_frame.after(self.delay, self.save_and_show)


    def close_camera(self):
        print("camera closed")
        self.ok = False
        self.video.release()
        self.out.release()
    
    def close_mic(self):

        # if self.open==True:
        self.open = False
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        waveFile = wave.open(self.audio_file_path, 'wb')
        waveFile.setnchannels(self.channels)
        waveFile.setsampwidth(self.audio.get_sample_size(self.format))
        waveFile.setframerate(self.rate)
        waveFile.writeframes(b''.join(self.audio_frames))
        waveFile.close()


    def __del__(self):
        if self.video.isOpened():
            self.video.release()
            self.out.release()

        



    





import helper.checker as chk
app =chk.Checker(Questions)
app.mainloop()