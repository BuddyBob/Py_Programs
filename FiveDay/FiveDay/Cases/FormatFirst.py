#This is the second file I created. It helps strip all the unnecessary elements such as 
#Backslashes, provinces, aand quotes
#I need to import pprint so I looks nice if anyone needs to read a certain file
import pprint
def full3(days,YourPath):
    #Deathrep is my temporary list. I used it to edit each row in the raw file.
    CasesRep = []
    #D ended up being my final list so I made it global hence I could use it outside the function
    global D
    D = []
    #Open csv file
    stats = open(str(YourPath)+"Hackathon/time_series_covid19_confirmed_global.csv",'r')
    #Create Death List
    count=0
    for row in stats:
        CasesRep.append(row)
        for i in CasesRep:
            CasesRep = i.split(',')
            if CasesRep[0] == '':
                del CasesRep[0]
        if CasesRep[0].isalpha() == True:
            pass
        if CasesRep[0] == '':
            del CasesRep[0]
        if all(x.isalpha() or x.isspace() for x in CasesRep[1]):
            del CasesRep[0]
            del CasesRep[1]
            del CasesRep[1]
        else:
            del CasesRep[1]
            del CasesRep[1]
        CasesRep[-1] = CasesRep[-1].strip()
        Country = CasesRep[0]
        cases = CasesRep[-days:]
        cases.insert(0,Country)
        D.append(cases)
        CasesRep.clear()
        count = 0
        

    Stats = open(str(YourPath)+"Hackathon/cases/Cases/CasesStats.txt",'w')
    for i in D:
        Stats.write(str(i)+'\n')
    Stats.close()