from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


low = 100
high = 1000
my_list = [el for el in range(low, high + 1) if el % 2 == 0]
print(f'Создан список: {my_list}\n Произведение всех элементов списка: {reduce(my_func, my_list)}')
