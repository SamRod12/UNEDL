
#Realizar un programa que imprima los numeros del 0 al 100

print("numeros del 0 al 100")

for x in range(101):
	print(x)


#la funcion range puede tener 2 parametros, el primero indica el valor inicial que tomara la 
#varialbe x, cada vuelta del for la variable x toma el valor siguiente
#hasta llegar al valor indicado por el segundo parametro de la funcion range menos uno

print("********************************************")
print("Programa para imprimir numeros del 20 al 30")

for x in range(20,31):
	print(x)


"""La funcion range puede tener tambien 3 parametros, el primero inica el valor incial
que tomara la variable x, el segundo el valor final y el tercer paramteo indica cuanto 
se incrementara cada vuelta X """

print("********************************************")
print("Numero impares del entre 1 y 100")	

for x in range(1,100,2):
	print(x)

#En la primera vuelta del for x recibe el valor 1, la siguiente el valor de 3 hasta el
#valor 99
