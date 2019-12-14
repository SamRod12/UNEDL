productos=[]
precio=[]
cont=0
for x in range(5):
    productos.append(input("ingresa el nombre del producto: "))
    precio.append(float(input("ingresa el precio del producto: ")))
    if precio[x]>precio[0]:
        cont+=1

print("productos con el precio mayor al primer producto ingresado: "+str(cont))