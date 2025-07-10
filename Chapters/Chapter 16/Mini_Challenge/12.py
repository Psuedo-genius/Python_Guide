# Use `filter()` to keep even numbers.
nums = [1, 2, 3, 4, 5, 6]

# Use lambda to define the even condition
evens = list(filter(lambda x: x % 2 == 0, nums))

print("Even numbers:", evens)
