def cargar_candidatos():
    candidatos = []
    for x in range(3):
        nom = input("Ingrese el nombre del candidato:")
        cant = int(input("Los votos de cuantas provincias tiene para cargar?"))
        provincias = []
        for z in range(cant):
            prov = input("Nombre de provincia:")
            votos = int(input("Cantidad de votos:"))
            provincias.append((prov, votos))
        candidatos.append((nom, provincias))
    return candidatos


def totalvotos_candidato(candidatos):
    for x in range(len(candidatos)):
        suma = 0
        for z in range(len(candidatos[x][1])):
            suma = suma + candidatos[x][1][z][1]
        print(candidatos[x][0], suma)

candidatos = cargar_candidatos()
totalvotos_candidato(candidatos)