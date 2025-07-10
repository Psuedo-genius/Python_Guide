correct_password = input("Select a password:  ")
attempts = 0

while attempts < 3:
    entry = input("Enter password: ")
    if entry == correct_password:
        print("Access granted")
        break
    else:
        print("Wrong password ")
        attempts += 1
else:
    print("Account locked")
