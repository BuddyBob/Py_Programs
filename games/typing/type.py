from tkinter import *
from difflib import SequenceMatcher
import random
#get sentences
file = open('/Users/aspera/Documents/Python/Py_Programs/games/typing/sentences.py','r')
sentences = [sen.strip() for sen in file.readlines()]
#set tk
tk = Tk()
sv = StringVar()
tk.geometry("1000x100")

#display text
while True:
    def getSentence(sentences):
        global s
        s = random.choice(sentences)
        sv.set(s)
    #submit
    def onclick(event=None):
        userInput = inp.get()
        chosen = s
        stat.config(text = f'Accuracy: {round((SequenceMatcher(None, userInput, chosen).ratio())*100,2)}')
    def nextUp(stat,inp):
        getSentence(sentences)
        stat.config(text='')
        inp.delete(0,'end')
    tk.bind('<Return>', onclick)
    label = Label(tk,text='',textvariable=sv)
    label.pack()
    getSentence(sentences)
    inp = Entry(tk,text='enter here',width=50)
    inp.pack()
    button = Button(tk,text='Enter when done',command=onclick)
    button.pack()
    stat = Label(tk,text='')
    stat.pack()
    next = Button(tk,text='Next',command=lambda: nextUp(stat,inp))
    next.place(x=555,y=53)
    # next.pack()
    tk.mainloop()