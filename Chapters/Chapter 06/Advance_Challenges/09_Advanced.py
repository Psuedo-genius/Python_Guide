# Check if a year is divisible by 4 and not 100 unless also 400
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} does not satisfy all the conditons.")
# or
if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} does not satisfy the third condition.")
    else:
        print("does not satisfy the first condition.")
else:
    print(f"{year} does not satisfy the first condition.")
"""although this works, it's not the most efficient way to check leap years.
The optimized code provided earlier is more efficient.
And its hard to read and understand."""
