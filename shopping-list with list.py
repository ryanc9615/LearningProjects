# Shopping List Manager using a List
shopping_list = []

# Function to add an item to the list
def add_item(shopping_list, item, quantity):
    for entry in shopping_list:
        if entry["item"] == item:
            entry["quantity"] += quantity
            print(f"Updated quantity of '{item}' to {entry['quantity']}.")
            return
    shopping_list.append({"item": item, "quantity": quantity})
    print(f"Item '{item}' added successfully!")

# Function to remove an item from the list
def remove_item(shopping_list, item):
    for entry in shopping_list:
        if entry["item"] == item:
            shopping_list.remove(entry)
            print(f"Item '{item}' removed successfully!")
            return
    print(f"Item '{item}' not found in the shopping list.")

# Function to update the quantity of an item
def update_quantity(shopping_list, item, quantity):
    for entry in shopping_list:
        if entry["item"] == item:
            entry["quantity"] = quantity
            print(f"Quantity of '{item}' updated to {quantity}.")
            return
    print(f"Item '{item}' not found in the shopping list.")

# Function to display the sorted shopping list
def display_sorted_list(shopping_list):
    print("\nShopping List (Sorted Alphabetically):")
    for entry in sorted(shopping_list, key=lambda x: x["item"]):
        print(f"- {entry['item']}: {entry['quantity']}")

# Function to search for an item in the list
def search_item(shopping_list, item):
    for entry in shopping_list:
        if entry["item"] == item:
            print(f"Item found: {entry['item']}, Quantity: {entry['quantity']}")
            return
    print(f"Item '{item}' not found in the shopping list.")

# Function to display the summary of the list
def display_summary(shopping_list):
    total_items = len(shopping_list)
    total_quantity = sum(entry["quantity"] for entry in shopping_list)
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
