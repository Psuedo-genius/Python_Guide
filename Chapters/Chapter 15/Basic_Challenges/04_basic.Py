# Reverse a list recursively.
def reverse_list(lst):
    if len(lst) == 0:
        return []
    return reverse_list(lst[1:]) + [lst[0]]


print(reverse_list([1, 2, 3, 4]))  # ➝ [4, 3, 2, 1]
