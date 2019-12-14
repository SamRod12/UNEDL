def maymen(list):
    mayor = list[0]
    menor = list[0]
    for x in range(5):
        if list[x] > mayor:
            mayor = list[x]
        elif list[x] < menor:
            menor = list[x]
    tupla = (mayor, menor)
    return tupla

lista = [1, 3, 5, 6, 2]
print(maymen(lista))