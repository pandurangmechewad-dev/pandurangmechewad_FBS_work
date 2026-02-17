# Compound Interest 

# Taking input from user
P = float(input("Enter Principal amount (P): "))
R = float(input("Enter Rate of Interest (R): "))
T = float(input("Enter Time in years (T): "))

# Calculating Compound Interest
Amount = P * (1 + R/100) ** T
CI = Amount - P

# Display result
print("Compound Interest =", CI)
print("Total Amount =", Amount)
