names = [ "Suzan" ,"Joan" ,"Vicky" ,"Ric","Linah"]
print (names[1])

names[0] = "Suzan"
print(names)

names.append("Frank")
print(names)  

names.insert(2, "Bathel")
print(names)  

del names[3]
print(names)  

print(names[-1])  

new_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
print(new_list[2:5])  

countries = ["USA", "Canada", "UK", "Japan", "Australia"]
countries_copy = countries.copy()
print(countries_copy)

for country in countries:
    print(country)

    animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]
ascending = sorted(animals)
descending = sorted(animals, reverse=True)
print("Ascending:", ascending)
print("Descending:", descending)

animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
print(animals_with_a)

first_names = ["John", "Jane"]
last_names = ["Doe", "Smith"]
full_names = first_names + last_names
print(full_names)





