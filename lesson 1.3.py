n = input("Введите целое положительное число: ")
if int(n) <= 0:
    print("Вы ошиблись при вводе данных. Попробуйте еще раз")
    n = input("Введите целое положительное число: ")
n2 = n + n
n3 = n2 + n
sum = int(n) + int(n2) + int(n3)
print(f"Cумма чисел вида 'n + nn + nnn' составит: {sum}")