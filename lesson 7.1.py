m_1 = [[3, 5, 8, 3], [8, 3, 7, 1], [2, 0, 4, -2]]
m_2 = [[6, 2, 4, 3], [3, 6, 5, 1], [4, 5, 3, 6]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)
print(f'matrix_1\n{matrix_1}\n{"*" * 15}')
print(f'matrix_2\n{matrix_2}\n{"*" * 15}')
print(f'matrix_sum\n{matrix_1 + matrix_2}\n{"*" * 15}')
