n=int(input("cuantos empleados hay en la empresa? "))
x=1
entre500_900 = 0
mas1000 = 0
menos500 = 0
importeTotal = 0
while x<=n:
    sueldo = float(input("ingrese el sueldo del empleado "+ str(x)+ ": "))
    if sueldo >=500 and sueldo <=900:
        entre500_900+=1
    elif sueldo >=1000:
        mas1000+=1
    elif sueldo <500:
        menos500+=1

    importeTotal+=sueldo
    x+=1

print("empleados que cobran entre 500 y 900: "+ str(entre500_900))
print("empleados que cobran mas de 1000: "+ str(mas1000))
print("importe total: "+ str(importeTotal))
