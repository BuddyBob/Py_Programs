#This is the third file.
#It takes all the countries in the similar.json file and writes it into a file called 'final.txt'
#It also takes all countries in Recovered.txt a file we created using the WriteDeaths.py file (Except countries that we have in our similar.json)
#* Thee whole process looks a bit like this
#!=================================================
#? Recovered.txt(Countries with no provinces) –––––––
#?                                                    | 'final.txt'
#? Similar.json(Countries with provinces[addedUp]) ––––
#!=================================================

import json
c = []
def full(YourPath):
    #Open json file
    with open(str(YourPath)+"Covid-19/RecoveredCases/Recovered/similar.json", "r") as read_file:
        data = json.load(read_file)
        #Store Deaths and Countries
        keys = list(data.keys())
        values = list(data.values())
    #Open Recovered file
    check = open(str(YourPath)+"Covid-19/RecoveredCases/Recovered/Recovered.txt")
    #Create file to write all rows of data
    lastFile = open(str(YourPath)+"Covid-19/RecoveredCases/Recovered/Final.txt",'w')
    L = []
    #Iterate through Recovered.txt turn each str(row) into list
    for row in check:
        row = row.replace('\'','')
        row = row.replace(']','')
        row = row.replace('[','')
        row = row.split(',')
        #If the country does not xxxain a province it is approved and is written to Final.txt
        if row[0] not in keys:
            lastFile.write(str(row)+'\n')
    #Close this file because it is no longer usefull
    check.close()
    #Take all elements in .json file and write it to 'final.txt'(In the same format as above)
    for i in range(len(keys)):
        values[i].append(keys[i])
    for subList in values:
        subList.insert(0, subList.pop())
    for i in range(len(keys)):
        lastFile.write(str(values[i])+'\n')
