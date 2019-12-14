numeros = []
def menMay(cont , numero):

    numeros.append(numero)
    if cont>=2:
        numeros.sort()
        print(numeros)


def carga():

    print("ingresa tres numeros")
    for x in range (3):
        num=int(input(""))
        menMay( x, num)


carga()