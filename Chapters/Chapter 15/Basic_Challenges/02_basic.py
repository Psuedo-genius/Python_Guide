# Create a function to return the sum of digits in a number.
"""
Goal:
sum = n + (n-1) + (n-2) + ... + 1
"""


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)


n = int(input("Enter a number: "))
print("Sum of digits is:", sum_of_digits(n))
