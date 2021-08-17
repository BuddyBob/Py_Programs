
import os
import shutil
import time
from tkinter import *
from tkinter import messagebox, simpledialog
tk = Tk()
tk.configure(background="yellow") 
def setFilePath():
    try:
        good = False
        while good == False:
            global filePath
            filePath = simpledialog.askstring('set path',str('Set your file path'),parent=tk)
            if os.path.exists(filePath):
                good = True
            else:
                messagebox.showerror(title="Path Error", message="There is no such directory")
    #none typed
    except TypeError:
        messagebox.showwarning(title="No Path Entered", message="No Path Entered")
def deleteFile():
    try:
        count = True
        try: 
            filePath + 'text'
        except NameError:
            messagebox.showwarning(title="No Path Entered", message="No Path Was Entered")
            count = False
        good = False
        while good == False and count != False:
            file = simpledialog.askstring('File',str('Choose a file'),parent=tk)
            total = filePath+str('/')+file
            if os.path.exists(total):
                os.remove(total)
                messagebox.showinfo(title="Deleted", message="Deleted")
                good = True
            else:
                messagebox.showerror(title="No such file", message="We could not find that file")
    #none entered
    except TypeError:
        pass
def renameMass():
        try:
            good = False    
            while good == False:
                folder = simpledialog.askstring('File',str('Choose a folder'),parent=tk)
                total = filePath+str('/')+folder
                if os.path.exists(total):
                    file = simpledialog.askstring('File',str('File Name'),parent=tk)
                    count = 0
                    for i in os.listdir(total):
                        count += 1
                        os.rename(total+str('/')+i,total+str('/')+file+count)
                    good = TRUE
                else:
                    messagebox.showerror(title="No such file", message="We could not find that file")
        except (TypeError,NameError):
            messagebox.showerror(title="No such file", message="No path entered")
def moveMass():
        try:
            good = False    
            while good == False:
                folder = simpledialog.askstring('File',str('Choose a folder'),parent=tk)
                total = filePath+str('/')+folder
                if os.path.exists(total):
                    destination = simpledialog.askstring('Destination',str('Enter Destination'),parent=tk)
                    if os.path.exists(destination):
                        count = 0
                        for i in os.listdir(total):
                            count += 1
                            shutil.move(total+'/'+i,'/Users/test/Downloads')
                            messagebox.showinfo(title="FILES MOVE", message="Files Succefully Moved") 
                        good = TRUE
                    else:
                       messagebox.showerror(title="No such file", message="We could not find that file") 
                else:
                    messagebox.showerror(title="No such file", message="We could not find that file")
        except (TypeError,NameError):
            messagebox.showerror(title="No such file", message="No path entered")
def deleteFolder():
    try:
        count = True
        try: 
            filePath + 'text'
        except NameError:
            messagebox.showwarning(title="No Path Entered", message="No Path Was Entered")
            count = False
        good = False
        while good == False and count != False:
            folder = simpledialog.askstring('Folder',str('Choose a folder'),parent=tk)
            total = filePath+str('/')+folder
            if os.path.isdir(total):
                shutil.rmtree(total)
                messagebox.showinfo(title="Deleted", message="Folder Deleted")
                good = True
            else:
                messagebox.showerror(title="No such directory", message="We could not find that folder")
    except TypeError:
        pass
def moveFile():
    try: 
        count = True
        try: 
            filePath + 'text'
        except NameError:
            messagebox.showwarning(title="No Path Entered", message="No Path Was Entered")
            count = False
        good = FALSE
        while good == FALSE and count != False:
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
    except TypeError:
            pass
tk.geometry("300x600")
setDefaultPath = Button(tk,height = 10, width = 20, text='Set Default File Path',command = setFilePath)
deleteFiles = Button(tk,height = 5, width = 20, text='Delete File',command = deleteFile)
renameMassFile = Button(tk,height = 5, width = 20, text='Mass File Rename',command = renameMass)
moveMassFile = Button(tk,compound=TOP,height=5, width = 20, text = 'Move Mass Files',command = moveMass)
deleteFolders = Button(tk,height = 5, width = 20, text='Delete Folder',command = deleteFolder)
moveFiles = Button(tk,height = 5, width = 20, text='Move File',command = moveFile)
setDefaultPath.pack()
renameMassFile.pack()
moveMassFile.pack()
deleteFiles.pack()
deleteFolders.pack()
moveFiles.pack()
tk.mainloop()