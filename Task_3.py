class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0.0, "bonus": 0.0}

class Position(Worker):
    def get_full_name(self):
        return self.surname.strip().capitalize() + ' ' + self.name.strip().capitalize()
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

p1 = Position()
p1.name = ' иван '
p1.surname = 'иваноВ '
p1.position = 'Главный специалист'
p1._income['wage'] = 80000
p1._income['bonus'] = 15000
print(f'Полное имя сотрудника: {p1.get_full_name()}')
print('Должность: ' + p1.position)
print(f'Доход: {p1.get_total_income()} р.')
