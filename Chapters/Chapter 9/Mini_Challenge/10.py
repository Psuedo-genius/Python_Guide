# Fix the bug: `text = "Hi"`; `text[0] = "h"`
# Output: TypeError: 'str' object does not support item assignmen
# String is immutable instead we have to do is
text = "Hi"
new_text = "h" + text[1:]
print(new_text)  # hi
