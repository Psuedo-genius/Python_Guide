# Reverse a string using slicing
type = "Python"
for char in type[::-1]:
    print(char, end="")
print()
# or
text = "Python"
reversed_text = ""

for i in range(len(text)):
    reversed_text = text[i] + reversed_text

print(reversed_text)
