print("ingrese 5 estaturas en metros: ")
estaturas=[]
suma=0
for x in range(5):
    estatura=float(input("estatura "+ str(x+1)+": "))

    suma+=estatura
    estaturas.append(estatura)

promedio=suma/len(estaturas)
contm=0
contM=0
for y in range(0,len(estaturas)):
    if estaturas[y]<promedio:
        contm+=1
    elif estaturas[y]>promedio:
        contM+=1
print(estaturas)
print("promedio: "+ str(promedio))
print(str(contm)+" personas menores al promedio\n"+str(contM)+" personas mayores al promedio")

