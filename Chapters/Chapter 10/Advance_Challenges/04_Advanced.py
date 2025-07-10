# Flatten a nested list of integers into a single list
list1 = [243, 24, [243, 2423], 524, 56753, ]
flattened = []
for item in list1:
    if isinstance(item, list):
        flattened.extend(item)  # add elements from inner list
    else:
        flattened.append(item)  # add normal element

print(flattened)

# 🧠 Explanation:
'''
    isinstance(item, list) checks if the current item is a sublist.

    .extend() adds elements inside the list.

    .append() adds a single item as-is.'''
