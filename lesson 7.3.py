class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(["*" * rows for i in range(self.nums // rows)]) + \
               '\n' + "*" * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return f'Сумма количества ячеек двух клеток: {self.nums + other.nums}'

    def __sub__(self, other):
        return f'Разность количества ячеек двух клеток: {self.nums - other.nums}' if self.nums - other.nums > 0 \
            else 'Разность количества ячеек двух клеток должна быть больше нуля'

    def __mul__(self, other):
        return f'Произведение количества ячеек двух клеток: {self.nums * other.nums}'

    def __truediv__(self, other):
        return f'Целочисленное деление количества ячеек двух клеток: {self.nums // other.nums}'


cl_1 = Cell(26)
cl_2 = Cell(8)
print(cl_1 + cl_2)
print(cl_1 - cl_2)
print(cl_2 - cl_1)
print(cl_1 * cl_2)
print(cl_1 / cl_2)
print(f'Внешний вид клетки №1:\n{cl_1.make_order(6)}\n'
      f'и клетки №2:\n{cl_2.make_order(6)}')
