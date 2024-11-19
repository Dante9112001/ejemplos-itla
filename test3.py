import tkinter as tk
import time
from turtle import bgcolor
import time

MainWindow = tk.Tk()
MainWindow.iconbitmap("testimages\IT\live_pictures_15405 (1).ico")
label1 = tk.Label(MainWindow, text="dame tu cosita", bg = "brown")
label1.config(font=("arial", 28, "bold"))

def hora ():
    label1.config(text=time.strftime("%H:%M:%S"))
    MainWindow.after(1000, hora)
hora()
label1.pack()
MainWindow.mainloop()