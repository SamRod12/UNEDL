def vocales(cadena):
    cont=0
    cadena.lower()
    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="e"or cadena[x]=="i" or cadena[x]=="u"or cadena[x]=="o":
            cont+=1

    print("hay " +str(cont)+" vocales en la oracion '"+cadena+"'")

vocales("hola como estas")
vocales("quesadilla")
vocales("mouse")