from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    @property
    def consumption(self):
        print(f'Расход ткани на пошив пальто: {round(self.param / 6.5, 2) + 0.5}')
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        print(f'Расход ткани на пошив костюма: {self.param * 2 + 0.3}')
        return self.param * 2 + 0.3


coat = Coat(54)
costume = Costume(1.93)
print(coat + costume)
