from colorama import Fore
import time
import random
from random import randint
average = []
def readFile():
    global sentance
    sentance = []
    file = open('sentances.txt','r')
    for sent in file:
        sentance.append(sent)
    sentance = [s.rstrip() for s in sentance]
readFile()
while True:  
    readFile()
    file = open('sentances.txt','r')
    for sent in file:
        sentance.append(sent)
    sentance = [s.rstrip() for s in sentance]
    sentance = random.choice(sentance)
    main = sentance
    while True:
        start_time = time.time()
        print(main)
        userSent = str(input(': '))
        if userSent == 'average':
            try:
                print('Your average time is {} '.format(sum(average)/len(average)))
                print('-------------------------------------------------')
                break
            except ZeroDivisionError:
                print('You have no times yet')
            break
        endTime = time.time() - start_time
        sentance = list(sentance)
        userSent = list(userSent)
        count = 0
        if len(userSent) != len(sentance):
            print('Incorrect')
        else:
            print('Your time was {}'.format(endTime))
            average.append(endTime)
            break
    try:
        for i in userSent:
            if i != sentance[count]:
                print('Check for letter {} at position {}'.format(i,count))
            count+=1
        print('------------------------------------------------')
    except IndexError:
        pass