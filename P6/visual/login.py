import tkinter as tk
class Aplicacion:
    def __init__(self):

        self.ventana1=tk.Tk()
        self.ventana1.title("login")
        self.label1=tk.Label(text="usuario ")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(text="contraseña ")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20, textvariable=self.dato2, show="*")
        self.entry2.grid(column=1, row=1)
        self.boton1=tk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=1, row=2)
        self.boton1 = tk.Button(self.ventana1, text="limpiar", command=self.lim)
        self.boton1.grid(column=2, row=2)
        self.ventana1.mainloop()
    def lim(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        res = ""
        self.label3.configure(text=res)

    def ingresar(self):
        if self.dato1.get()=="leonardo" and self.dato2.get()=="n330fh":
            self.label3 = tk.Label(text="correcto")
            self.label3.config(fg="green",font=("Verdana", 24))
            self.label3.grid(column=1, row=3)
        else:
            self.label3 = tk.Label(text="incorrecto")
            self.label3.config(fg="red", font=("Verdana", 24))
            self.label3.grid(column=1, row=3)
aplicacion1=Aplicacion()