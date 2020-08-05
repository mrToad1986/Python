my_file = open('my_text.txt', 'w', encoding='utf-8')
print('Введите строку для записи в файл.\nДля выхода введите пустую строку.')
while True:
    line = input('Введите следующую строку: ')
    try:
        if line == '':
            break
        else:
            my_file.write(line + '\n')
    except IOError:
        break
my_file.close()
