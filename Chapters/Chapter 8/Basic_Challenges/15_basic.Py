# Ask for age and check for valid (1–120 range)
age = int(input("Enter your age"))
valid_age = 1 <= age <= 120
if not valid_age:
    print("Invalid age. Age should be between 1 and 120.")
else:
    days = age * 365
    print(f"Your age in days is {days}.")

# or

while True:
    age = int(input("Enter your age: "))
    if 1 <= age <= 120:
        days = age * 365
        print(f"Your age in days is {days}.")
        break
    else:
        print("Invalid age. Please enter a value between 1 and 120.")
# There are hundreds of ways to handle this problem, so this is just example.

# Both of them are right and efficient ways to handle the problem.
# The first one is more readable and easier to understand,
# while the second one is more efficient and can handle larger inputs.
