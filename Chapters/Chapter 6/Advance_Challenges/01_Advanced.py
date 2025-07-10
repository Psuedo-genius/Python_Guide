# Ask for name and age. If age ≥ 18 and name isn’t empty → "Access granted"
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18 and name != "":
    print("Access granted")
else:
    print("Access denied")
