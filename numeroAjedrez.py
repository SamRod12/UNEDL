trigo = 0
for x in range(64):
    trigo+=2**x

print(trigo)

"""el sabio pido al inicio un grano de trigo y por cada casilla extra ese numero fuera el doble del anterior y se fuera sumando
entonces se toma la bas 2 porue se ira duplicando el numero de granos y se ira sumando a la cantidad anterior de granos
de trigo por eso obtenemos 18,446,744,073,709,551,615 , ya ue es la sumatoria de 2^n  n=cantidad de casillas
"""