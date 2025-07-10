# Print the Fibonacci sequence (first 10 terms using loop logic)
a = 0
b = 1
for i in range(10):
    print(a, end="")
    c = a + b
    a = b
    b = c

"""
| i (loop count) | a (printed) | b   | c = a + b |
| -------------- | ----------- | --- | --------- |
| 0              | 0           | 1   | 1         |
| 1              | 1           | 1   | 2         |
| 2              | 1           | 2   | 3         |
| 3              | 2           | 3   | 5         |
| 4              | 3           | 5   | 8         |
| 5              | 5           | 8   | 13        |
| ...            | ...         | ... | ...       |


"We start with 0 and 1. Then we add them to get the next number.
We always look at the last two numbers to make the next one. It's like:
0, 1 → 0+1=1
1, 1 → 1+1=2
1, 2 → 1+2=3...
and so on."
"""
