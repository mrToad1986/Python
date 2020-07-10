my_list = []
i = 0
j = 0
my_list_len = int(input("Укажите длину создаваемого списка: "))
while i < my_list_len:
    my_list.append(input("Введите значение следующего элемента: "))
    i += 1
print(f"Список создан {my_list}")
for element in range(int(len(my_list) / 2)):
    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    j += 2
print(f"Список изменен {my_list}")
