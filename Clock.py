from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")
root.wm_minsize(440, 90)
root.resizable(height=0, width=0)

def time():
    string = strftime("%H:%M:%S:%p")
    lable.config(text=string)
    lable.after(1000, time)

lable = Label(root, font=("ds-digital", 80), background = "black", foreground = "white")
lable.pack(anchor="center")
time()

mainloop()