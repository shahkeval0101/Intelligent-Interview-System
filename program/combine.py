# from gui import combine
import os
import json
from components.video import eye_tracker, face_spoofing, head_pose_estimation
from components.video import mouth_distance
# person and phone detection consumes a lot of time thus commented
# from components.video import  person_and_phone
from components.text.src import text_main
# prosidy analysis requires a complete silent environment thus commented
# from components.audio import testpro
from components.audio import audio_main
from components.video.Emotion_detection.src import emotions
from collections import Counter
from scripts import result_creation
# from scripts import mail_sender_code

# to remove warnings from tensorflow    
import tensorflow as tf
tf.get_logger().warning('test')
# WARNING:tensorflow:test
tf.get_logger().setLevel('ERROR')
tf.get_logger().warning('test')


def evaluate_video(path, result, mouth_distance_evaluation):
    result["eye_tracker"].append(eye_tracker.eye_tracker_f(path))
    result["face_spoofing"].append(face_spoofing.face_spoofing_f(path))
    result["head_pose"].append(
        head_pose_estimation.head_pose_estimation_f(path))

    # phones,persons = person_and_phone.p_and_p_f(path)
    # print("person and phone",phones,persons)
    # result["person_phone"]["phone"].append(phones)
    # result["person_phone"]["person"].append(persons)

    if(mouth_distance_evaluation == 0):
        result["mouth_distance"].append(mouth_distance.mouth_distance_f(path))
    result["emotions"].append((list(emotions.emotions_f(path))))


    print("\nResult for video evaluation\n",result)


def combine_f():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    student_interview_data_folder = os.path.join(
        str(dir_path), "gui", "student_interview_data")

    candidate_details_path = os.path.join(student_interview_data_folder,"temp_student_details.txt")
    #  this is a temporary file which gets created for the most recent user
    candidate_details_path_file = open(candidate_details_path)
    candidate_details = json.load(candidate_details_path_file)

    print("\nCandidate details are", candidate_details)

    # email will have complete address of form xyz@gmail.com
    global email
    email = candidate_details["email"]

    username = email.split("@")[0]
    c = os.path.join(student_interview_data_folder, username)
    print("\n candidates data folder path "+c)


    result = {
        "eye_tracker": [],
        "face_spoofing": [],
        "head_pose": [],
        "mouth_distance": [],
        "emotions": [],
        "text": [],
        "audio": [[], [], [], []],
        "person_phone": {"phone":[False], "person":[False]},#first will store instances of  phone, next of person
        "mcq": 0
    }

    questions_path = os.path.join(
        str(dir_path), "gui", "resources", "questions.json")


    questions = open(questions_path, 'r')
    q = json.load(questions)
    l_questions_text = ["2"]#text evaluation question
    for q_id in q:
        print("\n\n\nFor the question ID - ",q_id, end="\n")

        reading_file = os.path.join(c,str(q_id)+"_reading")
        answering_file = os.path.join(c,str(q_id)+"_answering")

        print("reading_file",reading_file)
        print("answering_file",answering_file)

        evaluate_video(reading_file+".avi" , result, 0)
        evaluate_video(answering_file+".avi", result, 1)
        # Gend_value, bal_value, pronoun_value, acc_value = testpro.speech_analysis(answering_file+".wav")
        # result["audio"][0].append(Gend_value)
        # result["audio"][1].append(bal_value)
        # result["audio"][2].append(pronoun_value)
        # result["audio"][3].append(acc_value)
        if(q_id in l_questions_text):
            result["text"].append(text_main.text_analysis(answering_file+".wav"))

    avg_result = {
        "eye_tracker": 0,
        "face_spoofing": 0,
        "head_pose": 0,
        "mouth_distance": 0,
        "emotions": [],
        "text": 0,
        "audio": [[], [], [], []],
        "person_phone": {"phone":[], "person":[]},
        "mcq": 0
    }

    eye_tracker_avg = 0
    eye_tracker_count = 1
    face_spoofing_avg = 0
    face_spoofing_count = 1
    head_pose_avg = 0
    head_pose_count = 1
    mouth_distance_avg = 0
    mouth_distance_count = 1
    postive_emotions_avg = 0
    negative_emotions_avg = 0
    emtions_count = 1
    balance_avg = 0
    balacne_count = 1
    pron_avg = 0
    pron_count = 1
    accuracy_avg = 0
    accuracy_count = 1
    audio_gender = ""
    for i in result:
        if(i == "eye_tracker"):
            for j in result[i]:
                if(j != -1):
                    eye_tracker_avg = j+eye_tracker_avg
                    eye_tracker_count += 1

        elif(i == "face_spoofing"):
            for j in result[i]:
                if(j != -1):
                    face_spoofing_avg = j+face_spoofing_avg
                    face_spoofing_count += 1

        elif(i == "head_pose"):
            for j in result[i]:
                if(j != -1):
                    head_pose_avg = j+head_pose_avg
                    head_pose_count += 1
        elif(i == "mouth_distance"):
            for j in result[i]:
                if(j != -1):
                    mouth_distance_avg = j+mouth_distance_avg
                    mouth_distance_count += 1
        elif(i == "emotions"):
            for j in result["emotions"]:
                # print(len(j))
                postive_emotions_avg = j[0]+postive_emotions_avg
                negative_emotions_avg = j[1]+negative_emotions_avg
                emtions_count += 1

        # elif(i == "person_phone"):
        #         phone_detected = any(result["person_phone"]["phone"])
        #         person_detected = any(result["person_phone"]["person"])
       
        # elif(i == "audio"):
        #     counter1 = Counter(result[i][0])
        #     audio_gender = counter1.most_common(1)[0][0]
        #     for j in result[i][1]:
        #         if(j != -1):
        #             balance_avg = j+balance_avg
        #             balacne_count += 1
        #     for j in result[i][2]:
        #         if(j != -1):
        #             pron_avg = j+pron_avg
        #             pron_count += 1
        #     for j in result[i][3]:
        #         if(j != -1):
        #             accuracy_avg = j+accuracy_avg
        #             accuracy_count += 1

    avg_result["eye_tracker"] = eye_tracker_avg//eye_tracker_count
    avg_result["face_spoofing"] = face_spoofing_avg//face_spoofing_count
    avg_result["head_pose"] = head_pose_avg//head_pose_count
    avg_result["mouth_distance"] = mouth_distance_avg//mouth_distance_count
    avg_result["emotions"].append(postive_emotions_avg//emtions_count)
    avg_result["emotions"].append(negative_emotions_avg//emtions_count)
    # avg_result["audio"][0] = audio_gender
    # avg_result["audio"][1] = balance_avg/balacne_count
    # avg_result["audio"][2] = pron_avg/pron_count
    # avg_result["audio"][3] = accuracy_avg//accuracy_count
    avg_result["text"] = result["text"]
    # avg_result["person_phone"]["phone"] = phone_detected
    # avg_result["person_phone"]["person"] = person_detected
    avg_result["mcq"] = result["mcq"]
    print(avg_result)
    result_creation.result_creation_f(avg_result, email )
    # mail_sender_code.mail_sender_f(candidate)

    with open(c+'result.json', 'w', encoding='utf-8') as f:
        json.dump(avg_result, f, ensure_ascii=False, indent=4)
    return avg_result


# combine_f(student_folder_directory)
combine_f()
# print(candidate)