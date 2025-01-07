def add(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b 
def division(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return (a/b)

def main():
    a = float(input("Please enter the first number: "))
    b = float(input("Please enter the second number (not zero): "))
    math_operation = input("Please choose which math operation you would like to run: addition, subtraction, multiplication, division: ").lower()
    if math_operation == "addition":
        result = add(a,b)
        print(f"The result of the addition is {result}")
    if math_operation == "subtraction":
        result = subtraction(a,b)
        print(f"The result of the subtraction is {result}")
    if math_operation == "multiplication":
        result = multiplication(a,b)
        print(f"The result of the multiplication is {result}")
    if math_operation == "division":
        result = division(a,b)
        print(f"The result of the division is {result}")

main()