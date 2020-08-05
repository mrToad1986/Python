with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    sal_low = []
    sal_sum = []
    content = my_file.read().split('\n')
    for line in content:
        line = line.split()
        sal_sum.append(float(line[1]))
        if float(line[1]) < 20000:
            sal_low.append((line[0]))
print(f'Средняя зарплата составляет: {sum(sal_sum) / len(sal_sum)}')
print('Список сотрудников с зарплатой менне 20 000: ')
for name in range(len(sal_low)):
    print(sal_low[name])
