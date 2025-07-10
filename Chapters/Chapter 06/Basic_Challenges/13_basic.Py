# Ask name and print only if it starts with "A"
name = input("Enter your name: ")
if name.startswith("A"):  # its a string method you will learn about in Python
    print("Hello, " + name)
else:
    print("Name does not start with 'A'.")
# or you may use this one
if name[0] == 'A':  # its a string indexing you will learn about in Python
    print("Hello, " + name)
else:
    print("Name does not start with 'A'.")
# The things you havent learned is given just to make you think more.
# So always think about it before seeing the solution.
# Thats if you wanna learn more about Python.
# Or else you can also be a average programmer. copy paste
