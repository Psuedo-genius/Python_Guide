# Create a triangle of numbers:
"""
1
1 2
1 2 3
"""
n = 9
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
"""
The outer loop (i) controls the number of rows.

The inner loop (j) prints numbers from 1 up to the row number.

end=' ' keeps printing on the same line with spaces.

print() without anything moves to the next line.
"""
