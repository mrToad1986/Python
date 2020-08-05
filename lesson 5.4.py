eng_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('new_text.txt', 'w', encoding='utf-8') as new_file:
    with open('text_4.txt', 'r', encoding='utf-8') as my_file:
        line = my_file.read().split('\n')
        for word in line:
            word = word.split(' - ')
            new_file.writelines(eng_rus[word[0]] + ' - ' + word[1] + '\n')