import tkinter as tk
import sys
from datetime import date
class Aplicacion:
    def __init__(self):
        self.valor=date.today() #valor a incrementar o decrementar
        self.ventana1=tk.Tk() #clase que representa una nueva ventana
        self.ventana1.title("Controles Button y Label") #titulo de la ventana
        self.ventana1.resizable(0,0)
        """Objeto de la calse Label, recibe como parametro la referencia la ventana donde aparecera y el valor del texto inicial """
        self.label1=tk.Label(self.ventana1, text=f"fecha de creacion: {self.valor}")
        self.label2=tk.Label(self.ventana1, text="Nombre programa: Grafico1")

        self.label1.grid(column=0, row=1)
        self.label2.grid(column=0,row=0)

        """ Botones"""
        self.boton1=tk.Button(self.ventana1, text="Cerrar", command=sys.exit)
        self.boton1.grid(column=0, row=2) #posicion del boton

        self.ventana1.mainloop()

aplicacion1=Aplicacion()