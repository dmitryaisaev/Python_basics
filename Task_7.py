def fact(val):
    for i in range(1, val + 1):
        res = 1
        for j in range(1, i + 1):
            res = res * j
        yield res

n = int(input('Введите целое число '))
for el in fact(n):
    print(el)
