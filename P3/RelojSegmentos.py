def numSegm (hora):
    cont=0
    for x in hora:
        if x=='0':
            cont+=6
        elif x=='1':
            cont+=2
        elif x=='2':
            cont+=5
        elif x=='3':
            cont+=5
        elif x=='4':
            cont+=4
        elif x=='5':
            cont+=5
        elif x=='6':
            cont+=6
        elif x=='7':
            cont+=3
        elif x=='8':
            cont+=7
        elif x=='9':
            cont+=6
    return cont
def tim(hora,min,seg):
    if len(str(int(hora))) < 2:
        hors = str(hora).zfill(2)
    else:
        hors = str(hora)
    if len(str(int(min))) < 2:
        mins = str(min).zfill(2)
    else:
        mins = str(min)
    if len(str(int(seg))) < 2:
        segs = str(seg).zfill(2)
    else:
        segs = str(seg)
    return hors+":"+mins+":"+segs

print("ingrese una hora en formato hh:mm:ss  : ")
hora=input("hora: ")
min=input("minuto: ")
seg=input("segundo: ")

contTotal=0
time=tim(hora,min,seg)
y=0
z=0

for x in range(0,int(hora)+1,1):
    for y in range(0,60,1):
        for z in range(0,60,1):
            tiempo = ""
            tiempo=tim(x,y,z)
            contTotal+=numSegm(tiempo)
            if tiempo == time:
                break
        if tiempo == time:
            break
        z = 0
    if tiempo==time:
        break
    y = 0

print("tiempo transcurrido "+ tiempo)

print("segmentos encendidos "+str(contTotal))
