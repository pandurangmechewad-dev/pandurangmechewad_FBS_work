#Write a program to convert days into years, weeks and days.

# Program to convert days into years, weeks and days

# Taking input from user
total_days = int(input("Enter number of days: "))

# Calculations
years = total_days // 365
remaining_days = total_days % 365

weeks = remaining_days // 7
days = remaining_days % 7

# Output
print("Years:", years)
print("Weeks:", weeks)
print("Days:", days)
