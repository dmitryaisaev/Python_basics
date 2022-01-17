i = 0
with open('Task_4_new.txt', 'w', encoding="utf-8") as f1:
    with open('Task_4.txt', encoding="utf-8") as f2:
        for ln in f2:
            i += 1
            if ln.split()[0] == 'One':
                f1.write(ln.replace('One', 'Один'))
            elif ln.split()[0] == 'Two':
                f1.write(ln.replace('Two', 'Два'))
            elif ln.split()[0] == 'Three':
                f1.write(ln.replace('Three', 'Три'))
            elif ln.split()[0] == 'Four':
                f1.write(ln.replace('Four', 'Четыре'))
print('Обработано строк = ',  i)