def cantidad(cadena):
    conta=0
    contA=0
    for x in range(len(cadena)):
        if cadena[x]=="a":
            conta+=1
        elif cadena[x]=="A":
            contA+=1
    print("cantdidad de a´s: "+ str(conta))
    print("cantidad de A´s: "+ str(contA))

palabra=input("ingresa una palabra en mayusculas o minusculas")
cantidad(palabra)
