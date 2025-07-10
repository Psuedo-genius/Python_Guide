# What does `continue` do?
# A: It skips the current iteration of the loop and moves to the next one.
# Example:
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Output: 1, 3, 5, 7, 9
