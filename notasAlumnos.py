
x=1
menorA = 0
mayorA = 0
while x<=10:
    cal = float(input("ingrese la calificacion del alumno "+ str(x)+ ": "))
    if cal < 7:
        menorA+=1
    else:
        mayorA+=1

    x+=1

print("calificaciones menores a 7: "+ str(menorA))
print("calificaciones mayores o iguales a 7: "+ str(mayorA))
