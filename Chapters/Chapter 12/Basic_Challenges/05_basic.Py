# **Delete a student entry from the dictionary.
mydi = {'Rahul': 98, 'Divya': 78, 'Sonam': 90, 'Jack': 78}
name = input("Enter student name to delete: ").strip()

if name in mydi:
    mydi.pop(name)
    print(f"{name} has been removed.")
else:
    print("Student not found!")

print(mydi)
