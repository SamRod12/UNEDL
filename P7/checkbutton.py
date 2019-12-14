import tkinter as tk


class App():
    def __init__(self):
        self.ventanaP = tk.Tk()
        self.ventanaP.title("")
        self.ventanaP.geometry("500x500+30+30")
        self.seleccion1 = tk.BooleanVar()
        self.seleccion2 = tk.BooleanVar()
        self.seleccion3 = tk.BooleanVar()
        self.seleccion4 = tk.BooleanVar()
        self.seleccion5 = tk.BooleanVar()

        self.check1 = tk.Checkbutton(self.ventanaP,text="Chrome", variable=self.seleccion1, command=self.concatenar)
        self.check1.grid(column=0,row=1)
        self.check2 = tk.Checkbutton(self.ventanaP, text="FireFox",variable=self.seleccion2,command=self.concatenar)
        self.check2.grid(column=0, row=2)
        self.check3 = tk.Checkbutton(self.ventanaP, text="Edge",variable=self.seleccion3,command=self.concatenar)
        self.check3.grid(column=0, row=3)
        self.check4 = tk.Checkbutton(self.ventanaP, text="Safari",variable=self.seleccion4,command=self.concatenar)
        self.check4.grid(column=0, row=4)
        self.check5 = tk.Checkbutton(self.ventanaP, text="Opera", variable=self.seleccion5,command=self.concatenar)
        self.check5.grid(column=0, row=5)
        self.ventanaP.mainloop()
    def concatenar(self):
        texto=""
        if self.seleccion1.get() == True :
            texto+="Chrome"

        if self.seleccion2.get() == True:
            texto+=" - "+ "FireFox"

        if self.seleccion3.get() == True:
            texto+=" - "+"Edge"

        if self.seleccion4.get()==True:
            texto+=" - "+"Safari"

        if self.seleccion5.get()==True:
            texto+=" - "+"Opera"

        self.ventanaP.title(texto)


ventana = App()