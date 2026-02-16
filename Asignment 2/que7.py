#7. Find the sum of three-digit number.

num = int(input("Enter a three-digit number: "))

# Extract digits
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10

# Calculate sum
sum_of_digits = digit1 + digit2 + digit3
print("Sum of digits =", sum_of_digits)
