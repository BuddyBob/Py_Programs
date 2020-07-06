import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

application_window = tk.Tk()

answer = simpledialog.askinteger('ask',"Enter a number",
                                parent=application_window,)
if answer is not None:
    print("The number you entered was: ", answer)
else:
    print("You did not enter a number")
answer2 = simpledialog.askinteger('ask',"Enter a number2",
                                parent=application_window,)

if answer2 is not None:
    print("The number you entered was: ", answer2)
else:
    print("You did not enter a number")
messagebox.showinfo("Information",answer2+answer)
