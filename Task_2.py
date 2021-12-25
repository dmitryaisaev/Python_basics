time_is_sec = int(input('Введите время в секудах = '))
ss = time_is_sec % 60
hh = time_is_sec // 3600
mm = abs(time_is_sec // 60 - 60 * hh)
print(F'Время в формате чч:мм:сс = {hh}:{mm}:{ss}')
