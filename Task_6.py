k_count = int(input('Введите результат за 1 день, км = '))
r_count = int(input('Введите цель, км = '))
i = 2
print('1-й день:', k_count)
while k_count < r_count:
    k_count = round(k_count + k_count * 0.1, 2)
    print(F'{i}-й день: {k_count}')
    i = i + 1
