def full1():
    import sys
    import os
    import tkinter as tk
    from tkinter import messagebox
    tk = tk.Tk()
    #PLEASE READ INSTRUCTIONS FILE BEFORE RUNNING
    file = open('/Users/aspera/Documents/python/Py_Programs/Covid-19/RecoveredCases/Info.txt','r')
    YourPath = file.readline().strip()
    Max = file.readline()
    Max = int(Max)
    days = int(Max)
    count = 0
    try:
        for file in os.listdir(YourPath):
            if file == 'Covid-19':
                print('good path')

    except FileNotFoundError:
        error = messagebox.showerror("Error Occured",'WE COULD NOT FIND THE "Covid-19" FOLDER IN THAT DIRECTORY')
        exit()
    sys.path.insert(0, str(YourPath)+'Covid-19/RecoveredCases/recovered')
    from RecoveredCases import GetFiles
    from FormatLast import full
    full(days,YourPath)
    from SpitProvinces import full
    full(days,YourPath)
    from ManageFiles import full
    full(YourPath)
    from UILast import full
    full(YourPath)