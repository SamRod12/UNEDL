import random
listaLados=[]
for x in range (3):
    num = random.randrange(1,100)
    listaLados.append(num)
listaLados.sort()
print(listaLados)
if  listaLados[1]!=listaLados[2] and listaLados[0]!=listaLados[2] and  listaLados[1]!=listaLados[0]:
    print("el triangulo es un triangulo escaleno ")
elif  listaLados[1]==listaLados[2] and listaLados[0]==listaLados[2] and  listaLados[1]==listaLados[0]:
    print("el triangulo es equilatero")
elif listaLados[1]==listaLados[2] or listaLados[0]==listaLados[2] or  listaLados[1]==listaLados[0]:
    print("el triangulo es isoseles")