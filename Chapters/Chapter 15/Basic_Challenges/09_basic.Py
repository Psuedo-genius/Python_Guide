# Find the minimum in a list using recursion.
def find_min(lst, index=0):
    if index == len(lst) - 1:
        return lst[index]
    min_rest = find_min(lst, index + 1)
    return lst[index] if lst[index] < min_rest else min_rest


lst = list(map(int, input("Enter list of numbers: ").split()))
print("Minimum value is:", find_min(lst))
