# Shopping List Manager
shopping_list = {}

# Function to add an item to the list
def add_item(shopping_list, item, quantity):
    if item in shopping_list:
        shopping_list[item] += quantity
    else:
        shopping_list[item] = quantity
    print(f"Item '{item}' added successfully!")

# Function to remove an item from the list
def remove_item(shopping_list, item):
    if item in shopping_list:
        del shopping_list[item]
        print(f"Item '{item}' removed successfully!")
    else:
        print(f"Item '{item}' not found in the shopping list.")

# Function to update the quantity of an item
def update_quantity(shopping_list, item, quantity):
    if item in shopping_list:
        shopping_list[item] = quantity
        print(f"Quantity of '{item}' updated to {quantity}.")
    else:
        print(f"Item '{item}' not found in the shopping list.")

# Function to display the sorted shopping list
def display_sorted_list(shopping_list):
    print("\nShopping List (Sorted Alphabetically):")
    for item, quantity in sorted(shopping_list.items()):
        print(f"- {item}: {quantity}")

# Function to search for an item in the list
def search_item(shopping_list, item):
    if item in shopping_list:
        print(f"Item found: {item}, Quantity: {shopping_list[item]}")
    else:
        print(f"Item '{item}' not found in the shopping list.")

# Function to display the summary of the list
def display_summary(shopping_list):
    total_items = len(shopping_list)
    total_quantity = sum(shopping_list.values())
    print("\nShopping List Summary:")
    print(f"Total Unique Items: {total_items}")
    print(f"Total Quantity of Items: {total_quantity}")

# Main program loop
def main():
    print("Welcome to the Shopping List Manager!")
    print("""
    1. Add Item
    2. Remove Item
    3. Update Quantity
    4. Display Sorted List
    5. Search for Item
    6. Display Summary
    7. Exit
    """)

    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            item = input("Enter item name: ").lower()
            quantity = int(input("Enter quantity: "))
            add_item(shopping_list, item, quantity)
        
        elif choice == 2:
            item = input("Enter item name to remove: ").lower()
            remove_item(shopping_list, item)
        
        elif choice == 3:
            item = input("Enter item name to update: ").lower()
            quantity = int(input("Enter new quantity: "))
            update_quantity(shopping_list, item, quantity)
        
        elif choice == 4:
            display_sorted_list(shopping_list)
        
        elif choice == 5:
            item = input("Enter item name to search: ").lower()
            search_item(shopping_list, item)
        
        elif choice == 6:
            display_summary(shopping_list)
        
        elif choice == 7:
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

main()
