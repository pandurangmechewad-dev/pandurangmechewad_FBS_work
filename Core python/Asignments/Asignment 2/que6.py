#6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

basic = float(input("Enter Basic Salary: "))

da = basic * 10 / 100
ta = basic * 12 / 100
hra = basic * 15 / 100

total = basic + da + ta + hra

print("\nSalary Details")
print("Basic Salary :", basic)
print("DA (10%)     :", da)
print("TA (12%)     :", ta)
print("HRA (15%)    :", hra)
print("Total Salary :", total)
