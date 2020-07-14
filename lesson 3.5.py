def my_sum():
    sum = 0
    while True:
        my_list = input('Введите ряд целых чисел. Для завершения введите q.: ')
        my_list = my_list.split()
        for number in my_list:
            if number == 'q' or number == 'Q':
                return sum
            else:
                try:
                    number = int(number)
                    sum += number
                except:
                    return 'Ошибка ввода данных'
        return f'Сумма числе равна: {sum}'


print(my_sum())
