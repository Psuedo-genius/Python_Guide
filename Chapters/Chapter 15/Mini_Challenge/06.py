# What’s the base case in factorial recursion?
def countdown(n):
    if n <= 0:       # This two line is the base case
        print("Done")
    else:
        print(n)
        countdown(n - 1)
