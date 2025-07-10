# Ask for a color. If it's "red", "blue", or "green" → valid color
color = input("Enter a color in capital letter: ")
if color == "RED" or color == "BLUE" or color == "GREEN":
    print("Valid color!")
else:
    print("Invalid color!")
