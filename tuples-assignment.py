def create_tuple(elements):
    return tuple(elements)

def access_elements(tuple_data,index):
    try:
        return tuple_data[index]
    except IndexError:
        return "Error: Index out of range."

def slice_tuple(tuple_data, start, end):
    tuple_data[start:end]

def count_occurrences(tuple_data, element):
    tuple_data.count(element)

def find_index(tuple_data, element):
    if element in tuple_data:
        return tuple_data.index(element)
    else:
        return "Error: Element not found in tuple."
    
def tuple_operations(tuple1, tuple2):
    concatenated = tuple1 + tuple2 
    repeated = tuple1 * 2
    return concatenated, repeated
 
def main():
    print("Welcome to the Tuple Data Processor!")
    
    while True:
        print("\nMenu:")
        print("1. Create Tuple")
        print("2. Access Element by Index")
        print("3. Slice Tuple")
        print("4. Count Occurrences of an Element")
        print("5. Find Index of an Element")
        print("6. Perform Tuple Operations")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            elements = input("Enter elements separated by spaces: ").split()
            my_tuple = create_tuple(elements)
            print(f"Tuple created successfully: {my_tuple}")

        elif choice == '2':
            index = int(input("Enter index: "))
            print(f"Element at index {index}: {access_element(my_tuple, index)}")

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(f"Sliced Tuple: {slice_tuple(my_tuple, start, end)}")

        elif choice == '4':
            element = input("Enter element to count: ")
            print(f"Element '{element}' occurs {count_occurrences(my_tuple, element)} time(s).")

        elif choice == '5':
            element = input("Enter element to find: ")
            print(find_index(my_tuple, element))

        elif choice == '6':
            tuple1 = tuple(input("Enter first tuple elements separated by spaces: ").split())
            tuple2 = tuple(input("Enter second tuple elements separated by spaces: ").split())
            concatenated, repeated = tuple_operations(tuple1, tuple2)
            print(f"Concatenated Tuple: {concatenated}")
            print(f"Repeated Tuple: {repeated}")

        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()