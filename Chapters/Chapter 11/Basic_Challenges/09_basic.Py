# Try modifying a tuple and handle the error
t = 423, 25, 542

try:
    t[0] = 999
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable — you cannot change their elements.")
