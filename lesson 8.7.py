class ComplexNumber:
    def __init__(self, a, b,):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма комплексных чисел: ')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение комплексных чисел: ')
        return f'z = {self.a * other.a - self.b * other.b} + {self.a * other.b + self.b*other.a} * i'

    def __str__(self):
        return f'z = ({self.a}) + ({self.b}) * i'


z_1 = ComplexNumber(2, 3)
z_2 = ComplexNumber(4, -1)
print(f'Первое комлексное число: {z_1}\nВторое комплексное число: {z_2}')
print(z_1 + z_2)
print(z_1 * z_2)