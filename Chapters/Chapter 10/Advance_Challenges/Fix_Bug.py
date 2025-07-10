# 🔧 Debug Challenges (5)

# Fix:

fruits = ["apple", "banana"]  # apple index = 0 and banana = 1
fruits[1] = "kiwi"
print(fruits)

# Fix:

x = [1, 2, 3]
y = x  # y is not a new list; it’s the same object as x
y.append(4)
print(x)


# What is the output?

x = [1, 2, 3]
y = x.copy()
y.append(4)
print(x)  # Output [1, 2, 3,]

# Fix:

lst = [1, 2, 3]   # 1 index = 0 2 index = 1 and 3 index = 2
print(lst[2])
