# Ask user for full name → print initials (e.g., John Doe → J.D.)
name = input("Enter your full name: ").strip()
parts = name.split()

if len(parts) >= 2:
    initials = parts[0][0].upper() + "." + parts[1][0].upper() + "."
    print("Initials:", initials)
else:
    print("Please enter at least a first and last name.")
# You will find it little hard to understand
# because we have used the strip method.
# So strip methods makes a list so you have to learn that in next chapter
# and try to learn this again after you are done with that.
# for you i have written one more code although logic is wrong
name = input("Enter your full name: ")
space = name.find(" ")
print(f"{name[0].upper()}.{name[space+1].upper()}.")
"""
Problem with this code is  If the user enters:

    Only one name like "John" → your code will break,
    because name[space+1] will throw an index error.

    Or enters more than two names, like "John Michael Doe" →
    it will only print initials for the first and middle name.
"""
