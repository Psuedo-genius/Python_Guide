# Ask for a password, validate: at least 8 chars, 1 digit, 1 uppercase
while True:
    password = input("Create a password: ")

    # Check 1: Length
    if len(password) < 8:
        print("Password should be at least 8 characters.")
        continue

    # Check 2: At least 1 digit
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        print("Password must contain at least one digit.")
        continue

    # Check 3: At least 1 uppercase letter
    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
        continue

    # All checks passed
    print("Password is valid!")
    break
