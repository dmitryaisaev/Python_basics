goods = [
            (1, {'название': '', 'цена': 0, 'количество': 0, 'eд': ''}),
            (2, {'название': '', 'цена': 0, 'количество': 0, 'eд': ''}),
            (3, {'название': '', 'цена': 0, 'количество': 0, 'eд': ''})
        ]
my_dic = {
            'название': [],
            'цена': [],
            'количество': [],
            'eд': []
         }
for i in range(0, len(goods)):
    goods[i][1].update({'название': input('Введите название товара = ')})
    goods[i][1].update({'цена': input('Введите цену = ')})
    goods[i][1].update({'количество': input('Введите количествотовара = ')})
    goods[i][1].update({'eд': input('Введите единицу измерения = ')})

for i in range(0, len(goods)):
    print(goods[i])

for i in range(0, len(goods)):
     my_dic.get('название').append(goods[i][1].get('название'))
     my_dic.get('цена').append(goods[i][1].get('цена'))
     my_dic.get('количество').append(goods[i][1].get('количество'))
     my_dic.get('eд').append(goods[i][1].get('eд'))

print('Названия', my_dic.get('название'))
print('Цены', my_dic.get('цена'))
print('Кол.', my_dic.get('количество'))
print('Ед', my_dic.get('eд'))
