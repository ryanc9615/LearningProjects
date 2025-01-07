def add(a,b):
    return a + b
def subtract(a,b):
    return a - b 
def multiply(a,b):
    return a * b
def division(a,b):
    if b == 0: 
        print("Unable to divide by zero.")
    return a/b

def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    calculation = input("Which function would you like to perform (addition, subtraction, multiplication, division): ").lower()
    if calculation == "addition":
        result = add(a,b)
        print(result)
    elif calculation == "subtraction":
        result = subtract(a,b)
        print(result)
    elif calculation == "multiplication":
        result = multiply(a,b)
        print(result)
    elif calculation == "division":
        result = division(a,b)
        print(result)
    else:
        print("Incorrect, please try again.")

main()
