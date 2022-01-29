class My_class:
    __lst = []
    def __str__(self):
        return ','.join(map(str, self.__lst))

    def __call__(self, *args, **kwargs):
        try:
            self.__lst.extend(map(int, args))
        except ValueError:
            print('Введено неверное значение')

m = My_class()
while True:
    v1 = input('Введите число = ')
    if v1 == 'stop':
        print(m)
        break
    m(v1)
