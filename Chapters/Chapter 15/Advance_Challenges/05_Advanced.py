# Count how many times a value appears in a nested structure.
def count_occurrences(data, target):
    count = 0
    for item in data:
        if isinstance(item, list):
            count += count_occurrences(item, target)  # 🔁 Recursive call
        elif item == target:
            count += 1  # ✅ Found match
    return count


nested_list = [1, [2, 3, [1, 1]], 4, [5, [1, 6]]]
target = 1
print("Count of", target, "is:", count_occurrences(nested_list, target))
