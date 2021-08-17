from ast import literal_eval
file = open("example.txt")
lines = [for line in file]
for line in file:
    x = line.strip().replace(" ","").split('=')
    lst = x[1]
    