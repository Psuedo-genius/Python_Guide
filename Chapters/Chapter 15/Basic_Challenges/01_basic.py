# Write a recursive function to count from `n` to `1`.
def num(n):
    if n == 0:
        print("done")
    else:
        print(n)
        num(n-1)


n = int(input("Enter the countdown start"))
num(n)
