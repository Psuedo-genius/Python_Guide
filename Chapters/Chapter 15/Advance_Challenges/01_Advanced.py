# Flatten a nested list using recursion.
def flatten(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat += flatten(item)  # Recursive case
        else:
            flat.append(item)     # Base case
    return flat


nested = [1, [2, [3, 4], 5], 6]
print("Flattened:", flatten(nested))
