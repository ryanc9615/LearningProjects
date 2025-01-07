product_details = {}

while True:
    product_name = input("Enter product name (or done to finish): ")

    if product_name.lower() == "done":
        break
    
    try:
        product_price = float(input("Enter price: "))
        product_details[product_name] = product_price
    except ValueError:
        print("Invalid Price. Please enter a numeric value.")
    
total = sum(product_details.values())

print(f"Total cost of all items ${total}")

