year = {"Зима":(12, 1, 2), "Весна":(3, 4, 5),
        "Лето":(6, 7, 8), "Осень":(9, 10, 11)}
while True:
    month = int(input("Введите номер месяца: "))
    for key in year.keys():
        if month in year[key]:
            print (f"Время года - {key}")