#Program to find quotient and remainder of two numbers.
# Input two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Check division by zero
if num2 == 0:
    print("Division by zero is not allowed.")
else:
    quotient = num1 // num2
    remainder = num1 % num2

    print("Quotient:", quotient)
    print("Remainder:", remainder)