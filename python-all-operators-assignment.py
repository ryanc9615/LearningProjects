# User Input
employee_name = input("Enter employees name: ")
employee_age = int(input("Enter employees age: "))
hourly_wage = int(input("Enter hourly wage: "))
hours_worked = int(input("Enter hours worked: "))

# Arithmetic Operators
gross_pay = hourly_wage * hours_worked
overtime_pay = 0

# Comparison Operators
if hours_worked > 40:
    overtime_pay = (hours_worked - 40) * (hourly_wage * 1.5)
if employee_age >= 60: 
    print("Eligible for retirement benefits.")

# Logical Operators
if hours_worked > 40 and hourly_wage > 20: 
    print("High earner with overtime.")

# Assignment Operators
gross_pay += overtime_pay

# Identity Operators
if employee_name == "John Doe":
    print("Exact Match with stored name.")

# Membership Operators
if "a" in employee_name: 
    print("The name contains letter 'a'")

# Bitwise Operators
shifted_age = employee_age >> 1
print(f"Age after right shift: {shifted_age}")

print(f"Gross Pay: ${gross_pay}")
print(f"Overtime Pay: ${overtime_pay}") 

