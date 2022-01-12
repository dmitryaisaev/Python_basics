from sys import argv

def get_salary(t1, t2, t3):
    return t1 * t2 + t3

#print(get_salary(float(argv[1]), float(argv[2]), float(argv[3])))
v1, v2, v3 = map(float, argv[1:])
print(get_salary(v1, v2, v3))
