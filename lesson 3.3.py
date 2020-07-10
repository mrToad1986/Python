def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    try:
        my_list = sorted(my_list)
        sum = my_list[-1] + my_list[-2]
        return sum
    except:
        "Введены неправильные значения"


print(my_func(2, -4, 6))
