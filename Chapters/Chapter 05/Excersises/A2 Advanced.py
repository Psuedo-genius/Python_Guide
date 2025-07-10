# Use all three logical operators in one if condition
no1 = int(input("Enter the first number: "))
no2 = int(input("Enter the second number: "))
no3 = int(input("Enter the third number: "))
result = not (no1 < 40 or no2 < 20 and no3 < 10)
print(result)
