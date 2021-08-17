from ast import literal_eval
file = open("example.txt")
output = {line.strip().split('=')[0]:literal_eval(strip().split('=')[1].strip())for line in file}
for line in file:
    your_line = line.strip().split('=')
    key = your_line[0]
    lst = literal_eval(your_line[1].strip())
    output[key] = lst
print(output)
    