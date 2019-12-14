n=int(input("cuantos numeros ingresara? "))
x=1
par = 0
impar = 0
while x<=n:
    num = int(input("ingrese el numero "+ str(x)+ ": "))
    if num%2 ==1:
        impar+=1
    else:
        par+=1

    x+=1

print("numeros pares: "+ str(par))
print("numeros impares: "+ str(impar))
