def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i
    return fact
while True:
    numero=int(input("ingresa un numero entero positivo: "))
    if numero>=0:
        print("el factorial de "+str(numero)+" es: "+str(factorial(numero)))
        break
    else:
        print("tu numero no es positivo")
