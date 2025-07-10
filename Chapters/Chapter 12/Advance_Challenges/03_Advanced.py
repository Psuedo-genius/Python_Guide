# Parse key-value pairs from a CSV-like line (e.g., `"name=Ali,age=20"`).
"""
Great task! You're being asked to parse a string that looks like this:
"name=Ali,age=20"
Into a dictionary:

{'name': 'Ali', 'age': '20'}
Let’s walk through it with an algorithm and code.

🧠 Algorithm: Parse CSV-like key-value string
Input a string like "name=Ali,age=20".

Split the string by "," → gives a list of key-value strings:
 ["name=Ali", "age=20"].

Create an empty dictionary.

Loop through each item:

Split each item by "=" to get key and value.

Store them in the dictionary.

Print or return the dictionary.
"""
data = "name=Ali,age=20"

# Step 2: Split into parts
pairs = data.split(',')

# Step 3: Create dictionary
result = {}

# Step 4: Loop and split each pair
for pair in pairs:
    key, value = pair.split('=')
    result[key] = value

print(result)
