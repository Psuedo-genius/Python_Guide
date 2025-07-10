# Take input and check if it's numeric (`.isdigit()`)
while True:
    user_input = input('Enter your sentence: ')

    if user_input.isdigit():
        print("It's numeric")
        break
    else:
        print("It contains alphabets or symbols")
