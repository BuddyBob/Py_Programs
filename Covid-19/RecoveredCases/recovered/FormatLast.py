  
import pprint
def full(days,YourPath):
    #Recrep is my temporary list. I used it to edit each row in the raw file.
    Recrep = []
    #R ended up being my final list so I made it global hence I could use it outside the function
    global D
    D = []
    #Open csv file
    stats = open(str(YourPath)+"Covid-19/time_series_covid19_recoveredGlobal.csv",'r')
    #Create Death List
    count=0
    for row in stats:
        Recrep.append(row)
        for i in Recrep:
            Recrep = i.split(',')
            if Recrep[0] == '':
                del Recrep[0]
        if Recrep[0].isalpha() == True:
            pass
        if Recrep[0] == '':
            del Recrep[0]
        if all(x.isalpha() or x.isspace() for x in Recrep[1]):
            del Recrep[0]
            del Recrep[1]
            del Recrep[1]
        else:
            del Recrep[1]
            del Recrep[1]
        Recrep[-1] = Recrep[-1].strip()
        Country = Recrep[0]
        Recovered = Recrep[-days:]
        Recovered.insert(0,Country)
        D.append(Recovered)
        Recrep.clear()
        count = 0
        

    Stats = open(str(YourPath)+"Covid-19/RecoveredCases/Recovered/Recovered.txt",'w')
    for i in D:
        Stats.write(str(i)+'\n')
    Stats.close()