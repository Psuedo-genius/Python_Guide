# Use `pass` in a dummy condition
status = input("Pass or fail").lower()


if status == "pass":
    has_id = input("Do you have an ID?(yes/no)").lower()
    if has_id == "yes":
        pass
    else:
        print("Needs ID.")
else:
    print("Too bad.")
