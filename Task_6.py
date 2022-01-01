def int_func(Astr):
    return Astr.capitalize()

a = input('Введите строку из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре = ').split(' ')
res_str = ''
for el in a:
    res_str = int_func(el) + ' ' + res_str
print(res_str)
