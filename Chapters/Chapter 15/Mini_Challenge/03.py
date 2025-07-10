# 1. Predict the output:
def test(n):
    if n == 0:
        return
    print(n)
    test(n - 1)


n = int(input("Enter the numbers: "))
print(test(n))
# If n = 23
# Output: 23, 22, 21, ..., 3, 2, 1, none
