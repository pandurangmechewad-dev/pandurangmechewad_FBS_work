#Write a Program to input two angles from user and find third angle of the tringle
# Input two angles from user
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))

# Calculate third angle
third_angle = 180 - (angle1 + angle2)

# Check if triangle is valid
if third_angle > 0:
    print("Third angle of the triangle is:", third_angle)
else:
    print("Invalid angles! Triangle not possible.")
