import random
billetes = [0.1,0.2,0.5,1,2,5,10,20,50,100,200,500,1000]
contadorbill=[0,0,0,0,0,0,0,0,0,0,0,0,0]
num = random.uniform(1,10000)
num = round(num,1)
comp = num
comps = comp
comps = round(comps,0)
print(num)
suma = 0

while True:
    for x in range (len(billetes)):
        if comp % billetes[12] == 0 :
            suma += billetes[12]
            comp -= suma
            contadorbill[12] +=1
            break
        elif comp % billetes[11] == 0:
            suma += billetes[11]
            comp -= suma
            contadorbill[11] += 1
            break
        elif comp % billetes[10] == 0 :
            suma += billetes[10]
            comp -= suma
            contadorbill[10] += 1
            break
        elif comp % billetes[9] == 0 :
            suma += billetes[9]
            comp -= suma
            contadorbill[9] += 1
            break
        elif comp % billetes[8] == 0  :
            suma += billetes[8]
            comp -= suma
            contadorbill[8] += 1
            break
        elif comp % billetes[7] == 0 :
            suma += billetes[7]
            comp -= suma
            contadorbill[7] += 1
            break
        elif comp % billetes[6] == 0 :
            suma += billetes[6]
            comp -= suma
            contadorbill[6] += 1
            break
        elif comp % billetes[5] == 0 :
            suma += billetes[5]
            comp -= suma
            contadorbill[5] += 1
            break
        elif comp % billetes[4] == 0 :
            suma += billetes[4]
            comp -= suma
            contadorbill[4] += 1
            break
        elif comp % billetes[3] == 0 :
            suma += billetes[3]
            comp -= suma
            contadorbill[3] += 1
            break
        elif comp % billetes[2] == 0 :
            suma += billetes[2]
            comp -= suma
            contadorbill[2] += 1
            break
        elif comp % billetes[1] == 0 :
            suma += billetes[1]
            comp -= suma
            contadorbill[1] += 1
            break
        elif comp % billetes[0] == 0 :
            suma += billetes[0]
            comp -= suma
            contadorbill[0] += 1
            break
    suma = round(suma,0)
    if suma == comps:
        break

print(str(suma)+" True" )
for x in range(len(billetes)-1,0,--1):
    print(f"billetes de {billetes[x]} hay {contadorbill[x]}")