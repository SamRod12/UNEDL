frase= input("ingresa una palabra o frase: ")
caracter=input("ingresa un solo caracter para introducir: ")
nuevaFrase=""
for x in range(0,len(frase)):
    if x==len(frase)-1:
        nuevaFrase+=frase[x]
    else:
        nuevaFrase+=frase[x]+caracter

print("tu frase es: "+nuevaFrase)