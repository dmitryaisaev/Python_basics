from random import randint

class Matrix:
    def __init__(self, value):
        self.m_array = value

    def __str__(self):
        return '\n'.join(['\t'.join([str(self.m_array[i][j]) for j in range(len(self.m_array[i]))]) for i in range(len(self.m_array))])

    def __add__(self, other):
        return Matrix([[self.m_array[i][j] + other.m_array[i][j] for j in range(len(self.m_array[i]))] for i in range(len(self.m_array))])



k = int(input('Введите предел значений матриц = '))
n = int(input('Введите количество строк = '))
m = int(input('Введите количество столбцов = '))
my_matrix1 = Matrix([[randint(1, k) for j in range(m)] for i in range(n)])
my_matrix2 = Matrix([[randint(1, k) for j in range(m)] for i in range(n)])
print(f'\nМатрица 1:\n{my_matrix1}')
print(f'\nМатрица 2:\n{my_matrix2}')
print('\nРезультат:')
print(my_matrix1 + my_matrix2)
