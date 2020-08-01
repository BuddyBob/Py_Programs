import random
from random import randint
import sys
import time
from termcolor import *
from colorama import *
init()
start_y = False
start_n = False
cpu = False
cpu_vs_you = False
#CHOOSE GAME MODE
print(Fore.GREEN+"A game made by Thavas Antonio")
time.sleep(2)
print(Fore.MAGENTA+'==============================')
time.sleep(1)
print(Fore.GREEN+"Instructions")
print(Fore.GREEN+'''This is a game all about luck. Not about skill but only about luck. This is an experiment to
check if us humans are in danger and if we should stop making advances in AI and robotics. The purpouse of 
this test is to see if robots are smart enough to beat us in a test of luck. If this
test shows positive, we must destroy all tech created so that the robots do not take over. If this
test comes back negative we are fine but still must be careful about how we deal with tech and our advancements 
in AI. It is your job to test this well created game and, please, please for us and everyone on the face of Earth,
Beat the Bot. Would you like to start or chicken out''')
start = (input())
if start == 'chicken out':
    start_n = True
    print(Fore.RED+"WOOOOOWWW you are not very nice!")
if start == 'start':
    print(Fore.GREEN+"You will go down in history")
    start_y = True
if start_y == False and start_n == False:
    if len(start)<=5:
        he_did_start=(input(Fore.RED+'Did you mean to start, please tell me you said yes [y/n]'))
        if he_did_start == 'y':
            print(Fore.GREEN+'Ok thank god dont scare me like that!')
            start_y = True
        if he_did_start == 'n':
            print(Fore.RED+'Welp! you were our last chance')
            start_n = False
            exit()
        if he_did_start != 'y' and he_did_start != 'n':
            print(Fore.RED+"How are you going to test this if you cant even type \'n or y\'?")
            exit()
if start_y == False and start_n == False:
    if len(start)>5:
        he_did_not_start=(input(Fore.RED+'Please tell me you meant to say start and not to chicken out! [y,n]'))
        if he_did_not_start == 'n':
            print(Fore.RED+'darnit! you were our last chance!')
            start_n = False
            exit()
        if he_did_not_start == 'y':
            print(Fore.GREEN+'Ok phew! Dont scare me like that again')
            start_y = True
        if he_did_not_start != 'y' and he_did_not_start != 'n':
            print(Fore.RED+"How are you going to save humanity if you cant type \'y\' or \'n\' ")
            start_n = False
