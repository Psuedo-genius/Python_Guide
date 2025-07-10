# Ask the user for a number. Keep looping until it’s positive
while True:
    num = int(input("Enter a integer: "))
    if num > 0:
        break
    else:
        print("Invalid input. Please enter a positive integer.")
