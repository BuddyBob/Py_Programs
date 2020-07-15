from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import os
import time
import shutil
tk = Tk()
def setFilePath():
    good = False
    while good == False:
        global filePath
        filePath = simpledialog.askstring('set path',str('Set your file path'),parent=tk)
        if os.path.exists(filePath):
            good = True
        else:
            messagebox.showerror(title="Path Error", message="There is no such directory")
def deleteFile():
    good = False
    while good == False:
        file = simpledialog.askstring('File',str('Choose a file'),parent=tk)
        total = filePath+str('/')+file
        if os.path.exists(total):
            os.remove(total)
            messagebox.showinfo(title="Deleted", message="Deleted")
            good = True
        else:
            messagebox.showerror(title="No such file", message="We could not find that file")
def massFile():
    good = False
    while good == False:
        folder = simpledialog.askstring('Folder',str('Choose a folder'),parent=tk)
        total = filePath+str('/')+folder
        if os.path.isdir(total):
            if variable== OPTIONS[0]:
                print('gi')
                good = TRUE
            else:
                print('hi')
        else:
            messagebox.showerror(title="No such directory", message="We could not find that folder")
def deleteFolder():
    good = False
    while good == False:
        folder = simpledialog.askstring('Folder',str('Choose a folder'),parent=tk)
        total = filePath+str('/')+folder
        if os.path.isdir(total):
            shutil.rmtree(total)
            messagebox.showinfo(title="Deleted", message="Folder Deleted")
            good = True
        else:
            messagebox.showerror(title="No such directory", message="We could not find that folder")
def moveFile():
    good = FALSE
    while good == FALSE:
        file = simpledialog.askstring('file',str('Choose a file'),parent=tk)
        total = filePath+str('/')+file
        print(total)
        if os.path.exists(total):
            destination = simpledialog.askstring('destination',str('Enter a path to your destination'),parent=tk)
            if os.path.exists(destination):
                try:
                    newPath = shutil.move(total,destination)
                    messagebox.showinfo(title="Moved", message="File Moved")
                    good = TRUE
                except:
                    messagebox.showerror(title="Error", message="File already exist in that directory")
            else:
                messagebox.showerror(title="Invalid Destination", message="Could not find that destination")
        else:
            messagebox.showerror(title="No such file", message="There is no such file in that directory")



OPTIONS = ['rename','delete','move']
variable = StringVar(tk)
variable.set(OPTIONS[0])
tk.geometry("300x600")
setDefaultPath = Button(tk,height = 10, width = 20, text='Set Default File Path',command = setFilePath)
deleteFiles = Button(tk,height = 5, width = 20, text='Delete File',command = deleteFile)
massFiles = Button(tk,height = 5, width = 20, text='Mass File Change',command = massFile)
deleteFolders = Button(tk,height = 5, width = 20, text='Delete Folder',command = deleteFolder)
moveFiles = Button(tk,height = 5, width = 20, text='Move File',command = moveFile)
menuDrop = OptionMenu(tk,variable,*OPTIONS)
menuDrop.pack()
setDefaultPath.pack()
massFiles.pack()
deleteFiles.pack()
deleteFolders.pack()
moveFiles.pack()
tk.mainloop()