Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])  

Shoes["brand"] = "Adidas"
print(Shoes)

Shoes["type"] = "sneakers"
print(Shoes)

print(list(Shoes.keys()))

print(list(Shoes.values()))

print("size" in Shoes)  

for key, value in Shoes.items():
    print(key, ":", value)

del Shoes["color"]
print(Shoes)

Shoes.clear()
print(Shoes)  

my_dict = {"name": "Ricky", "age": 30}
dict_copy = my_dict.copy()
print(dict_copy)

nested_dict = {
    "person1": {
        "name": "Suzan",
        "age": 25
    },
    "person2": {
        "name": "Hallie",
        "age": 30
    }
}
print(nested_dict)