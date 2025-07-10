# What does `.strip()` do?
# Removes whitespace from ends
text = "   Hello, world!   "
print(text.strip())    # → "Hello, world!"
print(text.lstrip())   # → "Hello, world!   " (left only)
print(text.rstrip())   # → "   Hello, world!" (right only)
