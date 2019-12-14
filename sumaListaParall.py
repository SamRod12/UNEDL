numsA=[]
numsB=[]
numsC=[]

for x in range(4):
    numsA.append(int(input("ingresa un numero entero en la lista A posicion "+ str(x+1)+": ")))
    numsB.append(int(input("ingresa un numero entero en la lista B posicion "+ str(x+1)+": ")))
    numsC.append(numsA[x]+numsB[x])

print(numsA)
print(numsB)
print(numsC)