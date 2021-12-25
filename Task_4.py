n = input('Введите целое положительное число = ')
i = 1
m = n[0]
while i < len(n):
    if n[i] > m:
        m = n[i]
    i = i + 1
print(m)
