class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Машина: {self.name} (цвет {self.color}) полицейская машина: {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}.')

    def car_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}.'


class TownCar(Car):
    def car_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"


class WorkCar(Car):
    def car_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        Car.__init__(self, name, color, speed, is_police)


class SportCar(Car):
    '''SportCar'''


town_car = TownCar('"Mazda"', 'синий', 60)
print(f'Машина: {town_car.name}')
print(f'Цвет: {town_car.color}')
town_car.go()
print(town_car.car_speed())
town_car.turn(0)
town_car.turn(1)
town_car.stop()

town_car_2 = TownCar('"Subary"', 'красный', 90)
town_car_2.go()
print(town_car_2.car_speed())
town_car_2.stop()

work_car = WorkCar('"Arctos"', 'черный', 40)
work_car.go()
print(work_car.car_speed())
work_car.stop()

police_car = PoliceCar('"Ford"', 'бело-синий', 100)
police_car.go()
print(police_car.car_speed())
police_car.turn(1)
police_car.stop()

sport_car = SportCar('"Mustang"', 'желтый', 160)
sport_car.go()
print(sport_car.car_speed())
sport_car.stop()

new_speed = 40
while new_speed <= 100:
    new_car = TownCar('"Лада Калина"', 'баклажановый', new_speed)
    new_car.go()
    print(new_car.car_speed())
    new_car.stop()
    new_speed += 20
