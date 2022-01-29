class Complex:
    def __init__(self, rez, im):
        self.rez = rez
        self.im = im

    def __str__(self):
        return f'{self.rez} + {self.im}i'

    def __add__(self, other):
        return  Complex(self.rez + other.rez, self.im + other.im)

    def __mul__(self, other):
        return  Complex(self.rez * other.rez - self.im * other.im, self.rez + other.im + other.rez * self.im)


n1 = Complex(2, -1)
print(n1)
n2 = Complex(-8, 3)
print(n2)
print(n1 + n2)
print(n1 * n2)