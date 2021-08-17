import random
import string
from tkinter import *   
from tkinter import simpledialog
from tkinter import messagebox
tk = Tk()  
def get_password():
    total = False
    while total == False:
        letters_Count = 0
        numbers_Count = 0
        spec_Count = 0
        password_characters = string.digits + string.ascii_letters + '!@#$%&*'
        password = ''.join(random.choice(password_characters)for i in range(8))
        for i in password:
            if i in 'abcdefghijklmnopqrstuvlxyz':
                letters_Count = 1
            if i in string.digits:
                numbers_Count = 1
            if i in '!@#$%&*':
                spec_Count = 1
            if spec_Count == 1 and numbers_Count == 1 and spec_Count == 1:
                total = True
                btn.destroy()
    btn.quit()
    start = messagebox.showinfo("Information","Password Generated: "+str(password))
while True:
    btn = Button(tk,height = 10, width = 20, text='generate password',command = get_password)
    btn.pack()
    btn.mainloop()
