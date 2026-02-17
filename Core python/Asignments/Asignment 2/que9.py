#9. Write a program to swap two numbers without using third variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping without third variable
a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)
