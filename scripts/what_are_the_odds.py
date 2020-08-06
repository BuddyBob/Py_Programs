from random import randint
Base = 10
for i in range(10):
    one = []
    two =[]
    for i in range(Base):
        number = randint(1,2)
        if number == 1:
            one.append(number)
        else:
            two.append(number)
    print('One: '+str(len(one))+str('/')+str(Base))
    print('Two: '+str(len(two))+str('/')+str(Base))
    print('--------------------------------------')