revenue = float(input('Введите выручку = '))
expenses = float(input('Введите издержки = '))
profit = revenue - expenses
if profit > 0:
    print(F'Результат: прибыль = {profit}')
    print(F'Рентабельность = {revenue/profit}')
    p_count = int(input('Введите количество сотрудников = '))
    print(F'Прибыль фирмы в расчете на одного сотрудника = {profit/p_count}')
elif profit == 0:
    print('Результат: сработали в ноль')
else:
    print('Результат: убылок')
