while True:
    rate_list = [7, 5, 3, 3, 2]
    rate = int(input("Оцените продукт по шкале от 1 до 10: "))
    for element in range(len(rate_list)):
        if rate == rate_list[element]:
            rate_list.insert(element + rate_list.count(rate), float(rate))
            break
        elif rate < rate_list[element] and rate > rate_list[element + 1]:
            rate_list.insert(element + rate_list.count(rate), rate)
            break
        elif rate > rate_list[0]:
            rate_list.insert(0, rate)
        elif rate < rate_list[-1]:
            rate_list.append(rate)
    print(f"Новый рейтинг {rate_list}")
