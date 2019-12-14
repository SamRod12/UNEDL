def ingresar_Datos():
    d = int(input("Ingrese un dia del mes: "))
    m = int(input("Ingrese un mes (1 al 12): "))
    a = int(input("Ingrese un año: "))
    dia_nuevo = dia(d, m, a)
    print(dia_nuevo)

def dia(dia, mes, year):
    de31 = (1, 3, 5, 7, 8, 10, 12)
    de30 = (4, 6, 9, 11)
    de28 = (2, )
    if (mes == 12) and (dia == 31):
        return (dia - 30), de31[0], (year + 1)
    elif mes in de31 and dia == 31:
        return (dia - 30), (mes + 1), year
    elif mes in de30 and dia == 30:
        return (dia - 29), (mes + 1), year
    elif mes in de28 and dia == 28:
        return (dia - 27), (mes + 1), year
    else:
        return (dia + 1), mes, year

ingresar_Datos()