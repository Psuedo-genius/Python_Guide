# Write a function that takes a tuple of numbers and
# returns a new tuple containing the minimum, maximum, and average
def tup():
    t = tuple(map(int, input("Enter values separated by space: ").split()))
    if not t:
        return ("none", 'none', 'none')
    mini = min(t)
    maxi = max(t)
    average = sum(t) / len(t)
    return (mini, maxi, average)


print(tup())
# No need to make a funtions its just to lets you prepare for future
