frase = input("ingrese una palabra o frase: ")
x=0
contador=0
fraseMinus=frase.lower()
while x<len(fraseMinus):

    if fraseMinus[x]=="a" or fraseMinus[x]=="e" or fraseMinus[x]=="i" or fraseMinus[x]=="o" or fraseMinus[x]=="u":
        contador+=1
    x+=1

print("hay "+ str(contador)+" vocales en la oracion")