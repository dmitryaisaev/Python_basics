f = open('Task_1.txt', 'w')
while True:
    _str = input('Введите строку для записи в файл ')
    if _str == '':
        break
    f.write(_str + '\n')
f.close
