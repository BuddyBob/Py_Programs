import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from cases import RunAll
from DeathStats import RunAll1
from RecoveredCases import RunAll2
import json
tk = tk.Tk()
Max = 190
import urllib.request
import datetime

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
urllib.request.urlretrieve(url, filename="time_series_covid19_recoveredGlobal.csv")
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
urllib.request.urlretrieve(url, filename="time_series_covid19_confirmed_global.csv")
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
urllib.request.urlretrieve(url, filename="time_series_covid19_deaths_global.csv")

s = open('setting.json')
setting = json.load(s)
btnColor = setting["ButtonColor"] 
def RunCases():
    try:
        open('/Users/aspera/Documents/python/Py_Programs/Covid-19/DeathStats/Info.txt','r')
        RunAll.full()
    except FileNotFoundError:
        YourPath = simpledialog.askstring('Countries','''Please Enter Your Path To Covid-19 Folder:
    Example: 
    \"/Users/Name/Documents/python/\" 
    Note: Leave out the Covid-19 folder and you must put a slash at the end''',parent=tk)
        file = open('/Users/aspera/Documents/python/Py_Programs/Covid-19/DeathStats/Info.txt','w')
        file.write(str(YourPath)+'\n')
        file.write(str(Max))
        file.close()

        RunAll.full()

def RunDeaths():


    try:
        open('/Users/aspera/Documents/python/Py_Programs/Covid-19/DeathStats/Info.txt','r')
        RunAll1.full()
    except FileNotFoundError:
        YourPath = simpledialog.askstring('Countries','''Please Enter Your Path To Covid-19 Folder:
    Example: 
    \"/Users/Name/Documents/python/\" 
    Note: Leave out the Covid-19 folder and you must put a slash at the end''',parent=tk)

        file = open('/Users/aspera/Documents/python/Py_Programs/Covid-19/DeathStats/Info.txt','w')
        file.write(str(YourPath)+'\n')
        file.write(str(Max))
        file.close()

        RunAll1.full()
def RunRecoveredCases():

    try:
        open('/Users/aspera/Documents/python/Py_Programs/Covid-19/RecoveredCases/Info.txt','r')
        RunAll2.full1()
    except FileNotFoundError:
        YourPath = simpledialog.askstring('Countries','''Please Enter Your Path To Covid-19 Folder:
    Example: 
    \"/Users/Name/Documents/python/\" 
    Note: Leave out the Covid-19 folder and you must put a slash at the end''',parent=tk)
        file = open('/Users/aspera/Documents/python/Py_Programs/Covid-19/RecoveredCases/Info.txt','w')

        file.write(str(YourPath)+'\n')
        file.write(str(Max))
        file.close()

        RunAll2.full1()


Cases =Button(tk,height = 10, width = 30, text='Run Cases',command = RunCases,highlightbackground = btnColor)
Deaths = Button(tk,height = 10, width = 30, text='Run Deaths',command = RunDeaths,highlightbackground=btnColor)
Recovered = Button(tk,height = 10, width = 30, text='Run Recovered Cases',command = RunRecoveredCases,highlightbackground=btnColor)
Cases.pack()
Deaths.pack()
Recovered.pack()
tk.mainloop()