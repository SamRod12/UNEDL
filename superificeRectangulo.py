def rectanguloSuperficie(ladoA,ladoB):
    superficie=ladoA*ladoB
    return superficie

superficie1=rectanguloSuperficie(33,21)
superficie2=rectanguloSuperficie(20,32)

print("rectangulo 1: "+str(superficie1))
print("rectangulo 2: "+str(superficie2))
if superficie1>superficie2:
    print("la superficie del rectangulo 1 es mayor")
elif superficie1<superficie2:
    print("la superficie del rectangulo 2 es mayor")
else:
    print("la superficie de los dos rectangulos es igual")