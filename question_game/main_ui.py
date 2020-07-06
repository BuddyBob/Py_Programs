import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
application_window = tk.Tk()
count = 0
from colorama import *
hint_count = 0
mydict = {

    "Which Jamaican runner is an 11-time world champion and holds the record in the 100 and 200-meter race?": "usain bolt",
    "Which boxer was known as “The Greatest” and “The People’s Champion”?":"muhammad ali", 
    "Which lightweight boxer had a 43-0 professional record?":"floyd mayweather",
    "How do you find the length of a list,tuple,variable,int or dictionary?":"len()",
    "what module is used to automate websites?":"selenium",
    "what does \"A.I\" stand for?":"artificial intelligence",
    "How much do the apple wheels cost?":"$700 dollars",
    "Who is the richest man in the world?":"jeff bezos",
    "I make two people out of one. What am I?":"a mirror",
    '''While on my way to St. Ives, I saw a man with 7 wives. Each wife had 7 sacks. each sack 
    had 7 cats. Each cat had 7 kittens. Kitten, cats, sacks, wives, How many were going to St. Ives?''':"1",
    "What runs around the whole yard without moving?":"a fence",
    "7-24÷8•4+6":"1"

}
length = len(mydict)
start = messagebox.showinfo("Information",str(length)+' question game')
i = 0
correct = 0
ch = False
while i < length:
    #select question
    if ch == False:
        question = (list(mydict.keys())[count])
        guess = simpledialog.askstring('ask',str(question),
                                    parent=application_window)
        guess = guess.lower()
    #check for keys value
    answer = (list(mydict.values())[count])
    hint = len(answer)/3
    hint = int(hint)
    take = answer[0:hint]
    #correct?
    if str(guess) == answer:
        correct += 1
        messagebox.showinfo("Information",'correct')
        count+=1
        i +=1 
    #hint?
    elif guess == 'hint' and hint_count < 3:
        hint_count+=1
        messagebox.showinfo("Information",str(take))
    elif guess == 'hint' and hint_count >= 3:
        hint_count+=1
        messagebox.showinfo("error","No more hints left")
        #wrong

    else:
        messagebox.showinfo("Information",'Incorrect')
        count+=1
        i +=1 
#how many out of how many
messagebox.showinfo("Information",str(correct)+'/'+str(length))

