diccionario={"apple":"manzana", "bubble":"burbuja","bread":"pan","mouse":"raton","pineapple":"piña","eye":"ojo", "light":"luz","tiny":"pequeño","attack":"atacar","strong":"fuerte"}
def cargar():
    ingles = input("ingresa la palabra en ingles: ")
    castellano = input("ingresa su traduccion en castellano: ")
    diccionario[ingles] = castellano

def imprimirDiccionario(dix):
    for clave in dix:
        print(clave, dix[clave])

def imprimirTraduccion(clave):
    print(clave,diccionario[clave])

def buscar(pal,dix):
    resp=True
    for clave in dix:
        if pal==clave:
            resp=True
            break
        else:
            resp=False
    return resp

while True:
    accion=input("que quieres hacer? \nbuscar\nimprimir\nsalir\n")
    if accion=="buscar":
        buqueda=input("ingresa la palabra a buscar en ingles: ")
        if buscar(buqueda,diccionario)==True:
            print("palabra econtrada: ")
            imprimirTraduccion(buqueda)
            print("")
        else:
            accion2=input("no se encontro la palabra, quiere agregarla al diccionario?\nsi/no\n")
            if accion2=="si":
                cargar()
                imprimirDiccionario(diccionario)
            elif accion2=="no":
                imprimirDiccionario(diccionario)
    elif accion == "imprimir":
        imprimirDiccionario(diccionario)
    elif accion == "salir":
        break
print("adios...")

