
from itertools import groupby
from operator import add
import json
import operator
def full(days,YourPath):

    stats = open(str(YourPath)+'Covid-19/cases/Cases/CasesStats.txt','r')

    stats.readline()

    L = []

    country = ''

    for row in stats:

        row = row.replace('\'','')
        row = row.replace(']','')
        row = row.replace('[','')
        row = row.split(',')
        if row[0] == country:
            L.append(row)
        else:
            country = row[0]
    grouped_lists = {}
    for xs in L:

        c = xs[0]
        vals = xs[1:]
        assert len(vals) == days

        nums = [int(v.strip()) for v in vals]

        grouped_lists.setdefault(c, []).append(nums)


    country_totals = {}
    for c, xss in grouped_lists.items():

        country_totals[c] = []

        for tup in zip(*xss):
            country_totals[c].append(sum(tup))
    sim = open(str(YourPath)+'Covid-19/cases/Cases/similar.json','w')
    sim.write(json.dumps(country_totals))
    sim.close()