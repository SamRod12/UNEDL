import sys
class Agenda:
    lista=[]
    def __init__(self, nombre="", tel="", email=""):
        self.nombre=nombre
        self.tel=tel
        self.email=email

    def agregar(self):
        nombres = self.nombre
        telefonos = self.tel
        emails = self.email
        self.lista.append([nombres,telefonos,emails])

    def imprimirlista(self):
        print(self.lista)

    def listar(self):
        for x in range(len(agenda.lista)):
            print(f"nombre: {agenda.lista[x][0]}")

    def buscar(self,buscar=""):
        for x in range(len(agenda.lista)):
            if buscar.__contains__(agenda.lista[x][0]):
                print(f"nombre: {agenda.lista[x][0]}\ntelefono: {agenda.lista[x][1]}\nemail: {agenda.lista[x][2]}")
                break

    def editar(self,buscar=""):
        for x in range(len(agenda.lista)):
            if buscar.__contains__(agenda.lista[x][0]):
                while True:
                    preg=input(f"que quiere cambiar de {agenda.lista[x][0]}? \nnombre\ttelefono\temail\tsalir\nescriba una de las opciones: ")
                    if preg=='nombre':
                        name=input(f"ingresa el nombre a cambiar\nnombre actual ({agenda.lista[x][0]}): ")
                        agenda.lista[x][0]=name
                    elif preg=='telefono':
                        telef=int(input(f"ingresa el telefono a cambiar\ntelefono actual ({agenda.lista[x][1]}): "))
                        agenda.lista[x][1]=telef
                    elif preg=='email':
                        email=input(f"ingresa el email a cambiar\nemail actual ({agenda.lista[x][2]}): ")
                        agenda.lista[x][2]=email
                    elif preg=='salir':
                        break
                    else:
                        print("opcion no valida")
                break
agenda=Agenda()
while True:
    preg = input("que quiere hacer? \nagregar\tlistar\tbuscar\teditar\tsalir\nescriba una de las opciones: ")
    if preg == 'agregar':
        name = input("ingresa el nombre: ")
        telef = input("ingresa el telefono: ")
        em = input("ingresa el email: ")
        agenda = Agenda(name, telef, em)
        agenda.agregar()
    elif preg == 'listar' :
        agenda.listar()
    elif preg == 'buscar':
        busqueda = input("ingrese el nombre a buscar: ")
        agenda.buscar(busqueda)
    elif preg=='editar':
        busqueda = input("ingrese el nombre a buscar para editar: ")
        agenda.editar(busqueda)
    elif preg == 'salir':
        sys.exit()
    else:
        print("opcion no valida")
