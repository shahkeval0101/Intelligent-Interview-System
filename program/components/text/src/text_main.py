# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:50:34 2020

@author: keval
"""

import re, math
from collections import Counter
import fuzzywuzzy.fuzz
import os
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
import pickle
import requests
from fuzzywuzzy import fuzz
from components.text.src.cosine_similarity import givKeywordsValue
from components.text.src.Speech_Recognition import speech_recognition

#   import  ...interviewer-system.program.main 
# some_file.py

# insert at 1, 0 is the script path (or '' in REPL)

def text_analysis(filename):
    model_answers= {
          "answer1": "Abstraction : Abstraction is the process of showing only essential/necessary features of an entity/object to the outside world and hide the other irrelevant information. For example to open your TV we only have a power button, It is not required to understand how infra-red waves are getting generated in TV remote control.\
                      Encapsulation : Encapsulation means wrapping up data and member function (Method) together into a single unit i.e. class. Encapsulation automatically achieve the concept of data hiding providing security to data by making the variable as private and expose the property to access the private data which would be public.\
                      Inheritance : The ability of creating a new class from an existing class. Inheritance is when an object acquires the property of another object. Inheritance allows a class (subclass) to acquire the properties and behavior of another class (super-class). It helps to reuse, customize and enhance the existing code. So it helps to write a code accurately and reduce the development time.\
                      Polymorphism: Polymorphism is derived from 2 Greek words: poly and morphs. The word poly means many and morphs means forms. So polymorphism means many forms. A subclass can define its own unique behavior and still share the same functionalities or behavior of its parent/base class. A subclass can have their own behavior and share some of its behavior from its parent class not the other way around",
          "keywords1": "['Encapsulation','Encapsulation','wrapping','Abstraction','data','binds','member','together', 'many','forms','relevant data', 'data hiding', 'data hiding', 'abstraction', 'combining data',object,'super-class','parent-class','reuse','customize','base class']",
          "out_of1": 5,
        
         
    }
    model_answer1 = model_answers['answer1']
    out_of1 = model_answers['out_of1']
    keywords1 = model_answers['keywords1']
    keywords1 = re.findall(r"[a-zA-Z]+", keywords1)
    
    
    
    #print(model_answer3)
    
    """
    answers= {
        "users1":{
          "a1": "It is object oreinted concept related to the data hiding. Abstraction of the program is the encapsulation. It shows the relvant data. It is the mechanism of binding the data, and the function that use them.",
          "a2": "time complexity analysis. Analyze the algorithm. Running time complexity analyse. Algorithms growth rate.It also measures the efficiency of the algorithm.",
          "a3": "htrfgbtrgdfrgfcb",
          "email": "vaibhavminiyar@gmail.com"
        }
    }
    """
    #print("dfaadaa")
    text = speech_recognition(filename)
    print("Text detected by speech to text is is",text)
        
    
    #print("nfafjaljf")
    local_path = os.path.realpath(__file__)
    parent_path = os.path.dirname(local_path)
    parent_path = os.path.dirname(parent_path)
    #print(local_path)
    #print(parent_path)
    fp = os.path.join( str(parent_path) ,"data","finaldataset.csv")
    #print(fp)
    
    
    df = pd.read_csv(fp)
    xf = df[['keyword', 'grammar', 'qst']]
    # intigrate keyword, grammar, qst :)
    '''
    keywords and qst:
    e = 1
    vg = 2
    g = 3
    o = 4
    p = 5
    vp = 6
    Grammar:
    y = 1
    n = 0
    class labels 0.1 to 0.9 simplifies to 0 to 9 for calculation purpose
    
    '''
    x = np.array(xf.values)
    yf = df[['class']]
    y = np.array(yf.values).ravel()
    clf = GaussianNB()
    clf.fit(x,y)
    
    
    #fp = (os.path.join( str(parent_path) ,"program","components","text","src","\\","nav_test_pickle"))
    
    with open("nav_test_pickle",'wb') as f:
    	pickle.dump(clf, f)
    
    
    #fp = (os.path.join( str(parent_path) ,"program","components","text","src","nav_test_pickle"))
    #print(fp)
    pickle_in = open("nav_test_pickle", 'rb')
    clf = pickle.load(pickle_in)
    
    
    
    def predict(k, g, q):
        predicted = clf.predict([[k, g, q]])
        accuracy = clf.predict_proba([[k, g, q]])
        #print("class[1-9] : " + str(predicted))
        # print(accuracy)
        # print(np.max(accuracy))
        return predicted
    
    
    def givVal(model_answer, keywords, answer, out_of):
        # KEYWORDS =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # TODO : Enhacnce this thing
        if (len(answer.split())) <= 5:
            return 0
        #
        # count = 0
        # keywords_count = len(keywords)
        # for i in range(keywords_count):
        #     if keywords[i] in answer:
        #         # print (keywords[i])
        #         count = count + 1
        # k = 0
        # if count == keywords_count:
        #     k = 1
        # elif count == (keywords_count - 1):
        #     k = 2
        # elif count == (keywords_count - 2):
        #     k = 3
        # elif count == (keywords_count - 3):
        #     k = 4
        # elif count == (keywords_count - 4):
        #     k = 5
        # elif count == (keywords_count - 5):
        #     k = 6
        k = givKeywordsValue(model_answer, answer)
        # print("checkkkkkk", k)
    
        # GRAMMAR =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
        req = requests.get("https://api.textgears.com/check.php?text=" + answer + "&key=c9YNqS8oSPyBcx0E")
    #     prin(req)
        no_of_errors = len(req.json()['errors'])
    
        if no_of_errors > 5 or k == 6:
            g = 0
        else:
            g = 1
    
        # QST =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # print("fuzz1 ratio: ", fuzz.ratio(model_answer, answer))
        q = math.ceil(fuzz.token_set_ratio(model_answer, answer) * 6 / 100)
    
        #print("Keywords : ", k)
        #print("Grammar  : ", g)
        #print("QST      : ", q)
    
        predicted = predict(k, g, q)
        # Mathematical model->
        # predicted / 10
        # what?	/ out_of
        result = predicted * out_of / 10
        #print("result",result[0])
        return result[0]
    
    
    for each_users_answers in range(1):
        # For the first answer ->
        #print("\n\n" + answers['users1']['email'])
    
        answer = text
        result = givVal(model_answer1, keywords1, answer, out_of1)
        print("Marks : " + str(result))
        #print("Results dictionary",Results)
    return result
