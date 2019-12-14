cadena=input("ingresa una frase o palabra: ")
x=0
contador=0
while x<len(cadena):
    if cadena[x]==" " :
        contador+=1
    x+=1

print("hay "+ str(contador) + " espacios en blanco")
