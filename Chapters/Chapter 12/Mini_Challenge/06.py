# Fix:
# will raise a TypeError, because lists ([1,2]) are unhashable
# and cannot be used as dictionary keys in Python.
mydict = {(1, 2): "val"}
print(mydict)
