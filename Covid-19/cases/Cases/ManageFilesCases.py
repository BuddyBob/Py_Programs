import json
c = []
def full(YourPath):

    with open(str(YourPath)+"Covid-19/cases/Cases/similar.json", "r") as read_file:
        data = json.load(read_file)

        keys = list(data.keys())
        values = list(data.values())

    check = open(str(YourPath)+"Covid-19/cases/Cases/CasesStats.txt")

    lastFile = open(str(YourPath)+"Covid-19/cases/Cases/Final.txt",'w')
    L = []

    for row in check:
        row = row.replace('\'','')
        row = row.replace(']','')
        row = row.replace('[','')
        row = row.split(',')

        if row[0] not in keys:
            lastFile.write(str(row)+'\n')

    check.close()

    for i in range(len(keys)):
        values[i].append(keys[i])
    for subList in values:
        subList.insert(0, subList.pop())
    for i in range(len(keys)):
        lastFile.write(str(values[i])+'\n')
