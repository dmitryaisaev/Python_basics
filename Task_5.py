my_list = [7, 5, 3, 3, 2]
n = int(input('Введите число = '))
for i in range(0, len(my_list)):
    if n > my_list[i]:
        my_list.insert(i, n)
        break
    if i == len(my_list) - 1:
        my_list.append(n)
print(my_list)
