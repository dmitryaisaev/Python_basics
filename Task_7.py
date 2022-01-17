from random import randint
import json

opf = ['ООО', "ЗАО", "ОАО"]

with open('Task_7.txt', 'w', encoding="utf-8") as f:
    for i in range(1, 21):
        f.write(f'Firm_{i} {opf[randint(0, 2)]} {randint(5, 20) * 1000} {randint(1, 15) * 1000}\n')

avr = 0
i = 0
my_dict = {}
with open('Task_7.txt', 'r', encoding="utf-8") as f:
    for el in f:
        _p = float(el.split()[2]) - float(el.split()[3])    # прибыль = выручка - издержки
        my_dict[el.split()[0]] = _p
        if _p > 0:
            i += 1
            avr = avr + _p
    my_list = [my_dict, {'average_profit': round(avr / i, 2)}]

with open("Task_7.json", "w") as f_json:
    json.dump(my_list, f_json)