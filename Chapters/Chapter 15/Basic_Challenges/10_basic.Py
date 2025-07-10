# Count how many even numbers are in a list recursively.
def count_even(lst, index=0):
    if index == len(lst):
        return 0  # base case: no more elements to check
    is_even = 1 if int(lst[index]) % 2 == 0 else 0
    return is_even + count_even(lst, index + 1)


lst = list(map(int, input("Enter list of numbers: ").split()))
print("Count of even numbers:", count_even(lst))
