import tkinter as tk
import sys
class Ejer:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("ejercicio001")
        self.label1=tk.Label(self.ventana1, text="nombre: TKINTER")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana1, text="fecha: 31/01/2019")
        self.label2.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Fin", command=self.finalizar)
        self.boton1.grid(column=0, row=2)
        self.boton1 = tk.Button(self.ventana1, text="cuack(fin2)", command=self.finalizar)
        self.boton1.grid(column=2, row=2)
        self.ventana1.resizable(False, False)
        self.ventana1.mainloop()
    def finalizar(self):
        sys.exit()
c=Ejer()