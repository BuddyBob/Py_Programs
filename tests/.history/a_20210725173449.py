file = open("example.txt")
for line in file:
    print(line.strip(" ").split('='))