nums=[]
print("ingresa 5 numeros enteros")
for x in range(5):
    nums.append(int(input("")))

nums.sort()
print("menor a mayor: "+ str(nums))
nums.reverse()
print("mayor a menor: "+ str(nums))