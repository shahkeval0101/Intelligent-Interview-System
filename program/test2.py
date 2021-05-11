import os
candidate = "kevalshah90909@gmail"
# local_path = os.getcwd()
# parent_path = os.path.dirname(local_path)
# print("parent ", parent_path, local_path)
# c = os.path.join(str(parent_path), "student_interview_data", candidate)
# print(c)
# c = c+"\\"
# print("printing c"+c)

os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
#parent_path = os.path.dirname(dir_path)
print("print", dir_path)
#print("print", parent_path)
student_interview_data_path = os.path.join(
    str(dir_path), "gui", "student_interview_data", candidate)
student_interview_data_path = student_interview_data_path + "\\"
print("student_interview_data_path", student_interview_data_path)
