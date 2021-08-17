import random
numberSet = ['1','2','3','4','5','6','7','8','9']
numberList = []
numbersReduced = []
for i in range(1,random.randint(5,10)):
        num = random.choice(numberSet)
        number = num*random.randint(1,6)
        numberSet.remove(num)
        numberList.append(number)
print(numberList)
for bigNums in numberList:
    amount = len(bigNums)
    bigNums = bigNums[0]

    bigNums = str(amount)+bigNums
    numbersReduced.append(bigNums)
print(numbersReduced)
