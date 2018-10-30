a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

cut = input("Give me a number: ")

for n in a:
    if n <= int(cut):
        b.append(n)

print(b)