# What's the difference between append() and extend()?
# ✅ append() – Adds a single object
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

#  extend() – Adds each element of the iterable separately
# extend() adds each item inside the given list to the original list.
fruits = ["apple", "banana"]
fruits.extend(["mango", "grape"])
print(fruits)
