# 🛠 Debug Challenges (5)

# What's wrong?
text = "Hello"
# text[0] = "Y"     'str' object does not support item assignment
text = "Y" + text[1:]
print(text)  # Yello
# Strings are immutable in Python. You can't change them directly
# instead, rebuild them.


# This doesn't remove all spaces:
msg = " hello "
print(msg.strip(" "))
# strip(" ") removes only leading and trailing spaces,not spaces in the middle.
# Want to remove all spaces? Use:
# print(msg.replace(" ", ""))

# Why is this giving error?
word = "test"
print(word[3])  # Becuase the last indices of the variable word is 3.

# Fix:
name = "John"
print(name.lower()[0])

# Output of:
print("hello".find("z"))
# find() returns the index of the first match.
# If not found, it returns -1 — not nothing or error.
