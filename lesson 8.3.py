class Exception:
    def __init__(self):
        self.my_list = []

    def num_input(self):

        while True:
            num = input('Введите числовое значение. Для выхода напишите "Stop": ')
            try:
                num = int(num)
                self.my_list.append(num)
            except:
                if num == 'Stop':
                    return f'Завершение работы.\nСформирован список: {self.my_list}'
                else:
                    print('Введено недопустимое значение. Попробуйте еще раз.')


my_exception = Exception()
print(my_exception.num_input())
