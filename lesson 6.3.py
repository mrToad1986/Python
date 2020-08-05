class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def get_full_profit(self):
        return f'Доход: {sum(self._income.values())}'


employee = Position('Anna', 'Lee', 'manager', 90000, 25000)
print(employee.name)
print(employee.position)
print(employee._income)
print(employee.get_full_name())
print(employee.get_full_profit())
