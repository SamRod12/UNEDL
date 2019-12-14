nombres=["sam","leonardo","karel","carlos","ana"]
contador=0
for x in range(0,len(nombres)):
    if len(nombres[x])>=5:
        contador+=1
        print(nombres[x])

print("nombres con 5 o mas caracteres: "+ str(contador))