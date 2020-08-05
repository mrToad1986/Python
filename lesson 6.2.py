class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def asp(self):
        asp_mas = int((self.length * self.width * 25 * 5) / 1000)
        return f'Масса асфальта {asp_mas} тонн'


while True:
    try:
        my_road = Road(int(input('Введите длину дороги: ')),
                       int(input('Введите ширину дороги: ')))
        print(my_road.asp())
    except:
        print('Введены неверные значения')
