# Create a function that accepts any number of arguments.
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add_all(5, 10))          # Output: 15
print(add_all(1, 2, 3, 4, 5))  # Output: 15
