def remove(l):
    used = []
    [used.append(syms) for syms in l if syms not in used]
    return used
list1 = [1,2,2,3,4,5,6,7,7,7,8,8,4]
print(remove(list1))


