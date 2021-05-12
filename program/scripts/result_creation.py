import os


def result_creation_f(result, email):
    print(result)
    f = open("result.txt", "w")
    var = 0
    #string = "Phone was detected by system " + str(dsa) +" times"+"\n"
    # print(string)
    # f.write(string)
    #string = "Mouth was open "+str(var) + " times" + "\n"
    # f.write(string)
    string = "Student was not facing the interviewer for eye tracker " + \
        str(result["eye_tracker"])+" % of time" + "\n"
    f.write(string)
    string = "Spoofed frames " + \
        str(result["face_spoofing"]) + " % of time" + "\n"
    f.write(string)
    string = "Student was NOT facing the interviewer for head pose " + \
        str(result["head_pose"])+" % of time" + "\n"
    f.write(string)
    string = "Pronunciation_posteriori_probability_score_percentage " + \
        str(result["audio"][2]) + " %" + "\n"
    f.write(string)
    string = "balance "+str(result["audio"][1]) + \
        " (speaking duration)/(original duration)" + "\n"
    f.write(string)
    string = "Gender and emotion of the interviee is " + \
        str(result["audio"][0]) + "\n"
    f.write(string)
    string = "accuracy of the interviee is " + \
        str(result["audio"][3]) + " %" + "\n"
    f.write(string)
    string = "technical analysis of the interviee is " + \
        str(result["text"]) + " marks out of 5" + "\n"
    f.write(string)
    string = "Technical Mcq correctly answerd:-"+str(result["mcq"])+"\n"
    f.write(string)
    string = "Student was "+str(result["person_phone"][0]) + " phone \n"
    f.write(string)
    if(result["person_phone"][1] > 1):
        stirng = "Number of person in the interview is " + \
            str(result["person_phone"][1])+"\n"
        f.write(string)

    from fpdf import FPDF
    width = 210
    height = 297
    pdf = FPDF()
    pdf.add_page()

    local_path = os.path.realpath(__file__)
    parent_path = os.path.dirname(os.path.realpath(__file__))
    # print(local_path)
    print(parent_path)
    filename = os.path.join(str(parent_path),"resources", "template_header.png")
    print(filename)


    pdf.image(filename, 0, 0, width, 30)
    pdf.set_font('Arial', 'B', 30)
    pdf.cell(width/2, 60, "INTELLIGENT INTERVIEW SYSTEM", border=5)
    pdf.line(10, 45, 200, 45)
    pdf.ln(10)
    f = open("result.txt", "r")
    # insert the texts in pdf
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(width/2, 90, txt="Reports", align="c")
    pdf.set_font("Arial", size=12)

    # open the text file in read mode
    f = open("result.txt", "r")
    pdf.ln(10)
    # insert the texts in pdf
    for x in f:
        pdf.cell(110, 100, txt=x, align='l')
        pdf.ln(10)
    pdf.output('Finalreport.pdf', 'F')

    local_path = os.getcwd()
    parent_path = os.path.dirname(local_path)
    # print(parent_path)
    c = os.path.join(str(parent_path), "program", "gui",
                     "student_interview_data", email)
    c = c+"\\"+"report.pdf"
    # save the pdf with name .pdf
    pdf.output(c)
