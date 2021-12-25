my_str = input('Введите строку ')
my_lst = my_str.split()
i = 1
for el in my_lst:
    if len(el) > 10:
        print(i, el[:10])
    else:
        print(i, el)
    i = i + 1
