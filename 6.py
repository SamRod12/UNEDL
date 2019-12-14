def dia_siguiente_t(dia, mes, ano):
    mes31 = ("enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre")
    mes30 = ("abril", "junio", "septiembre", "noviembre")
    mes28 = ("febrero")

    if (mes == 12) and (dia == 31):
        return (dia - 30), mes31[0], (ano + 1)
    elif mes in mes31 and dia == 31:
        return (dia - 30), (mes + 1), ano
    elif mes in mes30 and dia == 30:
        return (dia - 29), (mes + 1), ano
    elif mes in mes28 and dia == 28:
        return (dia - 27), (mes + 1), ano
    else:
        return (dia + 1), mes, ano


print(dia_siguiente_t(1, "julio", 1999))