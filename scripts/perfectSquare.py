num = 444
sqrtTable = {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}

def sqrt(num):
    lastNums = []
    for i in range(11):
        if str(sqrtTable.get(i))[-1] == str(num)[-1]:
            lastNums.append(i)
    num = str(num)[:-2]
    a_list = list(sqrtTable.values())
    def closest(li,num):
        closest = li[0]
        for i in range(1, len(li)):
            num = int(num)
            print(i)
            if abs(i - num) < closest and abs(i - num) < num:
                closest = i
        return closest
    firstNum = closest(a_list,num)
    print(firstNum)

    
sqrt(num)