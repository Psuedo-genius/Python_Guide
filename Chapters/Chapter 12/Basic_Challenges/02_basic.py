# Add a new subject to the dictionary
# To add anything in dictionary we use this method dictionary[key] = value
marks = {'Maths': 99, 'English': 78, 'Physics': 79, 'Chemisty': 67}
sub = input("Subject you wanna add: ")
val = int(input("Marks obatined: "))
marks[sub] = val
print(marks)
