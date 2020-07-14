from sys import argv


def income():
    try:
        time = int(argv[1])
        rate = int(argv[2])
        bonus = int(argv[3])
        salary = time * rate + bonus
        print(f'Ваш доход составляет: {salary}')
    except:
        print('Введены неверные значения')


income()
