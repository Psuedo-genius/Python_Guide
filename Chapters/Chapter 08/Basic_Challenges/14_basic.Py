# Loop to print digits of a number in reverse
num = int(input("Enter the number"))
while num > 0:
    digit = num % 10
    print(digit, end=" ")
    num //= 10
