from ast import literal_eval
file = open("example.txt")
# lines = [for line in file]
for line in file:
    x = line.strip().split('=')
    print(x)
    lst = literal_eval(x[1])
    print(lst)
    