class Galleta:
    chocolate=True
    def saludar(self):
        print("soy una galleta UwU")
    def __init__(self,sabor, color):
        self.sabor = sabor
        self.color= color
        print(f"la galleta acaba de ser cocinada {self.sabor} y {self.color}")
#Galleta.sador="Salado"#atributo clase
#galleta = Galleta()
#galleta.sabor="salado"#atributo objeto
#galleta.saludar()
#Galleta.saludar()
galleta_1 = Galleta("cafe", "moras")
galleta_2 = Galleta("blanca","vainilla")

