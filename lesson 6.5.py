class Stationery:
    def __init__(self, title='Канцелярская принадлежность.'):
        self.title = title
    def draw(self):
        print(f'Начинаем рисование. {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Начинаем рисование. Ручка: {self.title}.')

class Pencil(Stationery):
    def draw(self):
        print(f'Начинаем рисование. Карандаш: {self.title}.')

class Handle(Stationery):
    def draw(self):
        print(f'Начинаем рисование. Маркер: {self.title}.')

my_stationery = Stationery()
my_stationery.draw()
my_pen = Pen('Черная')
my_pen.draw()
my_pencil = Pencil("Красный")
my_pencil.draw()
my_handle = Handle("Желтый")
my_handle.draw()