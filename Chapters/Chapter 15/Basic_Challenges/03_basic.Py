# Write a function that calculates factorial using recursion.
"""
Goal:
fact = n*(n-1)*(n-2)*...*(1)
"""


def fact(n):
    if n <= 0:
        return 1
    else:
        return n*fact(n-1)


n = int(input("Enter a number: "))
print(f"The factorial of the {n} is {fact(n)}")
