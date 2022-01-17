from random import randint
_lst = []
_sum = 0
with open('Task_5.txt', 'w+') as f:
    for i in range(1, 11):
        f.write(str(randint(1, 100)) + ' ')
    f.seek(0)
    for ln in f:
        _lst = ln.split()
    for el in _lst:
        _sum = _sum + int(el)
print(_sum)