f_sel = input('Если хотите использовать файл из первого задания введите 1 если заране созданный 2 = ')
if f_sel == '1':
    fname = 'Task_1.txt'
elif f_sel == '2':
    fname = 'Task_2.txt'
else:
    print('Неверный ввод')
    exit

with open(fname, 'r') as f:
    i = 0
    for ln in f:
        i += 1
        print(f'Количество слов в {i}-й строке = ', len(ln.split()))
    print('Колмчество строк в файле = ', i)
