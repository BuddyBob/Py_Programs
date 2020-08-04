import matplotlib.pyplot as plt
import pprint
def ReadFile():
    rows = 10
    DeathsRep = []
    global D
    D = []
    #Open csv file
    stats = open('/Users/test/Documents/python/Py_Programs/Hackathon/time_series_covid19_deaths_global.csv','r')
    #Create Death List
    count=0
    for row in stats:
        DeathsRep.append(row)
        for i in DeathsRep:
            DeathsRep = i.split(',')
            if DeathsRep[0] == '':
                del DeathsRep[0]
        if DeathsRep[0].isalpha() == True:
            pass
        if DeathsRep[0] == '':
            del DeathsRep[0]
        if all(x.isalpha() or x.isspace() for x in DeathsRep[1]):
            del DeathsRep[0]
            del DeathsRep[1]
            del DeathsRep[1]
        else:
            del DeathsRep[1]
            del DeathsRep[1]
        DeathsRep[-1] = DeathsRep[-1].strip()
        Country = DeathsRep[0]
        Deaths = DeathsRep[-20:]
        Deaths.insert(0,Country)
        D.append(Deaths)
        DeathsRep.clear()
        count = 0
        
ReadFile()
pprint.pprint(D)
Stats = open('DeathStats.txt','w')
for i in D:
    Stats.write(str(i)+'\n')
Stats.close()