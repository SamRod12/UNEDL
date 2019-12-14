def cargar():
    productos={}
    for x in range (5):
        nombre=input("ingresa nombre del producto: ")
        precio=float(input("ingresa precio: "))
        productos[nombre]=precio
    return productos
def imprimir(prod):
    for clave in prod:
        print(clave, prod[clave])

producto=cargar()

imprimir(producto)