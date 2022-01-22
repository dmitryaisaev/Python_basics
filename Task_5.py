class Stationery:
    title = 'Канцелярская принадлежность'
    def draw(self):
        print('Запуск отрисовки»')

class Pen(Stationery):
    title = 'Ручка'
    def draw(self):
        print('Пишем ручкой»')

class Pencil(Stationery):
    title = 'Карандаш'
    def draw(self):
        print('Рисуем карандашом')

class Handle(Stationery):
    title = 'Маркер'
    def draw(self):
        print('Выделяем маркером')

s = Stationery()
p = Pen()
n = Pencil()
h = Handle()

s.draw()
p.draw()
n.draw()
h.draw()
