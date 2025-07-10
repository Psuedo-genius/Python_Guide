# Ask for age. If < 13 → "Child", if 13–19 → "Teen", else → "Adult"
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen \n time for romance??")
else:
    print("Adult \n Start working man")
