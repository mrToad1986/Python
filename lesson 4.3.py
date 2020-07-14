low = 20
high = 240
my_list = [el for el in range(low, high+1) if el % 20 == 0 or el % 21 == 0]
print(f'Список чисел, кратных 20 или 21 в пределах от {low} до {high} включительно: {my_list}')