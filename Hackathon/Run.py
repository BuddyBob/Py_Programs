import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from DeathStats import RunAll1
from RecoveredCases import RunAll2
tk = tk.Tk()
Max = 190
def RunDeaths():
    #If they click on RunDeaths I will run this function
    #Check if they have already entered a path
    try:
        open('/Users/test/Documents/python/Py_Programs/Hackathon/DeathStats/Info.txt','r')
        RunAll1.full()
    except FileNotFoundError:
        YourPath = simpledialog.askstring('Countries','''Please Enter Your Path To HACKATHON Folder:
    Example: 
    \"/Users/Name/Documents/python/\" 
    Note: Leave out the HACKATHON folder and you must put a slash at the end''',parent=tk)
    #Write this path to a file call Info.txt
        file = open('/Users/test/Documents/python/Py_Programs/Hackathon/DeathStats/Info.txt','w')
        file.write(str(YourPath)+'\n')
        file.write(str(Max))
        file.close()
        #Run all the files that gather the data for Corona Virus Deaths
        RunAll1.full()
def RunRecoveredCases():
    #If they click on RecoveredCases Run this
    #Check If they had already entered a path
    try:
        open('/Users/test/Documents/python/Py_Programs/Hackathon/RecoveredCases/Info.txt','r')
        RunAll2.full1()
    except FileNotFoundError:
        YourPath = simpledialog.askstring('Countries','''Please Enter Your Path To HACKATHON Folder:
    Example: 
    \"/Users/Name/Documents/python/\" 
    Note: Leave out the HACKATHON folder and you must put a slash at the end''',parent=tk)
        file = open('/Users/test/Documents/python/Py_Programs/Hackathon/RecoveredCases/Info.txt','w')
        #Write there path to a file
        file.write(str(YourPath)+'\n')
        file.write(str(Max))
        file.close()
        #Run all the files that gather all the Recovered Cases
        RunAll2.full1()

Deaths = Button(tk,height = 20, width = 30, text='Run Deaths',command = RunDeaths,highlightbackground='#000000')
Recovered = Button(tk,height = 20, width = 30, text='Run Recovered Cases',command = RunRecoveredCases,highlightbackground='#000000')
Deaths.pack()
Recovered.pack()
tk.mainloop()