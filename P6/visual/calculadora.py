import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("calculadora")
        self.label1=tk.Label(text="num1")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=7, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(text="num2")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=7, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        self.boton1=tk.Button(self.ventana1, text="SUMA", command=self.sumar)
        self.boton1.grid(column=0, row=2)
        self.boton1 = tk.Button(self.ventana1, text="RESTA", command=self.resta)
        self.boton1.grid(column=1, row=2)
        self.boton1 = tk.Button(self.ventana1, text="MUL", command=self.mul)
        self.boton1.grid(column=2, row=2)
        self.boton1 = tk.Button(self.ventana1, text="DIV", command=self.div)
        self.boton1.grid(column=3, row=2)
        self.boton1 = tk.Button(self.ventana1, text="POTENCIA", command=self.potencia)
        self.boton1.grid(column=4, row=2)
        self.boton1 = tk.Button(self.ventana1, text="LIMPIAR", command=self.lim)
        self.boton1.grid(column=5, row=2)

        self.label2=tk.Label(text="resultado:")
        self.label2.grid(column=1, row=3)
        self.label3 = tk.Label(text="")

        self.label3.config(fg="red", font=("Verdana", 10))
        self.label3.grid(column=2, row=3)
        self.ventana1.mainloop()
    def sumar(self):
        suma=int(self.dato1.get()) + int(self.dato2.get())
        self.label3.configure(text=suma)
    def resta(self):
        res= suma=int(self.dato1.get()) - int(self.dato2.get())
        self.label3.configure(text=res)
    def mul(self):
        mul = int(self.dato1.get()) * int(self.dato2.get())
        self.label3.configure(text=mul)
    def div(self):
        div = int(self.dato1.get()) / int(self.dato2.get())
        self.label3.configure(text=div)
    def potencia(self):
        pot=int(self.dato1.get()) ** int(self.dato2.get())
        self.label3.configure(text=pot)
    def lim(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        res=""
        self.label3.configure(text=res)


aplicacion1=Aplicacion()

