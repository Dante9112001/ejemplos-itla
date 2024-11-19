import tkinter as tk
ventana1=tk.Tk()
ventana2 = tk.Tk()
canvas1=tk.Canvas(ventana1, width=600, height=400, background="black")

canvas1.grid(column=0, row=0)


canvas1.create_line(0, 0, 100,50, fill="white")


canvas1.create_rectangle(150,10, 250,110, fill="white")

canvas1.create_oval(300,10,400,150, fill="red")

canvas1.create_arc(420,10,550,110, fill="yellow", start=180, extent=90)

canvas1.create_rectangle(150,210, 250,310, outline="white")

canvas1.create_oval(300,210,400,350, outline="red")

canvas1.create_arc(420,210,550,310, outline="yellow", start=180, extent=90)   

    
ventana1.mainloop()
       

