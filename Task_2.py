class My_exception(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    v1 = int(input('Введите делимое = '))
    v2 = int(input('Введите делитель = '))
    if v2 == 0:
        raise My_exception('Ошибка: деление на 0!')
except ValueError:
    print('Ошибка: введено не число!')
except My_exception as err:
    print(err.txt)
else:
    print(v1 / v2)