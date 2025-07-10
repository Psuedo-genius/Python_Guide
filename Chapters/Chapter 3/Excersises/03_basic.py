# Ask for name and age, then use `.format()` to print
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello, {}! You are {} years old.".format(name, age))
'''By the way you dont need to use the format function very often in Python.
It's more efficient to use it when you
want to insert multiple variables into a string.
In this case, we could've simply written: print(f"Hello, {NAME}! You are{age}
year old. or we could have used commas(,)in it '''
