num_one = int(input("Please enter a number: "))
num_two = int(input("Please enter another number: "))

print(num_one + num_two)
print(num_one - num_two)
print(num_one * num_two)
try:
    result = num_one / num_two
    print(result)
except ZeroDivisionError:
    print("Error. Division by zero not allowed.")

if num_one > num_two:
    print("First number is greater.")
elif num_two > num_one:
    print("Second number is greater.")
else:
    print("Both numbers are equal.")