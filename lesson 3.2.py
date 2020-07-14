def profile (first_name, last_name, dob, city, email, phone):
    return f"Имя: {first_name}; Фамилилия: {last_name}; Дата рождения: {dob}; " \
           f"Город: {city}; Почта: {email}; Телефон: {phone}"
user = profile(first_name="Николай", last_name="Петров", dob="01.01.1970",
               city="Москва", email="npetrov@mail.ru", phone="123-45-67")
print(user)