if start_y == True:
    print(Fore.YELLOW+"Which game mode would you like? [\"cpu\" or \"cpu vs you\"]")
    game_m = (input())
    if game_m == "cpu":
        cpu = True
    if game_m == "cpu vs you":
        cpu_vs_you = True
    if cpu_vs_you == False and cpu == False:
        if len(game_m) >= 5:
            print(Fore.RED+"an error occured")
            print(Fore.BLUE+"did you mean \'cpu vs you\'?[y/n] ")
            dym_a = (input())
            if dym_a ==  'y':
                print(Fore.RED+"Ok next time check your spelling")
                print(Fore.YELLOW+"Lets continue shall we")
                time.sleep(1)
                cpu_vs_you = True
            else:
                print(Fore.GREEN+"Ok thank you for playing")
                exit()
    if cpu_vs_you == False and cpu == False:
        if len(game_m) <= 3:
            print(Fore.RED+'an error occured')
            print(Fore.BLUE+"did you mean to say\'cpu\'[y/n] ")
            dym_b = (input())
            if dym_b == 'y':
                print(Fore.RED+'Ok next time check your spelling')
                print(Fore.YELLOW+'Ok lets continue then')
                cpu = True 
            else:
                print(Fore.GREEN+'Ok thanks for playing')
                exit()

    #CPU ONLY OPTION HAS BEEN CHOSEN   
    if cpu == True:
        #SET OPTIONS
        time.sleep(1)
        tries_a = int(input("How many tries: "))
        x = int(input("Enter the smallest number in this guess game: "))
        y = int(input("Enter the largest number in this guess game: "))
        cpu_correct = 0
        #DO NOT ALLOW THEM TO ENTER Y > X BEACAUSE THAT DOES NOT MAKE SENSE
        if y < x:
            cprint("follow instructions","red")
            sys.exit()
        tries_g = 0
        num = randint(x,y)
        #GIVE USER INFO ABOUT CPU'S NUMBER
        print(Fore.WHITE+"The number the cpu is trying to guess is: "+str(num))
        #CPU RUN CODE
        while cpu_correct == 0 and tries_g < tries_a:
            cpu = randint(x,y)
            if cpu == num:
                print(Fore.GREEN+str(cpu)+" cpu is correct")
                cpu_correct += 1
            else:
                tries_g += 1
                time.sleep(.3)
                print(cpu)
        if cpu_correct == 0:
            cprint("The cpu did not get anything correct","red")
        if cpu_correct > 0:
            print(str(cpu_correct)+" out of "+str(+tries_a))
            print(cpu_correct/tries_a*100)
        print(Fore.YELLOW+"==========================================================")
        exit()
    #======================================================================
    #COU VS YOU | YOUR TURN
    if cpu_vs_you == True:
        till_cc = 0
        given_tries = 0
        tries_attempted = 0
        correct_player = 0
        given_tries = int(input("How many tries would you like?: "))
        x_ = int(input("Enter a the smallest number possible to guess:"))
        y_ = int(input("Enter a the largest number possible to guess:"))
        if y_ < x_:
            cprint("follow instructions","red")
            sys.exit()
        p_correct = 0
        generate_number = randint(x_,y_)
        
        while given_tries > tries_attempted:
            ask = int(input("Guess: "))
            if ask == generate_number:
                
                print(Fore.GREEN + 'BINGO you got the GUESSED the number '+str(generate_number))
                
                tries_attempted += 1
                till_cc += 1
                correct_player += 1
                break
            if ask != generate_number:
                till_cc += 1
                tries_attempted += 1
        if correct_player == 0:
            print(Fore.RED+"You did not get anything correct, the number was "+str(generate_number))
            
        if correct_player == 1:
            print(Fore.YELLOW+"It took you "+str(till_cc)+" attempts to guess the number out of "+str(given_tries))
        number_thing = till_cc/given_tries
        cprint('______________________________________','yellow')
        #CUP'S TURN
        time.sleep(1)
        print(Fore.WHITE+"Now it is the cpu's turn")
        cpu_generate_number = randint(x_,y_)
        cpu_find_number = randint(x_,y_)
        till_c = 0
        tries_attempted = 0
        
        print(Fore.WHITE+"The number the cpu has to guess is: "+str(cpu_generate_number))
        time.sleep(4)
        print(Fore.WHITE+"guessing...")
        time.sleep(2)
        cpu_correct = 0
        if y_ < x_:
            cprint("follow instructions","red")
            sys.exit()
        tries_g = 0
        while tries_attempted < given_tries:
            cpu = randint(x_,y_)
            if cpu == cpu_generate_number:
                cprint(str(cpu)+", The cpu guessed accurately","green")
                cpu_correct += 1
                tries_attempted += 1
                till_c += 1
                break
            else:
                tries_attempted += 1
                till_c += 1
                cprint(cpu,'blue')
                time.sleep(.5)
                
        if cpu_correct == 1:        
            print(Fore.YELLOW+"It took the cpu "+str(till_c)+" attempts to guess the number out of "+str(given_tries))
        if cpu_correct == 0:
            cprint("The cpu did not guess the number","red")
        number_thing_two = till_c/given_tries
        cpu_string = ''
        player_string = ''
        winner_cpu = False
        winner_player = False
        if till_cc > till_c:
            winner_cpu = True
        if till_cc < till_c:
            winner_player = True
        
                
        time.sleep(2)
        if cpu_correct == 1 and correct_player == 1:
            print(Fore.MAGENTA+"We just got the back information that it took you "+str(till_cc)+" tries to guess the correct number")
            print(Fore.MAGENTA+"The computer took "+str(till_c)+" tries to guess the correct number")
        if cpu_correct == 1 and correct_player == 0:
            print(Fore.MAGENTA+"We just got the back information that it took you "+str(till_cc)+" tries to guess the correct number but you did not guess the number")
            print(Fore.MAGENTA+"The computer took "+str(till_c)+" tries to guess the correct number")
        if cpu_correct == 0 and correct_player == 1:
            print(Fore.MAGENTA+"We just got the back information that it took you "+str(till_cc)+" tries to guess the correct number")
            print(Fore.MAGENTA+"The computer took "+str(till_c)+" tries to guess the correct number and it still did not get it correct")
        if cpu_correct == 0 and correct_player == 0:
            print(Fore.MAGENTA+"We just got the back information that it took you "+str(till_cc)+" tries to guess the correct number but you did not guess the number")
            print(Fore.MAGENTA+"The computer took "+str(till_c)+" tries to guess the correct number and it still did not get it correct")
        time.sleep(4)
        if till_cc < till_c:
            print(Fore.GREEN+"THAT MEANS YOU WIN")
        if till_cc > till_c:
            print(Fore.RED+"THAT MEANS THE CPU WINS")
        if till_cc == till_c:
            print(Fore.BLUE+"THAT MEANS THERE WAS A TIE")
            
        












        

