nums=[]
print("ingresa 10 numeros enteros: ")
for x in range (10):
    nums.append(int(input("")))


print("lista: " +str(nums)  )
for x in range (10):
    if  nums.__contains__(5):
        nums.remove(5)
print("lista sin el numero 5: "+ str(nums))