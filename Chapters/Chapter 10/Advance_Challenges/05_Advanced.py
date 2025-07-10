# From a list of names, print only the ones starting with vowels
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fatima", "George"]
vowels = ('A', 'E', 'I', 'O', 'U')
found = False
for name in names:
    if name.startswith(vowels):
        print(name)
        found = True
    if not found:
        print("No name starts with vowles")
