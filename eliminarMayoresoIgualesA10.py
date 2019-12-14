nums=[]
numsCopy=[]
print("ingresa 5 numeros enteros: ")
for x in range (5):
    nums.append(int(input("")))
numsCopy=nums.copy()
print(nums)
for x in range(len(nums)):
    if numsCopy[x]>=10:
        numsCopy[x]= -1
for x in range(len(nums)):
    if numsCopy.__contains__(-1):
        numsCopy.remove(-1)
print(numsCopy)