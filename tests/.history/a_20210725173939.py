from ast import literal_eval
file = open("example.txt")
# lines = [for line in file]
for line in file:
    your_line = line.strip().split('=')
    key = your_line[0]
    lst = your_line[1]
    print(lst)
    