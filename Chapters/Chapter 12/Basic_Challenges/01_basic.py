# Create a dictionary of student marks.
mydi = {'Rahul': 98, 'Divya': 78, 'Sonam': 90, 'Jack': 78}
print(mydi)


# or this is a hard way.
mydic = {}

while True:
    k = input("Enter your name (or press Enter to stop): ").strip()
    if not k:  # Empty string or just spaces
        print("Nothing to add")
        break

    v_input = input("Enter your marks: ").strip()
    if not v_input.isdigit():
        print("Marks are required and must be a number.")
        break

    v = int(v_input)
    mydic[k] = v

print("\nStudent Marks:")
print(mydic)
