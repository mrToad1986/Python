inp = input("Введите целое положительное число: ")
num = int(inp)
max = 0
while num > 0:
    if num % 10 > max:
        max = num % 10
    #        print ("текущий максимум ", max)
    num = num // 10
#    print ("остаток числа ", num)
print(f"В числе {inp} наибольшей цифрой является {max}")
