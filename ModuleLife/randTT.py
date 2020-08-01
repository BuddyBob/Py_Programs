#I am just learnin modules so dont get mad because I am using random module to create a 
#random module. It is for learning purpouses
from random import randint
def random(num1,num2):
    if num1 > num2:
        print('An error occured: num1 must NOT be greater than num2')
        exit()
    exceed = False
    return randint(num1,num2)

