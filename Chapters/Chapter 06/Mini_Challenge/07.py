#  Create a nested  if  to check if a user is adult and has ID.
age = int(input("Enter your age: "))
has_id = bool(int(input("Enter your ID (0 for no, 1 for yes): ")))
if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Need ID.")
else:
    print("Too young.")
