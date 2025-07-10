# How would you skip even numbers in a loop from 1 to 10?
x = 1
while x <= 10:
    if x % 2 == 0:
        x += 1
        continue
    print(x)
    x += 1
