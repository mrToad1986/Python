from random import randint

numbers = ' '.join([str(randint(1, 100)) for i in range(100)])
with open('text_5.txt', 'w+', encoding='utf-8') as my_file:
    my_file.write(numbers)
    my_file.seek(0)
    print(sum(map(int, my_file.readline().split())))
