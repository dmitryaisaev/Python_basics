def my_func(str_val):
    res = 0
    for el in str_val.split(' '):
        if el == 'stop':
            break
        try:
            res = res + float(el)
        except ValueError:
            print(F'Ошибка: {el} не является числом')
            # pass
    return res

sum_total = 0
while True:
    s = input('Введите строку чисел через пробел = ')
    sum_total = sum_total + my_func(s)
    print('Сумма введенных чисел =', sum_total)
    if s.find('stop') > -1:
        break
