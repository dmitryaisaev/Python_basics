from itertools import cycle
from sys import argv

start = argv[1]
i = 0
for el in cycle(start):
    if i > 10:
        break
    else:
        print(el)
    i += 1
