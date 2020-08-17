def full():
    import sys
    import os
    import tkinter as tk
    from tkinter import messagebox
    tk = tk.Tk()
    #PLEASE READ INSTRUCTIONS FILE BEFORE RUNNING
    file = open('/Users/test/Documents/python/Py_Programs/Hackathon/DeathStats/Info.txt','r')
    YourPath = file.readline().strip()
    sys.path.insert(1, str(YourPath)+'Hackathon/DeathStats/Deaths')
    Countries = 'Germany,France' 
    Max = file.readline()
    days =int(Max)
    count = 0
    try:
        for file in os.listdir(YourPath):
            if file == 'Hackathon':
                print('Good Path')
    except FileNotFoundError:
        error = messagebox.showerror("Error Occured",'WE COULD NOT FIND THE "HACKATHON" FOLDER IN THAT DIRECTORY')
        exit()
    from DeathStats import GetFiles
    from FormatSecond import full
    full(days,YourPath)
    from SpitProvincesDeaths import full
    full(days,YourPath)
    from ManageFiles import full
    full(YourPath)
    from UI import fullSECOND
    fullSECOND(YourPath)