count = 0
from colorama import *
mydict = {
  "1+1": "2" , "2+2":"4", "4+4":"8"
}
length = len(mydict)
print(length)
i = 0
while i < length:
    question = (list(mydict.keys())[count])
    print(Fore.BLUE+"question "+str(question))
    guess = int(input(Fore.YELLOW+'guess: '))
    answer = (list(mydict.values())[count])
    if str(guess) == answer:
        print(Fore.GREEN+'correct')
        count+=1
        i +=1 
    else:
        print(Fore.RED+'incorrect')
        count+=1
        i +=1 

