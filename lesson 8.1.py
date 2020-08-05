class Date:
    def __init__(self, raw_date):
        self.raw_date = raw_date

    @classmethod
    def extract(cls, raw_date):
        my_date = []
        for i in raw_date.split('-'):
            my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if day in range(1, 31) and month in range(1, 12) and year in range(0, 2020):
            return 'Дата введена верно'
        else:
            return 'Дата введена неверно'

    def __str__(self):
        return f'Дата {Date.extract(self.raw_date)}'


print(Date.extract('26-06-2007'))
print(Date.valid(26, 6, 2007))
print(Date.valid(26, 14, 2007))
my_date = Date('13-11-2006')
print(my_date.extract('13-11-2006'))
print(my_date.valid(13, 11, 2006))
