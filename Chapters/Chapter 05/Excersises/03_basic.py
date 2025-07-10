# Use not  to check if a condition is False
no1 = int(input("Enter frist number:"))
no2 = int(input("Enter second number:"))
result = no1 > no2
if (result is False):
    print(f"The condition {no1} > {no2} is {not result}")
else:
    print(f"The condition {no1} > {no2} is {result}")
