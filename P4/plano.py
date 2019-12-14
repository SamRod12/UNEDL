import math
class Punto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def cuadrante(self):
        if self.x==0 and self.y!=0:
            print(f"el punto ({self.x},{self.y}) esta en el eje x ")
        elif self.x!=0 and self.y==0:
            print(f"el punto ({self.x},{self.y}) esta en el eje y ")
        elif self.x==0 and self.y==0:
            print(f"el punto ({self.x},{self.y}) esta en el origen ")
        elif self.x>0 and self.y>0:
            print(f"el punto ({self.x},{self.y}) esta en el cuadrante 1 ")
        elif self.x < 0 and self.y > 0:
            print(f"el punto ({self.x},{self.y}) esta en el cuadrante 2 ")
        elif self.x < 0 and self.y < 0:
            print(f"el punto ({self.x},{self.y}) esta en el cuadrante 3 ")
        elif self.x > 0 and self.y < 0:
            print(f"el punto ({self.x},{self.y}) esta en el cuadrante 4 ")
    def vector(self,p):
        print(f"El vector entre {self} y {p} es ({p.x-self.x},{p.y-self.y})")
    def distancia(self, p):
        dist = math.sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
        print(f"La distancia entre los puntos {self} y {p} es {dist}")


class Rectangulo:
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
        self.Base = abs(self.pFinal.x - self.pInicial.x)
        self.Altura = abs(self.pFinal.y - self.pInicial.y)
        self.Area = self.Base * self.Altura
    def base(self):
        print(f"La base del rectángulo es {self.Base}")
    def altura(self):
        print(f"La altura del rectángulo es {self.Altura}")
    def area(self):
        print(f"El área del rectángulo es {self.Area}")

puntoA=Punto(2,3)
puntoB=Punto(5,5)
puntoC=Punto(-3,-1)
puntoD=Punto(0,0)

Punto.cuadrante(puntoA)
Punto.cuadrante(puntoC)
Punto.cuadrante(puntoD)

Punto.vector(puntoA,puntoB)
Punto.vector(puntoB,puntoA)

Punto.distancia(puntoA,puntoB)
Punto.distancia(puntoB,puntoA)

rectangulo = Rectangulo(puntoA,puntoB)
rectangulo.base()
rectangulo.altura()
rectangulo.area()