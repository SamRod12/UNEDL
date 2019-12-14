materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(materias)-1, -1, -1):
    cal = float(input("¿Qué nota has sacado en " + materias[i] + "?"))
    if cal >= 6:
        materias.pop(i)
print("Tienes que repetir " + str(materias))