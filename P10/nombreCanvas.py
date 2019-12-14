import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=300, height=100, background="black")
        self.canvas1.grid(column=0, row=0)
        # L
        self.canvas1.create_rectangle(20,10,25,50,fill="white")
        self.canvas1.create_rectangle(20,50,40,55, fill="white")
        #e
        self.canvas1.create_rectangle(50, 25, 55, 50, fill="white")
        self.canvas1.create_rectangle(50, 50, 70, 55, fill="white")
        self.canvas1.create_rectangle(50, 25, 70, 30, fill="white")
        self.canvas1.create_rectangle(65, 25, 70, 45, fill="white")
        self.canvas1.create_rectangle(50, 40, 70, 45, fill="white")
        #o
        self.canvas1.create_rectangle(80, 25, 85, 50, fill="white")
        self.canvas1.create_rectangle(80, 50, 100, 55, fill="white")
        self.canvas1.create_rectangle(80, 25, 100, 30, fill="white")
        self.canvas1.create_rectangle(95, 25, 100, 55, fill="white")
        #n
        self.canvas1.create_rectangle(110, 25, 115, 55, fill="white")
        self.canvas1.create_rectangle(110, 25, 130, 30, fill="white")
        self.canvas1.create_rectangle(125, 25, 130, 55, fill="white")
        #a
        self.canvas1.create_rectangle(140, 27, 145, 50, fill="white")
        self.canvas1.create_rectangle(140, 45, 160, 50, fill="white")
        self.canvas1.create_rectangle(140, 27, 160, 33, fill="white")
        self.canvas1.create_rectangle(155, 25, 160, 55, fill="white")
        #r
        self.canvas1.create_rectangle(170, 25, 175, 55, fill="white")
        self.canvas1.create_rectangle(170, 28, 190, 33, fill="white")
        #d
        self.canvas1.create_rectangle(200, 30, 205, 50, fill="white")
        self.canvas1.create_rectangle(200, 50, 220, 55, fill="white")
        self.canvas1.create_rectangle(200, 30, 220, 35, fill="white")
        self.canvas1.create_rectangle(220, 10, 225, 55, fill="white")
        #o
        self.canvas1.create_rectangle(230, 25, 235, 50, fill="white")
        self.canvas1.create_rectangle(230, 50, 250, 55, fill="white")
        self.canvas1.create_rectangle(230, 25, 250, 30, fill="white")
        self.canvas1.create_rectangle(250, 25, 255, 55, fill="white")

        self.ventana1.mainloop()

aplicacion1=Aplicacion()