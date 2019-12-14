"""
crear una serie de 10 palabras donde las letras de esas palabras se van a generar aleatoriamente e imprimirlas alfabeticamente
"""
import string
import random
lista=[]

letters = string.ascii_lowercase
 # where k is the number of required rand_letters

for x in range(10):
    letras = random.choices(letters, k=5)
    strings = ''.join(map(str, letras))
    lista.append(strings)
    lista.sort()


print(lista)
