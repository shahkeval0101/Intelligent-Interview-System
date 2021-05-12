# authenticate student
# ask questions according to time
# genrate and mail report
import errors
import json
from time_manager import run, create_directory
import time
import os

"""
time.sleep is used to give the student enough time to read questions
"""

try:
    mail = input("Hello, please enter your registered email id\n")
    """
    check mail in student files
    """
    student_file = open("./students.txt", 'r')
    student_data = student_file.readlines()
    #print(student_data)


    if mail+"\n" not in student_data:
        
        raise errors.StudentNotResgistered

    time.sleep(1)

    # student_folder_directory = mail.split(".")[0]
    # print(" directory name ", student_folder_directory)
    # create_directory(student_folder_directory)
    

    welcome_speech = """
    I am 'robo', your AI interviewer
    I will ask you questions and you will have 15secs to read each question
    After which you will have to answer in given stipulated time
    I will judge you on the basis of soft skills and hard skills
    You will get your report on your mail
    BEST OF LUCK
    """

    print("\nHello "+ mail)

    time.sleep(2)

    print(welcome_speech)

    time.sleep(15)

    questions = open(r"./questions.json", 'r')

    """
    read question and allocated time then run a loop to capture video and save it
    """
    student_folder_directory = mail.split(".")[0]
    #print(" directory name ", student_folder_directory)
    create_directory(student_folder_directory)

    q = json.load(questions)
    for q_id in q:
        # print (q[q_id]['time'], q[q_id]['text'])
        print("YOU ARE BEING PROCTORED FOR READING- DON'T PERFORM ANY SUSPICIOUS ACTIVITY")

        time.sleep(2)

        print(q[q_id]["text"])
        run(q_id+ "_reading",  15, student_folder_directory)

        print("YOU ARE BEING PROCTORED FOR ANSWERING")

        time.sleep(2)

        run(q_id+ "_answering", q[q_id]['time'],student_folder_directory)


    # for 
    # print(questions.readline)


    

except FileNotFoundError as fe:
    print(fe)
except errors.StudentNotResgistered:
    print("You are not registered")
finally:
    student_file.close()
