def my_funk(Aname, Asurname, Abirthyear, Acity, Aemail, Aphone):
    print(F'имя = {Aname}, фамилия = {Asurname}, год рождения = {Abirthyear}, город проживания = {Acity}, email = {Aemail}, телефон = {Aphone}')

name = input('Введите имя = ')
surname = input('Введите фамилию = ')
birthyear = input('Введите год рождения = ')
city = input('Введите город проживания = ')
email = input('Введите email = ')
phone = input('Введите телефон = ')
my_funk(Aname=name, Asurname=surname, Abirthyear=birthyear, Acity=city, Aemail=email, Aphone=phone)

def my_func(val_1, val_2):
    return val_1/val_2
