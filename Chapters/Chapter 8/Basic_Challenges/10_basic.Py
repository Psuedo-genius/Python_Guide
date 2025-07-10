# Validate password (loop until correct)
password = ""
while password != "password":
    password = input("Enter a password: ")
    print("Incorrect password. Please try again.")
# Print success message
print("Password is correct!")
# or
password = "password"
while True:
    user_input = input("Enter a password: ")
    if user_input == password:
        print("Password is correct!")
        break
