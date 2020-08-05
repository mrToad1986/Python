line_count = 0
with open('my_text.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        line_count += 1
        line_words = len(line.split())
        print(f'Слов в {line_count}-й строке: {line_words} ')
    print(f'Всего строк в файле {line_count}')
