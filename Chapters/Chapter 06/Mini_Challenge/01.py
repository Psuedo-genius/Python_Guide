# What does  elif  stand for?
# Answer: Else if — checks another condition
# Example
age = int(input("Enter your age: "))
if (age > 18):
    print("You are above 18")
elif (age < 0):
    print("invalid input")
else:
    print("You are below 18")
