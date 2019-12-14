def nombre(nombre, sueldo):
    tupla = (nombre, sueldo)
    return tupla


def fun(tupla1, tupla2):
    nombre = ""
    if tupla1[1] > tupla2[1]:
        nombre = tupla1[0]
    elif tupla1[1] < tupla2[1]:
        nombre = tupla2[0]
    return nombre


nombre1 = input("Digite un nombre: ")
sueldo1 = int(input("Digite un sueldo: "))
nombre2 = input("Digite un nombre: ")
sueldo2 = int(input("Digite un sueldo: "))
print(fun(nombre(nombre1, sueldo1), nombre(nombre2, sueldo2)))