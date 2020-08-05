from tkinter import * 
from tkinter import messagebox, simpledialog
import tkinter as tk
import sys
import GetFiles
sys.path.insert(1, '/Users/test/Documents/python/Py_Programs/Hackathon/Deaths')
def full():
    L = []
    file = open('/Users/test/Documents/python/Py_Programs/Hackathon/Deaths/Final.txt','r')
    file.readline()
    for row in file:
        row = row.replace('\'','')
        row = row.replace(']','')
        row = row.replace('[','')
        row = row.split(',')
        L.append(row[0])
    print(L)
    def check():
        print('hi')
    root = tk.Tk()
    root.withdraw()
    days = simpledialog.askinteger('Days','Enter how many days you would like to inspect: ',parent=root,)
    countriesPassed = False
    while countriesPassed == False:
        countries = simpledialog.askstring('Countries','Enter how many countries toy would like to inspect: ',parent=root)
        if countries in L:
            countriesPassed = True
    countries.pack()
    days.pack()
    root.mainloop()
