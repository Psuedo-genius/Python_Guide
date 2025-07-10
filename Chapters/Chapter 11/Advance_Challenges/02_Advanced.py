# Unpack the tuple `(1, 2, 3, 4, 5)` into three variables:
# first`, `middle` (a list), and `last` using extended unpacking.
t = (1, 2, 3, 4, 5)
first, *middle, last = t
print(first, middle, last, end="       ")
