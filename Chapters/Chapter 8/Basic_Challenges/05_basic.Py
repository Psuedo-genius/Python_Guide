# Keep taking input until the user types "exit"
while True:
    word = input("Enter a word (or 'exit' to quit): ").lower()
    if word == "exit":
        print("Exiting...")
        break
