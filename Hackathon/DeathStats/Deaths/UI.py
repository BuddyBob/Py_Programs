# This files job is to provide the user with a UI
# I used tkinter for the frontend
from tkinter import * 
from tkinter import messagebox, simpledialog
import tkinter as tk
import sys
#I used matplotlib for the graphing
import  matplotlib.pyplot as plt
#I need a couple of variables from GlobalVar file
from GlobalVar import CountryMax
file = open('/Users/test/Documents/python/Py_Programs/Hackathon/DeathStats/Info.txt','r')
file.readline()
Max = file.readline()
Max = int(Max)
def full(YourPath):
    file = open(str(YourPath)+'Hackathon/DeathStats/Deaths/Final.txt','r')
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
    #Ask user for the amount of day they would like to inspect
    #Maxvalue is set to 196
    days = simpledialog.askinteger('Days','Enter how many days you would like to inspect: ',parent=root,minvalue=0, maxvalue=Max)
    #Here I will ask user for a country but I need to account for if they spelt a country wrong
    #Note: When looking for United States please enter ["US"] !NOT! Us
    countriesPassed = False
    while countriesPassed == False:
        countriesPassed = False
        count=0
        countriesFailed = []
        countriesList = []
        countries = simpledialog.askstring('Countries','Enter the comma seperated countries: ',parent=root)
        #Split countries at comma
        for i in countries:
            if i == ',':
                global length
                length = len(countries.split(','))
                splits = countries.split(',')
        for i in countries.split(','):
            #Check if all of there countries entered have data
            if i in L:
                count+=1
                #If yes count+=1 and append the row
                countriesList.append(i)
            else:
                #If not append it to countriesFailes
                countriesFailed.append(i)
        #Check if all countries passed
        length = len(countries.split(','))
        if count == length:
            countriesPassed = True
        #Check if they entered more countries than allowed(Default:20)
        if length > CountryMax:
            error = messagebox.showerror('Countries Exceeded','''Please Limit Your Country Choices up to 5!''')
        else:
            if len(countriesFailed)>1:
                error = messagebox.showerror('Could not these countries','''There is no data stored for '''+str(countriesFailed)+'''. Make sure you entered something like this:
                             US,France ''',parent=root) 
            if len(countriesFailed) == 1:
                error = messagebox.showerror('Could not find this country','''There is no data stored for '''+str(countriesFailed)+'''. Make sure you entered something like this:
                             US,France ''',parent=root) 

    file2 = open(str(YourPath)+'Hackathon/DeathStats/Deaths/Final.txt','r')
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
    plt.style.use(['dark_background'])
    plt.xlabel('Days')
    plt.ylabel('Deaths')
    plt.title('Corona Stats')
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
        Graph = plt.plot(range(length),lists,label=Country[count])
        count+=1
    plt.legend()
    plt.show()
    root.mainloop()
    file2.close()