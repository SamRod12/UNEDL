def imprimirDiccionario(dix):
    for clave in dix:
        print("["+ str(clave)+ " ," , str(dix[clave])+ "]")
avellanas={}
casos = int(input("cuantos casos quiere evaluar? "))
cont=0
total=0
listaCasos=[]
for x in range(casos):
    n=int(input("ingrese el numero de avellanas: "))
    binario=bin(n)[2:]
    listaCasos.append(binario)
    listabin=list(binario)
    for y in range(len(listabin)):
        if listabin[y]=="1":
            cont+=1
    avellanas[x+1] = cont
    total+=cont
    cont=0

print("[caso ,num avellanas]")
imprimirDiccionario(avellanas)
print("numero total de avellanas por todos los casos: "+ str(total))
print("casos de avellanas en binario: ")
print(listaCasos)