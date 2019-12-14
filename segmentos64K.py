#1.-0950:0100
#2.-0CD1:02E0
#3.-08F1:0100
#4.-09DE:0250
#5.-A179:0200
#6.-B844:0100
#7.-5D37:02E0
direccion= [0x0950,0x0cd1,0x08f1,0x09de,0xa179,0xb844,0x5d37]
desplazamiento=[0x0100,0x02e0,0x0100,0x0250,0x0200,0x0100,0x02e0]
segmentoAjustado =[]

for x in range (0,len(direccion)):
    ajuste = direccion[x]*0x0010
    segmento = ajuste + desplazamiento[x]
    segmentoAjustado.append(segmento)
    print(str(x+1) +"\najuste: "+ hex(ajuste)+ "\nsegmento ajustado + desplazamiento : "+ hex(segmentoAjustado[x])+"\n")
for x in range (0,len(direccion)):
    print(str(x+1)+"- "+hex(segmentoAjustado[x]))

print("listado en enteros: "+str(segmentoAjustado))

