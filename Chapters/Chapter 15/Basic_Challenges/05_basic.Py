# Write a recursive power function: `power(x, n)`.x^n= x*x^(n−1)
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


print(power(2, 3))  # ➝ 8 (2 × 2 × 2)
print(power(5, 0))  # ➝ 1
print(power(3, 2))  # ➝ 9 (3 × 3)
