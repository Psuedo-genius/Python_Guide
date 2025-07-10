# Use `.get()` to fetch a student’s mark safely.
mydi = {'Rahul': 98, 'Divya': 78, 'Sonam': 90, 'Jack': 78}

name = input("The name you wanna search: ").strip()

marks = mydi.get(name)

if marks is not None:
    print(f"The marks of the student {name} is {marks}")
else:
    print("Name not found!!!")
