# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:22:22 2020

@author: keval
"""

import os
script_dir = os.path.dirname(__file__)
rel_path = "audio/audio_wav1.wav"
abs_file_path = os.path.join(script_dir, rel_path)



local_path = os.getcwd()
parent_path = os.path.dirname(local_path)
print(local_path)
print(parent_path)
filename = os.path.join( str(local_path) ,"audio","audio_wav1.wav")
print(filename)