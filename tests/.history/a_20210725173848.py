from ast import literal_eval
file = open("example.txt")
# lines = [for line in file]
for line in file:
    your_line = line.strip().split('=')
    k = your_line[0]
    lst = literal_eval(x[1].str)
    print(lst)
    