#Write a program to calculate the percentage of student based on marks of any 5 subjects

## Taking input from user

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))
 
# Calculating total marks
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculating percentage
percentage = (total / 500) * 100   # assuming each subject is out of 100

# Display result
print("Total Marks =", total)
print("Percentage =", percentage, "%")