def mayorMenor(*lista):
    mayor = []
    for x in range(len(lista)):
        if lista[x]>=18:
           mayor.append(lista[x])
    return mayor
print("La edades mayores en la lista, 4,18,19,20,3,4,34 son: ")
print(mayorMenor(4,18,19,20,3,4,34))