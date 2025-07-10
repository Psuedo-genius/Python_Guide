# Use nested `if` to check if a user has passed and has ID
status = input("Pass or fail").lower()


if status == "pass":
    has_id = input("Do you have an ID?(yes/no)").lower()
    if has_id == "yes":
        print("Student have an id.")
    else:
        print("Needs ID.")
else:
    print("Too bad.")
