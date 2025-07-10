# Debug Challenges (5)

# Unhashable type error

bad_set = {(1, 2), (3, 4)}
# ✅ Fix: Use tuples instead: {(1, 2), (3, 4)}


# Removing missing item with `.remove()`

items = {"pen", "pencil"}
items.discard("eraser")
# ✅ Fix: Use .discard("eraser") or check before removing


# Wrong set comparison

a = {1, 2, 3}
b = {3, 2, 1}
print(a == b)  # ✅ Output: True
# ⚠️ Explanation: Sets are unordered; order doesn’t matter

# Empty set declaration

empty = {}        # ❌ This creates a dict, not a set!
print(type(empty))  # Output: <class 'dict'>
# ✅ Fix: Use set() to create an empty set

# Misuse of indexing

myset = {"a", "b", "c"}
print(myset[0])  # ❌ TypeError: 'set' object is not subscriptable
# ✅ Fix: Convert to list: list(myset)[0]
