# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 01:04:44 2020

@author: hp
"""

import cv2
from components.video.face_detector import get_face_detector, find_faces
from components.video.face_landmarks import get_landmark_model, detect_marks, draw_marks
import os
def mouth_distance_f(filename):
    try:
        face_model = get_face_detector()
        landmark_model = get_landmark_model()
        outer_points = [[49, 59], [50, 58], [51, 57], [52, 56], [53, 55]]
        d_outer = [0]*5
        inner_points = [[61, 67], [62, 66], [63, 65]]
        d_inner = [0]*3
        font = cv2.FONT_HERSHEY_SIMPLEX 

        #local_path = os.getcwd()
        #parent_path = os.path.dirname(local_path)
        #parent_path=os.path.dirname(parent_path)
        #print(local_path)
        #print(parent_path)
        #filename = os.path.join( str(parent_path) ,"student_interview_data",candidate,"tejas.mp4")
        #filename = os.path.join( str(local_path) ,"video","1_reading.avi")
        print(filename)

        cap = cv2.VideoCapture(filename)


        ret, img = cap.read()
        rects = find_faces(img, face_model)
        #qprint(rects)
        for rect in rects:
            shape = detect_marks(img, landmark_model, rect)
            draw_marks(img, shape)
            #cv2.putText(img, 'Press r to record Mouth distances', (30, 30), font,
            #          1, (0, 255, 255), 2)
            cv2.imshow("Output", img)
        #if cv2.waitKey(1) & 0xFF == ord('r'):
            for i in range(100):
                for i, (p1, p2) in enumerate(outer_points):
                    d_outer[i] += shape[p2][1] - shape[p1][1]
                for i, (p1, p2) in enumerate(inner_points):
                    d_inner[i] += shape[p2][1] - shape[p1][1]
            #break
        cv2.destroyAllWindows()
        d_outer[:] = [x / 100 for x in d_outer]
        d_inner[:] = [x / 100 for x in d_inner]



        total_frames =0
        mouth_open = 0
        while(True):
            total_frames+=1
            ret, img = cap.read()
            if ret ==True:
                rects = find_faces(img, face_model)
                for rect in rects:
                    shape = detect_marks(img, landmark_model, rect)
                    cnt_outer = 0
                    cnt_inner = 0
                    draw_marks(img, shape[48:])
                    for i, (p1, p2) in enumerate(outer_points):
                        if d_outer[i] + 3 < shape[p2][1] - shape[p1][1]:
                            cnt_outer += 1 
                    for i, (p1, p2) in enumerate(inner_points):
                        if d_inner[i] + 2 <  shape[p2][1] - shape[p1][1]:
                            cnt_inner += 1
                    if cnt_outer > 3 and cnt_inner > 2:
                        print('Mouth open')
                        mouth_open+=1
                        cv2.putText(img, 'Mouth open', (30, 30), font,
                                1, (0, 255, 255), 2)
                    # show the output image with the face detections + facial landmarks
                cv2.imshow("Output", img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        print("total frames",total_frames) 
        print(mouth_open)  
        result_ans=round( (mouth_open*100)/total_frames,2 )
        print(result_ans)
        cap.release()
        cv2.destroyAllWindows()
        return result_ans
    except Exception as e:
        print(str(e))
        cap.release()
        cv2.destroyAllWindows()
        return -1 
    #mouth_distance_f()