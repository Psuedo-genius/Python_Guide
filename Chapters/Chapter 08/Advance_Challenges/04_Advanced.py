# Number guess game with hints: "too high" / "too low"
while True:
    num = int(input("Guess the number"))
    if num == 6:
        print("Correct Guess")
        break
    elif num < 6:
        print("Too low")
    elif num > 6:
        print("Too high")
