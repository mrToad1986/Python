def div(arg1, arg2):
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
        result = round((arg1 / arg2), 2)
    except ValueError:
        return "Введено неверное значение"
    except ZeroDivisionError:
        return "Ошибка деления на ноль"
    return result

print(div(input("Введите первое чиcло: "), input("Введите второе число: ")))