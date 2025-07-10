# Write a function that modifies a global counter and returns its new value.
count = 0  # Global variable


def fun():
    global count  # Tell Python we want to use the global variable
    count += 1     # Modify it
    print("Inside function, count =", count)


fun()
print("Outside function, count =", count)
