import re
def full(Countries):
    L = []
    Country = []
    Countries = Countries.split(',')
    for countries in Countries:
        Country.append(countries)
    file = open('/Users/test/Documents/python/Py_Programs/Hackathon/Deaths/Final.txt','r')
    for row in file:
        row = row.replace('\'','')
        row = row.replace(']','')
        row = row.replace('[','')
        row = row.split(',')
        if row[0] in Country:
            L.append(row)
    for lists in L:
        lists[-1] = re.sub('\\\\n|\n', '' , lists[-1])