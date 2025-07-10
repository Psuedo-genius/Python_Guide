# Debug Challenges

# Identify the error:
# This function keeps calling itself infinitely → will crash with:
# RecursionError: maximum recursion depth exceeded
# Fix:
# Add a base case to stop recursion:


def loop(n):
    if n > 10:   # or any stopping condition
        return
    print(n)
    loop(n + 1)


# Fix the missing base case:
# This function keeps was calling itself infinitely → had crash with:
# RecursionError: maximum recursion depth exceeded
# Fix:
# Add a base case to stop recursion:


def hello(n):
    if n == 0:
        return
    print("Hello")
    hello(n - 1)


hello(3)  # prints "Hello" 3 times


# What’s wrong here?
# This function keeps was calling itself infinitely → had crash with:
# RecursionError: maximum recursion depth exceeded
# Fix:
# Add a base case to stop recursion:


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Find the logic error:
# This returns s + reverse(...) → which causes strings to repeat, not reverse.


def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]


# Fix and explain:
# It keeps calling itself with the same list, no element is removed.
# Results in infinite recursion.
# Fix: Remove the head of the list in each call:


def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])
