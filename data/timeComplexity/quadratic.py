# user list input
a = [int(x) for x in input("List 1: ").split()]
b = [int(y) for y in input("List 2: ").split()]
print(sorted(a+b,reverse=True))



