import re

my_dict = {}
with open('Task_6.txt', 'r', encoding="utf-8") as f:
    for ln in f:
        # разделяем по ":"
            # берем первую часть
            # берем вторую часть разделения
                # берем сумму списка
                    # конвертируем елементы списка в int
                        # ищем регуляркой блоки из цифр возвращаем список
        my_dict[ln.split(':', 1)[0]] = sum(list(map(int, re.findall(r'\d+', ln.split(':', 1)[1]))))
print(my_dict)
