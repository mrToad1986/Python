goods = []
features = {'название': '', 'цена': '', 'количество': '', 'ед.изм': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'ед.изм': []}
n = 0
while True:
    if input('Для продолжения работы нажмите "Enter", для выхода "Q": ').upper == "Q":
        break
    n += 1
    for feature in features.keys():
        inp = input(f'Введите значение свойства "{feature}": ')
        features[feature] = int(inp) if (feature == 'цена'or feature == 'количество') else inp
        analytics[feature].append(features[feature])
    goods.append((n, features))
    print(f'\n Текущая аналитика по товарам: \n {"*"*30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print('*'*30)