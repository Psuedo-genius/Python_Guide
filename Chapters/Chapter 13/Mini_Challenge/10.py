# What’s the difference between `.remove()` and `.discard()`?
'''
| Method        | If element **exists** | If element **does NOT exist** |
| ------------- | --------------------- | ----------------------------- |
| `.remove(x)`  | Removes `x`           |  **Raises `KeyError`**       |
| `.discard(x)` | Removes `x`           |  **Does nothing (no error)** |
'''
s = {1, 2, 3}

s.remove(2)     # Removes 2 → OK
s.discard(3)    # Removes 3 → OK
s.discard(5)    # 5 not in set → No error
s.remove(4)     # KeyError: 4 not found
