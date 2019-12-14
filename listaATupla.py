tupla=("dato1",2000,443,"hola")
lista=list(tupla)
print("esto es una tupla: "+ str(tupla))
print("tupla convertida a lista" + str(lista))
index=int(input("ingresa la posicion que quieres modificar (1 a "+ str(len(lista))+ "): "))
lista[index-1]=input("ingresa un dato: ")
tuplaModificada=tuple(lista)

print("lista modificada convertida a tupla: "+str(tuplaModificada))


