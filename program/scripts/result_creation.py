import os


def result_creation_f(result, email):
    print("candidates result in dictionary form :",result)
    f = open("result.txt", "w")


    string = "Mouth was open for " + \
        str(result["mouth_distance"])+ "% of question reading time"+ "\n"
    f.write(string)
    string = "Student was not facing the interviewer for " + \
        str(result["eye_tracker"])+"% of time" + "\n"
    f.write(string)
    string = "Spoofed frames were detected for " + \
        str(result["face_spoofing"]) + "% of time" + "\n"
    f.write(string)
    string = "Student's head pose was away from camera for " + \
        str(result["head_pose"])+"% of time" + "\n"
    f.write(string)
    string = "Pronunciation posteriori probability score percentage " + \
        str(result["audio"][2][0]) + "%" + "\n"
    f.write(string)
    string = "Balance (speaking duration)/(original duration) "+ \
        str(result["audio"][1][0]) +"\n"
    f.write(string)
    string = "Gender and emotion of the interviee " + \
        str(result["audio"][0][0]) + "\n"
    f.write(string)
    string = "Spoken Language Proficiency Level (accuracy) " + \
        str(result["audio"][3][0]) + "%" + "\n"
    f.write(string)
    string = "Technical analysis score is " + \
        str(result["text"]) + " marks out of 5" + "\n"
    f.write(string)
    string = "Technical Mcq correctly answerd are "+str(result["mcq"])+" out of 4\n"
    f.write(string)
    string = "Student was "+str(result["person_phone"][0]) + " phone \n"
    f.write(string)
    # if(result["person_phone"][1] > 1):
    string = "Number of person(s) in the interview  " + \
        str(result["person_phone"][1])+"\n"
    f.write(string)





    from fpdf import FPDF
    width = 210
    height = 297
    pdf = FPDF()
    pdf.add_page()

    local_path = os.path.realpath(__file__)
    parent_path = os.path.dirname(local_path)
    # print(local_path)
    # print(parent_path)
    filename = os.path.join(os.path.dirname(parent_path),"resources", "template_header.png")
    # print("template file name",filename)

    pdf.image(filename, 0, 0, width, 30)
    pdf.set_font('Arial', 'B', 30)
    pdf.cell(width/2, 60, "INTELLIGENT INTERVIEW SYSTEM".title(), border=5)
    pdf.line(10, 45, 200, 45)
    pdf.ln(10)
    f = open("result.txt", "r")
    # insert the texts in pdf
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(width/2, 90, txt="Report", align="c")
    pdf.set_font("Arial", size=12)

    # open the text file in read mode
    f = open("result.txt", "r")
    pdf.ln(10)
    # insert the texts in pdf
    for x in f:
        pdf.cell(110, 100, txt=x, align='l')
        pdf.ln(10)
    # os.unlink("Finalreport.pdf'"  )
    pdf.output('Finalreport.pdf', 'F')

    local_path = os.path.realpath(__file__)
    local_path = os.path.dirname(local_path)
    parent_path = os.path.dirname(local_path)
    # print(parent_path)
    c = os.path.join(str(parent_path), "gui",
                     "student_interview_data", email.split("@")[0],"report.pdf")
    # c = c+"\\"+"report.pdf"
    # save the pdf with name .pdf
    pdf.output(c)


# use this to test result creation, comment this part otherwise
# avg_result = {
#         "eye_tracker": 23,
#         "face_spoofing": 12,
#         "head_pose": 25,
#         "mouth_distance": 9,
#         "emotions": [1],
#         "text": 3.5,
#         "audio": [["a Male, mood of speech: speaking passionately"], [65], [72], [69]],
#         "person_phone": ["not using",1],
#         "mcq": 4
#     }
# result_creation_f(avg_result,"amit")