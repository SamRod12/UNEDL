import tkinter as tk

class App():
    def __init__(self):
        self.ventanaP = tk.Tk()
        self.ventanaP.title("Cambiar color de la ventana")
        self.ventanaP.geometry("500x500+30+30")
        self.seleccion = tk.IntVar()
        self.boton1 = tk.Radiobutton(self.ventanaP,text="Rojo", variable=self.seleccion, value=1, command=self.color)
        self.boton1.grid(column=0, row=0)
        self.boton2 = tk.Radiobutton(self.ventanaP,text="Verde", variable=self.seleccion,value=2, command=self.color)
        self.boton2.grid(column=1,row=0)
        self.boton3 = tk.Radiobutton(self.ventanaP, text="Azul", variable=self.seleccion, value=3, command=self.color)
        self.boton3.grid(column=2, row=0)

        self.ventanaP.mainloop()

    def color(self):
        if self.seleccion.get() == 1:
            self.ventanaP.configure(bg="red")
        elif self.seleccion.get() == 2:
            self.ventanaP.configure(bg="green")
        elif self.seleccion.get() == 3:
            self.ventanaP.configure(bg="blue")
ventana = App()

