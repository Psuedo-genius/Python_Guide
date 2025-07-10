# Ask the user to guess a secret number (until correct)
secret_number = 34
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == secret_number:
        print("Congratulations! You guessed the secret number correctly.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
