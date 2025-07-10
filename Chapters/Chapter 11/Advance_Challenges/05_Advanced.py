# Create a dictionary where keys are tuples of (first_name, last_name)
# and values are ages. Write code to look up the age of a person.
# Step 1: Create the dictionary with tuple keys
people = {
    ("John", "Doe"): 28,
    ("Jane", "Smith"): 34,
    ("Ali", "Khan"): 41
}

# Step 2: Define the person to look up
name_to_find = ("Jane", "Smith")

# Step 3: Perform the lookup
if name_to_find in people:
    print("Age:", people[name_to_find])
else:
    print("Person not found.")
