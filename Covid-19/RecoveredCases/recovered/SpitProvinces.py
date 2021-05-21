#This file was created just to read the file RecoveredStats and add up all the provinces to make only one 
#List per country
from itertools import groupby
from operator import add
import json
import operator
def full(days,YourPath):
    stats = open(str(YourPath)+'Covid-19/RecoveredCases/Recovered/Recovered.txt','r')
    #* I added this extra readline at the start to skip the first line which was a .csv header
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
    #print(sorted(L, key=operator.itemgetter(0)))
    grouped_lists = {}
    for xs in L:
        # Grab country name and the rest of the values.
        c = xs[0]
        vals = xs[1:]
        assert len(vals) == days
        # Convert the values to integers using a list comprehension.
        nums = [int(v.strip()) for v in vals]
        # Add the list of numbers to the country's list-of-lists.
        grouped_lists.setdefault(c, []).append(nums)

    # Sum up the separate lists for each country.
    country_totals = {}
    for c, xss in grouped_lists.items():
        # Initialize the key for the country.
        country_totals[c] = []
        # Since xss is a list-of-lists for the current country, we can use zip() to
        # weave together the values based on their positions (or indexes). For
        # example, on the first iteration tup will be a tuple holding the first
        # elements from the separate lists. On second iteration, second elements. Etc.
        for tup in zip(*xss):
            country_totals[c].append(sum(tup))

    sim = open(str(YourPath)+'Covid-19/RecoveredCases/Recovered/similar.json','w')
    sim.write(json.dumps(country_totals))
    sim.close()