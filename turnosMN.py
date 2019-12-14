print("ingresa los sueldos de los trabajadores del turno matutino: ")
sueldosM=[]
sueldosN=[]

for x in range(8):
    if x<=3:
        sueldoM = float(input("sueldo M " + str(x + 1) + ": "))
        sueldosM.append(sueldoM)
    else:
        sueldoN =float(input("sueldo N " + str(x - 3) + ": "))
        sueldosN.append(sueldoN)

print("Sueldos turno Matutino: "+ str(sueldosM)+"\nSueldos turno Nocturno: "+str(sueldosN))