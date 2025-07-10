# Implement recursive binary search.
# Its too hard for you fools!!!!!!!!!! learn some data structure and come again
def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Target found at index mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # Search left half
    else:
        return binary_search(arr, target, mid + 1, high)  # Search right half


arr = sorted(list(map(int, input("Enter sorted list: ").split())))
target = int(input("Enter target number: "))

index = binary_search(arr, target)
if index != -1:
    print(f"Target found at index: {index}")
else:
    print("Target not found.")
