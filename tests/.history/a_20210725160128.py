your_list = [5,4,3,2,1,0,0,0,-1,-2]
newList = []
zeros = [[0]*your_list.count(0)][0]
noZeros = [i for i in your_list if i != 0]
print(noZeros)

x = noZeros.extend(zeros)
print(x)