#5. WAP to calculate selling price of book based on cost price and discount.

cp = float(input("Enter cost price: "))
d = float(input("Enter discount (%): "))

sp = cp - (cp * d / 100)

print("Selling Price =", sp)
