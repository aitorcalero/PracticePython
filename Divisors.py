
num = int(input("Give me a number: "))

x = range(1,num+1)
y = []

for elem in x:
    if num % elem == 0:
        y.append(elem)

print(y)

