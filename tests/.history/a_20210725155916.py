your_list = [5,4,3,2,1,0,0,0,-1,-2]
newList = []
for element in your_list:
  noZeros = [i for i in your_list if i != 0]
  zeros = [[0]*your_list.count(0)]
  