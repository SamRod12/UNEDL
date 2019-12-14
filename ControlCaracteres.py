
while True:
    frase = input("ingrese una palabra o frase de entre 10 y 20 caracteres: ")
    if len(frase)>=10 and len(frase)<=20:
        break
    else:
        print("error, vuelve a ingresar")

print ("frase: "+ frase + "\nno. caracteres: "+ str(len(frase)))
