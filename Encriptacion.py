print("\tCodigo Murcielago")
murcielago = ["m", "u", "r", "c", "i", "e", "l", "a", "g", "o"]
salida = ""
cadena=""
while True:
    x = int(input("0) Salir\n1) Encriptar\n2) Desencriptar\n3) borrar palabra actual\nOpcion: "))
    if len(cadena)!=0 and x==3:
        cadena=""
    if not cadena:
        cadena=input("Escriba su palabra o frase: ").lower()

    if x == 1:
        for i in range(len(cadena)):
            if cadena[i] in murcielago:
                salida += str(murcielago.index(cadena[i]))
            else:
                salida += cadena[i]
    if x == 2:
        for i in range(len(cadena)):
            if cadena[i].isdigit():
                salida += murcielago[int(cadena[i])]
            else:
                salida += cadena[i]
    print("\t",salida)
    salida = ""
    if x == 0:
        break

