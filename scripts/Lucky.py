import random
number = []
for i in range(5):
    num = random.randint(1,69)
    number.append(num)
print('power ball: '+str(number))


def Guess(UserNumber):
    for i in range(5):
        num = random.randint(1,69)
        UserNumber.append(num)
count = 0
while True:
    UserNumber = []
    count += 1
    guess = Guess(UserNumber)
    if count % 100 == 0:
        print(count)
    if UserNumber == guess:
        print('You won 1 million dollars: '+str(UserNumber))
        print('It took you'+str(count)+'tries!')
        break
