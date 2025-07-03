phones = ("samsung", "iphone", "tecno", "redmi")
print(phones[1])  

print(phones[-2])  

phones_list = list(phones)
phones_list[1] = "itel"
phones = tuple(phones_list)
print(phones)  

phones_list = list(phones)
phones_list.append("Huawei")
phones = tuple(phones_list)
print(phones)

for phone in phones:
    print(phone)

    phones_list = list(phones)
del phones_list[0]
phones = tuple(phones_list)
print(phones)

uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print(uganda_cities)

city1, city2, city3, city4, city5 = uganda_cities
print(city1, city2, city3, city4, city5)

print(uganda_cities[1:4])  

first_names = ("John", "Jane")
last_names = ("Doe", "Smith")
full_names = first_names + last_names
print(full_names)

colors = ("red", "green", "blue")
print(colors * 3)

numbers = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(numbers.count(8))  

