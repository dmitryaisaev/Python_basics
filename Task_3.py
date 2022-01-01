def my_func(val_1, val_2, val_3):
    a = [val_1, val_2, val_3]
    a.sort()
    # print(a)
    return a[1] + a[2]

v1 = float(input('Введите первое число = '))
v2 = float(input('Введите второе число = '))
v3 = float(input('Введите третье число = '))
print(my_func(v1, v2, v3))
