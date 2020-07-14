def my_func(x, y):
    try:
        x, y = int(x), int(y)
        if x > 0 and y < 0:
            result = 1
            for numbers in range(y, 0):
                result *= 1 / x
            result_decimal = round(result, 6)
            result_fraction = ', или 1/' + str(x ** abs(y))
            return result_decimal, result_fraction
        elif x <= 0:
            return 'Ошибка ввода данных.\nХ должен быть целым положительным числом', ''
        elif y >= 0:
            return 'Ошибка ввода данных.\nY должен быть целым отрицательным числом', ''
    except:
        return 'Ошибка ввода данных.\nВведены нечисловые значения', ''


arg1 = input('Введите основание, целое положительное число: ')
arg2 = input('Введите степень, целое отрицательное число: ')
res1, res2 = my_func(arg1, arg2)
print(f'Результат возведения {arg1} в степень {arg2} равняется:\n{res1}{res2}')