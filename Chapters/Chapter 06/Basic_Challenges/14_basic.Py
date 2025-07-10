# If year is leap year (basic logic only)
year = int(input("Enter the year:"))
if year % 4 == 0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")
""" Let me tell you what logic i used on my first attempt:
year = int(input("How many days are in this year:"))
if year == 366
    print("leap year")
else:
    print("not a leap year")
surely, this is not the most efficient way to check if a year is a leap year.
A leap year is divisible by 4 but i tried on my own that make it fun.
Although the code is wrong but not entirely it get the work done
but not as expected."""
