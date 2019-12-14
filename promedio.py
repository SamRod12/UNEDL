""" realizar un programa que permite la carga de diez numeros y muestre la sma y promedio de los mismos"""
print("ingrese 10 numeros.")
x=1
suma=0
while x<=10:
    n = int(input("ingrese numeros:"))
    suma+=n
    x=x+1


promedio = suma/10
print("la suma es: "+str(suma))
print("el promedio es: " + str(promedio))