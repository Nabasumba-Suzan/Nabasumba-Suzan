
inventory = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 30,
    "Monitor": 20,
    "Headphones": 50
}

def display_inventory():
    print("\nCurrent Inventory:")
    print("-----------------")
    print("{:<15} {:<10}".format("Item", "Quantity"))
    for item, quantity in inventory.items():
        print("{:<15} {:<10}".format(item, quantity))

def update_inventory():
    while True:
        display_inventory()
        print("\nUpdate Inventory Options:")
        print("1. Add New Item")
        print("2. Modify Item Quantity")
        print("3. Remove Item")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            
            item = input("Enter new item name: ").strip().title()
            if item in inventory:
                print(f"{item} already exists in inventory.")
                continue
                
            try:
                quantity = int(input(f"Enter quantity for {item}: "))
                inventory[item] = quantity
                print(f"{item} added with quantity {quantity}.")
            except ValueError:
                print("Invalid input. Quantity must be a number.")
                
        elif choice == '2':
            
            item = input("Enter item name to modify: ").strip().title()
            if item not in inventory:
                print(f"{item} not found in inventory.")
                continue
                
            try:
                new_quantity = int(input(f"Enter new quantity for {item} (current: {inventory[item]}): "))
                inventory[item] = new_quantity
                print(f"{item} quantity updated to {new_quantity}.")
            except ValueError:
                print("Invalid input. Quantity must be a number.")
                
        elif choice == '3':
            
            item = input("Enter item name to remove: ").strip().title()
            if item not in inventory:
                print(f"{item} not found in inventory.")
                continue
                
            confirm = input(f"Are you sure you want to remove {item}? (y/n): ").lower()
            if confirm == 'y':
                del inventory[item]
                print(f"{item} removed from inventory.")
                
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def main_menu():
    while True:
        print("\nInventory Management System")
        print("1. Display Inventory")
        print("2. Update Inventory")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            display_inventory()
        elif choice == '2':
            update_inventory()
        elif choice == '3':
            print("Exiting Inventory Management System")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main_menu()
