# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:49:28 2020

@author: keval
"""


from os import path
from pydub import AudioSegment

# files                                                                         
src = "transcript.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")