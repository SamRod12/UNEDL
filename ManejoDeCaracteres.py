frase=input("ingrese una palabra o frase: ")
dos=""
tres=""
cadaDos=""
inversa=""
reflejo=""
for x in range(0, 2):
    dos+=frase[x]
print("primeras dos letras: "+dos)

for x in range(len(frase)-3,len(frase)):
    tres+=frase[x]
print("ultimas tres letras: "+tres)

for x in range(0, len(frase),2):
    cadaDos+=frase[x]
print("cada dos caracteres: "+cadaDos)

x=len(frase)-1
while x>=0:
    inversa+=frase[x]
    x-=1
print("inversa: "+inversa)

reflejo+=frase + inversa
print("reflejo: "+reflejo)