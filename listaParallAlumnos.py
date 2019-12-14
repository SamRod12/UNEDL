alumnos=[]
nota=[]
condicion=[]
cont=0
for x in range(4):
    alumnos.append(input("ingresa el nombre del alumno: "))
    nota.append(float(input("ingresa la calificacion del alumno: ")))
    if nota[x]>=8:
        condicion.append("Muy bueno")
        cont+=1
    elif nota[x]<8 and nota[x]>=4:
        condicion.append("Bueno")
    elif nota[x]<4:
        condicion.append("Insuficiente")

print("alumnos con muy buena calificacion: "+str(cont))
print("alumnos:      "+str(alumnos))
print("condicion:    "+str(condicion))
print("calificacion: "+str(nota))