from tkinter import*
from tkinter.ttk import*

from time import strftime

root = Tk()
root.title("Emos's Clock")


def time():
    stri= strftime('%H:%M:%S')
    lbl.config(text=stri)
    lbl.after(1000, time)

lbl= Label(root, font=("calibri", 40, "bold"),
            background= "pink",
            foreground= "white")

lbl.pack(anchor="center")


time()
mainloop()