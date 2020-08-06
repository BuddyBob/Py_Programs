import tkinter as tk
from tkinter import *
from tkinter import simpledialog
tk = tk.Tk()
Max = 195
def RunDeaths():
    YourPath = simpledialog.askstring('Countries','Please Enter Your Path To HACKATHON Folder',parent=tk)
    file = open('/Users/test/Documents/python/Py_Programs/Hackathon/DeathStats/Info.txt','w')
    file.write(str(YourPath)+'\n')
    file.write(str(Max))
    file.close()
    from DeathStats import RunAll
def RunRecoveredCases():
    YourPath = simpledialog.askstring('Countries','Please Enter Your Path To HACKATHON Folder',parent=tk)
    file = open('/Users/test/Documents/python/Py_Programs/Hackathon/RecoveredCases/Info.txt','w')
    file.write(str(YourPath)+'\n')
    file.write(str(Max))
    file.close()
    from RecoveredCases import RunAll
Deaths = Button(tk,height = 30, width = 70, text='Run Deaths',command = RunDeaths,highlightbackground='#000000')
Recovered = Button(tk,height = 30, width = 70, text='Run Recovered Cases',command = RunRecoveredCases,highlightbackground='#000000')
Deaths.pack()
Recovered.pack()
tk.mainloop()