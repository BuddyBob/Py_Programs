import tkinter as tk
from tkinter import *
from tkinter import simpledialog
tk = tk.Tk()
Max = 190
def RunDeaths():
    try:
        open('/Users/test/Documents/python/Py_Programs/Hackathon/DeathStats/Info.txt','r')
        from DeathStats import RunAll
    except:
        YourPath = simpledialog.askstring('Countries','''Please Enter Your Path To HACKATHON Folder:
    Example: 
    \"/Users/Name/Documents/python/\" 
    Note: Leave out the HACKATHON folder and you must put a slash at the end''',parent=tk)
        file = open('/Users/test/Documents/python/Py_Programs/Hackathon/DeathStats/Info.txt','w')
        file.write(str(YourPath)+'\n')
        file.write(str(Max))
        file.close()
        from DeathStats import RunAll
def RunRecoveredCases():
    try:
        open('/Users/test/Documents/python/Py_Programs/Hackathon/RecoveredCases/Info.txt','r')
        from RecoveredCases import RunAll
    except:
        YourPath = simpledialog.askstring('Countries','''Please Enter Your Path To HACKATHON Folder:
    Example: 
    \"/Users/Name/Documents/python/\" 
    Note: Leave out the HACKATHON folder and you must put a slash at the end''',parent=tk)
        file = open('/Users/test/Documents/python/Py_Programs/Hackathon/RecoveredCases/Info.txt','w')
        file.write(str(YourPath)+'\n')
        file.write(str(Max))
        file.close()
        from RecoveredCases import RunAll

Deaths = Button(tk,height = 20, width = 30, text='Run Deaths',command = RunDeaths,highlightbackground='#000000')
Recovered = Button(tk,height = 20, width = 30, text='Run Recovered Cases',command = RunRecoveredCases,highlightbackground='#000000')
Deaths.pack()
Recovered.pack()
tk.mainloop()