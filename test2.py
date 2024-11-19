from sys import argv
import tkinter as tk
from turtle import bgcolor

ventana_principal = tk.Tk()
frame1 = tk.Frame(ventana_principal)
frame2 = tk.Frame(frame1)
boton = tk.Button(frame1, text="Desembarco de normandia ")
label = tk.LabelFrame(ventana_principal, bg = "darkblue", text = "90000000 millone", width=400, height= 200 )
ventana_principal.title('NO FUMES MÁS MARIHUANAAAAAAAAA🗣🗣❗🔥🗣🗣❗🔥🗣🗣❗🔥🗣🗣❗🔥🗣🗣❗🔥🗣🗣❗🔥')
ventana_principal.geometry('500x250')
ventana_principal.minsize(300, 200)
ventana_principal.maxsize(800, 800)
ventana_principal.iconbitmap("C:/Users/PC/Documents/codigo/practicas-GUI/testimages/IT/live_pictures_15405 (1).ico")
ventana_principal.configure(bg="grey")
ventana_principal.resizable(True, True)
ventana_principal.attributes("-alpha", 1)


frame1.configure(width=100, height=200, bg = "red", bd=3, )
frame2.configure(width=50, height=100, bg = "blue", bd = 0)

frame1.pack()
frame2.pack()
boton.pack()
label.pack()
ventana_principal.mainloop()