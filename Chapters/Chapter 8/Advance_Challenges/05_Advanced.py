# Track highest number entered before quitting
highest = None  # Start with no number

while True:
    num = int(input("Enter a number: "))

    # Track the highest number
    if highest is None or num > highest:
        highest = num

    # Ask user if they want to continue
    command = input("Wanna continue? (yes = 1, no = 0): ")

    if command == "0":
        print(f"Highest value is: {highest}")
        break
