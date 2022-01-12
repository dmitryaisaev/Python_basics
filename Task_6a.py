from itertools import count
from sys import argv

start = int(argv[1])
for el in count(start):
    if el > start + 10:
        break
    else:
        print(el)
