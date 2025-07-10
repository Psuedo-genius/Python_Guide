# Is this valid?

def f():
    return f()


"""
Yes, it’s syntactically valid — Python will accept it without errors when
defining the function.
But it’s logically broken — because calling f()
will lead to infinite recursion.
"""
