# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:12:15 2020

@author: keval
"""

def coding_mcq():
    print("Now you will have your Mutltiple choice question test")
    print("Each question will have 4 answers and you have to select one ")
    print("Here are your questions")
    
    count = 0
    ans1 = input("With what data structure can a priority queue be implemented?\n"\
          "a) Array\n"\
          "b) List\n"\
          "c) Heap\n"\
          "d) Tree\n")
    if ans1.lower() == "d":
        count+=1
    ans2 = input("Architecture of database is viewed as?\n"\
          "a) two level\n"\
          "b) four level\n"\
          "c) three level\n"\
          "d) one level\n")
    if ans2.lower() == "c":
        count+=1
        
    ans3 = input(" _____ is used to find and fix bugs in the Java programs.\n"\
          "a) JVM\n"\
          "b) JRE\n"\
          "c) JDK\n"\
          "d) JDB\n")
    if ans3.lower() == "d":
        count+=1
    
    ans4 = input(" Study the following program:\n"\
                 "x = ['xy', 'yz']\n"\
                 "for i in a: \n" \
                     "\ti.upper()\n" \
                  "print(a)\n"\
                  "options\n"\
                 "a) ['xy', 'yz']\n"\
                 "b) ['XY', 'YZ']\n"\
                 "c) [None, None]\n"\
                 "d) [None of these]\n"
                 )
    
        
    if ans4.lower() == "a":
        count+=1
    
    ans5 = input("Which of the following requires a device driver?\n"\
                 "a) Register\n"\
                 "b) Cache\n"\
                 "c) Main memory\n"\
                 "d) Disk\nd"
                 )
    if ans5.lower() == "d":
        count+=1
    
    
    print(count)
    return count

    
