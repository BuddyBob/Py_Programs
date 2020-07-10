import random
from random import randint
from colorama import  *
import time
gen = randint(10,20)
space = gen
space_c = gen
print(Fore.BLUE+"There are "+str(space)+" Spaces in this game")
while space >= 0 or space_c >= 0:
    print(Fore.YELLOW+'-----------------')
    human_roll = (input("r to roll: ")) 
    if human_roll == 'r':
        h_r = randint(1,6)
        print(Fore.GREEN+'You rolled a '+str(h_r))
        space = space - h_r
        if space<=0:
            print('0 more to go')
        else:
            print(Fore.GREEN+str(space)+' to go')
        print(Fore.YELLOW+'-----------------')
    print("cpu rolling")
    c_r = randint(1,6)
    print(Fore.GREEN+"cpu rolled a "+str(c_r))
    space_c = space_c - c_r
    if space_c<=0:
        print('0 more to go')
    else:
        print(str(space_c)+' more to go')
    print(Fore.BLUE+'---------------------------------------------------------------------')
    print('cpu: '+str(space_c)+' <--> you: '+str(space))
    if space_c <= 0 and space_c<space:
        print(Fore.RED+'YOU LOSE')
        break
    if space <= 0 and space<space_c:
        print(Fore.GREEN+'YOU WIN')
        import pdb; pdb.set_trace()
        break
    if space <= 0 and space_c <= 0 and space==space_c:
        print(Fore.GREEN+'YOU TIED')
        break