i = 0
_sum = 0
with open('Task_3.txt', encoding="utf-8") as f:
    print('Сотрудники с величиной оклада менее 20 000:')
    for ln in f:
        i += 1
        if float(ln.split()[1]) < 20000:
            print(ln.split()[0])
        _sum = _sum + float(ln.split()[1])
    print('Средняя величина дохода = ', round(_sum / i, 2))
