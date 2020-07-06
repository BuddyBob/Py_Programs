count = 0
from colorama import *
mydict = {
  "Which Jamaican runner is an 11-time world champion and holds the record in the 100 and 200-meter race?": "usain bolt" ,
   "Which boxer was known as “The Greatest” and “The People’s Champion”?":"muhammad ali", 
   "Which lightweight boxer had a 43-0 professional record?":"floyd mayweather",
   "How do you find the length of a list,tuple,variable,int or dictionary?":"len()",
   "what module is used to automate websites?":"selenium",
   "what does \"A.I\" stand for?":"artificial intelligence",
   "How much do the apple wheels cost?":"$700 dollars",
   "Who is the richest man in the world?":"jeff bezos"
}
print('tpe hint to get a hint')
length = len(mydict)
print(str(length)+' question game')
i = 0
correct = 0
ch = False
while i < length:
    #select question
    question = (list(mydict.keys())[count])
    if ch == False:
        print(Fore.BLUE+"question: "+str(question))
    ch = False
    #ask for guess
    guess = (input(Fore.YELLOW+'guess: '))
    guess = guess.lower()
    #check for keys value
    anwser = (list(mydict.values())[count])
    hint = len(answer)/3
    hint = int(hint)
    take = answer[0:hint]
    #correct?
    if str(guess) == answer:
        correct += 1
        print(Fore.GREEN+'correct')
        count+=1
        i +=1 
    #hint?
    elif guess == 'hint':
        print(Fore.BLUE+take)
        ch = True
        #wrong

    else:
        print(Fore.RED+'incorrect')
        count+=1
        i +=1 
#how many out of how many
print(str(correct)+'/'+str(length))

