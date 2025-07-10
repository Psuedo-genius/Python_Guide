# Debug Challenges
def add(a, b):
    return a + b
# Fix this colon was mising


def f(x=2, y=3):
    return x + y
# What's wrong? There is no value for the y variable


def show():
    print(message)


message = "Hi"
show()
# Will this work? Why?**
# yes Python can access global variables inside
# functions as long as you're only reading them.
# exmaple 4
x = 3


def fx():
    global x
    x += 1


print(x)
# What will print Output 3


# Example 5
def print_twice(msg):
    print(msg)
    print(msg)
# Indentation fix? done
