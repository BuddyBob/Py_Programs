num = 104329
sqrtTable = {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
def sqrt(num):
    squaredNum = num
    lastNums = []
    for i in range(11):
        if str(sqrtTable.get(i))[-1] == str(num)[-1]:
            lastNums.append(i)
    lastNums.sort()
    num = str(num)[:-2]
    def closest(num):
        count = 0
        possibles = []
        while True:
            if count * count <= int(num):
                possibles.append(count)
                count += 1
            else:
                possibles.sort()
                return possibles[-1]
    firstNum = closest(num)
    if len(lastNums) > 1:
        nextNum = firstNum*(firstNum+1)
        if  int(num)>nextNum:lastNums = lastNums[-1]
        if int(num)<nextNum:lastNums = lastNums[0]
    return f'square of {squaredNum} = {str(firstNum)+str(lastNums)}'  
print(sqrt(num))