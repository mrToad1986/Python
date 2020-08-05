import re

result = {}
with open('text_6.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file.readlines():
        result[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
    print(result)
