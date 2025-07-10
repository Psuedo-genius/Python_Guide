# What does `break` do?
# breaks out of the loop immediately,
# without executing the remaining statements in the loop.
# Example:
while True:
    print("I will be printed infinitely")
    if input("Do you want to continue? (y/n): ") == "n":
        break  # This will stop the loop once it reaches this line
