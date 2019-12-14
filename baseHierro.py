"""una planta de bases de hierro posee un lote de n piezas
crear un programa que pida el numero de piezas a procesar y luego ingrese la longitud de cada base
sabiendo la longitud de cada base sabiendo qe las piezas cuya longitud esten en el rango de 1.2 y 1.3 son aptas
imprimir en pantalla la cantidad de piezas aptas que hay en el lote
"""
n=int(input("cuantas piezas vas a ingresar? "))
x=1
aptas = 0
noAptas = 0
while x<=n:
    base = float(input("ingrese la base de las pieza "+ str(x)+ ": "))
    if base >=1.2 and base <=1.3:
        aptas+=1
    else:
        noAptas+=1

    x+=1

print("piezas aptas en el lote: "+ str(aptas))
