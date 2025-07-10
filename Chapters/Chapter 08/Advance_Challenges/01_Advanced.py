# Login system: 3 tries max, then lockout
login_attempts = 0
locked_out = False

while login_attempts < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "password":
        print("Login successful!")
        break
    login_attempts += 1
    if login_attempts == 3:
        locked_out = True
        print("Too many login attempts. Account locked.")
