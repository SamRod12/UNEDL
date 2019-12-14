empleado=[]
sueldo=[]
cont=int(input("cuantos empleados hay? "))

for x in range(cont):
    empleado.append(input("ingresa el nombre del empleado: "))
    sueldo.append(float(input("ingresa el sueldo del empleado: ")))
print(empleado)
print(sueldo)
print("\n\n\n")
for x in range (len(sueldo)):
    if sueldo[x]>10000:
        sueldo[x]=0
        empleado[x]="."

for x in range (cont):
    if  sueldo.__contains__(0) and empleado.__contains__("."):
        sueldo.remove(0)
        empleado.remove(".")

print(empleado)
print(sueldo)
