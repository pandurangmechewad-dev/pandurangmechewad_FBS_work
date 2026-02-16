#3. Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

# Total inches
total_inches = feet * 12 + inches

# Convert to meter and centimeter
meter = total_inches * 0.0254
centimeter = total_inches * 2.54

print("Meter =", meter)
print("Centimeter =", centimeter)
