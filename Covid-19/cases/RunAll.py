def full():
    import sys
    import os
    import tkinter as tk
    from tkinter import messagebox
    tk = tk.Tk()

    file = open('/Users/aspera/Documents/python/Py_Programs/Covid-19/DeathStats/Info.txt','r')
    YourPath = file.readline().strip()
    sys.path.insert(1, str(YourPath)+'Covid-19/cases/Cases')
    Countries = 'Germany,France' 
    Max = file.readline()
    days =int(Max)
    count = 0
    try:
        for file in os.listdir(YourPath):
            if file == 'Covid-19':
                print('Good Path')
    except FileNotFoundError:
        error = messagebox.showerror("Error Occured",'WE COULD NOT FIND THE "Covid-19" FOLDER IN THAT DIRECTORY')
        exit()
    sys.path.insert(0, str(YourPath)+'Covid-19/cases')
    from FormatFirst import full3
    full3(days,YourPath)
    from SpitProvinces import full
    full(days,YourPath)
    from ManageFilesCases import full
    full(YourPath)
    from UIFirst import full
    full(YourPath)