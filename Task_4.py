class Car:
    is_police = False

    def __init__(self, nm, clr):
        self.speed = 0
        self.color = clr
        self.name = nm

    def go(self):
        if self.speed == 0:
            self.speed = 40
        print(f'{self.name}, машина поехала')

    def stop(self):
        self.speed = 0
        print(f'{self.name}, машина остановилась')

    def turn(self, direction):
        print(f'{self.name}, машина повернула ({direction})')

    def show_speed(self):
        print(f'{self.name}, скорость {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name}, Превышение скорости на {self.speed - 60} км/ч')
        else:
            super().show_speed()    # вызываем метод родителя

class SportCar(Car):
    def show_speed(self):
        print(f'{self.name}, скорость спорткара {self.speed} км/ч')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name}, Превышение скорости на {self.speed - 40} км/ч')
        else:
            super().show_speed()   # вызываем метод родителя

class PoliceCar(Car):
    is_police = True
# =====================================================================================================

tc = TownCar('Toyota', 'Белый')
sc = SportCar( 'Ferrari', 'Красный')
wc = WorkCar('Газель', 'Белый')
pc = PoliceCar('Ford', 'Черный')

print(tc.is_police)
print(sc.is_police)
print(wc.is_police)
print(pc.is_police)

print('===' * 9)

tc.go()
tc.speed = 50
tc.show_speed()
tc.turn('направо')
tc.speed = 80
tc.show_speed()
tc.stop()
tc.show_speed()

print('===' * 9)

wc.go()
wc.speed = 40
wc.show_speed()
wc.turn('налево')
wc.speed = 55
wc.show_speed()
wc.stop()
wc.show_speed()

print('===' * 9)

sc.go()
sc.speed = 200
sc.show_speed()
sc.turn('налево')
sc.stop()
sc.show_speed()

print('===' * 9)

pc.go()
pc.speed = 60
pc.show_speed()
pc.turn('направо')
pc.stop()
pc.show_speed()
