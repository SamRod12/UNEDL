empleados=int(input("cuantos empleados hay? "))
sueldos=[]
for x in range(empleados):
    sueldos.append(float(input("ingresa el sueldo "+ str(x+1)+": ")))

sueldos.sort()
print(sueldos)