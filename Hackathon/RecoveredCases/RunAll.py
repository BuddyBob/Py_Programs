import sys
import os
#PLEASE READ INSTRUCTIONS FILE BEFORE RUNNING
file = open('/Users/test/Documents/python/Py_Programs/Hackathon/RecoveredCases/Info.txt','r')
YourPath = file.readline().strip()
Max = file.readline()
sys.path.insert(1, str(YourPath)+'Hackathon/RecoveredCases/recovered')
days = int(Max)
count = 0
try:
    for file in os.listdir(YourPath):
        if file == 'Hackathon':
            count+=1
    if count == 0:
        print('Change Your Path, It does not contain Hackathon Folder')
        print('You can do this in the GlobalVar file')
        exit()
    else:
        print('Good Path')
except FileNotFoundError:
    print("Sorry we could not find a Hackathon Folder in that dirctory")
    exit()
from RecoveredCases import GetFiles
from Format import full
full(days,YourPath)
from SpitProvinces import full
full(days,YourPath)
from ManageFiles import full
full(YourPath)
from UI import full
full(YourPath)