# If number > 50 and even → "Perfect!"
number = int(input("Enter a number: "))
if number > 50 and number % 2 == 0:
    print("Perfect!")
else:
    print("Not perfect.")
