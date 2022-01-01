def my_func_1(Ax, Ay):
    return Ax ** Ay

def my_func_2(Ax, Ay):
    res = Ax
    for i in range(1, abs(Ay)):
        res = res * Ax
    return 1/res

x = float(input('Введите что возводим в степень = '))
y = int(input('Введите степень (целое отрицаткльное число) = '))
if y >=0:
    print('Ошибка, введено не отрирцательное значения степени')
    exit()
print('Вариант 1 =', my_func_1(x, y))
print('Вариант 2 =', my_func_2(x, y))
