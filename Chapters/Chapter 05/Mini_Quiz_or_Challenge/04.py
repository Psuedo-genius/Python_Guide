# Fix the bug: if x = 5:
"""What this question is asking is,
what will be the output of the following code?"""
# if (x = 5):
#    print(f'The value of x is {x}.')
"""output : syntaxError: invalid syntax.
Maybe you meant '==' or ':=' instead of '='?"""
# Thats the difference between '=' and '==' in Python.
# correct way
x = 5
'''Note: if you dont assign a value to x,
it will be None by default and it will throw a NameError.'''
x == 5
print(f'The value of x is: {x}.')
