# Make a short bio-generator:
# Ask name, age, city, and interest → print a paragraph using an f-string
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
interest = input("Enter your interest: ")

bio = f"My name is {name}, I am {age} years old. \n I live in {city} and I'm really interested in {interest}."
print(bio)
# Output: My name is John Doe, I am 30 years old.
# I live in New York City and I'm really interested in photography.
