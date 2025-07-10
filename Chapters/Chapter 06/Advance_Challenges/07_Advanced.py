# Ask for username and password. If both correct → "Login successful"
user_name = input("Enter your username: ")
password = input("Enter your password: ")
if user_name == "admin" and password == "password":
    print("Login successful")
else:
    print("Invalid username or password")
