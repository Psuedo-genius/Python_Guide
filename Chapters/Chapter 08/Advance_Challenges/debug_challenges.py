# Example 1
x = 10
while x > 0:
    print(x)
    x -= 1
# What’s missing?
# Answer: The missing code is the decrement operation `x -= 1` to decrement
# The value of `x` by 1 after each iteration.
# Its will run in infinite loop without this operation.

# Example 2
x = 0
while x < 5:
    print(x)
    x += 1
    continue
# so first of all continue statement was at wrong place.
# And statement x += 1 was missing.
# first it will have skip everthing after fixing that
# it would have an infinite loop.

# Example 3
i = 0
while i < 5:
    if i == 3:
        break
    i += 1
else:
    print("Done")
# Because the loop condition will met (i == 3),
# The break statement will stop the loop.
