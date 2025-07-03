beverages = set(["coffee", "tea", "juice"])
print(beverages)

beverages.add("water")
beverages.add("soda")
print(beverages)

appliances = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in appliances)  

appliances.remove("kettle")
print(appliances)

for item in appliances:
    print(item)

my_set = {"apple", "banana", "orange", "grape"}
my_list = ["pear", "kiwi"]
my_set.update(my_list)
print(my_set)

ages = {25, 30}
names = {"John", "Jane"}
combined = ages.union(names)
print(combined)