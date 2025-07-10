# Reverse a dictionary (values become keys).
marks = {'Maths': 99, 'English': 78, 'Physics': 79, 'Chemisty': 67}
inv = {v: k for k, v in marks.items()}
print(inv)
'''
| Part              | Meaning                           |
| ----------------- | --------------------------------- |
| `marks.items()`   | Gives pairs like `('Alice', 85)`  |
| `for k, v in ...` | Loops over each (key, value) pair |
| `{v: k ...}`      | Swaps value and key               |
| `inv = {...}`     | Creates a new dictionary          |

'''
