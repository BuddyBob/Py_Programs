from ast import literal_eval
file = open("example.txt")
output = {line.strip().split('=')[0]:literal_eval(line.strip().split('=')[1].strip()) for line in file}
print(output)
    