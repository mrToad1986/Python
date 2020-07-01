revenue = float(input("Ваша выручка составила: "))
cost = float(input("Ваши издержки составили: "))
staff = int(input("Сколько человек на вас работает: "))
profit = revenue - cost
if profit > 0:
    efficiency = (profit / revenue) * 100
    avg_sallary = profit / staff
    print(f"Прибыль вашей компании составила {profit:.2f} рублей.")
    print(f"Рентабельность выручки {efficiency:.2f} процентов.")
    print(f"Прибыль в расчете на одного сотрудника {avg_sallary:.2f} рублей.")
elif profit == 0:
    print("Ваша компания работает в ноль.")
elif profit < 0:
    print(f"Убыток от вашей деятельности составил {profit:.2f} рублей.")
