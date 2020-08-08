def full1():
    import sys
    import os
    import tkinter as tk
    from tkinter import messagebox
    tk = tk.Tk()
    #PLEASE READ INSTRUCTIONS FILE BEFORE RUNNING
    file = open('/Users/test/Documents/python/Py_Programs/Hackathon/RecoveredCases/Info.txt','r')
    YourPath = file.readline().strip()
    Max = file.readline()
    Max = int(Max)
    days = int(Max)
    count = 0
    try:
        for file in os.listdir(YourPath):
            if file == 'Hackathon':
                print('good path')

    except FileNotFoundError:
        error = messagebox.showerror("Error Occured",'WE COULD NOT FIND THE "HACKATHON" FOLDER IN THAT DIRECTORY')
        exit()
    sys.path.insert(0, str(YourPath)+'Hackathon/RecoveredCases/recovered')
    from RecoveredCases import GetFiles
    from Format import full
    full(days,YourPath)
    from SpitProvinces import full
    full(days,YourPath)
    from ManageFiles import full
    full(YourPath)
    from UIs import full
    full(YourPath)