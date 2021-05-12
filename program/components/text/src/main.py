# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:50:34 2020

@author: keval
"""

import re, math
from collections import Counter
import fuzzywuzzy.fuzz

from cosine_similarity import givKeywordsValue

model_answers= {
      "answer1": "Encapsulation is an object-oriented programming concept that binds together the data and functions that manipulate the data, and that keeps both safe from outside interference and misuse.Data encapsulation led to the important OOP concept of data hiding. If a class does not allow calling code to access internal object data and permits access through methods only, this is a strong form of abstraction or information hiding known as encapsulation. Data encapsulation is a mechanism of bundling the data, and the functions that use them and data abstraction is a mechanism of exposing only the interfaces and hiding the implementation details from the user. Abstraction and encapsulation are complementary concepts: abstraction focuses on the observable behavior of an object. encapsulation focuses upon the implementation that gives rise to this behavior. encapsulation is most often achieved through information hiding, which is the process of hiding all of the secrets of object that do not contribute to its essential characteristics.  Encapsulation is the process of combining data and functions into a single unit called class. In Encapsulation, the data is not accessed directly; it is accessed through the functions present inside the class. In simpler words, attributes of the class are kept private and public getter and setter methods are provided to manipulate these attributes. Thus, encapsulation makes the concept of data hiding possible Abstraction is a process where you show only “relevant” data and “hide” unnecessary details of an object from the user.",
      "keywords1": "['binds', 'together', 'relevant data', 'data hiding', 'data hiding', 'abstraction', 'combining data']",
      "out_of1": 5,
    
      "answer2": "Asymptotic Notations are languages that allow us to analyze an algorithm's running time by identifying its behavior as the input size for the algorithm increases. This is also known as an algorithm's growth rate. Main Types - 1. Big 2.Small 1. Big Notation further divided into three types- 1)Big O 2)Big Omega 3)Big Theta 2. Small Notation further divided into three types- 1)Small o 2)Small Theta",
      "keywords2": "['Analysing Algorithm', 'analyse running time','represent time complexity of algorithms','measure the efficiency']",
      "out_of2": 5,
      
      "answer3": "Polymorphism means to process objects differently based on their data type.     In other words it means, one method with multiple implementation, for a certain class of action. And     which implementation to be used is decided at runtime depending upon the situation (i.e., data type of     the object)     This can be implemented by designing a generic interface, which provides generic methods for a certain     class of action and there can be multiple classes, which provides the implementation of these generic     methods.     In object-oriented programming, polymorphism refers to a programming language&#39;s ability to process     objects differently depending on their data type or class. More specifically, it is the ability to redefine     methods for derived classes. 1) Static Polymorphism also known as compile time polymorphism - Polymorphism that is resolved     during compiler time is known as static polymorphism. Method overloading is an example of compile     time polymorphism.     2) Dynamic Polymorphism also known as runtime polymorphism - It is also known as Dynamic     Method Dispatch. Dynamic polymorphism is a process in which a call to an overridden method is     resolved at runtime, that is why it is called runtime polymorphism.",
      "keywords3": "['one name many forms' , 'generic interface', 'implementation', 'runtime', 'same method name', 'same function name']",
      "out_of3": 5
}
model_answer1 = model_answers['answer1']
out_of1 = model_answers['out_of1']
keywords1 = model_answers['keywords1']
keywords1 = re.findall(r"[a-zA-Z]+", keywords1)


model_answer3 = model_answers['answer3']
out_of3 = model_answers['out_of3']
keywords3 = model_answers['keywords3']
keywords3 = re.findall(r"[a-zA-Z]+", keywords3)


model_answer2 = model_answers['answer2']
out_of2 = model_answers['out_of2']
keywords2 = model_answers['keywords2']
keywords2 = re.findall(r"[a-zA-Z]+", keywords2)

print(model_answer3)


answers= {
    "users1":{
      "a1": "It is object oreinted concept related to the data hiding. Abstraction of the program is the encapsulation. It shows the relvant data. It is the mechanism of binding the data, and the function that use them.",
      "a2": "time complexity analysis. Analyze the algorithm. Running time complexity analyse. Algorithms growth rate.It also measures the efficiency of the algorithm.",
      "a3": "htrfgbtrgdfrgfcb",
      "email": "vaibhavminiyar@gmail.com"
    }
}
    
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
import pickle
import requests
from fuzzywuzzy import fuzz
import os

local_path = os.getcwd()
parent_path = os.path.dirname(local_path)
print(local_path)
print(parent_path)
filename = os.path.join( str(parent_path) ,"data","finaldataset.csv")
print(filename)


df = pd.read_csv(filename)
xf = df[['keyword', 'grammar', 'qst']]
# intigrate keyword, grammar, qst :)
''''
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



with open('nav_test.pickle','wb') as f:
	pickle.dump(clf, f)

pickle_in = open('nav_test.pickle', 'rb')
clf = pickle.load(pickle_in)


def predict(k, g, q):
    predicted = clf.predict([[k, g, q]])
    accuracy = clf.predict_proba([[k, g, q]])
    print("class[1-9] : " + str(predicted))
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

    print("Keywords : ", k)
    print("Grammar  : ", g)
    print("QST      : ", q)

    predicted = predict(k, g, q)
    # Mathematical model->
    # predicted / 10
    # what?	/ out_of
    result = predicted * out_of / 10
    print("result",result[0])
    return result[0]

Results = {}
for each_users_answers in range(2):
    # For the first answer ->
    print("\n\n" + answers['users1']['email'])

    answer1 = answers['users1']['a1']
    result1 = givVal(model_answer1, keywords1, answer1, out_of1)
    print("Marks : " + str(result1))
    Results.update({"result1":result1})


    # For the Second answer ->
    answer2 = answers['users1']['a2']
    result2 = givVal(model_answer2, keywords2, answer2, out_of2)
    print("Marks : " + str(result2))
    Results.update({"result2":result2})

    # For the third answer ->
    answer3 = answers['users1']['a3']
    result3 = givVal(model_answer3, keywords3, answer3, out_of3)
    print("Marks : " + str(result3))
    Results.update({"result3":result3})
    print("Results dictionary",Results)
