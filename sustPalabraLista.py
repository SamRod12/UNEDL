numPal=int(input("cuantas palabras quiere ingresar? "))
palabras=[]
for x in range(numPal):
    pal=input("ingrese la palabra num " +str(x+1)+": ")
    palabras.append(pal)
print(palabras)
busqueda=input("ingrese la palabra a buscar: ")
sustitucion=input("ingrese la palabra por la que se sustituira: ")
if palabras.__contains__(busqueda):
    palabras.__setitem__(palabras.index(busqueda,0,len(palabras)),sustitucion)
else:
    print("no se encontro la palabra a buscar")
print(palabras)