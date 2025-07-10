# Group names by first letter using `defaultdict`.
'''
🧠 Algorithm (Step-by-Step):
Import defaultdict from the collections module.

Create a defaultdict with list as the default type.

Loop through each name in the list.

Get the first letter of each name (e.g., name[0]).

Append the name to the corresponding list in the dictionary.

After the loop, print or return the dictionary.
'''

from collections import defaultdict
names = ['Alice', 'Bob', 'Ankit', 'Bella', 'Charlie']
group = defaultdict(list)
for name in names:
    first_letter = name[0].upper()  # You can also use .lower() for uniformity
    group[first_letter].append(name)  # this will make the dict
for letter, name_list in group.items():
    print(f"{letter}: {name_list}")
