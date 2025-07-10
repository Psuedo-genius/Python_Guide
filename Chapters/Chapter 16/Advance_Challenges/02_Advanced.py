# Use `filter()` to remove empty strings.
items = ["apple", "", "banana", "", "cherry", ""]

# Remove empty strings
non_empty = list(filter(lambda x: x != "", items))

print("Filtered list:", non_empty)
