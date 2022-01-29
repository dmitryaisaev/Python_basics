class Unit:
    def __init__(self, name):
        self.__name = name
        self._store = {}

    def __str__(self):
        return self.__name

    def get_store(self):
        s1 = f'В подразделении {self.__name}:\n'
        for k, v in self._store.items():
            if v:
                s2 = str(v[0])
                for i in range(1, len(v)):
                    s2 += ', ' + str(v[i])
            else:
                s2 = 'пусто'
            s1 += f'Товар: {k}, состав: = {s2}\n'
        return s1
    @staticmethod
    def get_descr(value):
        if isinstance(value, Printer):
            return 'Printer'
        elif isinstance(value, Copyr):
            return 'Copyr'
        elif isinstance(value, Xerox):
            return 'Xerox'
        else:
            print(f'Invalid object {type(value)}')
            return None
    @staticmethod
    def add_object(to_unit, obj):
        descr = Unit.get_descr(obj)
        if descr != None:
            v1 = to_unit._store.get(descr, 0)
            if v1 == 0:
                to_unit._store[descr] = [obj]
            else:
                if obj in v1:
                    print(f'Ошибка: Объект {obj.name} уже есть в {to_unit.__name}')
                else:
                    v1.append(obj)
                    to_unit._store[descr] = v1
    @staticmethod
    def del_object(from_unit, obj):
        descr = Unit.get_descr(obj)
        if descr != None:
            v1 = from_unit._store.get(descr, 0)
            if v1 != 0:
                v1.remove(obj)
            if not v1:
                del from_unit._store[descr]

    def push(self, from_unit, *arg):
        print(f'Переместить в {self} из {from_unit}\n')
        for el in arg:
            Unit.add_object(self, el)
            if from_unit != None:
                Unit.del_object(from_unit, el)

    def pop(self, to_unit, *arg):
        print(f'Переместить в {to_unit} из {self}\n')
        for el in arg:
            Unit.del_object(self, el)
            if to_unit != None:
                Unit.add_object(to_unit, el)

class Warehouse(Unit):
    def __init__(self):
        super().__init__('Основной склад')

class Department(Unit):
    pass

class Tech:
    def __init__(self, nm):
        self.name = nm
    def __str__(self):
        return self.name

class Printer(Tech):
    def __init__(self, nm, type):
        super().__init__(nm)
        self.type = type

class Copyr(Tech):
    def __init__(self, nm, format):
        super().__init__(nm)
        self.format = format

class Xerox(Tech):
    def __init__(self, nm,  isclr):
        super().__init__(nm)
        self.iscolor = isclr

# ===================================================================================================================

w1 = Warehouse()
d1 = Department('Кадры')
d2 = Department('Бухгалтерия')
p1 = Printer('HP LaserJet', 'Laser')
p2 = Printer('Epson', 'Inkjet')
c1 = Copyr('Rico', 'A4')
x1 = Xerox('NoName', True)

w1.push(None, p1, p2, c1, x1, x1, p2)
print(w1.get_store())
w1.pop(d1, p1)
print(w1.get_store())
print(d1.get_store())
w1.pop(d2, c1)
print(w1.get_store())
print(d2.get_store())