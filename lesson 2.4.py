my_str = input("Пожалуйста, введите строку из нескольких слов: ")
my_list = my_str.split()
i = 0
for words in my_list:
    word = my_list[i][0:10]
    print(f"{i+1}-е слово: {word}")
    i += 1
