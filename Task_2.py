class Road:
    def __init__(self, a_l, a_w):
        self._length = a_l
        self._width = a_w
    def get_weight(self, a1, a2):
        print(f'{self._width} м*{self._length} м*{a1} кг*{a2} см = {self._length * self._width * a1 * a2} т.')

l = float(input('Введите длину дороги в м. = '))
w = float(input('Введите ширину дороги в м. = '))
ms = float(input('Введите массу в кг. асфальта для покрытия 1 кв. метра дороги асфальтом, толщиной в 1 см. = '))
th = float(input('Введите толщину полотна в см. = '))
r1 = Road(l, w)
r1.get_weight(ms, th)
