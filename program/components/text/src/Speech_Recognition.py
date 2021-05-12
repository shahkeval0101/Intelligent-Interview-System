# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:17:34 2020

@author: keval
"""
import os
import speech_recognition as sr
def speech_recognition(filename):
    #print(sr.__version__)
    
    r = sr.Recognizer()
    text = ""
    harvard = sr.AudioFile(filename)
    with harvard as source:
        audio = r.record(source)
    type(audio)
    text = r.recognize_google(audio)
    return text


#local_path = os.getcwd()
#parent_path = os.path.dirname(local_path)
#filename = os.path.join( str(parent_path) ,"audio","audio_wav1.wav")
#text = speech_recognition(filename)
#print(text)