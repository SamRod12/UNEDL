nombre1= input("ingresa un nombre: ")
nombre2=input("ingresa otro nombre: ")

print("nombre 1: "+ nombre1 +"\nnombre 2: "+nombre2)
if nombre1==nombre2:
    print("Ingreso dos nombre iguales")
else:
    print("ordenados alfabeticamente: ")
    if nombre1<nombre2:
        print(nombre1)
        print(nombre2)
    else:
        print(nombre2)
        print(nombre1)
