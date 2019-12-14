"""
hacer un programa que pida 10 numeros y de la opcion que iran de menor a mayor
"""

print("ingrese 10 numeros")
lista = []
for x in range(10):
    numero = int(input("ingrese numero "+str(x+1)+": "))
    lista.append(numero)

while True:
    print("que quieres hacer?\n1)ordenarlos de menor a mayor\n2)ordenarlos de mayor a menor\n3)salir")
    op = int(input(""))
    if op == 1:
        listaord = lista
        listaord.sort()
        print(listaord)
    elif op ==2:
        listadesc= lista
        listadesc.sort(reverse=True)
        print(listadesc)
    elif op ==3:
        break