numPal=int(input("cuantas palabras quiere ingresar? "))
palabras=[]
for x in range(numPal):
    pal=input("ingrese la palabra num " +str(x+1)+": ")
    palabras.append(pal)

print(palabras)