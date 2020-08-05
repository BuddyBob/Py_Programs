import sys
from GlobalVar import Max,YourPath
import os
#PLEASE READ INSTRUCTIONS FILE BEFORE RUNNING
sys.path.insert(1, str(YourPath)+'Hackathon/DeathStats/Deaths')
Countries = 'Germany,France' 
days = Max
count = 0
for file in os.listdir(YourPath):
    if file == 'Hackathon':
        count+=1
if count == 0:
    print('Change Your Path, It does not contain Hackathon Folder')
    print('You can do this in the GlobalVar file')
    exit()
else:
    print('Good Path')
import GetFiles
from Format import full
full(days,YourPath)
from SpitProvinces import full
full(days,YourPath)
from ManageFiles import full
full(YourPath)
from UI import full
full(YourPath)