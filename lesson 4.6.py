from itertools import count, cycle


print ("Для ввода следующего числа нажмите 'Enter',\nдля выхода из программы - 'Q'")
for num in count(int(input("Введите первое число: "))):
    print(num)
    quit = input()
    if quit == 'q' or quit == 'Q':
        break