file = open('similar.txt','r')
L = []
for i in file:
    row = file.readline()
    row = row[1:]
    row = row[:-2]
    L.append(row)
    for i in L:
        L = i.split(',')
    L = [i.replace('\'','') for i in L]
    print(L[0])