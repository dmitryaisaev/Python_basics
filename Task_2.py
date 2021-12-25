lst = []
i = 1
s = input(F'Введите элемент № 1 (для завершения наберите "stop") = ')
while s != 'stop':
    lst.append(s)
    s = input(F'Введите элемент № {i + 1} (для завершения наберите "stop") = ')
print(lst)
for i in range(0, (len(lst) // 2) * 2, 2):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(lst)