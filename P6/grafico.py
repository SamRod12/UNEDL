import tkinter as tk
import sys
class Aplicacion:
    def __init__(self):
        self.valor=1 #valor a incrementar o decrementar
        self.ventana1=tk.Tk() #clase que representa una nueva ventana
        self.ventana1.title("Controles Button y Label") #titulo de la ventana
        """Objeto de la calse Label, recibe como parametro la referencia la ventana donde aparecera y el valor del texto inicial """
        self.label1=tk.Label(self.ventana1, text=self.valor)
        """Ubicacion de los controles visuales (numero a incrementar) """
        self.label1.grid(column=2, row=0)
        """Color del texto """
        self.label1.configure(foreground="red")

        """ Botones"""
        self.boton1=tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1) #posicion del boton

        self.boton2=tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)

        self.ventana1.mainloop()


    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)        


aplicacion1=Aplicacion()