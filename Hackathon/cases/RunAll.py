def full():
    import sys
    import os
    import tkinter as tk
    from tkinter import messagebox
    tk = tk.Tk()

    file = open('/Users/test/Documents/python/Py_Programs/Hackathon/DeathStats/Info.txt','r')
    YourPath = file.readline().strip()
    sys.path.insert(1, str(YourPath)+'Hackathon/cases/Cases')
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
    sys.path.insert(0, str(YourPath)+'Hackathon/cases')
    from FormatFirst import full3
    full3(days,YourPath)
    from SpitProvinces import full
    full(days,YourPath)
    from ManageFilesCases import full
    full(YourPath)
    from UIFirst import full
    full(YourPath)