import json
def full():
    with open("/Users/test/Documents/python/Py_Programs/Hackathon/Deaths/similar.json", "r") as read_file:
        data = json.load(read_file)
        keys = list(data.keys())
        values = list(data.values())
    check = open("/Users/test/Documents/python/Py_Programs/Hackathon/Deaths/DeathStats.txt")
    lastFile = open("/Users/test/Documents/python/Py_Programs/Hackathon/Deaths/Final.txt","a")
    L = []
    for row in check:
        row = row.replace('\'','')
        row = row.replace(']','')
        row = row.replace('[','')
        row = row.split(',')
        if row[0] not in keys:
            lastFile.write(str(row)+'\n')
        print('------------')
    check.close()
    for i in range(len(keys)):
        values[i].append(keys[i])
    for subList in values:
        subList.insert(0, subList.pop())
    for i in range(len(keys)):
        lastFile.write(str(values[i])+'\n')
    lastFile.close()