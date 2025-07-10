# Build a one-liner function using `lambda` that checks if a number is even.
num = int(input("Enter a number: "))
is_even = lambda num: num % 2 == 0

if is_even(num):  # Call the lambda function with input
    print("Is even")
else:
    print("Is odd")
