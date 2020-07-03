my_list = [26, 3.14, "name", True, [2, "b", 7], ("a", 5, "c"),
           {1: "jan", 2: "feb", 3: "mar"}, {1, 4, 8}, None]
i = 0
for element in my_list:
    print(f"{i + 1} элемент списка - {my_list[i]} - {type(my_list[i])}")
    i += 1
