def creartiempo(horas, minutos, segundos):
    horas = int(input("Ingrese las horas:"))
    minutos = int(input("Ingrese los minutos:"))
    segundos = int(input("Ingrese los segundos:"))
    if segundos > 59:
        segundos1 = (segundos / 60)
        minutos1 = minutos + segundos1
    horas1 = horas
    if minutos > 59:
        horas1 = horas + 1
    return (horas1, minutos1, segundos1 - segundos1)

print(creartiempo(1, 1, 120))