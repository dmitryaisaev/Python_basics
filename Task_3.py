class My_class:
    def __str__(self):
        return 'Какой-то класс'

class Cell:
    def __init__(self, value):
        self.__cell_numb = value

    def __str__(self):
        if self.__cell_numb < 0:
            return 'Отрицательный результат операции'
        else:
            return str(self.__cell_numb)

    def __add__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            return Cell(self.__cell_numb + other.__cell_numb)
        else:
            raise RuntimeError('Объект не является клеткой')

    def __sub__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            return Cell(self.__cell_numb - other.__cell_numb)
        else:
            raise RuntimeError('Объект не является клеткой')

    def __mul__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            return Cell(self.__cell_numb * other.__cell_numb)
        else:
            raise RuntimeError('Объект не является клеткой')

    def __truediv__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            return Cell(int(round(self.__cell_numb / other.__cell_numb, 0)))
        else:
            raise RuntimeError('Объект не является клеткой')

    def make_order(self, value):
        s = '*' * self.__cell_numb
        return '\n'.join([s[i:i + value] for i in range(0, len(s), value)])


c1 = Cell(int(input('Введите кол. ячеек первой клетки = ')))
c2 = Cell(int(input('Введите кол. ячеек второй клетки = ')))
qqq = My_class()

print(f'Сложение клеток: {c1} + {c2} = {c1 + c2}')
print(f'Вычитание клеток: {c1} - {c2} = {c1 - c2}')
print(f'Умножение клеток: {c1} * {c2} = {c1 * c2}')
print(f'Деление клеток: {c1} / {c2} = {c1 / c2}')

n = int(input('Введите длину ряда = '))
c3 = c1 * c2
print(f'Порядок ячеек клетки по рядам:\n{c3.make_order(n)}')

print(c1 * qqq)
