# Write a function that calls another function inside.
def sum_all(*args):
    return sum(args)


def find_max():
    num = list(map(int, input("Enter the list of numbers: ").split()))
    # Call sum_all and use its result
    total = sum_all(*num)
    print("Sum of all elements:", total)  # You can choose to return it too
    return max(num)


# Call the function and print the result
print("Maximum element is:", find_max())
