# When does `else` run in a `while` loop?
# `else` runs only if the loop finishes without `break`
x = 4
while x < 10:
    print(x)
    x += 1
else:
    print("Loop completed!")
