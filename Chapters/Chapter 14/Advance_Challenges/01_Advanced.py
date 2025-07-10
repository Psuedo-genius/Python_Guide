# Build a function that takes a list and returns the max element.
def find_max():
    num = list(map(int, input("Enter the list of numbers: ").split()))
    return max(num)


# Call the function and print the result
print("Maximum element is:", find_max())
