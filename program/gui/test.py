import os
import json

local_path = os.getcwd()
parent_path = os.path.dirname(local_path)
filename = os.path.join( str(local_path),"gui", "data.json")
print(filename)
f = open(filename, "r")
data = json.load(f)
		
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
print(question)