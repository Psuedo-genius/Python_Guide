# Count and print digits of a number
num = int(input("Enter a number"))
count = 0
while num > 0:
    digit = num % 10
    print(digit)
    count += 1
    num //= 10
print("Number of digits:", count)

"""
| Step | `num` | `num % 10` | Printed Digit | New `num` (`num // 10`) |
| ---- | ----- | ---------- | ------------- | ----------------------- |
| 1    | 416   | 6          | 6             | 41                      |
| 2    | 41    | 1          | 1             | 4                       |
| 3    | 4     | 4          | 4             | 0 → loop ends           |

"""
