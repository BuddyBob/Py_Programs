  
import pprint
def full(days,YourPath):
    #Deathrep is my temporary list. I used it to edit each row in the raw file.
    DeathsRep = []
    #D ended up being my final list so I made it global hence I could use it outside the function
    global D
    D = []
    #Open csv file
    stats = open(str(YourPath)+"Covid-19/time_series_covid19_deaths_global.csv",'r')
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
        Deaths = DeathsRep[-days:]
        Deaths.insert(0,Country)
        D.append(Deaths)
        DeathsRep.clear()
        count = 0
        

    Stats = open(str(YourPath)+"Covid-19/DeathStats/Deaths/DeathStats.txt",'w')
    for i in D:
        Stats.write(str(i)+'\n')
    Stats.close()