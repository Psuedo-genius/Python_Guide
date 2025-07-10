#  Create a function that checks if a number is even.
num = int(input("a number"))


def is_even(num):
    if num % 2 == 0:
        return "Even number"
    else:
        return "Odd number"


# Get input
num = int(input("Enter a number: "))
result = is_even(num)
print(result)
