# Create a function that accepts `*args` and returns their sum.
def sum_all(*args):
    return sum(args)


n = int(input("number"))
n2 = int(input("number"))
n3 = int(input("number"))
n4 = int(input("number"))
# Example usage:
print("Sum is:", sum_all(n, n2, n3, n4))      # ➝ 10
print("Sum is:", sum_all(10, 20, 30))     # ➝ 60
print("Sum is:", sum_all())               # ➝ 0 (no input, sum is zero)
# or


def sum_all(*args):
    return sum(args)


# Take a list of numbers from the user in one line
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Use *nums to unpack the list into individual arguments
print("Sum is:", sum_all(*nums))
