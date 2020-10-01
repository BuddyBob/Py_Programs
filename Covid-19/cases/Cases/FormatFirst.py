
import pprint
def full3(days,YourPath):

    CasesRep = []

    global D
    D = []
    stats = open(str(YourPath)+"Covid-19/time_series_covid19_confirmed_global.csv",'r')

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
        

    Stats = open(str(YourPath)+"Covid-19/cases/Cases/CasesStats.txt",'w')
    for i in D:
        Stats.write(str(i)+'\n')
    Stats.close()