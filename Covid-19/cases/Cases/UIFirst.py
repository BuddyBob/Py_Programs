
from tkinter import * 
from tkinter import messagebox, simpledialog
import tkinter as tk
import sys

import  matplotlib.pyplot as plt
import json
def full(YourPath):
    s = open('/Users/test/Documents/python/Py_Programs/Covid-19/setting.json')
    setting = json.load(s)
    gridd = setting["Grid"]
    CountryMax = setting["CountryMax"]
    GraphColor = setting["GraphColor"]
    TitleSize = setting["TitleSize"]
    LineThickness = setting["lineThickness"]
    GridLineThickness = setting["GridLineThickness"]
    GridLineColor = setting["GridLineColor"]
    LStyle = setting["lineStyles"]
    file = open('/Users/test/Documents/python/Py_Programs/Covid-19/DeathStats/Info.txt','r')
    file.readline()
    Max = file.readline()
    Max = int(Max)
    file = open(str(YourPath)+'Covid-19/cases/Cases/Final.txt','r')
    L = []
    file.readline()
    for row in file:
        row = row.replace('\'','')
        row = row.replace(']','')
        row = row.replace('[','')
        row = row.split(',')
        L.append(row[0])
    root = tk.Tk()
    root.withdraw()

    days = simpledialog.askinteger('Days','Enter how many days you would like to inspect: ',parent=root,minvalue=0, maxvalue=Max)

    countriesPassed = False
    while countriesPassed == False:
        countriesPassed = False
        count=0
        countriesFailed = []
        countriesList = []
        countries = simpledialog.askstring('Countries','Enter the comma seperated countries: ',parent=root)

        for i in countries:
            if i == ',':
                global length
                length = len(countries.split(','))
                splits = countries.split(',')
        for i in countries.split(','):

            if i in L:
                count+=1

                countriesList.append(i)
            else:

                countriesFailed.append(i)

        length = len(countries.split(','))
        if count == length:
            countriesPassed = True

        if length > CountryMax:
            error = messagebox.showerror('Countries Exceeded','''Please Limit Your Country Choices up to 5!''')
        else:
            if len(countriesFailed)>1:
                error = messagebox.showerror('Could not these countries','''There is no data stored for '''+str(countriesFailed)+'''. Make sure you entered something like this:
                             US,France ''',parent=root) 
            if len(countriesFailed) == 1:
                error = messagebox.showerror('Could not find this country','''There is no data stored for '''+str(countriesFailed)+'''. Make sure you entered something like this:
                             US,France ''',parent=root) 

    file2 = open(str(YourPath)+'Covid-19/cases/Cases/Final.txt','r')
    major = []
    for row in file2:
        row = row.replace('\'','')
        row = row.replace(']','')
        row = row.replace('[','')
        row = row.split(',')
        if row[0] in countriesList:
            major.append(row)
    for lists in major:
        lists[-1] = re.sub('\\\\n|\n', '' , lists[-1])
    plt.xlabel('Last '+str(days)+' Days',fontsize=10)
    plt.ylabel('Cases',fontsize=10)
    plt.title('Corona Stats-Cases',fontsize=TitleSize)
    ax = plt.gca()
    ax.set_facecolor(GraphColor)
    if gridd == True:
        plt.grid()
        ax.grid(color=GridLineColor, linestyle=LStyle, linewidth=GridLineThickness)
    Full = []
    Country = []
    for lists in major:
        dataN = lists[-days:]
        Country.append(lists[0]) 
        Full.append(dataN)
        length = len(dataN)
    for lists in Full:
        for i in range(0, len(lists)): 
            lists[i] = int(lists[i]) 
    count=0
    for lists in Full:
        Graph = plt.plot(range(length),lists,label=Country[count],linewidth=LineThickness)
        count+=1
    plt.legend()
    plt.show()
    root.mainloop()
    file2.close()