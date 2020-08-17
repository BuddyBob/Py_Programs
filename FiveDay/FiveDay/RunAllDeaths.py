def fullDay():
    import sys
    import os
    import tkinter as tk
    from tkinter import messagebox
    tk = tk.Tk()
    #PLEASE READ INSTRUCTIONS FILE BEFORE RUNNING
    file = open('/Users/test/Documents/python/Py_Programs/Hackathon/FiveDay/Info.txt','r')
    YourPath = file.readline().strip()
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
    sys.path.insert(1, str(YourPath)+'Hackathon/FiveDay/Deaths')
    from FormatDay import full
    full(days,YourPath)
    from SpitProvincesDay import full
    full(days,YourPath)
    from ManageFilesDay import full
    full(YourPath)
    from MovingAverageDeaths import full
    full(YourPath)
    sys.path.insert(0, str(YourPath)+'Hackathon/FiveDay/')
    from UIALL import full
    full(YourPath)