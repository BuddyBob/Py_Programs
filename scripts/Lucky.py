import random
number = []
for i in range(5):
    num = random.randint(1,69)
    number.append(num)
print('power ball: '+str(number))


def Guess(UserNumber):
    for i in range(5):
        num = random.randint(1,69
        )
        UserNumber.append(num)
count = 0
while True:
    UserNumber = []
    count += 1
    guess = Guess(UserNumber)
    if count % 1000000 == 0:
        zC = 0
        for zeros in str(count):
            if zeros == str(0):
                zC += 1
        print(f'{count} | zeros: ({zC})')
    if number == guess:
        print('You won 1 million dollars: '+str(UserNumber))
        print('It took you'+str(count)+'tries!')
        break
