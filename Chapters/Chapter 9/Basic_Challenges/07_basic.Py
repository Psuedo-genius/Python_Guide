# Get the last 3 characters of a string
user = input("Enter your string: ")
length = len(user)

if length >= 3:
    print(user[length - 3: length])  # From (length - 3) to end
else:
    print("String is too short!")

# or u can use simple negative inicing
user = input("Enter your string: ")
print(user[-3:])

"""
🧨 What About Negative Indexes?

In Python, negative indexes count from the end of the string.
Index	Character	Explanation
0	'H'	First character
-1	'd'	Last character
-2	'l'	Second last
-3	'r'	Third last

So negative slicing means:

string[-3:]  → from 3rd-last to end
string[:-2]  → from start to 2nd-last (excluding 2nd-last and after)

🔁 Examples:
Example 1:

text = "HelloWorld"
print(text[-3:])      # Output: "rld"

Why?

    -3 points to 'r'

    : means "go to the end"

    So we get 'r' + 'l' + 'd' = 'rld'

Example 2:

text = "HelloWorld"
print(text[:-3])      # Output: "HelloWo"

Why?

    :-3 means from the start up to 3rd-last character (excluding it)

    So 'HelloWo' gets printed

🛠 Common Use Cases
Code	Meaning
s[-1]	Last character
s[-2:]	Last 2 characters
s[:-1]	All characters except the last
s[-5:-2]	From 5th-last up to (but not including) 2nd-last
🧭 Tip to Remember:

    Positive index: starts from left (0, 1, 2, ...)

    Negative index: starts from right (-1, -2, -3, ...)
"""
