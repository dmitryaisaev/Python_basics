from functools import reduce

def my_func(p1, p2):
    return p1 * p2

my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(my_func, my_list))
