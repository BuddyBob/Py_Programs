import  matplotlib.pyplot as plt
stats = open('DeathStats.txt','r')
count1 = 0
count2 = 1
L = []
full = []
CountryList = []
countryName = ''
similar = open('similar.txt','w')
for i in stats:
    row = stats.readline()
    row = row[1:]
    row = row[:-2]
    L.append(row)
    for i in L:
        L = i.split(',')
    L = [i.replace('\'','') for i in L]
    if L[0] == countryName:
        similar.write(str(L)+'\n')
        countryName = L[0]
    else:
        countryName = L[0]
similar.close()





