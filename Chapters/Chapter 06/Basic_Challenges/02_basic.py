# Check if someone is eligible to vote (18+)
age = int(input("Enter your age: "))
if age >= 18:
    print(f"You are {age} years old eligible to vote.")
elif age < 0:
    print("Invalid age. Age must be a positive integer.")
else:
    print(f"You are {age} years old not eligible to vote.")
