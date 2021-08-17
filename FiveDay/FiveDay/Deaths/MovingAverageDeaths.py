import re
def full(YourPath):
    file = open(str(YourPath)+'Hackathon/FiveDay/Deaths/Final.txt','r')
    file.readline()
    Final = []
    for row in file:
        L = []
        countRep = 0
        count = 10
        count2 = 5
        countRep +=1
        Country = ''
        row = row.replace('\'','')
        row = row.replace(']','')
        row = row.replace('[','')
        row = row.split(',')
        row[-1] = re.sub('\\\\n|\n', '' , row[-1])
        row[-1] = row[-1].strip()
        Country = row[0]
        row = [elements.strip() for elements in row]
        row[1:] = [int(i) for i in row[1:]]
        for i in range(38):
            if countRep == 1:
                L.append(sum(row[-5:None])/5)
                countRep += 10000
            else:
                print(row[-count:-count2])
                try:
                    L.append(sum(row[-count:-count2])/5)
                except:
                    pass
            count += 5
            count2 +=5
        L.reverse()
        L.insert(0,Country)  
        Final.append(L)
    print(Final)
    secondFile =  open(str(YourPath)+'Hackathon/FiveDay/Deaths/Final.txt','w')
    for lists in Final:
        secondFile.write(str(lists)+'\n')
    secondFile.close()
