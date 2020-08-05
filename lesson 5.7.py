import json

with open('text_77.json', 'w', encoding='utf-8') as data_file:
    with open('text_7.txt', 'r', encoding='utf-8') as my_file:
        my_dict = {}
        avg_profit = {}
        tot_sum, number = 0, 0
        line = my_file.read().split('\n')
        for item in line:
            item = item.split()
            # print(item)
            profit = int(item[2]) - int(item[3])
            print(profit)
            my_dict[item[0]] = profit
            print(my_dict)
            if profit >= 0:
                tot_sum += profit
                number += 1
            avg_profit['average profit'] = tot_sum / number
        all_list = [my_dict, avg_profit]
    json.dump(all_list, data_file, ensure_ascii=False, indent=4)
print(f'All inf:\n{line}\n\nTotal list:\n{all_list}')
