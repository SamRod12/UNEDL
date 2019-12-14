lista=[]

cantidad=int(input("cuantas palabras quiere ingresar?"))
print("escribe "+ str(cantidad)+" palabras: ")
for x in range(cantidad):
    lista.append(input(""))


print("imprimir lista...\n\n\n")
print(lista)