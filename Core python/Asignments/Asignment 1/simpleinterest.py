#Write a program to enter P, T, R and calculate simple Interest.

P = float(input("Enter Principal amount (P): "))
T = float(input("Enter Time in years (T): "))
R = float(input("Enter Rate of Interest (R): "))

# Calculate Simple Interest
SI = (P * T * R) / 100

# Display result
print("Simple Interest =", SI)
