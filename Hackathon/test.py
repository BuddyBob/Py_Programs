import operator
L = [['b','7'],['a','4'],['c','2']]
print(sorted(L, key=operator.itemgetter(0)))