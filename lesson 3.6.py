def int_func(text):
    words = text.split()
    up_text = ''
    for i in range(len(words)):
        up_word = words[i][0].upper() + words[i][1:] + ' '
        up_text += up_word
    return up_text
print(int_func('каждое слово в фразе с большой буквы.'))