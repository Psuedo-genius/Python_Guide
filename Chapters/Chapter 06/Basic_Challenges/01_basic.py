# Check if a number is even or odd
no1 = int(input("Enter the  number: "))
if no1 % 2 == 0:
    print(f"{no1} is an even number.")
elif no1 == 0:
    print(f"{no1} is zero.")
else:
    print(f"{no1} is an odd number.")
