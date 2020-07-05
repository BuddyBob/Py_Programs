import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import *
application_window = tk.Tk()
while True:
    num1 = simpledialog.askfloat('ask',"Enter a number",
                                    parent=application_window,)
    op = simpledialog.askstring('ask',"Enter a operation",
                                    parent=application_window,)
    num2 = simpledialog.askfloat('ask',"Enter another number",
                                    parent=application_window,)
    if op == "*":   
        messagebox.showinfo("answer",num1 * num2)
    elif op == "/":
        messagebox.showinfo("answer",num1 / num2)
    elif op == "+":
        messagebox.showinfo("answer",num1 + num2)
    elif op == "-":
        messagebox.showinfo("answer",num1 - num2)
    elif op == "^":
        messagebox.showinfo("answer",num1 ** num2)
    elif op == "**":
        messagebox.showinfo("answer",num1 ** num2)
    else:
        messagebox.showerror("error","THAT IS NOT AN OPERATION!")



