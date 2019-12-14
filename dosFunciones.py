def cuadrado():
    num = int(input("ingresa un numero"))
    num = num*num
    return num
def producto():
    num1 = int(input("ingresa numero 1: "))
    num2 = int(input("ingresa numero 2: "))
    produc=num1*num2
    return produc

cuadrado=cuadrado()
producto=producto()
print("cuadrado de un numero: "+str(cuadrado))
print("producto de dos numeros: "+str(producto))