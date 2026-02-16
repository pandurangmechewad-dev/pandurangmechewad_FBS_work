#1. Convert the time entered in hh,min and sec into seconds.

hh = int(input("enter the hours :"))
min = int(input("enter the minutes :"))
sec = int(input("enter the secound :"))

total_secound = (hh * 3600) + (min * 60) + (sec)
print("total secound is :" , total_secound)
