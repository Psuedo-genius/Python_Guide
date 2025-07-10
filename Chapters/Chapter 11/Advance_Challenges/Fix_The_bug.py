# Debug Challenges

# Fix:
x = (5,)
print(type(x))  # ❌ Not a tuple

# What happens here?

a = (1, 2)
a[0] = 99
# Tuples are immutable — this raises a `TypeError`.


# Predict the Output:

x = (1, [2, 3])
x[1].append(4)
print(x)
# List inside tuple can still be changed`: `(1, [2, 3, 4])`
