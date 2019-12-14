import tkinter as tk
from tkinter import messagebox as ms
import sys
class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Suma de dos numeros")
        self.ventana1.geometry("290x70+150+150")
        self.label1=tk.Label(text="primer valor:")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(text="segundo valor:")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        self.boton1=tk.Button(self.ventana1, text="Sumar", command=self.sumar)
        self.boton1.grid(column=1, row=4)
        self.boton2 = tk.Button(self.ventana1, text="Salir", command=self.salir,width=10)
        self.boton2.grid(column=3, row=0, rowspan=2, sticky="ns")

        self.ventana1.mainloop()

    def sumar(self):
        if self.dato1.get() != "" and self.dato2.get() !="":
            suma=int(self.dato1.get())+int(self.dato2.get())
            ms.showinfo("Resultado","la suma es: "+str(suma))
        else:
            ms.showerror("Error","Debes ingresar ambos datos")

    def salir(self):
        res = ms.askyesno("salir","quiere salir?")
        if res== True:
            sys.exit()
app = Aplicacion()