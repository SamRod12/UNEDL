print("ingrese 5 sueldos: ")
sueldos=[]
suma=0

for x in range (5):
    sueldo= float(input("sueldo " + str(x+1)+": "))
    sueldos.append(sueldo)
    suma+=sueldo

promedio=suma/len(sueldos)
print(sueldos)
print("promedio sueldos: "+ str(promedio))